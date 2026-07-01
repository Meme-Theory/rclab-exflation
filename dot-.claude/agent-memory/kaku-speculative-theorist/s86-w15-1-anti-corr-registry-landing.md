---
name: s86-w15-1-anti-corr-registry-landing
description: S86 W15-1 created project-level correspondence-table-registry.md; entry #30 (Witten 1998 K-theory exclusion) plus sibling cluster #19/#20/#21 form 4-entry string-paradigm-exclusion bloc
type: project
---

# S86 W15-1 — ANTI-CORRESPONDENCE Registry Landing

**Date**: 2026-04-26
**Gate**: `S86-WATCHLIST-W7-ANTI-CORRESPONDENCE-REGISTRY`
**Verdict**: PASS (binary VERIFY (a) AND (b) AND (c) conjunction)
**Artifact**: `sessions/framework/correspondence/correspondence-table-registry.md` (newly created)

## What landed

Entry #30 in a NEW project-level registry at `sessions/framework/correspondence/correspondence-table-registry.md`. Entry #30 documents the 4-obstruction structural exclusion of the Witten 1998 Type IIB K-theoretic D-brane classification scheme as a candidate parent of the substrate's Connes spectral triple. The S85 W10-1 patch had landed §VII.Q in `permanent-results-registry.md`; W15-1 promoted that landing into a new sibling-clusters registry that lives in `sessions/framework/`.

## 4-obstruction vector (substrate vs Witten 1998)

Canonical data lives in `sessions/framework/correspondence/correspondence-table-registry.md` entry #30 (lines 52-59). Per `.claude/rules/agent-standards.md` §"What must NOT live in agent memory" — registry-row data must NOT duplicate into agent memory; this section now points to the canonical source rather than inlining the 4-obstruction-vector table.

The four axes (rank, K_0, Witten integral, Bott-period residue) are algebraically independent K-theoretic invariants — not small-correction perturbations. Substrate-side derivation pointers are at registry lines 65-79; Witten 1998 contrast anchor at lines 81-86.

## Sibling cluster (string-paradigm-exclusion bloc)

#19 no-T-duality (S64)
#20 no-S-duality (S64)
#21 no-Hagedorn (S64)
#30 no-K-theoretic-uplift-to-Witten-1998 (S85 W10-1, registered S86 W15-1)

Together: 4-entry string-paradigm-exclusion bloc. Future cross-paradigm structural-exclusion arguments route through this registry rather than re-deriving the case each time.

## Substrate-framing direction (MANDATORY for all entries)

Direction of explanation: substrate spectral triple FIRST, contrast paradigm SECOND.
- The substrate's K_0, rank, Witten integral, and Bott-period residue are computed FROM the Connes spectral triple's own representation theory (A_F = C + H + M_3(C); SU(3) representation lattice; third spectral moment of D_K; tau_fold parity flip).
- Witten 1998 is a CONTRAST ANCHOR providing the K-theoretic invariants of the Type IIB D-brane scheme.
- DO NOT write "the substrate looks like Witten's scheme except for these four corrections" -- this inverts the explanatory direction.

The registry file's own header (lines 12-24) carries this convention as a mandatory rule for all entries.

## Solution-space implication

The substrate is parent-Witten-1998-EXCLUDED at the K-theoretic level. Per S85 W10-5 (`s85_w10_witten_alternative_parents.py`), at least four parents fail along K-theoretic axes (Witten 1998, heterotic E8 x E8, M-theory C-field, twisted K). The framework remains parent-undetermined at the K-theoretic level but with a 4-parent exclusion ledger.

## Cross-references

- Source patch: `computations/s85_w10_anti_correspondence_30_REGISTRY_PATCH.md`
- Source data: `computations/s85_w10_anti_correspondence_30_registry.json`
- W10-1 verdict line: `computations/s85_gate_verdicts.txt:149`
  - audit_sha256: `e034e19f7fbc3d9642997559ed8fd77c070e98331d07dddbf04405b2c464fddc`
- W15-1 verdict line: `computations/s86_gate_verdicts.txt:235-236`
  - canonical audit_sha256: `f04182f73043e7958ea9e49e82486a58b0306b8661c499f25a5b9e8ad1b10277`
  - companion closure_sha (registry+W10-1+siblings): `5c3813b5a236af9b9b3971b6eae25c34a00c49f0f6c20898e3a49cba42913248`
- Producing script: `computations/s86_w15_anti_correspondence_registry_extension.py`
