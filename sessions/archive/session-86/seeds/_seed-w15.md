# Seed file — sessions/archive/session-86/session-86-w15-workingpaper.md

**Date**: 2026-04-26
**Investigator**: phonon-first-cosmologist
**Source WP**: `sessions/archive/session-86/session-86-w15-workingpaper.md` (309 lines)

## Candidates

### Candidate 1 — Substrate K-theoretic parent: enumerate the surviving candidate set

**What it would do**: W15-1 anchored ANTI-CORRESPONDENCE entry #30 excluding Witten 1998 Type IIB D-brane scheme as a candidate parent for the substrate's K-theory. The WP §W15-1 line 48 + line 230 explicitly note "framework remains parent-undetermined at the K-theoretic level overall" with heterotic E8×E8, M-theory C-field, twisted K, and now Witten 1998 all excluded (S85 W10-5 + W15-1). A solo synthesis would assemble the FULL exclusion ledger from `sessions/framework/correspondence/correspondence-table-registry.md` (entries #19/#20/#21/#30 plus any S85 W10-5 cousins), enumerate the K-theoretic candidate-parent space (e.g. orientifold variants, F-theory K-theory, twisted equivariant K, Karoubi K-theory of `A_F = C ⊕ H ⊕ M_3(C)`, KK-theory à la Kasparov), and report which candidates remain structurally compatible with the substrate's 4-obstruction-vector signature `(rank=3, K_0=torsion-free, Witten-integral=16.0, Bott-residue≠1)`. The deliverable is a structural map of "what K-theoretic schemes the substrate COULD still be a quotient/colimit/cover of," not a new gate verdict.

**Why it's worthwhile**: The WP itself flags this as an open structural question (§W15-1 line 48: "parent-Witten-1998-EXCLUDED with this registry landing" + line 230: "framework remains parent-undetermined at K-theoretic level overall"). Multiple parent candidates have now been individually excluded across S64 (#19/#20/#21) and S85 W10-5 + S86 W15-1 — the union of these exclusions defines a structurally narrow surviving region that no single workshop has mapped. Identifying which K-theoretic structures REMAIN compatible would convert "parent-undetermined" from an indefinite open question into a bounded short-list, materially advancing the framework's K-theoretic positioning. Cross-pillar payoff: the answer constrains Pillar III (NCG spectral triple's K-theoretic content) against Pillar VIII (KK on Lie groups — Kasparov KK-theory has natural overlap with the SU(3) representation lattice). If the surviving candidate set is empty, that itself is a structural finding (the substrate is K-theoretically novel, not a quotient of any existing scheme).

**Type**: solo (1 agent)

**Suggested agents**: connes-ncg-theorist (canonical NCG/K-theory expertise; substrate spectral triple is his native language)

**Rounds (workshops only)**: n/a (solo)

**Context the workshop will need**:
- `sessions/framework/correspondence/correspondence-table-registry.md` (NEW from W15-1; 103 lines; entries #19/#20/#21/#30 explicit)
- `computations/s85_w10_witten_alternative_parents.py` (S85 W10-5 source; per WP line 48 establishes heterotic E8×E8, M-theory C-field, twisted K all carry ≥1 obstruction)
- `computations/s86_w15_anti_correspondence_registry_extension.py` (W15-1 producing script with 4-obstruction-vector definitions)
- The 4-obstruction-vector signature pinned in W15-1: `(rank=3, K_0=torsion-free, Witten-integral=16.0, Bott-period-residue≠1)`
- `EXP_K0_RANK=3, EXP_K0_TORSION=0, EXP_WITTEN_INTEGRAL=16.0, EXP_WITTEN_REQUIRED=1.0` constants confirmed via knowledge MCP search per WP §W15-1 MCP audit
- Substrate-side derivation chains: `A_F = C + H + M_3(C) gives K_0 rank 3`; `SU(3) representation lattice gives torsion-free K_0`; `third spectral moment of D_K gives Witten integral 16.0`; `tau_fold parity flip breaks 8-periodicity` (per WP line 44)
- Adjudication rule: report (i) the FULL exclusion list with paper-traceable obstruction reasons, (ii) the candidate-parent space NOT yet litigated against the substrate's 4-vector, (iii) which of those candidates can be ELIMINATED by structural argument from the existing 4-vector alone (no new computation), (iv) which require new gates, (v) whether the surviving candidate set is empty, singleton, or multi-element. NOT a verdict gate — a structural map. Output is a §-anchored sub-section in `sessions/framework/correspondence/correspondence-table-registry.md` titled "## Candidate-parent ledger" plus a short solo synthesis report.
- Constraint: this is NOT a new ANTI-CORRESPONDENCE entry. New exclusion entries require their own pre-registered gates per the registry's substrate-framing convention. The synthesis only INVENTORIES the existing exclusion + open candidate space.
