#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S101-VIIBM-STATEPROJ-LANDING  (S101 Wave-6, gate W6-3)
======================================================

Registry landing of the §VII.BO.STATE-PROJ STAGE-1-CANDIDATE entry:
the Connes-distance state-pair-metric generation-resolution theorem complex
(Theorem A commutative-channel cure + Lemma B star-metric closed forms +
generation-resolution existence on the state-pair metric).

Gate class: REGISTRY-LANDING ([VERIFY], GEOMETRIC). Single-shot AFTER pattern
per `.claude/rules/registry-landing.md §"Bridge-Landing Script Architecture"`
and the template `computations/_bridge_landing_script_template.py`:

    build_promotion_text  ->  write_atomic_with_fsync (APPEND)
        ->  re_read + verify_section_matches  ->  emit ONCE.

NO numerical re-derivation. The promotion text is transcribed VERBATIM from the
Stage-0 candidate text `sessions/session-100a/session-100a-connes-machinery-synthesis.md`
§IV.2 (DECLARATION) + §IV.3 (clauses/anchors/exclusions) + §II.1/§II.2/§II.3
(theorem statements + recorded numerics) + §IV.4 (authorship) + §V.3 (Stage-2
spec pointer). Binding-text rule: re-derive NOTHING.

S-1 clauses (i)-(iii) cleared at FULL STRENGTH by:
  - W2-5  S101-STAR-METRIC-BLOCK-LEMMA          PASS  audit 08ee01cb... (Lemma-B boundary)
  - W2-6  S101-CONNES-DISTANCE-DISCONNECT-BOUNDARY PASS audit 9eea4708... (disconnect two-sided dichotomy)

Slot: §VII.BO.STATE-PROJ  (.STATE-PROJ suffix MANDATORY per
`registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"`; state-side
state-pair functional, Cell IV). Reserved RESERVED-FOR-S101-W6-3-VIIBM-STATEPROJ
in `sessions/framework/s101-slot-pre-allocation-lockfile.md`.

PD-2: all-header-level (##/###/####) runtime scan confirms §VII.BO reserved + free.
PD-3: occupancy => reroute next-free-letter (suffix PRESERVED) + FAIL-with-remediation.

EXCLUSION GREP (runs INSIDE build_promotion_text, pure phase, BEFORE any disk I/O):
4 forbidden over-claim patterns per synthesis §IV.3(d). A hit aborts with
exit != 0 (script breakage, NOT a verdict) before any write.

Audit-trail observation cited per template docstring discipline:
`computations/_bridge_landing_audit_trail_observation_S87_W5.md`.
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import re
import json
import hashlib
from pathlib import Path
from datetime import datetime, timezone

import numpy as np

# Canonical constants import (MANDATORY per .claude/rules/math-scripts.md).
# This landing transcribes recorded numerics from the anchor gate's verdict line;
# no framework constant is hardcoded here that belongs in canonical_constants.py.
sys.path.insert(0, str(Path("computations/_shared").resolve()))
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Pinned identities (plan §W6-3 machinery_pin_map + input_files)
# ---------------------------------------------------------------------------
GATE_ID = "S101-VIIBM-STATEPROJ-LANDING"
SLOT_PLANNED = "§VII.BO.STATE-PROJ"
SLOT_LETTER = "BO"  # next-free letter at-or-above BM (BM=W6-1, BN=W6-2 reserved)
SCHEME = "STAGE1-REGISTRATION-AFTER-PATTERN"
CONVENTION = "SINGLE-SHOT-VERBATIM-EXTRACTION-STATE-PROJ"
L_MAX_TAG = "N/A"  # landing gate (anchor numerics carried as recorded values; cache L_max=12)
LOCKFILE_RESERVED = "RESERVED-FOR-S101-W6-3-VIIBM-STATEPROJ"

REGISTRY = Path("sessions/permanent-results-registry.md")
LOCKFILE = Path("sessions/framework/s101-slot-pre-allocation-lockfile.md")
SYNTHESIS = Path("sessions/session-100a/session-100a-connes-machinery-synthesis.md")
LADDER_NPZ = Path("computations/session-100a/s100a_connes_distance_ladder.npz")
CANON = Path("computations/_shared/canonical_constants.py")
BRIDGE_TMPL = Path("computations/_bridge_landing_script_template.py")
OUT_NPZ = Path("computations/session-101/s101_w6_3_viibm_stateproj_landing.npz")

# PRIMARY anchor (S100a-CONNES-DISTANCE-LADDER) — full 64-hex (synthesis §IV.3 / §I)
ANCHOR_AUDIT_SHA = "5e24db72e3e5121b445477e2433a3c50084a4c5951111297c439a2da9b63491a"
# Clearance audits (full 64-hex; verified present in s101_gate_verdicts.txt)
W2_5_AUDIT = "08ee01cbb254879f0c71f4feee49d525dd36e0693fdc8ce626b10c297b6c98d7"  # Lemma-B boundary
W2_6_AUDIT = "9eea47088bef70fa734a7d9fa77f709f4b7e71626e96a81df4c09c7a13d036fd"  # disconnect dichotomy

# Static input-SHA pins (plan §W6-3 input_files; verified at authoring time)
PIN_SYNTHESIS = "5dad5f4c95591221c8f698e6f7fc0410e3af0ef6a6de89bfacff48ad5e4c6847"
PIN_LADDER_NPZ = "04a0062bdb94ff5e911695b71835d0a93923b99b98a2eb669adee1cee634e737"
PIN_BRIDGE_TMPL = "876c018fafea84742d06934a2061eb765ef41a042cb87ba0f4138caffbe9a68c"

# Frozen landing-time registry-state SHAs (captured at the ORIGINAL append, run 1).
# Used in the audit-pin map so the audit_sha256 is REPRODUCIBLE across idempotent
# re-runs (a re-run sees the registry already-appended, so its live PRE == live POST;
# pinning the original PRE/POST keeps the emitted audit_sha256 = 79d2a53f… stable and
# preserves emit_verdict sig_5 idempotency). These are NOT live re-reads.
REGISTRY_PRE_SHA_AT_LANDING = "cfd22a3594b33bb5e1d2db2165413f564c53884a3b756e2827cf22d313d067f3"
REGISTRY_POST_SHA_AT_LANDING = "a8787b779f77fa0eaeeaf224cc419f8e5c3c5aa33e5e0ed90869e324c0e14190"


def sha256_file(p: Path) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def closure_hash(pin_map: dict) -> str:
    """Audit SHA from the ordered input-pin map (canonical pattern;
    never hardcoded, computed at runtime)."""
    blob = json.dumps(pin_map, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# (1) build_promotion_text — pure function, NO I/O; exclusion-grep runs HERE
# ---------------------------------------------------------------------------
def build_promotion_text(slot_letter: str) -> str:
    """Produce the EXACT §VII.{letter}.STATE-PROJ registry section text.
    Pure function. The 4-pattern exclusion grep runs at the end of this
    function (pure phase, before any disk write); a forbidden over-claim
    aborts with exit != 0 BEFORE any I/O."""
    slot = f"§VII.{slot_letter}.STATE-PROJ"

    # NOTE: plain (non-f) triple-quoted string. The markdown body contains many
    # literal {...} math expressions (set-builder, intervals, {1/9,1/3,1/3}) that
    # an f-string would mis-parse as replacement fields. Dynamic values are spliced
    # via sentinel tokens + .replace() AFTER the literal (below).
    text = """
### @@SLOT@@ — Commutative-Channel Cure Theorem + Star-Metric Closed Forms + Generation Resolution in the State-Pair Metric (STAGE-1-CANDIDATE per joint-theorem-promotion.md; S100a W2-4 / S-1 connes-machinery synthesis Stage-0 text; S101 W6-3 landing — gen-physicist; Stage-0 author connes-ncg-theorist EXCLUDED from Stage-2)

**STAGE-1-CANDIDATE** (4-stage joint-theorem pathway per `joint-theorem-promotion.md`; Stage-0 text = `sessions/session-100a/session-100a-connes-machinery-synthesis.md` §IV.2–IV.4; Stage-2 gate = `S101-CONNES-STATEPROJ-STAGE2-VERIFY`, Wave-7 gate 1). Classification **GEOMETRIC**. The three structural clauses below are transcribed VERBATIM from the Stage-0 candidate text — re-derived NOTHING. The S-1 prerequisites were cleared at FULL STRENGTH by **W2-5** (`S101-STAR-METRIC-BLOCK-LEMMA` PASS, audit `08ee01cb…`; Lemma-B operator-norm boundary verified) + **W2-6** (`S101-CONNES-DISTANCE-DISCONNECT-BOUNDARY` PASS, audit `9eea4708…`; the disconnect-divergence two-sided dichotomy confirmed: severed-edge `d_R = c·R` exact, log-log slope 1.000000, connected pairs R-flat).

**Clause (i) — Theorem A (Commutative-Channel Finiteness + EXACT Regulator-Freeness), with the two-sided CLASS-γ dichotomy.** For the connected commutative channel restriction of ANY finite spectral triple `(A, H, D)` (channel algebra `A_chan = {Σ_x a_x P_x : a_x ∈ ℝ} ≅ ℝ^N`, coupling graph `G(D)` with edge `{x,y} ⟺ P_x D P_y ≠ 0`, constants gauge-quotiented): the Connes distance `d(ε_x, ε_y)` is **finite** (supremum attained on the compact unit ball of `V = A_chan/ℝ·1`) and **exactly** regulator-free — there is a finite activation threshold `ρ* = ‖a*‖_F` such that the Frobenius-regulated `d_R = d` EXACTLY for all `R ≥ ρ*` (slope identically zero on `[ρ*, ∞)`, not asymptotically zero). The two-sided dichotomy: **Connes-distance divergence ⟺ the Lipschitz-seminorm kernel separates the state pair.** Connected commutative channel restriction ⇒ kernel `= ℝ·1` (state-blind) ⇒ finite + regulator-free; disconnection ⇒ kernel separates ⇒ linear-in-`R` CLASS-γ divergence (`d = ∞` unregulated, `d_R ∝ R` regulated). The full-`M_n(ℂ)` route always fails this for generation states (kernel `= {D}′`, state-separating) — this is the S87/S88 CLASS-γ wall, now sharp and two-sided. Numerics consistent (NOT new evidence): the S100a R-sweep max deviation **1.79e-9 over 3 decades** sits at the solver floor (tol 1e-8), the echo of an exactly-flat quantity; W2-6 confirmed the disconnected-pair linear divergence (slope 1.000000, `|slope − 1| = 1.82e-11`) and `ρ* ≤ 10·ω_max`. PORTABLE — nothing SU(3)-specific is consumed; the only triple-specific residues are the location of `ρ*` and the distance VALUES (cache floors).

**Clause (ii) — Lemma B (Star-Metric Closed Forms (7)–(8) + doubling invariance + boundary).** On any finite star (center channel `v`, leaves `g`, center-to-leaf coupling `S_g := P_v D P_g`, no leaf–leaf coupling): `d(ε_v, ε_g) = 1/‖S_g‖_op` EXACT in operator-norm generality; with scalar couplings `‖S_g‖ = t_g` and the greybody pin `t_g = 1/ω_g`, `ω_g = λ_g²(τ_fold)` (channel `D_K²`-floor from the L_max=12 cache), this is the closed form **`d(ε_v, ε_g) = ω_g = λ_g²(τ_fold)` EXACT** (eq (7)). The leaf–leaf form is **Pythagorean** `(t_g^{−2} + t_h^{−2})^{1/2}` with **equality for scalar (channel-one-dimensional) couplings** — the two-sided pinch `(t_g^{−2}+t_h^{−2})^{1/2} ≤ d(g,h) ≤ 1/t_g + 1/t_h` (eq (8)), strictly below the path sum (the finite-triple metric is NOT a geodesic/path metric). **Doubling-invariant**: isospectral `J`-doubling onto the conjugate sectors leaves `d` exact (BDI conjugate-floor equality 1.2e-15). **Boundary** (where the closed forms stop): non-star topology (any leaf–leaf coupling), gapless channels (`ω_g → 0` ⇒ metric state-merging), and non-scalar (multiplicity-resolving) channel couplings (clause (1) survives as `1/‖S_g‖_op`; clause (2) degrades to the lower bound, saturated only under top-singular-subspace alignment — the ε_LX-relevant boundary). Numerics consistent (W2-5, audit `08ee01cb…`): SDP-vs-closed-form **2.5e-9**; doubling-invariance **1.8e-9**; W2-5 verified the operator-norm form at the boundary (max dev 2.63e-8, tol 1e-7) and the Lemma B(2) saturation criterion (leaf–leaf strictly above Pythagorean off-alignment, min witness 8.629e-3; equality restored at alignment, 3.61e-10). The reported pairwise diagnostic **`W_pairwise = 1.6776`** = `d(e,μ)/d(μ,τ) = 1.734545/1.033915` is reproduced.

**Clause (iii) — Generation-resolution EXISTENCE on the state-pair metric.** The Connes state-pair distances on the greybody star, `d(v,g) = λ_g²(τ_fold)`, form a **strict ladder** `d = (0.698718, 0.762085, 1.558163)` λ²-units for `(τ, μ, e)` (cache floors `λ_g(τ_fold) = (0.83589351, 0.87297503, 1.24826413)`), relative spread **0.5516**, regulator-invariant to **1.79e-9 over 3 decades**. **`e = (3,0)` is the MOST-DISTANT channel** (largest `d`) — two-route consistent with the `S100a-YUKAWA-OVERLAP-OFFDIAG` item-6 e-sector match (`e = (3,0)`, `|w| = 1/√6`): the fabric transmits the electron channel LEAST (most greybody-suppressed). Generation resolution EXISTS in the algebra-DEPENDENT state-pair metric, WHILE the operator side stays §VII.BL-obstructed. **Scope Statement C (first-order scope rider).** The first-order residual `max‖[[D_F, a], b°]‖ = 2.0450` is **REPORTED-not-asserted-zero**; it disqualifies precisely the axiom-complete-spectral-triple and operator-side claims and disqualifies NOTHING the state-pair distance observable needs — the Connes distance is an `(A, H, D)`-level functional (requires `D = D†` and bounded commutators only; no `J`, `γ`, order-one, orientability, or Poincaré-duality enter its definition, finiteness, or closed forms). `[J, D_F] = 0` holds at 1.6e-15 and the full KO-dimension-6 sign triple `(ε, ε′, ε″) = (+1, +1, −1)` is verified at machine zero (reality-COMPATIBLE class, the §VII.BL-predicted signature). Module-membership (§VII.BL E2) ≠ a forced order-one violation: the S99 order-one-silence result shows arbitrary generation textures on admissible internal blocks satisfy `[[D_F, a], Jb*J⁻¹] = 0` identically; the 2.0450 is sourced by THIS star's inter-sector orbital couplings (chosen for the metric, not optimized for order-one admissibility).

**Clause (iv) — Annotations at INFO scope, explicitly NON-LOAD-BEARING.** Per the Level-3 annotation discipline analog (`cross-pillar-bridge-anatomy.md §"Registry-PASS criterion"`): the **undeformed-Casimir corollary** `W → 9/5 exactly` (at bi-invariant scaling `ω_g ∝ C₂(g)`, triality tower `C₂ = (4/3, 3, 6)`, `W = (6−3)/(3−4/3) = 9/5`) and the **fold-deformation factor 6.979380** (`W_Connes = Δ₁/Δ₂ = 0.796078/0.063367 = 12.562884 = (9/5) × 6.979380`, bit-identical to the §W2-3 floor decomposition) are carried as **annotations at INFO scope, NON-LOAD-BEARING**: the widening/shape question is OPEN and queued at `CF-S101-W2-BLOCKTRACE-WIDENING` (the floor-graded widening corridor is CLOSED on both routes W2-3/W2-4; the surviving corridor is whole-block heat-trace couplings). These annotations do NOT enter the STAGE-1-CANDIDATE structural content.

**JOINT-clause flag (Stage-2 PASS-AND).** The clause *"generation resolution lives in the state-pair metric WHILE the operator side stays §VII.BL-obstructed"* is flagged for Stage-2 PASS-AND across BOTH axes (logical AND, not OR) per `joint-theorem-promotion.md §"Stage 2"`. The Stage-2 spec is synthesis §V.3 = Wave-7 gate `S101-CONNES-STATEPROJ-STAGE2-VERIFY`.

**Anchors.** PRIMARY = `S100a-CONNES-DISTANCE-LADDER` (INFO; sign=PASS, magnitude=INFO, regime=VALID; full 64-hex audit_sha256 `@@ANCHOR_AUDIT_SHA@@`; npz `computations/session-100a/s100a_connes_distance_ladder.npz`). Stage-0 text = `sessions/session-100a/session-100a-connes-machinery-synthesis.md` (§IV.2–IV.4; §II.1/§II.2/§II.3 proofs). **STRUCTURAL-ORTHOGONAL-COMPANION = §VII.BL** (explicitly NOT co-primary — cross-corner co-primary FORBIDDEN per the algebra-axis orthogonality K-counter, MANDATORY at K=3: §VII.BL is the Corner-I operator-side NEGATIVE obstruction, this entry is the Corner-IV state-side POSITIVE resolution). Supporting cross-check (non-clause) = `S100a-YUKAWA-OVERLAP-OFFDIAG` item-6 e-sector match `e = (3,0)`. Lineage citation = the S88 machinery value `0.9800418463588636` WITH its INFO CLASS-γ tag intact (full-`M_n(ℂ)`, regulator-DIVERGENT); per synthesis §IV.5 the gate-name wrinkle (`…-IDENTITY` companion-row vs `…-IDENTITY-CONJECTURE` registered in `s87_gate_verdicts.txt`, producing script `s87_w1b_connes_distance_finite_spectrum_identity.py`) resolves by producing-script + value, NOT session prefix; the distinct A_F STRICT residual `1.054e-01` (S87 S-2, registry Corner-III row) is a DIFFERENT observable and must NOT be conflated with the 0.98004… machinery value.

**Registry-anatomy compliance.** (i) Entry class = **intra-pillar structural theorem on the spectral-triple axis** (precedents §VII.BJ/§VII.BK; NOT a cross-pillar bridge ⇒ the 5-anatomy IS-not-IN elements + the 3-level ladder are declared **N/A-with-reason** — and the entry is NOT dressed as one: no HKR / K-theory / Connes-Karoubi map to a laboratory-IN observable is claimed; the ℓ-calibration is a one-parameter PDG-anchored OLS, `R² = 0.9228`, NOT a zero-free-parameter map, so the Level-2 binding/non-binding HARD-HALT does not apply). (ii) **Projection-side: `.STATE-PROJ` suffix MANDATORY** — bare slot FORBIDDEN because BOTH projection-side readings exist: the operator-side reading is the NEGATIVE §VII.BL obstruction (no generation-resolving `D_F` inside any `A_K`-module; Corner I), the state-side reading is this POSITIVE Connes-distance ladder (Connes distances are the rule's own canonical state-side example). (iii) **Corner-cell: Cell IV** (algebra-DEPENDENT state-pair functional) per `permanent-results-registry.md §VII.U.2`. (iv) **Defensive parse-tree expansion block** (Class-(h) insurance — "greybody" is not in the state-history pattern set, but the reduction is carried anyway): greybody label → `t_g = 1/ω_g` → `ω_g = λ_g²(τ_fold)` → per-sector `D_K²` cache floors at L_max=12 (a closed-form reduction to substrate-algebra data). (v) **Substrate-IS level tag = Level 1** (single-τ-slice at `τ_fold = 0.190`) per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`.

**Substrate framing** (`phononic-framing.md §"IS Space, Not IN Space"`; GEOMETRIC-class). The substrate IS the finite spectral triple `(A_K, H_K, D_K(τ_fold))`; the channel state space of its commutative channel algebra IS a metric space whose Connes distances are the fabric's own statement of how strongly the generation channels couple. **Direction**: D_K eigenvalue floors `λ_g²(τ_fold)` → greybody star couplings `S_g` → Connes state-pair distances `d(v,g) = λ_g²(τ_fold)` → strict generation ladder → the electron is the channel the fabric transmits LEAST. Metric depth IS inverse coupling strength (`d(v,g) = 1/‖S_g‖`). FORBIDDEN inversion (container thinking): "the generations are masses placed on the fabric, and the metric measures distances between them in a pre-existing space" → INVERT: "the fabric's own spectral floors ARE the couplings; the Connes metric on the channel state space IS the generation geometry; there is no container — the distance ladder is intrinsic to `(A_K, H_K, D_K)` at the τ_fold slice." The widening *shape* (Casimir 9/5) survives only at whole-block spectral content (annotation, queued) — the state-pair metric route adds NO shape freedom of its own.

**Authorship + Stage-2 routing** (binding). `connes-ncg-theorist` is Stage-0 author of this candidate complex AND the S100a W2-4 executing agent ⇒ **EXCLUDED from any Stage-2 cross-review** per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"` condition 2 (original-authoring-agent exclusion with downstream-inheritance reach), restating the S99 E1 lesson. Suggested Stage-2 pairing (subject to dispatch-time `--check-reviewers --strict` static leg + downstream-inheritance grep): Axis-A (NCG-axiomatic) ∈ {`van-den-dungen-bridge-theorist`, `lizzi-spectral-functional-theorist`}; Axis-B (substrate/state-pair) ∈ {`volovik-superfluid-universe-theorist`, `landau-condensed-matter-theorist`}. Substrate-input-orthogonality designed in: Axis-A audits Theorem A / Lemma B from the registry text ALONE (no npz); Axis-B audits the numerical clauses from the npz ALONE (single-loader). Stage-2 gate = `S101-CONNES-STATEPROJ-STAGE2-VERIFY` (Wave-7 gate 1).

**Provenance.** S-1 solo synthesis (`sessions/session-100a/session-100a-connes-machinery-synthesis.md`, Stage-0 candidate text) over the `S100a-CONNES-DISTANCE-LADDER` gate (audit `@@ANCHOR_AUDIT_SHA@@`); the structural clauses (i)–(iii) cleared at FULL STRENGTH by W2-5 (`S101-STAR-METRIC-BLOCK-LEMMA` PASS, audit `@@W2_5_SHORT@@…`) + W2-6 (`S101-CONNES-DISTANCE-DISCONNECT-BOUNDARY` PASS, audit `@@W2_6_SHORT@@…`). Binding source = the S-1 frozen Stage-0 text (transcribed VERBATIM; no re-derivation). Landed S101 W6-3 (gen-physicist), single-shot AFTER pattern per `registry-landing.md §"Bridge-Landing Script Architecture"`; slot `@@SLOT@@` reserved `@@LOCKFILE_RESERVED@@` in `sessions/framework/s101-slot-pre-allocation-lockfile.md`, runtime-verified next-free at all header levels (highest prior §VII.BN, W6-2). This is a §VII intra-pillar structural-theorem landing, NOT a §7 falsifier-surface row — `mack-cosmic-bridge` sole-writer does NOT apply (precedent: §VII.BL provenance note).
"""

    # -- splice dynamic values via sentinel tokens (NOT f-string interpolation;
    #    the body carries literal {...} math the f-string parser would choke on) --
    text = (text
            .replace("@@SLOT@@", slot)
            .replace("@@ANCHOR_AUDIT_SHA@@", ANCHOR_AUDIT_SHA)
            .replace("@@W2_5_SHORT@@", W2_5_AUDIT[:8])
            .replace("@@W2_6_SHORT@@", W2_6_AUDIT[:8])
            .replace("@@LOCKFILE_RESERVED@@", LOCKFILE_RESERVED))
    # fail loudly if any sentinel survived the splice (would corrupt the entry)
    assert "@@" not in text, "unresolved @@SENTINEL@@ in promotion text"

    # -- Exclusion grep: 4 forbidden over-claim families (synthesis §IV.3(d)) --
    # Patterns target the ASSERTION form of each over-claim. They MUST NOT match
    # the legitimate scoping/negation language this entry carries (e.g. naming
    # Scope C, declaring §VII.BL-obstructed, calling star couplings external data).
    forbidden = {
        # (1) widening/shape clause AS A STRUCTURAL CLAUSE (floor corridor CLOSED;
        #     block-trace corridor must run first). The entry may MENTION widening
        #     only as an INFO/NON-LOAD-BEARING annotation or as CLOSED/queued.
        #     Forbid: a widening clause asserted as a load-bearing structural result.
        "widening_shape_as_clause": re.compile(
            r"(widening|shape)[^.\n]{0,80}\b(clause|theorem|RESOLVED|established|"
            r"load-bearing|argument-grade)\b(?![^.\n]{0,40}"
            r"(NON-LOAD-BEARING|INFO scope|annotation|CLOSED|queued|open))",
            re.IGNORECASE,
        ),
        # (2) 7-axiom real-spectral-triple claim (Scope C forbids). The entry may
        #     say the residual disqualifies axiom-completeness; forbid the POSITIVE
        #     assertion that the triple IS a complete real spectral triple.
        "seven_axiom_complete_triple": re.compile(
            r"\b(complete|axiom-complete|all\s+(seven|7)\s+(NCG\s+)?axioms?(\s+(hold|"
            r"satisfied|pass))|7-axiom)\b[^.\n]{0,80}\b(real\s+spectral\s+triple|"
            r"spectral\s+triple)\b(?![^.\n]{0,40}(NOT|fails|disqualif|outside))",
            re.IGNORECASE,
        ),
        # (3) OP-PROJ generation-resolution claim (§VII.BL stands). Forbid any
        #     assertion that generations resolve on the OPERATOR / spectrum-only /
        #     module side. The entry's positive resolution is STATE-side only.
        "op_proj_generation_resolution": re.compile(
            r"\b(operator-side|operator\s+module|OP-PROJ|spectrum-only|"
            r"operator-projection)\b[^.\n]{0,80}\b(resolv\w*|resolution)\b"
            r"[^.\n]{0,40}\bgeneration",
            re.IGNORECASE,
        ),
        # (4) "eps_LX derived from A_K" claim (contradicts §VII.BL — star couplings
        #     are external cache data). Forbid any assertion that the star couplings
        #     / ε_LX are elements of / derived from / built from A_K.
        "eps_lx_from_AK": re.compile(
            r"(ε_?LX|eps_?LX|star\s+coupling\w*)[^.\n]{0,80}\b(derived\s+from|"
            r"element\s+of|built\s+from|inside|member\s+of|in\s+the\s+Hochschild)"
            r"[^.\n]{0,30}\bA_?K\b(?![^.\n]{0,40}(NOT|outside|external|obstruct))",
            re.IGNORECASE,
        ),
    }
    hits = {}
    for name, pat in forbidden.items():
        m = pat.search(text)
        if m:
            hits[name] = m.group(0)
    if hits:
        # Forbidden over-claim in the built text => abort BEFORE any disk I/O.
        # This is SCRIPT BREAKAGE (exit != 0), NOT a FAIL verdict.
        sys.stderr.write(
            "[BUILD-ABORT] forbidden over-claim pattern(s) in built promotion text "
            "(synthesis §IV.3(d)); no disk write performed:\n"
        )
        for name, frag in hits.items():
            sys.stderr.write(f"  - {name}: {frag!r}\n")
        sys.exit(3)

    return text, list(forbidden.keys())


# ---------------------------------------------------------------------------
# (2) write_atomic_with_fsync — APPEND to the registry, fsync
# ---------------------------------------------------------------------------
def write_atomic_with_fsync(section_text: str, registry_path: Path) -> None:
    """Append the section to the registry and fsync. The append is the only
    disk mutation. (Single-writer chain PD-4; raw append is fine because the
    W6 chain runs sequentially — this is the designated writer's turn.)"""
    p = Path(registry_path)
    with open(p, "a", encoding="utf-8", newline="\n") as fh:
        fh.write(section_text)
        fh.flush()
        os.fsync(fh.fileno())


# ---------------------------------------------------------------------------
# (3) re-read + verify_section_matches
# ---------------------------------------------------------------------------
def re_read_section(registry_path: Path, slot_letter: str) -> str:
    """Re-read the appended §VII.{letter}.STATE-PROJ section from disk
    (header line through end-of-file, since this entry is the file tail)."""
    full = Path(registry_path).read_text(encoding="utf-8")
    header = f"### §VII.{slot_letter}.STATE-PROJ —"
    idx = full.find(header)
    if idx == -1:
        return ""
    # this landing is the file tail; the section runs from the header's
    # preceding newline to EOF (matching the leading-\n of section_text)
    start = idx
    # include the leading blank line the section_text begins with
    if start > 0 and full[start - 1] == "\n":
        start -= 1
    return full[start:]


def verify_section_matches(actual: str, expected: str) -> bool:
    """Strict byte equality of the on-disk section against the built text."""
    return actual == expected


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note="", extra_rows=None):
    """PRINT the verdict payload for the dispatching AGENT to pass to the
    knowledge-MCP `emit_verdict` tool (race-safe, lock-serialized single writer
    per `.claude/rules/gate-verdicts.md §"Race-Safe Emission"`). The script does
    NOT write the verdict file. Mirrors `.claude/templates/script-template.py`
    `print_verdict_payload` (delimited `<<<EMIT_VERDICT_PAYLOAD>>>` JSON block).
    [VERIFY] gate ⇒ no SIGN 3-tuple."""
    payload = {
        "session": "101",
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX_TAG),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    # human-scan canonical line + companion row
    print(f"{GATE_ID}: {verdict} -- value='{value}' scheme={SCHEME} "
          f"convention={CONVENTION} L_max={L_MAX_TAG} "
          f"audit_sha256={audit_sha} content_sha256={content_sha} schema_version=S84+")
    if extra_rows:
        for r in extra_rows:
            print(r)
    # delimited machine block for deterministic agent extraction
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# main — single-shot AFTER pattern
# ---------------------------------------------------------------------------
def main():
    # ---- log input SHAs (first 20 lines of stdout per gate-verdicts.md) ----
    canon_sha = sha256_file(CANON)
    lockfile_sha = sha256_file(LOCKFILE)
    synthesis_sha = sha256_file(SYNTHESIS)
    ladder_sha = sha256_file(LADDER_NPZ)
    bridge_sha = sha256_file(BRIDGE_TMPL)
    registry_pre_sha = sha256_file(REGISTRY)

    print(f"[INPUT-SHA] canonical_constants.py = {canon_sha}")
    print(f"[INPUT-SHA] s101-slot-pre-allocation-lockfile.md = {lockfile_sha}")
    print(f"[INPUT-SHA] session-100a-connes-machinery-synthesis.md = {synthesis_sha}")
    print(f"[INPUT-SHA] s100a_connes_distance_ladder.npz = {ladder_sha}")
    print(f"[INPUT-SHA] _bridge_landing_script_template.py = {bridge_sha}")
    print(f"[INPUT-SHA] permanent-results-registry.md (PRE-append) = {registry_pre_sha}")

    # ---- static-pin reconciliation (plan §W6-3 input_files) ----
    assert synthesis_sha == PIN_SYNTHESIS, f"synthesis SHA drift: {synthesis_sha}"
    assert ladder_sha == PIN_LADDER_NPZ, f"ladder npz SHA drift: {ladder_sha}"
    assert bridge_sha == PIN_BRIDGE_TMPL, f"bridge template SHA drift: {bridge_sha}"
    print("[PIN-RECON] static input SHAs match plan §W6-3 pins (synthesis/ladder/bridge).")

    # ---- lockfile RESERVED-FOR cross-reference (PD-2) ----
    lock_txt = LOCKFILE.read_text(encoding="utf-8")
    assert LOCKFILE_RESERVED in lock_txt, f"{LOCKFILE_RESERVED} not in lockfile"
    assert SLOT_PLANNED in lock_txt, f"{SLOT_PLANNED} not in lockfile"
    print(f"[PD-2] lockfile carries {LOCKFILE_RESERVED} -> {SLOT_PLANNED}.")

    # ---- W2-5 / W2-6 clearance audits present in the verdict file ----
    vfile = Path("computations/session-101/s101_gate_verdicts.txt")
    vtxt = vfile.read_text(encoding="utf-8")
    assert W2_5_AUDIT in vtxt, "W2-5 Lemma-B clearance audit not found in verdict file"
    assert W2_6_AUDIT in vtxt, "W2-6 disconnect clearance audit not found in verdict file"
    print("[CLEARANCE] W2-5 (08ee01cb) + W2-6 (9eea4708) clearance audits present.")

    # ---- PD-2 + idempotent-recovery + PD-3, in the CORRECT precedence order ----
    # Build the PLANNED-slot (§VII.BO) text FIRST so the occupancy decision can
    # distinguish (A) this gate's OWN prior byte-identical landing (idempotent
    # re-run -> keep the planned slot, SKIP the append) from (B) a genuine FOREIGN
    # collision (a DIFFERENT entry occupies §VII.BO -> PD-3 reroute next-free letter
    # + FAIL-with-remediation). The earlier bug rerouted on ANY occupancy, treating
    # the gate's own run-1 landing as a collision; this ordering closes that.
    registry_pre_text = REGISTRY.read_text(encoding="utf-8")
    planned_text, excl_patterns = build_promotion_text(SLOT_LETTER)
    print(f"[BUILD] promotion text built ({len(planned_text)} chars); "
          f"exclusion-grep CLEAN on {len(excl_patterns)} forbidden patterns: {excl_patterns}")

    header_pat = re.compile(r"^#{2,4}\s*§VII\." + re.escape(SLOT_LETTER) + r"\b", re.MULTILINE)
    occupied = bool(header_pat.search(registry_pre_text))
    existing_planned = re_read_section(REGISTRY, SLOT_LETTER)
    reroute_fired = False
    slot_letter = SLOT_LETTER
    section_text = planned_text
    do_append = True

    if occupied and existing_planned == planned_text:
        # (A) idempotent re-run: §VII.BO already holds THIS gate's byte-identical
        #     section (mechanical-closure-discipline.md §"Carry-forward script-bytes
        #     immutability" idempotent-recovery branch). Keep the planned slot; skip.
        do_append = False
        print(f"[PD-2/IDEMPOTENT] §VII.{SLOT_LETTER}.STATE-PROJ already on disk and "
              f"byte-identical to the built text — idempotent re-run; keep planned slot, no re-append.")
    elif occupied:
        # (B) FOREIGN collision: §VII.BO occupied by DIFFERENT content. PD-3 reroute.
        reroute_fired = True
        for cand in ["BP", "BQ", "BR", "BS", "BT", "BU"]:
            cpat = re.compile(r"^#{2,4}\s*§VII\." + re.escape(cand) + r"\b", re.MULTILINE)
            if not cpat.search(registry_pre_text):
                slot_letter = cand
                break
        section_text, _ = build_promotion_text(slot_letter)
        print(f"[PD-3] PLANNED slot §VII.{SLOT_LETTER} OCCUPIED by FOREIGN content at runtime; "
              f"REROUTED to §VII.{slot_letter}.STATE-PROJ (suffix preserved) + FAIL-with-remediation.")
    else:
        print(f"[PD-2] all-header-level scan: §VII.{SLOT_LETTER} FREE on disk (reserved + free).")

    # ---- (2) write (APPEND) + fsync (skipped on idempotent re-run) ----
    if not do_append:
        pass  # idempotent re-run: section already on disk, verified below
    else:
        existing = re_read_section(REGISTRY, slot_letter)
        if existing:
            # a non-matching prior section would mean a corrupt/partial append; this
            # gate's AFTER pattern forbids a corrective rewrite — fail honestly.
            raise RuntimeError(
                f"§VII.{slot_letter}.STATE-PROJ exists on disk but does NOT match the "
                f"built text; AFTER pattern forbids corrective rewrite (honest close).")
        write_atomic_with_fsync(section_text, REGISTRY)
        print(f"[WRITE] appended §VII.{slot_letter}.STATE-PROJ to {REGISTRY} + fsync.")

    # ---- (3) re-read + verify (single point of decision) ----
    actual = re_read_section(REGISTRY, slot_letter)
    section_match = verify_section_matches(actual, section_text)
    print(f"[VERIFY] re-read section byte-match = {section_match}")

    # post-append SHA-uniqueness / content SHA (over the re-read on-disk section)
    content_sha = sha256_text(actual)
    registry_post_sha = sha256_file(REGISTRY)
    print(f"[CONTENT-SHA] on-disk §VII.{slot_letter}.STATE-PROJ section = {content_sha}")
    print(f"[REGISTRY-SHA] permanent-results-registry.md (POST-append) = {registry_post_sha}")

    # ---- exclusion-grep status on the ON-DISK section ----
    # build_promotion_text ABORTS (exit 3) on ANY forbidden pattern in the built
    # text BEFORE any disk write; reaching this point proves the built text was
    # clean, and section_match proves the on-disk bytes == the built text. So the
    # on-disk forbidden-hit count is provably zero by construction.
    disk_forbidden_hits = 0                       # (local)
    excl_grep_vector = [0, 0, 0, 0]               # (local) 4 patterns, all clean

    # ---- verdict determination (single point) ----
    # PASS iff byte-exact match AND zero forbidden hits AND no reroute.
    if reroute_fired:
        verdict = "FAIL"
        value = (f"slot-reroute_PLANNED_{SLOT_PLANNED}_OCCUPIED_rerouted_to_"
                 f"§VII.{slot_letter}.STATE-PROJ_section_match_{section_match}_"
                 f"remediation=assess_W7_eligibility_against_rerouted_slot")
    elif section_match and disk_forbidden_hits == 0:
        verdict = "PASS"
        value = (f"landed_VII.{slot_letter}.STATE-PROJ_section_byte_match_True_"
                 f"clauses_i-iii_FULL_STRENGTH_W2-5+W2-6_cleared_"
                 f"d_ladder=(0.698718,0.762085,1.558163)lam2_e=(3,0)_most_distant_"
                 f"relspread=0.5516_regulator_inv=1.79e-9/3decades_"
                 f"thmA_finite+exact_regfree_dichotomy_lemmaB_d=1/||Sg||_W_pairwise=1.6776_"
                 f"scopeC_firstorder=2.0450_REPORTED_KO6_signs_machineZero_"
                 f"cellIV_state_pair_FORBIDDEN_co-primary_with_VII.BL_level1_tau_fold_"
                 f"annot_INFO_W=9/5+fold6.979380_NON-LOAD-BEARING_5anatomy_NA_with_reason")
    else:
        verdict = "FAIL"
        value = (f"landed_VII.{slot_letter}.STATE-PROJ_section_byte_match_{section_match}_"
                 f"forbidden_hits_{disk_forbidden_hits}_honest_close")

    # ---- audit SHA from ordered input-pin map (runtime closure; NEVER hardcoded) ----
    input_pin_map = {
        "_gate_id": GATE_ID,
        "_slot": f"§VII.{slot_letter}.STATE-PROJ",
        "_scheme": SCHEME,
        "_convention": CONVENTION,
        "_wp_id": "S101-W6-3",
        "lockfile_RESERVED_FOR": LOCKFILE_RESERVED,
        "lockfile_sha256": lockfile_sha,
        # FROZEN landing-time registry SHAs (run-1 values) for reproducible audit_sha
        # across idempotent re-runs; see REGISTRY_*_SHA_AT_LANDING constants.
        "registry_state_at_runtime_PRE": REGISTRY_PRE_SHA_AT_LANDING,
        "registry_state_POST": REGISTRY_POST_SHA_AT_LANDING,
        "anchor_S100a_CONNES_DISTANCE_LADDER": ANCHOR_AUDIT_SHA,
        "clearance_W2_5_LEMMA_B": W2_5_AUDIT,
        "clearance_W2_6_DISCONNECT": W2_6_AUDIT,
        "synthesis_sha256": synthesis_sha,
        "ladder_npz_sha256": ladder_sha,
        "bridge_template_sha256": bridge_sha,
        "canonical_constants_sha256": canon_sha,
        "exclusion_patterns": excl_patterns,
        "section_byte_match": section_match,
        "reroute_fired": reroute_fired,
    }
    audit_sha = closure_hash(input_pin_map)

    # ---- landing-record npz ----
    OUT_NPZ.parent.mkdir(parents=True, exist_ok=True)
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        slot=f"§VII.{slot_letter}.STATE-PROJ",
        slot_planned=SLOT_PLANNED,
        verdict=verdict,
        section_byte_match=bool(section_match),
        reroute_fired=bool(reroute_fired),
        content_sha256=content_sha,
        audit_sha256=audit_sha,
        registry_pre_sha=registry_pre_sha,
        registry_post_sha=registry_post_sha,
        anchor_audit_sha=ANCHOR_AUDIT_SHA,
        clearance_w2_5=W2_5_AUDIT,
        clearance_w2_6=W2_6_AUDIT,
        exclusion_grep_vector=np.array(excl_grep_vector, dtype=int),
        exclusion_pattern_names=np.array(excl_patterns),
        d_ladder=np.array([0.698718, 0.762085, 1.558163]),
        lambda_floors=np.array([0.83589351, 0.87297503, 1.24826413]),
        rel_spread=0.5516,
        regulator_inv=1.79e-9,
        W_pairwise=1.6776,
        first_order_residual=2.0450,
        W_undeformed_casimir="9/5",
        fold_factor=6.979380,
        ts=datetime.now(timezone.utc).isoformat(),
    )
    print(f"[NPZ] landing record -> {OUT_NPZ}")

    # ---- (5) emit ONCE: PRINT the verdict payload (agent calls emit_verdict) ----
    # content_sha256 over the re-read on-disk section; audit_sha256 over the pin map.
    # The script does NOT write the verdict file (race-safe emit_verdict owns that
    # single lock-serialized write per gate-verdicts.md §"Race-Safe Emission").
    companion = (
        f"§VII.{slot_letter}.STATE-PROJ Cell-IV state-pair generation-resolution "
        f"STAGE-1-CANDIDATE; clauses (i)-(iii) FULL STRENGTH "
        f"[W2-5 Lemma-B 08ee01cb + W2-6 disconnect-dichotomy 9eea4708 cleared]; "
        f"STRUCTURAL-ORTHOGONAL-COMPANION to §VII.BL (cross-corner co-primary FORBIDDEN, "
        f"algebra-axis orthogonality K=3); 5-anatomy N/A-with-reason (intra-pillar, not a bridge); "
        f"Stage-0 author connes-ncg-theorist EXCLUDED from Stage-2 "
        f"(Wave-7 S101-CONNES-STATEPROJ-STAGE2-VERIFY)"
    )
    print("\n" + "=" * 72)
    print("VERDICT PAYLOAD (PRINT-only; agent calls emit_verdict knowledge-MCP tool):")
    print("=" * 72)
    print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note=companion)
    print("=" * 72)

    # script health: exit 0 regardless of PASS/FAIL (FAIL is a valid scientific result)
    sys.exit(0)


if __name__ == "__main__":
    main()
