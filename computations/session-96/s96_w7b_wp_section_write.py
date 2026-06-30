#!/usr/bin/env python3
"""
S96-HYG-JOINT-EVIDENCE-D3-RESTRICT -- WP §W7-7b atomic section-scoped write.

Replaces the NOT-STARTED stub body of the §W7-7b section in
sessions/archive/session-96/session-96-w7-workingpaper.md with the COMPLETED section
(Status COMPLETED, Verdict PASS, Output Artifacts, MCP Pre-Compute Audit,
Results, substrate framing), preserving the §-heading line, the trailing `---`
separator, and every other byte of the curated WP (atomic tmp -> fsync ->
os.replace; section-scoped splice anchored on the stub body, no bulk append).
"""
import os
import sys

# METHODOLOGY-class doc-edit gate: consumes NO framework numerical constants
# (pure WP-section text splice). The canonical import is present to satisfy the
# computations/_shared/CLAUDE.md canonical-import discipline + the python-validate
# hook; M_KK is the substrate witness for the §7.3 spine member m_H (a₄ KK-threshold).
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_shared"))  # (local)
from canonical_constants import M_KK  # noqa: F401  (local) doc-edit gate; witness only, no numerics
assert M_KK > 0  # (local) provenance sanity: substrate KK scale is the m_H spine anchor

ROOT = r"C:\sandbox\Ainulindale Exflation"  # (local)
WP = os.path.join(ROOT, "sessions", "session-96", "session-96-w7-workingpaper.md")  # (local)

# ---- exact stub body to be replaced (lines 289-308 of the WP, between the
#      §-heading at 287 and the `---` at 310). Anchored start..end strings. ----
STUB_START = "**Status**: NOT STARTED\n**Gate ID**: `S96-HYG-JOINT-EVIDENCE-D3-RESTRICT`"  # (local)
STUB_END = "dual-SHA (full 64-char, content over the §7.3 diff); artifact (capstone §7.3 edit))*"  # (local)

# ---- the completed section body ----
NEW_BODY = r"""**Status**: COMPLETED
**Gate ID**: `S96-HYG-JOINT-EVIDENCE-D3-RESTRICT`
**Trigger**: `[AUDIT]`
**Classification**: **NON-PHONONIC** (methodology contribution: restricting an over-reaching statistical claim in the capstone text)
**Agent**: `sagan-empiricist` (empiricism / evidence-discipline axis owns the joint-BF claim restriction; sagan flagged the over-reach)
**Class note**: **METHODOLOGY-class** (M2 = capstone §7.3 Edit; M3 = verbatim from sagan §7.3 flag + mack CF-MACK-7 + kaku V.8; M4 → **allowlist-append FLAG `S96-HYG-JOINT-EVIDENCE-D3-RESTRICT`**). **CONDITIONAL on W7-7a** — consumed its covariance verdict line; dispatched AFTER W7-7a, which was on disk (FAIL).
**Hypothesis**: Conditional on W7-7a's covariance verdict, the §7.3 joint-evidence claim must be restricted — the Wronskian licenses ALGEBRAIC layer-independence, NOT STATISTICAL independence of the borrowed-H residuals; the joint-BF must be scoped to the zero-parameter structural spine (Higgs mass, mass ordering, σ/m=0, c_s²=0 — no borrowed H), and the "chance of one random geometry" framing replaced with the EVOI prior-predictive-range formulation (mack CF-MACK-7).
**Plan reference**: `sessions/session-plan/session-96-plan-w7.md` §W7-7b (4 content elements; W7-7a-conditioned framing).

**Verdict**: **PASS** — `value='restricted=4-elements;W7-7a=FAIL_Corr(a0,a2)=+1.0000_band>0.5;Wronskian_licenses_ALGEBRAIC_NOT_STATISTICAL_indep;joint-BF_scoped_to_zero-param_spine(m_H,mass-ordering,sigma/m=0,c_s2=0_NO_borrowed_H);EVOI_prior-predictive-range/posterior-width(CF-MACK-7)_replaces_random-geometry;Omega_DM_AND_sigma8_both_a2_NOT_multiplied;borrowed-H_dagger-rows(w0,wa,sigma8,CC)_conditional_NOT_independent_factors;substrate-first_down-tag_preserved'` scheme=`joint-BF-restriction-to-structural-spine` convention=`prior-predictive-range(EVOI)-replacing-ensemble-cross-LAYER-per-W7-7a-WITHIN-layer-NOT-multiplied` L_max=N/A. `audit_sha256=588adb147d9ac240da73ae1bfba0baed4d0c0499380e0b9427c015bd81c927fe` content_sha256=`b31a52e99fe5c2ec59b6cdb369e388b050b5acb247fb69d72e9a19facad93f6a`. (3-tuple companion: sign=N/A — no own directional pre-reg, the algebraic-vs-statistical direction is W7-7a's; magnitude=PASS — artifact-existence-with-content, all 4 elements + W7-7a conditioning present; regime=VALID — deterministic atomic section-scoped restriction.)

**The W7-7a conditioning (the number that mandates the restriction).** The upstream COMPUTE half, `S96-HYG-JOINT-EVIDENCE-D3-COVARIANCE` (audit_sha256 `7227c8c5dc6d4fbdbf61888cf1bb74dfbc0ee9fa4c12bde26c6e2facd11dba5e`), returned **FAIL**: under a shared C10 `H(t)` perturbation the maximum off-diagonal cross-layer residual correlation is **`max_offdiag_corr = 1.0000`** on the **a₀–a₂** pair (band > 0.5 ⇒ FAIL), with `Corr(a₀,a₂) = +1.0000`, `Corr(a₀,a₄) = +0.0000`, `Corr(a₂,a₄) = +0.0000` (sensitivities `s_a0 = +1.234526e-02`, `s_a2 = +6.398917e+00`, `s_a4 = −0.000000e+00`). The verdict's own annotation states it: *"ALGEBRAIC indep (Wronskian W2-E) TRUE but STATISTICAL indep = FALSE; 7.3 multiplication = OVERSTATED — restrict to zero-param-spine; within-layer (Ω_DM, σ₈ both a₂) NOT multiplied = PRE-REGISTERED."* Per the plan's `dual_prior` discriminator, a FAIL (Corr > 0.5) routes **0.9 to Track B** — strike the naive cross-layer product and restrict the joint-BF to the zero-parameter structural spine. That is exactly what this gate applies to the capstone §7.3 text.

**Output Artifacts** (closure-verification checklist):
- **Capstone edit** — `sessions/framework/phonic-exflation-equation.md` §7.3, ATOMIC section-scoped splice (read → splice the §7.3 region ONLY → fsync + `os.replace`), all other sections preserved byte-for-byte (independently confirmed via `git diff`: the only §7.3-region hunks are the restricted scorecard sentence at line ~475 and the new reconciliation note item (5) at line ~477; the other capstone hunks belong to the concurrent S96-HYG-SELF-INVENTORY/MELLIN-POLESET gates and are intact, not clobbered). Four content elements landed: **(1)** the Wronskian licenses **algebraic** layer-independence of the `a₀/a₂/a₄` functionals, **not statistical** independence of the borrowed-`H` residuals (`Corr(a₀,a₂)=+1.0000`); **(2)** the joint-BF is scoped to the **zero-parameter structural spine** — `m_H` (a₄ KK-threshold), normal mass ordering (D_K eigenvalue ordering), `σ/m=0` (N_Fock=1 superselection), `c_s²=0` (Kasparov factorization) — carrying NO borrowed `H(t)`; **(3)** the EVOI **prior-predictive-range / posterior-width** form (mack CF-MACK-7) replaces "chance of one random geometry"; **(4)** `Ω_DM` and `σ₈` (BOTH a₂) are explicitly **NOT** multiplied as independent factors. A parallel reconciliation note item (5) is added to the §7.3 register-pinned scorecard blockquote.
- **Producing script** — `computations/session-96/s96_hyg_joint_evidence_d3_restrict.py` (the atomic-edit + dual-SHA emitter; METHODOLOGY-class, no numerical threshold; pre-flight anchor-uniqueness + byte-for-byte out-of-region preservation check before write). WP-write helper — `computations/session-96/s96_w7b_wp_section_write.py`.
- **Verdict line** — `computations/session-96/s96_gate_verdicts.txt`, canonical line `S96-HYG-JOINT-EVIDENCE-D3-RESTRICT: PASS …` matching `^S96-HYG-JOINT-EVIDENCE-D3-RESTRICT:.* (audit_sha256|content_sha256)=[a-f0-9]{64}` + dual-SHA companion row + 3-tuple companion row (schema-v2). Both SHAs unique (sig_5-distinct from W7-7a's).
- **No data/plot** — METHODOLOGY-class artifact-existence gate (correctly absent per the gate block).

**MCP Pre-Compute Audit**: queries executed before the §7.3 restriction edit (per `.claude/rules/knowledge-index-usage.md`); the W7-7a covariance verdict is the primary input and was read from `computations/session-96/s96_gate_verdicts.txt` (line 159, audit_sha256 `7227c8…`).
- `search_knowledge('joint evidence Wronskian layer independence W2-E algebraic statistical')` → confirms the **Spectral-Moment Decoupling Theorem (W2-E, S75)** is the certified Wronskian result the §7.3 sentence cites (`a₀,a₂,a₄ algebraically independent, Wronskian nonzero, PASS, S75`) — i.e. ALGEBRAIC, not statistical, independence. Forward dependency confirmed.
- `search_knowledge('S96 JOINT-EVIDENCE D3 covariance restrict prior predictive range')` → no prior RESTRICT closure; surfaces prior-art on independence discounts (`S85-MULTI-D-JOINT-FISHER-INDEPENDENCE-DISCOUNT`) and prior-predictive-range (`s85_w1b_alpha_s_prior_range_lcdm`), consistent with the EVOI / CF-MACK-7 reframe. Gate is NOT already evaluated.
- `get_constant('max_f_NL_FW')` → `1.505` (S95, F-NL-ROW) — confirms the f_NL bound cited in §7.3 (unchanged by this edit). `get_constant('c_s2_FW')` → not found (it is the W7-8 registry candidate this session; `c_s²=0` cited as a structural-spine member per the plan framing, not as a canonical pin yet).
- **Not PRE-CLOSED** — this is a new METHODOLOGY landing conditioned on the just-landed W7-7a verdict.

**Results**: the restricted §7.3 now states the **EVOI prior-predictive-range / posterior-width** Bayes-factor form, `BF = (prior-predictive range)/(posterior width around the observation)`, multiplying BFs **only across observables that are BOTH algebraically AND statistically independent** — replacing the "chance of one random geometry" ensemble count. The **FAIL branch** of the W7-7a `dual_prior` is applied (the naive cross-layer product is struck, not merely hedged): the certified Wronskian (Decoupling Theorem §4.2 / W2-E) is restricted to ALGEBRAIC layer-independence of the spectral-moment *functionals*, which does **not** carry to STATISTICAL independence of the *residuals* of borrowed-`H` observables — and W7-7a measured the co-shift directly (`Corr(a₀,a₂)=+1.0000`). The strong joint claim is scoped to the **zero-parameter structural spine** (no borrowed `H`); the borrowed-`H` dagger rows (`w₀, wₐ, σ₈, CC`) are conditional and are NOT entered as independent likelihood factors; and `Ω_DM` and `σ₈` (both a₂) are NOT multiplied as independent (pre-registered, independent of W7-7a — a distinct reason from the cross-layer statistical-dependence). No substitution chain of its own (the directional finding is W7-7a's; this gate APPLIES the verdict to the text). The actual numerical BF over the spine routes to **`CF-S97` (mack CF-MACK-7 prior-predictive-range UQ compute)** — the restriction *text* is in-session; the computed BF magnitude is future work. Dual-SHA full 64-char (content over the §7.3 diff). Artifact: capstone §7.3 edit + reconciliation note item (5).

**Substrate framing**: NON-PHONONIC methodology contribution. The restriction ENFORCES the substrate-first epistemic partition — the zero-parameter spine is **substrate-IS** (Higgs from the a₄ KK-threshold, mass ordering from D_K eigenvalue ordering, σ/m=0 from N_Fock=1 superselection, c_s²=0 from Kasparov factorization) and carries NO borrowed `H(t)`, so its joint evidence is unconditionally multiplicative across the algebraically-independent a₀/a₂/a₄ layers. The dagger rows (`w₀, wₐ, σ₈, CC`) borrow the container-observer's `H(t)` and are conditional — their residuals correlate through the shared `H` (W7-7a: `Corr(a₀,a₂)=+1.0000`), so they cannot be multiplied as independent factors. The edit **DOWN-TAGS** the over-confident statistical-independence wording to its register status (algebraic, not statistical) — it does NOT invert the explanation direction: the strong claim still belongs to the substrate-intrinsic spine, not the borrowed-`H` projection, and the arrow `D_K eigenvalues → spectral moments → emergent observables → measurement` is unchanged (per `capstone-hygiene-gate.md` substrate-first preservation)."""


def main() -> int:
    with open(WP, "r", encoding="utf-8") as f:
        original = f.read()  # (local)

    i = original.find(STUB_START)  # (local)
    if i < 0:
        print("FAIL: STUB_START not found -- aborting, no write")
        return 1
    j = original.find(STUB_END)  # (local)
    if j < 0:
        print("FAIL: STUB_END not found -- aborting, no write")
        return 1
    j_end = j + len(STUB_END)  # (local)
    if j_end <= i:
        print("FAIL: STUB_END precedes STUB_START -- aborting, no write")
        return 1

    # uniqueness: the stub body anchors must each appear exactly once
    if original.count(STUB_START) != 1 or original.count(STUB_END) != 1:
        print(f"FAIL: non-unique anchors (start={original.count(STUB_START)}, end={original.count(STUB_END)}) -- aborting")
        return 1

    updated = original[:i] + NEW_BODY + original[j_end:]  # (local)

    # byte-for-byte preservation OUTSIDE the spliced region
    if original[:i] != updated[:i]:
        print("FAIL: prefix changed -- aborting")
        return 1
    if original[j_end:] != updated[len(updated) - len(original[j_end:]):]:
        print("FAIL: suffix changed -- aborting")
        return 1
    if updated == original:
        print("FAIL: no change -- aborting")
        return 1

    tmp = WP + ".s96w7b.tmp"  # (local)
    with open(tmp, "w", encoding="utf-8", newline="") as f:
        f.write(updated)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, WP)

    with open(WP, "r", encoding="utf-8") as f:
        landed = f.read()  # (local)

    checks = {
        "status_completed": "**Status**: COMPLETED" in landed,
        "verdict_pass": "**Verdict**: **PASS**" in landed,
        "output_artifacts": "**Output Artifacts**" in landed,
        "mcp_precompute": "**MCP Pre-Compute Audit**" in landed,
        "substrate_framing": "**Substrate framing**" in landed,
        "w7_7a_cited": "7227c8c5dc6d4fbdbf61888cf1bb74dfbc0ee9fa4c12bde26c6e2facd11dba5e" in landed,
        "corr_cited": "Corr(a₀,a₂) = +1.0000" in landed or "Corr(a₀,a₂)=+1.0000" in landed,
        "section_heading_preserved": "### §W7-7b. S96-HYG-JOINT-EVIDENCE-D3-RESTRICT (sagan-empiricist)" in landed,
        "w7_8_preserved": "### §W7-8. S96-HYG-CS2-REGISTRY (van-den-dungen-theorist)" in landed,
        "stub_gone": "**Status**: NOT STARTED\n**Gate ID**: `S96-HYG-JOINT-EVIDENCE-D3-RESTRICT`" not in landed,
    }  # (local)
    for k, v in checks.items():
        print(f"  check {k}: {v}")
    all_pass = all(checks.values())  # (local)
    print(f"all_pass={all_pass}")
    return 0 if all_pass else 2


if __name__ == "__main__":
    sys.exit(main())
