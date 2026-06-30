#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S111-CF-M1-INTERTWINER registry landing (single-shot AFTER-pattern).
===================================================================
Lands the OBSTRUCT-PASS two-conjunct categorical obstruction theorem as a
STAGE-1-CANDIDATE registry entry in sessions/permanent-results-registry.md:
  - master-index TABLE ROW (after the §VII.CH row)
  - SECTION BODY (### §VII.CI, appended after the last §VII section)
both written in ONE run (the two-surface discipline; spawn-prompt requirement).

Single-shot AFTER-pattern per registry-landing.md §"Bridge-Landing Script
Architecture":
   build_promotion_text -> write_atomic_with_fsync -> re_read + verify -> emit ONE

Slot §VII.CI is runtime-verified next-free over ALL header levels (## / ### / ####
+ master-index | §VII.CI | rows) BEFORE writing, per registry-landing.md
§"Registry-Write Hygiene under Parallel-Writer Race" item 1 (scan ALL header
levels) and cross-pillar-bridge-anatomy.md slot-allocation discipline.

This is NOT a cross-pillar bridge (no laboratory-IN observable, no L^{-alpha}
envelope): it is an INTRA-NCG categorical / K-homology structural theorem, so the
5-anatomy IS-not-IN elements are N/A-with-reason (exactly as §VII.CH NOHOLOFLUX
declares for its intra-quantization-framework definitional theorem). The verdict
line for THIS landing is the closure SHA over the (registry-file, section-text,
master-row) it writes.
"""

import os
import re
import sys
import json
import hashlib
import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))

# Canonical-constants compliance import (MANDATORY S34+).  This registry-landing
# script is pure markdown bookkeeping (it writes a §VII.CI registry entry); it
# consumes NO framework numerical constant (no eigenvalue / moment / M_KK / tau).
# The import is the compliance anchor per computations/_shared/CLAUDE.md.
sys.path.insert(0, os.path.join(HERE, "..", "_shared"))
from canonical_constants import *  # noqa: F401,F403  (compliance import; no constant used)
REGISTRY = os.path.join(ROOT, "sessions", "permanent-results-registry.md")

SLOT = "§VII.CI"
GATE_ID = "S111-CF-M1-INTERTWINER-REGLAND"  # distinct gate-id for the landing closure
DATE = "2026-06-21"


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha256_text(s):
    return sha256_bytes(s.encode("utf-8"))


# ----------------------------------------------------------------------------------
# 1) Runtime next-free verification over ALL header levels + master-index rows.
# ----------------------------------------------------------------------------------
def verify_slot_free(text, slot):
    """Return True iff `slot` does NOT already appear as a header or master-index row."""
    # Any §VII.CI occurrence at all (header ## / ### / #### OR master-index | row |)
    # would be a collision.  We scan the WHOLE file (the strictest test).
    pat = re.compile(re.escape(slot) + r"\b")
    hits = pat.findall(text)
    return (len(hits) == 0), len(hits)


# ----------------------------------------------------------------------------------
# 2) Build promotion text (master-index ROW + section BODY) fully in memory.
# ----------------------------------------------------------------------------------
def build_master_index_row():
    desc = (
        "Categorical Two-Conjunct Obstruction Theorem for the χ Inheritance Morphism — "
        "the inheritance morphism χ : A_K = ℂ⊕ℍ⊕M_3(ℂ) → M_2(ℂ) (M_3(ℂ)→0) is the "
        "Connes-Karoubi DELETION, NOT the Kasparov shriek π_!^{CP²} of SU(3)→CP², for "
        "ALL constructions/bridges — the S110 W1 two-decidable-axes obstruction "
        "(ONE bridge ι_*∘HKR + ONE construction ACM) lifted to the CATEGORICAL all-X "
        "statement on TWO complementary conjuncts: CONJUNCT (i) [Axis-2, C*-algebra-type, "
        "van-den-dungen] no homomorphism-type construction realizes the Wedderburn quotient "
        "A_K→A_K/M_3(ℂ) as a fibre-integration (codomain-rank: ρ|_{M_3}=0 FORCED for every "
        "*-hom into M_2(ℂ) since C² carries no M_3-irrep, exhaustive over the two C²-decomps "
        "{2·ℂ, 1·ℍ}; Skolem-Noether block-rigidity: the only summand-removing morphism is the "
        "quotient = DELETION, not a fibre-integration which RETAINS its fibre Paper 01 Thm 3.4); "
        "CONJUNCT (ii) [Axis-1, K-homology, connes] all K-natural bridge maps send the "
        "M_3-generator of K^0(A_K)=ℤ³ → (0,0,0) (Morita-index-rigidity: g_3 is a homotopy "
        "invariant pinned once at (0,0,0) by gate S93-W2-1 residual 0.00e+00 + BDI/KO-dim=6 "
        "parity; faithful-shriek needs image ≠0 AND =(0,0,0) ⇒ contradiction); STRUCTURAL-"
        "ORTHOGONAL-COMPANIONs (Axis-1 algebra-INVARIANT + Axis-2 algebra-DEPENDENT; cross-"
        "corner co-primary FORBIDDEN per cross-pillar-bridge-anatomy.md K=3 MANDATORY); "
        "complementary conjuncts (Axis-2 forecloses (i) selection-by-deletion, Axis-1 forecloses "
        "(ii) the image); LBA-5 permanently undischargeable as a THEOREM, (c) EXTRINSIC "
        "RESTRICTION WITH AXIOM-FORCED KERNEL upgrades to categorically-obstructed-for-all-"
        "bridge-maps; L_max-INVARIANT (cohomology-class layer); STAGE-1-CANDIDATE, Stage-2 "
        "two-agent NON-AUTHOR cross-axis verify S112+ (verifiers MUST NOT be connes or "
        "van-den-dungen); S111 W3-4 JOINT gate, verdict audit_sha256 "
        "3bee7c3e87c73854817ed67f6e72fdaf0d2840c88dba45d864803ec384910868; "
        "single-shot AFTER-pattern, slot §VII.CI runtime-verified next-free over ALL header "
        "levels [frontier §VII.CH S111 W1-5]"
    )
    return (f"| {SLOT} | THM | {desc} | van-den-dungen-bridge-theorist + "
            f"connes-ncg-theorist | {DATE} |")


def build_section_body():
    # NOTE: plain (non-f) string -- the body contains LaTeX/math single braces
    # ({CP^2}, {M_3}, {(3)}, {-alpha}, ...) that must be LITERAL, not f-string
    # expressions.  The two {SLOT} placeholders are substituted via .replace().
    body = """

---

### {SLOT} — Categorical Two-Conjunct Obstruction Theorem for the χ Inheritance Morphism: χ : A_K = ℂ⊕ℍ⊕M_3(ℂ) → M_2(ℂ) is the Connes-Karoubi DELETION for ALL constructions/bridges, NOT the Kasparov shriek π_!^{CP²} of SU(3)→CP² (STAGE-1-CANDIDATE cross-axis JOINT theorem — Axis-2 C*-algebra-type [CONJUNCT (i)] ∧ Axis-1 K-homology [CONJUNCT (ii)], complementary-conjunct PASS-AND'd JOINT; S111 W3-4 van-den-dungen-bridge-theorist LEAD + connes-ncg-theorist Axis-1; single-shot AFTER-pattern per `registry-landing.md`; slot {SLOT} runtime-verified next-free over ALL header levels [frontier §VII.CH S111 W1-5]; 2026-06-21)

**STAGE TAG: STAGE-1-CANDIDATE** (registered S111 W3-4, single-shot AFTER-pattern; the JOINT OBSTRUCT-PASS verdict — gate `S111-CF-M1-INTERTWINER`, audit_sha256 `3bee7c3e87c73854817ed67f6e72fdaf0d2840c88dba45d864803ec384910868`. Stage-2 two-agent NON-AUTHOR cross-axis PASS-AND queued as a SEPARATE S112+ gate per `joint-theorem-promotion.md` 4-stage pathway — the Stage-2 verifiers MUST NOT be connes-ncg-theorist or van-den-dungen-bridge-theorist [original-author exclusion + downstream-inheritance reach], axis-distinct per the Axis-B Selection Protocol).

**Theorem (S111 W3-4).** The inheritance morphism `χ : A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ) → M_2(ℂ)` (the BdG/Nambu child; `χ(M_3(ℂ)) = 0`, `ℂ,ℍ → M_2(ℂ)` canonically) is the **Connes-Karoubi zero-map / DELETION**, NOT the Kasparov shriek `π_!^{{CP²}}` of the internal submersion `SU(3) → SU(3)/U(2) = CP²` (vertical fibre U(2)), for **ALL** homomorphism-type constructions and **ALL** K-natural bridge maps. This LIFTS the S110 W1 WS-M1-INTERTWINER reading-adjudication (Reading B on TWO decidable axes — ONE bridge `ι_*∘HKR` for Axis-1, ONE construction ACM for Axis-2) to the **categorical all-X statement**, proven on two **complementary** conjuncts. Consequently **LBA-5 is permanently undischargeable as a THEOREM** (not merely PROMOTED-UNDISCHARGED on two decidable axes), and the §VII.W-3.SUBSTRATE (c) verdict-name **"EXTRINSIC RESTRICTION WITH AXIOM-FORCED KERNEL"** upgrades from "PERMANENT on two independent decidable axes" to **"categorically obstructed for all bridge maps."** N7-(ii) spectral-triple-for-D_total stays **CONDITIONAL** (now permanently — the discharge condition is a proven impossibility); N7-(i) algebraic-singleton stays **UNCONDITIONAL**.

**Single-root statement (JOINT, complementary-conjunct PASS-AND'd across BOTH axes).** VDD2's (S110 W1) discharge condition is a CONJUNCTION: LBA-5 discharges iff a vertically-elliptic symbol `σ_v` on the U(2)-fibre (i) **SELECTS** exactly `ker(ι_*) = M_3(ℂ)` AND (ii) carries a **NON-trivial** integrated K-homology class. The theorem proves BOTH conjuncts independently impossible — `(i)` foreclosed for ALL constructions by Axis-2, `(ii)` foreclosed for ALL K-natural bridges by Axis-1. The two foreclosures CLOSE DIFFERENT (complementary) conjuncts; their logical AND is the categorical obstruction. This is the JOINT clause: BOTH cross-axis reviewers (Stage-2, S112+) must independently PASS the complementary pair.

**CONJUNCT (i) [Axis-2 — C*-algebra-type / algebra-DEPENDENT; van-den-dungen]: no homomorphism-type construction realizes `A_K → A_K/M_3(ℂ)` as a fibre-integration.** Generalizes the S110 W1 Axis-2 ACM-route foreclosure (ONE construction) to ALL `SU(3)→CP²` C*-algebra-homomorphism constructions, on facts NONE of which is ACM-specific:
  - **(i.a) Codomain rank obstruction (route-INDEPENDENT, exhaustive).** Any unital *-homomorphism `ρ : A_K → M_2(ℂ)`, restricted to the simple summand `M_3(ℂ)`, is `0` or injective; an injective unital *-hom would embed `M_3(ℂ)` (smallest faithful module `ℂ³`) into `M_2(ℂ)`'s module `ℂ²` — impossible (`3 > 2`). Exhaustively: the ONLY two decompositions of `ℂ²` as an `A_K`-module are `(mult_ℂ, mult_ℍ, mult_{M_3}) = (2,0,0)` and `(0,1,0)` — **neither contains the M_3-irrep** (Sage-verified). So in the BdG codomain `M_2(ℂ)`, `ρ(M_3(ℂ)) = 0` for **every** *-hom: retention of M_3 is impossible, deletion is FORCED, independent of construction. (Stronger than the ACM-route argument: a codomain-rank fact, not a missing-operation fact.)
  - **(i.b) Skolem-Noether block rigidity.** The three Wedderburn blocks of `A_K` are the unique minimal two-sided ideals, with an all-distinct `(center, real-dim)` signature: `ℂ` (center ℂ, dim 2), `ℍ` (center ℝ, dim 4), `M_3(ℂ)` (center ℂ, dim 18). `ℍ` is isolated by its center (ℝ vs ℂ); `ℂ` vs `M_3` separated by real-dim (2 vs 18). Every *-automorphism / *-endomorphism is therefore BLOCK-INNER (Skolem-Noether: all algebra autos of `M_n(ℂ)` inner; no block-swap when invariants are all distinct). The ONLY summand-removing morphism is the Wedderburn QUOTIENT `q : A_K → A_K/M_3(ℂ) = ℂ ⊕ ℍ` (the ideal `M_3 → 0`) — a **DELETION**. A fibre-integration / shriek RETAINS its fibre as a NON-trivial integrated class (Paper 01, 1811.07824, Thm 3.4: the shriek is the push-FORWARD of a vertically-elliptic operator, NOT an annihilation). **SELECTION (sub-object retention) ≠ DELETION (quotient)** — categorically opposite arrows; no construction bridges them.
  - **(i.c) Vertical-ellipticity consistency.** Vertical ellipticity (Paper 01 file line 41: `σ(D)` invertible in all fibre-orthogonal directions) is the DEFINING hypothesis of `π_!`. A zero-image "retention" requires the vertical symbol non-invertible everywhere = the NEGATION of the hypothesis ⇒ it is NOT a shriek. So a "shriek" whose image deletes M_3 (i.a) is not a degenerate shriek — it is not a shriek at all.
  - **K_0 Morita cross-check.** `K_0(M_n(ℂ)) = K_0(ℂ) = ℤ` ⇒ `K^0(A_K) = ℤ³`, one ℤ per Wedderburn block (the M_3 summand is a single generator). **CONJUNCT (i) VERDICT: FORECLOSED.**

**CONJUNCT (ii) [Axis-1 — K-homology / algebra-INVARIANT / Fredholm-index; connes]: all K-natural bridge maps send the M_3-generator of `K^0(A_K)=ℤ³` → (0,0,0).** Extends the S110 W1 Axis-1 one-bridge anchor (`ι_*∘HKR`, gate S93-W2-1 `[φ_cd]=(0,0,0)`, residual `0.00e+00`) to ALL K-natural bridges, DERIVED (not assumed) from two bridge-INDEPENDENT properties of the SOURCE class `g_3 = (0,0,1)` with the gate as the empirical anchor:
  - **(Pillar A — Morita-collapse + functoriality / index-rigidity).** `K_0(M_3(ℂ)) = K_0(ℂ) = ℤ` (matrix size does NOT inflate rank) ⇒ the deleted M_3 summand is the single generator `g_3` represented by a rank-1 projector `[e_11^{(3)}]`. A K-natural bridge is a homomorphism of K-groups; on `g_3` it returns a Fredholm INDEX (integer triple) that is a HOMOTOPY INVARIANT of the source class. Any two K-natural bridges agreeing on `g_3` (forced — same Wedderburn source) give the SAME triple. The gate computed that universal index once: `(0,0,0)`; functoriality propagates it to all bridges.
  - **(Pillar B — BDI / KO-dim=6 parity).** In AZ class BDI (`T²=+1`, `(ε,ε',ε'')=(+1,+1,−1)`) the real structure `J` + chirality `γ_9` force the signed winding of the deleted triality-0 sector identically zero (`T_signed_grading = +0.0`), a parity property of the SOURCE class inherited by ANY K-natural bridge intertwining `(J, γ_9)`.
  - **(Morita/faithfulness contradiction).** A faithful Kasparov shriek is the push-FORWARD of the fibre Dirac family (Paper 01 Thm 3.4) ⇒ NON-trivial integrated class ⇒ index `≠ 0`. A re-routing bridge `B'` would need `B'(g_3)` simultaneously `≠ (0,0,0)` [faithfulness] AND `= (0,0,0)` [the pinned index, Pillars A & B] ⇒ strict contradiction. An internal shriek changes the TARGET pairing at most, never the SOURCE generator. **CONJUNCT (ii) VERDICT: FORECLOSED** (with zero residual on the anchor).

**Complementary-conjunct decomposition (why the obstruction is now CATEGORICAL, not "two decidable axes").** The two conjuncts close the two HALVES of the discharge CONJUNCTION on DISJOINT scopes whose UNION is exhaustive: Axis-2 (i) covers ALL homomorphism-type / SELECTION-by-deletion constructions (including NON-K-natural fibre-integrations); Axis-1 (ii) covers ALL K-natural bridges. A construction is either K-natural (⇒ killed by (ii): image `(0,0,0)`) or not (⇒ killed by (i): no homomorphism-type fibre-integration realizes the Wedderburn quotient). **Neither conjunct alone closes the categorical obstruction; `(i) ∧ (ii)` does** — the binding qualifier "K-natural" on Axis-1 is exactly the scope (i) complements. This is the S110 W1 DISSENT-2 conjunct-decomposition lifted to the all-X level on BOTH axes: Axis-1 ι_*∘HKR → all-K-natural-bridges, Axis-2 ACM → all-constructions.

**STRUCTURAL-ORTHOGONAL-COMPANION anchor structure (NOT SOURCE-DOUBLE-CITE-CO-PRIMARY).** The two conjuncts/axes are recorded as STRUCTURAL-ORTHOGONAL-COMPANIONs: Axis-1 is the **algebra-INVARIANT** (K-homology / Fredholm-index) anchor; Axis-2 is the **algebra-DEPENDENT** (C*-algebra-homomorphism-type) anchor. Per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` (MANDATORY at K=3), a SOURCE-DOUBLE-CITE-CO-PRIMARY chain ACROSS the algebra-INVARIANT ↔ algebra-DEPENDENT orthogonality is STRUCTURALLY FORBIDDEN (`registry-landing.md §SOURCE-DOUBLE-CITE-CO-PRIMARY` Detection criterion 4: both anchors on the same algebra-axis cell). The two axes are on OPPOSITE cells ⇒ STRUCTURAL-ORTHOGONAL-COMPANIONs, never co-primary. This inherits the within-cell discriminator (α) structure of the registry line-287 W3/W4 "two independent derivations" pair (representation-theoretic anchor vs K-theoretic anchor).

**χ-vs-ρ_gauge distinct-morphisms guard (carried from S110 W1 — the relocation is CONSERVATION, NOT a partial discharge).** The triality-0/U(2)-invariant content that a genuine `π_!^{CP²}` would integrate is NOT lost when χ deletes M_3 — it is RELOCATED to the ACM gauge-module sector as topological-charge / Chern-class data via the DISTINCT morphism `ρ_gauge : (A_K,H_K,D_K) → C₀(P)⋊G` (a RETENTION onto a DIFFERENT child). LBA-5 is about **χ** (the BdG inheritance morphism — the only map the discharge condition concerns); the existence of `ρ_gauge` does NOT make χ a faithful shriek. The content is REDISTRIBUTED across children (deleted from BdG, kept in gauge), conserved at the substrate level — a substrate-IS conservation reading per `phononic-framing.md` Level-1, NOT a discharge. (Coherence with S98: the BdG child KEEPS the distinct fiber-Goldstone class — `c_s²=0` / `σ/m=0` protected zeros — under χ; it LOSES the triality-0/M_3 class. Two distinct K-homology classes, opposite fates, no collision.)

**Registry anatomy (intra-NCG categorical / K-homology structural theorem; 5-anatomy IS-not-IN cross-pillar elements N/A with reason).** This is an INTRA-NCG categorical / K-homology theorem (whether the inheritance morphism χ is a faithful shriek or the zero-map), NOT a cross-pillar substrate-IS ↔ laboratory-IN bridge: it has no continuum-measurement laboratory-IN observable and no `L^{-α}` convergence envelope (the obstruction is L-INDEPENDENT — it holds at every L_max; `K^0(A_K)=ℤ³` is fixed by Morita invariance independent of any truncation, and the C*-algebra-homomorphism type is a construction-level fact). The 5-anatomy elements (substrate-IS observable / laboratory-IN observable / HKR-or-K-theory bridge map / algebraic envelope / empirical anchor) are therefore N/A by construction; the structural-confidence content is the two-conjunct categorical proof + the gate S93-W2-1 `(0,0,0)` anchor. **Layer placement** (`phononic-framing.md §"Single-τ-slice vs moduli-deformation"`): Level-1 (single-τ-slice) — a statement about the finite spectral triple's algebra/K-theory at fixed τ, scheme-independent, L_max-independent, zero free parameters (the structural-floor side of the S73B "structural floor vs prediction layer" boundary).

**Direction of explanation (substrate-first).** The substrate IS `(A_K, H_K, D_K)` (Pillar III); χ is a morphism ONTO a child (the BdG `M_2(ℂ)` sector), NOT a constraint FROM the child onto `A_K`. Container-thinking inversion ("the BdG sector constrains A_K" / "the χ-image discharges the obstruction") is FORBIDDEN per `phononic-framing.md §"IS Space, Not IN Space"`. The triality-0/M_3 content χ deletes from the BdG child is RELOCATED (not lost) to the ACM gauge sector as topological charge via the distinct morphism `ρ_gauge` — substrate-IS conservation, EMERGENCE, NOT a discharge.

**Source / provenance.** S110 W1 WS-M1-INTERTWINER workshop (`sessions/session-110/workshops/ws-m1-intertwiner.md`, connes × van den Dungen CONVERGED, Reading B on two decidable axes + the residual categorical-obstruction CF this entry discharges); gate `S93-W2-1-VII-AU-CF37-FREDHOLM-INDEX-INTEGER-TRIPLE` `[φ_cd]=(0,0,0)` residual `0.00e+00` canonical audit_sha256 `76e5d744b36b7b35edced48bffe63659c0e667ee2f60bd9272203819496c5f99` (Axis-1 anchor); `05_2014_van_den_Dungen_Globally_Non_Trivial_ACM.md` (1405.5368: `A_F=ℂ⊕ℍ⊕M_3(ℂ)` FIXED line 58; crossed-product `C₀(P)⋊G` lines 68-70/81-83; Axis-2 ACM-route foreclosure this entry generalizes); `01_2018_van_den_Dungen_Kasparov_Submersions.md` (1811.07824 Thm 3.4 push-forward + vertical-ellipticity file line 41); §VII.W-3.SUBSTRATE (the two-axis obstruction record this entry upgrades to categorical); `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` (STRUCTURAL-ORTHOGONAL-COMPANION discipline). Sage-verified structural facts: codomain-rank exhaustion over the two `ℂ²` decompositions `{(2,0,0),(0,1,0)}`; all-distinct block `(center,real-dim)` signatures; `K^0(A_K)=ℤ³` Morita. **Substrate framing:** the substrate IS the finite spectral triple `(A_K, H_K, D_K)`; χ is the inheritance morphism onto the BdG `M_2(ℂ)` child; the no-faithful-shriek is foreclosed by what χ IS, on two complementary algebraic facts (codomain-rank deletion + all-K-natural-bridge zero-image), at the K-homology / categorical layer.

**Math-owners / Stage-0 authors (Stage-1 registrants, EXCLUDED from Stage-2 review per the original-author-exclusion + downstream-inheritance-reach clause):** van-den-dungen-bridge-theorist (CONJUNCT (i) / Axis-2 C*-algebra-type) + connes-ncg-theorist (CONJUNCT (ii) / Axis-1 K-homology). **Stage-2 reviewers (axis-distinct, original-author-excluded, no-workshop-context — to be dispatched as a SEPARATE S112+ gate):** Axis-A = K-homology/NCG-axiomatic NON-AUTHOR (e.g. lizzi-spectral-functional-theorist OR spectral-geometer — the all-K-natural-bridge zero-image conjunct); Axis-B = C*-algebra-type/submersion NON-AUTHOR (e.g. baptista-spacetime-analyst OR kaluza-klein-theorist — the homomorphism-type / Wedderburn-quotient-vs-fibre-integration conjunct). Both operate WITHOUT prior workshop context per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"`; JOINT complementary-conjunct PASS-AND'd across both verdicts (logical AND, not OR). Verdict audit_sha256 `3bee7c3e87c73854817ed67f6e72fdaf0d2840c88dba45d864803ec384910868` (gate `S111-CF-M1-INTERTWINER`).
"""
    return body.replace("{SLOT}", SLOT)


# ----------------------------------------------------------------------------------
# 3) write_atomic_with_fsync
# ----------------------------------------------------------------------------------
def write_atomic_with_fsync(path, new_text):
    tmp = path + ".tmp_s111regland"
    with open(tmp, "w", encoding="utf-8", newline="") as f:
        f.write(new_text)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)


# ----------------------------------------------------------------------------------
# 4) verify_section_matches (re-read)
# ----------------------------------------------------------------------------------
def verify_landed(text, master_row, section_anchor):
    row_ok = master_row.strip() in text
    body_ok = section_anchor in text
    # The slot must now appear EXACTLY as one master row + one section header (>=2 hits;
    # plus any internal cross-refs the body itself contains — so >=2 is the floor).
    n_slot = len(re.findall(re.escape(SLOT) + r"\b", text))
    return (row_ok and body_ok and n_slot >= 2), {
        "master_row_present": row_ok,
        "section_body_present": body_ok,
        "slot_occurrence_count": n_slot,
    }


def closure_hash(pin_map):
    blob = json.dumps(pin_map, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(blob).hexdigest()


def main():
    with open(REGISTRY, "r", encoding="utf-8") as f:
        text = f.read()

    free, n_pre = verify_slot_free(text, SLOT)
    if not free:
        # Slot collision at runtime -> FAIL-with-remediation (do NOT overwrite).
        print(f"SLOT COLLISION: {SLOT} already present ({n_pre} hits). "
              f"FAIL-with-remediation: reroute to next-free letter.")
        # Emit a FAIL closure so the rerouting is visible in the audit trail.
        verdict = "FAIL"
        value = (f"SLOT-COLLISION: {SLOT} occupied at runtime ({n_pre} hits); "
                 f"registry landing NOT applied; reroute to next-free letter required")
        pin_map = {"gate_id": GATE_ID, "slot": SLOT, "collision": True,
                   "n_pre_hits": n_pre, "verdict": verdict}
        audit_sha = closure_hash(pin_map)
        content_sha = sha256_text(build_master_index_row() + build_section_body())
        _print_payload(verdict, value, audit_sha, content_sha)
        return

    master_row = build_master_index_row()
    body = build_section_body()
    section_anchor = f"### {SLOT} — Categorical Two-Conjunct Obstruction Theorem"

    # --- Insert master-index row AFTER the §VII.CH master-index row ---
    # The master row is a single | ... | line beginning with "| §VII.CH |".
    lines = text.split("\n")
    ch_row_idx = None
    for i, ln in enumerate(lines):
        if ln.startswith("| §VII.CH |"):
            ch_row_idx = i
            break
    if ch_row_idx is None:
        raise RuntimeError("Could not locate §VII.CH master-index row for insertion.")
    lines.insert(ch_row_idx + 1, master_row)
    text2 = "\n".join(lines)

    # --- Append section body at end of file (after the last §VII section, which is
    #     §VII.CH ending at EOF) ---
    if not text2.endswith("\n"):
        text2 += "\n"
    text2 = text2 + body

    write_atomic_with_fsync(REGISTRY, text2)

    # --- Re-read + verify BOTH surfaces ---
    with open(REGISTRY, "r", encoding="utf-8") as f:
        reread = f.read()
    ok, detail = verify_landed(reread, master_row, section_anchor)

    verdict = "PASS" if ok else "FAIL"
    value = (f"REGISTRY-LANDED {SLOT}: master_row={detail['master_row_present']} "
             f"section_body={detail['section_body_present']} "
             f"slot_occurrences={detail['slot_occurrence_count']}; "
             f"STAGE-1-CANDIDATE two-conjunct categorical obstruction theorem; "
             f"both surfaces landed in ONE single-shot AFTER-pattern run")

    pin_map = {
        "gate_id": GATE_ID,
        "slot": SLOT,
        "registry_path": "sessions/permanent-results-registry.md",
        "master_row_sha256": sha256_text(master_row),
        "section_body_sha256": sha256_text(body),
        "verdict_gate_audit_sha256": "3bee7c3e87c73854817ed67f6e72fdaf0d2840c88dba45d864803ec384910868",
        "master_row_present": detail["master_row_present"],
        "section_body_present": detail["section_body_present"],
        "slot_occurrence_count": detail["slot_occurrence_count"],
        "verdict": verdict,
    }
    audit_sha = closure_hash(pin_map)
    content_sha = sha256_text(master_row + body)
    _print_payload(verdict, value, audit_sha, content_sha)


def _print_payload(verdict, value, audit_sha, content_sha):
    payload = {
        "session": 111,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": value,
        "scheme": "registry-landing-single-shot-AFTER-pattern",
        "convention": "STAGE-1-CANDIDATE-VII-CI-two-conjunct-categorical-obstruction",
        "l_max": "N/A",
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    print("=" * 78)
    print("REGISTRY-LANDING VERDICT PAYLOAD (agent: call emit_verdict):")
    print(json.dumps(payload, indent=2))
    print("=" * 78)
    with open(os.path.join(HERE, "s111_m1_intertwiner_regland_payload.json"),
              "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    print("Run timestamp:", datetime.datetime.now().isoformat())


if __name__ == "__main__":
    main()
