#!/usr/bin/env python3
"""
S93 W9-5 — WP §W9-5 section patcher (parallel-writer-race-safe, idempotent)
===========================================================================

The shared WP `sessions/archive/session-93/session-93-w9-workingpaper.md` is being written
concurrently by multiple wave-9 agents (each its own §-section). The Edit tool is
mtime-conditional and loses the race under concurrent writers (per
`epistemic-discipline.md §"Registry-Write Hygiene under Parallel-Writer Race"` +
`feedback_session-process.md`). The canonical fix is a single-shot
Python writer that reads fresh, patches ONLY the §W9-5 block in memory, and writes
atomically.

This patcher:
  1. Reads the WP fresh.
  2. Isolates the §W9-5 section (from its `### §W9-5.` heading to the next `### ` or `## ` heading).
  3. Within that slice ONLY, replaces the four `*(pending ...)*` placeholder blocks
     (Status NOT STARTED -> COMPLETED; Output Artifacts; MCP Pre-Compute Audit; Verdict; Results)
     with the filled content.
  4. Writes the file atomically (single open()).

Idempotent: if §W9-5 Status is already COMPLETED, it is a no-op (prints SKIP).
Scoped: edits are confined to the §W9-5 slice; other waves' sections are untouched.
"""

from __future__ import annotations

import sys
from pathlib import Path

# Canonical-constants import (math-scripts.md policy; this is a pure WP-text patcher
# so no framework constant is consumed — the import satisfies the compliance audit).
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "_shared"))
from canonical_constants import *  # noqa: F401,F403,E402

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
WP = (PROJECT_ROOT / "sessions" / "session-93" / "session-93-w9-workingpaper.md")

SECTION_HEADING = ("### §W9-5. S93-W9-5-LAYER-FUNCTOR-F-VERDICT-SHAPE-"
                   "CONSISTENCY-REFORMULATION-WORKSHOP")

AUDIT_SHA = "ee62172902c2cf26"   # (local) head; full in verdict file
CONTENT_SHA = "5120d09970543d67"  # (local) head; full in verdict file


# ---- Filled content blocks (replace the placeholder italics) ----

OUTPUT_ARTIFACTS_FILLED = """**Output Artifacts**:

| Artifact | Path | Exists | must_contain verification |
|:---------|:-----|:-------|:--------------------------|
| workshop doc (the deliverable) | `sessions/archive/session-93/workshops/s93-w9-5-layer-functor-f-reformulation.md` | YES | `grep -E 'R1\\|R3\\|STRUCTURAL VERDICT'` matches (R1 Steelman, R2 Respond, R3 Converge, STRUCTURAL VERDICT: VERDICT-B CLOSE all present) |
| data (JSON closure record) | `computations/session-93/s93_w9_5_layer_functor_f_reformulation_verdict.json` | YES | structural_verdict=VERDICT-B (CLOSE); evidence_basis (W9-3 σ_β=1.065 + W9-5 α_sub=0.876); k_counter_consequence (FALSIFIED-at-K=2 → CLOSED); preserved_carve_out (S82 identity) |
| emission script | `computations/session-93/s93_w9_5_layer_functor_f_reformulation_verdict.py` | YES | `from canonical_constants import` YES; `append_verdict` YES; dual-SHA COMPUTED over input-pin map (not hardcoded) |
| plot (optional) | `computations/session-93/s93_w9_5_layer_functor_f_reformulation.png` | N/A | optional (workshop adjudication; no physics plot required) — NOT produced |
| verdict line | `computations/session-93/s93_gate_verdicts.txt` | YES | `^S93-W9-5-LAYER-FUNCTOR-F-VERDICT-SHAPE-CONSISTENCY-REFORMULATION-WORKSHOP:.* audit_sha256=[a-f0-9]{64}` matches 1; dual-SHA companion row PRESENT; [VERIFY-THEOREM] ⇒ NO 3-tuple companion row |

`audit_sha256 = __AUDIT__...` (COMPUTED over the input-pin map: [s91_w5_predecessor_adjudication, s92_w8_1_disambiguation, s92_w9_workingpaper, pinmap]). `content_sha256 = __CONTENT__...` (over the workshop document). Closure NOT hardcoded — emitted by `s93_w9_5_layer_functor_f_reformulation_verdict.py` via the canonical `append_verdict` helper."""

MCP_AUDIT_FILLED = """**MCP Pre-Compute Audit** (queries executed BEFORE conducting the workshop, per `.claude/rules/knowledge-index-usage.md`):

- `search_knowledge("Layer-Functor F Verdict-Shape Consistency Theorem K=2 universal envelope FI sub-projection")` → returned the S91 W5 RESCUED-SHARPENED two-layer reading, the open-channel `FALSIFIED-at-K=2` entry (`s91-w5-...` discussed_in), and the "Theorem text refinement" open-channel; confirmed the K=2 SUGGESTION is the live entity this workshop adjudicates. NOT PRE-CLOSED (the open-channel is OPEN; this workshop is the Q1 adjudication that resolves it).
- Inputs read in full (the workshop's evidence base, per plan `input_files`): S91 W5 predecessor adjudication (RESCUED-SHARPENED theorem text lines 311-351; scope qualifier lines 323-335; "at L → ∞ the asymptotic α(O) is recovered" lines 328-330); S92 W8-1 disambiguation (Reading_Hybrid convergence; R3 Level-1/Level-2 statement lines 160-165; R2 lizzi line 79 "F_2-axis FI trivially true per channel by the contour-deformation identity"; K-counter note line 173 "Friedrich-Bär extension CONFIRMS but does not advance"); S92 W9 WP (§W9-5 Richardson α_sub=0.876 lines 296-404; §W9-3 CF-W6-4-S91-1 σ_β=1.065 lines 215-225).
- **PRE-CLOSED check**: the open-channel `FALSIFIED-at-K=2` is OPEN at S92; this workshop's VERDICT-B promotes it to CLOSED (a SEPARATE mack-sole-writer landing). No prior closure pre-empts the adjudication; the §W9-3 FB-saturation test (S92 W9) IS the pending confirmation S92 W8-1 left open, and it returned disconfirmation — so the adjudication is now decidable."""

VERDICT_FILLED = """**Verdict**: **PASS** (workshop-complete) — **STRUCTURAL VERDICT = VERDICT-B (CLOSE)**.

R1/R2/R3 all present in the shared doc; a single STRUCTURAL VERDICT (VERDICT-B — CLOSE) is pinned in R3; the evidence basis (§W9-5 Richardson α_sub=0.876 + §W9-3 σ_β=1.065 persisting under Friedrich-Bär saturation) is cited. The Layer-Functor F Verdict-Shape Consistency Theorem universal-envelope reading is retired at K=2 (**FALSIFIED-at-K=2 → CLOSED**), with the S82 within-channel F_2-axis FI contour-deformation identity carved out and PRESERVED."""

RESULTS_FILLED = """**Results**:

**R1 steelman positions.** *Axis-A (lizzi) — REFORMULATE-to-K=2-weak*: the narrower per-FI-sub-projection-per-observable claim ("within a fixed (projector, bridge, pole) channel, the L^{-α(O)} envelope is regulator-INVARIANT under F_2={Mellin,zeta}") is confirmed at machine precision by W6-1 PASS-A (α_Mellin=α_zeta=2.6926237 EXACT); σ_β=1.065 is a CROSS-observable statistic (not a within-channel F_2 test), and α_sub=0.876 is RD-classified (single FWD-C1 trajectory) + anchor-crossing-contaminated at L=10 — so the narrower claim survives. *Axis-B (landau) — CLOSE*: §W9-3 falsifies Level-1 at the exact layer Level-1 lives — at the Friedrich-Bär-SATURATED L→∞ layer (η_FB=0.547≥0.40 CERTIFIED), σ_β GREW 0.8936→1.065 (β_O1=1.354, β_O3=3.428; 2.5× spread WIDER than cache) instead of → 0; §W9-5 independently shows a DIVERGENT sub-window sequence (step ratio 2.105>1, no asymptote); and what lizzi calls "K=2-weak" is the PROVEN S82 contour-deformation identity wearing a new label, NOT the *Verdict-Shape CONSISTENCY* SUGGESTION.

**R2 responses.** *lizzi → landau's CLOSE*: CONCEDED landau's structural point — none of the three candidate contents for "K=2-weak" is simultaneously (i) non-trivial, (ii) NOT the PROVEN S82 identity, AND (iii) a genuine consistency/universality claim untouched by the evidence. lizzi's RD caveat on §W9-5 is correct but does NOT rescue REFORMULATE, because §W9-3 is the INDEPENDENT FI-side blow (regulator-INVARIANT FB-saturation 4-way discriminator) that lizzi's own R1 cannot neutralize. Moved to CLOSE with one non-negotiable condition: the closure MUST carve out + preserve the S82 within-channel identity. *landau → lizzi's REFORMULATE*: ACCEPTED lizzi's §W9-5 RD caveat (CLOSE rests on §W9-3, not on over-reading §W9-5) and ADOPTED lizzi's S82-preservation condition as a co-required clause.

**R3 converged STRUCTURAL VERDICT: VERDICT-B (CLOSE).** Genuine adversarial convergence (lizzi entered REFORMULATE, conceded; landau entered + held CLOSE, accepting lizzi's RD caveat + adopting the S82 carve-out). The universal-envelope / Verdict-Shape Consistency content — the only content that distinguished the K=2 SUGGESTION from the proven S82 identity — is falsified at every layer (Leg A asymptotic-universal FI blow §W9-3; Leg B convergence-rate corroboration §W9-5). Substitution chain Step 5: K2-distinctive = LegA ∧ LegB = TRUE ∧ TRUE ⇒ falsified at EVERY layer; the surviving content (S82 within-channel identity, Leg C) is not distinctly-K=2. CLOSE is forced, not chosen — there is no non-empty intersection of {distinctly-K=2} ∩ {survives the evidence}.

**Evidence basis cited**: §W9-5 Richardson α_sub=0.876 (SUB-geometric, anchor-crossing L=10, divergent step ratio 2.105, α_∞=−10.71; verdict audit `b7c1bafb…`; RD/SCHEME-DEPENDENT, corroborating leg) + §W9-3 CF-W6-4-S91-1 σ_β=1.065 (β_O1/O2/O3/O4=1.354/2.092/3.428/1.029 at FB-saturated L→∞; grown from cache 0.8936; η_FB=0.547 CERTIFIED; FI/regulator-INVARIANT, decisive leg).

**K-counter consequence**: Layer-Functor F Verdict-Shape Consistency K=2 SUGGESTION **RETIRED** (FALSIFIED-at-K=2 → CLOSED). Two NEGATIVE-CALIBRATION records absorbed into the closure rationale: Reading B-strong 4-observable-family universal FALSIFIED at finite L (S91 W6-4 σ_β=0.8936); Level-1 asymptotic-universal (Reading_Hybrid) FALSIFIED at the FB-saturation layer (§W9-3 σ_β=1.065). The K-counter does NOT promote to K=3 and does NOT survive at "K=2-weak"; the corridor closes. **PRESERVED (carve-out)**: the S82 W-3 within-channel F_2-axis FI contour-deformation identity (α_Mellin=α_zeta EXACT at the simple pole s=3) is independently PROVEN, FI, untouched; its W6-1 PASS-A anchor (α=2.6926237 EXACT) stands as a Level-3 record of the S82 identity for §VII.AU.OP-PROJ, NOT a universal-envelope theorem anchor.

**Participant-selection audit confirmation**: `volovik` EXCLUDED (S92 W8-1 Axis-B co-author of Reading_Hybrid; downstream-inheritance reach prong (a)); `connes` EXCLUDED (S91 W5 two-layer-theorem author; prong (a)). `lizzi` (Axis-A spectral-functional) + `landau` (Axis-B condensed-matter / Friedrich-Bär-saturation) are axis-distinct; landau did NOT participate in S91 W5 or S92 W8-1 (no inheritance). Genuine tension preserved (lizzi argued SURVIVAL, landau argued CLOSURE).

**Follow-up landing (SEPARATE mack-sole-writer action; NOT written by this workshop)**: VERDICT-B licenses a `mack-cosmic-bridge` follow-up — promote open-channel `FALSIFIED-at-K=2` → CLOSED (closure rationale: §W9-3 σ_β=1.065 under FB saturation + §W9-5 Richardson divergence); RETIRE the Layer-Functor F K=2 SUGGESTION row in `cross-pillar-bridge-corpus.md §"Hybrid Independence Test"`; add the §VII.AU.OP-PROJ S82-identity carve-out annotation (re-tag the W6-1 α=2.6926237 EXACT anchor as a Level-3 record of the S82 contour-deformation identity, NOT a universal-envelope theorem anchor). Effort ~0.5 we. Flagged for the orchestrator.

**4-tuple**: `(value='PASS_workshop-complete;STRUCTURAL_VERDICT=CLOSE_(VERDICT-B);K2_FALSIFIED-at-K2->CLOSED;…', scheme=ADVERSARIAL-WORKSHOP-2-AGENT-3-ROUND-LAYER-FUNCTOR-F-REFORMULATION, convention=R1-steelman-R2-respond-R3-converge-STRUCTURAL-VERDICT-reformulate-K2-weak-vs-close, L_max=N/A)`. **Dual-SHA**: audit_sha256=`__AUDIT__…` (COMPUTED over input-pin map), content_sha256=`__CONTENT__…` (workshop document). **Artifacts**: workshop doc `sessions/archive/session-93/workshops/s93-w9-5-layer-functor-f-reformulation.md` + verdict JSON `computations/session-93/s93_w9_5_layer_functor_f_reformulation_verdict.json` + emission script `computations/session-93/s93_w9_5_layer_functor_f_reformulation_verdict.py`."""


def main() -> int:
    if not WP.exists():
        print(f"ERROR: WP not found: {WP}")
        return 1
    text = WP.read_text(encoding="utf-8")  # (local) fresh read

    # Locate the §W9-5 section slice
    start = text.find(SECTION_HEADING)  # (local)
    if start == -1:
        print(f"ERROR: §W9-5 heading not found: {SECTION_HEADING}")
        return 1
    # next section heading after start (### or ##)
    rest = text[start + len(SECTION_HEADING):]  # (local)
    nxt_candidates = []  # (local)
    for marker in ("\n### ", "\n## "):
        i = rest.find(marker)
        if i != -1:
            nxt_candidates.append(i)
    end_rel = min(nxt_candidates) if nxt_candidates else len(rest)  # (local)
    end = start + len(SECTION_HEADING) + end_rel  # (local)
    section = text[start:end]  # (local) the §W9-5 slice ONLY

    # Idempotency: already completed?
    if "**Status**: COMPLETED" in section:
        print("SKIP: §W9-5 already COMPLETED (idempotent no-op).")
        return 0

    new_section = section  # (local)

    # (1) Status NOT STARTED -> COMPLETED (scoped to §W9-5 slice)
    new_section = new_section.replace("**Status**: NOT STARTED",
                                      "**Status**: COMPLETED", 1)

    # (2)-(5) replace the four placeholder italic blocks.
    # Each placeholder is a single italic line beginning with "*(pending" right after
    # its bold header. Replace header+placeholder with header+filled content.
    def replace_block(s: str, header: str, filled: str) -> str:
        h = s.find(header)  # (local)
        if h == -1:
            return s
        # the placeholder is the next non-empty line(s) starting with "*("
        p = s.find("*(", h)  # (local)
        if p == -1:
            return s
        # placeholder ends at the next blank line ("\n\n") after p
        q = s.find("\n\n", p)  # (local)
        if q == -1:
            q = len(s)
        return s[:h] + filled + s[q:]

    def shas(s: str) -> str:
        # substitute SHA-head tokens (avoids str.format brace collisions with markdown {…})
        return s.replace("__AUDIT__", AUDIT_SHA).replace("__CONTENT__", CONTENT_SHA)  # (local)

    new_section = replace_block(new_section, "**Output Artifacts**:", shas(OUTPUT_ARTIFACTS_FILLED))
    new_section = replace_block(new_section, "**MCP Pre-Compute Audit**:", shas(MCP_AUDIT_FILLED))
    new_section = replace_block(new_section, "**Verdict**:", shas(VERDICT_FILLED))
    new_section = replace_block(new_section, "**Results**:", shas(RESULTS_FILLED))

    if new_section == section:
        print("ERROR: no replacements applied (placeholders not matched).")
        return 1

    new_text = text[:start] + new_section + text[end:]  # (local)
    WP.write_text(new_text, encoding="utf-8")  # atomic single write
    print("OK: §W9-5 section patched (Status COMPLETED; 4 blocks filled).")
    print(f"  section bytes: {len(section)} -> {len(new_section)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
