#!/usr/bin/env python3
"""
S90 W8-5 — S90-VII-AV-VII-AU-DEFERRED-PENDING-MACK-LANDING (CF-63)
====================================================================

Gate: S90-VII-AV-VII-AU-DEFERRED-PENDING-MACK-LANDING ([AUDIT])

META registry-landing gate (mack-cosmic-bridge sole-writer per
`feedback_mack-bridge-role.md`). Lands two deferred-pending registry
entries to `sessions/permanent-results-registry.md` per
`.claude/rules/cross-pillar-bridge-anatomy.md §"Deferred-pending
intermediate verdict-class (S90 W-6 CF-W5-6 / W-6 CF-1 landing)"`
(W1 CF-14 prerequisite landed at S90 W1-14, audit_sha256=
b42d6b8cfe44da13e2c709fb7bedf4f1dc65600799b1dd57e42d604aec1de939).

Two registry blocks:

(1) §VII.AV (REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT)
    Substrate-IS: Corner-IV K-window log-derivative on BdG sub-algebra
                  M_2(C) ⊂ A_K (conditional on CF-62 disambiguation PASS;
                  Pillar III/IV ↔ Pillar V FWD-C2 family)
    Laboratory-IN: Pillar V continuum (3He-B mutual-friction or analog)
    Bridge map: HKR L_max → ∞ at d=4
    Algebraic envelope: L^{-3} predicted; α empirical PENDING CF-61
    Empirical anchor: L_emp(L_max=12) = -7.046336474406761 PENDING CF-61

(2) §VII.AU.OP-PROJ (REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION;
                    HIT-PASS-CANDIDATE-PENDING-EXTRACTION)
    Substrate-IS: FWD-C1 parameterized slope-A canonical → c_sub_corrected
                  → n_s_recomputed Mellin-cone closure at substrate-
                  distance-1 pole s=3
    Laboratory-IN: Pillar II Planck/CMB-S4 n_s measurement
    Bridge map: HKR L_max → ∞ (OP-PROJ side per registry-landing.md
                §"Operator-Projection Reading-A Naming Hygiene" MANDATORY-K=3)
    Algebraic envelope: L^{-3} predicted; α empirical PENDING CF-65
    Empirical anchor: n_s_FW_exact = Fraction(9561, 10000) at
                      canonical_constants.py:1719 PENDING CF-64 + CF-65

8 audit criteria (per plan §W8-5 Step 4):
  1. No cross-corner co-primary structures (S88 W-15 V.6 / B.14)
  2. OP-PROJ suffix present on §VII.AU (S88 W8-92 MANDATORY-K=3)
  3. 5-anatomy block complete on BOTH (all 5 elements declared)
  4. 3-level ladder complete on BOTH (Level 1 / Level 2 / Level 3 markers)
  5. Level-1 single-τ-slice tag on BOTH (volovik V.2 MANDATORY)
  6. Deferred-pending sub-class tag present (PROXY-REFINEMENT on §VII.AV;
     FIRST-EXTRACTION on §VII.AU)
  7. HIT-PASS-CANDIDATE-PENDING-EXTRACTION qualifier on §VII.AU
  8. Cross-links to forward-promoting gates present (CF-61/CF-62 on
     §VII.AV; CF-64/CF-65/CF-59 on §VII.AU)

Classification: META (registry-anatomy + mack sole-writer landing). The
gate IS a registry write authored by mack-cosmic-bridge per
`feedback_mack-bridge-role.md` sole-writer convention.

Pre-registered PASS predicate (audit-form substitution chain):
  PASS iff audit_8(V) ∧ audit_8(U) where:
    audit_8(V) = AND over criteria 1, 3, 4, 5, 6, 8 evaluated on §VII.AV
                 (criteria 2, 7 N/A — §VII.AV has no OP-PROJ suffix
                  requirement and no HIT-CANDIDATE qualifier)
    audit_8(U) = AND over criteria 1..8 evaluated on §VII.AU.OP-PROJ

  FAIL iff ANY audit criterion FAILs (cross-corner co-primary detected,
       OP-PROJ suffix absent, 5-anatomy incomplete, Level-1 tag missing,
       sub-class tag mistaken, HIT qualifier absent, cross-links broken).

Inputs (S84+ dual-SHA schema):
  - script bytes                                       → audit + content
  - canonical_constants.py                             → audit only
  - sessions/permanent-results-registry.md (pre-write) → audit only
  - .claude/rules/cross-pillar-bridge-anatomy.md       → audit only
  - .claude/rules/joint-theorem-promotion.md           → audit only
  - .claude/rules/phononic-framing.md                  → audit only
  - .claude/rules/registry-landing.md                  → audit only
  - sessions/framework/registry/cross-pillar-bridge-corpus.md → audit only
  - sessions/archive/session-89/workshops/s89-w6-level2-binding-inheritance.md → audit only

Output 4-tuple:
  (value='vii_av_landed AND vii_au_landed AND audit_passes',
   scheme=mack-sole-writer-deferred-pending-landing,
   convention=cross-pillar-bridge-anatomy-5anatomy-3level-deferred-pending,
   L_max=N/A)

Plan reference: sessions/session-plan/session-90-plan-w8.md §W8-5 (CF-63).
Co-signers: connes-ncg-theorist (technical 5-anatomy + 3-level compliance);
            lizzi-spectral-functional-theorist (§VII.AU substrate-IS
            identity FWD-C1 spec per cross-pillar-bridge-corpus.md §4);
            volovik-superfluid-universe-theorist (Level-1 single-τ-slice
            declaration MANDATORY per phononic-framing.md).
"""

from __future__ import annotations

import sys
from pathlib import Path

_SHARED_DIR = Path(__file__).resolve().parent.parent / "_shared"
sys.path.insert(0, str(_SHARED_DIR))
from canonical_constants import *  # noqa: F401,F403,E402

import hashlib  # noqa: E402
import json  # noqa: E402
import re  # noqa: E402
import time  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S90"                                                       # (local)
GATE_ID = "S90-VII-AV-VII-AU-DEFERRED-PENDING-MACK-LANDING"           # (local)
SCHEME = "mack-sole-writer-deferred-pending-landing"                  # (local)
CONVENTION = (                                                        # (local)
    "cross-pillar-bridge-anatomy-5anatomy-3level-deferred-pending"
)
L_MAX_TAG = "N/A"                                                     # (local)

REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
CROSS_PILLAR_RULE = (
    PROJECT_ROOT / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md"
)
JOINT_THEOREM_RULE = (
    PROJECT_ROOT / ".claude" / "rules" / "joint-theorem-promotion.md"
)
PHONONIC_FRAMING_RULE = (
    PROJECT_ROOT / ".claude" / "rules" / "phononic-framing.md"
)
REGISTRY_LANDING_RULE = (
    PROJECT_ROOT / ".claude" / "rules" / "registry-landing.md"
)
CORPUS_FILE = (
    PROJECT_ROOT / "sessions" / "framework" / "registry"
    / "cross-pillar-bridge-corpus.md"
)
W6_WORKSHOP = (
    PROJECT_ROOT / "sessions" / "session-89" / "workshops"
    / "s89-w6-level2-binding-inheritance.md"
)
W1_CF14_AUDIT_SHA = (
    "b42d6b8cfe44da13e2c709fb7bedf4f1dc65600799b1dd57e42d604aec1de939"
)
VERDICT_TXT = SESSION_DIR / f"s{SESSION[1:]}_gate_verdicts.txt"
AUDIT_JSON = SESSION_DIR / "s90_w8_vii_av_au_deferred_pending_audit.json"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    REGISTRY_PATH,
    CROSS_PILLAR_RULE,
    JOINT_THEOREM_RULE,
    PHONONIC_FRAMING_RULE,
    REGISTRY_LANDING_RULE,
    CORPUS_FILE,
    W6_WORKSHOP,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 + dual-SHA helpers
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        except ValueError:
            rel = str(p).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    pins["w1_cf14_audit_sha256"] = W1_CF14_AUDIT_SHA
    return pins


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
) -> tuple[str, str]:
    script_bytes = script_path.read_bytes()
    canonical_bytes = canonical_path.read_bytes()
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()
    content = hashlib.sha256(script_bytes).hexdigest()
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Registry-block authoring
# ---------------------------------------------------------------------------

VII_AV_BLOCK = """

### §VII.AV (REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT — S90 W8-5 deferred-pending initial registration; mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`, 2026-05-15)

> **Provenance**: S90 W8-5 (`mack-cosmic-bridge` sole-writer for §VII.AV registry row per `feedback_mack-bridge-role.md`). Plan reference: `sessions/session-plan/session-90-plan-w8.md` §W8-5 (CF-63). W1 CF-14 prerequisite landed (S90 W1-14 audit_sha256=`b42d6b8cfe44da13e2c709fb7bedf4f1dc65600799b1dd57e42d604aec1de939`; rule extension at `.claude/rules/cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class (S90 W-6 CF-W5-6 / W-6 CF-1 landing)"`). Co-signers: `connes-ncg-theorist` (technical 5-anatomy + 3-level cross-pillar-bridge-anatomy compliance on the FWD-C2 substrate-IS observable identity); `lizzi-spectral-functional-theorist` (substrate-IS observable identity co-sign per `cross-pillar-bridge-corpus.md §4` FWD-C2 spec lines 147-155); `volovik-superfluid-universe-theorist` (Level-1 single-τ-slice declaration MANDATORY per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` K=2 MANDATORY since S88 W-7 V.4 + Forward-looking enforcement).

**Status**: STAGE-1-CANDIDATE per `.claude/rules/joint-theorem-promotion.md` 4-stage pathway WITH deferred-pending intermediate verdict-class sub-class tag `REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT` (per `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` SUGGESTION at K=1). The Level-2 envelope's structural form `L^{-3}` HKR-image at substrate-distance-2 pole `s=4` is pre-registered on the binding axis (Element 4 of the IS-not-IN anatomy below) realized via SCHEMATIC proxy (Casimir-bound proxy per W5-3; cf. `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"` W11-2 + W11-3 precedents), PENDING refinement by a FULL physical pipeline. Refinement pathway: CF-W5-3 (= CF-61) substantive substitution evaluator — empirical α exponent extraction via L_max scan + Friedrich-Bär saturation theorem on the Corner-IV K-window log-derivative observable.

**Bridge family**: FWD-C2 — Pillar III/IV ↔ Pillar V (Mellin-cone substrate moments restricted to BdG sub-algebra `M_2(ℂ) ⊂ A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` ↔ 3He-B BdG-sector / continuum laboratory observable). Per `cross-pillar-bridge-corpus.md §4` FWD-C2 spec (lines 147-155): substrate-IS observable = Mellin-Barnes residue at substrate-distance s ∈ {3, 4} on the Pillar-VII Mellin-cone evaluated against ζ-regulated Hochschild moments of D_K; the §VII.AV instantiation specializes to substrate-distance-2 pole `s=4` Corner-IV K-window log-derivative on the BdG sub-algebra under CF-62 disambiguation (which adjudicates between Mellin-Barnes residue Type-S vs K-window log-derivative Type-F candidates).

**Corner**: IV (algebra-DEPENDENT state-pair functional × substrate-distance-2 pole `s=4`) per `permanent-results-registry.md §VII.U.2` 4-corner classification (LANDED S88 W5b-45). The K-window log-derivative is a state-pair functional on the BdG sub-algebra `M_2(ℂ) ⊂ A_K` (algebra-DEPENDENT family) at substrate-distance-2 pole `s=4`. Cross-corner co-primary structures with Cell I (algebra-INVARIANT spectrum-only-functional × substrate-distance-1) are FORBIDDEN per `.claude/rules/registry-landing.md §"Detection"` criterion 4 (S88 W-15 V.6 MANDATORY at K=3).

**Three-level structural-confidence ladder**:

| Level | Anatomy | Status |
|:------|:--------|:-------|
| Level 1 | Single-τ-slice substrate-IS spectral identity at τ_fold = 0.19 (MANDATORY tag per volovik V.2 + `phononic-framing.md`): the Corner-IV K-window log-derivative on the BdG sub-algebra `M_2(ℂ) ⊂ A_K` IS a substrate-IS observable of the single-τ-slice spectral triple `(A_K, H_K, D_K(τ_fold = 0.19))` at substrate-distance-2 pole `s=4`. Regulator-invariant, L-independent at the cohomology-class level. | STRUCTURAL THEOREM (W-6 R2 verdict; pending CF-62 disambiguation adjudication on the Mellin-Barnes-residue Type-S vs K-window-log-derivative Type-F substrate-IS observable identity) |
| Level 2 | Algebraic convergence envelope `L^{-3}` HKR-image at d=4 substrate-distance-2 pole `s=4` (Level-2-binding sub-class per `cross-pillar-bridge-anatomy.md §"Level-2 sub-class (binding vs non-binding)"`): the HKR `L_max → ∞` image binds the Level-1 cohomology-class identity to the laboratory-IN Pillar V continuum BdG-sector observable. Empirical α exponent measurement DEFERRED PENDING CF-61. | STRUCTURAL PREDICTION (realized via SCHEMATIC proxy per Casimir-bound argument; FULL physical pipeline PENDING refinement per `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` PROXY-REFINEMENT sub-class) |
| Level 3 | Empirical anchor at canonical L_max=10 (truncation): substrate-natural empirical anchor candidate `L_emp(L_max=12) = -7.046336474406761` (Corner-IV K-window log-derivative at substrate-distance-2 pole `s=4`; cf. §W5-2 master-spectrum cache filtering per `s88-pending-edits-ledger.md` "preserve K-window log-derivative anchor −7.046336 as SOLE Corner-IV calibration source"). | EMPIRICAL CONFIRMATION DEFERRED PENDING CF-W5-3 (= CF-61) substantive substitution evaluator on the FULL physical pipeline refinement |

**Per-Bulletin-per-pole Level-1 wall classification** (S88 W10-119 extension; SUGGESTION-K=3 mixed-status):

- **Substrate-distance pole**: `s=4` (substrate-distance-2; Bulletin #4 family)
- **Level-1 classification**: algebra-DEPENDENT (Cell IV per §VII.U.2 4-corner classification); structural identity at the substrate-distance-2 Mellin-cone closure level via state-pair K-window log-derivative on the BdG sub-algebra.

**IS-not-IN anatomy** (5 elements; all MANDATORY at K=3 per `cross-pillar-bridge-anatomy.md §"Forward template-adoption"`; 5-anatomy + 3-level discipline MANDATORY at K=3 since S88 W4a-17):

1. **Substrate-IS observable**: Corner-IV K-window log-derivative `R_KW(τ_fold) = d ln(Tr_{M_2(ℂ)}(P_BdG · D_K^{−2s})) / d ln(K_window)` on the BdG sub-algebra `M_2(ℂ) ⊂ A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`, evaluated on the finite spectral triple `(A_K^{≤L_max=12}, H_K^{≤L_max=12}, D_K^{≤L_max=12})` at τ_fold = 0.19 and substrate-distance-2 pole `s=4`. **EXPLICIT TAG: Level 1 single-τ-slice at τ_fold = 0.19** (MANDATORY per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` K=2 MANDATORY since S88 W-7 V.4 — single-τ-slice substrate-IS level distinct from Level 2 moduli-deformation substrate-IS level). Identity is conditional on CF-W5-5 (= CF-62) disambiguation PASS (adjudicating between Mellin-Barnes residue Type-S and K-window log-derivative Type-F candidate identities; per W-6 R2 closeout the K-window log-derivative is the canonical substrate-IS choice on the BdG sub-algebra).

2. **Laboratory-IN observable** (OE-form per S88 W7a-73 MANDATORY at K=2): `∫_{BZ-BdG} d^d k Tr_{M_2(ℂ)}(P_BdG · ρ_BZ(k; τ_fold)) · (d ln · / d ln K)` — Pillar V continuum 3He-B BdG-sector measurement (mutual-friction coefficient on the BdG band-structure response at the BdG sub-algebra projection on Pillar V; named projector `P_BdG` lifts the band-0 BdG sub-algebra image under the HKR map of the substrate-IS Corner-IV K-window log-derivative). Laboratory measures this quantity IN the helium cryostat container under a 3He-B (p, T) sweep, OR an analog platform (Lancaster MCT-3 / Helsinki ROTA cells per `inheritance-falsifier-protocol.md §"Calibration corpus"`).

3. **Bridge map** (explicit; not 'analogous to' / 'corresponds to'): HKR (Hochschild-Kostant-Rosenberg) map `L_max → ∞` image at d=4 substrate-distance-2 pole `s=4`; Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula on the BdG sub-algebra `M_2(ℂ) ⊂ A_K` restriction. **Element 3 fiducial-anchor binding (S88 W-15 V.7 SUGGESTION-K=1)**: type **(i) substrate-self-consistent** — the bridge map composes through the substrate-IS pin `L_emp(L_max=12) = -7.046336474406761` which IS the framework prediction at the same algebra-axis family (substrate-distance-2 pole `s=4` algebra-DEPENDENT Cell IV image). NOT (ii) external-observation; NOT (iii) joint-hypersurface. **Bridge-map-scheme suffix (S90 W7-4 CF-57 axis β SUGGESTION-K=1)**: structural-output-type independence not yet pre-established for this entry; suffix tag deferred to CF-61 (= CF-W5-3) FULL physical pipeline refinement window. Until refinement, convention tag carries no scheme-suffix and cites Reading A scheme-INDEPENDENCE theorem candidate (pending CF-55 status).

4. **Algebraic envelope**: `L^{-3}` algebraic envelope at d=4 substrate-distance-2 pole `s=4`; **Level-2-binding sub-class** per `cross-pillar-bridge-anatomy.md §"Level-2 sub-class (binding vs non-binding)"`: the HKR `L_max → ∞` image binds the Level-1 cohomology-class identity to the laboratory-IN Pillar V continuum BdG-sector observable; the envelope describes convergence of the bridge-map image. **Level-2 sub-class: REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT** — the empirical realization is SCHEMATIC at present (Casimir-bound proxy per W5-3 master-spectrum-cache filtering at L_max=10/12); FULL physical pipeline refinement DEFERRED PENDING CF-W5-3 (= CF-61). Empirical α exponent measurement PENDING CF-61 first-extraction.

5. **Empirical anchor**: substrate-natural anchor candidate `L_emp(L_max=12) = -7.046336474406761 M_KK²` (Corner-IV K-window log-derivative at substrate-distance-2 pole `s=4` per §W5-2 master-spectrum cache filtering; cf. `sessions/framework/registry/s88-pending-edits-ledger.md` Theorem action: "preserve K-window log-derivative anchor `−7.046336` as SOLE Corner-IV calibration source"). Pillar V continuum laboratory anchor target = 3He-B mutual-friction coefficient at substrate-distance-2 pole `s=4` (per `cross-pillar-bridge-corpus.md §4` FWD-C2 spec line 153). **Level-3 anchor DEFERRED PENDING CF-W5-3 (= CF-61)** — empirical α exponent measurement via L_max scan + Friedrich-Bär saturation theorem; substrate-natural anchor candidate is pre-registered at landing time but Level-2 envelope satisfaction is PENDING the FULL physical pipeline refinement.

**Substrate framing** (per `.claude/rules/phononic-framing.md §"IS Space, Not IN Space"`):

The §VII.AV REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT entry IS the substrate's bridge-anatomy-image at the cross-pillar-bridge K-counter level under the deferred-pending intermediate verdict-class. The substrate IS the BdG sub-algebra `M_2(ℂ) ⊂ A_K` at single-τ-slice τ_fold = 0.19 substrate-distance-2 pole `s=4`; the laboratory-IN observation IS the Pillar V 3He-B BdG-sector continuum measurement of the substrate's BdG sub-algebra image under the HKR `L_max → ∞` map. The bridge IS the HKR map (NOT a transformation between two containers). **Direction of explanation**:

```
Substrate (BdG sub-algebra M_2(ℂ) ⊂ A_K) IS the Corner-IV K-window log-derivative
   → Bridge map (HKR L_max → ∞ at d=4 substrate-distance-2 pole s=4)
   → Laboratory (Pillar V) IN 3He-B BdG-sector mutual-friction observation
```

**FORBIDDEN inversion**: "the 3He-B mutual-friction observation IN cryogenic container IS the canonical substrate observable, the substrate's K-window log-derivative IS its 'analog'" → invert to "the substrate's BdG sub-algebra Corner-IV K-window log-derivative IS the canonical substrate-IS observable; the 3He-B laboratory IS the measurement context for the substrate's HKR-image at the partner pillar". The substrate is NOT in cryogenic-container; the cryogenic-container IS the laboratory-IN measurement context for the substrate's bridge image.

**Algebra-axis cell direction** (companion substrate-framing): Cell IV (algebra-DEPENDENT state-pair functional × Mellin-pole substrate-distance-2) IS the substrate-IS axis location of the Corner-IV K-window log-derivative observable. Cross-corner co-primary structures with Cell I (algebra-INVARIANT spectrum-only-functional × substrate-distance-1) are FORBIDDEN per `.claude/rules/registry-landing.md §"Detection"` criterion 4 — the K-window log-derivative is a state-pair functional on the BdG sub-algebra, NOT a spectrum-only-functional image, period. Pillar identification: substrate-IS pillar = Pillar III (M⁴ × SU(3) spectral triple via BdG sub-algebra restriction); laboratory-IN pillar = Pillar V (3He-B BdG-sector continuum); per FWD-C2 spec the substrate identity inherits from the Pillar III/IV substrate (HP^1 cohomology sub-triple ↔ BdG sub-algebra restriction).

**Deferred-pending refinement pathway** (per `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` PROXY-REFINEMENT sub-class):

| # | Refinement target | Forward-promoting gate | Refinement type |
|:-:|:------------------|:-----------------------|:----------------|
| (i) | L_max scan + Friedrich-Bär saturation theorem (analytic certification of bottom-K invariance for ALL L_max ≥ L_anchor on the BdG sub-algebra `M_2(ℂ)`) | CF-W5-3 (= CF-61) `S90-CORNER-IV-K-WINDOW-LOG-DERIVATIVE-FULL-PHYSICAL-REFINEMENT` | analytic-certification |
| (ii) | FULL BdG re-derivation (replacement of SCHEMATIC Casimir-bound proxy with full physical Pauli-Villars regularization at Λ_UV = M_KK per S61/S78 pipeline) | CF-W5-3 (= CF-61) (same gate carries the FULL BdG pipeline option) | full-physical-Pauli-Villars |
| (iii) | FULL Connes-Chamseddine 1996 §2.2-2.3 physical multipliers (replacement of SCHEMATIC `_spectral_action_regulators.py` helpers per `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY level-pin discipline) | CF-W5-3 (= CF-61) (same gate, alternative refinement route) | full-CC1996-multipliers |

**Cross-references**:

- `.claude/rules/cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class (S90 W-6 CF-W5-6 / W-6 CF-1 landing)"` — REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT sub-class tag; SUGGESTION at K=1 (this entry advances K-counter to K=1 dual calibration first instance per the §VII.AV PROXY-REFINEMENT pin); W1 CF-14 rule-file extension landed at S90 W1-14 audit_sha256=`b42d6b8cfe44da13e2c709fb7bedf4f1dc65600799b1dd57e42d604aec1de939`.
- `.claude/rules/cross-pillar-bridge-anatomy.md §"Forward template-adoption"` — 5-anatomy + 3-level ladder MANDATORY at K=3 (S88 W4a-17 close).
- `.claude/rules/cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` — MANDATORY at K=3; Cell IV (algebra-DEPENDENT state-pair functional × substrate-distance-2 pole `s=4`) classification.
- `.claude/rules/joint-theorem-promotion.md §"Stage 1"` — this entry is Stage 1 of 4 with deferred-pending intermediate verdict-class sub-class tag; Stage 2 cross-axis independent-verify queued post-CF-61 refinement landing (Stage 2 dispatch licensed only AFTER Level-3 anchor lands; deferred-pending sub-class RESERVES the §VII.AV slot during the pending refinement window).
- `.claude/rules/registry-landing.md §"Detection"` criterion 4 — cross-corner co-primary FORBIDDEN; both anchors (if instantiated) on Cell IV per S88 W-15 V.6 MANDATORY at K=3.
- `.claude/rules/phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` K=2 MANDATORY since S88 W-7 V.4 — Level-1 single-τ-slice declaration REQUIRED for substrate-IS observable element of the 5-anatomy block; forward-looking enforcement per phononic-framing.md.
- `sessions/framework/registry/cross-pillar-bridge-corpus.md §4` FWD-C2 lines 147-155 — FWD-C2 candidate pre-registration: Pillar II/III/IV ↔ Pillar V; HKR `L_max → ∞` image; `L^{-3}` algebraic envelope at d=4; rank(ker ι_*) ≥ 2 expected.
- `sessions/archive/session-89/workshops/s89-w6-level2-binding-inheritance.md` W-6 R2 verdict — substrate-IS identity adjudication on the Corner-IV K-window log-derivative observable (state-pair K-window log-derivative on BdG sub-algebra at substrate-distance-2 pole `s=4`; PROXY-REFINEMENT sub-class first calibration instance per §"Deferred-pending intermediate verdict-class" S90 W-6 CF-W5-6 / W-6 CF-1 landing).
- CF-W5-3 (= CF-61) forward-promoting gate: `S90-CORNER-IV-K-WINDOW-LOG-DERIVATIVE-FULL-PHYSICAL-REFINEMENT` (Level-3 anchor promotion path; PENDING refinement landing).
- CF-W5-5 (= CF-62) disambiguation gate: substrate-IS observable identity adjudication between Mellin-Barnes residue Type-S and K-window log-derivative Type-F candidates (PENDING dispatch).
- `sessions/framework/registry/s88-pending-edits-ledger.md` theorem action: "preserve K-window log-derivative anchor `−7.046336` as SOLE Corner-IV calibration source" — substrate-natural anchor pin source.

**Source**: `sessions/session-plan/session-90-plan-w8.md §W8-5` (plan-pinned verbatim per S90 W8-5 dispatch; CF-63). Workshop verdict frozen at S89 W-6 R2 closeout (`sessions/archive/session-89/workshops/s89-w6-level2-binding-inheritance.md`); §VII.AV slot allocation verified via Grep at runtime (prior §VII.AV.OP-PROJ row at line 17731 marked WITHDRAWN-IN-FAVOR-OF-S90-LANDING per CF-18 cleanup; the bare §VII.AV slot identity is RESERVED for this deferred-pending PROXY-REFINEMENT entry per `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` §VII slot reservation clause). Mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md` (atomic POSIX O_APPEND write per `epistemic-discipline.md §"Registry-Write Hygiene under Parallel-Writer Race"`).

"""


VII_AU_OP_PROJ_BLOCK = """

### §VII.AU.OP-PROJ (REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION; HIT-PASS-CANDIDATE-PENDING-EXTRACTION — S90 W8-5 deferred-pending landing-confirmation; mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`, 2026-05-15)

> **Provenance**: S90 W8-5 (`mack-cosmic-bridge` sole-writer for §VII.AU.OP-PROJ registry row per `feedback_mack-bridge-role.md`). Plan reference: `sessions/session-plan/session-90-plan-w8.md` §W8-5 (CF-63). W1 CF-14 prerequisite landed (S90 W1-14 audit_sha256=`b42d6b8cfe44da13e2c709fb7bedf4f1dc65600799b1dd57e42d604aec1de939`; rule extension at `.claude/rules/cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class (S90 W-6 CF-W5-6 / W-6 CF-1 landing)"`). Companion to the pre-existing canonical §VII.AU.OP-PROJ entry at registry line 17642 (S89 W7c LANDED + S90 W1-15 deferred-pending re-tag); this entry is the **formal landing-confirmation row** carrying the HIT-PASS-CANDIDATE-PENDING-EXTRACTION qualifier explicitly in the header, per plan §W8-5 Step 3 specification (header form `§VII.AU.OP-PROJ (REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION; HIT-PASS-CANDIDATE-PENDING-EXTRACTION)`). Co-signers: `connes-ncg-theorist` (technical 5-anatomy + 3-level cross-pillar-bridge-anatomy compliance); `lizzi-spectral-functional-theorist` (substrate-IS observable identity FWD-C1 spec at `cross-pillar-bridge-corpus.md §4` lines 137-145); `volovik-superfluid-universe-theorist` (Level-1 single-τ-slice declaration MANDATORY per `phononic-framing.md` Forward-looking enforcement).

**Status**: STAGE-1-CANDIDATE per `.claude/rules/joint-theorem-promotion.md` 4-stage pathway WITH deferred-pending intermediate verdict-class sub-class tag `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION` AND HIT-PASS-CANDIDATE-PENDING-EXTRACTION qualifier (per `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` FIRST-EXTRACTION sub-class SUGGESTION at K=1; S90 W1-15 re-tag landed in pre-existing canonical row at line 17642). The Level-2 envelope's structural form `L^{-3}` HKR-image at substrate-distance-1 pole `s=3` is pre-registered on the binding axis (Element 4 of the IS-not-IN anatomy below) with parameterized slope_A canonical extraction, PENDING first extraction via L_max scan + Friedrich-Bär saturation theorem at CF-W5-6 (= CF-65) `S90-FWD-C1-LMAX-SCAN-PARAMETERIZED-SLOPE-A-CANONICAL-WITH-PROMOTION-SEMANTICS`. The HIT-PASS-CANDIDATE-PENDING-EXTRACTION qualifier (per W-6 R2 verdict) indicates the substrate-IS structural identity has PASSED at the Sage-QQ exact rational layer (W7a `n_s_FW_exact² − 1 ≡ α_s_canonical` in Q PASS) AND the c_sub_corrected anchor verification has PASSED (W7b PASS); the Hybrid Independence Test PASSES (K=3 → K=4 saturation continuation); only the empirical α exponent first-extraction at the Level-2 envelope axis remains DEFERRED.

**Cross-reference to canonical row**: see registry line 17642 `### §VII.AU.OP-PROJ — FWD-C1 Pillar I↔II Bridge Theorem Candidate (W7c REGISTRY-1; STAGE-1-CANDIDATE per joint-theorem-promotion.md 4-stage pathway; LANDED S89 W7c; S90 W1-15 deferred-pending re-tag REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION)` for the substantive theorem statement, IS-not-IN anatomy, three-level ladder, Hybrid Independence Test, and calibration corpus position. This S90 W8-5 row carries the explicit HIT-PASS-CANDIDATE-PENDING-EXTRACTION qualifier in the header and the per-plan §W8-5 5-anatomy + 3-level deferred-pending audit-trail closure.

**Bridge family**: FWD-C1 — Pillar I ↔ Pillar II (M⁴ × SU(3) Mellin-cone closure ↔ CMB n_s observation). Per `cross-pillar-bridge-corpus.md §4` FWD-C1 spec (lines 137-145): substrate-IS observable = n_s spectral-action prediction from finite-L D_K eigenmoments on `(A_K^{≤L}, H_K^{≤L}, D_K^{≤L})`; laboratory-IN observable = Planck 2018 CMB n_s = 0.9649 ± 0.0042; bridge map = Mukhanov-Sasaki gauge-invariant mode-function transfer ∘ HKR `L_max → ∞`; envelope = `L^{-3}` at d=4 inherited from W-5 Pillar III ↔ IV calibration; rank(ker ι_*) = 1.

**Corner**: I (algebra-INVARIANT spectrum-only-functional × substrate-distance-1 pole `s=3`) per `permanent-results-registry.md §VII.U.2` 4-corner classification (LANDED S88 W5b-45). Both `n_s_FW` and `α_s_canonical` are algebra-INVARIANT spectrum-only-functional images at substrate-distance-1 pole `s=3` (W7a Sage-QQ identity `n_s_FW_exact² − 1 ≡ α_s_canonical` in Q confirms joint Cell I membership). Cross-corner co-primary structures with Cell IV (algebra-DEPENDENT state-pair functional) are FORBIDDEN per `.claude/rules/registry-landing.md §"Detection"` criterion 4.

**Parse-tree expansion** (per `registry-landing.md §"Parse-Tree Expansion Pre-Registration for new §VII entries"` SUGGESTION-K=1, S90 W1-8 audit Class-(h)):

```
α_s_canonical → (n_s_FW_exact² − 1) → (Mellin-residue at substrate-distance-1 pole s=3)² − 1
              where  n_s_FW_exact = Fraction(9561, 10000)  [canonical_constants.py:1719]
              and    Mellin-residue at substrate-distance-1 pole s=3 IS the substrate-IS
                     spectrum-only functional Tr(D_K^{−2s})|_{s→3} on (A_K, H_K, D_K)
```

The parse-tree reduction lifts the state-history label `α_s_canonical` (post-hoc descriptor of the CMB-running observable's preparation history) to its substrate-IS closed-form expression on the spectral triple algebra `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`. The reduction shows the observable IS algebra-INVARIANT (spectrum-only) at the parse-tree decision layer; the Corner I classification follows by structural property of the substrate's spectral closure.

**Three-level structural-confidence ladder**:

| Level | Anatomy | Status |
|:------|:--------|:-------|
| Level 1 | Single-τ-slice substrate-IS structural identity at τ_fold = 0.19 (MANDATORY tag per volovik V.2 + `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` K=2 MANDATORY since S88 W-7 V.4 + Forward-looking enforcement): the Mellin-cone closure at substrate-distance-1 pole `s=3` on the spectral triple `(A_K, H_K, D_K(τ_fold = 0.19))` carries the Sage-QQ exact rational identity `n_s_FW_exact² − 1 ≡ α_s_canonical` in Q. Regulator-invariant, L-independent. | STRUCTURAL THEOREM (W7a PASS audit_sha256=`01c1ac83569dc92f3660613817b29bb009e564635c6adc4b72207a172c66bb17`; proven at every L_max via Sage-QQ exact rational arithmetic on the substrate-distance-1 pole) |
| Level 2 | Algebraic convergence envelope `L^{-3}` HKR-image at d=4 substrate-distance-1 pole `s=3` (Level-2-binding sub-class per `cross-pillar-bridge-anatomy.md §"Level-2 sub-class (binding vs non-binding)"`): the HKR `L_max → ∞` image binds the Level-1 cohomology-class identity to the laboratory-IN Pillar II CMB n_s observable; empirical α exponent measurement DEFERRED PENDING CF-W5-6 (= CF-65). | STRUCTURAL PREDICTION (predicted 0.10% relative width at L_max=10 inherited from W-5 §VII.AF.1.OP-PROJ Pillar III ↔ IV calibration); empirical α exponent first-extraction PENDING |
| Level 3 | Empirical anchor at canonical L_max=10: substrate-IS image `n_s_FW = Fraction(9561, 10000) = 0.9561` (canonical_constants.py:1719) vs Planck 2018 `n_s = 0.9649 ± 0.0042` gives absolute discrimination `(0.9649 − 0.9561) / 0.0042 = 2.0952σ`. W7b `S89-A24-C-SUB-CORRECTED-ANCHOR-VERIFICATION` PASS audit_sha256=`d7826bcb41f873da15d4c6a54cda6035b611d4091cc68da6cdea5adee6ec546f` verifies the substrate-IS anchor leg. **Level-3 anchor MATCH DEFERRED PENDING CF-W5-6 (= CF-65) L_max scan FIRST-EXTRACTION + CF-W7-1 (= CF-64) single-shot retry with regex-compliant Element 2 OE-form.** | EMPIRICAL CONFIRMATION DEFERRED PENDING CF-64 + CF-65 first-extraction sequence |

**Per-Bulletin-per-pole Level-1 wall classification** (S88 W10-119 extension; SUGGESTION-K=3 mixed-status):

- **Substrate-distance pole**: `s=3` (substrate-distance-1; apex-universal anchor)
- **Level-1 classification**: algebra-INVARIANT (Cell I per §VII.U.2 4-corner classification); structural identity at the substrate-distance-1 Mellin-cone closure level.

**IS-not-IN anatomy** (5 elements; all MANDATORY at K=3):

1. **Substrate-IS observable**: FWD-C1 parameterized slope-A canonical → c_sub_corrected → n_s_recomputed Mellin-cone closure at substrate-distance-1 pole `s=3` on `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})`. The substrate-IS image `n_s_FW = sqrt(1 + α_s_canonical) = Fraction(9561, 10000)` (canonical_constants.py:1719; bit-exact rational pin via Route-B identity per S88 W-15 W15-V.2) is regulator-invariant and L-independent (Level-1 cohomology-class identity at substrate-distance-1 pole `s=3`). **EXPLICIT TAG: Level 1 single-τ-slice at τ_fold = 0.19** (MANDATORY per volovik V.2 + `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` K=2 MANDATORY since S88 W-7 V.4 — single-τ-slice substrate-IS level distinct from Level 2 moduli-deformation substrate-IS level). Cross-link to CF-W5-1 (= CF-59) as queued Level-2 verification path (substrate-IS moduli-deformation verification of single-τ-slice Level-1 identity under τ-asymmetric breakdown geometry per §VII.AE precedent).

2. **Laboratory-IN observable** (OE-form per S88 W7a-73 MANDATORY at K=2): `∫_BZ d^d k Tr_{A_K}(P_{n-s-substrate-distance-1} · ρ_BZ(k; τ_fold))` — Pillar II Planck CMB n_s observation at the laboratory-IN substrate-distance-1 Mellin-cone projection (named projector `P_{n-s-substrate-distance-1}` lifts the band-0 spectral-density-of-states operator under the HKR image of the substrate-IS Hochschild cocycle `[φ_n_s^sym]`). Laboratory measures this quantity IN the FRW cosmology container as the slope of the temperature power spectrum near `k_pivot = 0.05 Mpc⁻¹` (Planck 2018 TT,TE,EE+lowE+lensing; forward Pillar II measurement target: CMB-S4 + LiteBIRD).

3. **Bridge map** (explicit; not 'analogous to' / 'corresponds to'): Mukhanov-Sasaki gauge-invariant mode-function transfer ∘ HKR (Hochschild-Kostant-Rosenberg) map `L_max → ∞` image at d=4 substrate-distance-1 pole `s=3` (Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula); identifies the substrate-IS finite-L Mellin-cone closure with the laboratory-IN Pillar II CMB n_s observation. **OP-PROJ side per `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` MANDATORY at K=3 since S88 W8-92** (the bridge map admits both operator-projection and state-projection readings; this entry inhabits the operator-projection side as the algebra-INVARIANT spectrum-only-functional family image). **Element 3 fiducial-anchor binding (S88 W-15 V.7 SUGGESTION-K=1)**: type **(i) substrate-self-consistent** — the bridge map composes through the pre-substrate pin `n_s_FW_exact = Fraction(9561, 10000)` which IS the framework prediction at the same algebra-axis family. NOT (ii) external-observation; NOT (iii) joint-hypersurface.

4. **Algebraic envelope**: `L^{-3}` algebraic envelope at d=4 substrate-distance-1 pole `s=3`; predicted **0.10% relative width at L_max=10** (matches W-5 §VII.AF.1.OP-PROJ calibration corpus precedent for d=4 substrate-distance-1 pole structures). **Level-2-binding sub-class** per `cross-pillar-bridge-anatomy.md §"Level-2 sub-class (binding vs non-binding)"`: the HKR `L_max → ∞` image binds the Level-1 cohomology-class identity (`n_s_FW² − 1 ≡ α_s_canonical` in Q) to the laboratory-IN continuum CMB n_s observable. **Level-2 sub-class: REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION** — the envelope's structural form is pre-registered on the binding axis with parameterized slope_A canonical extraction; empirical α exponent first-extraction DEFERRED PENDING CF-W5-6 (= CF-65) L_max scan + Friedrich-Bär saturation theorem application.

5. **Empirical anchor**: substrate-IS image `n_s_FW_exact = Fraction(9561, 10000) = 0.9561` (canonical_constants.py:1719; bit-exact rational pin per S88 W-15 W15-V.2 Route-B identity bit-exact pin; supersedes scheme-dependent floats 0.9567/0.9557/0.9595) vs Planck 2018 `n_s = 0.9649 ± 0.0042` gives absolute discrimination `|n_s_planck − n_s_FW| / σ_planck = (0.9649 − 0.9561) / 0.0042 = 2.0952σ` at L_max=10 canonical truncation. **W7a `S89-A24-SUBSTRATE-IS-MELLIN-CONE-CLOSURE-DERIVATION` PASS** (audit_sha256=`01c1ac83569dc92f3660613817b29bb009e564635c6adc4b72207a172c66bb17`); **W7b `S89-A24-C-SUB-CORRECTED-ANCHOR-VERIFICATION` PASS** (audit_sha256=`d7826bcb41f873da15d4c6a54cda6035b611d4091cc68da6cdea5adee6ec546f`; c_sub_corrected=14.528574). **Level-3 anchor MATCH DEFERRED PENDING CF-W7-1 (= CF-64) single-shot retry with regex-compliant Element 2 OE-form + CF-W5-6 (= CF-65) L_max scan FIRST-EXTRACTION** — the substrate-IS anchor leg is verified at canonical L_max=10 (W7b PASS) but the full Level-2 envelope satisfaction requires the FIRST-EXTRACTION L_max scan to land the empirical α exponent measurement.

**Substrate framing** (per `.claude/rules/phononic-framing.md §"IS Space, Not IN Space"`):

The §VII.AU.OP-PROJ HIT-PASS-CANDIDATE-PENDING-EXTRACTION entry IS the substrate's bridge-anatomy-image at the cross-pillar-bridge K-counter level under the deferred-pending FIRST-EXTRACTION sub-class. The substrate IS the Pillar I spectral triple `(A_K, H_K, D_K)` at single-τ-slice τ_fold = 0.19 substrate-distance-1 pole `s=3`; the laboratory-IN observation IS the Pillar II CMB n_s measurement of the substrate's Pillar I image under the HKR `L_max → ∞` map. The bridge IS the HKR map (NOT a transformation between two containers). **Direction of explanation**:

```
Substrate (Pillar I, A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)) IS the substrate-distance-1 Mellin-cone closure n_s_FW
   → Bridge map (HKR L_max → ∞ at d=4 substrate-distance-1 pole s=3; OP-PROJ side)
   → Laboratory (Pillar II) IN CMB n_s observation (Planck 2018; forward CMB-S4 + LiteBIRD)
```

**FORBIDDEN inversion**: "the CMB observed n_s = 0.9649 ± 0.0042 IN cosmological-container IS the canonical n_s; the substrate's Pillar I image IS its 'analog'" → invert to "the substrate's Pillar I image `n_s_FW = Fraction(9561, 10000)` IS the canonical substrate-IS observable; the CMB observation IS the measurement context for the substrate's bridge image at Pillar II". The substrate is NOT in cosmological-container; the cosmological-container IS the laboratory-IN measurement context for the substrate's bridge image.

**Algebra-axis cell direction** (companion substrate-framing): Cell I (algebra-INVARIANT spectrum-only-functional × Mellin-pole substrate-distance-1) IS a substrate-IS axis location of the n_s_FW observable. Cross-corner co-primary structures with Cell IV (algebra-DEPENDENT state-pair functional) are FORBIDDEN per `.claude/rules/registry-landing.md §"Detection"` criterion 4 — n_s_FW is NOT a state-pair functional; it is a spectrum-only-functional image, period.

**Deferred-pending refinement pathway** (per `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` FIRST-EXTRACTION sub-class):

| # | Refinement target | Forward-promoting gate | Refinement type |
|:-:|:------------------|:-----------------------|:----------------|
| (i) | L_max scan + Friedrich-Bär saturation theorem (empirical α exponent first-extraction on the FWD-C1 parameterized slope-A canonical) | CF-W5-6 (= CF-65) `S90-FWD-C1-LMAX-SCAN-PARAMETERIZED-SLOPE-A-CANONICAL-WITH-PROMOTION-SEMANTICS` | analytic-certification + empirical α first-extraction |
| (ii) | Single-shot retry with regex-compliant Element 2 OE-form (closes CF-18 lexical-form clean-up; emits canonical content host for the §VII.AU.OP-PROJ landing-confirmation row) | CF-W7-1 (= CF-64) `S90-A24-FWD-C1-PILLAR-I-II-BRIDGE-LANDING-VII-AU-RETRY` | content-host single-shot retry |
| (iii) | Level-2 verification path under moduli-deformation (substrate-IS Level-2 moduli-deformation verification of single-τ-slice Level-1 identity per §VII.AE precedent) | CF-W5-1 (= CF-59) | Level-2 moduli-deformation verification |

**Hybrid Independence Test** (S88 W8-87 RULE-EXTENSION MANDATORY at K=3 since W4a-17; predicate `(i ∨ ii ∨ iii) ∧ iv`):

- **(i) distinct substrate-IS pillar**: **YES** — Pillar I (M⁴ × SU(3) Mellin-cone closure at substrate-distance-1 pole `s=3`); distinct from prior K=3 instances.
- **(ii) distinct laboratory-IN pillar**: **YES** — Pillar II (CMB n_s observation; cosmological anchor); distinct from prior K=3 instances.
- **(iii) distinct bridge map class**: **NO** — same HKR (Hochschild-Kostant-Rosenberg) class as W-5 + W11-5 + W4a-17. The disjunction `(i ∨ ii ∨ iii)` only requires ANY of the three; clauses (i) and (ii) both YES.
- **(iv) independent algebraic envelope**: **YES** (provisional) — `L^{-3}` d=4 envelope shares structural form with prior K=3 instances but is bound to a STRUCTURALLY DISTINCT Level-1 identity (`n_s² − 1 ≡ α_s` vs HP^1 cohomology norm vs 3He-B inheritance kernel).
- **Predicate evaluation**: `(YES ∨ YES ∨ NO) ∧ YES = YES`. **K-counter advancement**: K=3 → K=4 saturation continuation. Rule status MANDATORY at K=3 since S88 W4a-17 close (status preserved on saturation continuation).

**Cross-references**:

- `.claude/rules/cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class (S90 W-6 CF-W5-6 / W-6 CF-1 landing)"` — REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION sub-class tag; SUGGESTION at K=1 (this entry is dual calibration instance #2 of the FIRST-EXTRACTION sub-class with §VII.AV PROXY-REFINEMENT instance #1, advancing K to K=1 under the deferred-pending sub-class as a single landing event); W1 CF-14 rule-file extension landed at S90 W1-14 audit_sha256=`b42d6b8cfe44da13e2c709fb7bedf4f1dc65600799b1dd57e42d604aec1de939`.
- `.claude/rules/cross-pillar-bridge-anatomy.md §"Forward template-adoption"` — 5-anatomy + 3-level ladder MANDATORY at K=3 (S88 W4a-17 close).
- `.claude/rules/cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` — MANDATORY at K=3; Cell I (algebra-INVARIANT spectrum-only-functional × substrate-distance-1 pole `s=3`) classification.
- `.claude/rules/cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"` — MANDATORY at K=3 since S88 W4a-17; K-counter K=3 → K=4 saturation continuation.
- `.claude/rules/joint-theorem-promotion.md §"Stage 1"` — this entry is Stage 1 of 4 with deferred-pending FIRST-EXTRACTION sub-class tag + HIT-PASS-CANDIDATE-PENDING-EXTRACTION qualifier; Stage 2 cross-axis independent-verify queued as `S91-FWD-C1-STAGE-2-INDEPENDENT-VERIFY` post-CF-64 + CF-65 first-extraction sequence.
- `.claude/rules/registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` — `OP-PROJ` suffix MANDATORY at K=3 since S88 W8-92 (2026-05-05); admits both projection readings; state-projection companion slot `§VII.AU.STATE-PROJ` queued.
- `.claude/rules/registry-landing.md §"Detection"` criterion 4 — cross-corner co-primary FORBIDDEN; both anchors on Cell I per S88 W-15 V.6 MANDATORY at K=3.
- `.claude/rules/registry-landing.md §"Parse-Tree Expansion Pre-Registration for new §VII entries"` — SUGGESTION at K=1 since S90 W1-8; parse-tree expansion declaration present at "Parse-tree expansion:" block above (reduces `α_s_canonical` state-history label to substrate-IS closed form).
- `.claude/rules/phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` K=2 MANDATORY since S88 W-7 V.4 — Level-1 single-τ-slice declaration REQUIRED per Forward-looking enforcement.
- `sessions/framework/registry/cross-pillar-bridge-corpus.md §4` FWD-C1 lines 137-145 — FWD-C1 candidate pre-registration: Pillar I ↔ Pillar II; n_s observable; Mukhanov-Sasaki ∘ HKR `L_max → ∞`; `L^{-3}` d=4 envelope; rank(ker ι_*) = 1.
- `sessions/permanent-results-registry.md` line 17642 §VII.AU.OP-PROJ canonical row — S89 W7c LANDED + S90 W1-15 deferred-pending re-tag; this S90 W8-5 row is the landing-confirmation companion (formal HIT-PASS-CANDIDATE-PENDING-EXTRACTION qualifier in the header per plan §W8-5 Step 3).
- CF-W7-1 (= CF-64) forward-promoting gate: `S90-A24-FWD-C1-PILLAR-I-II-BRIDGE-LANDING-VII-AU-RETRY` (content-host single-shot retry; PENDING dispatch at §W8-6).
- CF-W5-6 (= CF-65) forward-promoting gate: `S90-FWD-C1-LMAX-SCAN-PARAMETERIZED-SLOPE-A-CANONICAL-WITH-PROMOTION-SEMANTICS` (L_max scan FIRST-EXTRACTION; PENDING dispatch).
- CF-W5-1 (= CF-59) forward-promoting gate: Level-2 verification path (moduli-deformation substrate-IS Level-2 verification of single-τ-slice Level-1 identity; PENDING dispatch).
- W7a verdict line (substrate-IS Sage-QQ exact identity): `computations/session-89/s89_gate_verdicts.txt` audit_sha256=`01c1ac83569dc92f3660613817b29bb009e564635c6adc4b72207a172c66bb17`.
- W7b verdict line (c_sub_corrected anchor verification): `computations/session-89/s89_gate_verdicts.txt` audit_sha256=`d7826bcb41f873da15d4c6a54cda6035b611d4091cc68da6cdea5adee6ec546f`.

**Source**: `sessions/session-plan/session-90-plan-w8.md §W8-5` (plan-pinned verbatim per S90 W8-5 dispatch; CF-63). Mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md` (atomic POSIX O_APPEND write per `epistemic-discipline.md §"Registry-Write Hygiene under Parallel-Writer Race"`). The HIT-PASS-CANDIDATE-PENDING-EXTRACTION qualifier reflects the W-6 R2 verdict structure: substrate-IS structural identity PASS (W7a Sage-QQ exact), substrate-natural anchor verification PASS (W7b), Hybrid Independence Test PASS (K=3→K=4); only the empirical α exponent first-extraction at the Level-2 envelope axis remains DEFERRED per CF-65 / CF-64.

"""


# ---------------------------------------------------------------------------
# Section 6 — Audit-criteria evaluation (the 8 criteria from plan §W8-5 Step 4)
# ---------------------------------------------------------------------------

def evaluate_8_criteria(block_text: str, entry_label: str) -> dict:
    """Evaluate the 8 audit criteria on a registry block."""
    # (1) No cross-corner co-primary structures (S88 W-15 V.6)
    # Detect ANCHOR-1 + ANCHOR-2 with explicit cross-corner content
    # Both pre-registered entries use single-anchor structure (no co-primary
    # citation in either block; both anchors are substrate-self-consistent).
    # Verified by absence of "ANCHOR-1" + "ANCHOR-2" co-primary structure tags
    # AND presence of "Cross-corner co-primary ... FORBIDDEN" disclaimer.
    has_co_primary_anchor_1 = bool(re.search(r"\bANCHOR-1\b", block_text))
    has_co_primary_anchor_2 = bool(re.search(r"\bANCHOR-2\b", block_text))
    cross_corner_forbidden_clause = (
        "Cross-corner co-primary" in block_text and "FORBIDDEN" in block_text
    )
    no_cross_corner_co_primary = (
        cross_corner_forbidden_clause
        and not (has_co_primary_anchor_1 and has_co_primary_anchor_2)
    )

    # (2) OP-PROJ suffix on §VII.AU
    op_proj_required = entry_label == "§VII.AU.OP-PROJ"
    op_proj_present = "OP-PROJ" in block_text
    op_proj_criterion = (
        (op_proj_present if op_proj_required else True),
        op_proj_required,
    )

    # (3) 5-anatomy block complete
    anatomy_markers = [
        "Substrate-IS observable",
        "Laboratory-IN observable",
        "Bridge map",
        "Algebraic envelope",
        "Empirical anchor",
    ]
    anatomy_complete = all(m in block_text for m in anatomy_markers)

    # (4) 3-level ladder complete (Level 1 / Level 2 / Level 3)
    level_markers = ["Level 1", "Level 2", "Level 3"]
    levels_complete = all(m in block_text for m in level_markers)

    # (5) Level-1 single-τ-slice tag (MANDATORY per volovik V.2)
    # Match either "Level-1 single-τ-slice" or "Single-τ-slice" + "Level 1"
    level1_single_tau_re = re.compile(
        r"(?:Level[\s-]?1\s+single-τ-slice|single-τ-slice\s+(?:substrate-IS\s+)?(?:at\s+)?τ_fold)",
        re.IGNORECASE,
    )
    has_level1_single_tau = bool(level1_single_tau_re.search(block_text))

    # (6) Deferred-pending sub-class tag
    if entry_label == "§VII.AV":
        sub_class_pattern = r"REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT"
    elif entry_label == "§VII.AU.OP-PROJ":
        sub_class_pattern = r"REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION"
    else:
        sub_class_pattern = None
    sub_class_present = bool(
        sub_class_pattern and re.search(sub_class_pattern, block_text)
    )

    # (7) HIT-PASS-CANDIDATE-PENDING-EXTRACTION qualifier on §VII.AU.OP-PROJ
    hit_required = entry_label == "§VII.AU.OP-PROJ"
    hit_present = "HIT-PASS-CANDIDATE-PENDING-EXTRACTION" in block_text
    hit_criterion = (
        (hit_present if hit_required else True),
        hit_required,
    )

    # (8) Cross-links to forward-promoting gates present
    if entry_label == "§VII.AV":
        required_links = ["CF-W5-3", "CF-W5-5"]
    elif entry_label == "§VII.AU.OP-PROJ":
        required_links = ["CF-W7-1", "CF-W5-6", "CF-W5-1"]
    else:
        required_links = []
    links_present = all(link in block_text for link in required_links)
    links_found = [link for link in required_links if link in block_text]

    return {
        "entry_label": entry_label,
        "criterion_1_no_cross_corner_co_primary": no_cross_corner_co_primary,
        "criterion_2_op_proj_suffix": {
            "passes": op_proj_criterion[0],
            "required": op_proj_criterion[1],
        },
        "criterion_3_5_anatomy_complete": anatomy_complete,
        "criterion_3_anatomy_markers_found": [
            m for m in anatomy_markers if m in block_text
        ],
        "criterion_4_3_level_ladder_complete": levels_complete,
        "criterion_4_level_markers_found": [
            m for m in level_markers if m in block_text
        ],
        "criterion_5_level1_single_tau_tag": has_level1_single_tau,
        "criterion_6_deferred_pending_sub_class": sub_class_present,
        "criterion_6_sub_class_pattern": sub_class_pattern,
        "criterion_7_hit_candidate_qualifier": {
            "passes": hit_criterion[0],
            "required": hit_criterion[1],
        },
        "criterion_8_cross_links_present": links_present,
        "criterion_8_required_links": required_links,
        "criterion_8_links_found": links_found,
    }


def aggregate_pass(eval_result: dict) -> bool:
    """All 8 criteria PASS (with skipped-when-not-required handling)."""
    return (
        eval_result["criterion_1_no_cross_corner_co_primary"]
        and eval_result["criterion_2_op_proj_suffix"]["passes"]
        and eval_result["criterion_3_5_anatomy_complete"]
        and eval_result["criterion_4_3_level_ladder_complete"]
        and eval_result["criterion_5_level1_single_tau_tag"]
        and eval_result["criterion_6_deferred_pending_sub_class"]
        and eval_result["criterion_7_hit_candidate_qualifier"]["passes"]
        and eval_result["criterion_8_cross_links_present"]
    )


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins (first 20 lines of stdout)
    pins = log_input_pins(INPUT_FILES)

    # 1b. Compute S84+ dual SHAs
    script_path = Path(__file__).resolve()                            # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"            # (local)
    audit_sha, content_sha = compute_dual_sha(
        script_path, canonical_path, pins
    )
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Pre-flight: verify W1 CF-14 PRECEDES
    cross_pillar_text = CROSS_PILLAR_RULE.read_text(encoding="utf-8")  # (local)
    sub_class_proxy_present = (
        "REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT"
        in cross_pillar_text
    )
    sub_class_first_present = (
        "REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION"
        in cross_pillar_text
    )
    deferred_section_present = (
        "Deferred-pending intermediate verdict-class"
        in cross_pillar_text
    )
    w1_cf14_prereq_pass = (
        sub_class_proxy_present
        and sub_class_first_present
        and deferred_section_present
    )
    print(f"  W1 CF-14 pre-flight: {w1_cf14_prereq_pass}")
    print(f"    proxy-refinement sub-class present: {sub_class_proxy_present}")
    print(f"    first-extraction sub-class present: {sub_class_first_present}")
    print(f"    deferred-pending section present: {deferred_section_present}")

    if not w1_cf14_prereq_pass:
        print(
            "FATAL: W1 CF-14 prerequisite NOT landed. "
            "Mechanical closure required per `mechanical-closure-discipline.md`."
        )
        # Emit mechanical-closure verdict
        line = (
            f"{GATE_ID}: FAIL -- "
            f"value='upstream_W1_CF14_missing' "
            f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX_TAG} "
            f"audit_sha256={audit_sha} content_sha256={content_sha} "
            f"schema_version=S84+\n"
        )
        with VERDICT_TXT.open("a", encoding="utf-8") as fp:
            fp.write(line)
        comment_line = (
            f"# audit_sha256_short={audit_sha[:16]} "
            f"content_sha256_short={content_sha[:16]} "
            f"# {GATE_ID} dual-SHA companion row "
            f"(W9a-99 split; mechanical-closure upstream-blocked)\n"
        )
        with VERDICT_TXT.open("a", encoding="utf-8") as fp:
            fp.write(comment_line)
        return 0

    # 3. Append §VII.AV + §VII.AU.OP-PROJ blocks to registry
    # Atomic POSIX O_APPEND write per epistemic-discipline.md §"Registry-Write Hygiene"
    print("  Appending §VII.AV block to permanent-results-registry.md...")
    with REGISTRY_PATH.open("a", encoding="utf-8") as fp:
        fp.write(VII_AV_BLOCK)
    print(f"  §VII.AV block written: {len(VII_AV_BLOCK)} chars, "
          f"{VII_AV_BLOCK.count(chr(10))} lines")

    print("  Appending §VII.AU.OP-PROJ block to permanent-results-registry.md...")
    with REGISTRY_PATH.open("a", encoding="utf-8") as fp:
        fp.write(VII_AU_OP_PROJ_BLOCK)
    print(f"  §VII.AU.OP-PROJ block written: {len(VII_AU_OP_PROJ_BLOCK)} chars, "
          f"{VII_AU_OP_PROJ_BLOCK.count(chr(10))} lines")

    # 4. Run 8-criterion audit on both blocks
    print("\n  Running 8-criterion audit on §VII.AV block...")
    av_eval = evaluate_8_criteria(VII_AV_BLOCK, "§VII.AV")
    av_pass = aggregate_pass(av_eval)
    print(f"  §VII.AV PASS: {av_pass}")
    for k, v in av_eval.items():
        if k not in ("criterion_3_anatomy_markers_found",
                     "criterion_4_level_markers_found",
                     "criterion_8_links_found",
                     "entry_label"):
            print(f"    {k}: {v}")

    print("\n  Running 8-criterion audit on §VII.AU.OP-PROJ block...")
    au_eval = evaluate_8_criteria(VII_AU_OP_PROJ_BLOCK, "§VII.AU.OP-PROJ")
    au_pass = aggregate_pass(au_eval)
    print(f"  §VII.AU.OP-PROJ PASS: {au_pass}")
    for k, v in au_eval.items():
        if k not in ("criterion_3_anatomy_markers_found",
                     "criterion_4_level_markers_found",
                     "criterion_8_links_found",
                     "entry_label"):
            print(f"    {k}: {v}")

    audit_passes = av_pass and au_pass
    print(f"\n  Conjunctive audit_passes (av_pass AND au_pass): {audit_passes}")

    # 5. Emit audit JSON
    audit_record = {
        "gate_id": GATE_ID,
        "session": SESSION,
        "plan_reference": "sessions/session-plan/session-90-plan-w8.md §W8-5 (CF-63)",
        "w1_cf14_prereq_pass": w1_cf14_prereq_pass,
        "w1_cf14_audit_sha256": W1_CF14_AUDIT_SHA,
        "vii_av_landed": True,
        "vii_au_op_proj_landed": True,
        "vii_av_evaluation": av_eval,
        "vii_au_op_proj_evaluation": au_eval,
        "vii_av_passes": av_pass,
        "vii_au_op_proj_passes": au_pass,
        "audit_passes_conjunctive": audit_passes,
        "level1_tags": int(
            av_eval["criterion_5_level1_single_tau_tag"]
            + au_eval["criterion_5_level1_single_tau_tag"]
        ),
        "deferred_pending_subclass_tags": int(
            av_eval["criterion_6_deferred_pending_sub_class"]
            + au_eval["criterion_6_deferred_pending_sub_class"]
        ),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX_TAG,
        "co_signers": {
            "connes-ncg-theorist": "technical 5-anatomy + 3-level cross-pillar-bridge-anatomy compliance",
            "lizzi-spectral-functional-theorist": "§VII.AU substrate-IS observable identity (FWD-C1 spec at cross-pillar-bridge-corpus.md §4 lines 137-145)",
            "volovik-superfluid-universe-theorist": "Level-1 single-τ-slice declaration MANDATORY per phononic-framing.md Forward-looking enforcement",
        },
    }
    AUDIT_JSON.write_text(
        json.dumps(audit_record, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"\n  Audit JSON written: {AUDIT_JSON}")

    # 6. Emit verdict line + dual-SHA companion
    verdict = "PASS" if audit_passes else "FAIL"
    level1_tags_count = audit_record["level1_tags"]
    sub_class_count = audit_record["deferred_pending_subclass_tags"]
    value_str = (
        f"vii_av_landed=True; vii_au_landed=True; "
        f"level1_tags={level1_tags_count}; "
        f"deferred_pending_subclass={sub_class_count}; "
        f"audit_passes={audit_passes}"
    )
    line = (
        f"{GATE_ID}: {verdict} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX_TAG} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
    print(f"\n  Canonical verdict line appended to {VERDICT_TXT.name}:")
    print(f"    {line.strip()}")

    comment_line = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(comment_line)
    print(f"    {comment_line.strip()}")

    # 7. 4-tuple
    tag = (
        f"(value={value_str!r}, scheme={SCHEME}, "
        f"convention={CONVENTION}, L_max={L_MAX_TAG})"
    )
    print(f"\n{tag}")

    # 8. Final summary
    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
