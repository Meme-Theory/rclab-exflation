# α_s Multi-Valued Landscape Registry

**Provenance**: S88 W5a-41 (`S88-MULTI-VALUED-ALPHA-S-LANDSCAPE-MAPPING`); mack-cosmic-bridge sole writer per `feedback_mack-bridge-role.md`. Canonical 4-corner taxonomy source: `.claude/rules/cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` (MANDATORY at K=3 promoted S87 W-2 R3 close 2026-04-29).

**Plan-authorship gap noted**: plan §W5a-41 cites "S87 W-2 §VII.U.2 4-corner classification table" but §VII.U.2 does not exist in `permanent-results-registry.md` (only §VII.U.1, §VII.U.6, §VII.U.7 are allocated). This file consolidates the 4-corner taxonomy that would otherwise be dispersed across `cross-pillar-bridge-anatomy.md` (rule-file) and `s87-alpha-s-route-dissonance.md` (workshop transcript).

---

## 4-Corner Cell Enumeration

| Cell | Algebra-axis | Mellin-axis | Functional | Status | Substrate-IS value | Closure SHA / Carry-forward |
|:-----|:-------------|:------------|:-----------|:-------|:-------------------|:----------------------------|
| **Cell I** | INVARIANT | FI (substrate-distance-1 pole s=3) | `Res[M(s); s=3]` | CLOSED | -8587279/100000000 (Sage-QQ exact) | `e747495c1fbf8af144c3701ecaf5e77b...` |
| **Cell II** | INVARIANT | RD (substrate-distance-2 cone s=4) | `Res[M(s); s=4]` | OPEN | TBD | `S89-CELL-II-INVARIANT-RD-MELLIN-RESIDUE-COMPUTE` |
| **Cell III** | DEPENDENT | FI (substrate-distance-1 pole s=3, state-functional form) | `K-window-averaged variance at s=3 with GGE Bogoliubov vacuum` | OPEN | TBD | `S89-CELL-III-DEPENDENT-FI-K-WINDOW-VARIANCE-COMPUTE` |
| **Cell IV** | DEPENDENT | RD (substrate-distance-2 cone s=4, state-functional form) | `Var_a(n_a^GGE) at s=4 cross-cone` | CLOSED | -7.046336 (S87 W2-3 GGE-Bogoliubov-occupation-variance) | `—...` |

## Closed Cells: Per-Cell Detail

### Cell I

- **axis_algebra**: INVARIANT
- **axis_mellin**: FI (substrate-distance-1 pole s=3)
- **functional**: Res[M(s); s=3]
- **value_status**: CLOSED
- **value_form**: -8587279/100000000 (Sage-QQ exact)
- **value_decimal**: -0.08587279
- **L_max**: 12
- **closure_sha**: e747495c1fbf8af144c3701ecaf5e77b2497d3b876281bdffb703d8db22839f3
- **registered_at**: §VII.AN (S88 W5a-37, audit_sha256=cf5ec646...)
- **anchor_structure**: SOURCE-DOUBLE-CITE-CO-PRIMARY
- **lab_bridge**: Mukhanov-Sasaki gauge ∘ HKR L_max → ∞ (FWD-C1 candidate)

### Cell IV

- **axis_algebra**: DEPENDENT
- **axis_mellin**: RD (substrate-distance-2 cone s=4, state-functional form)
- **functional**: Var_a(n_a^GGE) at s=4 cross-cone
- **value_status**: CLOSED
- **value_form**: -7.046336 (S87 W2-3 GGE-Bogoliubov-occupation-variance)
- **value_decimal**: -7.046336
- **L_max**: 10
- **closure_sha_source**: S87-ALPHA-S-DIRECT-MOMENT-INDEPENDENT-ROUTE verdict (s87_gate_verdicts.txt)
- **scheme**: GGE-Bogoliubov-occupation-variance
- **convention**: horizon-crossing-K-window-canonical
- **anchor_structure**: STRUCTURALLY-ORTHOGONAL-COMPANION-NOT-CO-PRIMARY (with Cell I)
- **cross_corner_ratio_to_I**: 704633600/8587279 = 82.0556× (Sage-QQ exact, FORBIDDEN as gate per K=3 MANDATORY)

## Open Cells: PRDR Carry-Forward Specs

### Cell II

- **axis_algebra**: INVARIANT
- **axis_mellin**: RD (substrate-distance-2 cone s=4)
- **functional**: Res[M(s); s=4]
- **value_status**: OPEN
- **value_form**: TBD (carry-forward to S89+)
- **L_max_required**: 12
- **PRDR_recipe**: Compute Res[Tr(D_K^{−2s}); s=4] from s84_spectrum_cache_L12_tau019.npz via CM-1995 §III.4 dim-spectrum residue formula at d=4, n=−4 (generalized substrate-distance-2 pole). Mellin-moment normalization per S82 W3-9 convention extension to RD pole.
- **machinery_pin**: L_max=12 (Casimir-bound feasible); cache-hit on s84_spectrum_cache_L12_tau019.npz; Sage-QQ exact arithmetic via mcp__sage__sage_eval
- **carry_forward_id**: S89-CELL-II-INVARIANT-RD-MELLIN-RESIDUE-COMPUTE

### Cell III

- **axis_algebra**: DEPENDENT
- **axis_mellin**: FI (substrate-distance-1 pole s=3, state-functional form)
- **functional**: K-window-averaged variance at s=3 with GGE Bogoliubov vacuum
- **value_status**: OPEN
- **value_form**: TBD (carry-forward to S89+)
- **L_max_required**: 12
- **PRDR_recipe**: Compute Var_a(n_a^GGE) with K-window averaging restricted to s=3 substrate-distance-1 pole — ANALOG of Cell IV but at FI Mellin axis. Requires GGE Bogoliubov vacuum specification (S87 W2-3 machinery) plus FI-pole window restriction.
- **machinery_pin**: L_max=12; GGE Bogoliubov vacuum at τ=0.190; FI-pole K-window restriction (structurally analogous to W2-3 RD-pole construction)
- **carry_forward_id**: S89-CELL-III-DEPENDENT-FI-K-WINDOW-VARIANCE-COMPUTE

## Auxiliary Functionals (candidates on the 2D orthogonality grid)

- **Wodzicki-Schur reflection at s=3** (INVARIANT × FI, status: candidate-but-unverified). Recipe: Wodzicki residue × Schur orthogonality identity at substrate-distance-1 pole
- **Heitsch-cocycle-norm-ratio at s=4** (DEPENDENT × FI, status: candidate-but-unverified). Recipe: Heitsch GV cocycle pair-norm ratio at s=4 cone
- **Connes-Karoubi pairing on Jensen-deformed band-0 projector** (INVARIANT × RD, status: candidate-but-unverified). Recipe: Pairing ⟨[φ_g^{sym}], [Ch(P_0(τ_fold))]⟩ — substrate-IS regulator-invariant

## 6-Pair Orthogonality Cross-Check (algebra-axis K=3 MANDATORY)

Per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3: for each unordered pair of cells, verify at least one axis (algebra OR Mellin) is structurally distinct, ensuring no closed-form {λ_n}-only identity bridges the axis-difference.

| Pair | Same algebra-axis? | Same Mellin-axis? | At least one distinct? | Kind |
|:-----|:-------------------|:------------------|:----------------------|:-----|
| **(Cell I, Cell II)** | True | False | True | Mellin-axis-distinct |
| **(Cell I, Cell III)** | False | True | True | algebra-axis-distinct |
| **(Cell I, Cell IV)** | False | False | True | biaxial-orthogonal |
| **(Cell II, Cell III)** | False | False | True | biaxial-orthogonal |
| **(Cell II, Cell IV)** | False | True | True | algebra-axis-distinct |
| **(Cell III, Cell IV)** | True | False | True | Mellin-axis-distinct |

All 6 unordered pairs satisfy the orthogonality predicate (no pair has same-algebra AND same-Mellin; the 4 cells partition the 2×2 grid). The K=3 MANDATORY theorem holds at the 4-corner enumeration layer.

---

## Cross-References

- §VII.AN (S88 W5a-37): Cell I SOURCE-DOUBLE-CITE-CO-PRIMARY anchor structure.
- §VII.{slot} (W5a-42 pending): Cell I biaxial-FI registry row inheriting CO-PRIMARY anchor.
- §VII.{slot} (W5a-43 pending): Cell IV biaxial-DRESSED structurally-orthogonal companion.
- `.claude/rules/cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` — canonical taxonomy source.
- `sessions/archive/session-87/workshops/s87-alpha-s-route-dissonance.md` — S87 W-2 R3 closure (MANDATORY K=3 promotion).

## Hygiene observation (registry-pace concern, S88 2026-05-04)

This is the third α_s-themed registry file in `sessions/framework/registry/` alongside `alpha-s-structural-protection.md` and `alpha-s-watchlist.md`. Per `feedback_rules-compensate-missing-structure.md`, three α_s registries with overlapping scope is the failure mode. Next-session consolidation candidate: merge into a single `alpha-s-master-registry.md` with sections [structural-protection / watchlist / multi-valued-landscape] OR cross-link to a single canonical entry-point. Logged as S89 hygiene carry-forward.
