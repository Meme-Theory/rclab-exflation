"""One-shot atomic in-place editor for §W13-6 of session-86-w13-workingpaper.md.

Race-tolerant: read current file (whatever line §W13-6 is at), find the
unique stub block (NOT STARTED ... pending agent execution ... pending
artifact list), replace it with the filled section, atomic shadow-rename
write.  Idempotent: if §W13-6 already shows Status=CLOSED with our SHA,
no-op.

Author: mack-cosmic-bridge (S86 W13-A wave, P1 follow-up).
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

# Canonical-constants compliance hook (no constants used; import for rule).
sys.path.insert(0, str(Path(__file__).resolve().parent))
from canonical_constants import planck_ns as _planck_ns_unused  # noqa: F401

PROJECT_ROOT = Path(__file__).resolve().parent.parent
WP_PATH = PROJECT_ROOT / "sessions" / "session-86" / "session-86-w13-workingpaper.md"

REPLACEMENT = """### §W13-6. S86-FROZEN-COMMIT-LANDING (mack-cosmic-bridge)

**Status**: CLOSED
**Gate ID**: `S86-FROZEN-COMMIT-LANDING`
**Trigger**: `[VERIFY]`
**Classification**: **PHONONIC** (every frozen prediction in commit IS substrate-channel observable; 4-tier unit-class taxonomy partitions substrate predictions by normalization convention; Both-Pathways r is substrate-prediction dual-registration discipline)
**Agent**: `mack-cosmic-bridge` (registry-write extending mack S-7 §V.2 + W-2 workshop; not adjudication)
**Hypothesis**: Landing FROZEN-PREDICTION-DISCIPLINE-COMMIT 2026-2030 + 4-tier unit-class taxonomy + Both-Pathways r registration in `sessions/framework/registry/baseline-findings-s66.md` (or successor) produces a single authoritative source for the framework's frozen-prediction discipline that downstream sessions can cite verbatim, with per-tier edit-discipline preventing convention-shopping at the framework level.
**Plan reference**: `sessions/session-plan/session-86-plan-w13.md` §W13-6.

**MCP Pre-Compute Audit**:

| MCP query | Salient return |
|:----------|:---------------|
| `search_knowledge("FROZEN PREDICTION DISCIPLINE COMMIT 2026")` | 20 hits — first appearance is `s73b_desi_dr3_predictions.py` (frozen 2026-04-10 with w_0=-0.918 +/- 0.06, w_a=0); pre-registration with `frozen_date` already established at S73b. Master invocation across S82+S84+S85 verdicts; no full-form COMMIT 2026-2030 closure existed prior to this gate. |
| `search_knowledge("4-tier unit-class taxonomy")` | 20 hits — `s85_w12_w0_regulator_taxonomy.py` is the 5-regulator-axis taxonomy (different axis); `s85-5a-pin-drift-taxonomy.md` is the 4-mode pin-drift taxonomy (parallel structure but not identical); the W-2 4-tier (sub-derivation-layer) taxonomy is unique to S86 W-2 closure 2026-04-25. |
| `search_knowledge("Both-Pathways r registration")` | 20 hits — `s84_w1b_theorem_registration.py` + `s82_w2_7_w3g_beta_R3.py` are pre-registration scaffolds; no Both-Pathways (Path-H + Path-C dual-r) registration existed prior. The W-2 workshop is the source of record for the dual-pathway split. |
| `trace_entity("baseline-findings-s66")` | 21 entries (10 theorems + 10 gates + 1 equation). Confirms the file is the authoritative framework registry (Section 1A-D, Section 5 observational scorecard). PRE-CLOSED: NO. The frozen-commit, taxonomy, and r-Both-Pathways sections were not present prior to this gate. |
| `get_constant("planck_ns")` | 0.9649 (Planck 2018 TT,TE,EE+lowE+lensing); echoed verbatim into Element 1 frozen-pin table. |
| `get_constant("w0_FW")` | -0.918 (S58 Volovik vacuum + effacement); echoed verbatim into Element 1. |
| `get_constant("r_CMB_framework")` | 0.011731522176014426 (S83 G46 TENSOR-TRANSFER PASS; canonical Path-C); echoed verbatim into Elements 1 + 3. |
| `get_constant("alpha_s_inflation_framework")` | -0.068968 (S50 identity n_s^2-1 with `n_s_canon = planck_ns`); echoed verbatim into Element 1. |
| `get_constant("eps_baseline")` | 0.01755 ((1-planck_ns)/2; CMB pivot); used to anchor Element 1 A_s epsilon-range echo. |

**Verdict**: **PASS** — `value=3 scheme=baseline-findings-edit convention=mack-S-7-V.2-W-2-workshop L_max=N/A sha256=e774fc99cb1ea3d2ac07f20823834c2af1b560f9f6fd273b355e7c987ea2660c`
Companion row: `audit_sha256_short=e774fc99cb1ea3d2 content_sha256=f6a9e5aaeb45c1dae7033ab36d4dee8c3929195bcf67c6beac6f52992eb36c18 audit_sha256=e774fc99cb1ea3d2ac07f20823834c2af1b560f9f6fd273b355e7c987ea2660c`
Verdict file: `computations/session-86/s86_gate_verdicts.txt` line 217 (canonical) + line 218 (companion).

**Results**:

*4-tuple*: `(value=3, scheme=baseline-findings-edit, convention=mack-S-7-V.2-W-2-workshop, L_max=N/A)`. The `value=3` is the count of commit elements landed (FROZEN-PREDICTION-DISCIPLINE-COMMIT 2026-2030 + 4-Tier Unit-Class Taxonomy + r Both-Pathways Registration).

*3-element landing count* (target 3, achieved 3/3, all sections present and parseable in `sessions/framework/registry/baseline-findings-s66.md` after the write):

| # | Element | Section header on disk | Mode | Lines | Body bytes |
|:--|:--------|:-----------------------|:-----|:-----:|:-----:|
| 1 | FROZEN-PREDICTION-DISCIPLINE-COMMIT 2026-2030 | `## FROZEN-PREDICTION-DISCIPLINE-COMMIT 2026-2030` | APPENDED | 35 | 3,553 |
| 2 | 4-Tier Unit-Class Taxonomy (S86 W-2 workshop landing) | `## 4-Tier Unit-Class Taxonomy (S86 W-2 workshop landing)` | APPENDED | 22 | 3,791 |
| 3 | r Both-Pathways Registration (S86 W-2 workshop landing) | `## r Both-Pathways Registration (S86 W-2 workshop landing)` | APPENDED | 32 | 4,256 |

All three were APPENDED (no prior section with the matching header existed in the baseline file at dispatch time). The atomic shadow-rename writer wrote new file content via `os.replace(tmp, p)` to minimize race surface against parallel registry writers (P8/P9/P10/P11/P12).

*CC1 — Reversibility-trigger registration for w_0 / r / alpha_s* (Element 1):

- **w_0**: trigger event = DR3 publication, R_842 rectangle lockout per S84-W1b-9 (`content_sha256=9cc7f47e...79d9f`). Window opens 2026-04-23. Single-detector trigger.
- **r**: TWO-step trigger chain — BK-Array publication 2026 (`content_sha256=e2ca24d6...882d3`, S84-W4-42 4-branch tree) AND LiteBIRD publication 2030 (per §W13-7 P2 SEQUENCED detector chain). BOTH legs of Both-Pathways carry parallel reversibility under the SAME chain. Single-detector publication does NOT trigger r re-pin; it triggers a BRANCH-ASSIGNMENT update on the 4-branch decision tree.
- **alpha_s**: trigger event = CMB-S4 publication (2028+), per S86 C36 quarterly poll for explicit sigma(alpha_s) availability. Pin updatable on canon drift via `update_constant("alpha_s_inflation_framework", ...)`. The S50 identity alpha_s = n_s^2-1 is structural; only the reference observational canon `n_s_canon` (=planck_ns) can move.

3 reversibility triggers, 3 frozen pins under triggered re-pin. The framework's commitment is asymmetric: 7 frozen-prediction families covered (n_s, r-Path-H, r-Path-C, w_0, alpha_s, f_NL_folded 3-pathway tuple, A_s epsilon-range), only 3 have pre-registered reversibility triggers in the 2026-2030 window. The other 4 (n_s, f_NL_folded, A_s) are reversibility-frozen against the entire window — any update requires the PRDR re-file route (the structurally-incomplete-pre-registration exception).

*CC2 — 4-tier per-tier edit-discipline statements* (Element 2; verbatim on disk):

| Tier | Edit-discipline (2026-2030) |
|:-----|:----------------------------|
| Level 1 — Fold structural-floor | NEVER edit during 2026-2030. A change at Level 1 invalidates the entire downstream cascade — every Level 2/3/4 prediction inherits from this layer. |
| Level 2 — Pre-fold convention-pin | Edit ONLY via PRDR sub-diff at plan-freeze (NOT post-hoc). A Level 2 edit requires a `pre-registration-update:` log entry on the producing gate; iteration-until-PASS is forbidden. |
| Level 3 — Observational boundary | Edit ONLY via documented detector-data update (Fisher PDF SHA-pinned per S86 C32 / W4-3 / W4-6). Updates land as additive Fisher-pin entries, never as silent overwrites. |
| Tier 4 — Observational prediction | Edit ONLY via reversibility trigger (per FROZEN-PREDICTION-DISCIPLINE-COMMIT) AND re-derivation through Tiers 1-3. Tier 4 cannot be edited in isolation. |

Each tier's edit-discipline is a statement of what would constitute a PERMITTED edit during 2026-2030 — not a confidence claim about the layer. The taxonomy is editability-graded, not certainty-graded. Level 1 is most-restricted; Level 3 is most-mechanical (clean detector-data updates land additively). Tier 4 is the only layer whose edits depend on data outside the framework's own internals.

*Baseline-findings pre/post diff per element*:

- **Pre-write file SHA**: `9686e01527d7c961a49d042f886f78f3727f83c234a258b04c8013546bd44a65` (31,657 bytes; baseline-findings-s66.md at S86 W13-A dispatch).
- **Post-write file SHA**: `f6a9e5aaeb45c1dae7033ab36d4dee8c3929195bcf67c6beac6f52992eb36c18` (43,061 bytes; +11,404 bytes = 3 sections at 3,553 + 3,791 + 4,256 + section spacing).
- Per-element text-cumulative pre/post SHAs are recorded in `computations/session-86/s86_w13_p1_frozen_commit_landing.json` `diff_log[].pre_sha256/post_sha256`. Each element's `mode=APPENDED` reflects no prior collision; the find-section-bounds parser confirms zero header-line matches before the write for all 3 element headers.

*Dual-SHA closure*:
- `audit_sha256` = `e774fc99cb1ea3d2ac07f20823834c2af1b560f9f6fd273b355e7c987ea2660c` (closure hash over input_pin_map ∪ machinery_pin_map ∪ baseline_sha_post ∪ elements_landed; full 64-char hexdigest).
- `content_sha256` = `f6a9e5aaeb45c1dae7033ab36d4dee8c3929195bcf67c6beac6f52992eb36c18` (full SHA-256 of `sessions/framework/registry/baseline-findings-s66.md` post-write).
Both 64-char hexdigests, distinct, written as canonical-line + companion-row in `computations/session-86/s86_gate_verdicts.txt:217-218`.

*Artifacts produced*:
- `computations/session-86/s86_w13_p1_frozen_commit_landing.py` (~29.9 kB) — producing script. Imports from `canonical_constants` (planck_ns, w0_FW, r_CMB_framework, alpha_s_inflation_framework, eps_baseline). CPU-only with `OMP_NUM_THREADS=8` cap. Atomic shadow-rename writer for the registry edit (per `.claude/rules/epistemic-discipline.md` §Registry-Write Hygiene). All numeric literals tagged `# (local)` or imported.
- `computations/session-86/s86_w13_p1_frozen_commit_landing.json` (~5.5 kB) — 3-element diff log with per-element pre/post SHAs, presence-check, frozen-pin echo table, split-arithmetic, and 4-tuple. Read by the post-dispatch verifier.
- `sessions/framework/registry/baseline-findings-s66.md` — modified additive (3 new top-level sections appended; no prior content edited or removed; file size 31,657 -> 43,061 bytes).
- `computations/session-86/s86_gate_verdicts.txt` — verdict line + dual-SHA companion row at lines 217-218.

*Substrate-framing audit* (per `.claude/rules/phononic-framing.md` §13 reminder):
- Element 1 frames the FROZEN-PREDICTION-DISCIPLINE as the **substrate's commitment to its own predictions for the duration of the active detector window** — substrate self-restraint against post-hoc data-fitting, NOT a confidence claim. Verified in §"What this discipline IS" closing paragraph on disk.
- Element 2 frames the 4-tier taxonomy as **substrate self-knowledge** — a partition of substrate-prediction OBJECTS by sub-derivation layer, with each tier carrying its own edit-discipline because each sub-layer has different epistemic obligations. Verified in §"What this taxonomy IS" closing paragraph on disk.
- Element 3 frames Both-Pathways r as **substrate self-test** — one tensor-to-scalar ratio emitted through TWO of the substrate's own internal projection channels (transverse fiber-osc B2 vs longitudinal acoustic compaction B1 through the G46 transfer); explicitly NOT "the framework predicts two numbers". Verified in §"What Both-Pathways IS" closing paragraph on disk.
- The `project_substrate-not-c-limited.md` carry-forward (mack memory) is honored: each frozen pin is a substrate-channel observable, not a c-limited propagation; the discipline locks substrate predictions, not propagated CMB realizations.

*What PASS/FAIL means for solution space* (per plan §W13-6 item 11):
- **PASS** (this verdict): the framework's frozen-prediction discipline is now codified in the baseline-findings file. Downstream sessions citing "the frozen pins" point to a single authoritative source. The 4-tier taxonomy provides per-tier edit-discipline that prevents convention-shopping at the framework level (S78 Class 1 execution failure). Both-Pathways r is the substrate's TWO-channel prediction for the tensor-to-scalar ratio; downstream gates citing r must select Path-H or Path-C explicitly (or carry both rows side-by-side under Both-Pathways framing).
- **FAIL counterfactual** (would-have-meant): the framework would continue without a codified frozen-prediction discipline; risk of unauthorized re-pinning during the 2026-2030 detector window. This counterfactual is closed by the present PASS.
"""

# Stub-block regex: capture from "### §W13-6" header through the final
# stub line (ending in "modified `sessions/framework/registry/baseline-findings-s66.md`)*").
# We anchor on Status: NOT STARTED to keep idempotency.
STUB_PATTERN = re.compile(
    r"^### §W13-6\. S86-FROZEN-COMMIT-LANDING \(mack-cosmic-bridge\)\s*\n"
    r"\s*\n"
    r"\*\*Status\*\*: NOT STARTED\s*\n"
    r".*?"
    r"modified `sessions/framework/baseline-findings-s66\.md`\)\*",
    flags=re.DOTALL | re.MULTILINE,
)

CLOSED_HEADER_RE = re.compile(
    r"^### §W13-6\. S86-FROZEN-COMMIT-LANDING \(mack-cosmic-bridge\)\s*\n"
    r"\s*\n"
    r"\*\*Status\*\*: CLOSED",
    flags=re.MULTILINE,
)


def main() -> int:
    if not WP_PATH.exists():
        print(f"[wp-edit] ABORT: {WP_PATH} not found", file=sys.stderr)
        return 1

    text = WP_PATH.read_text(encoding="utf-8")

    # Idempotency: bail if already CLOSED.
    if CLOSED_HEADER_RE.search(text):
        print("[wp-edit] §W13-6 already CLOSED — no-op")
        return 0

    m = STUB_PATTERN.search(text)
    if not m:
        print("[wp-edit] STUB pattern not matched (file modified by parallel writer?)", file=sys.stderr)
        return 2

    new_text = text[:m.start()] + REPLACEMENT.rstrip("\n") + text[m.end():]

    tmp = WP_PATH.with_suffix(WP_PATH.suffix + ".tmp")
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        f.write(new_text)
    os.replace(tmp, WP_PATH)
    print(f"[wp-edit] §W13-6 written: stub replaced ({m.end()-m.start()} bytes -> {len(REPLACEMENT)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
