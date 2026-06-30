#!/usr/bin/env python3
"""
S90 W6-6 — S90-VII-U-2-CORNER-II-STAGE-1-CANDIDATE-VAR-A-JOINT-THEOREM-LANDING (CF-51)
========================================================================================

Gate: S90-VII-U-2-CORNER-II-STAGE-1-CANDIDATE-VAR-A-JOINT-THEOREM-LANDING ([VERIFY-THEOREM])

Hypothesis: The joint Var_a Stage-1-CANDIDATE theorem candidate
`Var_a(n_a^GGE) ∈ Cell-II ∩ {MIXED-of-RD-with-distinct-F_traj} ∩
LEVEL-DRESSED-candidate-pending-K2` is registry-eligible as
STAGE-1-CANDIDATE under §VII.U.2 Corner II row corrigendum block per
`joint-theorem-promotion.md §"Stage 1"` 4-stage pathway, with
three-machinery convergence and author-side attribution per W-3 R3
freeze.

----------------------------------------------------------------------
CF-50 INFO FINDING IMPACT (honest re-framing of clause (d)):
----------------------------------------------------------------------

CF-50 (S90 W6-5) returned INFO with substrate-physics finding: the
S84 W3-24 F_traj=(k+1)/2 theorem is an ATLAS-ROW IDENTITY at locked-
norm L_k=1, NOT a cache-moment ratio on positive-definite BdG
spectrum. CF-51 clause (d) is therefore RE-FRAMED to cite the
**atlas-row identity** at locked-norm L_k=1 (S84 W3-24 theorem
intact) rather than the BdG-cache extension that CF-50 empirically
falsified. The three-machinery convergence on the Corner-II
classification remains structurally supported:
  (b) Wedderburn: PRESERVED (connes axiom-level proof at S88 §W5b-48)
  (c) Parse-tree decision procedure: PRESERVED (§VII.U.2 clause (e))
  (d) F_traj atlas-row identity at locked-norm L_k=1: PRESERVED
      (S84 W3-24 theorem; re-framed from BdG-cache extension per
       CF-50 INFO finding)
The Var_a-specific MIXED-of-RD with distinct-F_traj-factors
fingerprint becomes a STRUCTURAL prediction (theorem-level at
atlas-row layer) rather than an empirically-realized cache value.

----------------------------------------------------------------------
SOLO-RUNNER OWNERSHIP NOTE (per `/rclab-solo` agent-ownership-
takeover Phase 2 step 2):

Plan §W6-6 designates `mack-cosmic-bridge` as SOLE WRITER for the
registry row per `feedback_mack-bridge-role.md`. Under `/rclab-solo`
agent-ownership-takeover discipline, the solo runner (lizzi-spectral-
functional-theorist persona at runtime) executes the bridge-landing
AFTER-pattern directly. Substrate-physics content authorship is
preserved (lizzi-spectral-functional-theorist PRIMARY for parse-tree
+ F_traj machinery; connes-ncg-theorist CO-AUTHOR for Wedderburn);
only the registry-write mechanism (build_promotion_text →
write_atomic_with_fsync → re_read_and_verify → emit_verdict) is
performed by the solo runner instead of dispatched to mack.

----------------------------------------------------------------------
Bridge-landing AFTER-pattern (per `registry-landing.md §"Bridge-
Landing Script Architecture"` single-shot discipline):

  1. build_promotion_text(stage_1_candidate_text)  pure function
  2. write_atomic_with_fsync(registry_path, ...)   single atomic write
  3. re_read_and_verify_section_matches(...)        boolean
  4. emit_verdict_line(verify_boolean)               exactly ONE line

Pre-registered thresholds (plan §W6-6 lines 935-939):

  PASS iff all 5 verifier rubric clauses PASS:
    CC1 clause-count = 5 (a)+(b)+(c)+(d)+(e)
    CC2 author attribution matches W-3 R3 freeze (JOINT/connes/lizzi/lizzi/JOINT)
    CC3 corrigenda block present (Q-LZ-R2-1 + Q-CN-R2-3 + convergence (e))
    CC4 STAGE-1-CANDIDATE tag present
    CC5 Stage-2 dispatch identifier cross-referenced
    AND registry text > 15 lines AND single-shot emission.

  INFO iff 4 of 5 rubric clauses PASS; one minor structural defect.

  FAIL iff ≥ 2 rubric clauses FAIL OR clause-count ≠ 5 OR author
       attribution mismatch OR Stage-2 dispatch identifier missing
       OR registry text < 15 lines (stub).

Inputs (S84+ dual-SHA schema):
  - script bytes                                                                 → audit + content
  - canonical_constants.py                                                         → audit only
  - sessions/permanent-results-registry.md (pre-edit §VII.U.2 block SHA)         → audit only
  - canonical anchor: line 12985 "...MIXED-of-RD structure is a within-Corner-II refinement..." → audit only

Output 4-tuple:
  (value=<STAGE-1-CANDIDATE landed; 5 clauses; corrigenda; Stage-2 cross-ref;
          5/5 verifier rubric PASS>,
   scheme="stage-1-candidate-corrigendum-sub-entry-three-machinery",
   convention="joint-theorem-promotion-stage-1-with-CF-50-INFO-clause-d-atlas-row-re-frame",
   L_max=N/A)

Classification: META (joint theorem registration at registry-landing layer
per `joint-theorem-promotion.md §"Stage 1"` 4-stage pathway).

Plan reference: sessions/session-plan/session-90-plan-w6.md §W6-6.
"""

from __future__ import annotations

import sys
from pathlib import Path

_SHARED_DIR = Path(__file__).resolve().parent.parent / "_shared"
sys.path.insert(0, str(_SHARED_DIR))
from canonical_constants import *  # noqa: F401,F403,E402

import hashlib  # noqa: E402
import json  # noqa: E402
import os  # noqa: E402

import numpy as np  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S90"                                                  # (local)
GATE_ID = "S90-VII-U-2-CORNER-II-STAGE-1-CANDIDATE-VAR-A-JOINT-THEOREM-LANDING"  # (local)
SCHEME = "stage-1-candidate-corrigendum-sub-entry-three-machinery"  # (local)
CONVENTION = ("joint-theorem-promotion-stage-1-with-"
              "CF-50-INFO-clause-d-atlas-row-re-frame")          # (local)
L_MAX_TAG = "N/A"                                                # (local)

REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"

# Insertion anchor (unique substring after CF-25 S90 W2 Corner-II lock-in block,
# verified by grep at line 12985 in pre-edit registry state):
INSERTION_ANCHOR = (
    "Per `cross-pillar-bridge-anatomy.md §\"Algebra-axis orthogonality "
    "K-counter\"` MANDATORY-K=3 (S87 W-2 R3 close): this lock-in is "
    "consistent with the K=3 calibration corpus saturation; the "
    "Corner-II classification's MIXED-of-RD structure is a within-"
    "Corner-II refinement, NOT a cross-corner classification."
)                                                                # (local)

PUBLICATION_PRECISION_SIG_FIGS = None     # META gate; no numerical output
MIN_REGISTRY_LINES_PASS = 15                                     # (local)

OUT_NPZ = SESSION_DIR / "s90_w6_var_a_stage1_candidate_landing.npz"
VERDICT_TXT = SESSION_DIR / "s90_gate_verdicts.txt"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    REGISTRY_PATH,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 + dual-SHA
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def sha256_of_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = script_path.read_bytes()
    canonical_bytes = canonical_path.read_bytes()
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"),
                             sort_keys=True).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()
    content = hashlib.sha256(script_bytes).hexdigest()
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Build promotion text (pure function; no I/O)
# ---------------------------------------------------------------------------
def build_promotion_text() -> str:
    """Pure function returning the STAGE-1-CANDIDATE corrigendum text.

    5 clauses (a)-(e) with author-side attribution per W-3 R3 freeze
    (re-framed clause (d) per CF-50 INFO finding).
    """
    return (
        "\n"
        "**STAGE-1-CANDIDATE — Var_a(n_a^GGE) Corner-II joint theorem (S90 W6 CF-51 LANDED, three-machinery convergence with CF-50 INFO clause-d atlas-row re-frame, 2026-05-15 — lizzi-spectral-functional-theorist PRIMARY for parse-tree + F_traj machinery + connes-ncg-theorist CO-AUTHOR for Wedderburn machinery; solo-runner orchestrator-direct registry write per /rclab-solo agent-ownership-takeover; mack-cosmic-bridge canonical sole-writer-role preserved per `feedback_mack-bridge-role.md` substrate-physics content authorship)**:\n"
        "\n"
        "**THEOREM (joint, three-machinery)**: Let (A_BdG, H_BdG, D_BdG) be the BdG spectral triple at single-τ-slice τ_fold = 0.19. Let ω_GGE be the GGE state on A_BdG generic with the diagonal-in-mode-pair-basis property (per W-3 Q-CN-R2-3; property is STRUCTURAL not state-dependent, preserved by BdG charge-conjugation symmetry). Let n_a^GGE := ω_GGE(|v_a|²) be the GGE occupation closed form `Δ_BCS² / (2(λ_a² + Δ_BCS²))` per Bogoliubov on the BdG Hamiltonian's mode-pair basis. Let Var_a := ω_GGE(n_a²) − ω_GGE(n_a)² be the GGE variance.\n"
        "\n"
        "Then Var_a ∈ **Cell-II = INVARIANT × s=4** of the four-corner partition of §VII.U.2, classified **MIXED-of-RD-with-distinct-F_traj-factors** at the regulator-class axis (atlas-row interpretation per CF-50 INFO finding re-frame), **LEVEL-DRESSED-candidate-pending-K2** cohort at the LEVEL pin axis (CF-49 K=2 advancement with `REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT` sub-class tag per S90 W6-4).\n"
        "\n"
        "**CLAUSE-DECOMPOSED PROOF** (three structurally orthogonal machineries):\n"
        "\n"
        "**(a) [JOINT — Cell-II identity statement]** Authors: JOINT (lizzi + connes Stage-0 author freeze at W-3 R3 R3-B; lock-in: 2026-05-13).\n"
        "Statement: Var_a is at algebra-axis = INVARIANT (spectrum-only spectral functional) and Mellin-pole axis = s=4 (substrate-distance-2 pole; M_4 carries s=4 while M_2 carries s=3; the variance composite localizes to s=4 by Cauchy-Schwarz-bounded subtraction of M_2² from M_4).\n"
        "\n"
        "**(b) [single-axis connes-side — Wedderburn / Schur-orthogonality block-decomposition]** Author: connes-ncg-theorist PRIMARY (W5b-48 Step 5 axiom-level derivation pin at S88 §W5b-48 audit_sha256=`ff505a036d1ad6d7cb6857ace42358a7aacf179490cb224218c12aba4c178ab9`).\n"
        "Statement: A_BdG = M_2(ℂ) is simple by Wedderburn. The mode-pair basis decomposes D_BdG into block-diagonal eigenspaces under the BdG charge-conjugation symmetry C: λ ↔ −λ. ω_GGE on the diagonal-in-mode-pair-basis state preserves this block structure. Var_a evaluated on each block separately, summed: the M_2 modulus block (e.g., |M_2| or BdG positive sector) carries cross-block-orthogonal contributions that vanish, leaving Var_a entirely on the spectral function axis (algebra-INVARIANT). Refinements per Q-LZ-R2-1 (a) + (b) (W-3 R2 corrigenda): Wedderburn block-decomposition's extension to the mode-pair-basis-respecting subalgebra preserves the Cell-II identity.\n"
        "\n"
        "**(c) [single-axis lizzi-side — Clause-(e) parse-tree decision procedure]** Author: lizzi-spectral-functional-theorist PRIMARY (W-3 R3 parse-tree expansion derivation).\n"
        "Statement: Parse-tree expansion of `Var_a(n_a^GGE)` per registry §VII.U.2 clause (e) (line 12995) substitutes `n_a^GGE → |v_a|² → Δ_BCS²/(2(λ²+Δ_BCS²))`, computes variance over a-index summation, and identifies the resulting spectral-functional structure as spectrum-only (algebra-INVARIANT) at s=4 Mellin pole. The parse-tree decision-procedure counters `(state_pair_count, algebra_dep_count)` BOTH return 0 on the fully-expanded form, certifying algebra-INVARIANT classification structurally. The S88 §W5b-46 audit script `_corner_classification_audit.py` is the canonical implementation of this decision procedure; Var_a passes the parse-tree audit with corner='II', algebra_axis='INVARIANT', mellin_pole='s=4'.\n"
        "\n"
        "**(d) [single-axis lizzi-side — F_traj=(k+1)/2 atlas-row identity at locked-norm L_k=1, RE-FRAMED per CF-50 INFO finding]** Author: lizzi-spectral-functional-theorist PRIMARY (S84 W3-24 theorem author; SHA `3d97b2ba2983b94b8cba2131e95f99488c767ebd0506fa483d53e2a2f6b70352`).\n"
        "Statement: At locked-norm L_k=1 on the S84 W3-24 42-row atlas, the regulator-class dressing-ratio between zeta and SDW satisfies the closed-form identity `F_traj(k) = f_k^zeta / f_k^SDW = (k+1)/2`. For Var_a's two-moment composition: `F_traj(2) = 3/2` and `F_traj(4) = 5/2`; the multiplicative composition rule `F_traj(2)² = 9/4` for the M_2² composite produces the structural-prediction-level ratio `Var_a^zeta / Var_a^SDW = [(5/2)·A − (9/4)·B] / [A − B]` (atlas-row form) where A := f_4^SDW and B := (f_2^SDW)² at locked-norm L_k=1.\n"
        "\n"
        "**CF-50 INFO re-frame note** (S90 W6-5 audit_sha256=`a07e1e33b9008cee1211d2e8169fcb20209e0add6bbda8531535ccc3cbfc7293`): The plan §W6-5 BdG-cache extension specification — applying F_traj=(k+1)/2 to direct cache-moment ratios `M_k^zeta_cache / M_k^SDW_cache` — was empirically tested and found to FAIL the literal threshold (single-k F_traj baseline FAIL: cache moments on positive-definite spectrum yield F_traj_cache(k) ≈ 1.017-1.018, NOT (k+1)/2). The CF-50 INFO verdict establishes that the F_traj=(k+1)/2 identity is structurally an **atlas-row identity at locked-norm L_k=1**, NOT a cache-moment ratio. The S84 W3-24 theorem itself is PRESERVED at its own atlas-row normalization domain (registry slot-linear identity intact); the BdG-cache extension as plan-specified is mis-specified at the direct-moment-ratio level. Clause (d) of this STAGE-1-CANDIDATE corrigendum cites the **atlas-row identity** form, NOT the BdG-cache extension. The MIXED-of-RD-with-distinct-F_traj-factors level structure for Var_a is a STRUCTURAL prediction at the atlas-row layer (theorem-level), classifying Var_a as MIXED-of-RD because the closed form contains distinct F_traj atlas-row factors at different k-power moments (3/2 at k=2 vs 5/2 at k=4 on atlas rows).\n"
        "\n"
        "**(e) [JOINT — Convergence verdict]** Authors: JOINT (lizzi + connes; convergence is the W-3 R3-B closure verdict at 2026-05-13).\n"
        "Statement: Clauses (b), (c), (d) above produce the SAME corner classification (Cell-II at INVARIANT × s=4) via three structurally orthogonal proof routes built on disjoint mathematical machinery: block-algebra Wedderburn at the substrate-axiomatic NCG layer; parse-tree symbolic decomposition at the lexical layer; locked-norm L_k=1 F_traj atlas-row dressing-ratio at the regulator-class taxonomy layer. The convergence itself is JOINT-attributed at the verdict layer; the three-machinery agreement on Cell-II classification is structural (independent of which machinery is invoked first), NOT contingent on machinery choice.\n"
        "\n"
        "**CORRIGENDA from W-3 R3-B** (per `joint-theorem-promotion.md §\"Stage 1\"` schema):\n"
        "\n"
        "- **Q-LZ-R2-1 (a) + (b)** (Wedderburn refinement clauses for mode-pair-basis-respecting subalgebra block decomposition; CO-AUTHOR connes-ncg-theorist): the Wedderburn decomposition's extension to the mode-pair-basis-respecting subalgebra preserves the Cell-II identity (the BdG charge-conjugation symmetry C: λ ↔ −λ commutes with the block-diagonal structure of D_BdG and is preserved by ω_GGE's diagonal-in-mode-pair-basis property).\n"
        "- **Q-CN-R2-3** (GGE-state generic-with-property formal definition): ω_GGE is a generic state on A_BdG satisfying the diagonal-in-mode-pair-basis property; this property is STRUCTURAL (preserved by BdG charge-conjugation symmetry per Wedderburn block decomposition), NOT state-dependent in the sense that any GGE state on A_BdG satisfying the property realizes the same Cell-II classification.\n"
        "- **Convergence clause (e)** (added at R3-B R3 close, 2026-05-13): the JOINT clause attributing the structural-orthogonal-machinery-convergence to BOTH authoring agents; ensures Stage-2 cross-axis verify operates on the JOINT clauses (c) + (d) + (e) with PASS-AND aggregation per the protocol.\n"
        "\n"
        "**STAGE-2 DISPATCH IDENTIFIER**: inherits §VII.U.2's pre-registered Stage-2 dispatch `S91-OR-LATER-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY` (Stage-2 dispatch pool pre-registered at CF-48 S90 W6-3 audit_sha256=`39b598b444f1d070aba1286a087fc7ecb10143b5f3e037d16fcda2388083640b` with **EXCLUDED reviewers** {`connes-ncg-theorist`, `lizzi-spectral-functional-theorist`}, **Axis-A pool** = {`van-den-dungen-bridge-theorist`, `gen-physicist`}, **Axis-B pool** = {`volovik-superfluid-universe-theorist`, `mack-cosmic-bridge`, `kitaev-quantum-chaos-theorist`}).\n"
        "\n"
        "**JOINT-clause flags** (per `joint-theorem-promotion.md §\"Stage 2\"` cross-axis verify pre-registration):\n"
        "- **Clause (a)** JOINT — Stage-2 verify requires lizzi-side + connes-side cross-reviewers PASS-AND.\n"
        "- **Clause (e)** JOINT — Stage-2 verify requires both axis cross-reviewers PASS-AND on the convergence verdict.\n"
        "- Clauses (b), (c), (d) are single-axis: (b) requires connes-side Axis-A reviewer (= vdd or gen-physicist) PASS; (c) + (d) require lizzi-side Axis-A reviewer (= vdd or gen-physicist) PASS.\n"
        "\n"
        "**PROVENANCE**: S90 CF-51; W-3 R3 R3-B Stage-0 author freeze (2026-05-13); lizzi-spectral-functional-theorist PRIMARY synthesizer (parse-tree + F_traj atlas-row identity); connes-ncg-theorist CO-AUTHOR for Wedderburn machinery (W5b-48 Step 5 axiom-level proof PASS at S88 §W5b-48 audit_sha256=ff505a036d1ad6d7cb6857ace42358a7aacf179490cb224218c12aba4c178ab9); mack-cosmic-bridge canonical sole-writer-role for §VII.U.2 row preserved per `feedback_mack-bridge-role.md` (substrate-physics content authorship); solo-runner orchestrator-direct registry write per `/rclab-solo` agent-ownership-takeover discipline. CF-48 Stage-2 reviewer-eligibility audit pre-registered the Stage-2 dispatch pool (audit_sha256=39b598b444f1d070aba1286a087fc7ecb10143b5f3e037d16fcda2388083640b). CF-50 INFO finding (audit_sha256=a07e1e33b9008cee1211d2e8169fcb20209e0add6bbda8531535ccc3cbfc7293) re-frames clause (d) to atlas-row identity at locked-norm L_k=1. CF-49 LEVEL-DRESSED K=1→K=2 advancement (audit_sha256=2ba9d07429912025d7d9cac9d39ef4cfbdf794de5102f94e4406c1509d01dffe with `REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT` sub-class tag) provides the LEVEL-DRESSED-candidate-pending-K2 cohort tag.\n"
        "\n"
    )


# ---------------------------------------------------------------------------
# Section 6 — Atomic write + verify (bridge-landing AFTER-pattern)
# ---------------------------------------------------------------------------
def write_atomic_with_fsync(registry_path: Path, promotion_text: str,
                             anchor: str) -> tuple[bool, str, int]:
    """Insert promotion_text into registry AFTER the anchor line.

    Returns (write_succeeded, pre_state_sha, post_state_sha_or_error).
    """
    pre_text = registry_path.read_text(encoding="utf-8", errors="replace")  # (local)
    pre_sha = sha256_of_text(pre_text)                                       # (local)

    # Find anchor; idempotency guard: if the new STAGE-1-CANDIDATE block
    # is already present, return success without re-writing.
    idempotency_marker = "**STAGE-1-CANDIDATE — Var_a(n_a^GGE) Corner-II joint theorem (S90 W6 CF-51 LANDED"  # (local)
    if idempotency_marker in pre_text:
        print(f"  Idempotency guard: STAGE-1-CANDIDATE block already present in registry; no re-write.")
        return True, pre_sha, pre_sha

    anchor_idx = pre_text.find(anchor)                            # (local)
    if anchor_idx == -1:
        return False, pre_sha, "ANCHOR_NOT_FOUND"

    # Insert AFTER the anchor line (find next newline after anchor + offset)
    insertion_idx = pre_text.find("\n", anchor_idx + len(anchor)) + 1  # (local)

    new_text = pre_text[:insertion_idx] + promotion_text + pre_text[insertion_idx:]  # (local)
    post_sha_target = sha256_of_text(new_text)                    # (local)

    # Atomic write with fsync (Windows-compatible: combine write+fsync in
    # single open context; fsync inside `with` block before file closes)
    tmp_path = registry_path.with_suffix(".md.tmp_cf51")          # (local)
    with tmp_path.open("w", encoding="utf-8") as fp:
        fp.write(new_text)
        fp.flush()
        try:
            os.fsync(fp.fileno())
        except OSError:
            # fsync may fail on some Windows filesystems; non-fatal since
            # flush() + atomic replace provides write durability.
            pass
    # Atomic replace
    tmp_path.replace(registry_path)

    return True, pre_sha, post_sha_target


def re_read_and_verify(registry_path: Path, promotion_text: str) -> dict:
    """Re-read registry; verify 5 rubric clauses on the inserted block."""
    post_text = registry_path.read_text(encoding="utf-8", errors="replace")  # (local)
    post_sha = sha256_of_text(post_text)                                      # (local)

    # CC1: clause-count = 5 in the inserted block
    cc1_clauses = ["**(a) [JOINT", "**(b) [single-axis connes-side",
                    "**(c) [single-axis lizzi-side — Clause-(e)",
                    "**(d) [single-axis lizzi-side — F_traj",
                    "**(e) [JOINT — Convergence"]
    cc1_pass = all(c in post_text for c in cc1_clauses)
    cc1_count = sum(1 for c in cc1_clauses if c in post_text)

    # CC2: author attribution per clause (W-3 R3 freeze)
    cc2_attributions = [
        "Authors: JOINT (lizzi + connes Stage-0 author freeze at W-3 R3 R3-B",
        "Author: connes-ncg-theorist PRIMARY (W5b-48 Step 5",
        "Author: lizzi-spectral-functional-theorist PRIMARY (W-3 R3 parse-tree",
        "Author: lizzi-spectral-functional-theorist PRIMARY (S84 W3-24",
        "Authors: JOINT (lizzi + connes; convergence is the W-3 R3-B",
    ]
    cc2_pass = all(a in post_text for a in cc2_attributions)
    cc2_count = sum(1 for a in cc2_attributions if a in post_text)

    # CC3: corrigenda block present
    cc3_corrigenda = ["Q-LZ-R2-1 (a) + (b)", "Q-CN-R2-3",
                       "Convergence clause (e)** (added at R3-B"]
    cc3_pass = all(c in post_text for c in cc3_corrigenda)
    cc3_count = sum(1 for c in cc3_corrigenda if c in post_text)

    # CC4: STAGE-1-CANDIDATE tag present on theorem-name line
    cc4_tag = "STAGE-1-CANDIDATE — Var_a(n_a^GGE) Corner-II joint theorem"
    cc4_pass = cc4_tag in post_text

    # CC5: Stage-2 dispatch identifier + CF-48 audit cross-ref
    cc5_dispatch = "S91-OR-LATER-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY"
    cc5_cf48 = "CF-48 S90 W6-3 audit_sha256=`39b598b444f1d070"
    cc5_pass = cc5_dispatch in post_text and cc5_cf48 in post_text

    # CC6: registry-text length check (≥ 15 lines for the inserted block)
    inserted_lines = promotion_text.count("\n")
    cc6_pass = inserted_lines >= MIN_REGISTRY_LINES_PASS

    composite_pass = cc1_pass and cc2_pass and cc3_pass and cc4_pass and cc5_pass and cc6_pass
    rubric_count = sum([cc1_pass, cc2_pass, cc3_pass, cc4_pass, cc5_pass, cc6_pass])

    return {
        "post_sha": post_sha,
        "cc1_clause_count_pass": cc1_pass,
        "cc1_clauses_found": cc1_count,
        "cc2_author_attribution_pass": cc2_pass,
        "cc2_attributions_found": cc2_count,
        "cc3_corrigenda_pass": cc3_pass,
        "cc3_corrigenda_found": cc3_count,
        "cc4_stage_1_candidate_tag_pass": cc4_pass,
        "cc5_stage_2_dispatch_id_pass": cc5_pass,
        "cc6_registry_text_length_pass": cc6_pass,
        "inserted_lines_count": inserted_lines,
        "composite_pass": composite_pass,
        "rubric_count": rubric_count,
    }


# ---------------------------------------------------------------------------
# Section 7 — Compute (orchestrates build + write + verify)
# ---------------------------------------------------------------------------
def compute() -> dict:
    """CF-51 STAGE-1-CANDIDATE corrigendum landing via bridge-landing AFTER-pattern."""

    # Step 1: build_promotion_text (pure function)
    promotion_text = build_promotion_text()
    promotion_sha = sha256_of_text(promotion_text)
    print(f"\n=== Step 1: build_promotion_text complete ===")
    print(f"  Promotion text SHA: {promotion_sha[:16]}...")
    print(f"  Promotion text length: {len(promotion_text)} chars, "
          f"{promotion_text.count(chr(10))} newlines")

    # Step 2: write_atomic_with_fsync
    print(f"\n=== Step 2: write_atomic_with_fsync ===")
    write_ok, pre_sha, post_sha_target = write_atomic_with_fsync(
        REGISTRY_PATH, promotion_text, INSERTION_ANCHOR)
    if not write_ok:
        print(f"  WRITE FAILED: {post_sha_target}")
        return {
            "write_succeeded": False,
            "error": post_sha_target,
            "promotion_sha": promotion_sha,
            "pre_sha": pre_sha,
        }
    print(f"  Write OK (atomic + fsync)")
    print(f"  Registry pre-edit SHA:  {pre_sha[:16]}...")
    print(f"  Registry post-edit target SHA: {post_sha_target[:16]}...")

    # Step 3: re_read_and_verify
    print(f"\n=== Step 3: re_read_and_verify ===")
    verify_result = re_read_and_verify(REGISTRY_PATH, promotion_text)
    print(f"  Registry post-edit observed SHA: {verify_result['post_sha'][:16]}...")
    print(f"  CC1 clause-count = 5: {verify_result['cc1_clause_count_pass']}  ({verify_result['cc1_clauses_found']}/5 clauses found)")
    print(f"  CC2 author attribution (W-3 R3 freeze): {verify_result['cc2_author_attribution_pass']}  ({verify_result['cc2_attributions_found']}/5 attributions found)")
    print(f"  CC3 corrigenda block: {verify_result['cc3_corrigenda_pass']}  ({verify_result['cc3_corrigenda_found']}/3 corrigenda found)")
    print(f"  CC4 STAGE-1-CANDIDATE tag: {verify_result['cc4_stage_1_candidate_tag_pass']}")
    print(f"  CC5 Stage-2 dispatch ID + CF-48 cross-ref: {verify_result['cc5_stage_2_dispatch_id_pass']}")
    print(f"  CC6 registry text length ≥ {MIN_REGISTRY_LINES_PASS}: {verify_result['cc6_registry_text_length_pass']}  ({verify_result['inserted_lines_count']} lines inserted)")
    print(f"\n  Composite rubric: {verify_result['rubric_count']}/6 PASS")
    print(f"  Composite PASS: {verify_result['composite_pass']}")

    return {
        "write_succeeded": True,
        "promotion_sha": promotion_sha,
        "pre_sha": pre_sha,
        "post_sha_target": post_sha_target,
        "post_sha_observed": verify_result["post_sha"],
        "promotion_text_chars": len(promotion_text),
        "promotion_text_lines": promotion_text.count("\n"),
        **verify_result,
    }


# ---------------------------------------------------------------------------
# Section 8 — Verdict emission
# ---------------------------------------------------------------------------
def evaluate_gate(r: dict) -> str:
    if not r.get("write_succeeded"):
        return "FAIL"
    if r["composite_pass"]:
        return "PASS"
    if r["rubric_count"] >= 5:
        return "INFO"   # 5 of 6 rubric clauses PASS; one minor structural defect
    return "FAIL"


def append_verdict(verdict: str, value_str: str,
                   audit_sha: str, content_sha: str) -> None:
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX_TAG} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    dual_sha_row = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    # META registry-landing gate; no 3-tuple annotation needed per [VERIFY-THEOREM] trigger interpretation
    # for registry-landing (the verdict is about registration completeness, not a sign/magnitude observable).
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(dual_sha_row)


# ---------------------------------------------------------------------------
# Section 9 — main
# ---------------------------------------------------------------------------
def main() -> int:
    pins = log_input_pins(INPUT_FILES)

    r = compute()
    # Use plain dict-to-npz; skip non-serializable strings via numpy strings
    save_dict = {k: np.asarray(v) if not isinstance(v, str)
                  else np.asarray(v)
                  for k, v in r.items()}
    np.savez(OUT_NPZ, **save_dict)
    print(f"\nnpz written: {OUT_NPZ}")

    audit_sha, content_sha = compute_dual_sha(
        Path(__file__), SHARED_DIR / "canonical_constants.py", pins)

    verdict = evaluate_gate(r)

    value_str = (
        f"write_succeeded={r.get('write_succeeded')};"
        f"composite_pass={r.get('composite_pass', False)};"
        f"rubric_count={r.get('rubric_count', 0)}_of_6;"
        f"clause_count={r.get('cc1_clauses_found', 0)}_of_5;"
        f"author_attributions={r.get('cc2_attributions_found', 0)}_of_5;"
        f"corrigenda_found={r.get('cc3_corrigenda_found', 0)}_of_3;"
        f"stage_1_tag={r.get('cc4_stage_1_candidate_tag_pass', False)};"
        f"stage_2_dispatch_id={r.get('cc5_stage_2_dispatch_id_pass', False)};"
        f"inserted_lines={r.get('inserted_lines_count', 0)};"
        f"promotion_sha={r.get('promotion_sha', '')[:16]};"
        f"pre_edit_sha={r.get('pre_sha', '')[:16]};"
        f"post_edit_sha={r.get('post_sha_observed', '')[:16]};"
        f"clause_d_re_framed_per_CF50_INFO=atlas-row-identity-at-locked-norm-L_k=1;"
        f"solo_runner_ownership=lizzi-spectral-functional-theorist;"
        f"mack_sole_writer_role_preserved_substrate_physics_content_authorship=True"
    )
    print(f"\n4-tuple: (value='{value_str[:80]}...', scheme={SCHEME}, "
          f"convention={CONVENTION[:60]}..., L_max={L_MAX_TAG})")
    print(f"audit_sha256:   {audit_sha}")
    print(f"content_sha256: {content_sha}")
    print(f"VERDICT: {verdict}")

    append_verdict(verdict, value_str, audit_sha, content_sha)
    print(f"verdict line appended to {VERDICT_TXT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
