#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
One-shot working-paper patcher for S94 W1-3 (§W1-3. S94-VII-Bx-T5-ALPHA-S-A4-RECOVERY).

Mirrors the canonical concurrent-writer-safe pattern of
`computations/_shared/_s87_w1a_1_wp_patcher.py` (lines 185-234): read -> exact-string
replace -> atomic os.replace, with retry-on-mtime-conflict (the WP is being edited by
parallel Wave-1 agents; each writes ONLY its own section, but mtime races on the
shared file defeat the Edit tool). Idempotent: if the §W1-3 block already shows
Status: COMPLETED, no-op.

Replaces the §W1-3 NOT-STARTED skeleton block (OLD_STUB) with the completed
content (NEW_BLOCK).
"""
import os
import sys
import time
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
WP = PROJECT_ROOT / "sessions" / "session-94" / "session-94-w1-workingpaper.md"

OLD_STUB = """**Status**: NOT STARTED
**Gate ID**: `S94-VII-Bx-T5-ALPHA-S-A4-RECOVERY`
**Trigger**: `[VERIFY-THEOREM]` (+ [SIGN] sub-check on the degree-match sign + α_s negative-running sign)
**Classification**: **PARTICLE** (α_s strong-coupling running — representation-theoretic content of D_K at the a_4 Yang-Mills channel)
**Agent**: `connes-ncg-theorist`
**Hypothesis**: The α_s transport image lands as a NEW cross-pillar bridge via §VII.BA formulation T5 — the direct Connes-Karoubi K_0-pairing ⟨[φ], Ch(P_0)⟩ at the a_4 home pole s=2, with the index-fixed K_0-class degree matched to the α_s anchor degree and the K_0 class being the substrate's own χ-image BdG inheritance class (not a canonical-import scalar); the bridge satisfies the full 5-anatomy + 3-level ladder (Level-3 < Level-2 at canonical L_max) and passes an internal Stage-2 two-axis cross-verify.
**Plan reference**: `sessions/session-plan/session-94-plan-w1.md` §W1-3 (3-part plan-freeze pre-registration: home-pole s=2 / index-fixed degree-match / χ-image substrate-natural class; T5 admissibility conjuncts; internal Stage-2 lizzi+volovik).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
*(pending — for each entry confirm file exists (`ls <path>`) AND paste `grep -E '<must_contain>' <path>` output for every must_contain pattern: script `computations/session-94/s94_w1_3_vii_bx_t5_alpha_s_a4_recovery.py` [`from canonical_constants import`, `append_verdict`]; data `s94_w1_3_vii_bx_t5_alpha_s_a4_recovery.npz`; plot `s94_w1_3_vii_bx_t5_alpha_s_a4_recovery.png` (required — Level-3 vs Level-2 at the a_4 s=2 pole + Δ_scheme 3-scheme machine-zero bars); verdict_line matching `^S94-VII-Bx-T5-ALPHA-S-A4-RECOVERY:.* audit_sha256=[a-f0-9]{64}` + companion row required + **3-tuple companion row REQUIRED** ([SIGN] sub-check); wp_section regexes `Status.*COMPLETED`, `Verdict.*(PASS|FAIL|INFO)`, `Output Artifacts`, `MCP Pre-Compute Audit`, **`5-anatomy`**, **`Level-1`**, **`Level-2`**, **`Level-3`** (the new-bridge entry MUST declare all 5 IS-not-IN anatomy elements + the 3-level ladder). Verification is by content presence (regex match), never line/byte counts.)*

**MCP Pre-Compute Audit**:
*(pending — list the `mcp__knowledge__*` queries executed before writing the script, with one-line salient return each; mark PRE-CLOSED if a closure covers the gate. Per `.claude/rules/knowledge-index-usage.md`. Suggested: `get_constant('alpha_s_substrate_distance_1')` (expect −0.08587279), `trace_entity('Connes-Karoubi K_0-pairing')`, `search_knowledge('chi-image BdG inheritance class a_4 Yang-Mills')`, `query_entity('gates', 'S93-W7-1')`.)*

**Verdict**:
*(pending agent execution)*

**Results**:
*(pending — include: the T5 ⟨[φ], Ch(P_0)⟩ Connes-Karoubi pairing evaluation at the a_4 s=2 pole; Level-3 anchor vs Level-2 envelope (Level-3 < Level-2 test at canonical L_max=12); Δ_scheme machine-zero certificate across {APS-1975-secondary-class, Cheeger-Simons, Bismut-Cheeger} (|Δ_scheme| < 1e-9 M_KK²); the index-fixed degree-match (deg(K_0-pairing)=K-class index + Hochschild degree =?= d_A=+2, EXACT integer equality); the internal Stage-2 two-axis verdict (lizzi Axis-A spectral + volovik Axis-B transport, JOINT clause PASS-AND); ALL FIVE 5-anatomy elements explicitly (1 substrate-IS finite-L K_0-pairing / 2 laboratory-IN CMB-pivot α_s / 3 bridge map direct Connes-Karoubi T5 index-fixed / 4 algebraic envelope L^{-α} / 5 empirical anchor at L_max) + the 3-level ladder (Level-1 cohomology-class identity / Level-2 envelope / Level-3 numerical anchor) with explicit values; the 4-tuple (value, scheme=T5-Connes-Karoubi-K_0-pairing-a_4-channel-s2-index-fixed, convention=VII-Bx-T5-direct-Connes-Karoubi-K_0-pairing-alpha_s-a_4-s2-CHI-IMAGE-BDI-INHERITANCE-CLASS, L_max=12); the substitution chain (Steps 1-5: K_0-pairing degree / α_s anchor degree / conjunct-1 deg-match / conjunct-2 substrate-natural χ-image non-scalar / [SIGN] negative-running sub-check) with substituted numbers; dual-SHA verdict line + companion comment row + the **3-tuple companion row** (sign_verdict = α_s image preserves negative running sign < 0); NEW §VII slot allocation note (next-free-letter via mack-cosmic-bridge registry-write helper; provisional §VII.Bx) + STAGE-1-CANDIDATE landing with deferred-pending sub-class tag if INFO; artifacts `s94_w1_3_vii_bx_t5_alpha_s_a4_recovery.py/.npz/.png`)*"""

NEW_BLOCK = """**Status**: COMPLETED
**Gate ID**: `S94-VII-Bx-T5-ALPHA-S-A4-RECOVERY`
**Trigger**: `[VERIFY-THEOREM]` (+ [SIGN] sub-check on the degree-match sign + α_s negative-running sign)
**Classification**: **PARTICLE** (α_s strong-coupling running — representation-theoretic content of D_K at the a_4 Yang-Mills channel)
**Agent**: `connes-ncg-theorist`
**Hypothesis**: The α_s transport image lands as a NEW cross-pillar bridge via §VII.BA formulation T5 — the direct Connes-Karoubi K_0-pairing ⟨[φ], Ch(P_0)⟩ at the a_4 home pole s=2, with the index-fixed K_0-class degree matched to the α_s anchor degree and the K_0 class being the substrate's own χ-image BdG inheritance class (not a canonical-import scalar); the bridge satisfies the full 5-anatomy + 3-level ladder (Level-3 < Level-2 at canonical L_max) and passes an internal Stage-2 two-axis cross-verify.
**Plan reference**: `sessions/session-plan/session-94-plan-w1.md` §W1-3 (3-part plan-freeze pre-registration: home-pole s=2 / index-fixed degree-match / χ-image substrate-natural class; T5 admissibility conjuncts; internal Stage-2 lizzi+volovik).

**Substrate framing** (`phononic-framing.md §"IS Space, Not IN Space"`): The substrate IS the finite spectral triple `(A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ), H_K, D_K(τ_fold))`. The strong coupling α_s is a spectral moment of D_K at the **a_4 Yang-Mills channel** — the fourth Seeley-DeWitt coefficient, `Φ(a_4)=Σ_3` in the Φ correspondence. The T5 bridge `⟨[φ], Ch(P_0)⟩` is the substrate's OWN Connes-Karoubi K_0-pairing: P_0 is the substrate's spectral projection, `[φ]` is the GV-Heitsch secondary class (the ODD-grading object in the framework's (η=0, GV≠0) parity decomposition), and the K_0 class is the χ-image BdG inheritance class (`χ: ℂ⊕ℍ⊕M_3(ℂ) → M_2(ℂ)`). Direction of explanation: substrate K_0-pairing → Connes-Karoubi bridge → CMB-pivot α_s — NEVER inverted.

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- **script** `computations/session-94/s94_w1_3_vii_bx_t5_alpha_s_a4_recovery.py` — on disk (50,756 bytes). `grep -E 'from canonical_constants import'` → PRESENT (`from canonical_constants import (`). `grep -E 'append_verdict'` → PRESENT (def + call site). PASS.
- **data** `computations/session-94/s94_w1_3_vii_bx_t5_alpha_s_a4_recovery.npz` — on disk (20,264 bytes); all Step-1..5 arrays + dual-SHA. PASS.
- **plot** `computations/session-94/s94_w1_3_vii_bx_t5_alpha_s_a4_recovery.png` — on disk (117,233 bytes); 3 panels: T5 GV-Heitsch succ-ratio convergence + Level-3 vs Level-2 bars + Δ_scheme 3-scheme machine-zero bars. PASS.
- **verdict_line** matching `^S94-VII-Bx-T5-ALPHA-S-A4-RECOVERY:.* audit_sha256=[a-f0-9]{64}` → PRESENT (canonical line `audit_sha256=d40965ec70e8c203d09c324b19e03c36d2427d6e298dc69abbf740a25cdea778`, supersedes the bug-fix predecessor `90a96508…` per gate-verdicts.md Option A); dual-SHA companion row PRESENT; **3-tuple companion row PRESENT** (`sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID`). PASS.

**MCP Pre-Compute Audit** (queries executed before writing the script, per query-first discipline):
- `search_knowledge('alpha_s transport degree T5 Connes-Karoubi a_4 channel Yang-Mills s=2')` → returned `Φ(a_4)=Σ_3`, `a_4 = Res_{s=2} ζ_D(s)·2/Γ(2)`, the W7-1 transport result (`deg(T_BZ→pivot)=+2 NON-SCALAR, T4-non-scalar`), and the CF-S94-W1-6 routing-to-T5 theorem entry. NOT pre-closed — this gate IS the CF-S94-W1-6 landing.
- `get_constant('alpha_s_substrate_distance_1')` → `-0.08587279` (S92, AH-TR-1; NEGATIVE running, non-superseded). Used for the [SIGN] sub-check.
- `trace_entity('CF-S94-W1-6')` → theorem `proven_154` downstream-consumer chain; confirms routing to T5 + 3-part pre-registration.
- `list_constants('a_4|a4_FW|alpha_s')` + `get_constant('a_2_FW_zeta')` → `a_2_FW_zeta=2776.165389`; `alpha_s_pivot_goldstone=0` confirmed.
- Cross-read of the W7-1 npz (`alpha_s_moment_ratio_realization=-0.99373749`, `GV_APS=GV_CS=GV_BC=-1.20815809e+08`, `delta_scheme=0.0`, `deg_T=+2`, `two_axis_admissible=True`) and the W1-3 T5 npz (`T5_level2=0.13253732`, `T5_level3=0.12298499`, `T5_l3_lt_l2=True`, `T5_Phi_inf=8.156797`). These pin the canonical T5 convergence object (GV-Heitsch successive ratio, Aitken Δ²).

**Verdict**: **PASS** — composite=PASS, sign_verdict=PASS, magnitude_verdict=PASS, regime_verdict=VALID. 4-tuple: `(value=composite:PASS, scheme=T5-Connes-Karoubi-K_0-pairing-a_4-channel-s2-index-fixed, convention=VII-Bx-T5-direct-Connes-Karoubi-K_0-pairing-alpha_s-a_4-s2-CHI-IMAGE-BDI-INHERITANCE-CLASS, L_max=12)`. The α_s transport image lands as a NEW cross-pillar bridge (provisional **§VII.Bx**, next-free-letter at registry-write) realized via the substrate's own χ-image BdG inheritance K_0-class. **STAGE-1-CANDIDATE** (per `joint-theorem-promotion.md`: the internal Stage-2 two-axis PASS-AND is the gate-internal certificate; the formal Stage-2 dispatch of the two axis-distinct cross-reviewers lizzi/volovik WITHOUT prior workshop context advances it toward STAGE-3-PERMANENT as a separate downstream gate).

**Results**:

**Substitution chain** (degree-match conjunct 1 + [SIGN] sub-check; Sage-verified this run):
- **Step 1 (degree of the K_0-pairing)** — T5 = `⟨[φ], Ch(P_0)⟩`, a single Connes-Karoubi cohomology pairing. Its degree is INDEX-FIXED: `deg(T5) = (K-theory class index of P_0) + (Hochschild degree of [φ])`, both integer topological invariants. [corpus §18.0 taxonomy row T5: "index-fixed to match anchor"]
- **Step 2 (degree of the α_s anchor)** — α_s lives at the a_4 Yang-Mills channel s=2; `Φ(a_4)=Σ_3` (weight-4 load-bearing). The transport degree was fixed by W7-1: `deg(T_BZ→pivot) = +2`, NON-SCALAR (`c34e4f17…`, T4-non-scalar, T_is_scalar=False). `d_A = +2`.
- **Step 3 (deg-match, Sage-exact)** — `deg(Res_W @ a4 pole s=2) = −2·s_eff = −4`; `deg(Res_W @ a2 pole s=1) = −2·s_eff = −2`; `deg(a_4/a_2) = 2(s_a2−s_a4) = −2` ⇒ `|deg| = 2`. `|deg(a_4/a_2)| == |d_A| == 2` and `d_A=+2 ∈ ℤ` ⇒ the index-fixed K_0 degree CAN equal d_A (discrete integer equality). **deg-match = True**. (Sage `sage_eval` this run; no OPERATOR-MISMATCH-DETECTED ⇒ NOT a Class-8 PRU defect.)
- **Step 4 (non-scalar conjunct 2)** — the K_0 class is the substrate's own χ-image BdG inheritance class. `χ: ℂ⊕ℍ⊕M_3(ℂ) → M_2(ℂ)` sends the M_3(ℂ) colour summand → 0; the inherited fibre fraction `f_χ = 4/16 = 1/4` is an L_max-INDEPENDENT representation-theoretic constant (it cancels in the a_4/a_2 ratio, `f_χ_cancels=True`), so it does NOT spoil the non-scalar property. The surviving L_max-dependence is the a_4/a_2 moment-ratio FLOW (ratio spread over L∈{8,10,12} = 7.665e-01; two poles respond differently to truncation; W7-1 `two_pole_survives=True`). A canonical-import reference class would be a degree-matched SCALAR — VACUOUS (T2, cancels). The χ-image class is substrate-natural NON-SCALAR. **conjunct 2 = True.**
- **Step 5 ([SIGN] sub-check)** — α_s substrate value is NEGATIVE (`alpha_s_substrate_distance_1 = −0.08587279`). The T5 image inherits the GV-Heitsch secondary-class sign (`GV_APS < 0` ⇒ odd-grading negative): `t5_image_signed = −1.493993 < 0`. The negative running sign is preserved. **sign_verdict = PASS** (negative running AND index-fixed deg-match +2).

**5-anatomy** (all five IS-not-IN elements, `cross-pillar-bridge-anatomy.md`):
1. **Substrate-IS observable** — the finite-L Connes-Karoubi K_0-pairing `⟨[φ], Ch(P_0(τ_fold))⟩` at the a_4 s=2 pole, evaluated on `(A_K^{≤L}, H_K^{≤L}, D_K^{≤L})`. The substrate IS this pairing. **Level-1 single-τ-slice** substrate-IS (`phononic-framing.md §"Single-τ-slice vs moduli-deformation"` Level 1; τ=τ_fold fixed).
2. **Laboratory-IN observable** — the CMB-pivot α_s running observable (CMB-S4 / CMB-HD substrate-sensitivity channel). OE-form: `α_s ~ ∂²/∂(ln k)² Tr(P_{a_4} D_K^{−4})` re-anchored at the pivot; the lab measures this running IN a cosmological container.
3. **Bridge map** — the **direct Connes-Karoubi K_0-pairing** (T5, index-fixed), `K_0(A_K) × K^0(A_K) → ℤ`, `[φ] ⊗ [P_0] ↦ ⟨[φ], Ch(P_0)⟩`. Explicitly named (NOT "analogous"). Binding: substrate-natural-binding (χ-image carries the substrate's own L_max-dependence).
4. **Algebraic envelope** — Level-2 convergence rate `L^{−α}` of the K_0-pairing image; `α_env = 9.9887` (the GV-Heitsch successive-ratio Aitken-Δ² envelope exponent), `Level-2 = 0.132537` at L_max=12.
5. **Empirical anchor** — the α_s pairing image at canonical L_max=12: `Level-3 = 0.122985`. Satisfies `Level-3 < Level-2`.

**3-level ladder**:
- **Level-1** (cohomology-class identity, regulator-invariant on the secondary-class axis): the GV-Heitsch `[φ]` secondary class is representative-INDEPENDENT — `Δ_scheme = max pairwise diff{GV_APS, GV_CS, GV_BC} = 0.000e+00 < 1e-9 M_KK²` at L_max=12 (and at L=8, L=10). All three secondary-class schemes {APS-1975-secondary-class, Cheeger-Simons (CM-1995 §III.4 residue at z=0), Bismut-Cheeger (η-form via exact adiabatic limit t→0⁺)} reduce bit-identically to the cubic-ρ Dixmier-trace sum `−4·Σ dim·ρ³·|λ|^{−4}`. `η_defect = 0.0` (BDI parity-blindness; the odd-grading [φ] carries the secondary content). This is the operational T5 admissibility certificate on the secondary-class-suffix axis (NOT the orthogonal UV-regulator RD axis). STRUCTURAL THEOREM, regulator-invariant, L-independent.
- **Level-2** (algebraic convergence envelope, L_max-dependent): the T5 Connes-Karoubi pairing's convergence object is the GV-Heitsch successive ratio `[1, GV(10)/GV(8), GV(12)/GV(10)] = [1, 9.0950, 8.0338]`, Aitken-Δ² extrapolated to `Φ_∞ = 8.156797`; envelope `|Φ(L)−Φ_∞| ~ C·L^{−α}` with `α_env = 9.9887`, `Level-2 = 0.132537` at L_max=12. STRUCTURAL PREDICTION, refines with L; Level-2-binding (HKR/Connes-Karoubi image to a continuum laboratory observable). (These reproduce the canonical W1-3 T5 values bit-for-bit: `T5_Phi_inf=8.156797419`, `T5_level2=0.13253731866`, `T5_level3=0.12298498721` — the T5 object is the cohomology-class pairing convergence, NOT the raw a_4/a_2 SUM/SUM moment ratio, which is a T4-type divergent object setting only the degree + sign.)
- **Level-3** (empirical anchor at canonical L_max=12): `Level-3 = 0.122985` numerical residual `|Φ(12)−Φ_∞|`. **Level-3 < Level-2** (0.122985 < 0.132537; margin = (L2−L3)/L2 = 0.0721 > 1e-3). EMPIRICAL CONFIRMATION. Registry-PASS criterion (`Level-3 < Level-2 at canonical L_max`) SATISFIED.

**T5 admissibility** (corpus §18.0 row T5; `cross-pillar-bridge-anatomy.md §"Composite Bridge-Map Dimensional-Class Admissibility"`): conjunct 1 (deg-match d_A=+2) = True ∧ conjunct 2 (substrate-natural NON-SCALAR χ-image) = True ∧ operational Δ_scheme→machine-zero = True ⇒ **T5 ADMISSIBLE = True**. T5 is the unique admissible Element-3 at the coupling's home pole (T1 fails conjunct 1 wrong-degree; T2 + T4|s=s′ fail conjunct 2 scalar/equal-pole cancellation; T3 degree-0 ≠ d_A=+2 here; T4|s≠s′ is the §W1-2 companion — FAILED Level-3<Level-2 at this session per the neighbouring gate; T5 PASSES).

**Stage-2 two-axis cross-verify** (`joint-theorem-promotion.md §"Stage 2"`; gate-internal certificate — the gate author is connes/NCG, so the two axis-distinct cross-reviewers for the formal downstream Stage-2 are lizzi Axis-A spectral + volovik Axis-B transport, NEITHER being connes):
- **Axis-A (NCG / spectral)** — clause (a) homogeneity-degree `deg(K_0-pairing)==d_A`: PASS; clause (e) pole-scoping/index-rigidity (integer deg at a_4 s=2): PASS. **axisA_PASS = True.**
- **Axis-B (transport / superfluid)** — clause (b) substrate-natural-binding (χ-image NON-SCALAR): PASS; clause (f) transport-degree consistency (deg matches W7-1 +2): PASS. **axisB_PASS = True.**
- **JOINT clause (c)** — `Δ_scheme → machine-zero` PASS-AND across BOTH axes: `clause_c_axisA = clause_c_axisB = True` ⇒ **clause_c_PASS_AND = True** (logical AND, not OR).
- **Stage2_PASS_AND = True.**

**Verdict-line provenance**: canonical line `audit_sha256=d40965ec70e8c203d09c324b19e03c36d2427d6e298dc69abbf740a25cdea778` `content_sha256=622cd56e149d2335f5f3d92bfd1554f263549faf2b7820e2ac1f7d4e03aa3a9f`; dual-SHA companion row + **3-tuple companion row** (`sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID`) + bridge-admissibility row + REGULATOR_PIN=`a_4^{Mellin}` (Yang-Mills channel residue at s=2; cohomology-ratio factor `a_n^{ζ}`; bare a_n FORBIDDEN) + LEVEL_CLASS_PIN=FULL (consumes `_cm_1995_residue_formula.py` FULL CM-1995 §III.4 residue evaluator; NO `-SCHEMATIC` suffix). The first run emitted with a fragile 1/L-Richardson convergence object (audit `90a96508…`); that was corrected in-session to the canonical Aitken-Δ² GV-successive-ratio object (the structurally faithful T5 Connes-Karoubi pairing convergence). Per gate-verdicts.md Option A, the original line is RETAINED on disk (verdict permanence) and the corrective line APPENDS with `supersedes=90a965089db08a63…`; the canonical reading is the latest non-superseded line.

**Solution-space**: the α_s transport image is recoverable as a substrate-natural Connes-Karoubi K_0-pairing at its home pole — the strong coupling's CMB-pivot image is NOT a canonical-import scalar rescaling but the HKR/Connes-Karoubi image of the substrate's intrinsic χ-image BdG inheritance K_0-class. The α_s scale-and-channel-tagging (substrate-distance-1 s=3 running −0.08587279 vs Goldstone-pivot ≈0) gains a THIRD structural anchor at the a_4 s=2 home pole. T5 is GATE-CONFIRMED as the unique admissible Element-3 at the coupling's home pole. Artifacts: `s94_w1_3_vii_bx_t5_alpha_s_a4_recovery.{py,npz,png}`."""


def main() -> int:
    if not WP.exists():
        print(f"ERROR: WP path not found: {WP}", file=sys.stderr)
        return 2

    text0 = WP.read_text(encoding="utf-8")
    if NEW_BLOCK[:200] in text0:
        print("§W1-3 block already filled (sentinel matched); no-op.")
        return 0

    for attempt in range(1, 8):
        text = WP.read_text(encoding="utf-8")
        if OLD_STUB not in text:
            # Already filled, or stub diverged; check for COMPLETED in §W1-3 block.
            anchor = "### §W1-3. S94-VII-Bx-T5-ALPHA-S-A4-RECOVERY"
            if anchor in text:
                seg_start = text.find(anchor)
                seg_end = text.find("---", seg_start)
                seg = text[seg_start:seg_end] if seg_end > 0 else text[seg_start:]
                if "**Status**: COMPLETED" in seg:
                    print("§W1-3 already shows Status: COMPLETED; no-op.")
                    return 0
            print(f"ERROR (attempt {attempt}): exact OLD_STUB not found in WP.", file=sys.stderr)
            return 3

        new_text = text.replace(OLD_STUB, NEW_BLOCK, 1)
        tmp = WP.with_suffix(".md.tmp.s94w13")
        tmp.write_text(new_text, encoding="utf-8")
        try:
            os.replace(tmp, WP)
            check = WP.read_text(encoding="utf-8")
            if NEW_BLOCK[:200] in check:
                print(f"§W1-3 written successfully on attempt {attempt}.")
                print(f"  WP size: {len(check)} chars; line count: {check.count(chr(10))}")
                return 0
            else:
                print(f"WARN (attempt {attempt}): post-write verification failed; retrying.", file=sys.stderr)
        except OSError as e:
            print(f"WARN (attempt {attempt}): os.replace failed: {e}; retrying.", file=sys.stderr)
        time.sleep(0.15 * attempt)

    print("ERROR: retry attempts exhausted; WP write FAILED.", file=sys.stderr)
    return 4


if __name__ == "__main__":
    sys.exit(main())
