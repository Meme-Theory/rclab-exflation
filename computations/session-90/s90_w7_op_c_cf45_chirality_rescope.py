"""
S90 W7 Operation C — CF-45 CHIRALITY-RESCOPE (mack-cosmic-bridge sole-writer)

Gate ID: S90-CF-A40-FAIL-ALTERNATIVE-CHIRALITY-RESCOPE

Source plan: sessions/session-plan/session-90-plan-w7.md §W7-6 (lines 1113-1352)

Operation: registry-anatomy refactor on sessions/permanent-results-registry.md +
           edit on sessions/archive/session-89/session-89-w2-workingpaper.md CF-A40 plan-block +
           slot-allocation lockfile creation.

Steps (per plan §W7-6 §6):
  STEP 1: Append §VII.AQ.OP-PROJ Stage-2-style upgrade clause for candidate (c)
          substrate-natural inner-fluctuation 1-form A (preserves γ_9 = γ_5 ⊗ γ_F;
          Connes-Chamseddine 1996 §2.2-2.3 inner-fluctuation construction;
          cross-link to CF-55 Reading A; DEFERRED to S91+ per W-5 Q-R-3).
  STEP 2: Scaffold NEW §VII.AT.OP-PROJ slot for candidate (a) bi-chirality
          (γ_5 ⊕ γ_F direct-sum) per plan §6 Step 2 template
          (Element-1 spec + Level-1 single-τ-slice + STAGE-0-CANDIDATE-PENDING).
  STEP 3: Scaffold NEW §VII.AW.OP-PROJ slot for candidate (b) SU(3)-coloured
          chirality (γ_F^c per Connes-Marcolli 2008 §11) per plan §6 Step 3 template.
  STEP 4: Edit sessions/archive/session-89/session-89-w2-workingpaper.md CF-A40 plan-block
          at lines 415-420: replace "convention-shopping framing" with
          "registry-anatomy hygiene at Element-1"; add cross-links.
  STEP 5: Create sessions/framework/s90-slot-pre-allocation-lockfile.md with
          RESERVED-FOR-WORKSHOP-W7-CF-45 tags for §VII.AT and §VII.AW.
  STEP 6: Single-shot AFTER-pattern emission.

Author: mack-cosmic-bridge (sole writer per feedback_mack-bridge-role.md)
"""

import hashlib
import os
import sys
from pathlib import Path

# (local) Gate identity
GATE_ID = "S90-CF-A40-FAIL-ALTERNATIVE-CHIRALITY-RESCOPE"  # (local)
SCHEME = "cf-a40-fail-alternative-chirality-rescope"  # (local)
CONVENTION = "cf-a40-rescope-via-w-5-cf-w5-3-stage-2-upgrade-plus-vii-at-vii-aw-scaffold"  # (local)
L_MAX = 10  # (local)

# (local) Paths
PROJECT_ROOT = Path(r"C:\sandbox\Ainulindale Exflation")  # (local)
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)
VERDICT_PATH = PROJECT_ROOT / "computations" / "session-90" / "s90_gate_verdicts.txt"  # (local)
PLAN_W7 = PROJECT_ROOT / "sessions" / "session-plan" / "session-90-plan-w7.md"  # (local)
S89_W2_WP = PROJECT_ROOT / "sessions" / "session-89" / "session-89-w2-workingpaper.md"  # (local)
LOCKFILE = PROJECT_ROOT / "sessions" / "framework" / "s90-slot-pre-allocation-lockfile.md"  # (local)
CROSS_PILLAR_RULE = PROJECT_ROOT / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md"  # (local)
PHONONIC_FRAMING_RULE = PROJECT_ROOT / ".claude" / "rules" / "phononic-framing.md"  # (local)
EPISTEMIC_DISCIPLINE_RULE = PROJECT_ROOT / ".claude" / "rules" / "epistemic-discipline.md"  # (local)

# (local) Provenance pins
OP_A_AUDIT_SHA = "bad7c3244606a08f1e12512f813540fe51bd9665010aad84b9aeb605a1cce8f3"  # (local)
OP_B_AUDIT_SHA = "23a60ab5b0a09a44b2c722e5dd30b831b90b73298ce73a345cc10c42a8fe8395"  # (local)
CF_54_AUDIT_SHA = "3643ca19211edfc455e8a9528c46969682e77ce999ccac2e478fa055de15fb51"  # (local)
CF_55_AUDIT_SHA = "f634be0d942241095e40ce71562b69fee522faaa520c9ce861844c15f02a8f77"  # (local)


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def text_sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def closure_hash(input_pin_map: dict) -> str:
    items = sorted(input_pin_map.items())
    serialized = "\n".join(f"{k}={v}" for k, v in items)
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


def build_vii_aq_stage2_upgrade_clause() -> str:
    """STEP 1: §VII.AQ.OP-PROJ Stage-2-style upgrade clause for candidate (c).

    Per plan §W7-6 §6 Step 1 template (lines 1130-1166).
    """
    return """**Stage-2-style upgrade clause (S90 W7 CF-45 — substrate-natural inner-fluctuation 1-form A, candidate (c))**:

STATUS: Stage-2-style upgrade pre-registered per W-5 R2 verdict Q-R-3 (S89 CF-W5-3 re-scoping); S91+ DEFERRED substrate-physics computation per W-5 Q-R-3.

PROVENANCE: W-5 R2 verdict freeze (workshop `sessions/archive/session-89/workshops/s89-w5-vii-aq-level3-binding.md`); authoring agents connes-ncg-theorist + volovik-superfluid-universe-theorist; S90 W7 CF-45 re-scoping per `sessions/archive/session-89/session-89-w2-workingpaper.md` CF-A40-FAIL-ALTERNATIVE-CHIRALITY (lines 415-420).

SUBSTRATE TRIPLE (preserves §VII.AQ.OP-PROJ Element-1 chirality grading):
- Fixed: `γ_9 = γ_5 ⊗ γ_F` (registered §VII.AQ.OP-PROJ chirality grading; Connes 1996 chirality axiom + axiom 5 `{D_K, γ_9} = 0` NCG anticommutation)
- Modified: `D_K → D_K + A` where `A` is a substrate-natural inner-fluctuation 1-form (Connes-Chamseddine 1996 §2.2-2.3; `A ∈ Ω¹_D(A_K)` with `A* = A` and `γ_9 A γ_9 = -A`)
- The modification PRESERVES the registered spectral triple at the level of `γ_9 + J +` axioms 1-7 by construction (`A` is built from elements of `A_K` + commutators with `D_K`; `A` is intrinsic to the spectral triple).

STAGE-2-STYLE UPGRADE CLAUSE: The candidate (c) construction provides a substrate-natural deformation of `D_K` within the registered spectral triple. The Stage-2 upgrade asks: does the inner-fluctuation deformation preserve the §VII.AQ.OP-PROJ Reading A (scheme-INDEPENDENT) verdict OR shift the verdict to Reading B (scheme-DEPENDENT) under the deformed `D_K`? Substrate-physics computation: re-evaluate SECONDARY-CLASS-SCHEME-DISCRIMINATOR (CF-55 analog) under `D_K + A`; emit comparison `Δ_scheme(D_K + A) vs Δ_scheme(D_K)` at fixed `γ_9`.

CROSS-LINK TO CF-55 OUTCOME (Reading A confirmed at S90 W7): If CF-55 Reading A under `D_K` extends to `D_K + A` (i.e., `Δ_scheme(D_K + A) = 0` to bit precision), Reading A is robust under substrate-natural inner-fluctuation deformation. If `Δ_scheme(D_K + A) ≥ 1e-3`, the substrate-natural inner-fluctuation breaks the scheme-INDEPENDENCE and forces a Reading B re-spec under deformed `D_K`. Pre-registered as S91+ gate per Q-R-3.

S91+ DEFERRED COMPUTATION (per W-5 Q-R-3 + W-5 CF-W5-3):
- Construct substrate-natural inner-fluctuation 1-form `A` from `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` + commutators with `D_K` per Connes-Chamseddine 1996 §2.2-2.3 (full leaf-foliation infrastructure required; NOT in S90 dispatch budget)
- Re-compute GV cocycle under `D_K + A` at both APS-1975 and Cheeger-Simons schemes
- Compare `Δ_scheme(D_K + A) vs Δ_scheme(D_K)` at L_max ∈ {10, 12, 14}
- Emit Stage-2 verdict on §VII.AQ.OP-PROJ Reading A robustness under inner-fluctuation deformation
- Effort estimate: ~1.0 wave-equivalent (subset of the ~1.5 we W-5 CF-W5-5 budget for §VII.AT + §VII.AW combined)

CONTAINER-THINKING REMINDER: Candidate (c) is a DEFORMATION WITHIN the §VII.AQ.OP-PROJ spectral triple (preserves `γ_9 + J +` axioms); the substrate IS the spectral triple at fixed `(A_K, H_K, D_K + A, γ_9, J)`. The inner-fluctuation 1-form `A` IS intrinsic to the substrate algebra (built from elements of `A_K` + commutators with `D_K`); it is NOT a "perturbation FROM OUTSIDE" the substrate. Direction of explanation: substrate IS the deformed spectral triple → inner-fluctuation deformation IS a substrate-internal modification within the registered chirality grading → §VII.AQ.OP-PROJ Stage-2 upgrade extends Reading A robustness check to the deformed `D_K + A` evaluator.

"""


def build_vii_at_op_proj_slot() -> str:
    """STEP 2: NEW §VII.AT.OP-PROJ slot for candidate (a) bi-chirality.

    Per plan §W7-6 §6 Step 2 template (lines 1168-1210).
    """
    return """## §VII.AT.OP-PROJ — Bi-Chirality Spectral Triple (γ_5 ⊕ γ_F Direct-Sum) (W-5 candidate (a); STAGE-0-CANDIDATE-PENDING-S91-SUBSTRATE-PHYSICS; S90 W7 CF-45 — mack-cosmic-bridge sole-writer per feedback_mack-bridge-role.md, 2026-05-15)

> **Slot allocation provenance**: S90 W7 CF-45 (mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`, 2026-05-15). Next-free-letter assignment per `registry-landing.md` next-free-letter protocol: §VII.AR (W-22 W7a-74 LEVEL-DRESSED) + §VII.AS (W-18 W6a-51 geometric-resummation) + §VII.AU (CF-63 REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION) + §VII.AV (CF-W7-1 W7c rerouted) all occupied; §VII.AT is the next-free letter for the W-5 candidate (a) bi-chirality slot scaffolding. Slot-allocation lockfile entry: `sessions/framework/s90-slot-pre-allocation-lockfile.md` with RESERVED-FOR-WORKSHOP-W7-CF-45-VII-AT tag.

**Status**: STAGE-0-CANDIDATE-PENDING-S91-SUBSTRATE-PHYSICS per `joint-theorem-promotion.md §"Stage 0"` + `cross-pillar-bridge-anatomy.md §"Forward template-adoption"`. Substrate-physics derivation deferred to S91+ per W-5 Q-R-3 + W-5 CF-W5-5.

**Provenance**: W-5 R2 verdict freeze (workshop `sessions/archive/session-89/workshops/s89-w5-vii-aq-level3-binding.md`); CF-A40 FAIL diagnostic re-scoping (`sessions/archive/session-89/session-89-w2-workingpaper.md` lines 415-420 per S90 W7 CF-45 edit); Connes-Marcolli 2008 ch.1 chirality discussion.

**SUBSTRATE TRIPLE (Element-1 specification)**:

- **Algebra**: `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` (unchanged from §VII.AQ.OP-PROJ)
- **Hilbert space**: `H_K` (unchanged from §VII.AQ.OP-PROJ)
- **Dirac operator**: `D_K` (unchanged; finite L_max=10 truncation)
- **Chirality grading**: `γ_9 → γ_9' = γ_5 ⊕ γ_F` (DIRECT-SUM grading; NOT tensor product)
  - The candidate (a) bi-chirality grading replaces the standard tensor product `γ_9 = γ_5 ⊗ γ_F` with a direct sum, treating the spacetime chirality `γ_5` and finite-sector chirality `γ_F` as INDEPENDENT chiralities rather than tensor-multiplied
  - Substrate-physics implication: the bi-chirality decomposes the Hilbert space `H_K` into 4 sectors `(+,+), (+,-), (-,+), (-,-)` via the joint `(γ_5, γ_F)` eigenvalue assignment, rather than into 2 sectors `(+,-)` via the joint `γ_9 = γ_5 ⊗ γ_F` eigenvalue
- **Real structure**: `J` (unchanged from §VII.AQ.OP-PROJ; verify `J γ_9' = -γ_9' J` per axiom 5' under direct-sum grading)
- **KO-dim**: TO BE COMPUTED at S91+ (direct-sum chirality may differ from KO-dim=6 tensor case)
- **Axioms 1-7 + Poincaré duality**: TO BE VERIFIED at S91+ (re-derivation of the 7 NCG axioms under direct-sum chirality grading is the S91+ substrate-physics task)

**ELEMENT-1 (substrate-IS observable)**: substrate-natural cocycle on `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10}, γ_9' = γ_5 ⊕ γ_F, J)` — exact form TBD at S91+ pending the bi-chirality NCG axiom re-derivation. Candidate cocycle classes: η-invariant under bi-chirality grading; GV cocycle under bi-chirality grading; Heitsch cubic trace under bi-chirality grading.

**ELEMENT-2 (laboratory-IN observable)**: TBD at S91+. Candidate laboratory-IN images: (η_{γ_5}, η_{γ_F})-joint-probe in 3He-B BdG sector under independent-chirality-axis decomposition; Cheeger-Simons differential character at bi-chirality grading.

**ELEMENT-3 (bridge map)**: TBD at S91+. Candidate bridge maps: HKR (Hochschild-Kostant-Rosenberg) at bi-chirality grading; K-theory boundary under direct-sum grading; Connes-Karoubi pairing under bi-chirality axioms (if axiom 5' is satisfied).

**ELEMENT-4 (algebraic envelope)**: TBD at S91+. Level-2-binding vs Level-2-non-binding classification deferred per `cross-pillar-bridge-anatomy.md §"Level-2 sub-class (binding vs non-binding)"` — pending S91+ bridge-map identification.

**ELEMENT-5 (empirical anchor)**: TBD at S91+ pending numerical evaluation of the bi-chirality cocycle on the L_max=10 spectrum cache.

**LEVEL-1 declaration**: Level 1 (single-τ-slice at τ_fold = 0.190) — explicit per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` K=2 MANDATORY + VOLOVIK V.2 refinement (S89 line 21). The bi-chirality grading IS a substrate-IS structural property at the fixed τ-slice; the moduli-deformation behavior (Level 2) is a separate question deferred to S91+.

**S91+ DEFERRED COMPUTATION (W-5 CF-W5-5 substrate-physics)**:

1. Re-derive 7 NCG axioms under direct-sum chirality grading `γ_9' = γ_5 ⊕ γ_F`
2. Verify KO-dim is well-defined; compute KO-dim under bi-chirality
3. Determine whether substrate-IS observables under bi-chirality have laboratory-IN images (Element-2 + Element-3 bridge map identification)
4. Compute candidate cocycles (η_{γ_9'}, GV_{γ_9'}) on `s84_spectrum_cache_L12_tau019.npz` under bi-chirality grading
5. Compare `Δ_GV_bi-chirality` against the L_max=10 spectrum cache's chirality split under bi-chirality (predicted: NOT uniform 8d:8d per-sector — bi-chirality gives 4 sectors `(+,+), (+,-), (-,+), (-,-)` with non-uniform cardinality per (p,q); breaks the 78080:78080 cancellation diagnosed at S89 §W2-5)
6. Effort estimate: ~1.5 wave-equivalents (combined with §VII.AW candidate (b))

**Cross-link**:
- §VII.AQ.OP-PROJ (parent slot; Stage-2-style upgrade for candidate (c) substrate-natural inner-fluctuation 1-form A)
- §VII.AW.OP-PROJ (sibling slot; candidate (b) SU(3)-coloured chirality γ_F^c per Connes-Marcolli 2008 §11)
- CF-A40 FAIL diagnostic (S89 §W2-5; re-scoped at S90 W7 CF-45 from "convention-shopping framing" to "registry-anatomy hygiene at Element-1")
- W-5 CF-W5-3 re-scoping (Q-R-3 substrate-physics computation deferred to S91+)
- W-5 CF-W5-5 S91+ substrate-physics computation spec
- `sessions/framework/s90-slot-pre-allocation-lockfile.md` (RESERVED-FOR-WORKSHOP-W7-CF-45-VII-AT)
- Connes-Marcolli 2008 ch.1 chirality discussion (literature reference for bi-chirality vs tensor-product chirality)

**Substrate framing**: The bi-chirality grading `γ_9' = γ_5 ⊕ γ_F` IS a STRUCTURALLY DISTINCT spectral triple from the standard tensor-product chirality `γ_9 = γ_5 ⊗ γ_F` at §VII.AQ.OP-PROJ. The substrate IS a spectral triple `(A, H, D, γ, J)`; modifying any of `(A, H, D, γ, J)` IS a new substrate. Direction of explanation: substrate IS spectral triple → chirality-grading-modification IS new-spectral-triple → new substrate-IS observables → new §VII registry slot at §VII.AT.OP-PROJ. Container-thinking violation avoided: "We're choosing between chirality conventions" — INVERT: "each chirality grading IS a structurally distinct substrate; §VII.AT.OP-PROJ registers the bi-chirality substrate as a separate spectral-triple slot with its own Element-1 specification". The candidate (a) bi-chirality is NOT a convention choice on §VII.AQ.OP-PROJ; it is a different substrate registered at a separate §VII slot.

**Source**: S90 W7 CF-45 (`sessions/session-plan/session-90-plan-w7.md §W7-6` Step 2 template; mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`).

---

"""


def build_vii_aw_op_proj_slot() -> str:
    """STEP 3: NEW §VII.AW.OP-PROJ slot for candidate (b) SU(3)-coloured chirality.

    Per plan §W7-6 §6 Step 3 template (lines 1212-1242).
    """
    return """## §VII.AW.OP-PROJ — SU(3)-Coloured Chirality Spectral Triple (γ_F^c per Connes-Marcolli 2008 §11) (W-5 candidate (b); STAGE-0-CANDIDATE-PENDING-S91-SUBSTRATE-PHYSICS; S90 W7 CF-45 — mack-cosmic-bridge sole-writer per feedback_mack-bridge-role.md, 2026-05-15)

> **Slot allocation provenance**: S90 W7 CF-45 (mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`, 2026-05-15). Next-free-letter assignment per `registry-landing.md` next-free-letter protocol: §VII.AU (CF-63 REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION) + §VII.AV (CF-W7-1 W7c rerouted emission #3) occupied; §VII.AW is the next-free letter for the W-5 candidate (b) SU(3)-coloured chirality slot scaffolding (skipping §VII.AU + §VII.AV). Slot-allocation lockfile entry: `sessions/framework/s90-slot-pre-allocation-lockfile.md` with RESERVED-FOR-WORKSHOP-W7-CF-45-VII-AW tag.

**Status**: STAGE-0-CANDIDATE-PENDING-S91-SUBSTRATE-PHYSICS per `joint-theorem-promotion.md §"Stage 0"`. Substrate-physics derivation deferred to S91+ per W-5 Q-R-3 + W-5 CF-W5-5.

**Provenance**: W-5 R2 verdict freeze (workshop `sessions/archive/session-89/workshops/s89-w5-vii-aq-level3-binding.md`); Connes-Marcolli 2008 ch.1 + §11 SU(3)-coloured chirality discussion (γ_F^c is the colour-dressed finite-sector chirality).

**SUBSTRATE TRIPLE (Element-1 specification)**:

- **Algebra**: `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` (unchanged from §VII.AQ.OP-PROJ)
- **Hilbert space**: `H_K` (unchanged from §VII.AQ.OP-PROJ)
- **Dirac operator**: `D_K` (unchanged; finite L_max=10 truncation)
- **Chirality grading**: `γ_9 → γ_9'' = γ_F^c` (SU(3)-coloured chirality per Connes-Marcolli 2008 §11; `γ_F^c` is the colour-dressed finite-sector chirality acting on the `M_3(ℂ)` summand via the colour-axis decomposition `(r, g, b)`)
  - The candidate (b) SU(3)-coloured chirality refines the finite-sector chirality `γ_F` by attaching a colour-axis label to each chirality eigenstate, producing a finer decomposition of the `M_3(ℂ)` summand than the colour-blind tensor product `γ_9 = γ_5 ⊗ γ_F` provides
  - Substrate-physics implication: the colour-dressed chirality decomposes the `M_3(ℂ)` summand into colour-tagged chirality sectors, allowing colour-axis-resolved chirality cocycle observables
- **Real structure**: `J` (unchanged from §VII.AQ.OP-PROJ; verify `J γ_9'' = ε γ_9'' J` for sign `ε` per axiom 5'' under colour-dressed grading)
- **KO-dim**: TO BE COMPUTED at S91+ (colour-dressed chirality may shift KO-dim from 6; per Connes-Marcolli 2008 §11 the colour-dressing may produce KO-dim shift mod 8 dependent on the J anticommutation sign ε)
- **Axioms 1-7 + Poincaré duality**: TO BE VERIFIED at S91+ under SU(3)-coloured grading

**ELEMENT-1 through ELEMENT-5**: TBD at S91+ per Connes-Marcolli 2008 §11 framework. Candidate Element-1 forms include the colour-axis-resolved GV cocycle (`GV_{γ_F^c}` per colour-tagged sector), colour-axis-resolved η-invariant, colour-axis-resolved Heitsch cubic trace. Element-3 bridge maps under SU(3)-coloured grading: HKR at colour-dressed grading; K-theory boundary with SU(3)-colour-axis decomposition; Connes-Karoubi pairing under colour-dressed axioms.

**LEVEL-1 declaration**: Level 1 (single-τ-slice at τ_fold = 0.190) — explicit per VOLOVIK V.2 refinement (S89 line 21) + `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` K=2 MANDATORY. The SU(3)-coloured chirality grading IS a substrate-IS structural property at the fixed τ-slice; the moduli-deformation behavior (Level 2) is a separate question deferred to S91+.

**S91+ DEFERRED COMPUTATION (W-5 CF-W5-5 substrate-physics)**:

1. Re-derive 7 NCG axioms under SU(3)-coloured chirality grading per Connes-Marcolli 2008 §11
2. Verify KO-dim under `γ_F^c` grading (predicted: KO-dim shift mod 8 dependent on J anticommutation sign ε)
3. Determine bridge-map class for SU(3)-coloured substrate-IS observables (Element-3 identification)
4. Compute candidate cocycles (η_{γ_F^c}, GV_{γ_F^c}) per colour-tagged sector on `s84_spectrum_cache_L12_tau019.npz` under SU(3)-coloured grading
5. Compare `Δ_GV_SU(3)-coloured` against the L_max=10 spectrum cache's chirality split under SU(3)-coloured grading (predicted: NOT uniform per-sector; colour-axis decomposition produces 9 colour-tagged sectors per (p,q) rather than uniform 8d:8d)
6. Effort estimate: ~1.5 wave-equivalents (combined with §VII.AT candidate (a))

**Cross-link**:
- §VII.AQ.OP-PROJ (parent slot; Stage-2-style upgrade for candidate (c) substrate-natural inner-fluctuation 1-form A)
- §VII.AT.OP-PROJ (sibling slot; candidate (a) bi-chirality γ_5 ⊕ γ_F direct-sum)
- CF-A40 FAIL diagnostic (S89 §W2-5; re-scoped at S90 W7 CF-45 from "convention-shopping framing" to "registry-anatomy hygiene at Element-1")
- W-5 CF-W5-3 re-scoping (Q-R-3 substrate-physics computation deferred to S91+)
- W-5 CF-W5-5 S91+ substrate-physics computation spec
- `sessions/framework/s90-slot-pre-allocation-lockfile.md` (RESERVED-FOR-WORKSHOP-W7-CF-45-VII-AW)
- Connes-Marcolli 2008 ch.1 + §11 SU(3)-coloured chirality framework (literature reference for γ_F^c)

**Substrate framing**: The SU(3)-coloured chirality grading `γ_9'' = γ_F^c` IS a STRUCTURALLY DISTINCT spectral triple from the standard tensor-product chirality `γ_9 = γ_5 ⊗ γ_F` at §VII.AQ.OP-PROJ. The substrate IS a spectral triple `(A, H, D, γ, J)`; the colour-dressing of the chirality grading at §VII.AW.OP-PROJ produces a new spectral triple with a refined sector decomposition of the `M_3(ℂ)` summand. Direction of explanation: substrate IS spectral triple → colour-axis-resolved chirality grading IS new-spectral-triple → new substrate-IS observables (colour-axis-tagged cocycles) → new §VII registry slot at §VII.AW.OP-PROJ. Container-thinking violation avoided: "Colour is a label we attach to chirality eigenstates" — INVERT: "the SU(3)-coloured chirality grading IS the substrate's intrinsic refinement of the chirality decomposition at the `M_3(ℂ)` summand; the colour-axis IS substrate-IS, not a label imposed FROM OUTSIDE the substrate".

**Source**: S90 W7 CF-45 (`sessions/session-plan/session-90-plan-w7.md §W7-6` Step 3 template; mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`; Connes-Marcolli 2008 ch.1 + §11 framework literature reference).

---

"""


def build_lockfile_text() -> str:
    """STEP 5: Create s90-slot-pre-allocation-lockfile.md with RESERVED-FOR-WORKSHOP-W7-CF-45 tags."""
    return """# S90 Slot Pre-Allocation Lockfile

> **Provenance**: S90 W7 CF-45 (mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`, 2026-05-15). Slot pre-allocation lockfile per `.claude/rules/epistemic-discipline.md §"Registry-Write Hygiene under Parallel-Writer Race"` slot-allocation lockfile discipline (multi-slot pre-allocation; canonical pattern: `sessions/framework/s87-slot-pre-allocation-lockfile.md`). This lockfile pre-allocates registry slots in `sessions/permanent-results-registry.md` for S90 workshop landings to prevent parallel-writer race collisions.

## Purpose

When a single workshop produces MULTIPLE registry-landings whose slot-identity must remain non-colliding across waves, the orchestrator pre-allocates the slot-letter assignments at plan-freeze time and records them here. Producing scripts consult this lockfile to confirm their planned slot is RESERVED to them; on runtime occupancy by an intervening landing, they reroute to the next-free-letter and emit FAIL-with-remediation per `epistemic-discipline.md §"Registry-Write Hygiene"` item 3.

## Allocations

### RESERVED-FOR-WORKSHOP-W7-CF-45-VII-AT

- **Reserved for**: `S90-CF-A40-FAIL-ALTERNATIVE-CHIRALITY-RESCOPE` gate (S90 W7 CF-45)
- **Slot**: `§VII.AT.OP-PROJ`
- **Workshop**: W-5 candidate (a) bi-chirality `γ_5 ⊕ γ_F` direct-sum
- **Next-free-letter basis**: §VII.AR (W-22 W7a-74) + §VII.AS (W-18 W6a-51) occupied → §VII.AT is next-free at S90 W7 CF-45 dispatch time
- **Provenance**: Spawn-prompt §"OPERATION C" Step 5; plan reference `sessions/session-plan/session-90-plan-w7.md §W7-6` lines 1167-1171
- **Sponsors**: mack-cosmic-bridge (sole writer); gen-physicist (5-anatomy completeness audit co-sign per `cross-pillar-bridge-anatomy.md §"Audit at plan-freeze"`); volovik-superfluid-universe-theorist (Level-1 declaration discipline co-sign per VOLOVIK V.2 refinement)
- **Anchor list**: §VII.AQ.OP-PROJ (parent) + §VII.AW.OP-PROJ (sibling); CF-A40 FAIL diagnostic (S89 §W2-5); W-5 CF-W5-3 + CF-W5-5 substrate-physics deferred to S91+

### RESERVED-FOR-WORKSHOP-W7-CF-45-VII-AW

- **Reserved for**: `S90-CF-A40-FAIL-ALTERNATIVE-CHIRALITY-RESCOPE` gate (S90 W7 CF-45)
- **Slot**: `§VII.AW.OP-PROJ`
- **Workshop**: W-5 candidate (b) SU(3)-coloured chirality `γ_F^c` per Connes-Marcolli 2008 §11
- **Next-free-letter basis**: §VII.AU (CF-63 REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION) + §VII.AV (CF-W7-1 W7c rerouted emission #3) occupied → §VII.AW is next-free at S90 W7 CF-45 dispatch time (skipping §VII.AU + §VII.AV)
- **Provenance**: Spawn-prompt §"OPERATION C" Step 5; plan reference `sessions/session-plan/session-90-plan-w7.md §W7-6` lines 1213-1216
- **Sponsors**: mack-cosmic-bridge (sole writer); gen-physicist (5-anatomy completeness audit co-sign); volovik-superfluid-universe-theorist (Level-1 declaration discipline co-sign)
- **Anchor list**: §VII.AQ.OP-PROJ (parent) + §VII.AT.OP-PROJ (sibling); CF-A40 FAIL diagnostic (S89 §W2-5); W-5 CF-W5-3 + CF-W5-5 substrate-physics deferred to S91+

## Cross-link to canonical slot-allocation lockfile precedent

- `sessions/framework/s87-slot-pre-allocation-lockfile.md` (S87 precedent for the lockfile pattern)
- `.claude/rules/epistemic-discipline.md §"Registry-Write Hygiene under Parallel-Writer Race"` item 3 (FAIL-with-remediation discipline on runtime occupancy)
- `.claude/rules/registry-landing.md §"Bridge-Landing Script Architecture (single-shot pattern)"` (single-shot AFTER-pattern emission, no in-place edits)

## Lockfile updates

| Date | Operation | Slot | Status |
|:-----|:----------|:-----|:-------|
| 2026-05-15 | Initial allocation per S90 W7 CF-45 | §VII.AT.OP-PROJ | RESERVED |
| 2026-05-15 | Initial allocation per S90 W7 CF-45 | §VII.AW.OP-PROJ | RESERVED |
"""


def write_atomic_with_fsync(path: Path, content: str) -> None:
    tmp_path = path.with_suffix(path.suffix + ".tmp_s90_w7_op_c")
    with open(tmp_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp_path, path)


def verify_section_matches(registry_path: Path, expected_substrings: list) -> tuple:
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
    print("=" * 78)
    print("S90 W7 Operation C — CF-45 CHIRALITY-RESCOPE")
    print(f"Gate ID: {GATE_ID}")
    print("=" * 78)

    # ============================================================
    # STAGE 1: BUILD (pure-function, no I/O)
    # ============================================================

    # (local) Input-pin SHAs
    registry_pre_sha = file_sha256(REGISTRY_PATH)  # (local)
    s89_w2_wp_pre_sha = file_sha256(S89_W2_WP)  # (local)
    plan_w7_sha = file_sha256(PLAN_W7)  # (local)
    cross_pillar_sha = file_sha256(CROSS_PILLAR_RULE)  # (local)
    phononic_framing_sha = file_sha256(PHONONIC_FRAMING_RULE)  # (local)
    epistemic_discipline_sha = file_sha256(EPISTEMIC_DISCIPLINE_RULE)  # (local)

    print(f"\n[INPUT-PIN MAP]")
    print(f"  registry_pre_edit_sha = {registry_pre_sha}")
    print(f"  s89_w2_wp_pre_edit_sha = {s89_w2_wp_pre_sha}")
    print(f"  plan_w7_md_sha = {plan_w7_sha}")
    print(f"  op_a_audit_sha = {OP_A_AUDIT_SHA}")
    print(f"  op_b_audit_sha = {OP_B_AUDIT_SHA}")

    # (local) Build all texts in memory
    stage2_upgrade_clause = build_vii_aq_stage2_upgrade_clause()
    vii_at_slot = build_vii_at_op_proj_slot()
    vii_aw_slot = build_vii_aw_op_proj_slot()
    lockfile_text = build_lockfile_text()

    # ============================================================
    # STAGE 2: REGISTRY EDIT — STEP 1 (Stage-2 upgrade clause appended at §VII.AQ.OP-PROJ)
    #                         + STEP 2 (§VII.AT.OP-PROJ scaffolded after §VII.AS)
    #                         + STEP 3 (§VII.AW.OP-PROJ scaffolded after §VII.AT)
    # ============================================================

    with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
        registry_text = f.read()  # (local)

    # (local) STEP 1: Find §VII.AQ.OP-PROJ section; append Stage-2 upgrade clause BEFORE the "**Source**" or cross-links section.
    # (local) The §VII.AQ.OP-PROJ section ends where the next "## §" header begins or where the "---\n\n" boundary sits.
    # (local) For STEP 1, we insert the Stage-2 upgrade clause AFTER the "**Substrate framing** (per `.claude/rules/phononic-framing.md`):..." block
    # (local) and BEFORE the "**Cross-references**:" block. The cleanest anchor is the "**Cross-references**:" header line in §VII.AQ.OP-PROJ.
    section_header = "## §VII.AQ.OP-PROJ — STRUCTURAL-EVEN-GRADING-BLINDNESS-AT-CORNER-I-SCOPE"
    section_idx = registry_text.find(section_header)
    if section_idx == -1:
        print(f"\n[FAIL] §VII.AQ.OP-PROJ section header not found (Operation A may not have landed)")
        sys.exit(0)

    # (local) Find "**Cross-references**:" anchor within §VII.AQ.OP-PROJ section (NOT the global occurrence — restrict to the section)
    next_section_idx = registry_text.find("\n## §VII.K-PROP-W8-LAYERED", section_idx)
    if next_section_idx == -1:
        print(f"\n[FAIL] next-section marker §VII.K-PROP-W8-LAYERED not found")
        sys.exit(0)
    xref_anchor = "**Cross-references**:\n- §VII.AF.1.OP-PROJ"
    xref_idx = registry_text.find(xref_anchor, section_idx, next_section_idx)
    if xref_idx == -1:
        print(f"\n[FAIL] **Cross-references**: anchor not found within §VII.AQ.OP-PROJ section")
        sys.exit(0)

    # (local) Insert Stage-2 upgrade clause BEFORE the Cross-references anchor
    registry_after_step1 = (
        registry_text[:xref_idx]
        + stage2_upgrade_clause
        + registry_text[xref_idx:]
    )

    # (local) STEP 2 + STEP 3: Scaffold §VII.AT.OP-PROJ + §VII.AW.OP-PROJ after §VII.AS (which is at registry lines 17037-17062 pre-edit).
    # (local) Find §VII.AS section's end boundary (the "---\n\n" before the next "## §VII.AQ.OP-PROJ" header).
    # (local) Equivalently: find the start of "## §VII.AQ.OP-PROJ" header; the slots go immediately BEFORE it.
    aq_op_proj_after_step1 = registry_after_step1.find("## §VII.AQ.OP-PROJ — STRUCTURAL-EVEN-GRADING-BLINDNESS")
    if aq_op_proj_after_step1 == -1:
        print(f"\n[FAIL] §VII.AQ.OP-PROJ header not found in step-1-updated text")
        sys.exit(0)

    # (local) The new §VII.AT.OP-PROJ + §VII.AW.OP-PROJ slots go BEFORE the §VII.AQ.OP-PROJ header
    # (local) per next-free-letter discipline (§VII.AT < §VII.AQ alphabetically? No — A-Q < A-T alphabetically since Q < T).
    # (local) Actually for next-free-letter the slots are appended in order; §VII.AR/AS already precede §VII.AQ in the registry
    # (local) (since §VII.AR was assigned at S88 W22 AFTER §VII.AQ was originally registered at S88 W7b-79 with a slot-reroute remediation).
    # (local) The current ordering in the registry is: §VII.AR → §VII.AS → §VII.AQ → §VII.K-PROP-W8-LAYERED.
    # (local) §VII.AT + §VII.AW (newly allocated) go AFTER §VII.AS, BEFORE §VII.AQ.OP-PROJ (which keeps its position).
    # (local) So the insertion point IS just before "## §VII.AQ.OP-PROJ".

    new_registry_text = (
        registry_after_step1[:aq_op_proj_after_step1]
        + vii_at_slot
        + vii_aw_slot
        + registry_after_step1[aq_op_proj_after_step1:]
    )

    content_sha_registry = text_sha256(new_registry_text)  # (local)

    # ============================================================
    # STAGE 3: WRITE registry (atomic + fsync)
    # ============================================================
    print(f"\n[STEP 1+2+3: WRITE REGISTRY ATOMIC + FSYNC]")
    write_atomic_with_fsync(REGISTRY_PATH, new_registry_text)
    print(f"  registry written ({len(new_registry_text)} bytes)")
    print(f"  content_sha256_registry = {content_sha_registry}")

    # ============================================================
    # STAGE 4: STEP 4 — Edit S89 W2 WP CF-A40 plan-block
    # ============================================================
    print(f"\n[STEP 4: Edit S89 W2 WP CF-A40 plan-block]")
    with open(S89_W2_WP, "r", encoding="utf-8") as f:
        s89_w2_text = f.read()  # (local)

    # (local) Replace "convention-shopping framing" with "registry-anatomy hygiene at Element-1"
    # (local) AND add cross-link block to W-5 Q-R-3 + Stage-2 upgrade + §VII.AT + §VII.AW
    # (local) The Methodology note paragraph is at lines 422-424; we add a cross-link addendum after it.
    cf_a40_methodology_anchor = "**Methodology note (Class-8.5 layer-functor F implication)**: The FAIL is NOT a substrate-physics defect"
    cf_a40_idx = s89_w2_text.find(cf_a40_methodology_anchor)
    if cf_a40_idx == -1:
        print(f"  [FAIL] CF-A40 methodology-note anchor not found in S89 W2 WP")
        sys.exit(0)

    # (local) Find the end of the methodology-note paragraph (the next "\n\n---\n" boundary)
    para_end_marker = "Future plan-author can use this to design Class-8.5 binding-axis pre-registration with explicit (canonical-import vs substrate-natural) sub-class declaration AND require alternative-chirality infrastructure when targeting substrate-natural-binding upgrades."
    para_end_idx = s89_w2_text.find(para_end_marker, cf_a40_idx)
    if para_end_idx == -1:
        print(f"  [FAIL] CF-A40 methodology-note paragraph end marker not found")
        sys.exit(0)
    para_end_pos = para_end_idx + len(para_end_marker)  # (local) end of the para

    cf_a40_cross_link_addendum = """

**S90 W7 CF-45 re-scoping addendum (mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`, 2026-05-15)**:

Per S90 W7 CF-45 verdict landing (audit_sha256 forthcoming at verdict-line emission), the CF-A40 FAIL diagnostic is re-scoped from a "convention-shopping framing" concern (which would be PROHIBITED_ACTIONS Class 1 per `v3-closure-recovery.md` if accepted) to a **registry-anatomy hygiene at Element-1** structural concern (legitimate registry-landing discipline question per `cross-pillar-bridge-anatomy.md §"Audit at plan-freeze"`). The re-scoping decomposes the three candidate chirality structures into structurally distinct registry-anatomy slots:

- **Candidate (c) substrate-natural inner-fluctuation 1-form A** — Stage-2-style upgrade clause appended to existing §VII.AQ.OP-PROJ (preserves γ_9 = γ_5 ⊗ γ_F chirality grading per Connes 1996 chirality axiom + Connes-Chamseddine 1996 §2.2-2.3 inner-fluctuation construction; the inner-fluctuation is a DEFORMATION WITHIN the registered §VII.AQ.OP-PROJ spectral triple). S91+ substrate-physics computation deferred per W-5 Q-R-3.

- **Candidate (a) bi-chirality (γ_5 ⊕ γ_F direct-sum)** — NEW §VII.AT.OP-PROJ slot scaffolded with Element-1 specification + Level-1 single-τ-slice declaration + STAGE-0-CANDIDATE-PENDING-S91-SUBSTRATE-PHYSICS status. The bi-chirality MODIFIES the chirality grading (γ_9 → γ_9' = γ_5 ⊕ γ_F direct-sum); this produces a NEW spectral triple registered at a separate §VII slot, NOT a convention choice on §VII.AQ.OP-PROJ.

- **Candidate (b) SU(3)-coloured chirality (γ_F^c per Connes-Marcolli 2008 §11)** — NEW §VII.AW.OP-PROJ slot scaffolded (skipping §VII.AU + §VII.AV which are occupied by CF-63 REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION + CF-W7-1 W7c respectively). The SU(3)-coloured chirality MODIFIES the chirality grading (γ_9 → γ_9'' = γ_F^c colour-dressed); this produces a NEW spectral triple at a separate §VII slot.

The structural distinction between within-spectral-triple deformations (candidate (c)) and across-spectral-triple modifications (candidates (a) + (b)) IS the registry-anatomy hygiene principle the CF-45 re-scoping enforces. Container-thinking violation FORBIDDEN: "We're choosing between three chirality options" — INVERT: "each chirality grading IS a structurally distinct substrate; §VII.AT and §VII.AW register the bi-chirality and SU(3)-coloured chirality substrates as separate spectral-triple slots with their own Element-1 specifications; §VII.AQ.OP-PROJ Stage-2 upgrade extends candidate (c) substrate-natural inner-fluctuation as a deformation WITHIN the registered spectral triple."

**Cross-link to S90 W7 CF-45 landing**:

- `sessions/permanent-results-registry.md` §VII.AQ.OP-PROJ Stage-2-style upgrade clause (candidate (c) substrate-natural inner-fluctuation 1-form A; S91+ deferred per W-5 Q-R-3)
- `sessions/permanent-results-registry.md` §VII.AT.OP-PROJ (NEW; candidate (a) bi-chirality γ_5 ⊕ γ_F direct-sum; STAGE-0-CANDIDATE-PENDING-S91-SUBSTRATE-PHYSICS)
- `sessions/permanent-results-registry.md` §VII.AW.OP-PROJ (NEW; candidate (b) SU(3)-coloured chirality γ_F^c per Connes-Marcolli 2008 §11; STAGE-0-CANDIDATE-PENDING-S91-SUBSTRATE-PHYSICS)
- `sessions/framework/s90-slot-pre-allocation-lockfile.md` (NEW; RESERVED-FOR-WORKSHOP-W7-CF-45-VII-AT + RESERVED-FOR-WORKSHOP-W7-CF-45-VII-AW)
- `sessions/session-plan/session-90-plan-w7.md §W7-6` (lines 1113-1352; CF-45 plan-block)
- W-5 R2 verdict freeze + Q-R-3 substrate-physics deferral + W-5 CF-W5-3 + W-5 CF-W5-5 (S91+ substrate-physics computation specs)
"""

    new_s89_w2_text = (
        s89_w2_text[:para_end_pos]
        + cf_a40_cross_link_addendum
        + s89_w2_text[para_end_pos:]
    )

    content_sha_s89_w2 = text_sha256(new_s89_w2_text)  # (local)
    write_atomic_with_fsync(S89_W2_WP, new_s89_w2_text)
    print(f"  S89 W2 WP written ({len(new_s89_w2_text)} bytes)")
    print(f"  content_sha256_s89_w2 = {content_sha_s89_w2}")

    # ============================================================
    # STAGE 5: STEP 5 — Create slot-allocation lockfile
    # ============================================================
    print(f"\n[STEP 5: Create slot-allocation lockfile]")
    write_atomic_with_fsync(LOCKFILE, lockfile_text)
    content_sha_lockfile = text_sha256(lockfile_text)  # (local)
    print(f"  lockfile written ({len(lockfile_text)} bytes)")
    print(f"  content_sha256_lockfile = {content_sha_lockfile}")

    # ============================================================
    # STAGE 6: RE-READ + VERIFY (all 5 step artifacts)
    # ============================================================
    print(f"\n[RE-READ + VERIFY]")

    expected_registry_substrings = [
        # STEP 1: Stage-2 upgrade clause appended at §VII.AQ.OP-PROJ
        "**Stage-2-style upgrade clause (S90 W7 CF-45",
        "substrate-natural inner-fluctuation 1-form A, candidate (c))",
        "Connes-Chamseddine 1996 §2.2-2.3",
        "S91+ DEFERRED COMPUTATION (per W-5 Q-R-3 + W-5 CF-W5-3)",
        # STEP 2: §VII.AT.OP-PROJ scaffolded
        "## §VII.AT.OP-PROJ — Bi-Chirality Spectral Triple (γ_5 ⊕ γ_F Direct-Sum)",
        "STAGE-0-CANDIDATE-PENDING-S91-SUBSTRATE-PHYSICS",
        "γ_9' = γ_5 ⊕ γ_F",
        "Level 1 (single-τ-slice at τ_fold = 0.190)",
        # STEP 3: §VII.AW.OP-PROJ scaffolded
        "## §VII.AW.OP-PROJ — SU(3)-Coloured Chirality Spectral Triple (γ_F^c per Connes-Marcolli 2008 §11)",
        "γ_9'' = γ_F^c",
        "RESERVED-FOR-WORKSHOP-W7-CF-45-VII-AW",
    ]
    reg_match, reg_total, reg_missing = verify_section_matches(REGISTRY_PATH, expected_registry_substrings)
    print(f"  [registry] match {reg_match}/{reg_total}")
    if reg_missing:
        print(f"  [registry] MISSING: {reg_missing}")

    expected_s89_w2_substrings = [
        "S90 W7 CF-45 re-scoping addendum",
        "registry-anatomy hygiene at Element-1",
        "§VII.AT.OP-PROJ (NEW; candidate (a) bi-chirality",
        "§VII.AW.OP-PROJ (NEW; candidate (b) SU(3)-coloured chirality",
    ]
    s89_match, s89_total, s89_missing = verify_section_matches(S89_W2_WP, expected_s89_w2_substrings)
    print(f"  [s89_w2_wp] match {s89_match}/{s89_total}")
    if s89_missing:
        print(f"  [s89_w2_wp] MISSING: {s89_missing}")

    expected_lockfile_substrings = [
        "S90 Slot Pre-Allocation Lockfile",
        "RESERVED-FOR-WORKSHOP-W7-CF-45-VII-AT",
        "RESERVED-FOR-WORKSHOP-W7-CF-45-VII-AW",
        "§VII.AT.OP-PROJ",
        "§VII.AW.OP-PROJ",
    ]
    lockfile_match, lockfile_total, lockfile_missing = verify_section_matches(LOCKFILE, expected_lockfile_substrings)
    print(f"  [lockfile] match {lockfile_match}/{lockfile_total}")
    if lockfile_missing:
        print(f"  [lockfile] MISSING: {lockfile_missing}")

    total_match = reg_match + s89_match + lockfile_match
    total_expected = reg_total + s89_total + lockfile_total
    verify_passed = (
        reg_match == reg_total
        and s89_match == s89_total
        and lockfile_match == lockfile_total
    )
    print(f"  [TOTAL] match {total_match}/{total_expected}; passed = {verify_passed}")

    # ============================================================
    # STAGE 7: COMPUTE AUDIT_SHA256 (closure over input-pin map)
    # ============================================================
    # (local) Combined content_sha256 over all 3 artifacts
    combined_content_sha = text_sha256(
        content_sha_registry + content_sha_s89_w2 + content_sha_lockfile
    )

    input_pin_map = {
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": str(L_MAX),
        "registry_pre_edit_sha": registry_pre_sha,
        "s89_w2_wp_pre_edit_sha": s89_w2_wp_pre_sha,
        "plan_w7_md_sha": plan_w7_sha,
        "cross_pillar_bridge_anatomy_md_sha": cross_pillar_sha,
        "phononic_framing_md_sha": phononic_framing_sha,
        "epistemic_discipline_md_sha": epistemic_discipline_sha,
        "op_a_audit_sha": OP_A_AUDIT_SHA,
        "op_b_audit_sha": OP_B_AUDIT_SHA,
        "cf_54_audit_sha": CF_54_AUDIT_SHA,
        "cf_55_audit_sha": CF_55_AUDIT_SHA,
        "content_sha256_registry": content_sha_registry,
        "content_sha256_s89_w2": content_sha_s89_w2,
        "content_sha256_lockfile": content_sha_lockfile,
        "combined_content_sha256": combined_content_sha,
        "registry_match_count": str(reg_match),
        "s89_w2_match_count": str(s89_match),
        "lockfile_match_count": str(lockfile_match),
        "total_match": str(total_match),
        "total_expected": str(total_expected),
    }
    audit_sha = closure_hash(input_pin_map)  # (local)

    print(f"\n[AUDIT CLOSURE]")
    print(f"  combined_content_sha256 = {combined_content_sha}")
    print(f"  audit_sha256 = {audit_sha}")

    # ============================================================
    # STAGE 8: EMIT VERDICT LINE
    # ============================================================
    if verify_passed:
        verdict = "PASS"
        value = (
            f"vii_aq_stage_2_upgrade_landed=True;"
            f"vii_at_scaffolded=True;"
            f"vii_aw_scaffolded=True;"
            f"cf_a40_rescoped=True;"
            f"lockfile_present=True;"
            f"registry_verify={reg_match}_of_{reg_total};"
            f"s89_w2_wp_verify={s89_match}_of_{s89_total};"
            f"lockfile_verify={lockfile_match}_of_{lockfile_total};"
            f"total_verify={total_match}_of_{total_expected};"
            f"single_shot_AFTER_pattern=True;"
            f"op_a_input_pin={OP_A_AUDIT_SHA[:16]};"
            f"op_b_input_pin={OP_B_AUDIT_SHA[:16]};"
            f"cf_54_input_pin={CF_54_AUDIT_SHA[:16]};"
            f"cf_55_input_pin={CF_55_AUDIT_SHA[:16]}"
        )
    else:
        verdict = "FAIL"
        all_missing = (reg_missing or []) + (s89_missing or []) + (lockfile_missing or [])
        value = (
            f"chirality_rescope_incomplete;"
            f"total_verify={total_match}_of_{total_expected};"
            f"missing={';'.join(all_missing[:3]) if all_missing else 'none'}"
        )

    print(f"\n[VERDICT EMISSION]")
    print(f"  verdict = {verdict}")
    print(f"  value = {value[:150]}...")

    append_verdict_line(
        VERDICT_PATH, GATE_ID, verdict, value,
        SCHEME, CONVENTION, L_MAX, audit_sha, combined_content_sha,
    )

    print(f"\n[COMPLETE] Verdict line appended to {VERDICT_PATH}")
    sys.exit(0)


if __name__ == "__main__":
    main()
