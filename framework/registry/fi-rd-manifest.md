<!-- registry-meta: type=registry; topic=FI/RD classification manifest; sole-writer=designated; created=S110 -->
# FI/RD Manifest — Functional-Invariant / Regulator-Dependent Classification

**Created**: 2026-06-20 (S110 W0, HK-FIRD).  **Source**: `sessions/investigation/_promotion-triage.md` Bucket-3 §A (HK-FIRD = inv-12 HK-4 / HK-5 / HY1 / HY2 / HY6).
**Status**: investigation-track manifest (per `gate-verdicts.md §"Investigation-Track"`, the entries below are register-permanent only on session-promotion; this manifest records the inv-12 classification for downstream consumers).
**Scope**: classifies spectral-moment / ratio observables on `(A_K, H_K, D_K)` as **FI** (Functional-Invariant — value invariant across the F_2 K-invariant identity sub-atlas / same-regulator cancellation) vs **RD** (Regulator-Dependent — value shifts with the UV-regulator scheme). Cross-link: `.claude/rules/regulator-pin-discipline.md §"Extension: β_shell FI Classification"`; `epistemic-discipline.md §"Source Reconciliation"` FI/RD/MIXED taxonomy.

## Manifest rows

| Observable | Class | Value | Basis | Source |
|:-----------|:------|:------|:------|:-------|
| `R_1` (a₂-ratio at locked-norm L_k=1) | **FI** | **1.1286546** (Sage-Q exact) | Functional-Invariant on **verified same-regulator cancellation** (the regulator factor cancels in the ratio); inherits FI from the F_traj a₂-ratio FI theorem (parent). Supersedes the round-figure 1.128653. | inv-12 HY1 |
| `a_2^ζ` vs `a_2^SDW` | **HARMLESS_ALIAS** | — | `a_2^ζ ≡ a_2^SDW` as a label: the zeta-regulated and Seeley-DeWitt a₂ coincide for this observable (same-regulator-class members); the distinct labels are aliases, not a class split. | inv-12 HY2 |

## Per-moment pole-convergence ledger (inv-12 HK-4 / HK-5)

5/5 of the load-bearing Mellin-cone poles are **divergent-pole** (the shell-sum `L^{d−2s}` diverges at the pole), with a **3-class split** across the moment family (FI / RD / MIXED per the `epistemic-discipline.md` taxonomy). The per-moment classification:

- The FI members are the K-invariant identity sub-atlas observables (ratios where the regulator factor cancels — e.g., `R_1`).
- The RD members shift with the UV-regulator scheme (the `a_n^{regulator}` tag is load-bearing per `regulator-pin-discipline.md`).
- The MIXED members carry a regulator-dependent magnitude with a regulator-invariant sign/structural content.

(Full per-moment table is investigation-track in `sessions/investigation/investigation-12/`; this manifest records the FI/RD class assignments for downstream pin-discipline consumers. Session-promotion of the numerical per-moment values is required before any becomes a canonical pin.)

## Forward enforcement

New `a_n` / ratio citations consuming these observables MUST carry the FI/RD class tag (per `regulator-pin-discipline.md`); FI observables are cited at Sage-Q exact precision (round-figure forms FORBIDDEN in canonical pins). The `R_1 = 1.1286546` Sage-Q exact value supersedes any `1.128653` round-figure in downstream docs (doc-patch HK-FIRD).
