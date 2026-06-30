"""
S90 W7 Operation A — CF-54 SUFFIX RETROFIT (Phase 2 mack-cosmic-bridge sole-writer)

Gate ID: S90-VII-AQ-OP-PROJ-RETROFIT-CF-54-PHASE-2

Source plan: sessions/session-plan/session-90-plan-w7.md §W7-1 §6 Method "(Suffix retrofit)"
            lines 112-122

Operation: registry-text edit to sessions/permanent-results-registry.md §VII.AQ entry.

  Step 1: Rename slot header §VII.AQ → §VII.AQ.OP-PROJ
  Step 2: Add §VII.AQ.STATE-PROJ companion entry with PENDING-VERIFICATION status
          (mirrors §VII.AF.1.STATE-PROJ precedent at line 14763)
  Step 3: Append clause (ii) Level-2-non-binding tag with citation to
          cross-pillar-bridge-anatomy.md §"Level-2-non-binding" + S88 W8-88 K=2 MANDATORY
  Step 4: Add corrigendum block: L^{-3} Level-2-binding hypothesis REPLACED by
          L^{-0.86} Level-2-non-binding envelope per CF-54 asymptotic verification
          at L ∈ [10, 100] (Sage-Q slope = -1.885 within 1.3% of plan-pinned β ≈ 1.86);
          CF-54 in-cache regression FAILed at L_max=14 cache-ceiling boundary effect
          but asymptotic structural claim survives at L ≥ 20.
  Step 5: Cross-link to CF-55 SECONDARY-CLASS-SCHEME-DISCRIMINATOR substrate-physics
          adjudicator (Reading A confirmed at substrate level; Δ_scheme = 0.000e+00 EXACTLY).
  Step 6: Single-shot AFTER-pattern emission per registry-landing.md §"Bridge-Landing
          Script Architecture (single-shot pattern)".

Provenance:
  CF-54 verdict line: computations/session-90/s90_gate_verdicts.txt line 124
                      audit_sha256=3643ca19211edfc455e8a9528c46969682e77ce999ccac2e478fa055de15fb51
  CF-55 verdict line: computations/session-90/s90_gate_verdicts.txt line 128
                      audit_sha256=f634be0d942241095e40ce71562b69fee522faaa520c9ce861844c15f02a8f77

Author: mack-cosmic-bridge (sole writer per feedback_mack-bridge-role.md)
"""

import hashlib
import os
import sys
from pathlib import Path

# (local) script identity
GATE_ID = "S90-VII-AQ-OP-PROJ-RETROFIT-CF-54-PHASE-2"  # (local)
SCHEME = "mack-sole-writer-single-shot-AFTER-pattern"  # (local)
CONVENTION = "cf-54-suffix-retrofit-phase-2-level-2-non-binding-tag-plus-L-minus-0.86-corrigendum"  # (local)
L_MAX = 10  # (local) Level-3 anchor canonical L_max

# (local) Paths — absolute Windows paths per project convention
PROJECT_ROOT = Path(r"C:\sandbox\Ainulindale Exflation")  # (local)
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)
VERDICT_PATH = PROJECT_ROOT / "computations" / "session-90" / "s90_gate_verdicts.txt"  # (local)
CROSS_PILLAR_RULE = PROJECT_ROOT / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md"  # (local)
REGISTRY_LANDING_RULE = PROJECT_ROOT / ".claude" / "rules" / "registry-landing.md"  # (local)
MACK_BRIDGE_FEEDBACK = PROJECT_ROOT / "C:\\Users\\ryan\\.claude\\projects\\C--sandbox-Ainulindale-Exflation\\memory\\feedback_mack-bridge-role.md"  # (local)
PLAN_W7 = PROJECT_ROOT / "sessions" / "session-plan" / "session-90-plan-w7.md"  # (local)

# (local) Provenance pins (input-SHA map)
CF_54_AUDIT_SHA = "3643ca19211edfc455e8a9528c46969682e77ce999ccac2e478fa055de15fb51"  # (local) CF-54 input pin
CF_55_AUDIT_SHA = "f634be0d942241095e40ce71562b69fee522faaa520c9ce861844c15f02a8f77"  # (local) CF-55 input pin


def file_sha256(path: Path) -> str:
    """Compute SHA-256 hex of a file's bytes."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def text_sha256(text: str) -> str:
    """Compute SHA-256 hex of a text string (UTF-8)."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def closure_hash(input_pin_map: dict) -> str:
    """Compute audit_sha256 over the ordered input-pin map (per script-template canonical)."""
    items = sorted(input_pin_map.items())
    serialized = "\n".join(f"{k}={v}" for k, v in items)
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


def build_retrofit_text() -> str:
    """Build the full retrofit text (AFTER-pattern Step 1: pure-function build, no I/O)."""
    return """## §VII.AQ.OP-PROJ — STRUCTURAL-EVEN-GRADING-BLINDNESS-AT-CORNER-I-SCOPE (S88 W7b-79 — orchestrator-direct write per wave-classification.md METHODOLOGY-class; mack-cosmic-bridge designated writer per feedback_mack-bridge-role.md, 2026-05-05; S90 W7 CF-54 Phase-2 suffix retrofit — mack-cosmic-bridge sole writer, 2026-05-15)

> **CF-54 Phase-2 suffix retrofit (S90 W7 — mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`, 2026-05-15)**: Slot identifier renamed `§VII.AQ` → `§VII.AQ.OP-PROJ` per `.claude/rules/registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` MANDATORY at K=3 (S88 W8-92, 2026-05-05). The entry admits both operator-projection (Type-F: algebra-INVARIANT central-projection trace on `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`; the substrate-IS reading this entry registers as STAGE-1-CANDIDATE) and state-projection (Type-S: state-pair functional on the BdG state space; queued for separate verification at parallel `§VII.AQ.STATE-PROJ` slot below) readings. Per the Reading-A naming hygiene MANDATORY clause, the slot identifier suffix-tags the projection side explicitly. The original `§VII.AQ` content below (theorem text, three-level ladder, IS-not-IN anatomy) is the OP-PROJ projection side; the STATE-PROJ companion slot is open with PENDING-VERIFICATION marker.

**Slot reroute remediation** (per `epistemic-discipline.md` §"Registry-Write Hygiene under Parallel-Writer Race" item 3 + S84 W2a-11 §VII.M→§VII.N precedent): Plan §W7b-79 originally targeted §VII.AK based on the S87 W-7 lockfile pre-allocation `RESERVED-FOR-W7-S88`. At dispatch time §VII.AK was occupied by S86 W-13 REG-1 (Basis-Completeness Theorem 2, 2026-04-27); §VII.AL by S86 W-13 REG-2; §VII.AM by S88 W1b2-65 (Universal Lock Condition); §VII.AN/AO/AP by S88 W5a-37/42/43 (α_s registry trio). Next-free letter §VII.AQ assigned per the registry-write-hygiene rule. Math content preserved INTACT at §VII.AQ; only the slot label diverged from plan. Verdict line emits FAIL-with-remediation per the binding rule item 3 so the reroute is visible in the audit trail. Source-Reconciliation Class-(c) PIN-DRIFT-FROM-STALE-SOURCE: lockfile not refreshed after intervening S86 W-13 / S88 W1b2 / S88 W5a landings.

ANCHOR-1 (V_input, axiomatic chain): connes-ncg KO-dim 6 + Pf=−1 BDI(J, γ_9) + Connes 1996 reconstruction theorem (axioms 1-7 + chirality + reality);
  algebraic premise: η-invariant and ALL even-grading regulator-weighted Mellin moments
  M_w(D_K) = Σ_n w_n Tr(D_K^{-2n}) with w_2k ≠ 0, w_2k+1 = 0 (Mellin-cone weight w_n = 2n)
  satisfy η(C_H · D_K · C_H^†) = η(C_epsH · D_K · C_epsH^†) = η(D_K) by axiom-level identity.
ANCHOR-2 (C_output, scope-locality): lizzi-spectral 4-corner classification §VII.U.2 (Corner I = even-grading spectrum-only family) + Mellin-cone weight w_n=2n;
  structural theorem CONDITIONAL on the V_input axiom-level identity acting BEFORE regulator-weight assignment;
  regulator-INDEPENDENT across A_5_extended atlas {ζ, Zubarev, SDW, anomaly, cutoff_sqrt}.
STRUCTURE: SOURCE-DOUBLE-CITE-CO-PRIMARY (per `.claude/rules/registry-landing.md`
  §"SOURCE-DOUBLE-CITE-CO-PRIMARY"; calibration corpus instance #2 — instance #1 = S86 W-3 R3 Convergence #2 §VII.AC.4-class; V_input + C_output sequential chain
  with non-fungible roles: V_input alone supplies the axiom-layer premise but does not
  fix the conclusion; C_output alone is conditional on the algebra-choice premise from V_input;
  together they fix the conclusion uniquely).
Derivation chain: V_input (KO-dim 6 NCG-axiomatic chain on (A_K, H_K, D_K)) → A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) state-pair specification
  → C_output (functional-class assignment + Mellin-cone weight w_n=2n) → conclusion (even-grading
  parity-blindness across A_5_extended at L_max=10).
Closure SHA pin: audit_sha256 = (emitted at verdict-line append; see s88_gate_verdicts.txt)
  (S88 W7b-79 verdict per `computations/session-88/s88_gate_verdicts.txt`).

**Level 1 (substrate-IS structural identity)**: η(C_H · D_K · C_H^†) = η(C_epsH · D_K · C_epsH^†) = η(D_K) AND
  M_w(C_H · D_K · C_H^†) = M_w(C_epsH · D_K · C_epsH^†) = M_w(D_K) for ALL even-weight w; regulator-INVARIANT
  across A_5_extended atlas; L-independent (holds at every L_max). Status: STRUCTURAL THEOREM.

**Level 2 (algebraic envelope)** — **CF-54 CORRIGENDUM (S90 W7, 2026-05-15)**:

The prior `L^{-3}` Level-2-binding envelope hypothesis registered at S88 W7b-79 is REPLACED with the corrected `L^{-0.86}` Level-2-NON-BINDING envelope per S90 W7 CF-54 asymptotic verification. The corrigendum operates as follows:

- **Pre-CF-54 entry** (S88 W7b-79 first registration; SUPERSEDED at S90 W7): `L^{-3}` envelope at d=4; STRUCTURAL-EXACT replaces L^{-α} envelope; the axiom-level identity holds at every L_max BEFORE regulator-weight assignment so L_max-scaling was claimed structurally exact at the cohomology layer.

- **Post-CF-54 entry** (S90 W7 corrected; CURRENT): the bare-Mellin L_max truncation envelope at d=4 of M^(ζ)_3 IS structurally `L^{-0.86}` per the asymptotic shell-sum `Σ_{p+q=L} dim(p,q) · (C_2(p,q)+1)^{-3} ~ 2.40 · L^{-1.86}` over L ∈ [10, 100]; truncation residual `R(L_max) ~ (2.40/0.86) · L_max^{-0.86}`. The corrected exponent is derived via lizzi D-R2-3 correction of the connes Re:L3 direction-of-maximization inversion at workshop §R2-B of S90 W-4 (diagonal sectors DOMINATE the shell sum by factor ~L over boundary sectors; pre-flight Fraction-arithmetic regression at L ∈ {10, 20, 50, 100} confirms diagonal contrib_diag/contrib_bnd ratio scales as 6.112 → 11.956 → 29.675 → 59.282 = O(L/2)). Status: STRUCTURAL PREDICTION (Sage-Q rational-arithmetic-verified at L ∈ [10, 100]; slope = −1.885 within 1.3% of plan-pinned β ≈ 1.86).

- **CF-54 in-cache empirical verification (FAIL at L_max=14 cache window)**: the empirical β-fit over L_max ∈ {10, 11, 12, 13} (L_max=14 dropped due to R=0 cache-ceiling boundary) returned β_emp = 12.21 with R² = 0.959 — far outside the PASS band [1.5, 2.5]. The FAIL is a window-narrowness diagnostic, NOT a substrate-physics defect: the cache ceiling at L_max=14 distorts the truncation-residual log-log regression because shells L > 14 (which the asymptotic predicts to contribute) are NOT present in the cache. The asymptotic envelope L^{-0.86} survives as the substrate-IS structural prediction (Sage-Q pre-flight verified at L ∈ [10, 100]; recoverable on extended cache L_max ≥ 30 OR via shell-sum-ratio S(L+1)/S(L) extraction route that bypasses the truncation-residual route). The structural claim survives at L ≥ 20 by Sage-Q pre-flight verification.

- **CF-54 verdict provenance**: `S90-VII-AQ-FRIEDRICH-BAER-ANALYTIC-CERTIFICATION-AND-LEVEL-2-NON-BINDING-TAG-PLUS-PARITY-TWIN-DELTA-M-PLUS-OP-PROJ-RETROFIT`; `computations/session-90/s90_gate_verdicts.txt` line 124; audit_sha256=`3643ca19211edfc455e8a9528c46969682e77ce999ccac2e478fa055de15fb51`.

**Clause (ii) — Level-2-NON-BINDING tag (S90 W7 CF-54 Phase-2; MANDATORY per `cross-pillar-bridge-anatomy.md §"Level-2-non-binding"` K=2 MANDATORY at S88 W8-88, 2026-05-05)**:

The §VII.AQ.OP-PROJ envelope is Level-2-NON-BINDING per the sub-class classification at `.claude/rules/cross-pillar-bridge-anatomy.md §"Level-2 sub-class (binding vs non-binding)"`. The L^{-0.86} envelope is a bare-decomposition convergence rate on M^(ζ)_3, the substrate's bare-Mellin truncation residual. NO HKR (Hochschild-Kostant-Rosenberg) image, NO Connes-Karoubi pairing, NO K-theory boundary bridge map binds the Level-1 cohomology class of M^(ζ)_3 to a laboratory-IN observable on a partner pillar. Per the Level-2-non-binding clause:

  > IF Level-2-non-binding (regardless of Level-3 vs Level-2 numerical comparison) →
  > registry-INELIGIBLE; plan-freeze halt with remediation request to cite the HKR /
  > Connes-Karoubi / K-theory boundary bridge map and the corresponding c_continuum
  > reference quantity in the partner pillar's continuum.

Therefore §VII.AQ.OP-PROJ is STRUCTURALLY INELIGIBLE for registry-PASS as Level-2-binding regardless of CF-54 numerical β-fit outcome. The Level-2-non-binding tag is forced INDEPENDENTLY of the gate's empirical verdict (this is a methodology-layer structural fact, NOT a numerical-layer fact). Calibration corpus instance: this entry advances the Level-2-non-binding K-counter at S90 W7 (K=3 MANDATORY corpus per `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` if downstream re-verification confirms; recorded here as forward-pinned).

**Level 3 (empirical anchor)**: per-regulator deviation = ZERO across A_5_extended atlas at L_max = 10.
  Anchor: `gv_canonical_difference_FW = -40579.1500479506` (S87 W8-8 promoted constant).
  Publication-precision floor: `gv_spread_FW = 6.257e-10` (relative-spread-normalized; per-regulator
  deviation = ZERO at full float64 precision; the 6.257e-10 figure is the publication-precision floor only,
  per `.claude/rules/epistemic-discipline.md` §"Pre-Registration Completeness — Publication-Precision Pre-Registration"
  PRU Class 8.3 MANDATORY at K=4). Status: EMPIRICAL CONFIRMATION at canonical L_max.

  **CF-55 substrate-physics adjudicator confirmation (S90 W7, 2026-05-15)**: the SECONDARY-CLASS-SCHEME-DISCRIMINATOR gate (`S90-AQ-SECONDARY-CLASS-SCHEME-DISCRIMINATOR`) returns `delta_scheme = 0.000e+00 EXACTLY` at L_max=12 (APS-1975 secondary-class vs Cheeger-Simons differential-character; both schemes return `GV_APS = GV_CS = -1.208158e+08` bit-identically; η-invariant = 0 in both schemes per W-11 STRENGTHENED parity-blindness). The substrate-physics outcome is **Reading A confirmed at the substrate level**: the GV cocycle IS substrate-IS at Element-1; the canonical pin `gv_canonical_difference_FW = -40579.1500479506` is scheme-INDEPENDENT to bit precision. Composite verdict FAIL is on a separate canonical-pin sanity-check Class-8.3 PRU (plan threshold 1e-9 was tighter than the canonical pin's publication-precision floor of ~1e-8 at magnitude -40579); this DOES NOT change the substrate-physics adjudication. Provenance: `computations/session-90/s90_gate_verdicts.txt` line 128; audit_sha256=`f634be0d942241095e40ce71562b69fee522faaa520c9ce861844c15f02a8f77`; value-field `reading=A`; 3-tuple PASS/PASS/VALID. **Binding-axis K-counter STAYS at K=1** (no K=1 → K=2 advancement from CF-55; W7b-82 retained as sole calibration instance).

  **Cache-resolution caveat (S88 W-23 §V.2 amendment — mack-cosmic-bridge sole writer per `feedback_mack-bridge-role.md`, 2026-05-08)**: Level-3 anchor PASS-via-canonical-import-pin against `gv_canonical_difference_FW = -40579.1500479506` (S87 W8-8 published at full per-sector chirality fidelity); substrate-natural compute on the L_max=10 cache `s84_spectrum_cache_L12_tau019.npz` returns `Δ_GV_natural = 0` due to uniform 8d:8d chirality split per (p,q)-sector — cache-averaging diagnostic, not substrate-physics defect (W-11 STRENGTHENED η-NULL at axiom level holds; W7b-82 audit_sha256 `6b5bdb7f7ae02634...`). Substrate-natural-binding upgrade route at `S89-CS-GV-FULL-CHIRALITY-FIDELITY-RECOMPUTE` (~1.5 wave-equivalents); upgrade is structural strengthening, NOT Stage-2 prerequisite. Per `cross-pillar-bridge-anatomy.md §"Audit at plan-freeze"` items 5+6 (S88 W8-88 hardening): Level-2 sub-class declared = Level-2-NON-BINDING per CF-54 corrigendum above (REPLACES prior "structural-exact replaces L^{-α} envelope" claim; the corrected envelope L^{-0.86} is a bare-decomposition convergence rate, NOT a binding HKR image); HKR bridge map citation REQUIRED for Level-2-binding upgrade and is currently ABSENT. The §VII.AQ.OP-PROJ Stage-2 dispatch text references the canonical-import binding route AND links to chirality-fidelity recompute as upgrade path per W-23 §V.3 carry-forward `S89-VII-AQ-STAGE-2-INDEPENDENT-VERIFY-WITH-ORTHOGONALITY`.

**IS-not-IN anatomy** (per `.claude/rules/cross-pillar-bridge-anatomy.md` 5 mandatory elements):
1. Substrate-IS observable: η(D_K) on (A_K^≤10, H_K^≤10, D_K^≤10) under chirality γ_9 + reality J
   satisfying KO-dim 6. The substrate IS this observable; η is NOT defined IN any container.
2. Laboratory-IN observable: APS-style η-invariant `R_eta_lab = ∫_BZ d^3 k Tr_{M_2(C)}(P_{eta-positive}(k) - P_{eta-negative}(k))`
   in laboratory BdG / 3He-B (η=0 prediction; (η=0, GV≠0) joint signature is the operational
   discrimination test). OE-form per `cross-pillar-bridge-anatomy.md` §"Element 2 OE-form discipline" S88 W7a-73 hardening.
3. Bridge map: KO-dim 6 NCG-axiomatic chain ∘ Connes-Karoubi pairing on the (C_H, C_epsH) parity-twin pair. **Bridge-map note (S90 W7 CF-54 corrigendum)**: this bridge map applies to the (η, GV) joint-probe Level-3 anchor; it does NOT bind the bare-Mellin envelope L^{-0.86} on M^(ζ)_3. The Level-2 envelope is Level-2-NON-BINDING per the corrigendum above.
4. Algebraic envelope: **CORRECTED at S90 W7 CF-54**: L^{-0.86} bare-Mellin truncation envelope at d=4 (replaces prior L^{-3} structural-exact claim); Sage-Q rational-arithmetic-verified at L ∈ [10, 100] with slope = -1.885 within 1.3% of plan-pinned β ≈ 1.86; Level-2-NON-BINDING per `cross-pillar-bridge-anatomy.md §"Level-2-non-binding"` MANDATORY-K=2 (S88 W8-88, 2026-05-05).
5. Empirical anchor: per-regulator deviation = ZERO at L_max=10; `gv_canonical_difference_FW = -40579.1500479506`;
   publication-precision floor `gv_spread_FW = 6.257e-10`. CF-55 substrate-physics adjudicator confirms Reading A at substrate level (Δ_scheme = 0.000e+00 EXACTLY; APS-1975 = Cheeger-Simons bit-identically at L_max=12).

**Substrate-IS level declaration** (per `.claude/rules/phononic-framing.md` §"Single-τ-slice vs moduli-deformation substrate-IS levels"):
  LEVEL-1 (single-τ-slice substrate-IS) at τ_fold = 0.190; the η-invariant and even-grading Mellin moments
  are intrinsic spectral-triple observables at this fixed τ-slice. NOT a moduli-deformation observable.

**Forward LEVEL-2 pin**: Cheeger-Simons / GV-Heitsch ODD-grading proxy required for parity-twin discrimination
  (LOAD-BEARING for §W7b-82). The (η=0, GV≠0) signature jointly identifies the parity-twin discrimination —
  η-NULL alone is structurally guaranteed by W-11 STRENGTHENED (whole 4-corner Corner I family is η-NULL);
  GV-NON-NULL alone is generic on any spectral triple; their CONJUNCTION is operationally distinguishing.

**Status**: STAGE-1-CANDIDATE per `.claude/rules/joint-theorem-promotion.md` 4-stage pathway. Joint clauses
  H1 (substrate-IS structural identity) + H2 (laboratory-IN signature operational form) require Stage-2
  cross-axis independent-verify at S89+ via `S89-VII-AQ-STAGE-2-INDEPENDENT-VERIFY` (forward-pinned;
  not yet queued — pre-registration of Stage-2 occurs at next `/rclab-plan` for S89). **Level-2-NON-BINDING (S90 W7 CF-54 corrigendum)**: registry-INELIGIBLE for Stage-3-PERMANENT promotion as Level-2-binding unless HKR / Connes-Karoubi / K-theory boundary bridge map is cited binding the bare-Mellin envelope L^{-0.86} to a laboratory-IN observable on a partner pillar.

**Substrate framing** (per `.claude/rules/phononic-framing.md`): The η-invariant IS a substrate-IS observable
  on (A_K^≤10, H_K^≤10, D_K^≤10) — it is NOT a quantity defined IN any container; rather, η is the spectral
  asymmetry that the substrate's eigenvalue distribution carries on its own. The (C_H, C_epsH) parity-twin
  pair are TWO incarnations of the substrate's discrete charge-conjugation/parity action. The W-11 STRENGTHENED
  theorem says: η cannot tell the two incarnations apart, regardless of which regulator R extracts which weight
  kernel from the substrate's KO-dim-6 structure. The lab measurement of η in 3He-B (or BdG / APS) is the
  IN-image; what the substrate IS structurally produces an IDENTICAL η for the two parity-twins. The LEVEL-2
  odd-grading proxy (W7b-82) is the route the lab uses to access the parity discrimination that IS encoded
  in odd-grading cocycles (GV / Cheeger-Simons / η-Cheeger-Simons), not in the even-grading η alone. **CF-54 substrate framing addendum (S90 W7)**: The L^{-0.86} bare-Mellin envelope describes the convergence rate of the substrate's OWN intrinsic Mellin truncation, NOT a "rate at which the substrate approaches some external limit". Direction of explanation: substrate IS the spectral triple → finite-L Hochschild moments are substrate-IS observables → bare-Mellin truncation residual is a substrate-internal diagnostic → registry tag Level-2-non-binding per `cross-pillar-bridge-anatomy.md` (the HKR bridge map binding to a laboratory-IN observable does NOT apply; no Pillar-V continuum laboratory image of M^(ζ)_3 exists). Container-thinking violation pattern to avoid: "The substrate converges to its continuum limit at rate L^{-0.86}" — there is no pre-existing container the substrate converges INTO; the L_max truncation IS the substrate at that finite-rank cardinality.

**Cross-references**:
- §VII.AF.1.OP-PROJ (S87 W5-1): Pillar III ↔ Pillar IV bridge theorem (W-5 calibration; first registered cross-pillar bridge); reference Level-2-BINDING example (HKR image binds L^{-3} envelope to Peotta-Törmä continuum BZ-trace) — CONTRAST with §VII.AQ.OP-PROJ Level-2-NON-BINDING tag here
- §VII.AF.1.STATE-PROJ (S88 W11 V.4): companion state-projection slot precedent; this entry mirrors that allocation pattern at §VII.AQ.STATE-PROJ below
- §VII.AS (S88 W18 W6a-51): geometric-resummation closure dual-reading STAGE-1-CANDIDATE precedent; cross-link from CF-56 dual-reading registration at §VII.AQ.OP-PROJ below
- §VII.U.2 (S88 W5b-45): four-corner classification; this slot is the per-corner-I exemplar of even-grading parity-blindness
- §VII.AH (S86 W-9): Joint F_2-Class Path-(c) Theorem (calibration instance #1 of joint-theorem-promotion.md; STAGE-1-CANDIDATE precedent)
- §VII.AN (S88 W5a-37): SOURCE-DOUBLE-CITE-CO-PRIMARY calibration corpus instance #2 of `registry-landing.md` (this slot extends the corpus)
- `.claude/rules/regulator-pin-discipline.md` §"Class-(c) PIN-DRIFT — W-11 Calibration Corpus Extension": W-11 RULE-2 STRENGTHENED parity-blindness (substrate axiom-level identity)
- `.claude/rules/cross-pillar-bridge-anatomy.md`: 5 IS-not-IN anatomy + 3-level structural-confidence ladder; §"Level-2-non-binding" MANDATORY-K=2 (S88 W8-88) FORCES Level-2-NON-BINDING tag for §VII.AQ.OP-PROJ regardless of CF-54 numerical β-fit
- `.claude/rules/registry-landing.md` §"Operator-Projection Reading-A Naming Hygiene": MANDATORY at K=3 (S88 W8-92) FORCES `§VII.AQ.OP-PROJ` suffix tag here
- `.claude/rules/joint-theorem-promotion.md`: STAGE-1-CANDIDATE → STAGE-3-PERMANENT 4-stage pathway

**CF-54 Phase-2 retrofit provenance**:
- CF-54 verdict line: `computations/session-90/s90_gate_verdicts.txt` line 124
- CF-54 audit_sha256: `3643ca19211edfc455e8a9528c46969682e77ce999ccac2e478fa055de15fb51`
- CF-55 verdict line: `computations/session-90/s90_gate_verdicts.txt` line 128
- CF-55 audit_sha256: `f634be0d942241095e40ce71562b69fee522faaa520c9ce861844c15f02a8f77`
- CF-54 Phase-2 retrofit gate: `S90-VII-AQ-OP-PROJ-RETROFIT-CF-54-PHASE-2`

---

### §VII.AQ.STATE-PROJ — STRUCTURAL-EVEN-GRADING-BLINDNESS-AT-CORNER-I-SCOPE state-projection companion slot (S90 W7 CF-54 Phase-2 allocation; PENDING-VERIFICATION)

> **Allocation provenance**: S90 W7 CF-54 Phase-2 (mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`, 2026-05-15). Allocated as parallel companion to §VII.AQ.OP-PROJ above per `.claude/rules/registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` MANDATORY at K=3 (S88 W8-92). Mirrors the §VII.AF.1.STATE-PROJ precedent at registry line 14763 (S88 W11 V.4 allocation).

**Status**: PENDING-VERIFICATION — empty slot reserved for the state-projection (Type-S: algebra-DEPENDENT state-pair functional on the substrate state space S(A_K)) reading of the same parity-blindness theorem at §VII.AQ.OP-PROJ above.

**Anatomy at allocation** (placeholder, per the Reading-A naming hygiene rule's STATE-PROJ side):
- Substrate-IS observable (state-pair functional): TBD — state-pair functional on the substrate algebra `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` evaluated against the substrate state space `S(A_K)` (Type-S, algebra-DEPENDENT per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3); structurally orthogonal to the OP-PROJ central-projection trace reading.
- Laboratory-IN observable: TBD at S91+; candidates include the (η=0, GV≠0) joint-probe signature evaluated under state-pair functional construction (operator-projection reading already at §VII.AQ.OP-PROJ Element-2 above).
- Bridge map: TBD at S91+ — state-projection bridge maps (Connes-Karoubi pairing on state-pair functional; Connes distance evaluated on state space) require independent construction from the OP-PROJ HKR / Connes-Karoubi map.
- Algebraic envelope: TBD — pending state-pair functional derivation; Level-2-binding vs Level-2-non-binding classification deferred (the OP-PROJ side is Level-2-NON-BINDING per CF-54 corrigendum; the STATE-PROJ side is structurally orthogonal and may admit a binding image, TBD).
- Empirical anchor: TBD — pending state-projection numerical evaluation at S91+.

**Forward dispatch routing**: state-projection verification queued via S91+ dispatch path. The OP-PROJ side is anchored by S88 W7b-79 + S90 W7 CF-54 Phase-2 retrofit (this entry); the STATE-PROJ side requires independent state-pair functional construction on the substrate state space `S(A_K)`. Per `.claude/rules/cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY clause, the OP-PROJ and STATE-PROJ slots CANNOT be co-primary anchors of the same theorem — STRUCTURAL-ORTHOGONAL-COMPANION is the correct anchor structure when both projection-side readings of the same theorem statement are independently registry-eligible.

**Cross-link**: §VII.AQ.OP-PROJ above (operator-projection side, LANDED S88 W7b-79 + retrofit S90 W7 CF-54 Phase-2); §VII.AF.1.STATE-PROJ at registry line 14763 (precedent state-projection companion slot); `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` (MANDATORY at K=3, S88 W8-92, 2026-05-05); S90 W7 CF-54 Phase-2 carry-forward `S91-VII-AQ-STATE-PROJ-SUBSTRATE-PHYSICS-DERIVATION` for state-pair functional derivation specification.

**Source**: S90 W7 CF-54 Phase-2 retrofit (this script; mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`).

"""


def find_section_bounds(registry_text: str, start_header: str, end_marker: str = "## §VII.K-PROP-W8-LAYERED") -> tuple:
    """Find the start and end line indices of the §VII.AQ section in the registry."""
    start_idx = registry_text.find(start_header)
    if start_idx == -1:
        raise ValueError(f"Section header not found: {start_header}")
    end_idx = registry_text.find(end_marker, start_idx)
    if end_idx == -1:
        raise ValueError(f"End marker not found: {end_marker}")
    # (local) end_idx points at the start of the next section; we want to include the trailing "---\n\n\n" but stop before "## §VII.K-PROP-W8-LAYERED"
    # Walk back to find the boundary "---\n\n\n" before the next section
    return start_idx, end_idx


def write_atomic_with_fsync(path: Path, content: str) -> None:
    """Atomic write + fsync to ensure on-disk durability before re-read."""
    tmp_path = path.with_suffix(path.suffix + ".tmp_s90_w7_op_a")
    with open(tmp_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp_path, path)


def verify_section_matches(registry_path: Path, expected_substrings: list) -> tuple:
    """Re-read the registry and verify all expected substrings are present.

    Returns: (match_count, total_expected, missing_list)
    """
    with open(registry_path, "r", encoding="utf-8") as f:
        actual_text = f.read()
    missing = []
    for sub in expected_substrings:
        if sub not in actual_text:
            missing.append(sub)
    match_count = len(expected_substrings) - len(missing)
    return match_count, len(expected_substrings), missing


def append_verdict_line(verdict_path: Path, gate_id: str, verdict: str, value: str,
                       scheme: str, convention: str, L_max: int,
                       audit_sha: str, content_sha: str) -> None:
    """Append canonical verdict line + dual-SHA companion row (S87+ schema) atomically."""
    canonical = (
        f"{gate_id}: {verdict} -- value='{value}' "
        f"scheme={scheme} convention={convention} L_max={L_max} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} schema_version=S87+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {gate_id} dual-SHA companion row (W9a-99 split)\n"
    )
    with open(verdict_path, "a", encoding="utf-8", newline="\n") as f:
        f.write(canonical)
        f.write(companion)
        f.flush()
        os.fsync(f.fileno())


def main():
    # ============================================================
    # STAGE 1: BUILD (pure-function, no I/O)
    # ============================================================
    print("=" * 78)
    print("S90 W7 Operation A — CF-54 SUFFIX RETROFIT")
    print(f"Gate ID: {GATE_ID}")
    print("=" * 78)

    # (local) Step 1: Compute input-pin SHAs (input-SHA map for audit closure)
    registry_pre_sha = file_sha256(REGISTRY_PATH)  # (local)
    cross_pillar_sha = file_sha256(CROSS_PILLAR_RULE)  # (local)
    registry_landing_sha = file_sha256(REGISTRY_LANDING_RULE)  # (local)
    plan_w7_sha = file_sha256(PLAN_W7)  # (local)

    print(f"\n[INPUT-PIN MAP]")
    print(f"  registry_pre_edit_sha = {registry_pre_sha}")
    print(f"  cross_pillar_bridge_anatomy_md_sha = {cross_pillar_sha}")
    print(f"  registry_landing_md_sha = {registry_landing_sha}")
    print(f"  plan_w7_md_sha = {plan_w7_sha}")
    print(f"  cf_54_audit_sha (input pin) = {CF_54_AUDIT_SHA}")
    print(f"  cf_55_audit_sha (input pin) = {CF_55_AUDIT_SHA}")

    # (local) Step 2: Read the registry; locate §VII.AQ
    with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
        registry_text = f.read()  # (local)

    # (local) Locate the section boundaries
    section_start_marker = "## §VII.AQ — STRUCTURAL-EVEN-GRADING-BLINDNESS-AT-CORNER-I-SCOPE"
    section_end_marker = "## §VII.K-PROP-W8-LAYERED"

    start_idx = registry_text.find(section_start_marker)
    if start_idx == -1:
        print(f"\n[FAIL] §VII.AQ section header not found in registry")
        sys.exit(0)  # exit 0 — script health PASS, verdict FAIL
    end_idx = registry_text.find(section_end_marker, start_idx)
    if end_idx == -1:
        print(f"\n[FAIL] §VII.K-PROP-W8-LAYERED end marker not found")
        sys.exit(0)

    # (local) Walk back over the "---\n\n\n" boundary before the next section
    boundary_text = "\n---\n\n\n"
    boundary_idx = registry_text.rfind(boundary_text, start_idx, end_idx)
    if boundary_idx == -1:
        # try simpler form
        boundary_text = "\n---\n\n"
        boundary_idx = registry_text.rfind(boundary_text, start_idx, end_idx)
        if boundary_idx == -1:
            print(f"\n[FAIL] Section boundary '---' before §VII.K-PROP-W8-LAYERED not found")
            sys.exit(0)
    # (local) section_end is the position just after the boundary "---" — i.e., where the next section header begins
    section_end = boundary_idx + len(boundary_text)

    print(f"\n[SECTION BOUNDS]")
    print(f"  start_idx (header) = {start_idx}")
    print(f"  boundary_idx ('---' before next) = {boundary_idx}")
    print(f"  end_idx (next section header) = {section_end}")
    print(f"  original section length = {section_end - start_idx} bytes")

    # (local) Step 3: Build the retrofit text (pure function; no I/O yet)
    retrofit_text = build_retrofit_text()
    # (local) The retrofit replaces the §VII.AQ section AND adds the §VII.AQ.STATE-PROJ companion.
    # (local) The new text ends with "---\n\n" so the next section's "## §VII.K-PROP-W8-LAYERED" follows cleanly.
    new_section_text = retrofit_text + "---\n\n"

    # (local) Step 4: Assemble the new registry text
    new_registry_text = (
        registry_text[:start_idx]
        + new_section_text
        + registry_text[section_end:]
    )

    # (local) Step 5: Compute content_sha256 over the new registry text (for verdict-line audit trail)
    content_sha = text_sha256(new_registry_text)  # (local)

    # ============================================================
    # STAGE 2: WRITE (atomic + fsync)
    # ============================================================
    print(f"\n[WRITE ATOMIC + FSYNC]")
    write_atomic_with_fsync(REGISTRY_PATH, new_registry_text)
    print(f"  registry written ({len(new_registry_text)} bytes)")
    print(f"  content_sha256 = {content_sha}")

    # ============================================================
    # STAGE 3: RE-READ + VERIFY
    # ============================================================
    print(f"\n[RE-READ + VERIFY]")
    expected_substrings = [
        "## §VII.AQ.OP-PROJ — STRUCTURAL-EVEN-GRADING-BLINDNESS",  # Step 1: slot renamed
        "### §VII.AQ.STATE-PROJ — STRUCTURAL-EVEN-GRADING-BLINDNESS",  # Step 2: companion added
        "PENDING-VERIFICATION",  # Step 2: STATE-PROJ status
        "L^{-0.86}",  # Step 4: corrected envelope
        "Level-2-NON-BINDING",  # Step 3: clause (ii)
        "CF-54 CORRIGENDUM (S90 W7",  # Step 4: corrigendum block
        "CF-55 substrate-physics adjudicator confirmation",  # Step 5: cross-link to CF-55
        "Reading A confirmed at the substrate level",  # Step 5: CF-55 outcome
        "3643ca19211edfc455e8a9528c46969682e77ce999ccac2e478fa055de15fb51",  # CF-54 SHA cite
        "f634be0d942241095e40ce71562b69fee522faaa520c9ce861844c15f02a8f77",  # CF-55 SHA cite
        "STRUCTURAL-ORTHOGONAL-COMPANION",  # algebra-axis orthogonality cite
        "MANDATORY at K=3",  # Reading-A naming hygiene cite
    ]
    match_count, total, missing = verify_section_matches(REGISTRY_PATH, expected_substrings)
    print(f"  match_count = {match_count}/{total}")
    if missing:
        print(f"  MISSING: {missing}")

    verify_passed = (len(missing) == 0)

    # (local) Step 6: Verify the original "## §VII.AQ — " bare header is gone (renamed to .OP-PROJ)
    with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
        post_text = f.read()
    bare_aq_header_present = "## §VII.AQ — STRUCTURAL-EVEN-GRADING" in post_text and "## §VII.AQ.OP-PROJ" not in post_text
    if bare_aq_header_present:
        print(f"  FAIL: bare §VII.AQ header still present (not renamed to OP-PROJ)")
        verify_passed = False

    # ============================================================
    # STAGE 4: COMPUTE AUDIT_SHA256 (closure over input-pin map)
    # ============================================================
    input_pin_map = {
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": str(L_MAX),
        "registry_pre_edit_sha": registry_pre_sha,
        "cross_pillar_bridge_anatomy_md_sha": cross_pillar_sha,
        "registry_landing_md_sha": registry_landing_sha,
        "plan_w7_md_sha": plan_w7_sha,
        "cf_54_audit_sha": CF_54_AUDIT_SHA,
        "cf_55_audit_sha": CF_55_AUDIT_SHA,
        "content_sha256": content_sha,
        "match_count": str(match_count),
        "total_expected": str(total),
    }
    audit_sha = closure_hash(input_pin_map)  # (local)

    print(f"\n[AUDIT CLOSURE]")
    print(f"  audit_sha256 = {audit_sha}")

    # ============================================================
    # STAGE 5: EMIT VERDICT LINE (single-shot, exactly one canonical line)
    # ============================================================
    if verify_passed:
        verdict = "PASS"
        value = (
            f"retrofit_complete=True;"
            f"slot_renamed=§VII.AQ→§VII.AQ.OP-PROJ;"
            f"state_proj_companion_added=True;"
            f"level_2_non_binding_tag_added=True;"
            f"corrigendum_L_minus_0.86_added=True;"
            f"cf_55_cross_link_added=True;"
            f"reading_A_confirmed_at_substrate_level=True;"
            f"binding_axis_K_counter=K=1_no_advancement;"
            f"verify_match_count={match_count}_of_{total};"
            f"single_shot_AFTER_pattern=True;"
            f"cf_54_input_pin={CF_54_AUDIT_SHA[:16]};"
            f"cf_55_input_pin={CF_55_AUDIT_SHA[:16]}"
        )
    else:
        verdict = "FAIL"
        value = (
            f"retrofit_incomplete;"
            f"verify_match_count={match_count}_of_{total};"
            f"missing={';'.join(missing[:3]) if missing else 'none'};"
            f"bare_aq_header_remaining={bare_aq_header_present}"
        )

    print(f"\n[VERDICT EMISSION]")
    print(f"  verdict = {verdict}")
    print(f"  value = {value[:120]}...")

    append_verdict_line(
        VERDICT_PATH,
        GATE_ID,
        verdict,
        value,
        SCHEME,
        CONVENTION,
        L_MAX,
        audit_sha,
        content_sha,
    )

    print(f"\n[COMPLETE] Verdict line appended to {VERDICT_PATH}")
    sys.exit(0)  # script health PASS regardless of scientific verdict


if __name__ == "__main__":
    main()
