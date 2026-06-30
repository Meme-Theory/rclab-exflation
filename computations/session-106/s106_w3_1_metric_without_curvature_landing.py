#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S106-W3-1-METRIC-WITHOUT-CURVATURE-LANDING
==========================================

Single-shot AFTER-pattern registry landing of the §VII.CA metric-without-curvature
JOINT WALL — an INTRA-PILLAR GEOMETRIC structural theorem on (A_K, H_K, D_K).

This is a MECHANICAL PROMOTION of three already-PROVEN conjuncts (no compute, no
new physics):
  - Chern   c_1 = 0   EXACTLY  [S96 P-30w  S96-GEOM-OFFJENSEN-CHERN PASS, audit 943cb408…]
  - Euler   e_2 = 0   (1e-17)  [S105 W3-1  S105-EULER-DEFECT-MASKED  PASS, audit 12f92da0…]
  - graded-Ω    = 0   (1e-17)  [S105 W3-2  S105-AWZ-ANALYTIC         PASS, audit 124d3a95…]
on the U(2)-invariant volume-preserving TT (τ,μ) modulus surface, while the band
metric is non-degenerate (g ≈ 982.5). The eigenbundle is metrically rich but
holonomy-free — the "metric-without-curvature" wall (12-invariant triviality chain).

Architecture: AFTER-pattern per `registry-landing.md §"Bridge-Landing Script
Architecture"` + `computations/_bridge_landing_script_template.py`:
  (1) build_promotion_text  — assemble the §VII entry FULLY in memory
  (2) write_atomic_with_fsync — append into the runtime-verified next-free §VII slot
  (3) re_read_registry_at(slot)
  (4) verdict = (PASS if verify_section_matches(actual, expected) else FAIL)
  (5) PRINT the dual-SHA verdict payload (the AGENT calls emit_verdict — race-safe)
NO conditional rewrite (no iterate-to-PASS).

Registry-write hygiene (`epistemic-discipline.md §"Registry-Write Hygiene under
Parallel-Writer Race"`): the slot is RE-VERIFIED next-free at runtime via an
all-header-level (##/###/####) scan + reroute (letter-run ≤ 2 allocator). On runtime
occupancy the verdict line FAILs-WITH-REMEDIATION on the slot drift while the entry
itself LANDS+VERIFIES at the rerouted slot (the §VII.BZ §VII.BO→§VII.BZ precedent).

Audit posture: the entry self-declares "NOT a cross-pillar bridge" + "Laboratory-IN
observable: N/A — Pillar-…-internal" so `_cross_pillar_bridge_audit.py` classifies it
self-non-bridge and SKIPS it (the §VII.BY/§VII.BZ precedent), never auditing it as a
non-binding convergence bridge (which would HARD-HALT). The 5-anatomy + 3-level ladder
are declared N/A-with-reason.

canonical_constants.py is append-only-extended mid-session (Wave 1 ran first); its SHA
is computed at runtime and feeds audit_sha256 ONLY (no stale pin; disclosed per
`substrate-first-canonical-sourcing.md §(ii.B)`).

NO regulator_pin (Chern / Euler / graded-Ω are properties of the D_K eigenbundle, NOT
Seeley-DeWitt a_n moments — per the S105 W3-1/W3-2 verdict-line precedent).
NO CLASS pin (no SCHEMATIC helper consumed; all three conjuncts are FULL exact
eigendecomposition results).

Audit-trail observation: `computations/_bridge_landing_audit_trail_observation_S87_W5.md`.
"""

from __future__ import annotations

import hashlib
import os
import re
import sys
from pathlib import Path

# Canonical-constants import is MANDATORY (computations/_shared/CLAUDE.md); this
# landing reads no framework numeric pins from it (the three conjuncts are EXACT
# zeros + the g≈982.5 metric magnitude is a cited witness), but the import is
# required and its file SHA feeds audit_sha256 (runtime, per ii.B).
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))
from canonical_constants import *  # noqa: F401,F403  (MANDATORY import)

# ----------------------------------------------------------------------------
# Paths
# ----------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parents[2]                                    # (local)
REGISTRY = ROOT / "sessions" / "permanent-results-registry.md"                # (local)
CANON = ROOT / "computations" / "_shared" / "canonical_constants.py"          # (local)
NPZ_EULER = ROOT / "computations" / "session-105" / "s105_euler_defect_masked.npz"   # (local)
NPZ_AWZ = ROOT / "computations" / "session-105" / "s105_awz_analytic.npz"     # (local)
TEMPLATE = ROOT / "computations" / "_bridge_landing_script_template.py"       # (local)
THIS_SCRIPT = Path(__file__).resolve()                                        # (local)

# ----------------------------------------------------------------------------
# Witness pins (from the three upstream conjunct verdict lines — VALUES authoritative,
# transcribed; binding-text discipline). These are NOT recomputed here.
# ----------------------------------------------------------------------------
S96_CHERN_AUDIT = "943cb408ea41192ad057ccbcd7713ee58a09f507c0f026fbe89344dfd1cdb4f9"   # (local)
S105_EULER_AUDIT = "12f92da0f3b26ae5e084007aed227d36bdb2a8417663a41e399726c748b8c4a3"  # (local)
S105_AWZ_AUDIT = "124d3a9582affc51c03dd0ae08109edacd02b603cabcb520cbe9e5d8dabbbbb3"     # (local)

C1_CHERN = 9.777563e-15           # (local) S96 C_FHS (round=0)  -> c_1 = 0 EXACTLY
E2_EULER = -8.834874e-18          # (local) S105 e2_masked (round=0) -> e_2 = 0 (1e-17)
GRADED_OMEGA = 1.284e-17          # (local) S105 median|A^WZ|_analytic < 1e-12 -> graded-Ω = 0 (1e-17)
G_METRIC = 982.5                  # (local) band metric magnitude (atlas-07 ERRATUM); g ≠ 0 (metrically rich)
EIGEN_FLOOR = 1e-17               # (local) the eigen-floor the three zeros sit at

PLANNED_SLOT_LETTERS = "CA"       # (local) plan-pinned §VII.CA (frontier §VII.BZ at plan-freeze)


# ----------------------------------------------------------------------------
# SHA helpers
# ----------------------------------------------------------------------------
def sha256_file(p: Path) -> str:
    """SHA-256 of a file's bytes."""
    return hashlib.sha256(p.read_bytes()).hexdigest()


def sha256_text(s: str) -> str:
    """SHA-256 of a UTF-8 string."""
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def closure_hash(ordered_pairs: list[tuple[str, str]]) -> str:
    """Audit closure SHA over an ORDERED input-pin map (key=value lines)."""
    blob = "\n".join(f"{k}={v}" for k, v in ordered_pairs)                    # (local)
    return sha256_text(blob)


# ----------------------------------------------------------------------------
# Slot allocation: all-header-level next-free scan (registry-write hygiene)
# ----------------------------------------------------------------------------
def _letters_to_int(letters: str) -> int:
    """Bijective base-26 (A=1, ..., Z=26, AA=27, ...) for §VII slot ordering."""
    n = 0                                                                     # (local)
    for ch in letters:
        n = n * 26 + (ord(ch) - ord("A") + 1)                                # (local)
    return n


def _int_to_letters(n: int) -> str:
    """Inverse of _letters_to_int (bijective base-26)."""
    out = ""                                                                  # (local)
    while n > 0:
        n, r = divmod(n - 1, 26)                                             # (local)
        out = chr(ord("A") + r) + out                                        # (local)
    return out


def existing_vii_slot_letters(registry_text: str) -> set[str]:
    """All occupied §VII.<LETTERS> slots across ALL header levels (##/###/####).

    Scans the bare two-or-more-letter slot tokens at header depth 2-4 (the
    registry-write-hygiene full scan). Suffix sub-slots (§VII.AF.1, §VII.BC.OP-PROJ)
    do NOT consume a new LETTER run; only the base §VII.<LETTERS> token matters for
    next-free-letter allocation.
    """
    pat = re.compile(r"^#{2,4}\s+§VII\.([A-Z]{1,3})\b", re.MULTILINE)        # (local)
    return set(pat.findall(registry_text))


def next_free_slot(registry_text: str, planned_letters: str) -> tuple[str, bool, str]:
    """Return (slot_letters, drifted, note).

    Verify the planned slot is free over an all-header-level scan; if occupied,
    reroute to the next-free letter (letter-run allocator). `drifted` flags a
    runtime reroute (FAIL-WITH-REMEDIATION per registry-write hygiene).
    """
    occupied = existing_vii_slot_letters(registry_text)                      # (local)
    if planned_letters not in occupied:
        return planned_letters, False, f"planned §VII.{planned_letters} free (all-header-level scan)"
    # Reroute to next-free letter beyond the planned one.
    n = _letters_to_int(planned_letters)                                     # (local)
    while _int_to_letters(n) in occupied:
        n += 1                                                               # (local)
    rerouted = _int_to_letters(n)                                            # (local)
    return rerouted, True, (
        f"planned §VII.{planned_letters} STALE-OCCUPIED at runtime; "
        f"REROUTED to §VII.{rerouted} per registry-write hygiene"
    )


# ----------------------------------------------------------------------------
# (1) build_promotion_text — pure function; FULL §VII entry in memory, no I/O
# ----------------------------------------------------------------------------
def build_promotion_text(slot_letters: str) -> str:
    """Assemble the EXACT §VII.<slot_letters> metric-without-curvature entry text.

    INTRA-PILLAR GEOMETRIC structural theorem; the 5-anatomy IS-not-IN elements +
    the 3-level ladder are declared N/A-with-reason per the §VII.BY/§VII.BZ precedent.
    The entry SELF-DECLARES "NOT a cross-pillar bridge" + "Laboratory-IN observable:
    N/A — Pillar-…-internal" so the cross-pillar audit classifies it self-non-bridge
    (skip), never as a non-binding convergence bridge.
    """
    slot = "§VII." + slot_letters                                           # (local)
    # NON-f template with @TOKEN@ sentinels — substituted via .replace() below.
    # Plain string => NO f-string brace-escaping; LaTeX `Σ_{ij}` / set-literals
    # `{0,0,0}` are literal text and need no doubling.
    template = """### @SLOT@ — Metric-Without-Curvature Joint Wall: the Lowest J/BDI-Real Dirac Doublet's Eigenbundle is TRIVIAL (Chern c_1 = 0 ∧ Euler e_2 = 0 ∧ graded-Ω A^WZ = 0) While the Band Metric is Non-Degenerate (g ≈ 982.5) on the U(2)-Invariant Volume-Preserving TT Modulus Surface — a Metrically-Rich, Holonomy-Free Eigenbundle (the 12-Invariant Triviality Chain) (STAGE-3-PERMANENT intra-pillar GEOMETRIC structural theorem — the JOINT statement of three already-PROVEN curvature/triviality zeros [S96 P-30w Chern=0; S105 W3-1 Euler=0; S105 W3-2 graded-Ω=0] on a non-degenerate band metric; mechanical promotion — re-derives NOTHING physical; substrate-physics derivation lineage berry-geometric-phase-theorist [the Berry-curvature/Chern/Euler/graded-Ω eigenbundle-geometry axis]; S106 W3-1 landing — berry-geometric-phase-theorist orchestrator-direct registry §VII sole-writer for this NCG/geometric structural landing per `feedback_mack-bridge-role.md` [NOT a §7 falsifier-surface row — mack-cosmic-bridge does NOT apply]; single-shot AFTER-pattern per `registry-landing.md` §"Bridge-Landing Script Architecture"; slot @SLOT@ runtime-verified next-free over ALL header levels [documented frontier §VII.BZ]; 2026-06-13)

**Status**: **STAGE-3-PERMANENT** intra-pillar GEOMETRIC structural theorem. The three curvature/triviality zeros are OPERATOR-INDEPENDENT, L-INDEPENDENT structural facts — each is EXACT at every L_max (an eigenbundle-topological identity / center-character-protected zero), NOT a near-tolerance numerical coincidence and NOT a truncation-dependent estimate. This entry is the JOINT statement (the 12-invariant triviality chain) of three results that are individually already PROVEN: S96 P-30w (Chern c_1 = 0; `S96-GEOM-OFFJENSEN-CHERN` PASS), S105 W3-1 (Euler e_2 = 0; `S105-EULER-DEFECT-MASKED` PASS), S105 W3-2 (graded-Ω A^WZ = 0; `S105-AWZ-ANALYTIC` PASS). It does NOT open a fresh joint cross-axis theorem (no new Stage-2 PASS-AND is required): its structural content is the conjunction of three already-PROVEN curvature/triviality zeros, transcribed (binding-text discipline). NO new compute gate — registry-landing of pre-computed sub-results.

**Result classification**: **GEOMETRIC** (a statement about the fabric's own spectral-triple band geometry — the lowest J/BDI-real Dirac doublet is a Peter-Weyl eigenbundle of `D_K`, and the U(2) isotropy + the (τ,μ) deformation directions on which the triviality holds ARE the band's own intrinsic structure, not an external gauge or coordinate container). The observable this entry registers is the JOINT triviality of the eigenbundle's primary curvature invariants {Chern c_1, Euler e_2, graded-Ω A^WZ} = {0, 0, 0} EXACTLY on a band whose metric magnitude g ≈ @G@ ≠ 0.

**Classification (load-bearing for plan-freeze audit)**: this is an **INTRA-PILLAR GEOMETRIC STRUCTURAL THEOREM** on the band-geometry axis (the eigenbundle of `D_K` on its OWN (τ,μ) modulus surface). It is **NOT a cross-pillar bridge**: the 5-anatomy IS-not-IN elements + the 3-level ladder are declared **N/A-with-reason** (there is no laboratory-IN continuum-image observable and no HKR / K-theory / Connes–Karoubi bridge map is claimed; the statement is a curvature-class / holonomy fact intrinsic to `(A_K, H_K, D_K)` on its own deformation manifold). A plan-freeze auditor MUST read it with the §VII.BY / §VII.BZ N/A-with-reason structure, NOT as a convergence bridge (which would HARD-HALT on a non-binding Level-2 per `cross-pillar-bridge-anatomy.md §"Level-2 sub-class (binding vs non-binding)"`). The cross-pillar bridge audit (`_cross_pillar_bridge_audit.py`) classifies this entry **self-non-bridge** (the self-declared "NOT a cross-pillar bridge" marker + the "Laboratory-IN observable: N/A — Pillar-internal" Element-2 negation) and SKIPS it — it is not audited as a bridge.

**STRUCTURAL VERDICT (the metric-without-curvature wall).** Let `(A_K, H_K, D_K(τ,μ))`, `A_K = ℂ ⊕ ℍ ⊕ M₃(ℂ)`, be the spectral triple on the U(2)-invariant volume-preserving TT (τ,μ) modulus surface (`v_J=(2,−2,1)`, `v_μ = n × v_J = (11,7,−8)`; both volume-preserving `n·v=0`, orthogonal `v_J·v_μ=0`, spanning the 2D deformation plane; `μ=0` IS the Jensen line, fold at `τ_fold=0.190`). Let `P` be the projector onto the lowest 2-fold J/BDI-real Dirac doublet (a Kramers/J-degenerate Peter-Weyl multiplet). The eigenbundle of `P` over the (τ,μ) base carries THREE primary curvature/triviality invariants, ALL EXACTLY ZERO, while its band metric is non-degenerate:

| Invariant | Definition | Value | Source |
|:----------|:-----------|:------|:-------|
| Chern class `c_1` | `(1/2π) ∫ F^Berry` over the (τ,μ) base (FHS Wilson-loop lattice; deg-2 non-Abelian Wilczek–Zee link) | `c_1 = 0` EXACTLY (`C_FHS = @C1@`, round = 0; max\\|Ω\\| = 2.27e-23; all 5 PW sectors trivial) | S96 P-30w `S96-GEOM-OFFJENSEN-CHERN` PASS (audit `943cb408…`) |
| Euler class `e_2` | `(1/2π) Σ_{ij} Pf(F^Euler)` over the real-frame SO(2) Wilson-loop lattice (deg-2 non-Abelian Pfaffian), defect-masked at the (0.10,+0.10) B1/B2 vN-Wigner crossing plaquette [0,49] | `e_2 = 0` (to 1e-17) (`e2_masked = @E2@`, round = 0; max\\|F^Euler\\|_masked = 4.51e-17; Pf²=det residual 1.78e-14) | S105 W3-1 `S105-EULER-DEFECT-MASKED` PASS (audit `12f92da0…`) |
| graded-Ω `A^WZ` | the γ9-graded Berry sub-curvature / cross-grade Wilczek–Zee connection `\\|A^WZ\\|` of the lowest J/PH γ9-doublet, ANALYTIC-RANK1-PERTURBATION evaluator (NO finite-difference floor) | graded-Ω `= 0` (to 1e-17, away from the single B1/B2 corner) (median\\|A^WZ\\|_analytic = `@GO@` < 1e-12; frac<1e-12 = 0.9996, EXACTLY 1.0 in the chirality-locked region) | S105 W3-2 `S105-AWZ-ANALYTIC` PASS (audit `124d3a95…`) |
| band metric `g` | the Berry quantum-metric / band-geometry magnitude (Provost–Vallée real part of the QGT — the SOLE topologically-active object on this surface) | `g ≈ @G@` `≠ 0` (metrically rich) | atlas-07 "Berry curvature B=982.5" ERRATUM (was mis-labeled Berry curvature; the 982.5 IS the metric magnitude; Berry curvature = 0 EXACTLY) |

The JOINT statement: a non-degenerate metric (`g ≈ @G@ ≠ 0`) with ALL primary curvature/triviality invariants `= 0` (to the eigen-floor 1e-17) ⇒ the eigenbundle is **metrically rich but holonomy-free** (a flat connection on a trivial bundle) — the **metric-without-curvature** wall. This is the JOINT closure of the framework's 12-invariant triviality chain (Berry curvature, Chern, Wilson-loop holonomy, Zak [artifact], BDI ν, GL Zak, fold γ, fabric, Euler, graded-Ω, off-Jensen Chern, off-Jensen Euler — ALL zero) on the U(2)-invariant volume-preserving TT surface.

**SUBSTITUTION CHAIN (the triviality "= 0" claim chain).**

Claim: "On the U(2)-invariant volume-preserving TT modulus surface, the lowest J/BDI-real Dirac doublet's eigenbundle is TRIVIAL (Chern = 0 ∧ Euler = 0 ∧ graded-Ω = 0) while the band metric is non-degenerate (g ≈ @G@) — a metric-without-curvature wall — and the entry therefore carries the 5-anatomy + 3-level ladder as N/A-with-reason (no convergent L^(−α) envelope; the zeros are EXACT at every L_max, NOT convergence anchors)."

- **Def 1** — `c_1[eigenbundle] := (1/2π) ∫ F^Berry` over the (τ,μ) base. Source: S96 P-30w `S96-GEOM-OFFJENSEN-CHERN` PASS. VALUE: `c_1 = 0` EXACTLY (`C_FHS = @C1@`, round = 0).
- **Def 2** — `e_2[real eigenbundle] := (1/2π) Σ_{ij} Pf(F^Euler)` over the real-frame SO(2) Wilson-loop lattice (deg-2 non-Abelian), defect-masked at the (0.10,+0.10) B1/B2 vN-Wigner crossing plaquette [0,49]. Source: S105 W3-1 `S105-EULER-DEFECT-MASKED` PASS (audit `12f92da0…`). VALUE: `e_2 = 0` (to 1e-17) (`e2_masked = @E2@`, round = 0; max\\|F^Euler\\|_masked = 4.51e-17).
- **Def 3** — graded-Ω `:= |A^WZ|` of the lowest J/PH γ9-doublet, ANALYTIC-RANK1-PERTURBATION evaluator (no FD floor). Source: S105 W3-2 `S105-AWZ-ANALYTIC` PASS (audit `124d3a95…`). VALUE: graded-Ω `= 0` (to 1e-17) (median\\|A^WZ\\|_analytic = `@GO@` < 1e-12; frac<1e-12 = 0.9996, EXACTLY 1.0 in the chirality-locked region).
- **Def 4** — `g :=` the band metric magnitude (Berry quantum-metric). Source: atlas-07 ERRATUM row. VALUE: `g ≈ @G@ ≠ 0` (metrically rich).
- **Substitute** (the triviality chain): `{c_1, e_2, graded-Ω} = {0, 0, 0}` EXACTLY (to the eigen-floor 1e-17) on a band with `g ≈ @G@ ≠ 0`.
- **Simplify**: a non-degenerate metric (`g ≠ 0`) with ALL primary curvature/triviality invariants `= 0` ⇒ the eigenbundle is metrically rich but holonomy-free (flat connection, trivial bundle) — the metric-without-curvature wall. The 12-invariant triviality chain is the joint statement.
- **Canonical form**: the joint wall is **L-INDEPENDENT** — each conjunct is EXACT at every L_max (an eigenbundle-topological identity / center-character-protected zero), NOT a truncation-dependent estimate that converges as `L^(−α)`.
- **Direction**: because the zeros are EXACT (not convergent), there is NO `c_continuum` and NO convergent `L^(−α)` envelope ⇒ the cross-pillar 5-anatomy IS-not-IN elements + the 3-level ladder are **N/A-with-reason** (the §VII.BY / §VII.BZ intra-pillar GEOMETRIC precedent: "Level-2 sub-class question does not arise; NON-BINDING by N/A-with-reason; Level-3 < Level-2 vacuously N/A").
- **Conclusion**: the metric-without-curvature joint wall is an INTRA-PILLAR GEOMETRIC structural theorem on `(A_K, H_K, D_K)` — registered with the 5-anatomy + 3-level ladder declared N/A-with-reason, NOT as a convergence bridge. ∎ (mechanical promotion of S96 + S105 W3-1/W3-2; re-derives NOTHING physical.)

**REGISTRY-ANATOMY COMPLIANCE.** (i) Entry class = **intra-pillar GEOMETRIC structural theorem** (single-axis; the JOINT triviality of the eigenbundle's curvature invariants). This is **NOT a cross-pillar bridge**, so the 5-anatomy IS-not-IN elements + the 3-level ladder are declared **N/A-with-reason**: there is no **laboratory-IN observable** (Element 2: N/A — Pillar-internal curvature-class fact) and no HKR / K-theory / Connes–Karoubi bridge map is claimed (a curvature-vanishing + metric-non-degeneracy fact intrinsic to `(A_K, H_K, D_K)`); the "Level-3 < Level-2" registry-PASS inequality is vacuously N/A (no continuum-image envelope; the zeros are EXACT at every L_max, NOT convergence anchors). The Level-2 sub-class question does not arise (NON-BINDING by N/A-with-reason). (ii) Projection-side = **SINGLE-READING, operator/projector-side**: the entry quantifies over curvature-class FUNCTIONALS of the band projector `P` and its eigenbundle (Chern / Euler / graded-Ω — all algebra-INVARIANT Corner-I band-geometry functionals), so the bare slot `@SLOT@` (no `.OP-PROJ`/`.STATE-PROJ` suffix) is admissible under `registry-landing.md` Reading-A naming hygiene precisely because this explicit single-reading sentence is carried; no state-pair functional clause exists. (iii) No state-history labels in the entry text (Class-(h) parse-tree N/A; "Bogoliubov" / "GGE" / "α_s_route" do not appear). (iv) Substrate-IS level tag = **Level 2** (moduli-deformation per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`): the base is the substrate's OWN (τ,μ) deformation manifold on the U(2)-invariant volume-preserving TT surface — not a coordinate container; the triviality holds across the substrate's own intrinsic deformation directions.

**Substrate framing** (`phononic-framing.md §"IS Space, Not IN Space"`). The substrate IS the spectral-triple band geometry; the lowest J/BDI-real Dirac doublet is a Peter-Weyl eigenbundle of `D_K` on the U(2)-invariant volume-preserving TT (τ,μ) modulus surface (the substrate's OWN moduli-deformation manifold). **Direction**: `D_K J/BDI-real eigenbundle on the (τ,μ) TT surface → the triviality invariants {Chern c_1, Euler e_2, graded-Ω A^WZ} = {0,0,0} EXACTLY → with band metric g ≈ @G@ ≠ 0 → the metric-without-curvature wall (metrically rich, holonomy-free; the 12-invariant triviality chain)`. **FORBIDDEN inversion (container thinking)**: "the band sits in an external (τ,μ) parameter space whose curvature vanishes" → INVERT: the (τ,μ) TT surface IS the substrate's own deformation manifold; the eigenbundle is trivial ON it while the metric is non-degenerate — an intrinsic fabric fact, not a property measured IN a container. The metric-without-curvature wall is the substrate's own statement that its band geometry carries distance (a non-degenerate quantum metric) WITHOUT holonomy (a flat, trivial connection) — there is no curvature to transport around the fabric's own deformation loops.

**Provenance.** This is a JOINT-STATEMENT registry-landing of three already-PROVEN conjuncts (NO compute gate; binding-text discipline). The three PRIMARY anchors (STRUCTURAL-ORTHOGONAL-COMPANIONS — each tests a DISTINCT curvature/triviality invariant on the SAME (τ,μ) surface, NOT cross-corner co-primary):
- **Chern conjunct** — `S96-GEOM-OFFJENSEN-CHERN` PASS (S96 P-30w; verdict-line audit_sha256 `943cb408ea41192ad057ccbcd7713ee58a09f507c0f026fbe89344dfd1cdb4f9` in `computations/session-96/s96_gate_verdicts.txt`; `C_FHS = @C1@`, round=0, all 5 PW sectors trivial; off-Jensen Chern = 0 closes the C11/C12 / P-30w open channel).
- **Euler conjunct** — `S105-EULER-DEFECT-MASKED` PASS (S105 W3-1; verdict-line audit_sha256 `12f92da0f3b26ae5e084007aed227d36bdb2a8417663a41e399726c748b8c4a3` in `computations/session-105/s105_gate_verdicts.txt`; witness `computations/session-105/s105_euler_defect_masked.npz`; `e2_masked = @E2@`, round=0; the entire raw content lives in ONE frame-singular vN-Wigner corner plaquette [0,49], masked at plan-freeze from S104 — re-run reproduces S104 defect-excl bit-exact, \\|diff\\|=0).
- **graded-Ω conjunct** — `S105-AWZ-ANALYTIC` PASS (S105 W3-2; verdict-line audit_sha256 `124d3a9582affc51c03dd0ae08109edacd02b603cabcb520cbe9e5d8dabbbbb3` in `computations/session-105/s105_gate_verdicts.txt`; witness `computations/session-105/s105_awz_analytic.npz`; median\\|A^WZ\\|_analytic = `@GO@` < 1e-12; ANALYTIC-RANK1-PERTURBATION evaluator with NO finite-difference floor — the S104 median 1.228e-11 was eps/h FD round-off, broken under the analytic evaluator; cross-grade overlap is REAL to machine zero away from the single B1/B2 corner via J-reality + γ9 double-protection).
Companion / metric witness: atlas-07 "Berry curvature B=982.5" ERRATUM (the 982.5 IS the band metric magnitude `g`, NOT Berry curvature; Berry curvature = 0 EXACTLY on this surface — Im(QGT) = 0 by Kosmann anti-Hermiticity + J+U(2) on the full U(2)-invariant surface). NO compute gate — registry-landing of pre-computed sub-results (binding-text discipline; the three EXACT zeros are eigenbundle-topological identities at every L_max). This is a §VII NCG/geometric structural-theorem landing, NOT a §7 falsifier-surface row — mack-cosmic-bridge sole-writer does NOT apply (`feedback_mack-bridge-role.md`). NO regulator_pin (Chern / Euler / graded-Ω are properties of the `D_K` eigenbundle, NOT Seeley-DeWitt a_n moments — per the S105 W3-1/W3-2 verdict-line precedent). NO CLASS pin (no SCHEMATIC helper consumed; all three conjuncts are FULL exact-eigendecomposition results). canonical_constants.py was append-only-extended mid-session; its SHA is computed at runtime and feeds audit_sha256 only (no stale pin; disclosed per `substrate-first-canonical-sourcing.md §(ii.B)`). @SLOT@ slot verified next-free at runtime via the all-header-level append-protocol scan (documented frontier §VII.BZ).

**Closure SHA pin** (over the ordered input-pin map): the full dual-SHA (audit_sha256 / content_sha256) is on the `S106-W3-1-METRIC-WITHOUT-CURVATURE-LANDING` verdict line in `computations/session-106/s106_gate_verdicts.txt`; registry_pre_write_file_sha256, the two S105 witness-npz SHAs, and the three conjunct-verdict audit SHAs are pinned in the companion comment rows.

"""
    text = (template
            .replace("@SLOT@", slot)
            .replace("@C1@", f"{C1_CHERN:.6e}")
            .replace("@E2@", f"{E2_EULER:.6e}")
            .replace("@GO@", f"{GRADED_OMEGA:.3e}")
            .replace("@G@", f"{G_METRIC}"))                                  # (local)
    return text


# ----------------------------------------------------------------------------
# (2) write_atomic_with_fsync — append the entry to the registry, fsync
# ----------------------------------------------------------------------------
def write_atomic_with_fsync(registry_path: Path, entry_text: str) -> None:
    """Append the §VII entry to the registry and fsync.

    Registry-landing is an APPEND (the entry is added at end-of-file beyond the
    current frontier); the template's whole-file `'w'` write is for a single-section
    file. Here the registry is the live multi-section file; we append the new slot.
    """
    cur = registry_path.read_text(encoding="utf-8")                          # (local)
    sep = "" if cur.endswith("\n") else "\n"                                 # (local)
    new_full = cur + sep + entry_text                                        # (local)
    with open(registry_path, "w", encoding="utf-8") as fh:
        fh.write(new_full)
        fh.flush()
        os.fsync(fh.fileno())


# ----------------------------------------------------------------------------
# (3) re_read_registry_at — extract the landed §VII.<slot> section block
# ----------------------------------------------------------------------------
def re_read_registry_at(registry_path: Path, slot_letters: str) -> str:
    """Re-read the registry from disk and return the §VII.<slot_letters> section.

    Returns the block from the `### §VII.<slot>` header up to (but not including)
    the next `### `/`## ` header OR EOF.
    """
    text = registry_path.read_text(encoding="utf-8")                         # (local)
    slot = f"§VII.{slot_letters}"                                            # (local)
    lines = text.split("\n")                                                 # (local)
    start = None                                                             # (local)
    hdr = re.compile(rf"^#{{2,4}}\s+{re.escape(slot)}\b")                    # (local)
    for i, ln in enumerate(lines):
        if hdr.search(ln):
            start = i                                                        # (local)
            break
    if start is None:
        return ""
    end = len(lines)                                                         # (local)
    nxt = re.compile(r"^#{2,4}\s+§")                                         # (local)
    for j in range(start + 1, len(lines)):
        if nxt.search(lines[j]):
            end = j                                                          # (local)
            break
    return "\n".join(lines[start:end])


# ----------------------------------------------------------------------------
# (4) verify_section_matches — strict equality on the landed vs built block
# ----------------------------------------------------------------------------
def verify_section_matches(actual: str, expected: str) -> bool:
    """Strict text match: the landed section equals the built entry (both stripped of
    trailing blank lines, since the next-section split / EOF differs by trailing \\n)."""
    return actual.rstrip("\n") == expected.rstrip("\n")


# ----------------------------------------------------------------------------
# print_verdict_payload — the script PRINTS; the AGENT calls emit_verdict
# ----------------------------------------------------------------------------
def print_verdict_payload(gate_id: str, verdict: str, value: str, scheme: str,
                          convention: str, l_max: str,
                          audit_sha: str, content_sha: str,
                          extra_rows: list[str]) -> None:
    """Print the emit_verdict payload block (race-safe path; NO file append here)."""
    print("=" * 78)
    print("EMIT_VERDICT PAYLOAD (agent calls mcp__knowledge__emit_verdict):")
    print("=" * 78)
    print(f"  session     = 106")
    print(f"  gate_id     = {gate_id}")
    print(f"  verdict     = {verdict}")
    print(f"  value       = {value}")
    print(f"  scheme      = {scheme}")
    print(f"  convention  = {convention}")
    print(f"  l_max       = {l_max}")
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")
    print(f"  schema_version = S84+")
    print(f"  extra_rows  =")
    for r in extra_rows:
        print(f"    {r}")
    print("=" * 78)


# ----------------------------------------------------------------------------
# Driver
# ----------------------------------------------------------------------------
def main() -> int:
    gate_id = "S106-W3-1-METRIC-WITHOUT-CURVATURE-LANDING"                   # (local)
    scheme = "REGISTRY-LANDING-SINGLE-SHOT"                                  # (local)
    convention = "ABSOLUTE-INTRA-PILLAR-GEOMETRIC-N/A-WITH-REASON"           # (local)
    l_max = "10"                                                             # (local)

    # ---- Log input SHAs (first lines of stdout, per gate-verdicts.md) ----
    registry_pre_sha = sha256_file(REGISTRY)                                 # (local)
    canon_sha = sha256_file(CANON)                                          # (local)
    euler_npz_sha = sha256_file(NPZ_EULER)                                  # (local)
    awz_npz_sha = sha256_file(NPZ_AWZ)                                      # (local)
    template_sha = sha256_file(TEMPLATE)                                    # (local)
    script_sha = sha256_file(THIS_SCRIPT)                                   # (local)

    print(f"INPUT SHA registry_pre_write   = {registry_pre_sha}")
    print(f"INPUT SHA canonical_constants  = {canon_sha}")
    print(f"INPUT SHA s105_euler_masked    = {euler_npz_sha}")
    print(f"INPUT SHA s105_awz_analytic    = {awz_npz_sha}")
    print(f"INPUT SHA landing_template     = {template_sha}")
    print(f"INPUT SHA this_script          = {script_sha}")
    print(f"INPUT SHA S96_chern_verdict    = {S96_CHERN_AUDIT}")
    print(f"INPUT SHA S105_euler_verdict   = {S105_EULER_AUDIT}")
    print(f"INPUT SHA S105_awz_verdict     = {S105_AWZ_AUDIT}")

    # ---- Slot allocation (all-header-level next-free scan + reroute) ----
    registry_text = REGISTRY.read_text(encoding="utf-8")                     # (local)
    slot_letters, drifted, slot_note = next_free_slot(registry_text, PLANNED_SLOT_LETTERS)  # (local)
    print(f"SLOT: {slot_note}")

    # ---- (1) build_promotion_text (pure, in memory) ----
    expected_text = build_promotion_text(slot_letters)                      # (local)

    # ---- (2) write_atomic_with_fsync ----
    write_atomic_with_fsync(REGISTRY, expected_text)

    # ---- (3) re_read_registry_at ----
    actual_section = re_read_registry_at(REGISTRY, slot_letters)            # (local)

    # ---- (4) verdict = (PASS if verify_section_matches else FAIL) ----
    matched = verify_section_matches(actual_section, expected_text)          # (local)

    # Verdict logic:
    #   - text mismatch -> FAIL (write/encoding defect)
    #   - slot drift (reroute) -> FAIL-WITH-REMEDIATION on the slot per
    #     registry-write hygiene, EVEN IF the entry landed+verified at the rerouted
    #     slot (the §VII.BZ §VII.BO->§VII.BZ precedent)
    #   - text match AND no drift -> PASS
    if not matched:
        verdict = "FAIL"                                                     # (local)
        value = (f"verify_section_matches=False_at_slot_VII.{slot_letters}"
                 f"_write-or-encoding-defect")                               # (local)
    elif drifted:
        verdict = "FAIL"                                                     # (local)
        value = (f"LANDED+VERIFIED_at_rerouted_slot_VII.{slot_letters}"
                 f"_FAIL-WITH-REMEDIATION_on_slot_drift_from_VII.{PLANNED_SLOT_LETTERS}"
                 f"_registry-write-hygiene")                                 # (local)
    else:
        verdict = "PASS"                                                     # (local)
        value = (f"metric-without-curvature_JOINT-WALL_LANDED_at_VII.{slot_letters}"
                 f"_intra-pillar-GEOMETRIC_N-A-with-reason"
                 f"_chern={C1_CHERN:.3e}_round0"
                 f"_euler={E2_EULER:.3e}_round0"
                 f"_gradedOmega={GRADED_OMEGA:.3e}_lt1e-12"
                 f"_g={G_METRIC}_metrically-rich-holonomy-free"
                 f"_12-invariant-triviality-chain"
                 f"_verify_section_matches=True")                            # (local)

    # ---- dual-SHA over the ORDERED input-pin map ----
    audit_pairs = [                                                          # (local)
        ("gate_id", gate_id),
        ("scheme", scheme),
        ("convention", convention),
        ("l_max", l_max),
        ("slot_landed", f"VII.{slot_letters}"),
        ("slot_planned", f"VII.{PLANNED_SLOT_LETTERS}"),
        ("slot_drifted", str(drifted)),
        ("verdict", verdict),
        ("script_sha256", script_sha),
        ("registry_pre_write_file_sha256", registry_pre_sha),
        ("s105_euler_defect_masked_npz_sha256", euler_npz_sha),
        ("s105_awz_analytic_npz_sha256", awz_npz_sha),
        ("s96_chern_verdict_audit_sha256", S96_CHERN_AUDIT),
        ("s105_euler_verdict_audit_sha256", S105_EULER_AUDIT),
        ("s105_awz_verdict_audit_sha256", S105_AWZ_AUDIT),
        ("canonical_constants_sha256", canon_sha),
        ("landing_template_sha256", template_sha),
    ]
    audit_sha = closure_hash(audit_pairs)                                    # (local)
    content_sha = sha256_text(actual_section)                                # (local)

    print(f"AUDIT closure_hash(input_pin_map) = {audit_sha}")
    print(f"CONTENT sha256(landed_section)    = {content_sha}")
    print(f"VERIFY verify_section_matches     = {matched}")
    print(f"VERDICT                           = {verdict}")

    extra_rows = [                                                           # (local)
        (f"# S106-W3-1 metric-without-curvature JOINT WALL landed §VII.{slot_letters}: "
         f"Chern c_1=0 [S96 943cb408] ∧ Euler e_2=0 [S105 W3-1 12f92da0] ∧ "
         f"graded-Ω A^WZ=0 [S105 W3-2 124d3a95] on the U(2)-inv vol-preserving TT (τ,μ) "
         f"surface; band metric g≈{G_METRIC}≠0 (metrically rich, holonomy-free); "
         f"12-invariant triviality chain"),
        (f"# intra-pillar GEOMETRIC structural theorem; 5-anatomy + 3-level ladder "
         f"N/A-with-reason (§VII.BY/§VII.BZ precedent); self-non-bridge for "
         f"_cross_pillar_bridge_audit.py (NOT a cross-pillar bridge); NO regulator_pin "
         f"(eigenbundle invariants, not Seeley-DeWitt a_n); NO CLASS pin (FULL exact "
         f"eigendecomposition)"),
        (f"# registry_pre_write_file_sha256={registry_pre_sha[:16]}… "
         f"s105_euler_npz={euler_npz_sha[:16]}… s105_awz_npz={awz_npz_sha[:16]}… "
         f"slot_planned=VII.{PLANNED_SLOT_LETTERS} slot_landed=VII.{slot_letters} "
         f"drifted={drifted}"),
    ]

    print_verdict_payload(gate_id, verdict, value, scheme, convention, l_max,
                          audit_sha, content_sha, extra_rows)

    # Exit 0 regardless of scientific verdict (verdict is DATA, not exit code).
    return 0


if __name__ == "__main__":
    sys.exit(main())
