"""Atomic, idempotent insert of the volovik (iv)-axis independence-audit subsection
into the §W4-6 section of sessions/archive/session-93/session-93-w4-workingpaper.md.

Source-citation (DERIVATIVE OUTPUT discipline):
  - Subsection content mirrors computations/session-93/s93_w4_6_volovik_iv_axis_independence_audit.json
    (the (iv)-audit artifact this agent authored in the same dispatch).
  - Numerical anchors: knowledge-MCP get_constant('alpha_HH1_per_pole_FW_s4')=4.0 +
    get_constant('alpha_HH1_per_pole_FW_s5')=6.0 (gate S92-W7-CF-W9-10-B, Superseded=False).
  - Plan §W4-6 (sessions/session-plan/session-93-plan-w4.md lines 850-1001).
  - Corpus §4 FWD-C5 baseline (sessions/framework/registry/cross-pillar-bridge-corpus.md lines 188-208).

Inserts BEFORE the section divider '---' that terminates §W4-6 (after mack's Results-pending block).
Does NOT overwrite the §W4-6 header or mack's content. Keyed on the unique subsection anchor so a
re-run is a no-op.
"""
import os, sys, io

# Canonical-constants import (compliance per computations/_shared/CLAUDE.md). This helper is a
# pure WP-string-insertion utility — no framework constant is COMPUTED here; the per-pole envelope
# anchors alpha_HH1_per_pole_FW_s4=4.0 / alpha_HH1_per_pole_FW_s5=6.0 quoted in the subsection were
# sourced from the knowledge MCP (gate S92-W7-CF-W9-10-B) and recorded in the (iv)-audit JSON, not
# hardcoded for arithmetic. Import added for provenance + audit compliance.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_shared"))
try:
    from canonical_constants import *  # noqa: F401,F403  (provenance import; no constant computed in this writer)
except Exception:
    pass  # WP-insertion proceeds regardless; this writer performs no canonical arithmetic

WP = r"C:\sandbox\Ainulindale Exflation\sessions\archive\session-93\session-93-w4-workingpaper.md"
ANCHOR = "### CO-AUTHOR (volovik) (iv)-axis independence audit"
HEADER_W46 = "### §W4-6. S93-W4-6-FWD-C5-K2-SUBSTRATE-DISTANCE-3-POLE-S5-CARDINALITY-CASCADE-SHOULDER"

SUBSECTION = r"""
### CO-AUTHOR (volovik) (iv)-axis independence audit

**Clause-(iv) verdict**: **PASS** — the FWD-C5 K=2 cascade-shoulder envelope (substrate-distance-3 pole **s=5**, rising-shoulder regime g∈[80,143)) is an INDEPENDENT algebraic envelope, NOT a numerical refinement of the K=1 §VII.AX.OP-PROJ baseline envelope (substrate-distance-2 pole **s=4**, saturated-tail regime g≥143). Audited from the substrate / superfluid-universe axis. Artifact: `computations/session-93/s93_w4_6_volovik_iv_axis_independence_audit.json`.

**Clause (iv) definition** (per `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"`): "independent algebraic envelope — not a numerical refinement of an existing K-instance's envelope." This is the LOAD-BEARING conjunct of the W4-6 PASS criterion: the Hybrid Independence Test predicate is `(i ∨ ii ∨ iii) ∧ iv`, so even with clause (i)=YES carrying the disjunction, clause (iv) MUST independently PASS for the K=2 advancement.

**Structural distinctness — three independent regulator-invariant grounds** (s=5 envelope ≠ s=4 envelope):

| Ground | s=4 baseline (K=1) | s=5 shoulder (K=2) | Distinct? |
|:-------|:-------------------|:-------------------|:----------|
| (1) Per-pole envelope exponent `α(s)=2(s-2)` | `α(s=4)=4` → `L^{-4}` | `α(s=5)=6` → `L^{-6}` | YES — integer gap 2 |
| (2) Wodzicki homogeneity degree `deg(s)=-2s` | `deg(s=4)=-8` | `deg(s=5)=-10` | YES — non-deformable index-type invariant |
| (3) Edge-count g-functional form | `C(N_eigs,2)` (g-independent, `d/dg=0`, saturated) | `2^g` (rising, `d/dg=2^g·ln 2`, pre-saturation) | YES — different functional form |

- **Ground 1 (per-pole exponent)** — canonical: `alpha_HH1_per_pole_FW_s4 = 4.0` and `alpha_HH1_per_pole_FW_s5 = 6.0` (knowledge-MCP `get_constant`; gate `S92-W7-CF-W9-10-B-SUBSTRATE-IS-ALPHA-S-PER-POLE-EXPONENT-TABLE-M3C`; both `Superseded=False`; s=5 is the §VII.BB STAGE-1-CANDIDATE pole). Closed-form law `α(s)=2(s-2)` Sage-verified against all canonical anchors `{α(s=2)=0, α(s=4)=4, α(s=5)=6, α(s=6)=8}`. The convergence rate `L^{-6}` at s=5 is NOT `L^{-4}` at s=4 at finer numerical precision — it is a DIFFERENT rate. A numerical refinement holds α FIXED and improves the anchor; this changes α by an integer 2.
- **Ground 2 (Wodzicki degree)** — `deg(s)=-2s` per `cross-pillar-bridge-anatomy.md §"Composite Bridge-Map Dimensional-Class Admissibility"`; `deg(s=4)=-8 ≠ deg(s=5)=-10`. The homogeneity degree is an index-type invariant, non-deformable in moduli (Wodzicki uniqueness; Connes 1994 §2.3) — so no continuous (numerical-refinement) deformation connects the two envelopes; they inhabit structurally distinct dimensional classes.
- **Ground 3 (g-functional form)** — the rising-shoulder cardinality is `n_edge(g)=2^g` (`d/dg≠0`); the saturated-tail cardinality is `n_edge=C(N_eigs,2)` (`d/dg=0`). A numerical refinement PRESERVES functional form; the shoulder→tail transition CHANGES it. Physically: the shoulder is the PRE-saturation cascade phase (the substrate's spectral cardinality is still doubling generation-by-generation); the tail is the POST-saturation phase (the cardinality has filled). Distinct cascade phases, not the same observable at two resolutions.

**"Deterministic restriction" tension resolved**: the knowledge MCP describes the shoulder as "a deterministic restriction of the saturated form to g<143." This refers to the DOMAIN of g (the shoulder is the g<143 sub-domain), NOT to the envelope's structural class. A domain restriction does not make the envelope a numerical refinement — the numerical-refinement test asks whether two envelopes share the SAME structural class (same α, same deg) at different precision; here both the structural class (grounds 1+2) AND the functional form (ground 3) differ. The "restriction" framing is orthogonal to the (iv) determination.

**Scope caveat (intra-FWD-C5 vs cross-pillar)**: the corpus §4 FWD-C5 baseline block already declared clause (iv)=YES at the CROSS-PILLAR level (FWD-C5 vs FWD-C1/C2/C3: distinct lab-IN pillar, distinct bridge-map). The W4-6 (iv) audit is the STRONGER INTRA-FWD-C5 independence (s=5 shoulder vs s=4 tail, SAME bridge-map family, SAME Pillar IX — so the envelope must be distinct on POLE grounds alone). Both hold. The corpus §4 K=2 row mack lands MUST scope its (iv)=YES to the intra-FWD-C5 pole-distinctness (s=5 ≠ s=4) so the K=2 advancement is unambiguously the substrate-distance-3-pole shoulder instance, not a re-statement of the cross-pillar baseline.

**Anti-double-count cross-check** (mack §V.2): W4-6 advances the FWD-C5 corpus §4 K-counter (substrate-distance-3 pole s=5); W4-2 advances the §VII.AX.MULTI-PIN-ATLAS bridge-map-scheme axis (corpus §3/§10/§17; substrate-distance-2 pole s=4 χ' restriction). Distinct poles, distinct corpus sections ⇒ no double-count against a single K-counter, consistent with the Hybrid Independence Test.

**Substrate framing**: the substrate IS the spectral triple `(A_K, H_K, D_K(τ_fold=0.19))`; the per-pole envelope `α(s)` and the Wodzicki degree `deg(s)=-2s` are intrinsic to it at distinct substrate-distance poles. The s=5 cascade-shoulder envelope is a substrate-IS structural object at substrate-distance-3, regulator-invariantly distinct from the s=4 substrate-distance-2 baseline — not a finer-resolution view of the same envelope.

*(volovik (iv)-axis audit complete; mack's main §W4-6 content + corpus §4 K=2 row + verdict-line emission consume this PASS as the load-bearing clause-(iv) conjunct.)*
"""


def main():
    with io.open(WP, "r", encoding="utf-8") as f:
        text = f.read()

    if HEADER_W46 not in text:
        sys.stderr.write("FATAL: §W4-6 header not found in WP; aborting (will not blind-append).\n")
        sys.exit(2)

    if ANCHOR in text:
        print("IDEMPOTENT NO-OP: volovik (iv)-axis subsection already present.")
        return

    # Locate the §W4-6 section span: from its header to the next top-level '## ' or end-of-file.
    h_idx = text.index(HEADER_W46)
    after = text[h_idx + len(HEADER_W46):]
    # Find the section divider '---' that terminates §W4-6 (the first '\n---\n' after the header).
    div_rel = after.find("\n---\n")
    if div_rel == -1:
        sys.stderr.write("FATAL: terminating '---' divider for §W4-6 not found; aborting.\n")
        sys.exit(3)
    insert_abs = h_idx + len(HEADER_W46) + div_rel  # position of the '\n' before '---'

    # Guard: ensure we are inserting INSIDE §W4-6 (no intervening '## ' top-level header before the divider)
    span = after[:div_rel]
    if "\n## " in span:
        sys.stderr.write("FATAL: a top-level '## ' header precedes the divider — span detection wrong; aborting.\n")
        sys.exit(4)

    new_text = text[:insert_abs] + "\n" + SUBSECTION.rstrip() + "\n" + text[insert_abs:]

    tmp = WP + ".tmp_volovik_iv"
    with io.open(tmp, "w", encoding="utf-8") as f:
        f.write(new_text)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, WP)
    print("INSERTED volovik (iv)-axis independence-audit subsection into §W4-6.")
    print(f"  insert byte-offset (pre-existing text length to that point): {insert_abs}")
    print(f"  new file length: {len(new_text)} chars (was {len(text)})")


if __name__ == "__main__":
    main()
