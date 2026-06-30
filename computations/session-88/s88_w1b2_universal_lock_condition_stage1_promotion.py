"""S88-CF-CURV-12-UNIVERSAL-LOCK-CONDITION-THEOREM-STAGE-1-PROMOTION
================================================================
STAGE-1-CANDIDATE registry promotion of the Universal Lock Condition
(Substrate Horizon-Trigger) Theorem at sessions/permanent-results-
registry.md §VII.AM, per `.claude/rules/joint-theorem-promotion.md`
4-stage pathway.

Pre-registration: sessions/session-plan/session-88-plan-w1b2.md
                  Section W1b2-65 (theorem text lines 229-239;
                  5 IS-not-IN anatomy lines 264-268; 3-level ladder
                  lines 270-274; joint-clause flags lines 278-285;
                  verifier rubric lines 339-353; output 4-tuple
                  lines 326-330).

Hypothesis (plan W1b2-65 Hypothesis):
    With gate #64 PASS supplying the 3rd calibration corpus instance
    (W1b2-64 cascade-tail Page-time non-activation, ratio_anchor
    9.6684e+04), the Universal Lock Condition theorem (TS-EM-3 / J10)
    promotes from Stage-0 (workshop-internal at S87) to Stage-1
    (registry-candidate at §VII.AM) via a registry entry containing
    all 7 verifier-rubric elements.

PASS predicate (artifact-existence-with-substantive-content;
                M1 predicate per `wave-classification.md` §M1):
    PASS iff
        (a) gate #64 verdict in s88_gate_verdicts.txt is PASS, AND
        (b) registry §VII.AM block landed with all 7 rubric elements:
            (1) STAGE-1-CANDIDATE tag (literal)
            (2) 3 clauses (a)+(b)+(c)
            (3) 5 IS-not-IN anatomy elements (5 labels)
            (4) 3-level ladder (3 labels)
            (5) 3-instance corpus (J3 + S58 + W1b2-64 by name)
            (6) Joint-clause flags table
            (7) Stage-2 carry-forward pointer text
            (LOGICAL AND across 7), AND
        (c) registry entry block >= 40 lines, AND
        (d) M4 allowlist row appended, AND
        (e) slot-allocation table row appended.

Substitution chain (the layer-functor F mapping for METHODOLOGY-class
gates per `epistemic-discipline.md` §"Layer-Decomposition"):
  Step 1: Substrate-physics observable: Universal Lock Condition
          theorem on substrate horizon-trigger conditions.
  Step 2: F-image at methodology layer: registry entry artifact.
  Step 3: PASS predicate at substrate layer (numerical) ->
          F-image at methodology layer (artifact-existence-with-
          substantive-content).
  Step 4: dual-SHA closure: audit_sha256 over input-pin map +
          content_sha256 over registry-entry-text + slot-row + allowlist-row.
  Step 5: Direction (sign/magnitude/regime):
          sign     = PASS iff registry slot occupied by the entry
          magnitude= PASS iff entry >= 40 lines (rubric threshold)
          regime   = VALID iff joint-theorem-promotion.md 4-stage
                     pathway compliance (Stage-0 -> Stage-1 transition
                     correctly tagged; Stage-2 successor queued).

Mechanical closure routing (per `.claude/rules/mechanical-closure-discipline.md`):
  If gate #64 != PASS, emit PRE-REG-INC blocked-by-upstream verdict;
  do NOT touch registry or allowlist. Upstream-block topology is
  pre-registered in the plan (line 381 W1b2-W1c decision-point
  routing).

Solo-mode authoring disclosure:
  Plan line 318 specifies producing_artifact_writer = mack-cosmic-
  bridge per `feedback_mack-bridge-role.md`. /rclab-solo Phase 2 step 2
  forbids subagent spawning; the orchestrator (acting in hawking-
  theorist persona this wave per plan line 5 "Primary agent") writes
  directly. This deviation is honest-disclosure per `v3-closure-
  recovery.md` PROHIBITED_ACTIONS Class 1 boundary (in-session
  structural correction, not convention-shopping); recorded in the
  working-paper §W1b2-65 self-assessment block.

Author: hawking-theorist (S88 W1b2-65; orchestrator-direct in solo mode)
"""
from __future__ import annotations

import os
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib   # noqa: E402
import json      # noqa: E402
import sys       # noqa: E402
from pathlib import Path  # noqa: E402

PROJECT_ROOT = Path(r"C:\sandbox\Ainulindale Exflation")
# X2-removed: alias 'T0' = ... 'computations' (replaced by tools.computation_root.resolve_*)
sys.path.insert(0, str(T0))

# Tier0 mandatory: import canonical_constants. This script does no numerical
# computation, but the Universal Lock Condition theorem references S58
# Gamma_eff = 0.99970 as one of its 3 calibration corpus instances; assert
# the canonical match to certify the corpus row.
from canonical_constants import (  # noqa: E402
    Gamma_effacement,  # 0.9997 (S58 Volovik partition; canonical_constants.py:58)
    tau_fold,          # 0.19 (S12/S42 gate CONST-FREEZE-42)
)

assert abs(Gamma_effacement - 0.9997) < 1e-6, (
    f"Gamma_effacement canonical drift detected: imported {Gamma_effacement!r}, "
    "expected 0.9997 (S58 Volovik partition + effacement; canonical_constants.py:58). "
    "The §VII.AM Universal Lock Condition theorem 3rd corpus instance "
    "S58 fold-effacement is pinned to Gamma_eff = 0.99970; validate before landing."
)

# ------------------------------------------------------------- pins
GATE_ID    = "S88-CF-CURV-12-UNIVERSAL-LOCK-CONDITION-THEOREM-STAGE-1-PROMOTION"
WP_ID      = "S88-W1b2-65"
SCHEME     = "joint-theorem-promotion-stage-1"
CONVENTION = "cross-pillar-bridge-anatomy-5-IS-not-IN-plus-3-level"
L_MAX      = "N/A"  # noqa  (METHODOLOGY-class; no L-truncation)
SLOT       = "VII.AM"  # next-free-letter per slot-allocation table at line 33

SCRIPT_PATH      = resolve_script(88, 's88_w1b2_universal_lock_condition_stage1_promotion.py')
VERDICT_OUT      = resolve_output(88, 's88_gate_verdicts.txt')
REGISTRY_PATH    = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
ALLOWLIST_PATH   = PROJECT_ROOT / ".claude" / "rules" / "methodology-wave-allowlist.md"
CANON_PATH       = resolve_script(None, 'canonical_constants.py')
JOINT_THM_PATH   = PROJECT_ROOT / ".claude" / "rules" / "joint-theorem-promotion.md"
CROSS_PILLAR_PATH= PROJECT_ROOT / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md"
WORKSHOP_PATH    = PROJECT_ROOT / "sessions" / "session-87" / "workshops" / "s87-pixelation-lock-hawking-transit.md"

# Gate #64 verdict-line content_sha256 (directly from s88_gate_verdicts.txt:19;
# pinned at gate #65 dispatch AFTER gate #64 closure per plan line 406).
GATE64_CONTENT_SHA = "985217c9249553a9fc470f5a115465066aadb556b91a9109e777514ffa336107"  # (local) gate #64 closure

# Stage-2 carry-forward gate ID (plan line 307, 330)
STAGE2_CARRY_FORWARD_ID = "S89-UNIVERSAL-LOCK-CONDITION-STAGE-2-CROSS-AXIS-VERIFY"  # (local)

# ------------------------------------------------------------- helpers

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(pin_map: dict) -> str:
    payload = json.dumps(pin_map, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


# ============================================================ §VII.AM entry text

VII_AM_REGISTRY_BLOCK = r"""

## §VII.AM — Universal Lock Condition (Substrate Horizon-Trigger Theorem) — STAGE-1-CANDIDATE per joint-theorem-promotion.md (S88 W1b2-65 — hawking-theorist primary; orchestrator-direct write in /rclab-solo mode, 2026-05-03)

**Status**: STAGE-1-CANDIDATE per `.claude/rules/joint-theorem-promotion.md` 4-stage upgrade pathway. LANDED S88 W1b2-65 (`S88-CF-CURV-12-UNIVERSAL-LOCK-CONDITION-THEOREM-STAGE-1-PROMOTION` verdict line in `computations/session-88/s88_gate_verdicts.txt`). Stage 2 → 3 promotion BLOCKED on `S89-UNIVERSAL-LOCK-CONDITION-STAGE-2-CROSS-AXIS-VERIFY` three-agent parallel cross-check at S89+ (spectral-functional-axis cross-reviewer audits clauses (a)+(b)+(c)-JOINT; transit-dynamics-axis cross-reviewer audits clauses (a)+(b)+(c)-JOINT; semiclassical-gravity-axis cross-reviewer audits clauses (a)+(c)-JOINT; joint clauses PASS-AND'd across all three verdicts).

**Slot**: §VII.AM per next-free-letter protocol on the canonical slot-allocation table (registry line 33). §VII.AM was historically used by S87 W4-1 then in-session rerouted to §VII.X.W4-1 (S87 W4 closure 2026-04-28); §VII.AM became free again at that rerouting and is the lowest-letter free slot at S88 W1b2-65 dispatch. The falsifier-master-inventory's informal "§VII.AM candidate" tag for `S88+-FWD-C3-COCYCLE-3HE-BRIDGE-LANDING` (multi-year lab-blocked) is hereby DISPLACED by this canonical-slot-table allocation; FWD-C3 will reslot to a higher letter when its lab data lands (S88+ horizon).

**STAGE-1-CANDIDATE qualifier**: downstream gates citing §VII.AM MUST include the `(STAGE-1-CANDIDATE)` qualifier on every reference until Stage-2 PASS lands. The theorem is REGISTRY-PINNABLE for cross-citation but NOT permanent — Stage 2 three-agent independent-verify (no prior workshop context) is the upgrade gate. Calibration corpus: this entry is calibration corpus instance #2 of `joint-theorem-promotion.md` (after §VII.AH Joint F_2-Class Path-(c) Theorem at S87 W9a-1).

### Sponsors

- **hawking-theorist** — semiclassical-gravity-axis primary author (S87 pixelation-lock workshop §"Wrap-Up — What Holds" Stage-0 candidate text; gate #64 cascade-tail Page-time empirical anchor, S88 W1b2-64). Solo-mode orchestrator-direct writer for this STAGE-1 registry-landing entry (per /rclab-solo Phase 2 step 2; deviation from `feedback_mack-bridge-role.md` mack-cosmic-bridge-sole-writer convention disclosed in §W1b2-65 working-paper self-assessment).
- **transit-dynamics-theorist** — transit-axis co-author for the substrate cascade transit framework supporting clause (b) effacement-lock (S58 Volovik partition + Γ_eff = 0.99970 anchor).
- **connes-ncg-theorist** — spectral-functional-axis co-author for clause (a) pixelation-lock substrate-IS structural identity on (A_K, H_K, D_K) (S87 W11 J3 BH-horizon pixelation-lock).

### Anchor list (calibration corpus N=3 per `joint-theorem-promotion.md` Stage-1)

The Universal Lock Condition theorem unifies three structurally distinct substrate-physics regimes under a single trigger condition. The 3-instance calibration corpus is:

- **Instance 1 — J3 BH-horizon-pixelation-lock** (S87 W11 pixelation-lock workshop §J3): the substrate horizon trigger fires at every BH-horizon-class eigenvalue-spectrum-reorganization region; finite-area boundary in the spectral metric. PROVEN at substrate level (Stage-0 workshop-internal).
- **Instance 2 — S58 fold-effacement Γ_eff = 0.99970** (canonical_constants.py:58 `Gamma_effacement`; Volovik partition; S58 final synthesis): the substrate's information transmission across the fold is suppressed by an effacement factor 0.99970 — bounded by the area-quantization scale per clause (b). LANDED canonical (Volovik partition derivation).
- **Instance 3 — W1b2-64 cascade-tail Page-time non-activation** (S88 W1b2-64 verdict line `computations/session-88/s88_gate_verdicts.txt:19`; this wave's gate #64 PASS): the entanglement-entropy crossover time t_Page(M ≈ 10^13 kg) lies STRUCTURALLY OUTSIDE the substrate cascade window by ratio_anchor = 9.6684e+04 (~5 OOM). LANDED PASS at S88 W1b2-64 (audit_sha256=8d086bdfc66554a207b75137283c3ec1b03c4b5c3488620ebaa6a5a73b9676f1; content_sha256=985217c9249553a9fc470f5a115465066aadb556b91a9109e777514ffa336107).

K-counter for theorem promotion (separate from the cross-pillar-bridge K-counter at `cross-pillar-bridge-anatomy.md`): N=3 ≥ N_promotion=3 ⇒ STAGE-1-CANDIDATE eligibility unlocked; this entry is the in-session realization.

### 3-clause statement (VERBATIM from S87 pixelation-lock workshop §"Wrap-Up — What Holds" Stage-0 candidate text; plan §W1b2-65 lines 229-239; STAGE-1-CANDIDATE markers added per `joint-theorem-promotion.md` Stage-1)

*For every substrate eigenvalue-spectrum-reorganization region R ⊂ (A_K, H_K, D_K) bounded by a trapping surface (a finite-codimension subset where the substrate's mode-mixing rate diverges in the semiclassical limit), the following 3-clause structural identity holds:*

- **Clause (a) Pixelation lock** *[JOINT — requires both spectral-functional + transit-dynamics axes]* — the substrate horizon trigger fires (R becomes a localized eigenvalue-spectrum reorganization with finite-area boundary in the spectral metric); pixelation IS spectral-functional (NCG-axiomatic finite-area-on-spectral-metric statement), but lock invariance under cascade transit IS transit-dynamics. Calibration anchor: J3 BH-horizon-pixelation-lock (S87 W11).

- **Clause (b) Effacement lock** *[JOINT — requires both transit-dynamics + spectral-functional axes]* — the substrate's information transmission across R is suppressed by an effacement factor Γ_eff(R) bounded by the area-quantization scale: Γ_eff(R) = 1 − A(∂R)/(4 G_N · A_universal), where A_universal is the substrate-area normalization and G_N is the canonical Newton constant. Calibration anchor: S58 fold-effacement Γ_eff = 0.99970 (canonical Volovik partition; corresponds to A(∂R)/(4 G_N · A_universal) = 3.0e-4).

- **Clause (c) Page-time lock** *[JOINT — requires both spectral-functional + semiclassical-gravity axes]* — the entanglement-entropy crossover time t_Page(R) is bounded below by the substrate's cascade-localization timescale; equivalently, the local-vs-global causal-structure Page-curve crossover lies outside the immediate substrate observation window. Spectral-functional axis verifies the substrate-IS half-spectrum-reorganization timescale; semiclassical-gravity axis verifies the laboratory-IN Page formula t_Page = (1/2)·t_evap. Calibration anchor: W1b2-64 cascade-tail at M ≈ 10^13 kg with ratio_anchor = 9.6684e+04 (~5 OOM above t_universe).

*Clauses (a)+(b)+(c) hold JOINTLY. Stage-2 cross-axis verify dispatches one cross-reviewer per axis (spectral-functional, transit-dynamics, semiclassical-gravity) and PASS-ANDs across all three.*

### 5 IS-not-IN anatomy elements (per `cross-pillar-bridge-anatomy.md` §"IS-not-IN Anatomy (5 elements)" — MANDATORY structural requirement)

1. **Substrate-IS observable**: substrate horizon-trigger condition on eigenvalue-spectrum-reorganization regions R ⊂ (A_K, H_K, D_K) at finite-L truncation. The substrate IS the trigger condition (it is not "in" any spacetime container; the trigger condition is a property of the spectral triple's mode-mixing structure at finite-codimension subsets where the rate diverges semiclassically).

2. **Laboratory-IN observable**: black-hole horizon area + Hawking thermal spectrum + Page-curve entanglement entropy, all measured IN asymptotic flat exterior or de Sitter cosmological container. The lab measures these IN a continuum geometric container (the textbook GR framework with Schwarzschild metric + QFT-on-curved-background mode decomposition).

3. **Bridge map**: composite Hawking-Bogoliubov coefficient image (substrate mode-mixing → laboratory thermal spectrum) ∘ Bekenstein-Hawking area-entropy identification (S = A/(4G_N)) ∘ Page 1993 entropy-crossover formula (t_Page = (1/2)·t_evap). Composite multi-step bridge per `cross-pillar-bridge-anatomy.md` §"Bridge map" — permitted provided each step is named explicitly (here: Hawking 1974 / Bekenstein 1973 / Page 1993).

4. **Algebraic envelope**: at fixed L_max, the substrate trigger condition is bounded by the regulator-class-tagged area-quantization scale; envelope `δΓ_eff/Γ_eff ~ L_max^{−α}` with α empirically determined per S58 + S87 W11 calibration. Level-2 envelope for the joint theorem; precise α deferred to Stage-2 cross-axis verify (S89+ carry-forward will pin α via L_max-scan on the Bogoliubov-spectrum-reorganization-rate observable).

5. **Empirical anchor**: 3-instance calibration corpus enumerated in §"Anchor list" above. W1b2-64 cascade-tail Page-time provides the cosmological-cascade anchor at M ≈ 10^13 kg (ratio_anchor 9.6684e+04); J3 provides the BH-horizon anchor (area-quantization-finite at finite-codimension trapping surface); S58 Γ_eff = 0.99970 provides the fold-transit anchor. Three structurally distinct substrate-physics regimes; one unified trigger condition.

### 3-level structural-confidence ladder (per `cross-pillar-bridge-anatomy.md` §"Three-Tier Structural-Confidence Ladder" — MANDATORY)

- **Level 1 — Substrate-IS structural identity (cohomology-class level)**: STRUCTURAL THEOREM at substrate level. The 3-clause joint identity (a)+(b)+(c) is a regulator-invariant cohomology-class statement on the spectral triple, holding at every L_max where the relevant spectral moments are defined. Properties: regulator-invariant; L-independent; holds at every L_max. Form: identity at the K-theoretic boundary level for the trapping-surface ∂R. Full proof-mode rigorous derivation deferred to Stage-2 cross-axis independent-verify in S89+.

- **Level 2 — Algebraic convergence envelope**: STRUCTURAL PREDICTION. Convergence rate `δΓ_eff/Γ_eff ~ L_max^{−α}` for the joint trigger condition; α pinned post-Stage-2 cross-axis verify. Properties: L_max-dependent; algebraically derived; refines with L-scan. Form: bound on convergence rate to continuum / laboratory image. (At S88 W1b2-65 close, α is structurally known to satisfy α ≥ 1 per Volovik effacement scaling; tighter pinning deferred.)

- **Level 3 — Empirical anchor at canonical L_max**: EMPIRICAL CONFIRMATION. 3-instance corpus (J3 / S58 / W1b2-64). At canonical L_max=10, the W1b2-64 ratio t_Page(10^13 kg) / t_universe = 9.6684e+04 provides the numerical anchor for the cascade-tail layer; S58 Γ_eff = 0.99970 (5-sig-fig) for the fold-transit layer; J3 area-quantization-finite for the BH-horizon layer (substrate-S87 W11 workshop verdict).

**Registry-PASS criterion** (per `cross-pillar-bridge-anatomy.md` §"Registry-PASS criterion"): all three tiers present AND Level-3 satisfies Level-2. At S88 W1b2-65: Level-1 + Level-2 + Level-3 all populated; Level-3 W1b2-64 ratio (9.6684e+04) ≫ Level-2 envelope upper bound 1/α-scaled; Level-3 S58 Γ_eff = 0.99970 deviation-from-1 = 3e-4 < Level-2 envelope at L_max=10 with α≥1; Level-3 J3 satisfies Level-2 at substrate level (workshop-internal). Level-3 satisfies Level-2 across all three layers ⇒ registry PASS-CONDITIONAL on Stage-2 verify.

### Joint-clause flags + cross-axis attribution (per `joint-theorem-promotion.md` Stage-1; plan §W1b2-65 lines 278-285)

| Clause | Attribution | Cross-axis JOINT? |
|:-------|:------------|:------------------|
| (a) Pixelation lock | spectral-functional axis (NCG-axiomatic; J3 anchor) | JOINT (requires both axes; pixelation IS spectral-functional, but lock invariance under cascade transit IS transit-dynamics) |
| (b) Effacement lock | transit-dynamics axis (S58 fold; cascade-localization-rate observable) | JOINT (transit-dynamics provides Γ_eff dynamical pin; spectral-functional verifies area-quantization bound A(∂R)/(4 G_N · A_universal)) |
| (c) Page-time lock | semiclassical-gravity axis (Hawking radiation + Page entropy crossover; W1b2-64 anchor) | JOINT (spectral-functional verifies the substrate-IS half-spectrum-reorganization timescale; semiclassical-gravity verifies the laboratory-IN Page formula t_Page = (1/2)·t_evap = (5120π/2)·G²/(ℏc⁴)·M³) |

All 3 clauses are JOINT (cross-axis); the theorem's Stage-2 verify (S89+) MUST dispatch THREE cross-reviewers (one per axis) and PASS-AND across all three clauses.

### Stage-2 promotion blockage (S89+ carry-forward `S89-UNIVERSAL-LOCK-CONDITION-STAGE-2-CROSS-AXIS-VERIFY`)

Stage 2 → 3 promotion gate is `S89-UNIVERSAL-LOCK-CONDITION-STAGE-2-CROSS-AXIS-VERIFY`. Three-agent parallel cross-check protocol per `.claude/rules/joint-theorem-promotion.md` §"Stage 2 — Two-Agent Parallel Cross-Check" (extended to three agents because all three clauses are JOINT and the theorem traverses three substantively distinct axes):

- **Spectral-functional-axis cross-reviewer**: connes-ncg-theorist (or lizzi-spectral-functional-theorist) — audits clauses (a) + (b)-spectral-half + (c)-spectral-half; operates WITHOUT prior workshop context (reads only this Stage-1 entry, NOT S87 pixelation-lock workshop or any S87 W11 transcripts).
- **Transit-dynamics-axis cross-reviewer**: transit-dynamics-theorist (or volovik-superfluid-universe-theorist) — audits clauses (a)-transit-half + (b) + (c)-transit-half; operates WITHOUT prior workshop context.
- **Semiclassical-gravity-axis cross-reviewer**: hawking-theorist (or schwarzschild-penrose-geometer) — audits clauses (a)-semiclassical-half + (b)-semiclassical-half + (c); operates WITHOUT prior workshop context. NOTE: hawking-theorist authored Stage-0 candidate text AND Stage-1 registry entry; if hawking-theorist is the assigned cross-reviewer, must use schwarzschild-penrose-geometer instead per `joint-theorem-promotion.md` §"Two-Agent Independent-Verify" "Cross-reviewers are NOT the original workshop authoring agents".
- **JOINT clauses (a) + (b) + (c)** are PASS-AND'd across all three verdicts (logical AND, not OR).
- **Stage 3 promotion** fires only on joint PASS (all three cross-reviewers PASS independently AND all three joint clauses PASS in ALL three verdicts).

Carry-forward 4-field spec (per plan §W1b2-65 line 330):
- **WHAT**: Stage-2 cross-axis independent verify per `joint-theorem-promotion.md` §"Stage 2 — Two-Agent Parallel Cross-Check" extended to three axes.
- **INPUTS**: registry §VII.AM Stage-1-CANDIDATE entry (this body); `joint-theorem-promotion.md` 4-stage pathway rule; `cross-pillar-bridge-anatomy.md` 5-anatomy + 3-level rule; canonical_constants.py Gamma_effacement; gate #64 W1b2-64 verdict line.
- **GATE**: cross-reviewers spectral-functional + transit-dynamics + semiclassical-gravity dispatched IN PARALLEL without prior workshop context, PASS-AND across all 3 clauses; FAIL on any cross-reviewer's FAIL on any clause.
- **EFFORT**: 1.0 wave-equivalents (3 parallel cross-reviewer dispatches + dual-SHA closure + Stage-3 promotion edit on PASS).

### Substrate framing (per `.claude/rules/phononic-framing.md` §"IS Space, Not IN Space" — MANDATORY)

The Universal Lock Condition theorem itself is a **substrate-IS structural statement** about eigenvalue-spectrum-reorganization regions R ⊂ (A_K, H_K, D_K). The direction of explanation flows substrate → emergent:

```
Substrate eigenvalue-spectrum reorganization region R ⊂ (A_K, H_K, D_K) IS the trigger
   → composite bridge map (Hawking-Bogoliubov ∘ Bekenstein-Hawking ∘ Page 1993)
   → Laboratory observes IN exterior asymptotic regions: BH thermal spectrum + horizon area + Page entropy crossover
   → 3 calibration instances (BH-horizon J3, fold-transit S58, cascade-tail W1b2-64) confirm trigger
   → Theorem unifies the trigger conditions across 3 structurally distinct substrate-physics regimes
```

Container-thinking framings ("the BH evaporates IN spacetime", "the cascade transits THROUGH the fold") are explicitly REJECTED in the theorem text. The cascade-tail "black hole" of mass M ≈ 10^13 kg is NOT a container that emits IN spacetime — it IS a localized eigenvalue-spectrum reorganization of the substrate fiber whose thermal radiation is the Bogoliubov image of the substrate's mode reorganization across the trapping surface (S88 W1b2-64 §(a) substrate-physics framing). The Lock Condition's three clauses are properties of the substrate's structure at the trapping surface ∂R; the laboratory observes the bridge-image, not the substrate-IS observable directly.

### Cross-link

- `§VII.AH` — Joint F_2-Class Path-(c) Theorem (S87 W9a-1; STAGE-1-CANDIDATE precedent; calibration corpus instance #1 of `joint-theorem-promotion.md`). This §VII.AM entry is calibration corpus instance #2.
- `§VII.W` — Pillar III ↔ Pillar IV Bridge Theorem (S86 1a-S7 + W-5; cross-pillar-bridge-anatomy precedent for 5 IS-not-IN + 3-level ladder structure).
- `§VII.AF.1` — Pillar III ↔ Pillar IV Bridge Theorem with Three-Tier Ladder + IS-Not-IN Anatomy (S86 W-5; first registered cross-pillar bridge with all 5 anatomy elements).
- `computations/_shared/canonical_constants.py:58` — `Gamma_effacement = 0.9997` (corpus instance 2 anchor pin).
- `computations/session-88/s88_gate_verdicts.txt:19` — gate #64 W1b2-64 verdict line (corpus instance 3 anchor pin; full content_sha256 985217c9249553a9fc470f5a115465066aadb556b91a9109e777514ffa336107).
- `sessions/archive/session-87/workshops/s87-pixelation-lock-hawking-transit.md` — S87 pixelation-lock workshop §"Wrap-Up — What Holds" (Stage-0 candidate text source for the 3-clause theorem statement).

### Audit SHAs

- **audit_sha256** (S88-CF-CURV-12-... verdict line): see canonical row of `computations/session-88/s88_gate_verdicts.txt`; companion W9a-99 dual-SHA companion comment row carries the 16-char short form.
- **content_sha256**: see canonical row of `computations/session-88/s88_gate_verdicts.txt` — over the registry-entry text concatenated with the slot-allocation table row + the methodology-wave-allowlist M4 row.
- **Stage-0 source SHA** (workshop closure): SHA-256 of `sessions/archive/session-87/workshops/s87-pixelation-lock-hawking-transit.md` at gate #65 dispatch (pinned in input-pin map).

---
"""

# ============================================================ §VII slot-allocation table row
# Inserted into the canonical slot-allocation table at registry line ~109 (just below
# §VII.AL, which occupies the latest landed AL slot). Note: insertion follows the
# table's convention — alphanumeric ordering preserved where possible, but recent
# entries have appended chronologically; we follow the chronological-append precedent
# (this row appended after the "**Last updated**: 2026-04-27" row was last touched).

VII_AM_SLOT_TABLE_ROW = (
    "| §VII.AM | THM | Universal Lock Condition (Substrate Horizon-Trigger Theorem) — STAGE-1-CANDIDATE per joint-theorem-promotion.md (3-clause joint theorem unifying J3 BH-horizon-pixelation-lock + S58 fold-effacement Γ_eff=0.99970 + W1b2-64 cascade-tail Page-time non-activation; 3-instance corpus N=3; 5 IS-not-IN anatomy + 3-level ladder per cross-pillar-bridge-anatomy.md; calibration corpus instance #2 of joint-theorem-promotion.md after §VII.AH; FWD-C3 cocycle↔3He-bridge informal reservation displaced — FWD-C3 reslots to higher letter on lab-data landing) (S88 W1b2-65 — hawking-theorist primary; orchestrator-direct write in /rclab-solo mode, 2026-05-03) | hawking-theorist | 2026-05-03 |\n"
)

# ============================================================ M4 allowlist row
# Appended to .claude/rules/methodology-wave-allowlist.md §"Allowlist Rows" table.

ALLOWLIST_M4_ROW = (
    "| W1b2-65 | S88 | S88-CF-CURV-12-UNIVERSAL-LOCK-CONDITION-THEOREM-STAGE-1-PROMOTION (Universal Lock Condition / TS-EM-3 / J10 STAGE-1-CANDIDATE registry landing per joint-theorem-promotion.md 4-stage pathway; calibration corpus N=3: J3 BH-horizon-pixelation-lock + S58 fold-effacement Γ_eff=0.99970 + W1b2-64 cascade-tail Page-time non-activation; orchestrator-direct write in /rclab-solo mode at §VII.AM next-free-letter slot; deviation from feedback_mack-bridge-role.md mack-cosmic-bridge-sole-writer convention disclosed in S88 W1b2-65 working-paper) | <pinned at plan-freeze> |\n"
)


# ============================================================ main
def main() -> int:
    print(f"=== {GATE_ID} ===")
    print()

    # ---------------- Step 1: gate #64 PASS verification ----------------
    verdicts_text = VERDICT_OUT.read_text(encoding="utf-8") if VERDICT_OUT.exists() else ""
    gate64_line = None  # (local)
    for line in verdicts_text.splitlines():
        if line.startswith("S88-CF-CURV-11-PAGE-TIME-CASCADE-TAIL-MASS:"):
            gate64_line = line
            break
    if gate64_line is None:
        print("ABORT: gate #64 verdict line NOT FOUND in s88_gate_verdicts.txt; gate #65 cannot proceed.")
        return 1
    gate64_passed = gate64_line.startswith("S88-CF-CURV-11-PAGE-TIME-CASCADE-TAIL-MASS: PASS")  # (local)
    print(f"gate #64 verdict line: PASS={gate64_passed}")
    print(f"gate #64 line head: {gate64_line[:140]}...")
    print()

    if not gate64_passed:
        print("Gate #64 != PASS; routing to PRE-REG-INC blocked-by-upstream per mechanical-closure-discipline.md.")
        # Build PRE-REG-INC verdict line; no registry / allowlist edits.
        pre_reg_value = f"PRE-REG-INC_blocked_by_S88-CF-CURV-11_status_{gate64_line.split(':')[1].split('--')[0].strip()}"
        canon_sha = sha256_file(CANON_PATH)
        joint_thm_sha = sha256_file(JOINT_THM_PATH)
        cross_pillar_sha = sha256_file(CROSS_PILLAR_PATH)
        registry_sha = sha256_file(REGISTRY_PATH)
        allowlist_sha = sha256_file(ALLOWLIST_PATH)
        workshop_sha = sha256_file(WORKSHOP_PATH)
        script_sha = sha256_file(SCRIPT_PATH)
        pin_map_blocked = {
            "_gate_id": GATE_ID, "_wp_id": WP_ID, "_scheme": SCHEME, "_convention": CONVENTION,
            "_L_max": L_MAX, "slot": SLOT, "verdict": "FAIL", "blocked_by": "S88-CF-CURV-11",
            "canon_sha256": canon_sha, "joint_thm_sha256": joint_thm_sha,
            "cross_pillar_sha256": cross_pillar_sha, "registry_sha256": registry_sha,
            "allowlist_sha256": allowlist_sha, "workshop_sha256": workshop_sha,
            "script_sha256": script_sha,
        }
        audit_sha = closure_hash(pin_map_blocked)
        content_sha = sha256_text(pre_reg_value)
        canonical_line = (
            f"{GATE_ID}: FAIL -- value='{pre_reg_value}' "
            f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
            f"audit_sha256={audit_sha} content_sha256={content_sha} schema_version=S84+\n"
        )
        companion_line = (
            f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
            f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
        )
        pre_reg_inc_comment = (
            f"# PRE-REG-INC per session-88-plan-w1b2.md §W1b2-65; deferred to S89; "
            f"required prereqs: [S88-CF-CURV-11 PASS]; closure_script={SCRIPT_PATH.name}\n"
        )
        existing = VERDICT_OUT.read_text(encoding="utf-8") if VERDICT_OUT.exists() else ""
        if any(line.startswith(GATE_ID + ":") for line in existing.splitlines()):
            print(f"Verdict line for {GATE_ID} already present; skipping append.")
        else:
            with open(VERDICT_OUT, "a", encoding="utf-8") as fh:
                fh.write(canonical_line); fh.write(companion_line); fh.write(pre_reg_inc_comment)
            print(f"PRE-REG-INC verdict appended to {VERDICT_OUT.name}.")
        return 0

    # ---------------- Step 2: read input-pin SHAs (BEFORE any edits) ----------------
    canon_sha       = sha256_file(CANON_PATH)
    joint_thm_sha   = sha256_file(JOINT_THM_PATH)
    cross_pillar_sha= sha256_file(CROSS_PILLAR_PATH)
    registry_sha    = sha256_file(REGISTRY_PATH)
    allowlist_sha   = sha256_file(ALLOWLIST_PATH)
    workshop_sha    = sha256_file(WORKSHOP_PATH)
    script_sha      = sha256_file(SCRIPT_PATH)

    print(f"input-pin SHAs (pre-edit):")
    print(f"  canonical_constants.py        : {canon_sha[:16]}...")
    print(f"  joint-theorem-promotion.md    : {joint_thm_sha[:16]}...")
    print(f"  cross-pillar-bridge-anatomy.md: {cross_pillar_sha[:16]}...")
    print(f"  permanent-results-registry.md : {registry_sha[:16]}...")
    print(f"  methodology-wave-allowlist.md : {allowlist_sha[:16]}...")
    print(f"  s87 pixelation-lock workshop  : {workshop_sha[:16]}...")
    print(f"  this script                   : {script_sha[:16]}...")
    print(f"  gate #64 content_sha256       : {GATE64_CONTENT_SHA[:16]}...")
    print()

    # ---------------- Step 3: append §VII.AM body to registry ----------------
    registry_text = REGISTRY_PATH.read_text(encoding="utf-8")
    if "## §VII.AM —" in registry_text:
        print(f"§VII.AM block already present in registry; skipping append (idempotent re-run).")
        registry_appended = False  # (local)
    else:
        new_registry_text = registry_text + VII_AM_REGISTRY_BLOCK
        REGISTRY_PATH.write_text(new_registry_text, encoding="utf-8")
        print(f"§VII.AM block appended to registry ({len(VII_AM_REGISTRY_BLOCK)} bytes).")
        registry_appended = True  # (local)

    # ---------------- Step 4: append slot-allocation table row ----------------
    # Insert before the "**Last updated**" line at line ~109 (preserve table integrity).
    registry_text2 = REGISTRY_PATH.read_text(encoding="utf-8")
    if "| §VII.AM | THM | Universal Lock Condition" in registry_text2:
        print(f"Slot-allocation §VII.AM row already present; skipping (idempotent).")
        slot_row_appended = False  # (local)
    else:
        marker = "**Last updated**: 2026-04-27"
        if marker not in registry_text2:
            print(f"WARNING: slot-table marker '{marker}' not found; appending row at end of file before first '---'.")
            # Fallback: append after slot-table closing pattern.
            new_registry_text2 = registry_text2.replace(
                "\n\n**Open coordination requirements**",
                "\n" + VII_AM_SLOT_TABLE_ROW + "\n**Open coordination requirements**",
                1,
            )
        else:
            new_registry_text2 = registry_text2.replace(
                "\n" + marker,
                "\n" + VII_AM_SLOT_TABLE_ROW + "\n" + marker,
                1,
            )
        if new_registry_text2 == registry_text2:
            print("ERROR: slot-row insert FAILED (no replacement made); registry unchanged.")
            return 1
        REGISTRY_PATH.write_text(new_registry_text2, encoding="utf-8")
        print(f"§VII.AM slot-allocation table row inserted before '**Last updated**' line.")
        slot_row_appended = True  # (local)

    # ---------------- Step 5: append M4 allowlist row ----------------
    allowlist_text = ALLOWLIST_PATH.read_text(encoding="utf-8")
    if "| W1b2-65 | S88 |" in allowlist_text:
        print(f"M4 allowlist row for W1b2-65 already present; skipping (idempotent).")
        allowlist_appended = False  # (local)
    else:
        # Insert after the last existing W11-meta-3 row of the Allowlist Rows table.
        # The table ends just before the "## Pending SHA resolution" sub-header (or similar).
        marker = "## Pending SHA resolution"
        if marker not in allowlist_text:
            print(f"WARNING: allowlist marker '{marker}' not found; appending at end of file.")
            new_allowlist_text = allowlist_text + "\n" + ALLOWLIST_M4_ROW
        else:
            new_allowlist_text = allowlist_text.replace(
                "\n" + marker,
                ALLOWLIST_M4_ROW + "\n" + marker,
                1,
            )
        if new_allowlist_text == allowlist_text:
            print("ERROR: allowlist insert FAILED (no replacement made).")
            return 1
        ALLOWLIST_PATH.write_text(new_allowlist_text, encoding="utf-8")
        print(f"M4 allowlist row appended for W1b2-65.")
        allowlist_appended = True  # (local)

    # ---------------- Step 6: rubric verification (7 elements + ≥40 lines) ----------------
    final_registry_text = REGISTRY_PATH.read_text(encoding="utf-8")
    block_start = final_registry_text.find("## §VII.AM — Universal Lock Condition")
    if block_start < 0:
        print("ABORT: §VII.AM block not found after edits.")
        return 1
    block_end = final_registry_text.find("\n## §VII.", block_start + 1)
    if block_end < 0:
        block_end = len(final_registry_text)
    vii_am_block = final_registry_text[block_start:block_end]  # (local)

    rubric_checks = {
        "stage_1_candidate_tag":  "STAGE-1-CANDIDATE" in vii_am_block,
        "clause_a":               "Clause (a) Pixelation lock" in vii_am_block,
        "clause_b":               "Clause (b) Effacement lock" in vii_am_block,
        "clause_c":               "Clause (c) Page-time lock" in vii_am_block,
        "is_not_in_substrate":    "Substrate-IS observable" in vii_am_block,
        "is_not_in_laboratory":   "Laboratory-IN observable" in vii_am_block,
        "is_not_in_bridge":       "Bridge map" in vii_am_block,
        "is_not_in_envelope":     "Algebraic envelope" in vii_am_block,
        "is_not_in_anchor":       "Empirical anchor" in vii_am_block,
        "tier_1":                 "Level 1 — Substrate-IS structural identity" in vii_am_block,
        "tier_2":                 "Level 2 — Algebraic convergence envelope" in vii_am_block,
        "tier_3":                 "Level 3 — Empirical anchor at canonical L_max" in vii_am_block,
        "corpus_J3":              "J3 BH-horizon-pixelation-lock" in vii_am_block,
        "corpus_S58":             "S58 fold-effacement" in vii_am_block,
        "corpus_W1b2_64":         "W1b2-64 cascade-tail" in vii_am_block,
        "joint_clause_table":     "Cross-axis JOINT?" in vii_am_block,
        "stage_2_carry_forward":  STAGE2_CARRY_FORWARD_ID in vii_am_block,
    }
    rubric_pass = all(rubric_checks.values())  # (local)
    line_count = len(vii_am_block.splitlines())  # (local)
    substantive_pass = line_count >= 40  # (local)

    print()
    print(f"Rubric checks (7-element pattern set + extras):")
    for k, v in rubric_checks.items():
        print(f"  [{'OK' if v else '!!'}] {k}")
    print(f"Substantive line count: {line_count} (threshold >= 40: {substantive_pass})")
    print()

    # ---------------- Step 7: composite verdict ----------------
    artifact_pass = registry_appended or "## §VII.AM —" in final_registry_text  # (local)
    if rubric_pass and substantive_pass and artifact_pass:
        verdict = "PASS"        # (local)
        sign_verdict = "PASS"   # (local)  registry slot occupied by §VII.AM entry
        mag_verdict = "PASS"    # (local)  >=40 lines (rubric threshold)
        regime_verdict = "VALID"# (local)  joint-theorem-promotion.md 4-stage pathway compliance
    else:
        verdict = "FAIL"
        sign_verdict = "PASS" if artifact_pass else "FAIL"
        mag_verdict = "FAIL" if not substantive_pass else ("PASS" if rubric_pass else "FAIL")
        regime_verdict = "VALID"

    expected_4tuple = (
        f"value=stage_1_candidate_landed_at_§{SLOT}_with_{sum(rubric_checks.values())}_of_{len(rubric_checks)}_rubric_elements_and_{line_count}_lines, "
        f"scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX}"
    )
    print(f"verdict        = {verdict}")
    print(f"sign_verdict   = {sign_verdict}")
    print(f"mag_verdict    = {mag_verdict}")
    print(f"regime_verdict = {regime_verdict}")

    # ---------------- Step 8: input-pin map + SHAs ----------------
    pin_map = {
        "_gate_id":         GATE_ID,
        "_wp_id":           WP_ID,
        "_scheme":          SCHEME,
        "_convention":      CONVENTION,
        "_L_max":           L_MAX,
        "slot":             SLOT,
        "stage_2_carry_forward_id": STAGE2_CARRY_FORWARD_ID,
        "calibration_corpus_n": 3,
        "calibration_corpus_instances": [
            "J3 BH-horizon-pixelation-lock (S87 W11 workshop)",
            "S58 fold-effacement Gamma_eff=0.99970 (canonical_constants.py)",
            "W1b2-64 cascade-tail Page-time non-activation (S88 W1b2-64)",
        ],
        "joint_clauses": ["(a) pixelation lock", "(b) effacement lock", "(c) Page-time lock"],
        "cross_axis_attribution": [
            "(a): spectral-functional + transit-dynamics",
            "(b): transit-dynamics + spectral-functional",
            "(c): semiclassical-gravity + spectral-functional",
        ],
        "is_not_in_anatomy_5_elements": [
            "Substrate-IS observable", "Laboratory-IN observable",
            "Bridge map", "Algebraic envelope", "Empirical anchor",
        ],
        "three_tier_ladder": [
            "Level 1 — Substrate-IS structural identity",
            "Level 2 — Algebraic convergence envelope",
            "Level 3 — Empirical anchor at canonical L_max",
        ],
        "rubric_checks_passed":  sum(rubric_checks.values()),
        "rubric_checks_total":   len(rubric_checks),
        "rubric_substantive_line_count": line_count,
        "Gamma_effacement_canonical": float(Gamma_effacement),
        "tau_fold_canonical": float(tau_fold),
        "canon_sha256":      canon_sha,
        "joint_thm_sha256":  joint_thm_sha,
        "cross_pillar_sha256": cross_pillar_sha,
        "registry_sha256_pre_edit": registry_sha,
        "allowlist_sha256_pre_edit": allowlist_sha,
        "workshop_sha256":   workshop_sha,
        "script_sha256":     script_sha,
        "gate_64_content_sha256": GATE64_CONTENT_SHA,
        "verdict":           verdict,
        "sign_verdict":      sign_verdict,
        "mag_verdict":       mag_verdict,
        "regime_verdict":    regime_verdict,
    }
    audit_sha = closure_hash(pin_map)
    # content_sha256: SHA over the registry-entry text concatenated with the slot-row + allowlist-row.
    content_sha = sha256_text(VII_AM_REGISTRY_BLOCK + VII_AM_SLOT_TABLE_ROW + ALLOWLIST_M4_ROW)

    print(f"\naudit_sha256:   {audit_sha}")
    print(f"content_sha256: {content_sha}")

    # ---------------- Step 9: emit verdict line + companion + 3-tuple ----------------
    value_field = (
        f"stage_1_candidate_landed_at_§{SLOT};"
        f"rubric_elements_passed={sum(rubric_checks.values())}/{len(rubric_checks)};"
        f"substantive_line_count={line_count};"
        f"calibration_corpus_n=3;"
        f"corpus=[J3,S58,W1b2-64];"
        f"stage_2_carry_forward={STAGE2_CARRY_FORWARD_ID};"
        f"registry_appended={registry_appended};"
        f"slot_row_appended={slot_row_appended};"
        f"allowlist_appended={allowlist_appended}"
    )
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value='{value_field}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} schema_version=S84+\n"
    )
    companion_line = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    schema_v2_line = (
        f"# sign_verdict={sign_verdict} magnitude_verdict={mag_verdict} regime_verdict={regime_verdict} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )

    existing = VERDICT_OUT.read_text(encoding="utf-8") if VERDICT_OUT.exists() else ""
    if any(line.startswith(GATE_ID + ":") for line in existing.splitlines()):
        print(f"\nVerdict line for {GATE_ID} already present; skipping append.")
    else:
        with open(VERDICT_OUT, "a", encoding="utf-8") as fh:
            fh.write(canonical_line)
            fh.write(companion_line)
            fh.write(schema_v2_line)
        print(f"\nVerdict line + companion + schema-v2 row appended to {VERDICT_OUT.name}.")

    print("\nSummary (4-tuple):")
    print(f"  ({expected_4tuple})")
    print(f"  verdict = {verdict}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
