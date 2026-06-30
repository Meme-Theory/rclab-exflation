# Investigation 12 — Housekeeping Ledger

**Date**: 2026-06-17 | **Closed by**: `/rclab-coordinate investigation-12-plan-index.md` (full investigation, 4 waves, 18 gates)
**Track-local boundary** (`gate-verdicts.md §"Investigation-Track Canonical Path"`): an investigation CANNOT mutate session-track curated registers (Atlas, falsifier registries, `canonical_constants.py`, `permanent-results-registry.md`). Every register/methodology action below is therefore **routed to session-promotion** at `/rclab-investigate --investigation 12` close (§D), NOT executed in-track. §A records in-investigation process resolutions only.

This ledger follows the §A–E partition of `.claude/templates/session-housekeeping.md`.

## §A — In-session resolutions (completed during the investigation; record only)

- [x] **Plan-typo correction (W1-4)** — the plan cited R_1 = 1.128653; W1-4 computed the canonical 1.1286546 and flagged the typo. Doc-level correction noted in §W1-4; not a register value change (R_1 itself is unchanged and FI-valid).
- [x] **W3-1 cache-path drift corrected at runtime** — the producing script hit plan-text drift on a cache path and resolved it to `computations/session-84/...` per `substrate-first-canonical-sourcing.md §(ii.B)`; disclosed in the W3-1 verdict value string.
- [x] **W3-4 no-op re-dispatch** — the first W3-4 agent went idle without producing any artifact (verified on disk: no script/npz/verdict). Re-dispatched fresh as `w3-4b`, which landed the FAIL verdict + 3/3 artifacts. Process observation: an idle signal is not a completion signal — closure was confirmed by on-disk artifacts, per `agent-standards.md §"Completion Verification"`.
- [x] **W1-1 + W1-5 Option-A supersedes** — both emitted a corrective verdict line carrying `supersedes=<64-hex>` (W1-1 dual-SHA refactor; W1-5 print-helper byte change, physics unchanged). sig_5 verified unique across the whole verdict file. No remediation needed (correct discipline).

## §B — Hygiene compute carry-forwards (Q2 mechanical re-run)

None. The investigation's genuine future computes are first-class math carry-forwards (CF-INV12-W3-A greybody-resonance scan; CF-INV12-W4-B Krein-modular-pairing-sign ladder; CF-INV12-W2-A FWD-C1 families-index, consolidated into W4-B), recorded in the per-wave WP `## Carry-Forward Computations` sections — NOT hygiene re-runs.

## §C — Parallel-compute-wave carry-forwards (Q3 wave-together)

None.

## §D — Register / methodology reconciliations routed to session-promotion

These require mutating session-track curated registers and so CANNOT be effected in-track. They are lifted by `/rclab-investigate --investigation 12` → a session-mode `/rclab-plan` for the promoting session.

- [ ] **CF23 prose split (atlas-08-open-questions.md)** — split the single "A_s 3.02× permanent structural-position wall" bullet into (a) FLOOR `A_s ≥ A_s^{BD}` (PERMANENT, 3-axis confirmed: reference-state W1-2 / families-index W2-5 / dynamical W3) and (b) MAGNITUDE + upper-edge FILTER (SCHEME-DEPENDENT, OPEN). Q3 capstone-hygiene status-change; designated register writer; reviewed patch, NOT bulk append. Source: W4-3 synthesis §V.
- [ ] **falsifier-rigor-registry A_s Row 8 floor-confirmation sub-annotation** — keep the SCHEME-DEPENDENT tag for the magnitude; add that the FLOOR (sign) is FUNCTIONAL-INDEPENDENT/PERMANENT on three orthogonal axes. Sole writer `mack-cosmic-bridge` (`feedback_mack-bridge-role.md`).
- [ ] **atlas-04 S3 re-tag** ("SA = correct modulus effective action" ASSUMED) — re-tag is the register consequence of CF-INV12-W4-B (Krein-modular-pairing-sign) PASS, not of the W4-2 workshop itself. Gated on that gate.
- [ ] **HY1 / HY2 (W1-4-gated)** — HY1 FI/RD manifest authoring; HY2 a_2^ζ≡a_2^SDW label disambiguation (W1-4 PASS established HARMLESS_ALIAS, so HY2 is a label cleanup, not a re-derivation).
- [ ] **HY6 (W2-2)** — a_n pole-status registry-lift (the per-moment pole-convergence ledger) to the appropriate register.
- [ ] **S69 W5-G → STRUCTURAL-THEOREM promotion (W2-3)** — BdG-dressing K-homology invariance promoted per-case → structural theorem; register the promotion in `permanent-results-registry.md` via the joint-theorem pathway at session-promotion.
- [ ] **W3-3 STRUCTURAL THEOREM** — dq/da ∝ −(n₁−n₂)² ≤ 0 (two diluting fluids ⇒ monotone-non-increasing q), establishing relic-Friedmann q ≠ SCALE-FACTOR-54 Connes-distance-proxy q (sharpens S95-W4-4). Registration candidate at session-promotion.
- [ ] **FWD-C1 slot landing (W2-5)** — record the §VII FWD-C1 slot as `REGISTRY-INCOMPLETE-PENDING-OPERATIONAL-ALIGNMENT` (η-form ≡ 0 Level-1 identity; Level-2 NON-BINDING) at session-promotion, with CF-INV12-W2-A/W4-B as the refinement-pathway forward gate.

## §E — Pre-compute shell waves (escalation)

None. All 4 waves executed; all 15 compute/solo gates landed verdicts; all 3 W4 review/workshop gates closed by artifact-existence.

## Closeout

18/18 gates complete and verified on disk. Compute verdicts: 7 PASS / 2 FAIL / 3 INFO (W1: 2P/2F/1I; W2: 4P/1I; W3: 2P/1F/2I — counting the foundational W3-1). W4: 2 workshops + 1 review closed by artifact-existence. sig_5 unique across `computations/investigation-12/inv12_gate_verdicts.txt`. Next pipeline step is the USER's call (`/rclab-investigate --investigation 12`), not an orchestrator recommendation.
