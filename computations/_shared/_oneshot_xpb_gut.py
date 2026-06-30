#!/usr/bin/env python3
"""One-shot: reduce .claude/rules/cross-pillar-bridge-anatomy.md to directives-only
per the file's own header. Deletes dated `> Provenance:` blocks and condenses the
narrative-bloated paragraphs to rule + pointer. KEEPS every section header (cross-ref
targets), every criterion/taxonomy table/status line/audit+corpus pointer. Anchors are
ASCII; .*? swallows old unicode (no transcription). Asserts every cut; writes only if
all pass. Throwaway."""
import re
from pathlib import Path

P = Path(r"C:\sandbox\Ainulindale Exflation\.claude\rules\cross-pillar-bridge-anatomy.md")
text = P.read_text(encoding="utf-8")
orig_lines = text.count("\n")

# Sanity: headers we must NOT lose
must_keep_headers = [
    "## Three-Level Structural-Confidence Ladder",
    "### Tier-1/Tier-2 dimensional-re-anchorability gate",
    "## Single-observable-per-triple structural filter",
    "### Diffusion-window-observable specialization",
    "## IS-not-IN Anatomy (5 elements)",
    "#### Bridge-map-scheme suffix discipline",
    "### Element 2 OE-form discipline",
    "## Composite Bridge-Map Dimensional-Class Admissibility",
    "### Per-observable transport-degree scale-separation",
    "## S92 Workshop-Campaign Forward-Directive Mirrors",
    "## Calibration corpus + K-counter status (pointers)",
]
for h in must_keep_headers:
    assert text.count(h) >= 1, f"pre-check: header missing already: {h!r}"

# --- A. delete dated provenance / meta blocks (single `>` line + trailing blank) ---
text, n_prov = re.subn(r"(?m)^> \*\*Provenance\*\*:[^\n]*\n\n", "", text)
assert n_prov == 4, f"expected 4 **Provenance** blocks, removed {n_prov}"
text, n_verb = re.subn(r"(?m)^> Verbatim directive mirrors[^\n]*\n\n", "", text)
assert n_verb == 1, f"expected 1 'Verbatim directive mirrors' meta block, removed {n_verb}"

# --- B-G: condense narrative paragraphs (anchor = ASCII header/marker; .*? = old) ---
NEW = {}

NEW["tier"] = """### Tier-1/Tier-2 dimensional-re-anchorability gate (S93 W-1; SUGGESTION at K=1)

A Level-3 anchor is registry-PASS-ELIGIBLE only if EITHER **(Tier-1)** its residual-to-`c_continuum` shrinks with L_max (convergent → a substrate-singled-out evaluation point `L*` exists), OR **(Tier-2)** its divergent channel's truncation-invariant content is DIMENSIONLESS and the anchor is RE-ANCHORED to that invariant functional (a log-derivative / ratio / cohomology-class anchor — the §VII.AV.STATE-PROJ route). A divergent channel whose anchor is a DIMENSIONFUL magnitude (**Tier-2-dimensionful**) is registry-PASS-INELIGIBLE; its Level-3 row is HELD as `NOT-SATISFIED-PENDING-substrate-physical-scale-anchor`, while the joint theorem-STRUCTURE may independently hold STAGE-3-PERMANENT via Stage-2 PASS-AND on the non-Level-3 clauses. Dovetails with the Level-2-binding-vs-non-binding sub-class.

**Status**: SUGGESTION at K=1; promotes to MANDATORY at K=3. Audit: Tier-1/Tier-2 detector at `computations/_shared/_cross_pillar_bridge_audit.py` (S2 advisory at K=1). Structural basis, inaugural occupant (§VII.AX.OP-PROJ n_PBH), and calibration corpus: `cross-pillar-bridge-corpus.md §25`.

"""

NEW["diffusion"] = """### Diffusion-window-observable specialization (spectral-dimension comparisons; S92 AH-PF-1 + S93 W7-3; SUGGESTION at K=2)

For a substrate-IS spectral-dimension observable `d_s(σ) = −2 d ln P(σ)/d ln σ` compared against an external-framework dimensional-reduction reference (CDT / asymptotic-safety), the structural coordinate that MUST be fixed before any reduction verdict is the **(observable, diffusion-window) pair**: the σ→0 asymptotic `lim_{σ→0} d_s(σ)` (Weyl/MP manifold dimension) and the windowed value `d_s(σ_*)` are DISTINCT functionals of the SAME `P(σ)`. Fair comparison applies the SAME functional `Φ: P(σ) ↦ −2 d ln P/d ln σ` at the SAME scale-type; the bridge map IS `Φ`. The discriminating sub-quantity is the directly-fitted energy-axis DOS exponent `γ_E`; impedance/product constraints are CONSISTENCY CHECKS, not locks. A criterion calibrated on one functional (e.g. `Φ_graph-Laplacian`) is NOT transportable to a distinct one (`Φ_heat-trace`).

**Status**: SUGGESTION at K=2. Full directive + K=1/K=2 calibration corpus: `cross-pillar-bridge-corpus.md §24`.

"""

NEW["bridge_status"] = """**Status**: MANDATORY at K=3 (axis-β bridge-map-scheme suffix track). Calibration corpus + cross-link to the MACHINERY-SCOPE axis (`regulator-pin-discipline.md`): `cross-pillar-bridge-corpus.md §10`.

"""

NEW["composite_tail"] = """**Sub-question verdicts** (theorem-vs-heuristic CONFIRMED as a joint two-axis theorem; pole-extension and regulator/MACHINERY-SCOPE invariance closed): `cross-pillar-bridge-corpus.md §18`.

**Forward-design rule**: any FWD-C1/C2/C3 composite candidate MUST declare deg(Element-1-composite) and deg(Element-5-anchor) at plan-freeze and verify they match AND that the matching morphism is non-scalar — a scalar corrector is a Class-8 PRU defect detectable before compute. Downstream consumers (CF-S93-W2-1 Element-3 F-functor reconstruction; CF-S94-W1-6 α_s direct-Connes-Karoubi recovery → T5): `cross-pillar-bridge-corpus.md §18`.

"""

NEW["transport"] = """### Per-observable transport-degree scale-separation (S92 AH-TR-1; SUGGESTION at K=2)

Each substrate-IS spectral functional `O ∈ {n_s, r, n_T, α_s, …}` has a substrate-scale value (`O(M_KK)`, inside the BZ) and a CMB-pivot image under the composite bridge map `T_{BZ→pivot} ⊙ (HKR ∘ Connes-Karoubi)`; the two coincide iff `deg(T_{BZ→pivot})` is the T2-VACUOUS scalar case (unit-conversion cancelling in the dimensionless observable), and differ iff the transport is a substrate-natural NON-SCALAR morphism. The substrate=pivot-vs-substrate≠pivot verdict IS the §VII.BA five-formulation taxonomy verdict on the transport factor.

**Status**: SUGGESTION at K=2 (instances n_T, α_s). Full directive + K-counter calibration corpus: `cross-pillar-bridge-corpus.md §23`.

"""

NEW["s92mirrors"] = """### Registry-PASS criterion — Level-3 annotation discipline (S92 §VII.AX.OP-PROJ; SUGGESTION at K=1)

A registered Level-3 row's PASS verdict is governed SOLELY by the central-value criterion `Level-3 < Level-2 at canonical L_max`. Descriptive 1σ-band / edge-containment statements are NON-LOAD-BEARING annotations and MUST NOT be read as PASS predicates; a stronger band-containment gate MUST be pre-registered as a Class-8.2 verifier-rubric criterion — and is ADMISSIBLE ONLY for a substrate-IS / laboratory-IN PHYSICAL band that survives L_max → ∞ (a finite-L truncation-uncertainty envelope can NEVER be credentialed as a PASS gate). Audit-mirror: Class-(i) `INTERNALLY-INCONSISTENT-LEVEL-3-BAND-STATEMENT` at `registry-landing.md`. Calibration corpus: `cross-pillar-bridge-corpus.md §20`.

### Algebra-axis orthogonality K-counter — Regulator-behavior sibling discriminator (S92 §VII.AV; SUGGESTION at K=1)

On `(A_K, H_K, D_K)`, an algebra-DEPENDENT state-pair functional on a GAPPED occupation distribution is regulator-INVARIANT (IR-self-regularized by the gap `|Δ_a|`); an algebra-INVARIANT spectrum-only functional `Σ_k m_k g(λ_k)` is regulator-DEPENDENT (no intrinsic IR scale; bounded `O(20%)`). This is a SIBLING discriminator of the algebra-axis orthogonality conjecture on an axis ORTHOGONAL to parse-tree-membership; INDEPENDENT per Hybrid Independence Test (iv), NOT folded into the parse-tree K-counter. Full directive + calibration corpus + 2-bit fingerprint: `cross-pillar-bridge-corpus.md §22`.

### Element-5 — Class-8.3 publication-precision extension (S92 §VII.AY; SUGGESTION at K=1)

An Element-5 anchor published at `n` sig figs MUST set its Stage-2/Stage-3 verifier tolerance RELATIVE at `rel_tol ≥ 10^(−sig_figs_of_agreement)`; a floor-level PASS that cannot discriminate the anchor's candidate F-images MUST carry a `canonical-value-question-DEFERRED-to-<recompute-CF>` tag; Stage-3 separates ELIGIBILITY (tolerance fix) from STAGE-3-PERMANENT (re-pin to bit-exact substrate canonical). Primary directive home: `epistemic-discipline.md §"Publication-Precision Pre-Registration (Class 8.3)"`. Calibration corpus: `cross-pillar-bridge-corpus.md §21`.

"""

# (start_anchor, lookahead_anchor, NEW_key)
cuts = [
    ("### Tier-1/Tier-2 dimensional-re-anchorability gate", "## Single-observable-per-triple structural filter", "tier"),
    ("### Diffusion-window-observable specialization", "## IS-not-IN Anatomy (5 elements)", "diffusion"),
    ("**Status**: MANDATORY at K=3 (axis-", "**Audit**: extend", "bridge_status"),
    ("**Sub-question verdict**:", "**Status**: SUGGESTION at K=1. Promotes to MANDATORY at K=3 distinct", "composite_tail"),
    ("### Per-observable transport-degree scale-separation", "## S92 Workshop-Campaign Forward-Directive Mirrors", "transport"),
    ("### Registry-PASS criterion — Level-3 annotation discipline", "## Calibration corpus + K-counter status", "s92mirrors"),
]

for start, lookahead, key in cuts:
    pat = re.compile(re.escape(start) + r"(?s:.*?)(?=" + re.escape(lookahead) + r")")
    text, n = pat.subn(lambda m, k=key: NEW[k], text, count=1)
    assert n == 1, f"cut {key!r}: expected 1 replacement, got {n} (start anchor not found / non-unique?)"

# --- post-checks ---
assert "**Provenance**" not in text, "residual **Provenance** block remains"
assert "Verbatim directive mirrors landed by the orchestrator" not in text, "residual meta remains"
assert "subagents are edit-denied" not in text, "residual edit-denied meta remains"
for h in must_keep_headers:
    assert text.count(h) >= 1, f"post-check: header LOST: {h!r}"
# spot-check a few load-bearing rules survived
for needle in [
    "Level-2-binding** (admissible for registry-PASS)",
    "Five-formulation taxonomy",
    "| **T5** |",
    "Corner-cell declaration",
    "All 5 IS-not-IN anatomy elements present in entry text.",
]:
    assert needle in text, f"post-check: load-bearing content LOST: {needle!r}"

P.write_text(text, encoding="utf-8")
print(f"OK. lines {orig_lines} -> {text.count(chr(10))}")
print("provenance blocks removed:", n_prov, "+ meta:", n_verb, "| narrative cuts:", len(cuts))
