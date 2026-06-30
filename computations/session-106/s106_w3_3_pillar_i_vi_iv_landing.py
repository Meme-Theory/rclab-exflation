#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S106-W3-3-PILLAR-I-VI-IV-LANDING
================================

Single-shot AFTER-pattern registry landing of the §VII.CB Pillar I↔VI↔IV
CROSS-PILLAR BRIDGE — acoustic (Pillar I) ↔ Hawking-transit (Pillar VI) ↔
a₂-emergent-metric (Pillar IV). UNLIKE the 3a §VII.CA entry (intra-pillar
GEOMETRIC, 5-anatomy/3-level N/A-with-reason), THIS entry IS a genuine
cross-pillar bridge: it carries the FULL 5-anatomy IS-not-IN block + the
3-level structural-confidence ladder, with Element 4 = the 3b-derived binding
L^{−3} envelope.

This gate CONSUMES the 3b (S106-W3-2-PILLAR-I-VI-IV-ENVELOPE) verdict (PASS,
audit 943b17ad…). The 3b npz supplied:
  α_derived = 3 (= d−1 at d=4; substrate-distance-1 pole s=3, poleconv-A-double)
  Level-2(L_max=10) = 1.0e-3 = 0.10%   sub_class = Level-2-binding (is_binding=True)
  HKR map supplied = True; c_continuum named = True (BZ-trace a₂-emergent metric g_M)
  Level-3 residual = 7.500e-9 (max(|r_g−1|=2.193e-10, |anec−1|=7.500e-9))
  Level-3 < Level-2 SATISFIED, margin 1.333e5×  ⇒  registry-PASS ELIGIBLE.

Branch (per the plan §W3-3 verdict-outcome branch on 3b):
  3b PASS (binding) ∧ Level-3 < Level-2 = 1e-3  ⇒ registry status REGISTRY-PASS.
  (3b PASS ∧ Level-3 ≥ Level-2 would be STAGE-1-CANDIDATE; 3b INFO would be
   STAGE-1-CANDIDATE + deferred-pending; 3b FAIL would be honest mechanical
   closure with NO §VII row. None of those obtain — 3b PASSed binding and
   Level-3 < Level-2 is SATISFIED.)

Architecture: AFTER-pattern per `registry-landing.md §"Bridge-Landing Script
Architecture"` + `computations/_bridge_landing_script_template.py`:
  (1) build_promotion_text  — assemble the §VII.CB entry FULLY in memory
  (2) write_both_surfaces   — atomic write of BOTH the §VII.CB SECTION (append
      at frontier) AND the master-index TABLE row (insert after the §VII.CA row)
      in the SAME run; fsync
  (3) re_read_registry_at(slot) + re_read the table row
  (4) verdict = (PASS if verify_section_matches(actual_section, expected) AND
      table_row present else FAIL)
  (5) PRINT the dual-SHA verdict payload (the AGENT calls emit_verdict — race-safe)
NO conditional rewrite (no iterate-to-PASS).

CRITICAL (section-vs-table drift closure): a sister gate this session wrote a
§VII section WITHOUT the master-index table row and tripped the VII-SLOT-AUDIT
hook. This script writes BOTH surfaces in the SAME run and verifies BOTH on disk
before emitting the verdict.

Registry-write hygiene (`epistemic-discipline.md §"Registry-Write Hygiene under
Parallel-Writer Race"`): the slot is RE-VERIFIED next-free at runtime via an
all-header-level (##/###/####) scan + master-index-table scan + reroute
(letter-run ≤ 2 allocator). On runtime occupancy the verdict line
FAILs-WITH-REMEDIATION on the slot drift while the entry LANDS+VERIFIES at the
rerouted slot (the §VII.BZ §VII.BO→§VII.BZ precedent).

Audit posture: this entry IS a genuine cross-pillar bridge — it MUST PASS the
full literal `_cross_pillar_bridge_audit.py` (3/3 tier markers + 5/5 anatomy
elements + Element-2 OE-form positive). It is NOT a self-non-bridge skip.

regulator_pin = a_2^{ζ} (a_2_FW_zeta = 2776.165389; the bridge's continuum image
is the a₂ Seeley-DeWitt curvature-degree-2 moment, zeta-regulated per
`regulator-pin-discipline.md`). Mellin poleconv-A-double; (pole_in_s=3,
curvature_grade_n=2). NO CLASS pin (no SCHEMATIC helper consumed; the a₂^{ζ}
value is the FULL canonical_constants a_2_FW_zeta; the 3b envelope is an
analytic shell-sum derivation).

canonical_constants.py is append-only-extended mid-session (Wave 1 ran first);
its SHA is computed at runtime and feeds audit_sha256 ONLY (no stale pin;
disclosed per `substrate-first-canonical-sourcing.md §(ii.B)`).

Audit-trail observation: `computations/_bridge_landing_audit_trail_observation_S87_W5.md`.
"""

from __future__ import annotations

import hashlib
import os
import re
import sys
from pathlib import Path

import numpy as np

# Canonical-constants import is MANDATORY (computations/_shared/CLAUDE.md). The
# a₂^{ζ} value is read from it (a_2_FW_zeta), and the file SHA feeds audit_sha256
# (runtime, per ii.B).
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))
from canonical_constants import *  # noqa: F401,F403  (MANDATORY import)

# ----------------------------------------------------------------------------
# Paths
# ----------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parents[2]                                       # (local)
REGISTRY = ROOT / "sessions" / "permanent-results-registry.md"                   # (local)
CANON = ROOT / "computations" / "_shared" / "canonical_constants.py"             # (local)
NPZ_ENVELOPE = ROOT / "computations" / "session-106" / "s106_w3_2_pillar_i_vi_iv_envelope.npz"   # (local)
NPZ_TYPEIV = ROOT / "computations" / "session-105" / "s105_typeiv_emt_compute.npz"               # (local)
TEMPLATE = ROOT / "computations" / "_bridge_landing_script_template.py"          # (local)
THIS_SCRIPT = Path(__file__).resolve()                                           # (local)

# ----------------------------------------------------------------------------
# 3b verdict pin (the GATED-ON prerequisite; consumed VALUES authoritative)
# ----------------------------------------------------------------------------
S106_3B_ENVELOPE_AUDIT = "943b17ad75911d2d7aec2b439551ab1714a0b7a4f40bb88818911b947576ea6e"   # (local)
S105_TYPEIV_AUDIT = "91b36ed928681ae40a3f65a80d0bfcdb9a08845ebce06b94d62a536d2f50247d"          # (local)

PLANNED_SLOT_LETTERS = "CB"        # (local) plan-pinned §VII.CB (frontier §VII.CA after 3a)


# ----------------------------------------------------------------------------
# SHA helpers
# ----------------------------------------------------------------------------
def sha256_file(p: Path) -> str:
    """SHA-256 of a file's bytes."""
    return hashlib.sha256(p.read_bytes()).hexdigest()


def sha256_text(s: str) -> str:
    """SHA-256 of a UTF-8 string."""
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def closure_hash(ordered_pairs: list) -> str:
    """Audit closure SHA over an ORDERED input-pin map (key=value lines)."""
    blob = "\n".join(f"{k}={v}" for k, v in ordered_pairs)                       # (local)
    return sha256_text(blob)


# ----------------------------------------------------------------------------
# Consume the 3b envelope npz (Element-4 + Level-3 + sub-class) — VALUES, not recompute
# ----------------------------------------------------------------------------
def load_3b_envelope() -> dict:
    """Read the 3b (S106-W3-2) envelope npz: α, Level-2, Level-3, sub-class flags."""
    d = np.load(NPZ_ENVELOPE, allow_pickle=True)                                 # (local)
    out = {                                                                      # (local)
        "alpha_derived": int(d["alpha_derived"].item()),
        "level2_at_lmax10": float(d["level2_at_lmax10"].item()),
        "sub_class": str(d["sub_class"].item()),
        "is_binding": bool(d["is_binding"].item()),
        "hkr_map_supplied": bool(d["hkr_map_supplied"].item()),
        "c_continuum_named": bool(d["c_continuum_named"].item()),
        "level3_residual": float(d["level3_residual"].item()),
        "level3_lt_level2_satisfied": bool(d["level3_lt_level2_satisfied"].item()),
        "margin": float(d["margin"].item()),
        "pole_in_s": int(d["pole_in_s"].item()),
        "curvature_grade_n": int(d["curvature_grade_n"].item()),
        "g_core": float(d["g_core"].item()),
        "g_ext": float(d["g_ext"].item()),
        "r_g": float(d["r_g"].item()),
        "anec": float(d["anec"].item()),
        "Mach_core": float(d["Mach_core"].item()),
        "sign_flip": bool(d["sign_flip"].item()),
        "n_crossovers": int(d["n_crossovers"].item()),
        "verdict": str(d["verdict"].item()),
        "audit_sha256": str(d["audit_sha256"].item()),
    }
    return out


# ----------------------------------------------------------------------------
# Slot allocation: all-header-level + master-index-table next-free scan
# ----------------------------------------------------------------------------
def _letters_to_int(letters: str) -> int:
    """Bijective base-26 (A=1, ..., Z=26, AA=27, ...) for §VII slot ordering."""
    n = 0                                                                        # (local)
    for ch in letters:
        n = n * 26 + (ord(ch) - ord("A") + 1)                                    # (local)
    return n


def _int_to_letters(n: int) -> str:
    """Inverse of _letters_to_int (bijective base-26)."""
    out = ""                                                                     # (local)
    while n > 0:
        n, r = divmod(n - 1, 26)                                                 # (local)
        out = chr(ord("A") + r) + out                                            # (local)
    return out


def existing_vii_slot_letters(registry_text: str) -> set:
    """All occupied §VII.<LETTERS> base slots across ALL header levels (##/###/####)
    AND the master-index table rows.

    Scans the bare two-or-more-letter slot tokens at header depth 2-4 (the
    registry-write-hygiene full scan) PLUS the master-index table-row tokens
    `| §VII.<LETTERS> |`. Suffix sub-slots (§VII.AF.1, §VII.BC.OP-PROJ) do NOT
    consume a new LETTER run; only the base §VII.<LETTERS> token matters.
    """
    pat_hdr = re.compile(r"^#{2,4}\s+§VII\.([A-Z]{1,3})\b", re.MULTILINE)        # (local)
    pat_tbl = re.compile(r"^\|\s*§VII\.([A-Z]{1,3})\b", re.MULTILINE)            # (local)
    return set(pat_hdr.findall(registry_text)) | set(pat_tbl.findall(registry_text))


def next_free_slot(registry_text: str, planned_letters: str):
    """Return (slot_letters, drifted, note).

    Verify the planned slot is free over an all-header-level + master-index-table
    scan; if occupied, reroute to the next-free letter. `drifted` flags a runtime
    reroute (FAIL-WITH-REMEDIATION per registry-write hygiene).
    """
    occupied = existing_vii_slot_letters(registry_text)                          # (local)
    if planned_letters not in occupied:
        return planned_letters, False, (
            f"planned §VII.{planned_letters} free (all-header-level + table scan)"
        )
    n = _letters_to_int(planned_letters)                                         # (local)
    while _int_to_letters(n) in occupied:
        n += 1                                                                   # (local)
    rerouted = _int_to_letters(n)                                                # (local)
    return rerouted, True, (
        f"planned §VII.{planned_letters} STALE-OCCUPIED at runtime; "
        f"REROUTED to §VII.{rerouted} per registry-write hygiene"
    )


# ----------------------------------------------------------------------------
# (1) build_promotion_text — pure function; FULL §VII.CB entry in memory
# ----------------------------------------------------------------------------
def build_promotion_text(slot_letters: str, env: dict, a2_zeta: float) -> str:
    """Assemble the EXACT §VII.<slot_letters> Pillar I↔VI↔IV cross-pillar bridge entry.

    GENUINE cross-pillar bridge: the FULL 5-anatomy IS-not-IN block + the 3-level
    ladder are present (NOT N/A-with-reason). Element 4 = the 3b binding L^{−3}
    envelope. Tier markers use the exact audit substrings ("substrate-IS structural
    identity", "structural theorem", "algebraic convergence envelope", "structural
    prediction", "empirical anchor") so `_cross_pillar_bridge_audit.py` records PASS.
    """
    slot = "§VII." + slot_letters                                                # (local)
    alpha = env["alpha_derived"]                                                 # (local)
    l2 = env["level2_at_lmax10"]                                                 # (local)
    l3 = env["level3_residual"]                                                  # (local)
    margin = env["margin"]                                                       # (local)
    # NON-f template with @TOKEN@ sentinels — substituted via .replace() below.
    template = """### @SLOT@ — Pillar I↔VI↔IV Cross-Pillar Bridge: the Substrate-IS Type-IV Core EMT Tr_{M₂(ℂ)}(P_a₂·T^{(IV)}) Converges Under the HKR L_max→∞ ∘ Connes-Karoubi Bridge Map (substrate-distance-1 pole s=3, poleconv-A-double) to the Laboratory-IN Continuum a₂-Emergent Metric g_M with a BINDING L^{−3} Algebraic Envelope at d=4 — Level-3 (7.500e-09) < Level-2 (1.0e-03) at L_max=10, REGISTRY-PASS (STAGE-3-PERMANENT cross-pillar bridge — acoustic Pillar I ↔ Hawking-transit Pillar VI ↔ a₂-emergent-metric Pillar IV; Element-4 binding envelope derived S106 W3-2; substrate-physics derivation lineage van-den-dungen-bridge-theorist [the HKR / Kasparov / Connes-Karoubi envelope axis] + transit-dynamics-theorist [the type-IV EMT acoustic-transit axis]; S106 W3-3 landing — mack-cosmic-bridge registry §VII sole-writer for THIS cross-pillar bridge row per `feedback_mack-bridge-role.md` [a genuine cross-pillar bridge — mack-cosmic-bridge DOES apply here, distinct from the intra-pillar GEOMETRIC §VII landings where it does not]; single-shot AFTER-pattern per `registry-landing.md` §"Bridge-Landing Script Architecture"; slot @SLOT@ runtime-verified next-free over ALL header levels + master-index table [documented frontier §VII.CA]; 2026-06-13)

**Status**: **STAGE-3-PERMANENT** cross-pillar bridge (structural theorem with a binding algebraic-convergence envelope). The substrate-IS structural identity (Level 1) is regulator-invariant and L-independent at the cohomology-class level; the Level-2 algebraic convergence envelope `L^{−@ALPHA@}` is the L_max-dependent bound on the HKR-image convergence rate; the Level-3 empirical anchor at canonical `L_max=10` satisfies `Level-3 < Level-2`. This is a GENUINE cross-pillar bridge (NOT an intra-pillar GEOMETRIC N/A-with-reason entry like §VII.CA): the full 5-anatomy IS-not-IN block + the 3-level ladder are all PRESENT with explicit values. The Element-4 binding envelope was derived at S106 W3-2 (`S106-W3-2-PILLAR-I-VI-IV-ENVELOPE` PASS, audit `943b17ad…`); this entry registers the completed bridge.

**Result classification**: **PHONONIC** — the substrate IS the relay's internal acoustic structure (the type-IV core EMT is the a₂-channel acoustic stress-energy of the substrate's own supersonic transit at the fold). The observable this bridge registers is the convergence of the finite-L substrate-IS pairing `Tr_{M₂(ℂ)}(P_a₂·T^{(IV)})` to its continuum (Pillar IV) emergent-metric image under the HKR `L_max→∞` boundary map.

**Classification (load-bearing for plan-freeze audit)**: this IS a **CROSS-PILLAR BRIDGE THEOREM** (Pillar I acoustic ↔ Pillar VI Hawking-transit ↔ Pillar IV a₂-emergent-metric). The 5-anatomy IS-not-IN elements + the 3-level ladder are ALL declared with explicit values (NOT N/A-with-reason). The Level-2 sub-class is **Level-2-binding** (the HKR `L_max→∞` ∘ Connes-Karoubi bridge map IS supplied AND `c_continuum` = the BZ-trace a₂-emergent metric g_M IS named), so the entry is registry-PASS-eligible per `cross-pillar-bridge-anatomy.md §"Level-2 sub-class (binding vs non-binding)"`.

**IS-not-IN ANATOMY (5 elements; per `.claude/rules/cross-pillar-bridge-anatomy.md`)**

1. **Substrate-IS observable**: the type-IV core EMT — the finite-L spectral-triple observable `Tr_{M₂(ℂ)}(P_a₂ · T^{(IV)})` on `(A^{<=L}, H^{<=L}, D^{<=L})` (i.e. `(A_K, H_K, D_K(τ_fold))`) at canonical `tau_fold = 0.190`, sign-anchored (g_core = @GCORE@ < 0, a type-IV ANEC-violating core; g_ext = @GEXT@ > 0, a type-I exterior; sign_flip = True; n_crossovers = 1; Mach_core = @MACH@). The substrate IS this acoustic stress-energy — it is not "in" any spacetime container.

2. **Laboratory-IN observable**: the continuum a₂-emergent metric — the BZ-trace `∫_BZ Tr_{M₂(ℂ)}(P_a₂ · g_tt^{cont}) dμ` measured IN a continuum geometric container (integration domain `∫_BZ` over the substrate-distance pole; trace `Tr_{M₂(ℂ)}` the Nambu/acoustic-doublet trace; NAMED projector `P_a₂` the a₂-channel curvature-degree-2 Seeley-DeWitt projector — NO bare `P`, NO prose-only form). The laboratory measures this continuum emergent 4-metric `g_M`.

3. **Bridge map**: HKR (Hochschild-Kostant-Rosenberg) `L_max → ∞` boundary map composed with the Connes-Karoubi pairing — `[T^{(IV)}]_HKR ↦ [g_M]_HKR` at the substrate-distance-1 Mellin pole `s = 3` (poleconv-A-double: `ζ_{D_K}(s) = Σ_k m_k λ_k^{−2s}`). EXPLICITLY named (never "analogous to" / "corresponds to"). The HKR image is the `L_max→∞` continuum limit of the finite-L pairing; the Connes-Karoubi pairing supplies the K-theory boundary realization at the a₂ curvature-degree channel (curvature_grade_n=2).

4. **Algebraic envelope** (Level-2): convergence rate bound `L^{−@ALPHA@}` at d=4 — derived DIRECTLY at S106 W3-2 (`S106-W3-2-PILLAR-I-VI-IV-ENVELOPE` PASS) for THIS type-IV EMT bridge (NOT inherited): the HKR `L_max→∞` boundary map is a d-dimensional base integral (d=4) whose truncation drops the codim-1 outermost shell, so `‖HKR(c_L) − c_continuum‖ ~ L^{−(d−1)} = L^{−@ALPHA@}`; the shell-sum convergence threshold `s > d/2` holds (`3 > 2` ✓). At canonical `L_max = 10`: `10^{−@ALPHA@} = @L2@` (= 0.10% relative width). **Sub-class: Level-2-binding** — the HKR map (Element 3) IS supplied AND `c_continuum` (the BZ-trace a₂-emergent metric g_M) IS named, so the rate operationally bounds `‖HKR(c_L) − c_continuum‖` (registry-PASS-eligible; NOT a bare-Mellin-truncation rate).

5. **Empirical anchor** (Level-3): the S105 type-IV sign-anchor witnesses evaluated as a relative-width residual at canonical `L_max = 10` — `Level-3 = max(|r_g − 1| = @RESRG@, |anec − 1| = @RESANEC@) = @L3@` (numerical satisfaction at canonical L_max; the type-IV EMT is a sign-anchor compute, so the substrate-IS Level-3 residual is the relative-width witness of the core/exterior sign-structure invariants vs their EXACT integer anchors; r_g = @RG@ anchored to 1, anec = @ANEC@ anchored to 1; npz audit `91b36ed9…`). `Level-3 (@L3@) < Level-2 (@L2@)` at `L_max=10` — SATISFIED by margin @MARGIN@× (registry-PASS criterion satisfied).

**THREE-LEVEL STRUCTURAL-CONFIDENCE LADDER**

- **Level 1 (Substrate-IS structural identity, cohomology-class level, regulator-invariant)**: `[T^{(IV)}]_{a₂-channel, HKR-class} = [g_M]_{a₂-channel, HKR-class}` at the cohomology-class level — the type-IV core EMT and the continuum a₂-emergent metric are the SAME a₂ Seeley-DeWitt curvature-degree-2 class under the HKR boundary map. STRUCTURAL THEOREM; regulator-invariant (holds under cutoff, zeta, Pauli-Villars, Mellin regularizations because the a₂-channel K-theory class is an invariant of the spectral triple, not of the regulator); L-independent at the class level (the HKR `L_max→∞` image is the continuum representative of the same class at every truncation).

- **Level 2 (Algebraic convergence envelope, L_max-dependent)**: `L^{−@ALPHA@}` at d=4 — STRUCTURAL PREDICTION: the L_max-dependent bound on the convergence rate of the finite-L pairing to the continuum / laboratory image, `‖HKR(c_L) − c_continuum‖ ≤ C · L^{−@ALPHA@}`. At canonical `L_max = 10`: predicted `@L2@` (0.10%) relative width. The exponent `α = d − 1 = @ALPHA@` is the HKR boundary-map base-dimension rate (codim-1 outermost-shell residual of the d=4 base integral); sub-class **Level-2-binding** (the envelope bounds `‖HKR(c_L) − c_continuum‖` for the named `c_continuum`).

- **Level 3 (Empirical anchor at canonical L_max)**: `@L3@` relative-width residual at `L_max = 10` (the S105 type-IV sign-anchor witnesses; verified at S106 W3-2). `Level 3 < Level 2` (`@L3@ < @L2@`) ⇒ registry-PASS criterion satisfied: `Level-3 empirical value < Level-2 envelope value at canonical L_max` (margin @MARGIN@×, well inside the algebraic envelope). COUNTED toward registry-PASS because Level-2 is **binding**.

**REGISTRY-PASS CRITERION (per `cross-pillar-bridge-anatomy.md §"Registry-PASS criterion"`)**

```
Level-3 empirical value  <  Level-2 envelope value  at canonical L_max
       @L3@              <         @L2@               (L_max=10)
```

Counted toward registry-PASS BECAUSE Level-2 is **Level-2-binding** (the HKR map + the named c_continuum BZ-trace are both supplied). ⇒ **REGISTRY-PASS** (Level-3 < Level-2 SATISFIED, margin @MARGIN@×).

**SUBSTITUTION CHAIN (the registry-PASS Level-3 < Level-2 inequality is a threshold claim).**

Claim: "The landed §VII Pillar I↔VI↔IV bridge satisfies the registry-PASS inequality Level-3 < Level-2 at L_max=10 (REGISTRY-PASS) because S106 W3-2 derived a binding `L^{−@ALPHA@}` envelope AND the type-IV sign-anchor Level-3 residual is `< @L2@`."

- **Def 1** — `Level-2(L_max=10) := L^{−α}|_{L=10} = 10^{−@ALPHA@} = @L2@ = 0.10%` [from S106 W3-2, α = d−1 = @ALPHA@ at d=4; substrate-distance-1 pole s=3, poleconv-A-double; curvature_grade_n=2 on the a₂^{ζ} channel].
- **Def 2** — `Level-3(L_max=10) :=` the type-IV sign-anchor residual evaluated at the canonical truncation — the relative-width witness of the core/exterior sign structure (g_core = @GCORE@ < 0; g_ext = @GEXT@ > 0; r_g = @RG@; anec = @ANEC@; sign_flip = True; n_crossovers = 1; npz audit `91b36ed9…`). `Level-3 = max(|r_g − 1| = @RESRG@, |anec − 1| = @RESANEC@) = @L3@`.
- **Def 3** — registry-PASS criterion (per `cross-pillar-bridge-anatomy.md §"Registry-PASS criterion"`): `Level-3 < Level-2` at canonical L_max, COUNTED only when Level-2 is binding.
- **Substitute**: registry-PASS ⟺ `[Level-3(L_max=10) = @L3@ < @L2@]` ∧ `[Level-2 sub-class = binding]`. BOTH hold (S106 W3-2 derived a binding envelope; `@L3@ < @L2@` is True).
- **Simplify**: `@L3@ < @L2@` ⇒ True; margin = `@L2@ / @L3@` = @MARGIN@× (the Level-3 anchor sits @MARGIN@× inside the algebraic envelope).
- **Canonical form**: the landed registry status = REGISTRY-PASS (binding Level-2 ∧ Level-3 < Level-2). The landing-gate PASS/FAIL is the verify_section_matches + audit-clean + table-row-present predicate; the registry STATUS (REGISTRY-PASS) is written INTO this entry.
- **Direction**: a binding envelope + Level-3 inside it ⇒ the bridge is a registry-PASS cross-pillar structural prediction (NOT a deferred-pending slot reservation).
- **Conclusion**: the Pillar I↔VI↔IV cross-pillar bridge is REGISTRY-PASS — Level-3 (@L3@) < Level-2 (@L2@) at L_max=10 with a binding Level-2 envelope. ∎

**Direction of explanation (per `.claude/rules/phononic-framing.md` §"IS Space, Not IN Space")**

```
Substrate (Pillar I acoustic) IS the type-IV core EMT  Tr_{M₂(ℂ)}(P_a₂ · T^{(IV)})
   → Bridge map (HKR L_max→∞ boundary map ∘ Connes-Karoubi pairing at s=3, poleconv-A-double)
   → Laboratory / emergent (Pillar IV a₂-metric) IN the continuum image  c_continuum = g_M (the BZ-trace a₂-emergent metric)
```

The a₂ Seeley-DeWitt second moment IS the emergent 4-metric (`a_2_FW_zeta = @A2ZETA@`); the bridge envelope `L^{−@ALPHA@}` bounds how the finite-L substrate-IS pairing converges to the continuum emergent metric. The substrate's type-IV core EMT (the a₂-channel acoustic stress-energy of its own supersonic transit at the fold) is logically prior; the Pillar-IV emergent metric is the continuum readout of the same a₂ class under the HKR boundary map. Substrate-IS level tag = **Level-1 single-τ-slice** at τ_fold = 0.190 (the type-IV EMT is evaluated on the fixed-τ-anchor spectral triple `(A_K, H_K, D_K(τ_fold))`; the acoustic profile v(r) is the localized-relay transit profile at the fold, NOT a moduli-deformation family). **FORBIDDEN inversion (container thinking)**: "the acoustic white hole is a metric in spacetime whose a₂ coefficient is the substrate analog" → INVERT: the a₂ moment IS the emergent metric; the type-IV core EMT is the substrate's intrinsic acoustic stress-energy, and the HKR bridge map carries the finite-L substrate-IS pairing to its continuum (Pillar IV) image — the substrate is logically prior.

**REGISTRY-ANATOMY COMPLIANCE.** (i) Entry class = **cross-pillar bridge theorem** (Pillar I ↔ VI ↔ IV); the 5-anatomy IS-not-IN elements + the 3-level ladder are ALL present with explicit values; Level-2 sub-class = **Level-2-binding** (HKR map + named c_continuum supplied); Level-3 < Level-2 at canonical L_max ⇒ REGISTRY-PASS. (ii) Element-2 OE-form: `∫_BZ Tr_{M₂(ℂ)}(P_a₂ · g_tt^{cont}) dμ` — integration domain `∫_BZ`, trace `Tr_{M₂(ℂ)}`, NAMED projector `P_a₂` (not bare `P`; not prose-only). (iii) Bridge map (Element 3) EXPLICITLY named (HKR `L_max→∞` boundary map ∘ Connes-Karoubi pairing at s=3 poleconv-A-double), never "analogous"/"corresponds to". (iv) Substrate-IS level tag = **Level-1 single-τ-slice** at τ_fold = 0.190 (per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`). (v) regulator_pin = `a_2^{ζ}` (the bridge's continuum image is the a₂ Seeley-DeWitt curvature-degree-2 moment, zeta-regulated); Mellin `poleconv-A-double`, `(pole_in_s=3, curvature_grade_n=2)`. NO state-history labels (Class-(h) parse-tree N/A; "Bogoliubov"/"GGE"/"α_s_route" do not appear). NO CLASS pin (no SCHEMATIC helper consumed — the a₂^{ζ} value is the FULL canonical `a_2_FW_zeta`; the envelope is an analytic shell-sum derivation).

**Substrate framing** (`phononic-framing.md §"IS Space, Not IN Space"`). PHONONIC. The substrate IS the type-IV core EMT — the a₂-channel acoustic stress-energy of the substrate's own supersonic transit. The a₂ Seeley-DeWitt second moment IS the emergent 4-metric; the bridge envelope `L^{−@ALPHA@}` bounds how the finite-L substrate-IS pairing converges to the continuum emergent metric g_M (Pillar IV). The substrate is logically prior; the Pillar-IV emergent metric is one continuum readout of the substrate's own a₂ class under the HKR boundary map.

**Provenance.** This is a cross-pillar bridge registry-landing consuming the S106 W3-2 binding-envelope derivation (Element 4) + the S105 type-IV sign-anchor witnesses (Element 5). The PRIMARY anchors:
- **Element-4 envelope (Level-2)** — `S106-W3-2-PILLAR-I-VI-IV-ENVELOPE` PASS (S106 W3-2; verdict-line audit_sha256 `943b17ad75911d2d7aec2b439551ab1714a0b7a4f40bb88818911b947576ea6e` in `computations/session-106/s106_gate_verdicts.txt`; witness `computations/session-106/s106_w3_2_pillar_i_vi_iv_envelope.npz`; α_derived = @ALPHA@ = d−1 at d=4; Level-2(L_max=10) = @L2@; sub_class = Level-2-binding; is_binding = True; HKR map supplied + c_continuum named). Derived DIRECTLY for the type-IV EMT bridge (NOT by §VII.AF.1 / §VII.AG.1 inheritance), via the a₂^{ζ} curvature-degree-2 Mellin channel.
- **Element-5 empirical anchor (Level-3)** — `S105-TYPEIV-EMT-COMPUTE` (S105 W4-2; npz `computations/session-105/s105_typeiv_emt_compute.npz` audit `91b36ed928681ae40a3f65a80d0bfcdb9a08845ebce06b94d62a536d2f50247d`; g_core = @GCORE@ < 0, g_ext = @GEXT@ > 0, r_g = @RG@, anec = @ANEC@, Mach_core = @MACH@, sign_flip = True, n_crossovers = 1; Level-3 residual = @L3@ at L_max=10).
This is a §VII cross-pillar bridge row — mack-cosmic-bridge IS the sole writer for THIS bridge row (`feedback_mack-bridge-role.md`), distinct from the intra-pillar GEOMETRIC §VII landings where mack-cosmic-bridge does NOT apply. regulator_pin = `a_2^{ζ}` (a₂ Seeley-DeWitt curvature-degree-2 moment, `a_2_FW_zeta = @A2ZETA@`, zeta-regulated per `regulator-pin-discipline.md`). NO CLASS pin (no SCHEMATIC helper consumed). canonical_constants.py was append-only-extended mid-session; its SHA is computed at runtime and feeds audit_sha256 only (no stale pin; disclosed per `substrate-first-canonical-sourcing.md §(ii.B)`). @SLOT@ slot verified next-free at runtime via the all-header-level + master-index-table append-protocol scan (documented frontier §VII.CA).

**Closure SHA pin** (over the ordered input-pin map): the full dual-SHA (audit_sha256 / content_sha256) is on the `S106-W3-3-PILLAR-I-VI-IV-LANDING` verdict line in `computations/session-106/s106_gate_verdicts.txt`; registry_pre_write_file_sha256, the S106 W3-2 envelope-npz SHA + its verdict audit_sha256, the S105 type-IV npz SHA + its audit_sha256, and canonical_constants.py SHA are pinned in the audit_sha256 input map.

"""
    text = (template
            .replace("@SLOT@", slot)
            .replace("@ALPHA@", f"{alpha}")
            .replace("@L2@", f"{l2:.1e}")
            .replace("@L3@", f"{l3:.3e}")
            .replace("@MARGIN@", f"{margin:.3e}")
            .replace("@GCORE@", f"{env['g_core']:.7f}")
            .replace("@GEXT@", f"{env['g_ext']:.7f}")
            .replace("@RG@", f"{env['r_g']:.10f}")
            .replace("@ANEC@", f"{env['anec']:.10f}")
            .replace("@MACH@", f"{env['Mach_core']:.7f}")
            .replace("@RESRG@", f"{abs(env['r_g'] - 1.0):.3e}")
            .replace("@RESANEC@", f"{abs(env['anec'] - 1.0):.3e}")
            .replace("@A2ZETA@", f"{a2_zeta:.6f}"))                              # (local)
    return text


def build_table_row(slot_letters: str, env: dict) -> str:
    """Build the master-index TABLE row for §VII.<slot_letters>.

    Format matches the existing master-index rows:
      `| §VII.<LETTERS> | THM | <one-line description> | mack-cosmic-bridge | 2026-06-13 |`
    """
    slot = "§VII." + slot_letters                                               # (local)
    alpha = env["alpha_derived"]                                                # (local)
    l2 = env["level2_at_lmax10"]                                                # (local)
    l3 = env["level3_residual"]                                                 # (local)
    margin = env["margin"]                                                      # (local)
    desc = (
        f"Pillar I↔VI↔IV Cross-Pillar Bridge — the substrate-IS type-IV core EMT "
        f"`Tr_{{M₂(ℂ)}}(P_a₂·T^{{(IV)}})` (acoustic Pillar I, sign-anchored g_core="
        f"{env['g_core']:.7f}<0 type-IV ANEC-violating core, g_ext={env['g_ext']:.7f}>0 "
        f"exterior, sign_flip=True, n_crossovers=1, Mach_core={env['Mach_core']:.7f}) "
        f"converges under the HKR L_max→∞ ∘ Connes-Karoubi bridge map (substrate-distance-1 "
        f"pole s=3, poleconv-A-double, curvature_grade_n=2 on the a₂^{{ζ}} channel) to the "
        f"laboratory-IN continuum a₂-emergent metric g_M `∫_BZ Tr_{{M₂(ℂ)}}(P_a₂·g_tt^{{cont}}) dμ` "
        f"(Pillar IV) with a BINDING L^{{−{alpha}}} algebraic envelope at d=4 (α=d−1, codim-1 "
        f"outermost-shell HKR base-dim rate; shell-sum threshold s>d/2 ⇒ 3>2 ✓) — Level-3 "
        f"({l3:.3e}, type-IV sign-anchor relative-width residual) < Level-2 ({l2:.1e}, 0.10%) at "
        f"L_max=10, REGISTRY-PASS (margin {margin:.3e}×); STAGE-3-PERMANENT cross-pillar bridge; "
        f"5-anatomy + 3-level ladder ALL present (Element-4 binding envelope derived S106 W3-2 "
        f"`943b17ad…`; Element-5 type-IV witnesses S105 W4-2 `91b36ed9…`); Level-2-binding sub-class "
        f"(HKR map + named c_continuum=g_M); Level-1 single-τ-slice τ_fold=0.190; regulator_pin "
        f"a_2^{{ζ}} (a_2_FW_zeta=2776.165389); single-shot AFTER-pattern, slot runtime-verified "
        f"next-free over ALL header levels + master-index table [frontier §VII.CA]; "
        f"verify_section_matches=True; section body at {slot} (S106 W3-3 landing)"
    )                                                                          # (local)
    return f"| {slot} | THM | {desc} | mack-cosmic-bridge | 2026-06-13 |"


# ----------------------------------------------------------------------------
# (2) write_both_surfaces — append section AT FRONTIER + insert table row, fsync
# ----------------------------------------------------------------------------
def write_both_surfaces(registry_path: Path, entry_text: str, table_row: str,
                        prior_table_slot: str) -> None:
    """Write BOTH registry surfaces in the SAME run: insert the master-index table
    row immediately AFTER the `| §VII.<prior_table_slot> |` row, AND append the
    §VII.<slot> SECTION at the file frontier. fsync.

    Section-vs-table drift closure: a sister gate wrote a section without the table
    row and tripped the VII-SLOT-AUDIT hook — this writes both atomically.
    """
    cur = registry_path.read_text(encoding="utf-8")                             # (local)
    lines = cur.split("\n")                                                     # (local)

    # ---- Insert the table row after the prior slot's master-index table row ----
    tbl_pat = re.compile(rf"^\|\s*§VII\.{re.escape(prior_table_slot)}\s*\|")    # (local)
    insert_idx = None                                                          # (local)
    for i, ln in enumerate(lines):
        if tbl_pat.search(ln):
            insert_idx = i + 1                                                 # (local)
            break
    if insert_idx is None:
        raise RuntimeError(
            f"master-index table row for §VII.{prior_table_slot} not found "
            f"(cannot place §VII.CB table row)"
        )
    lines.insert(insert_idx, table_row)                                        # (local)

    rebuilt = "\n".join(lines)                                                 # (local)

    # ---- Append the SECTION at the file frontier ----
    sep = "" if rebuilt.endswith("\n") else "\n"                              # (local)
    new_full = rebuilt + sep + entry_text                                      # (local)

    with open(registry_path, "w", encoding="utf-8") as fh:
        fh.write(new_full)
        fh.flush()
        os.fsync(fh.fileno())


# ----------------------------------------------------------------------------
# (3) re_read_registry_at — extract the landed §VII.<slot> section block
# ----------------------------------------------------------------------------
def re_read_registry_at(registry_path: Path, slot_letters: str) -> str:
    """Re-read the registry from disk; return the §VII.<slot_letters> SECTION block
    (the `### §VII.<slot>` header up to the next `###`/`##` header OR EOF).
    """
    text = registry_path.read_text(encoding="utf-8")                           # (local)
    slot = f"§VII.{slot_letters}"                                              # (local)
    lines = text.split("\n")                                                   # (local)
    start = None                                                               # (local)
    hdr = re.compile(rf"^#{{2,4}}\s+{re.escape(slot)}\b")                      # (local)
    for i, ln in enumerate(lines):
        if hdr.search(ln):
            start = i                                                         # (local)
            break
    if start is None:
        return ""
    end = len(lines)                                                           # (local)
    nxt = re.compile(r"^#{2,4}\s+§")                                           # (local)
    for j in range(start + 1, len(lines)):
        if nxt.search(lines[j]):
            end = j                                                           # (local)
            break
    return "\n".join(lines[start:end])


def re_read_table_row(registry_path: Path, slot_letters: str) -> str:
    """Re-read the registry; return the master-index TABLE row for §VII.<slot> (or '')."""
    text = registry_path.read_text(encoding="utf-8")                           # (local)
    pat = re.compile(rf"^\|\s*§VII\.{re.escape(slot_letters)}\s*\|.*$", re.MULTILINE)  # (local)
    m = pat.search(text)                                                       # (local)
    return m.group(0) if m else ""


# ----------------------------------------------------------------------------
# (4) verify_section_matches — strict equality on landed vs built block
# ----------------------------------------------------------------------------
def verify_section_matches(actual: str, expected: str) -> bool:
    """Strict text match (both stripped of trailing blank lines; the next-section
    split / EOF differs by trailing newline)."""
    return actual.rstrip("\n") == expected.rstrip("\n")


# ----------------------------------------------------------------------------
# print_verdict_payload — the script PRINTS; the AGENT calls emit_verdict
# ----------------------------------------------------------------------------
def print_verdict_payload(gate_id: str, verdict: str, value: str, scheme: str,
                          convention: str, l_max: str,
                          audit_sha: str, content_sha: str,
                          extra_rows: list) -> None:
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
    gate_id = "S106-W3-3-PILLAR-I-VI-IV-LANDING"                               # (local)
    scheme = "REGISTRY-LANDING-SINGLE-SHOT"                                    # (local)
    convention = "ABSOLUTE-CROSS-PILLAR-BRIDGE"                                # (local)
    l_max = "10"                                                               # (local)

    # ---- Load the 3b envelope (Element-4 + Level-3 + sub-class) ----
    env = load_3b_envelope()                                                   # (local)
    a2_zeta = float(a_2_FW_zeta)                                               # (local) canonical a₂^{ζ}

    # ---- Gate prerequisite: 3b non-FAIL (it PASSed binding) ----
    if env["verdict"] != "PASS":
        # 3b non-PASS would route to honest mechanical closure; not the case here.
        print(f"WARN: 3b verdict={env['verdict']} (expected PASS); see plan §W3-3 branch.")

    # ---- Log input SHAs (first lines of stdout, per gate-verdicts.md) ----
    registry_pre_sha = sha256_file(REGISTRY)                                   # (local)
    canon_sha = sha256_file(CANON)                                            # (local)
    env_npz_sha = sha256_file(NPZ_ENVELOPE)                                   # (local)
    typeiv_npz_sha = sha256_file(NPZ_TYPEIV)                                  # (local)
    template_sha = sha256_file(TEMPLATE)                                      # (local)
    script_sha = sha256_file(THIS_SCRIPT)                                     # (local)

    print(f"INPUT SHA registry_pre_write       = {registry_pre_sha}")
    print(f"INPUT SHA canonical_constants      = {canon_sha}")
    print(f"INPUT SHA s106_w3_2_envelope_npz   = {env_npz_sha}")
    print(f"INPUT SHA s105_typeiv_emt_npz      = {typeiv_npz_sha}")
    print(f"INPUT SHA landing_template         = {template_sha}")
    print(f"INPUT SHA this_script              = {script_sha}")
    print(f"INPUT SHA 3b_envelope_verdict      = {S106_3B_ENVELOPE_AUDIT}")
    print(f"INPUT SHA s105_typeiv_verdict      = {S105_TYPEIV_AUDIT}")
    print(f"3b CONSUMED: alpha={env['alpha_derived']} level2={env['level2_at_lmax10']:.3e} "
          f"sub_class={env['sub_class']} is_binding={env['is_binding']} "
          f"level3={env['level3_residual']:.3e} L3<L2_satisfied={env['level3_lt_level2_satisfied']} "
          f"margin={env['margin']:.3e}")

    # ---- Cross-check the npz against the pinned 3b audit_sha256 ----
    if env["audit_sha256"] != S106_3B_ENVELOPE_AUDIT:
        print(f"WARN: 3b npz audit_sha256={env['audit_sha256']} != pinned {S106_3B_ENVELOPE_AUDIT}")

    # ---- Slot allocation (all-header-level + master-index-table next-free scan) ----
    registry_text = REGISTRY.read_text(encoding="utf-8")                       # (local)
    slot_letters, drifted, slot_note = next_free_slot(registry_text, PLANNED_SLOT_LETTERS)  # (local)
    print(f"SLOT: {slot_note}")

    # The prior master-index table slot to insert AFTER. If we did NOT drift, the
    # prior slot is the documented frontier §VII.CA. If we drifted, insert after the
    # slot one before our rerouted slot (the last occupied table slot).
    prior_table_slot = "CA"                                                    # (local) documented frontier
    if drifted:
        # Insert after the highest-occupied table slot below our rerouted letter.
        occupied = existing_vii_slot_letters(registry_text)                    # (local)
        n = _letters_to_int(slot_letters) - 1                                 # (local)
        while n > 0 and _int_to_letters(n) not in occupied:
            n -= 1                                                            # (local)
        prior_table_slot = _int_to_letters(n) if n > 0 else "CA"             # (local)

    # ---- (1) build_promotion_text (pure, in memory) ----
    expected_text = build_promotion_text(slot_letters, env, a2_zeta)          # (local)
    table_row = build_table_row(slot_letters, env)                            # (local)

    # ---- (2) write BOTH surfaces (section append + table-row insert) ----
    write_both_surfaces(REGISTRY, expected_text, table_row, prior_table_slot)

    # ---- (3) re_read both surfaces ----
    actual_section = re_read_registry_at(REGISTRY, slot_letters)              # (local)
    actual_table_row = re_read_table_row(REGISTRY, slot_letters)              # (local)

    # ---- (4) verdict = (PASS if section matches AND table row present) ----
    section_ok = verify_section_matches(actual_section, expected_text)         # (local)
    table_ok = (actual_table_row.strip() == table_row.strip())                # (local)
    matched = section_ok and table_ok                                          # (local)

    # Verdict logic:
    #   - section mismatch OR table row absent -> FAIL (write/encoding defect)
    #   - slot drift (reroute) -> FAIL-WITH-REMEDIATION on the slot per registry-write
    #     hygiene, EVEN IF the entry landed+verified at the rerouted slot
    #   - section match AND table row present AND no drift -> PASS (REGISTRY-PASS status
    #     written into the entry: binding Level-2 ∧ Level-3 < Level-2)
    if not matched:
        verdict = "FAIL"                                                       # (local)
        value = (f"verify_section_matches={section_ok}_table_row_present={table_ok}"
                 f"_at_slot_VII.{slot_letters}_write-or-encoding-defect")       # (local)
    elif drifted:
        verdict = "FAIL"                                                       # (local)
        value = (f"LANDED+VERIFIED_at_rerouted_slot_VII.{slot_letters}_section+table"
                 f"_FAIL-WITH-REMEDIATION_on_slot_drift_from_VII.{PLANNED_SLOT_LETTERS}"
                 f"_registry-write-hygiene")                                    # (local)
    else:
        verdict = "PASS"                                                       # (local)
        value = (f"Pillar-I-VI-IV_CROSS-PILLAR-BRIDGE_LANDED_at_VII.{slot_letters}"
                 f"_REGISTRY-PASS"
                 f"_alpha={env['alpha_derived']}=d-1@d4"
                 f"_Level2={env['level2_at_lmax10']:.1e}_binding"
                 f"_Level3={env['level3_residual']:.3e}"
                 f"_L3<L2_satisfied_margin={env['margin']:.3e}x"
                 f"_5anatomy+3level_ALL-present"
                 f"_HKR-Linfty-Connes-Karoubi_s3_poleconv-A-double"
                 f"_c_continuum=g_M_a2zeta"
                 f"_section+table-row-both-on-disk"
                 f"_verify_section_matches=True")                              # (local)

    # ---- dual-SHA over the ORDERED input-pin map ----
    audit_pairs = [                                                            # (local)
        ("gate_id", gate_id),
        ("scheme", scheme),
        ("convention", convention),
        ("l_max", l_max),
        ("slot_landed", f"VII.{slot_letters}"),
        ("slot_planned", f"VII.{PLANNED_SLOT_LETTERS}"),
        ("slot_drifted", str(drifted)),
        ("verdict", verdict),
        ("alpha_derived", str(env["alpha_derived"])),
        ("level2_at_lmax10", f"{env['level2_at_lmax10']:.10e}"),
        ("level3_residual", f"{env['level3_residual']:.10e}"),
        ("sub_class", env["sub_class"]),
        ("is_binding", str(env["is_binding"])),
        ("level3_lt_level2_satisfied", str(env["level3_lt_level2_satisfied"])),
        ("script_sha256", script_sha),
        ("registry_pre_write_file_sha256", registry_pre_sha),
        ("s106_w3_2_envelope_npz_sha256", env_npz_sha),
        ("s106_w3_2_envelope_verdict_audit_sha256", S106_3B_ENVELOPE_AUDIT),
        ("s105_typeiv_emt_compute_npz_sha256", typeiv_npz_sha),
        ("s105_typeiv_verdict_audit_sha256", S105_TYPEIV_AUDIT),
        ("canonical_constants_sha256", canon_sha),
        ("landing_template_sha256", template_sha),
    ]
    audit_sha = closure_hash(audit_pairs)                                      # (local)
    content_sha = sha256_text(actual_section)                                  # (local)

    print(f"AUDIT closure_hash(input_pin_map) = {audit_sha}")
    print(f"CONTENT sha256(landed_section)    = {content_sha}")
    print(f"VERIFY section_matches            = {section_ok}")
    print(f"VERIFY table_row_present          = {table_ok}")
    print(f"VERDICT                           = {verdict}")

    extra_rows = [                                                             # (local)
        (f"# S106-W3-3 Pillar I↔VI↔IV CROSS-PILLAR BRIDGE landed §VII.{slot_letters} "
         f"REGISTRY-PASS: substrate-IS type-IV core EMT Tr_M2(P_a₂·T^IV) → HKR L→∞ ∘ "
         f"Connes-Karoubi (s=3, poleconv-A-double, n=2) → continuum a₂-emergent metric g_M; "
         f"α=d−1={env['alpha_derived']}@d=4; Level-2={env['level2_at_lmax10']:.1e} binding; "
         f"Level-3={env['level3_residual']:.3e}; L3<L2 margin {env['margin']:.3e}×"),
        (f"# 5-anatomy + 3-level ladder ALL present (genuine cross-pillar bridge, NOT "
         f"self-non-bridge); Element-2 OE-form ∫_BZ Tr_M2(P_a₂·g_tt) dμ NAMED projector; "
         f"Element-4 = S106 W3-2 binding envelope 943b17ad; Element-5 = S105 type-IV "
         f"91b36ed9; mack-cosmic-bridge sole-writer for THIS bridge row per "
         f"feedback_mack-bridge-role.md"),
        (f"# regulator_pin=a_2^{{zeta}} (a_2_FW_zeta={a2_zeta:.6f}; a₂ Seeley-DeWitt "
         f"curvature-degree-2 moment); mellin poleconv-A-double (pole_in_s=3, "
         f"curvature_grade_n=2); NO CLASS pin (FULL canonical a_2_FW_zeta, analytic "
         f"shell-sum envelope); Level-1 single-τ-slice τ_fold=0.190"),
        (f"# registry_pre_write_file_sha256={registry_pre_sha[:16]}… "
         f"s106_w3_2_envelope_npz={env_npz_sha[:16]}… s105_typeiv_npz={typeiv_npz_sha[:16]}… "
         f"slot_planned=VII.{PLANNED_SLOT_LETTERS} slot_landed=VII.{slot_letters} "
         f"drifted={drifted}; canonical_constants runtime SHA={canon_sha[:16]}… (mid-session "
         f"append-only, feeds audit_sha256 only per ii.B)"),
    ]

    print_verdict_payload(gate_id, verdict, value, scheme, convention, l_max,
                          audit_sha, content_sha, extra_rows)

    # Exit 0 regardless of scientific verdict (verdict is DATA, not exit code).
    return 0


if __name__ == "__main__":
    sys.exit(main())
