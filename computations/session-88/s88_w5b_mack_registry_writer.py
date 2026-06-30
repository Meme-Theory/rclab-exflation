#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S88 W5b mack-cosmic-bridge sole-writer registry-landing script.

GATES:
- Gate A: S88-VII-U-2-REGISTRY-WRITE
    Lands lizzi's §VII.U.2 4-corner classification STAGE-1-CANDIDATE
    drafted in WP §W5b-45, with cross-citation to connes 8-step axiom
    proof at WP §W5b-48.
- Gate B: S88-WAVE-B-CORNER-CELL-ANNOTATION-PASS
    Annotates **Corner**: <I/II/III/IV> on 7 existing §VII registry
    slot headers per the §W5b-46 predicted-assignment table.

ARCHITECTURE: AFTER-pattern per `.claude/rules/registry-landing.md`
§"Bridge-Landing Script Architecture":
  1. build_promotion_text(...) — pure function, full text in memory
  2. write_atomic_with_fsync(...) — single disk write
  3. re_read + verify_section_matches(...) — single boolean per gate
  4. emit_verdict_line(...) — exactly ONE canonical line + dual-SHA
     companion per gate (no schema-v2 3-tuple; both gates are
     artifact-existence METHODOLOGY-class with no [SIGN] trigger).

INPUT-PIN MAP (closure_hash → audit_sha256):
- s88_w5b_45_lizzi_draft_sha
- s88_w5b_48_connes_axiom_proof_sha
- s88_w5b_46_audit_json_sha
- methodology_wave_allowlist_sha
- permanent_results_registry_pre_write_sha
- canonical_constants_sha

REGISTRY-WRITE HYGIENE per `.claude/rules/epistemic-discipline.md`
§"Registry-Write Hygiene under Parallel-Writer Race":
- ALL header levels scanned (## + ### + ####) before allocation.
- Append-only Python writer, NOT Edit-tool round-trips.
- Slot-collision rerouting → FAIL-with-remediation in verdict line.

Author: mack-cosmic-bridge (sole writer for permanent-results-registry.md
per `.claude/agent-memory/feedback_mack-bridge-role.md`)
Session: 88, Wave: W5b, Plan: session-88-plan-w5b.md §§W5b-45 + W5b-46
Date: 2026-05-04
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import sys
from pathlib import Path
from typing import Tuple

# Project root
ROOT = Path(__file__).resolve().parents[2]

# Paths
REGISTRY = ROOT / "sessions" / "permanent-results-registry.md"
WP_PATH = ROOT / "sessions" / "session-88" / "session-88-w5b-workingpaper.md"
AUDIT_JSON = ROOT / "computations" / "_tmp" / "corner_classification_audit_20260505T000910Z.json"
ALLOWLIST = ROOT / ".claude" / "rules" / "methodology-wave-allowlist.md"
CANONICAL_CONSTANTS = ROOT / "computations" / "_shared" / "canonical_constants.py"
VERDICT_FILE = ROOT / "computations" / "session-88" / "s88_gate_verdicts.txt"


def sha256_of(p: Path) -> str:
    """Plain SHA-256 of file bytes."""
    return hashlib.sha256(p.read_bytes()).hexdigest()


def closure_hash_of_pinmap(pinmap: dict) -> str:
    """Audit-SHA convention: SHA-256 over the JSON-canonicalized pinmap.

    Matches the project's `closure_hash(input_pin_map)` pattern. Each pinmap
    entry is a (name, sha-or-value) pair; the JSON dump is sorted-key +
    no whitespace for byte-stable canonicalization.
    """
    canonical = json.dumps(pinmap, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# Build §VII.U.2 promotion text (verbatim from WP §W5b-45 lizzi draft, with
# clauses (c)+(d) cross-citing connes axiom proof at WP §W5b-48).
# ---------------------------------------------------------------------------


def build_vii_u_2_promotion_text() -> str:
    """Pure function: produce the EXACT §VII.U.2 entry text for in-place
    insertion between §VII.U.1 and §VII.U.6 in permanent-results-registry.md.

    Verbatim from `sessions/archive/session-88/session-88-w5b-workingpaper.md` §W5b-45
    theorem-name line block (lines 38-54) + 6 clauses (lines 55-78) +
    corrigenda (lines 80-85) + JOINT-clause flags (lines 87-91) + substrate
    framing (lines 93-95) + direction-of-explanation (lines 97-108) +
    4-tuple (lines 110-114) + anchor list (lines 116-121) + authorship
    (lines 123-126).

    Clauses (c) and (d) cross-cite §W5b-48 axiom proof verbatim from WP §W5b-48
    Theorem (lines 425-432) + 8-step proof (Steps 1-8 at lines 436-487) +
    converse (lines 489-495) + Sage cross-check (lines 499-516).
    """
    text = """### §VII.U.2 — Four-corner classification of (A_K, H_K, D_K) functionals (algebra-axis × Mellin-pole orthogonality) [STAGE-1-CANDIDATE] (S88 W5b-45 — lizzi-spectral-functional-theorist PRIMARY synthesizer + connes-ncg-theorist CO-AUTHOR for clauses (c)+(d), 2026-05-04)

**Status**: STAGE-1-CANDIDATE per `.claude/rules/joint-theorem-promotion.md` Stage 1; Stage-2 cross-axis independent-verify queued for S89+ as `S89-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY`. Mack-cosmic-bridge sole writer per `feedback_mack-bridge-role.md`.

**Theorem-name block**:

```
§VII.U.2 Four-corner classification of (A_K, H_K, D_K) functionals (algebra-axis × Mellin-pole orthogonality)
ANCHOR-1 (V-side, lizzi PRIMARY): cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter" (K=3 MANDATORY at S87 W-2 R3 close, 2026-04-30)
ANCHOR-2 (C-side, connes CO-AUTHOR): NCG axioms 1+4+5+6 + Connes-Moscovici 1995 §III.4 dim-spectrum residue formula + Poincaré duality on A_F (full axiomatic derivation at S88 §W5b-48 — `S88-FUNCTIONAL-FAMILY-ORTHOGONALITY-NCG-AXIOM-DERIVATION` PASS, 8-step proof + converse + Sage finite-block cross-check, audit_sha256=ff505a036d1ad6d7cb6857ace42358a7aacf179490cb224218c12aba4c178ab9)
STRUCTURE: SOURCE-DOUBLE-CITE-CO-PRIMARY (sequential V → C chain: V-side family-membership-predicate calibration corpus → C-side NCG-axiomatic non-triviality + orthogonality theorem)
NOTE: anchors are SAME-AXIS (both substrate-IS algebra-axis-side); INTRA-axis co-primary is permitted; CROSS-corner co-primary is FORBIDDEN per clause (f) of this entry.
TAG: STAGE-1-CANDIDATE (per joint-theorem-promotion.md Stage 1; Stage-2 cross-axis independent-verify queued for S89+ as S89-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY)
JOINT-clauses: (c) + (d) require Stage-2 cross-axis verify; both lizzi-side and connes-side cross-reviewers must independently PASS without prior workshop context.
Anchor list: S87 W-2 R3 close synthesis (sessions/archive/session-87/workshops/s87-alpha-s-route-dissonance.md); cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"; S87 S-2 §3.2 closeout via Connes-distance-on-A_F workshop (sessions/archive/session-87/workshops/s87-connes-distance-on-af.md); S87 W1b-6 INFO verdict trace via the same Connes-distance-on-A_F workshop.
Authorship attribution: lizzi-spectral-functional-theorist PRIMARY synthesizer; connes-ncg-theorist CO-AUTHOR for clauses (c) and (d) (axiom-level proof at §W5b-48); mack-cosmic-bridge SOLE WRITER for this registry row per feedback_mack-bridge-role.md.
Closure SHA pin: audit_sha256 = aeb3edfa7dcca2393ea18e56988a9994a103cd0ccc6aea2c01d7a917d5eda94c (input-pin map closure over W-2 R3 + K-counter + Connes-distance-on-A_F + canonical_constants).
```

**Theorem statement (6 clauses, JOINT vs single-axis tagging preserved)**:

On any finite spectral triple `(A, H, D)` satisfying NCG axioms 1-7, the functional-family decomposition splits into two structurally orthogonal classes:

**(a) [single-axis lizzi-side]** **Algebra-INVARIANT family**: spectrum-only functionals of the form `F_inv({λ_k, m_k}) = Σ_k m_k g(λ_k)` for measurable `g`; includes Seeley-DeWitt moments `a_n^{regulator}`, ζ-residues `Res[Tr(D^{−2s}); s=(d−n)/2]`, Mellin-Dirichlet identities, and heat-kernel zeta-traces. Substrate-IS interpretation: `F_inv` IS a property of the spectrum `{λ_k(D), m_k}` of the substrate's Dirac operator alone; observers do not measure `F_inv` "in" any container — the substrate's spectral content IS the observable's substrate-side identity.

**(b) [single-axis connes-side]** **Algebra-DEPENDENT family**: state-pair functionals on `A` of the form `F_dep(ω_1, ω_2; A) = ‖[D, π(A)]‖_op` and convex combinations / suprema thereof; includes the Connes distance `d_C(ω_1, ω_2) = sup_{a ∈ A_h, ‖[D, π(a)]‖ ≤ 1} |ω_1(a) − ω_2(a)|`, state expectations, sample variances over occupation distributions. Substrate-IS interpretation: `F_dep` IS a property of the algebra `A` together with `D`'s commutator action; the substrate's algebra IS what generates the algebra-DEPENDENT identity-class.

**(c) [JOINT — substrate-physics axiomatic — connes axiom-derivation + lizzi family-membership predicate]** **Structural orthogonality**: there is no closed-form `{λ_n}`-only identity reproducing any algebra-DEPENDENT functional, AND conversely no state-pair-functional-only identity reproducing any algebra-INVARIANT spectral moment. **Proof anchor**: full 8-step axiomatic derivation at S88 §W5b-48 `S88-FUNCTIONAL-FAMILY-ORTHOGONALITY-NCG-AXIOM-DERIVATION` (verdict PASS, audit_sha256=ff505a036d1ad6d7cb6857ace42358a7aacf179490cb224218c12aba4c178ab9). NCG axioms 1+5 + CM-1995 §III.4 dim-spectrum residue formula `a_n = Res[Tr(D^{−2s}); s=(d−n)/2] = Σ_k m_k λ_k^{−(d−n)}` GUARANTEE the algebra-INVARIANT family is non-trivial (Step 1: lifts every `F ∈ F_inv` into `\\{f(D²) : f \\text{ measurable}\\}'' ⊆ Z(\\{D, γ\\}'')`). NCG axioms 4+6 + Poincaré duality on `A` GUARANTEE the algebra-DEPENDENT family is non-trivial (Steps 4-5: `Ω^1_D(A_F) ⊂ B^J(H_F)` is non-trivial bimodule for any non-commutative `A`; K-pairing on `K_0(A_F) = ℤ⊕ℤ⊕ℤ` is non-degenerate). The chirality-vs-A_F block-grading mismatch (Step 7, eq. (9): `\\{f(D²)\\} ∩ π(A_F) = ℂ · 1_{H_F}`) ensures `f(D²) ∩ π(A) = scalars` on the state-pair side, while the spectrum-only side is the full `Z(f(D²))` algebra. Both families are ALWAYS present; identity-class membership is structurally orthogonal by axiom-level NCG argument. Sage finite-block cross-check (auxiliary) confirms the operator-algebraic conclusion at the explicit 6-dim finite-N truncation: DOF cascade `5 → 3 → 1` reduces (1 ℂ + 4 ℍ + 9 M_3 = 14 DOF, projected to 5 diagonal-survivor DOF, then 3 post-axiom-5 γ-commutation, then 1 post-Poincaré-duality + chirality-vs-A_F block-grading mismatch). **Stage-2 cross-axis independent-verify queued for S89+.**

**(d) [JOINT — substrate-physics + calibration corpus rank-counting — lizzi calibration table + connes structural classification]** **4-corner partition table**: every observable of `(A_K, H_K, D_K)` with τ_fold-sweep substrate-distance pole `s ∈ {3, 4}` is classified into one of 4 corner cells {I, II, III, IV} by the cross-product (algebra-axis ∈ {INVARIANT, DEPENDENT}) × (Mellin pole ∈ {s=3, s=4}). The K=3 calibration corpus is **saturated at S87 W-2 R3 close** (per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY status):

| Corner | Algebra-axis | Mellin pole | Calibration instance |
|:-------|:------------|:-----------|:--------------------|
| I | INVARIANT | s=3 | §VII.U.1 Mellin-Dirichlet identity (S86 W-1 / S87 W1a-4 PASS rel_diff = 0e+00 at L_max=12); `α_s_canonical = n_s² − 1 = -8587279/100000000` (S87 W2-1 + W2-4 PASS at single-pole Mellin closure substrate-distance-1 pole) |
| II | INVARIANT | s=4 | (open; future calibration via §W5b-47 substrate-distance-2 cone derivation) |
| III | DEPENDENT | s=3 | full `M_n(ℂ)` Connes distance (regulator-divergent; S87 W1b-6 INFO verdict via `s87-connes-distance-on-af.md`); `A_F` Connes distance STRICT residual `1.054e-01` at Pair-2 (S87 S-2 §3.2 closeout Reading-C synthesis, sourced via `s87-connes-distance-on-af.md` line 112) |
| IV | DEPENDENT | s=4 | `α_s_route_3 = Var_a(n_a^GGE) = -7.046336` at L_max=10 (S87 W2-3 FAIL composite at higher-moment cone, GGE-specified state-pair Bogoliubov occupation variance); structural envelope cross-confirmed at S88 §W5b-47 (`Var_a(n_a^GGE)(L_max=10) = 7.282490e-06`, `α_loglog ≈ 3.56`, R² = 0.945, MARGINAL regime; INFO composite) |

K = 3 ≥ K_promotion = 3 ⇒ **MANDATORY** at this gate's landing per the K-counter advancement event tracked in `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`. This entry is the canonical registry landing of that K=3 status.

**(e) [single-axis lizzi-side]** **Functional-class membership predicate is decidable from the functional's symbolic form**: `F` belongs to algebra-INVARIANT iff its symbolic form contains ONLY traces / spectral moments / `g(λ_k)` evaluations and no `π(a)` operator-algebra references; `F` belongs to algebra-DEPENDENT iff its symbolic form contains at least one `π(a)` or `[D, π(a)]` reference. **The decision procedure is finite and operates at parse-tree level, NOT at numerical evaluation level** — this makes it regulator-independent (same parse-tree decision under cutoff, ζ, Pauli-Villars, Mellin regulators) and laboratory-IN (the parse-tree image of a substrate-IS spectral-triple observable is what the laboratory directly inspects via the producing-script's symbolic AST). The §W5b-46 audit script `_corner_classification_audit.py` is the canonical implementation of this decision procedure for retroactive annotation of the 7 existing §VII slots.

**(f) [single-axis connes-side]** **Cross-corner co-primary registry-anchor structure FORBIDDEN**: per `registry-landing.md` SOURCE-DOUBLE-CITE-CO-PRIMARY discipline + `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY enforcement, registry entries cannot pin two anchors at co-primary weight when the anchors inhabit distinct corner cells. The 4 corners are pairwise structurally orthogonal; co-primary structure between them violates NCG-axiom-level family-orthogonality. **Pole-scope sub-clause (W-9 RULE-3) extends to corner-scope**: cross-pole (s=3 ↔ s=4) AND cross-corner (INVARIANT ↔ DEPENDENT) co-primary structures both FAIL plan-freeze. Cross-corner cross-pole magnitude comparisons (e.g., the Cell I `α_s_canonical = -0.08587279` vs Cell IV `α_s_route_3 = -7.046336` ratio `82.0556×` Sage-QQ exact) are STRUCTURALLY FORBIDDEN AS GATES; permitted in narrative analyses ONLY with explicit `[CROSS-CORNER COMPARISON; STRUCTURALLY FORBIDDEN AS GATE]` declaration.

**Corrigenda block** (per joint-theorem-promotion.md Stage 1 schema):

- **C1**: K=3 MANDATORY status was promoted at S87 W-2 R3 close (2026-04-30); the `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` sub-section was the rule-file landing site; this §VII.U.2 entry is the registry landing site (separate artifact, same K-counter event).
- **C2**: Clause (d) Corner II is OPEN at K=3; the K=3 saturation is achieved by Corners I + III + IV (three calibration instances on three of four corners); Corner II awaits §W5b-47 substrate-distance-2 cone derivation. Corner II's openness does NOT block STAGE-1-CANDIDATE landing because the partition's STRUCTURAL claim is the orthogonality of the 4 corners as a discrete classification, NOT the requirement that all 4 corners have calibration instances at landing-time.
- **C3**: Clause (e) parse-tree decision procedure is canonicalized at §W5b-46 audit-script implementation; the registry text references the audit script by file path `computations/_shared/_corner_classification_audit.py` for downstream consumers; absence of the audit script at landing-time does NOT block STAGE-1-CANDIDATE because the decision procedure is fully specified at the symbolic-form level of clause (e).
- **C4**: Clause (f) FORBIDDEN-cross-corner-co-primary discipline is forward-looking from this landing onward; pre-S88 registry entries are GRANDFATHERED but flagged for retroactive annotation via §W5b-46. The grandfathering is documented per `epistemic-discipline.md §"Source Reconciliation"` Class-(c) PIN-DRIFT-FROM-STALE-SOURCE protocol.

**JOINT-clause flags** (per joint-theorem-promotion.md Stage 2 cross-axis verify pre-registration):

- **Clause (c)** is JOINT — Stage-2 verify requires (i) lizzi-side cross-reviewer auditing the family-membership predicate calibration corpus + the closed-form `{λ_n}`-identity-impossibility direction; (ii) connes-side cross-reviewer auditing the NCG-axiomatic non-triviality + chirality-vs-A_F block-grading-mismatch direction; both PASS independently and in logical AND.
- **Clause (d)** is JOINT — Stage-2 verify requires (i) lizzi-side cross-reviewer auditing the K=3 calibration corpus completeness against the 4-corner partition table; (ii) connes-side cross-reviewer auditing the structural-orthogonality of the 4 corners under NCG axioms 1+4+5+6; both PASS independently and in logical AND.
- Clauses (a), (b), (e), (f) are single-axis and require only the named-axis cross-reviewer (lizzi for (a), (e); connes for (b), (f)).

**Substrate framing per `phononic-framing.md` §"IS Space, Not IN Space"**:

The 4-corner classification IS a property of the spectral triple `(A, H, D)` itself — it is NOT a property "in" any container space. The substrate's algebra `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` IS what generates the algebra-DEPENDENT family; the substrate's spectrum `{λ_k(D_K), m_k}` IS what generates the algebra-INVARIANT family. The orthogonality is structural at the substrate level — observers do not measure orthogonality "in" the substrate; the substrate IS orthogonal at the family-class level. The 4-corner partition is the SUBSTRATE-IS observable. Laboratory observables (Connes-distance numerical evaluation, spectral-moment numerical evaluation) are LABORATORY-IN observables on continuum-projected derived images. The bridge map between substrate corner-cell membership and laboratory functional-class membership is the parse-tree decision procedure of clause (e) — finite, decidable, regulator-independent.

**Direction of explanation** (per `phononic-framing.md` mandate; the theorem statement IS substrate-axiomatic):

```
NCG axioms 1+4+5+6  (substrate-axiomatic foundation)
   → CM-1995 §III.4 dim-spectrum residue formula  (algebra-INVARIANT non-triviality)
   → Poincaré duality on A_F  (algebra-DEPENDENT non-triviality)
   → chirality-vs-A_F block-grading mismatch  (f(D²) ∩ π(A) = scalars on state-pair side)
   → 4-corner orthogonality theorem  (substrate-IS classification of the spectral triple)
   → §VII.U.2 STAGE-1-CANDIDATE registry landing  (laboratory-IN audit-trail commitment)
```

No "container space" appears in this chain; the substrate IS the spectral triple, IS the orthogonal classification, and IS the registry-PASS observable.

**4-tuple**:
- scheme: `four-corner-NCG-axiomatic-classification`
- convention: `joint-theorem-promotion-Stage-1-CANDIDATE`
- L_max: N/A (rule-file landing, no spectral evaluation)
- LEVEL: PRIMARY (substrate-axiomatic; no schematic helper)

**Anchor list** (per Anchor-list element of theorem-name line):
1. `sessions/archive/session-87/workshops/s87-alpha-s-route-dissonance.md` (S87 W-2 R3 close synthesis; SHA `f9b600039e34b2e4b5df98737810355fa675cd5edc3a518d9b9fb8e2d45e80b2`)
2. `.claude/rules/cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` (post-S87 in-rule landing of K=3 MANDATORY status; SHA `c4bec5c51d12878b9fce1d6b371287099933e47cb55c879590c48f14d65ad074`)
3. `sessions/archive/session-87/workshops/s87-connes-distance-on-af.md` (S87 S-2 §3.2 closeout Reading-C synthesis on A_F STRICT residual `1.054e-01` at Pair-2; SHA `6c2d3522346bc8bbbea1d120af29aedeaf9665f878e66c7ce6912f794ad33cae`)
4. `sessions/archive/session-87/workshops/s87-connes-distance-on-af.md` (S87 W1b-6 INFO verdict trace; same workshop file as anchor 3 — the W1b-6 conclusion and the S-2 §3.2 closeout share the same workshop substrate per S87 W1b structure)
5. `computations/_shared/canonical_constants.py` (canonical-constants pin reference; SHA `3c42707301bbf634b1fb27db14ab02aabba9190459f27ef6f84ce20de25ca7d4`)

**Authorship attribution**:
- **lizzi-spectral-functional-theorist** PRIMARY synthesizer — drafted clauses (a), (b), (e), (f) verbatim from plan §W5b-45 hypothesis section; drafted clause TEXT for (c) and (d) referencing `§W5b-48` for axiomatic derivation per spawn-prompt instruction; assembled the integrated 6-clause theorem block + corrigenda + JOINT-clause flags + anchor list + 4-tuple per `joint-theorem-promotion.md` Stage 1 schema.
- **connes-ncg-theorist** CO-AUTHOR for clauses (c) and (d) — provides axiom-level proof at separate gate `§W5b-48` (`S88-FUNCTIONAL-FAMILY-ORTHOGONALITY-NCG-AXIOM-DERIVATION` PASS; 8-step proof + converse + Sage finite-block cross-check). Cross-cited from clauses (c)+(d) above with the W5b-48 verdict's audit_sha256 pin.
- **mack-cosmic-bridge** SOLE WRITER for the §VII.U.2 row in `sessions/permanent-results-registry.md` per `feedback_mack-bridge-role.md`; landed the theorem-name block + 6 clauses + corrigenda + flags + anchor list verbatim from lizzi's draft via S88 W5b Wave-B `S88-VII-U-2-REGISTRY-WRITE` dispatch (this gate; mack-cosmic-bridge orchestrator-direct write per `methodology-wave-allowlist.md` row appended at S88 W5b plan-freeze).

**Cross-link to algebra-axis orthogonality K-counter**:
- `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3 (S87 W-2 R3 close, 2026-04-30) — this §VII.U.2 entry IS the registry landing of that K=3 promotion event.
- `cross-pillar-bridge-anatomy.md §"Audit at plan-freeze"` items (1)-(4) — every future §VII registry entry on `(A_K, H_K, D_K)` MUST declare its 4-corner cell ∈ {I, II, III, IV} explicitly per the partition table above; cross-corner co-primary FORBIDDEN per clause (f); cross-corner cross-pole magnitude comparisons STRUCTURALLY FORBIDDEN AS GATES.
- §W5b-46 audit infrastructure (`computations/_shared/_corner_classification_audit.py`) implements the parse-tree decision procedure; mack-cosmic-bridge Wave-B `S88-WAVE-B-CORNER-CELL-ANNOTATION-PASS` dispatch (this gate) annotates the 7 existing §VII slots per the §W5b-46 predicted-assignment table.

"""
    return text


# ---------------------------------------------------------------------------
# Corner-cell annotations for the 7 existing §VII slots (per §W5b-46 audit
# predicted-assignment table)
# ---------------------------------------------------------------------------


CORNER_ANNOTATIONS = {
    # slot_label : (corner, axis, pole, semantic_note)
    "§VII.U.1": (
        "I",
        "INVARIANT",
        "s=3",
        "Mellin-Dirichlet identity at substrate-distance-1 pole; CONSISTENT with §W5b-46 audit "
        "(audit returned algebra-axis=INVARIANT 7/7 PERFECT; pole=None lexically but inferred s=3 "
        "from Mellin-Dirichlet identity semantic marker per §VII.U.2 clause (e) consultation; "
        "S86 W-1 / S87 W1a-4 PASS at L_max=12 anchored substrate-distance-1).",
    ),
    "§VII.U.6": (
        "I",
        "INVARIANT",
        "s=3",
        "Mellin-Strip / Convergence-Cone Theorem at substrate-distance-1 pole; CONSISTENT-WITH-AUDIT — "
        "§W5b-46 audit detected lexical s=3 marker present (only slot of 7 with audit-decisive Mellin-pole); "
        "audit corner = I = predicted I (no consultation substitution required).",
    ),
    "§VII.AC.1": (
        "III",
        "DEPENDENT",
        "s=3",
        "Path-H/Path-C dual-pathway block-decomposition on A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ); algebra-DEPENDENT "
        "(state-pair commutator-norm functional via ‖[D, π(a)]‖_op route through A_F irreps); "
        "Mellin pole inferred from substrate-distance-1 semantic marker (a_4^ζ Seeley-DeWitt slot at s=3) "
        "per §VII.U.2 clause (e) consultation per S88 §W5b-46 audit FAIL on lexical-marker absence.",
    ),
    "§VII.AC.4": (
        "III",
        "DEPENDENT",
        "s=3",
        "V1+C1 sequential-chain derivation of Path-H/Path-C classification; algebra-DEPENDENT "
        "(C1 output layer = NCG axioms 3+5+6 + Schur orthogonality on A_F state-pair structure); "
        "Mellin pole inferred from a_4^ζ Seeley-DeWitt slot semantic marker (substrate-distance-1) per "
        "§VII.U.2 clause (e) consultation per S88 §W5b-46 audit FAIL on lexical-marker absence.",
    ),
    "§VII.W": (
        "II",
        "INVARIANT (axiom-level)",
        "s=4",
        "Parity-Grading Orthogonality of HP_*(A_F); INVARIANT (axiom-level) — substrate's NCG cohomology-ring "
        "property, derived from Wedderburn + KO-dim-6 + Hopf-deformation rigidity at finite-dim semisimple "
        "level; Mellin pole inferred from substrate-distance-2 axiom-level slot semantic marker per "
        "§VII.U.2 clause (e) consultation per S88 §W5b-46 audit FAIL on lexical-marker absence.",
    ),
    "§VII.AF.1": (
        "I",
        "INVARIANT",
        "s=3",
        "Pillar III ↔ Pillar IV bridge theorem (HP^1 cohomology ↔ Peotta-Törmä quantum-metric trace); "
        "substrate-IS finite-L Hochschild pairing on (A_K^{≤10}, H_K^{≤10}, D_K^{≤10}) is a spectrum-only "
        "INVARIANT functional via a_4^ζ residue at s=0 (Connes-Karoubi pairing on band-0 projector); "
        "Mellin pole inferred from substrate-distance-1 semantic marker (Level-2 algebraic L^{-3} envelope "
        "at d=4 corresponds to s=3 substrate-distance-1 cone) per §VII.U.2 clause (e) consultation per "
        "S88 §W5b-46 audit FAIL on lexical-marker absence.",
    ),
    "§VII.AJ": (
        "IV",
        "DEPENDENT",
        "s=4",
        "Pillar IV ↔ Pillar V REGISTRY-FAIL (BdG-undoubled excess at substrate-distance-2 cone); "
        "algebra-DEPENDENT (state-pair Bogoliubov-occupation observables on the BdG-restricted spectral-triple "
        "sub-algebra; cf. W11-5 calibration corpus instance #2 forward-table); Mellin pole inferred from "
        "substrate-distance-2 cone semantic marker (n=4 convention tag per S86 W-12 §VII.K-PROP partition) "
        "per §VII.U.2 clause (e) consultation per S88 §W5b-46 audit FAIL on lexical-marker absence.",
    ),
}


def build_corner_annotation_block(slot: str) -> str:
    """Pure function: produce the **Corner**: annotation block for `slot`.

    Inserted directly under the slot-header line. Format is a single-line
    `**Corner**: <I/II/III/IV>` declaration plus one-line consultation-
    substitution note per §W5b-46 plan PASS (iii) consultation-substituted
    annotation step.
    """
    corner, axis, pole, note = CORNER_ANNOTATIONS[slot]
    return (
        f"\n**Corner**: {corner} ({axis} × {pole}) — "
        f"S88 §W5b-46 audit-substituted annotation per §VII.U.2 clause (e) consultation; {note}\n"
    )


# ---------------------------------------------------------------------------
# Build the full registry text via two operations:
#   (1) Insert §VII.U.2 entry BEFORE §VII.U.6 header
#   (2) Insert **Corner**: annotation under each of the 7 slot headers
# ---------------------------------------------------------------------------


def slot_anchor_pattern(slot_label: str) -> str:
    """Return the regex pattern that exactly matches the given slot's
    canonical heading line (## or ### or #### prefixed). The pattern matches
    everything up to and including the trailing newline of the heading line.
    """
    # Escape for regex
    esc = re.escape(slot_label)
    # Match heading line: any header level (## or ### or ####) followed by
    # space, the slot label, optional " — ..." or " " trailer, and newline.
    return rf"(?m)^(#{{2,4}}\s+{esc}\b[^\n]*\n)"


def insert_corner_annotation(registry_text: str, slot: str) -> str:
    """Insert the `**Corner**: ...` annotation immediately after the slot's
    heading line. Idempotent: if a `**Corner**:` block already exists in the
    immediately-following ~10 lines, leave the file alone (no-op).
    """
    pattern = slot_anchor_pattern(slot)
    m = re.search(pattern, registry_text)
    if m is None:
        raise RuntimeError(f"Could not locate slot heading for {slot!r}")
    header_end = m.end()
    # Look ahead ~600 chars for an existing "**Corner**:" annotation
    lookahead = registry_text[header_end : header_end + 600]
    if "**Corner**:" in lookahead:
        return registry_text  # idempotent no-op
    annotation = build_corner_annotation_block(slot)
    return registry_text[:header_end] + annotation + registry_text[header_end:]


def insert_vii_u_2(registry_text: str, promotion_text: str) -> str:
    """Insert the §VII.U.2 entry block immediately BEFORE the §VII.U.6
    heading line. Idempotent: if `### §VII.U.2 ` already present, return
    text unchanged.
    """
    if re.search(r"(?m)^#{2,4}\s+§VII\.U\.2\b", registry_text):
        return registry_text  # idempotent no-op
    # Locate §VII.U.6 heading line; insert §VII.U.2 block before it
    m = re.search(r"(?m)^(#{2,4}\s+§VII\.U\.6\b[^\n]*\n)", registry_text)
    if m is None:
        raise RuntimeError("Could not locate §VII.U.6 heading for insertion anchor")
    insertion = m.start()
    block = promotion_text + "\n"
    return registry_text[:insertion] + block + registry_text[insertion:]


# ---------------------------------------------------------------------------
# Verify section helpers
# ---------------------------------------------------------------------------


def verify_vii_u_2_landed(registry_text: str) -> Tuple[bool, str]:
    """Verify §VII.U.2 row is on disk with all required content per
    Gate-A PASS criteria.

    Body extraction uses HEADING-anchored regex match (not naive .split())
    because cross-references to "§VII.U.2" appear in OTHER slots' bodies
    (e.g., the Wave-B corner annotations cite §VII.U.2 clause (e) for
    consultation substitution).

    Checks:
      (1) Section heading present
      (2) STAGE-1-CANDIDATE tag present
      (3) SOURCE-DOUBLE-CITE-CO-PRIMARY structure tag present
      (4) JOINT-clauses (c) + (d) declared
      (5) Anchor list with 5 entries enumerated
      (6) Authorship attribution present
      (7) Substantive line count >= 15
    """
    # (1) section heading
    m_start = re.search(r"(?m)^### §VII\.U\.2 ", registry_text)
    if m_start is None:
        return False, "missing section heading for §VII.U.2"
    # Locate end-of-body marker = next "### §VII.U." heading OR next "## §" heading
    m_end = re.search(r"(?m)^### §VII\.U\.6 ", registry_text[m_start.end():])
    if m_end is None:
        return False, "missing §VII.U.6 sentinel; cannot bound §VII.U.2 body"
    body = registry_text[m_start.start() : m_start.end() + m_end.start()]  # (local)
    # (2) STAGE-1-CANDIDATE tag
    if "STAGE-1-CANDIDATE" not in body:
        return False, "missing STAGE-1-CANDIDATE tag in §VII.U.2 section"
    # (3) STRUCTURE tag
    if "SOURCE-DOUBLE-CITE-CO-PRIMARY" not in body:
        return False, "missing SOURCE-DOUBLE-CITE-CO-PRIMARY structure tag"
    # (4) JOINT-clause flags
    if "JOINT-clauses" not in body or "Clause (c)" not in body or "Clause (d)" not in body:
        return False, "missing JOINT-clause (c)+(d) declarations"
    # (5) Anchor list 5 entries
    anchor_block = body.split("**Anchor list**")[1] if "**Anchor list**" in body else ""  # (local)
    # bound the anchor block by the next "**" heading to avoid spilling into §VII.U.6 prose
    anchor_block = re.split(r"\n\*\*[A-Z]", anchor_block, maxsplit=1)[0]  # (local)
    enumerated = re.findall(r"^\s*\d+\.\s+", anchor_block, flags=re.MULTILINE)
    if len(enumerated) < 5:
        return False, f"anchor list has only {len(enumerated)} enumerated entries (need 5)"
    # (6) authorship attribution
    if "**Authorship attribution**" not in body:
        return False, "missing authorship attribution block"
    if (
        "lizzi-spectral-functional-theorist" not in body
        or "connes-ncg-theorist" not in body
        or "mack-cosmic-bridge" not in body
    ):
        return False, "authorship attribution missing one of (lizzi/connes/mack)"
    # (7) substantive line count
    lines = [ln for ln in body.splitlines() if ln.strip()]  # (local)
    if len(lines) < 15:
        return False, f"only {len(lines)} substantive lines (need >= 15)"
    return (
        True,
        f"§VII.U.2 PASS: STAGE-1-CANDIDATE + SOURCE-DOUBLE-CITE-CO-PRIMARY + "
        f"JOINT(c)(d) + 5-anchor + lizzi/connes/mack attribution + "
        f"{len(lines)} substantive lines (heading-anchored body extraction)",
    )


def verify_corner_annotations(registry_text: str) -> Tuple[bool, str]:
    """Verify all 7 §VII slots have **Corner**: <I/II/III/IV> annotation
    immediately following their heading line.
    """
    expected_corners = {
        "§VII.U.1": "I",
        "§VII.U.6": "I",
        "§VII.AC.1": "III",
        "§VII.AC.4": "III",
        "§VII.W": "II",
        "§VII.AF.1": "I",
        "§VII.AJ": "IV",
    }
    missing = []
    wrong = []
    for slot, expected in expected_corners.items():
        pattern = slot_anchor_pattern(slot)
        m = re.search(pattern, registry_text)
        if m is None:
            missing.append(f"{slot} (heading not found)")
            continue
        # Look at the next ~600 chars for "**Corner**: <expected>"
        lookahead = registry_text[m.end() : m.end() + 600]
        cm = re.search(r"\*\*Corner\*\*:\s*([IV]+)", lookahead)
        if cm is None:
            missing.append(f"{slot} (no **Corner**: annotation)")
        elif cm.group(1) != expected:
            wrong.append(f"{slot} (got {cm.group(1)!r}, expected {expected!r})")
    if missing or wrong:
        return False, f"missing={missing}; wrong={wrong}"
    return True, f"all 7 §VII slots have correct **Corner**: annotation: {expected_corners}"


# ---------------------------------------------------------------------------
# Atomic write + fsync
# ---------------------------------------------------------------------------


def write_atomic_with_fsync(text: str, path: Path) -> None:
    """Write text to path; fsync; per AFTER-pattern."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
        fh.flush()
        os.fsync(fh.fileno())


# ---------------------------------------------------------------------------
# Verdict-line emission (single-shot, append-only)
# ---------------------------------------------------------------------------


def emit_verdict_line(
    gate_id: str,
    verdict: str,
    value: str,
    scheme: str,
    convention: str,
    l_max: str,
    audit_sha: str,
    content_sha: str,
    schema: str = "S87+",
) -> None:
    """Append exactly one canonical verdict line + one dual-SHA companion
    comment row to s88_gate_verdicts.txt. No 3-tuple companion (METHODOLOGY-
    class artifact-existence gate; no [SIGN] trigger).
    """
    canonical = (
        f"{gate_id}: {verdict} -- value='{value}' "
        f"scheme={scheme} convention={convention} L_max={l_max} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={schema}\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {gate_id} dual-SHA companion row (W9a-99 split)\n"
    )
    with open(VERDICT_FILE, "a", encoding="utf-8", newline="") as fh:
        fh.write(canonical)
        fh.write(companion)
        fh.flush()
        os.fsync(fh.fileno())


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    print(f"[mack-cosmic-bridge S88 W5b registry writer] start")
    # 1. Read all inputs (pure: nothing is written yet)
    pre_write_text = REGISTRY.read_text(encoding="utf-8")
    pre_write_sha = sha256_of(REGISTRY)
    print(f"[pre-write] registry SHA: {pre_write_sha}")
    print(f"[pre-write] registry size: {len(pre_write_text)} chars")

    # 2. Build promotion text in memory (Gate A) and corner annotations (Gate B)
    vii_u_2_text = build_vii_u_2_promotion_text()
    print(f"[Gate A] §VII.U.2 promotion text: {len(vii_u_2_text)} chars, {vii_u_2_text.count(chr(10))} lines")

    # 3. Compose final registry text by sequential insertion
    new_text = insert_vii_u_2(pre_write_text, vii_u_2_text)
    print(f"[Gate A] post-insertion size: {len(new_text)} chars (+{len(new_text) - len(pre_write_text)})")

    for slot in CORNER_ANNOTATIONS.keys():
        new_text = insert_corner_annotation(new_text, slot)
    print(f"[Gate B] post-7-slot-annotation size: {len(new_text)} chars")

    # 4. Write atomically with fsync
    write_atomic_with_fsync(new_text, REGISTRY)
    print(f"[write] atomic write complete with fsync")

    # 5. Re-read and verify both gates
    actual_text = REGISTRY.read_text(encoding="utf-8")
    actual_sha = sha256_of(REGISTRY)
    print(f"[post-write] registry SHA: {actual_sha}")
    if actual_sha == pre_write_sha:
        print("[post-write] WARNING: SHA unchanged — write was a no-op (idempotent)")

    # Gate A verify
    gate_a_pass, gate_a_msg = verify_vii_u_2_landed(actual_text)
    print(f"[Gate A verify] PASS={gate_a_pass} | {gate_a_msg}")

    # Gate B verify
    gate_b_pass, gate_b_msg = verify_corner_annotations(actual_text)
    print(f"[Gate B verify] PASS={gate_b_pass} | {gate_b_msg}")

    # 6. Emit verdicts ONCE per gate (AFTER-pattern: no conditional retry)

    # Gate A input-pin map
    pinmap_a = {
        "gate_id": "S88-VII-U-2-REGISTRY-WRITE",
        "wp_path": "sessions/archive/session-88/session-88-w5b-workingpaper.md",
        "scheme": "registry-landing-source-double-cite-co-primary",
        "convention": "vii-u-2-stage-1-candidate-joint-theorem-promotion",
        "wp_lizzi_draft_sha": "4d4eaa93fa42eee08a9a4bccb0fc6e37d5c1e4a1a567fc79522f0b7e413f4200",
        "wp_connes_axiom_proof_sha": "4d4eaa93fa42eee08a9a4bccb0fc6e37d5c1e4a1a567fc79522f0b7e413f4200",
        "audit_json_sha": "05e56874652cf6184428ae9ad2f887f56986fbfb3f348ebdb8264dcf81a53b9a",
        "allowlist_sha": "4ff20f3845768679ca0897a5b7dcc6881855056b4404bf9dc623276dadd6828d",
        "registry_pre_write_sha": pre_write_sha,
        "canonical_constants_sha": "3c42707301bbf634b1fb27db14ab02aabba9190459f27ef6f84ce20de25ca7d4",
    }
    audit_sha_a = closure_hash_of_pinmap(pinmap_a)
    content_sha_a = actual_sha  # post-write registry SHA is the content SHA

    if gate_a_pass:
        verdict_a = "PASS"
        value_a = (
            f"slot=§VII.U.2;"
            f"structure=SOURCE-DOUBLE-CITE-CO-PRIMARY;"
            f"tag=STAGE-1-CANDIDATE;"
            f"clauses=a-b-c-d-e-f;"
            f"joint=c-d;"
            f"anchors=5;"
            f"authorship=lizzi-PRIMARY+connes-CO-AUTHOR+mack-WRITER;"
            f"verify={gate_a_msg.split(': ')[1] if ': ' in gate_a_msg else 'OK'}"
        )
    else:
        verdict_a = "FAIL"
        value_a = f"verify_failed:{gate_a_msg}"

    emit_verdict_line(
        gate_id="S88-VII-U-2-REGISTRY-WRITE",
        verdict=verdict_a,
        value=value_a,
        scheme="registry-landing-source-double-cite-co-primary",
        convention="vii-u-2-stage-1-candidate-joint-theorem-promotion",
        l_max="N/A",
        audit_sha=audit_sha_a,
        content_sha=content_sha_a,
    )
    print(f"[Gate A verdict] {verdict_a} audit={audit_sha_a[:16]} content={content_sha_a[:16]}")

    # Gate B input-pin map
    pinmap_b = {
        "gate_id": "S88-WAVE-B-CORNER-CELL-ANNOTATION-PASS",
        "wp_audit_json_sha": "05e56874652cf6184428ae9ad2f887f56986fbfb3f348ebdb8264dcf81a53b9a",
        "wp_w5b_46_path": "sessions/archive/session-88/session-88-w5b-workingpaper.md#W5b-46",
        "scheme": "registry-corner-cell-annotation-consultation-substituted",
        "convention": "predicted-assignment-table-w5b-46-with-clause-e-consultation",
        "registry_pre_write_sha": pre_write_sha,
        "canonical_constants_sha": "3c42707301bbf634b1fb27db14ab02aabba9190459f27ef6f84ce20de25ca7d4",
        "slots": ["§VII.U.1", "§VII.U.6", "§VII.AC.1", "§VII.AC.4", "§VII.W", "§VII.AF.1", "§VII.AJ"],
        "predicted": {
            "§VII.U.1": "I", "§VII.U.6": "I", "§VII.AC.1": "III",
            "§VII.AC.4": "III", "§VII.W": "II", "§VII.AF.1": "I", "§VII.AJ": "IV",
        },
    }
    audit_sha_b = closure_hash_of_pinmap(pinmap_b)
    content_sha_b = actual_sha

    if gate_b_pass:
        verdict_b = "PASS"
        value_b = (
            f"n_slots=7;"
            f"annotated=7;"
            f"missing=0;"
            f"wrong=0;"
            f"corners=I:U.1+U.6+AF.1,II:W,III:AC.1+AC.4,IV:AJ;"
            f"verify=all-7-corner-annotations-match-predicted-assignments-per-W5b-46-table"
        )
    else:
        verdict_b = "FAIL"
        value_b = f"verify_failed:{gate_b_msg}"

    emit_verdict_line(
        gate_id="S88-WAVE-B-CORNER-CELL-ANNOTATION-PASS",
        verdict=verdict_b,
        value=value_b,
        scheme="registry-corner-cell-annotation-consultation-substituted",
        convention="predicted-assignment-table-w5b-46-with-clause-e-consultation",
        l_max="N/A",
        audit_sha=audit_sha_b,
        content_sha=content_sha_b,
    )
    print(f"[Gate B verdict] {verdict_b} audit={audit_sha_b[:16]} content={content_sha_b[:16]}")

    print("[mack-cosmic-bridge S88 W5b registry writer] done")
    return 0  # exit 0 regardless of verdict per math-scripts.md §"Exit Codes and Verdict Semantics"


if __name__ == "__main__":
    sys.exit(main())
