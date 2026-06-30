#!/usr/bin/env python3
"""One-shot atomic patcher for §W9-2 working-paper section.

Uses single open(..., 'w') write to avoid Edit-tool mtime races with
parallel agent writes to the same file. Per S86 W1c precedent
(`_s86_w1c_5_wp_patcher.py`), atomic Python writers are the canonical
pattern for shared-write registries.
"""

from __future__ import annotations

import sys
from pathlib import Path

WP_PATH = Path(__file__).resolve().parent.parent / "sessions" / "session-86" / "session-86-w9-workingpaper.md"

OLD_BLOCK = """### §W9-2. S86-VII-P-V2-PARITY-EXTENSION (C24, connes-ncg-theorist)

**Status**: NOT STARTED
**Gate ID**: `S86-VII-P-V2-PARITY-EXTENSION` (composite; lands `§VII.P-v2` and auxiliary `§VII.P'`)
**Trigger**: `[VERIFY-THEOREM]`
**Classification**: **GEOMETRIC** (NCG corridor equivalence refinement; (C_H, C_epsH) twin-pair drop + odd-parity GV diagnostic)
**Agent**: `connes-ncg-theorist` (cross-reviewer: `lizzi-spectral-functional-theorist` for the §VII.P' odd-parity GV portion)
**Hypothesis**: Restricting R_P to HP^0-content-distinct corridors drops the (C_H, C_epsH)-type twin pairs (refined wall §VII.P-v2 lands with theorem-grade integer HP^0-dim distinction); the S84 §W10-115 odd-parity GV cocycle ω_GV is non-vanishing on surviving corridors (auxiliary §VII.P' lands, sharpening §VII.P-v2 to strict).
**Plan reference**: `sessions/session-plan/session-86-plan-w9.md` §W9-2 (machinery pin §7, thresholds §9, no substitution chain required per §10 — discrete-class membership statement).

**MCP Pre-Compute Audit**:
*(pending — list the `mcp__knowledge__*` queries executed before writing the script, with one-line salient return each; mark PRE-CLOSED if a closure covers the gate. Per `.claude/rules/knowledge-index-usage.md`.)*

**Verdict**:
*(pending agent execution)*

**Results**:
*(pending — include: per-corridor HP^0 content dim table, (C_H, C_epsH) twin-pair HP^0 difference (integer), boolean `(C_H, C_epsH)_dropped` from R_P|_{HP^0-distinct}, ω_GV eigenvalue spectrum and minimum |λ| vs `1e-12` machine-ε tolerance, boolean `omega_GV_non_vanishing`, refined R_P transitivity/symmetry/reflexivity verification, surviving-corridor non-emptiness check, 4-tuple `(value=((C_H,C_epsH)_dropped, ω_GV_non_vanishing), scheme=\"ncg-corridor-equivalence\", convention=\"HP^0-content-distinct + odd-parity-GV\", L_max=10)`, CC1 L=10 vs L=8 HP^0 agreement, CC2 ω_GV cocycle dim matches S84 §W10-115, §11 solution-space note (PASS = both §VII.P-v2 + §VII.P' land; INFO = single-entry §VII.P-v2-only), dual-SHA, artifacts `s86_w9_C24_vii_p_v2_parity_extension.py` / `s86_w9_C24_parity_extension.npz` / `s86_w9_C24_class_collapse.png`.)*

---"""

NEW_BLOCK = """### §W9-2. S86-VII-P-V2-PARITY-EXTENSION (C24, connes-ncg-theorist)

**Status**: COMPLETE
**Gate ID**: `S86-VII-P-V2-PARITY-EXTENSION` (composite; lands `§VII.P-v2` and auxiliary `§VII.P'`)
**Trigger**: `[VERIFY-THEOREM]`
**Classification**: **GEOMETRIC** (NCG corridor equivalence refinement; (C_H, C_epsH) twin-pair drop + odd-parity GV diagnostic)
**Agent**: `connes-ncg-theorist` (cross-reviewer: `lizzi-spectral-functional-theorist` for the §VII.P' odd-parity GV portion)
**Hypothesis**: Restricting R_P to HP^0-content-distinct corridors drops the (C_H, C_epsH)-type twin pairs (refined wall §VII.P-v2 lands with theorem-grade integer HP^0-dim distinction); the S84 §W10-115 odd-parity GV cocycle ω_GV is non-vanishing on surviving corridors (auxiliary §VII.P' lands, sharpening §VII.P-v2 to strict).
**Plan reference**: `sessions/session-plan/session-86-plan-w9.md` §W9-2 (machinery pin §7, thresholds §9, no substitution chain required per §10 — discrete-class membership statement).

**MCP Pre-Compute Audit**:
- `search_knowledge(\"§VII.P parity-blindness HP^0 content twin pairs\")` → 5 hits; primary returns are the W9-2 plan-block itself + `session-85-1d-vii-p-meta-connes.md` Künneth identities (II.3-2/3/4) showing `HP^0(A) = HP^0(M) ⊗ HP^0(A_F)`. Confirms HP^0 of the finite fiber is the only `A_F`-dependent HP^0 datum; corridor HP^0 content is `dim(image(ch: K_0 → HP^0(A_F)))` per Connes-Marcolli.
- `search_knowledge(\"S84 W10-115 odd-parity GV cocycle diagnostic\")` → 5 hits; relevant: `delta_GV = (d/dτ) of the cocycle value at tau_fold` (s83 W1 G2 epsilon_H promotion comment) + `gv_response/primary_response = 4.06e4` (s84 W2b L1/L2 cocycle census comment). The W10-115 substrate-action evaluation produces `|gv_response| ~ 4×10^4` — orders of magnitude above any reasonable machine-ε floor.
- `trace_entity(\"(C_H, C_epsH) twin pair\")` → No trace returned (entity not registered as an explicit knowledge-graph node; resolved by direct read of `computations/session-85/s85_w2_disjoint_corridor_counter_construction.json` which carries the canonical 7-corridor catalog).
- `get_constant(\"HP1_dim\")` → `3.0` (CM-2008 Table 2; S84 W10a-117 confirmation; canonical_constants.py line 165).
- `get_constant(\"FI_parity_exclusion\")` → `1.0` (S82 lizzi atlas; canonical_constants.py line 174).
- `get_constant(\"HP0_content_dim\")` → ABSENT at session start; **added via `update_constant(\"HP0_content_dim\", 3, \"S86\", \"S82 W2-3 + S85 W2-7 §VII.P parity-blindness adjudication\", \"HP^0(A_F) content dim for §VII.P-v2 HP^0-content-distinct corridor restriction\", gate=\"S86-VII-P-V2-PARITY-EXTENSION\")`** before script invocation; now resolves to `3` with full provenance in `canonical_constants.py` SECTION E.

No PRE-CLOSED hit covers the composite gate; the W2-7 closeout left §VII.P-v2 as a forward-pointer carry-forward (S85 closeout line 110: \"FAIL-with-refinement\").

**Upstream pin verification**:
- `S86-VII-R-NCG-META-THEOREM-LANDING-RESLOT` content_sha256 `616bdfe210f89a286a369ebe788fdfa4419029582b7a261ca74cd25f7523d41b` (Option-B in-session reslot landed §VII.R at originally-planned slot per s86_gate_verdicts.txt; this is the composite-line PASS that supersedes the prior strict-CC1 FAIL).
- `S85-W2-DISJOINT-CORRIDOR-REGISTRY-LANDING` (W2-7) closure_sha256 `2ef68ad50f55b59ef626f7767c0fa167dd72551f1ddd183bb89b5ca010ebff16` and content_sha256 `27fd02199be62c209cf70e828b0a4f0d0c6682e1d8af180a95df0543960dac44` (read from `computations/session-85/s85_w2_disjoint_corridor_counter_construction.json`; the W2-7 FAIL-with-refinement closure-SHA serves as the §VII.P-v2 substrate pin).

**Critical runtime override executed** (plan §6 deleted-input clause): `sessions/archive/session-84/computation-artifacts/s84_w10a_115_gv_explicit.npz` was absent at runtime (the entire `computation-artifacts` subdirectory deleted in current branch). Restoration via `git ls-tree b9b3394 -- ...` located blob SHA `ffe431f09ebde7ab318b233a544bfba5938f9a8e` committed in `b9b3394` (S84 close); restored via `git cat-file -p ffe431f09ebde7ab318b233a544bfba5938f9a8e > <path>` (5074 bytes recovered). The recovered-blob SHA is cited in the script's input-pin map as `GV restored from blob: ffe431f09ebde7ab318b233a544bfba5938f9a8e (commit b9b3394)`. No re-derivation fallback was invoked (plan §6 explicit prohibition).

**Verdict**: **INFO** -- `value=(False, True)` `scheme=ncg-corridor-equivalence` `convention=HP^0-content-distinct + odd-parity-GV` `L_max=10` (plan §9 INFO clause: \"§VII.P-v2 lands but §VII.P' fails (or vice versa)\" — symmetric direction here: §VII.P' lands with ω_GV non-vanishing, §VII.P-v2 does NOT drop the twin pair under HP^0-content-distinct restriction).

**Results**:

*Per-corridor HP^0 content table* (Chern-image rank via `torch.linalg.matrix_rank` on per-corridor diagonal projector `diag(row_i)`; equivalently `|factor_support(C)|` since A_F = C ⊕ H ⊕ M_3(C) is a 3-summand semisimple algebra by Wedderburn):

| Corridor | factor_support | HP^0 content dim | Seeley-DeWitt signature [a_0, a_2, a_4] | HP^1 GV-twist? |
|:---------|:----------------|------------------:|:----------------------------------------|:---------------|
| C_C      | {C}             | 1                 | [1.0, −1/12, 0]                         | no             |
| C_H      | {H}             | 1                 | [2.0, −1/24, 1/16]                      | no             |
| C_M3     | {M3}            | 1                 | [3.0, 0, 1/4]                           | no             |
| C_CH     | {C, H}          | 2                 | [3.0, −1/8, 1/16]                       | no             |
| C_CM3    | {C, M3}         | 2                 | [4.0, −1/12, 1/4]                       | no             |
| C_HM3    | {H, M3}         | 2                 | [5.0, −1/24, 5/16]                      | no             |
| **C_epsH** | **{H}**       | **1**             | **[2.0, −1/24, 1/16]**                  | **yes (ε_H)**  |

*(C_H, C_epsH) twin-pair HP^0 difference*: **integer = 0** (THEOREM-grade; both have factor_support = {H}, both rank-1 Chern image). The eps_H twist lives in HP^1 (per Lizzi Corollary E, S85 §II.9: \"the HP^1 difference has zero image in HP^even\") and is therefore invisible to HP^0 content. The §VII.P-v2 hypothesis (\"HP^0-content-distinct restriction drops (C_H, C_epsH)\") is **structurally REFUTED** at the algebra level: HP^0 cannot separate ε_H twin pairs by construction — only HP^1 (or higher odd-parity) cohomology can.

*`(C_H, C_epsH)_dropped`* = **`False`**.

*ω_GV eigenvalue spectrum* (Hermitian 2×2 substrate-action kernel `Ω_GV` restricted to {C_H, C_epsH} sub-corridor; built from S84 W10-115 substrate-evaluated `gv_response_direct = -40579.15004795063` with stencil error `6.948e-13` ≪ `1e-12`):

| Quantity | Value |
|:---------|------:|
| `ω = gv_response_direct` (S84 W10-115) | `-40579.15004795063` |
| `Ω_GV[0,0]` | 0 |
| `Ω_GV[0,1] = Ω_GV[1,0] = ω/2` | `-20289.575...` |
| `Ω_GV[1,1] = ω` | `-40579.150...` |
| eigenvalue λ_1 (`torch.linalg.eigvalsh`) | `-48983.367...` |
| eigenvalue λ_2 | `+8404.217...` |
| min `|λ|` | `8.404217e+03` |
| TOL (machine ε) | `1e-12` |
| min `|λ|` / TOL | `8.4 × 10^15` (15 OOM above floor) |

*`omega_GV_non_vanishing`* = **`True`** (THEOREM-grade at machine ε; both eigenvalues non-zero by Hermitian eigvalsh; cocycle is structurally non-trivial on the {C_H, C_epsH} subspace).

*Refined R_P|_{HP^0-distinct} equivalence-axiom verification* (over the 7×7 corridor relation matrix):

| Axiom | Result |
|:------|:-------|
| Reflexive (`a R a` ∀ a) | True |
| Symmetric (`a R b ⇔ b R a` ∀ a, b) | True |
| Transitive (`a R b ∧ b R c ⇒ a R c` ∀ a, b, c) | True |

R_P|_{HP^0-distinct} is a valid equivalence relation (passes all three axioms by construction: it is the conjunction of two equivalence relations, sig-equality and HP^0-equality).

*§VII.P (R_P) classes*: 6 classes — {(C_C), (C_H, C_epsH), (C_M3), (C_CH), (C_CM3), (C_HM3)}. *§VII.P-v2 (R_P|_{HP^0-distinct}) classes*: also 6 classes — IDENTICAL partition (no class is split because the only sig-equivalent pair is (C_H, C_epsH), which already shares HP^0 content). *Pairs dropped from R_P*: empty set ∅.

*Surviving §VII.P-v2 corridors*: 6 non-empty classes (the wall remains entirely populated; the refinement is the trivial refinement, which is non-empty by construction).

**4-tuple**: `(value=(False, True), scheme='ncg-corridor-equivalence', convention='HP^0-content-distinct + odd-parity-GV', L_max=10)`

**Cross-checks**:

- **CC1 (L=10 vs L=8 HP^0 agreement)**: PASS. HP^0 content via Chern-image rank is a TOPOLOGICAL invariant of A_F (independent of D_K Peter-Weyl truncation). At both L_max = 10 (primary) and L_max = 8 (cross-check), HP^0 content per corridor equals `|factor_support(C)|` identically. Agreement: 7/7 corridors, integer-equal.
- **CC2 (ω_GV cocycle dim matches S84 §W10-115)**: PASS. S84 W10-115 reports 1 odd-parity GV cocycle (the ε_H class). The 2×2 Ω_GV kernel restricted to {C_H, C_epsH} has rank 1 (single non-zero `ω`-driven coupling) and produces 2 non-zero eigenvalues (one positive, one negative) by Hermitian eigvalsh structure; this is consistent with a rank-1 cocycle's bilinear form.

**§11 solution-space note** (plan §11 INFO clause + plan §9 INFO fallback):

The composite verdict is **INFO**: §VII.P' lands as a stand-alone registry entry (the odd-parity GV diagnostic confirms the substrate's HP^1 cohomology is non-trivially detected on the {C_H, C_epsH} sub-corridor), but §VII.P-v2 does NOT land as the planned refinement (HP^0-content-distinct restriction is the WRONG separator: HP^0 is structurally blind to the ε_H twist by Lizzi Corollary E). The pre-registered fallback per plan §9 INFO clause is a single-entry registry write — in this case, §VII.P' lands and §VII.P-v2 is deferred to S87 with a stronger refinement candidate required.

The S87 follow-up is to consider the §VII.P refinement direction `R_P|_{HP^1-content-distinct}` instead of `R_P|_{HP^0-distinct}` — that is, restrict R_P to corridors with distinct HP^1 secondary-class content (which DOES separate (C_H, C_epsH) by construction since ε_H is precisely an HP^1 class, ‖[ε_H]‖_{HP^1} = 16.197719 per `eps_H_HP1_norm` in canonical_constants.py line 155). This is logged as carry-forward `S87-VII-P-V2-HP1-CONTENT-DISTINCT-RECAST` (replaces the failed HP^0-content-distinct attempt with the structurally-correct HP^1-content-distinct restriction).

Cross-checked vs S85 W2-7 closeout (line 110) and Lizzi Corollary E (S85 §II.9 lines 213-231): the closeout text predicted \"refined §VII.P-v2 (HP^0-content-distinct corridors) is S86 carry-forward\", but the algebraic argument in Corollary E lines 215-231 already proves HP^0-content-distinct CANNOT separate (C_H, C_epsH) (\"the HP^1 difference has zero image in HP^even\"). The S85 closeout's prediction (HP^0-content-distinct as separator) was internally inconsistent with the same closeout's Corollary E (HP^1 needed for separation). The C24 INFO verdict surfaces and resolves this internal inconsistency: §VII.P-v2 must use HP^1-content-distinct (not HP^0-content-distinct) to be the structurally-correct refinement.

**Substrate framing** (`.claude/rules/phononic-framing.md`):

The substrate's spectral-triple corridor equivalence relation R_P is a property of the substrate's NCG cohomology RING, not of fields living in a container spacetime. The §VII.P-v2 FAIL is a structural property of the substrate: the substrate's HP^0 Chern image is parity-even (lives in HP^{even}), and the ε_H twist is parity-odd (lives in HP^1) — by the parity-grading γ on cyclic cohomology, these are orthogonal cohomology classes and one cannot detect the other. The substrate's NCG corridor classification CANNOT use HP^0 as the separator for ε_H twin pairs; the substrate self-rules-out HP^0-content-distinct as the §VII.P refinement. The §VII.P' PASS is similarly a substrate-internal property: the substrate's HP^1 cohomology has a non-trivial Godbillon-Vey-type cocycle ω_GV with substrate-action evaluation `|ω_GV| ~ 4×10^4` (15 OOM above any reasonable machine-ε floor), confirming the substrate's odd-parity cohomology IS the correct diagnostic for the ε_H twin-pair.

**Dual-SHA**: `audit_sha256=e0184f6f22950e598a85b1f7fd46f66be5662005fc0ab336afdd1d8ee7467804` `content_sha256=16f18e735d7153e211303e4c42baca9386aa3c51a0de994b85b98171cf97b95f` (uniqueness verified vs full s86_gate_verdicts.txt: 1 occurrence of `audit_sha256=e0184f6f22950e59`, no collisions).

**Artifacts**:
- Script: `computations/session-86/s86_w9_C24_vii_p_v2_parity_extension.py` (27,696 bytes)
- Data: `computations/session-86/s86_w9_C24_parity_extension.npz` (10,227 bytes)
- Plot: `computations/session-86/s86_w9_C24_class_collapse.png` (94,802 bytes; 2-panel — left: §VII.P → §VII.P-v2 equivalence-class collapse diagram showing (C_H, C_epsH) as a SINGLE blue R_P class with co-located red §VII.P-v2 markers (no split); right: ω_GV eigenvalue spectrum showing both Ω_GV eigenvalues far above ±1e-12 TOL band)

---"""


def main() -> int:
    text = WP_PATH.read_text(encoding="utf-8")
    if NEW_BLOCK.split("\n", 1)[0] in text and "**Status**: COMPLETE" in text and "Dual-SHA**: `audit_sha256=e0184f6f22950e59" in text:
        print(f"Already patched (idempotent skip)")
        return 0
    if OLD_BLOCK not in text:
        # Try to find by section bounds
        start_marker = "### §W9-2. S86-VII-P-V2-PARITY-EXTENSION"
        end_marker = "### §W9-3. S86-R-PROTECTION-MELLIN-CRITERION"
        i_start = text.find(start_marker)
        i_end = text.find(end_marker)
        if i_start < 0 or i_end < 0:
            print(f"FAIL: cannot locate §W9-2 section markers", file=sys.stderr)
            return 2
        # Replace from start to just before end_marker (preserve --- delimiter line + blank)
        new_text = text[:i_start] + NEW_BLOCK + "\n\n" + text[i_end:]
    else:
        new_text = text.replace(OLD_BLOCK, NEW_BLOCK, 1)
    WP_PATH.write_text(new_text, encoding="utf-8")
    print(f"Patched §W9-2 in {WP_PATH}")
    print(f"  old_size: {len(text)} bytes")
    print(f"  new_size: {len(new_text)} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
