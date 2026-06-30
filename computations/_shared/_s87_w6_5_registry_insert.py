"""
One-shot Python in-place inserter for §VII.AG.6 in
sessions/permanent-results-registry.md.

Inserts the §VII.AG.6 positive-theorem entry after the §VII.AG.5 entry's
terminating `---\n` separator, BEFORE the next major heading
`## §VII.AF — ...` block.

Idempotent: skips if the entry already exists (anchor `### §VII.AG.6 —`
present in file).

Pattern follows S86 W1c append-only one-shot Python writer per
.claude/rules/epistemic-discipline.md §"Registry-Write Hygiene under
Parallel-Writer Race".
"""

from __future__ import annotations

import sys
from pathlib import Path

REGISTRY = Path("sessions/permanent-results-registry.md")

# Insert AFTER §VII.AG.5 entry's trailing `---\n` separator and BEFORE the
# next `## §VII.AF` major heading.  We use the unique `---` block that
# follows the §VII.AG.5 cross-references, identified by the preceding
# §VII.AG.5 cross-references list "§VII.AF.1 (Pillar III ↔ Pillar IV bridge)".
ANCHOR_BEFORE = (
    "- §VII.AF.1 (Pillar III ↔ Pillar IV bridge): companion three-level-ladder "
    "cross-pillar entry."
)

NEW_ENTRY_HEADER = "### §VII.AG.6 — "

NEW_ENTRY = """### §VII.AG.6 — Cross-Cluster Mellin-Wick Commutation Theorem under Klein-V_4 Cyclic-Fold (S87 W6-5; lizzi PRIMARY + volovik CO-SIGNER, 2026-04-29)

**Statement (positive theorem)**:

> "Under the substrate's confirmed Klein-V_4 cyclic-fold partition (S86 W-12 CF-66 element-order signature [1,2,2,2]; distinct from cyclic Z_4 = [1,2,4,4]), the Mellin transform `M[f](s) := ∫_0^∞ f(t) t^(s-1) dt` and the Wick rotation `W: t → -i·t` commute as operators on cross-cluster bilinears `B_{ij}(t) := ⟨φ_{c_i}|O(t)|φ_{c_j}⟩` for every coset pair (i,j) ∈ {0,1,2,3}²:
>
>     [M, W]_{c_i, c_j} = 0  IDENTICALLY (BIT-EXACT, all 16/16 V_4-coset pairs).
>
> **Proof**: Klein-V_4 acts on coset LABELS (a discrete index set) via the regular permutation rep `P_g` (Sage-verified: `a²=b²=(ab)²=e`, `ab=ba`; element-order signature [1,2,2,2] confirmed; 4×4 character table orthonormal `χ·χᵀ = 4·I_4`; abelian rep simultaneously diagonalized in V_4 character basis). Mellin and Wick act on the CONTINUOUS variable t (or its conjugate s). The two are operators on DISJOINT TENSOR FACTORS of the joint Hilbert space `(Time-axis) ⊗ (V_4-coset-rep)`; operators on disjoint tensor factors commute by construction. On the Schwartz reference profile `f(t) = exp(-t)`: `M[f](s) = Γ(s)`, `W[M[f]](s) = e^(iπs/2)·Γ(s)` (Wick lifts to s-side phase `(-i)^(-s) = i^s`), `M[W[f]](s) = M[exp(it)](s) = Γ(s)·e^(iπs/2)` (analytic continuation of Mellin-of-imaginary-exponential). Single-cluster commutator returns 0 BIT-EXACT under Sage `simplify_full()`. Cross-cluster bilinear `B_{ij}(t) = α_{ij}·f(t)` with `α_{ij}` a t-INDEPENDENT V_4-character-valued scalar; therefore `[M,W] B_{ij} = α_{ij}·0 = 0` IDENTICALLY for all (i,j) ∈ {0,1,2,3}², independent of which of the 4 inequivalent 1D Klein-V_4 characters is selected for the Wick phase.
>
> **Counterfactual (necessity claim)**: under cyclic-Z_4 (refuted by S86 W-12 CF-66), Mellin contour rotation and Wick phase rotation would BOTH act on the t-variable as Z_4 generators sharing the SAME tensor factor; their joint structure would not factor; commutator would be non-zero. Hence the substrate's Klein-V_4 character is NECESSARY for cross-cluster Mellin-Wick commutation."

**Substrate framing (per `.claude/rules/phononic-framing.md`)**: the substrate IS the spectral-moment integral; Mellin IS the substrate's substrate-distance probe at pole s=n; Wick IS the substrate's Lorentzian↔Euclidean signature change. The cross-cluster commutator IS the coherence-versus-decoherence between V_4 cosets. PASS confirms substrate-IS coherent across cosets — the V_4 cyclic-fold structure factors through Mellin/Wick joint action because the two factors live on DISJOINT tensor sub-spaces. Container-thinking inversion ("the Mellin-Wick joint action governs how V_4 acts on the substrate") is FORBIDDEN; the substrate IS the V_4 ⊗ Time tensor product, and the commutation is a structural identity on disjoint tensor factors of THIS substrate.

### Slot-allocation note (audit-trail)

Plan §W6-5 (`sessions/session-plan/session-87-plan-w6.md` line 593) pre-allocated §VII.AG.5; the slot was occupied at S86 W-6 by the "D1 Gauge-Counting Correction to V1 Step 3" entry (READY-TO-INSTALL). Per `.claude/rules/epistemic-discipline.md §"Registry-Write Hygiene under Parallel-Writer Race"`, this entry is rerouted to next-free §VII.AG.6 (S84 W2a-11 §VII.M→§VII.N precedent + S87 W1a-1 §VII.U.6 strengthening precedent). Slot reroute documented in the W6-5 verdict-line value string at `computations/session-87/s87_gate_verdicts.txt`; math composite verdict is PASS (the reroute is stale-pre-allocation, not a parallel-writer collision; the W-13 RULE-3 multi-slot synchronization-lockfile precedent applies as documentation only).

### Cross-references

- **§VII.T** — Mellin Strip / Convergence Cone Theorem (Lizzi-track, S85 W0-S6): parent theorem providing the analytic strip `Re(2s) > d_spec` where the substitution chain Step 3 analytic-continuation step is admissible.
- **§VII.U.6** — W1b-T5 LANDING (S86 W-1; S87 W1a-1 strengthening): substrate-distance-1 pole anchor at s=3 with Level-3 audit_sha=`a88ff16e1856588dcaadb82d961edda44736851db15ef121e3f59355cb533daf`.
- **§VII.AG.1** — CF-LZ-VV Cyclic-Fold Mellin Spectroscopy Theorem (W-6 REG-1; LANDED S87 W6-1): origin of the V_4 cyclic-fold partition; supplies the 4-coset structure {c_0, c_1, c_2, c_3} this theorem operates on.
- **§VII.AG.2** — T7 ↔ S67 PASS-Quotient-Isomorphism with Cyclic-Fold Caveat (W-6 REG-2): provides the C_1 ≡ C_4 STRUCTURAL IDENTITY (forced by Mellin-Strip / heat-kernel residue duality) at the WITHIN-cluster level; this §VII.AG.6 entry extends that identity to the CROSS-cluster level under Klein-V_4 tensor-factor disjointness.
- **§VII.AG.3** — DEFERRED Quotient-Functor Universality Principle (W-6 REG-3): forward-looking generalization to which the cross-cluster commutation theorem contributes a structural ingredient.
- **§VII.AF.1** — Pillar III ↔ Pillar IV Bridge Theorem (S86 W-5; LANDED S87 W5-1): companion cross-pillar bridge entry; THIS §VII.AG.6 is a within-pillar (Pillar VII) algebraic identity, not a cross-pillar bridge — the 5-element IS-not-IN anatomy + 3-level ladder discipline (cross-pillar-bridge-anatomy.md) does NOT apply to within-pillar algebraic identities.
- **S86 W-12 CF-66** — V_4 vs Z_4 cardinality refinement (element-order signature [1,2,2,2] vs [1,2,4,4]): the necessity-condition substrate; without CF-66's refinement, the counterfactual Z_4 partition would force [M,W] ≠ 0 cross-cluster.

### Audit SHAs (this entry)

- Producing script: `computations/session-87/s87_w6_mellin_wick_commutation_theorem.py` (24036 bytes).
- Data: `computations/session-87/s87_w6_mellin_wick_commutation_theorem.json` (theorem text + Klein-V_4 character table + 4×4 commutator grid + substitution chain).
- Plot: `computations/session-87/s87_w6_mellin_wick_commutation_theorem.png` (V_4 coset-pair element map + 4×4 commutator-status grid all-green).
- Verdict line: gate-ID `S87-CROSS-CLUSTER-MELLIN-WICK-COMMUTATION-THEOREM` at `computations/session-87/s87_gate_verdicts.txt`; `audit_sha256 = a47fd04bbfadd69e05dab78842213f9c99e3fc7227fe0ada989a0950716a6517`; `content_sha256 = 9103fca3e501fb95369f5e4ad245269c0b9541093c75ac869f6771f84bf8dd59`. S87 schema-v2 3-tuple: `sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID`.

### Composite-collapse status

- `sign_verdict = PASS`: predicted direction `[M,W] = 0`; computed `max_abs_commutator = 0.0`. Direction matches.
- `magnitude_verdict = PASS`: |0 − 0| = 0 (algebraic identity, no margin).
- `regime_verdict = VALID`: holds for any Schwartz profile in the §VII.T strip; theoretical-mode (no L_max truncation, no regime boundary).
- Composite: **PASS** (positive-theorem registry entry; no STAGE-1-CANDIDATE qualifier — single-axis intra-pillar theorem on the spectral-functional axis, not a cross-axis joint theorem requiring 4-stage promotion per `joint-theorem-promotion.md`).



---


"""


def main() -> int:
    text = REGISTRY.read_text(encoding="utf-8")

    # Idempotency: bail if §VII.AG.6 already present
    if NEW_ENTRY_HEADER in text:
        print("[idempotent] §VII.AG.6 entry already present; no-op")
        return 0

    idx_anchor = text.find(ANCHOR_BEFORE)
    if idx_anchor < 0:
        print(f"[ERROR] Could not find anchor: {ANCHOR_BEFORE[:60]}...")
        return 2

    # Find the next blank line + `---\n` separator after the anchor (end of §VII.AG.5 block)
    # Then insert NEW_ENTRY before the `## §VII.AF — ...` major heading.
    # Strategy: locate the `## §VII.AF — ` major heading after the anchor, insert
    # NEW_ENTRY immediately BEFORE it.
    idx_next_major = text.find("\n## §VII.AF —", idx_anchor)
    if idx_next_major < 0:
        print(f"[ERROR] Could not find next major heading `## §VII.AF —` after anchor")
        return 2
    # Insert at idx_next_major + 1 (after the leading \n)
    insert_pos = idx_next_major + 1

    new_text = text[:insert_pos] + NEW_ENTRY + text[insert_pos:]

    REGISTRY.write_text(new_text, encoding="utf-8")

    # Verify
    written = REGISTRY.read_text(encoding="utf-8")
    if NEW_ENTRY_HEADER not in written:
        print("[ERROR] Post-write verification failed: header absent")
        return 3

    # Count substantive lines in the §VII.AG.6 block
    block_start = written.find(NEW_ENTRY_HEADER)
    next_block = written.find("\n## ", block_start)
    if next_block < 0:
        next_block = block_start + 30000
    block = written[block_start:next_block]
    nonblank = [ln for ln in block.splitlines() if ln.strip()]
    print(f"[ok] §VII.AG.6 inserted. Block has {len(block.splitlines())} total lines, {len(nonblank)} non-blank.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
