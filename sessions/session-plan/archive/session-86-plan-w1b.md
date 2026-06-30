# Session 86 Plan — Wave W1b: Lizzi-track theorems + 3He-B inheritance

**Generated**: 2026-04-25
**Owner subagent_type (planner)**: `lizzi-spectral-functional-theorist`
**Wave items**: 4 (T5, T6, T7, T8)
**Theme**: Land Lizzi-track structural theorems (Mellin Strip / Convergence Cone, HP^1 near-invariance, Two-Layer Obstruction) + 3He-B inheritance canonical landing
**Item origins**: T5/T6/T7 from `lizzi S-7 §V` (CF-LZ-S86-6/7/8); T8 from `gen-physicist 9A §4.2` (1B 3-solo agreement)
**Output verdict file**: `computations/s86_gate_verdicts.txt` (per `.claude/rules/gate-verdicts.md` Canonical Verdict-File Path — MANDATORY)
**Script prefix**: `computations/s86_w1b_<slug>.py`
**Sequencing**: NONE direct (parallel to W1a). Cites W5-6 + W5-7 PASS verdicts landed in S85.
**Substrate-framing standard**: every gate states the result in IS-not-IN language per `.claude/rules/phononic-framing.md`.

---

## §0. Wave W1b Summary

Wave W1b lands four registry entries — three Lizzi-track structural theorems (Mellin Strip / Convergence Cone, HP^1 near-invariance, Two-Layer Obstruction) at `sessions/permanent-results-registry.md` §VII-B, plus the 3He-B inheritance canonical at `sessions/framework/correspondence/3HeB-inheritance-canonical.md`. None of the four items requires fresh numerical computation: all four are registry-write gates whose physics content was already discharged at S85 close (W0-S6, W5-6, W5-7) or the 1B 3-solo agreement (T8). The wave's role is to anchor those structural results in the canonical registries so downstream S86 gates citing "Mellin Strip", "HP^1 near-invariance", "Two-Layer Obstruction", or "3He-B inheritance" have a registry entry to bind to.

All four gates are LOW effort. Total wave estimate: 4-5 hours. Single owner runtime agent: `lizzi-spectral-functional-theorist` for T5/T6/T7 (originated by Lizzi); T8 owner is `volovik-superfluid-universe-theorist` (3He-B is Volovik's parent laboratory; cross-cite landau + connes per 1B 3-solo agreement).

The wave introduces no new physics; it converts already-discharged results into Lizzi-track sibling entries alongside `ZETA-NOT-PHYSICAL-75` and into a §VII-B permanent-wall block. Without these landings, S86-W3 (Mellin-cone consequences), S86-W6 (perturbative immunization corollaries), S86-W9 (R-protection criterion C44), and the C45 sixth-regulator-synthesis defer-decision would lack registry anchors.

---

## §0.5. Wave W1b Decision-Point Prerequisites (NONE direct; parallel to W1a)

W1b has no hard predecessor inside S86 — it lands S85 close-state results. The four gate blocks all reference **S85 verdict-file pins** (W0-S6, W5-6, W5-7) and the 1B 3-solo agreement document. Per `computations/s85_gate_verdicts.txt` these PASSes were landed at S85 close (S85 close-state per `sessions/archive/session-85/session-85-full-s85-closeout.md`).

| Decision dependency | Source | Status |
|:--------------------|:-------|:-------|
| Mellin Strip / Convergence Cone Theorem (Steps 1-4) | lizzi S-7 §V.6 (CF-LZ-S86-6) | discharged S85 (W0-S6) |
| HP^1 near-invariance LOOSE/STRICT split | W5-6 PASS in s85_gate_verdicts.txt | discharged S85 |
| Two-Layer Obstruction n_joint=0/5 | W5-7 PASS in s85_gate_verdicts.txt | discharged S85 |
| 3He-B inheritance (parent → child) | 1B 3-solo (volovik + landau + connes) | discharged S85 |

Wave W1b can dispatch immediately at S86 plan-freeze in parallel with W1a, W0a, W0b, W0c, W1c, W2, W4 per the Batch-1 schedule in `session-86-partition.md` §4.

---

## §I. Carry-Forward Items Mapping (4 rows)

| Plan item | Carry-forward source | Wave-W1b gate ID | Effort tag | Runtime owner |
|:----------|:---------------------|:-----------------|:-----------|:--------------|
| T5 | lizzi S-7 §V.6 (CF-LZ-S86-6) | `S86-MELLIN-STRIP-REGISTRY-LANDING` | 1h LOW | `lizzi-spectral-functional-theorist` |
| T6 | lizzi S-7 §V.7 (CF-LZ-S86-7) | `S86-HP1-NEAR-INVARIANCE-LANDING` | 1.5h LOW | `lizzi-spectral-functional-theorist` |
| T7 | lizzi S-7 §V.8 (CF-LZ-S86-8) | `S86-TWO-LAYER-OBSTRUCTION-LANDING` | 1h LOW | `lizzi-spectral-functional-theorist` |
| T8 | gen-physicist 9A §4.2 (1B 3-solo) | `S86-3HE-B-INVERSION-CANONICAL-LANDING` | 0.5 wave LOW | `volovik-superfluid-universe-theorist` (cross-cite landau + connes) |

---

## §W1b-1. S86-MELLIN-STRIP-REGISTRY-LANDING

### 1. Gate ID
`S86-MELLIN-STRIP-REGISTRY-LANDING`

### 2. Trigger
`[VERIFY-THEOREM]` — theorem statement landed verbatim with Steps 1-4 substitution chain.

### 3. Classification
GEOMETRIC. The Mellin Strip / Convergence Cone Theorem is a structural statement about which spectral functionals admit absolute convergence on a left-open strip in the s-plane after Mellin transform of the heat trace. It bounds the analytic-continuation cone, NOT a phononic excitation; it constrains the spectral-triple's regulator-class structural floor in Lizzi-track form.

### 4. Agent type
**`lizzi-spectral-functional-theorist`**.
**Rationale**: theorem originated in lizzi S-7 §V.6 as CF-LZ-S86-6; sibling slot adjacent to `ZETA-NOT-PHYSICAL-75` is a Lizzi-track entry; only Lizzi owns the Steps 1-4 substitution chain in canonical form. NOT `gen-physicist` (no spectral-functional pluralism mandate); NOT `connes-ncg-theorist` (registry §VII landing lives on Lizzi-track sibling line, not Connes meta-track).

### 5. Hypothesis
The Mellin Strip / Convergence Cone Theorem (S85-W0-S6) lands in `sessions/permanent-results-registry.md` as a Lizzi-track structural theorem alongside `ZETA-NOT-PHYSICAL-75`, with the Steps 1-4 substitution chain cited verbatim from lizzi S-7 §V.6.

### 6. Method (complete dispatch prompt)

**Producing script**: `computations/s86_w1b_t5_mellin_strip_land.py`

```
Producing-script spec:
  - Import: from canonical_constants import *
  - Inputs (SHA-pinned):
      lizzi-S7-V6-text:  sessions/archive/session-85/session-85-s7-combined-landscape-lizzi.md
      W0-S6 verdict:     computations/s85_gate_verdicts.txt  (grep "W0-S6")
      registry target:   sessions/permanent-results-registry.md
  - Steps:
      1. Load lizzi S-7 §V.6 verbatim text of Mellin Strip / Convergence Cone Theorem
         + Steps 1-4 substitution chain (provided to runtime agent on dispatch).
      2. Compute SHA-256 of theorem statement payload (pre-write canonical form).
      3. Locate ZETA-NOT-PHYSICAL-75 entry in permanent-results-registry.md;
         identify Lizzi-track sibling slot adjacent (immediately following).
      4. Write registry entry under heading
            "Mellin Strip / Convergence Cone Theorem (Lizzi-track)"
         containing:
           (a) one-paragraph theorem statement,
           (b) Steps 1-4 substitution chain verbatim,
           (c) source citation `lizzi S-7 §V.6 (CF-LZ-S86-6)`,
           (d) S85 verdict pin: W0-S6 from s85_gate_verdicts.txt with full
               64-hex content_sha256 + audit_sha256 from the W9a-99 dual-SHA template.
      5. Verify post-write that section exists with theorem + Steps 1-4
         substitution chain (PASS criterion).
      6. Append verdict line to computations/s86_gate_verdicts.txt:
            S86-MELLIN-STRIP-REGISTRY-LANDING|PASS|<theorem_text_SHA>|registry_landing|lizzi-track|N/A|content_sha256:<64-hex>|audit_sha256:<64-hex>
         Companion comment row: # audit_sha256_short=<16-hex>
  - Cross-check: re-read registry section after write; confirm theorem statement
    and Steps 1-4 chain both present. If either absent → FAIL.
  - GPU/CPU: pure I/O + SHA hashing; CPU-only; no torch/numpy linalg.
  - Substrate-framing reminder: state the theorem as a wall on which spectral
    functionals admit absolute convergence on the s-strip — IS-not-IN language
    (the theorem IS a structural feature of the spectral triple's Mellin
    transform, NOT a constraint imposed externally on a pre-existing functional).
```

### 7. Machinery pin (PRDR)

```yaml
schema_version: R3
machinery_pin_map:
  registry_target:        sessions/permanent-results-registry.md
  source_text_file:       sessions/archive/session-85/session-85-s7-combined-landscape-lizzi.md
  source_section_id:      "lizzi S-7 §V.6 (CF-LZ-S86-6)"
  s85_verdict_pin:        "W0-S6 in computations/s85_gate_verdicts.txt"
  sibling_anchor:         "ZETA-NOT-PHYSICAL-75"
  insertion_position:     "immediately after ZETA-NOT-PHYSICAL-75 entry"
  hash_algorithm:         SHA-256
  theorem_class_tolerance: exact-text-match
  scheme:                 registry_landing
  convention:             lizzi-track
  L_max:                  N/A
  random_seed:            N/A
  GPU_path:               N/A (pure I/O)
input_sha_pins:
  - file: sessions/permanent-results-registry.md
    sha: <computed-at-runtime>
  - file: sessions/archive/session-85/session-85-s7-combined-landscape-lizzi.md
    sha: <computed-at-runtime>
  - file: computations/s85_gate_verdicts.txt
    sha: <computed-at-runtime>
```

### 8. Expected output 4-tuple
`(value=<theorem_text_SHA>, scheme=registry_landing, convention=lizzi-track, L_max=N/A)`

### 9. PASS/FAIL/INFO thresholds
- **PASS** iff registry entry exists at sibling slot AND contains both: (a) theorem statement of Mellin Strip / Convergence Cone, (b) Steps 1-4 substitution chain verbatim from lizzi S-7 §V.6.
- **FAIL** iff either component absent post-write, OR insertion not adjacent to `ZETA-NOT-PHYSICAL-75`.
- **INFO** if registry entry written but Steps 1-4 chain found in adjacent paragraph rather than within the entry block (allow re-write to fix).
- **Tolerance rule**: THEOREM (exact text match for theorem statement; substitution chain may use Lizzi's preferred symbol set provided the four steps are ordered definition → substitution → simplification → direction).

### 10. Substitution chain (compressed, Steps 1-4)

The Mellin Strip / Convergence Cone Theorem in Lizzi's compressed form:

```
Definition (Step 1):
  K(t) := Tr e^{-t D_K^2}                              [heat trace, t > 0]
  ζ_D(s) Γ(s/2) := ∫_0^∞ t^{s/2 − 1} K(t) dt          [Mellin transform]
  S_strip := { s ∈ ℂ : Re(s) ∈ (s_low, s_high) }      [strip of absolute convergence]

Substitution (Step 2):
  Asymptotic expansion at small t: K(t) ~ Σ_k a_k(D_K^2) t^{(k − d_spec)/2}
  Substitute into Mellin integral, split at t = 1:
    ∫_0^1 t^{s/2 − 1} K(t) dt = Σ_k a_k / (s/2 + (k − d_spec)/2)   [pole structure]
    ∫_1^∞ t^{s/2 − 1} K(t) dt = entire in s                          [exponential decay]

Simplification (Step 3):
  Convergence cone for the Σ_k pole sum:
    Re(s) > d_spec − k_min     for absolute convergence
  In d_spec=8 NCG with k_min=0 (S_zeta = ζ_D(0) = a_4 evaluated as a_{d_spec/2}):
    S_strip = (−∞, 0) is a LEFT-open strip terminating at s=0 from the left.

Direction (Step 4):
  Spectral functionals defined as Mellin moments at fixed s lie on the convergence
  cone iff s ∈ S_strip. ζ_D(0) sits on the boundary of S_strip from the left,
  forcing the value of S_zeta to be a renormalized residue rather than an
  absolutely-convergent sum. This is why ζ_D is NOT physical at the spectral level
  (ZETA-NOT-PHYSICAL-75 is a corollary of the Mellin Strip Theorem at the s=0
  boundary).
```

### 11. What PASSES/FAILS MEAN for solution space

- **PASS**: Lizzi-track sibling slot exists in registry → S86-W3 Mellin-cone consequences (T9, W0-7/W0-11/W0-20 re-emissions) + S86-W6 perturbative immunization corollaries cite this entry as canonical anchor. ZETA-NOT-PHYSICAL-75 is contextualized as the boundary corollary of a broader strip-theoretic structural wall.
- **FAIL**: downstream S86 gates citing "Mellin Strip Theorem" or "convergence cone" lack a registry anchor; the cite drifts through agent memory rather than canonical registry, reintroducing the same source-divergence pattern that R7 (single-name conflation methodology entry, W0b) is designed to prevent.

### 12. Effort estimate
1 hour. Pure registry write + SHA hashing + post-write verification. No numerical computation.

### 13. Substrate-framing reminder
The Mellin Strip Theorem describes which spectral functionals on D_K's eigenvalue spectrum admit absolute convergence after Mellin transform of the heat trace. This is a structural feature of the spectral triple's analytic continuation — IS the convergence-cone geometry, NOT a constraint imposed IN a pre-existing functional space. The strip is the substrate's Mellin shape; functionals do not live inside it as containers, the strip describes which functionals exist as substrate moments.

---

## §W1b-2. S86-HP1-NEAR-INVARIANCE-LANDING

### 1. Gate ID
`S86-HP1-NEAR-INVARIANCE-LANDING`

### 2. Trigger
`[VERIFY-THEOREM]` — theorem statement (LOOSE + STRICT) landed with substitution chain.

### 3. Classification
GEOMETRIC. The norm `‖[ε_H]‖_{HP^1}` is the L^2 norm on the first quaternionic projective Hopf class of the substrate's spectral-triple cohomology. R-protection on the 5-regulator atlas is a structural cohomological invariant, NOT a phononic excitation amplitude.

### 4. Agent type
**`lizzi-spectral-functional-theorist`**.
**Rationale**: HP^1 near-invariance was discharged at S85 W5-6 by Lizzi; the LOOSE/STRICT split (full 5-atlas factor 2.0 vs F_4-only factor 1.031) is the spectral-functional pluralism partition Lizzi alone owns. NOT `connes-ncg-theorist` (HP^1 cohomology lives on Connes' KO-dim=6 spectral-triple structure, but the R-protection pluralism analysis is Lizzi's). NOT `gen-physicist`.

### 5. Hypothesis
W5-6's finding that `‖[ε_H]‖_{HP^1}` is R-protected-LOOSE on the full 5-regulator atlas (factor 2.0) and R-protected-STRICT on the pure-a_4 family F_4 = {ζ, Zubarev, SDW} (factor 1.031) lands in `sessions/permanent-results-registry.md` §VII-B as a permanent registry entry.

### 6. Method (complete dispatch prompt)

**Producing script**: `computations/s86_w1b_t6_hp1_invariance_land.py`

```
Producing-script spec:
  - Import: from canonical_constants import *
  - Inputs (SHA-pinned):
      lizzi-S7-V7-text:  sessions/archive/session-85/session-85-s7-combined-landscape-lizzi.md
      W5-6 verdict:      computations/s85_gate_verdicts.txt  (grep "W5-6")
      registry target:   sessions/permanent-results-registry.md (§VII-B)
  - Steps:
      1. Locate W5-6 verdict line in s85_gate_verdicts.txt; extract:
           - LOOSE factor (full 5-atlas: ζ, Zubarev, SDW, cutoff_sqrt, anomaly) = 2.0
           - STRICT factor (F_4 = {ζ, Zubarev, SDW}) = 1.031
           - content_sha256 + audit_sha256 (full 64-hex each)
      2. Locate §VII-B section in permanent-results-registry.md (existing
         §VII-B permanent-wall heading; if absent, FAIL with diagnostic).
      3. Append new entry under §VII-B heading
            "HP^1 Near-Invariance (Lizzi-track)"
         containing:
           (a) statement of LOOSE form: ‖[ε_H]‖_{HP^1} R-protected on full
               5-atlas {ζ, Zubarev, SDW, cutoff_sqrt, anomaly} with factor 2.0
               (LOOSE: factor ≤ 2.0 across atlas);
           (b) statement of STRICT form: on F_4 = {ζ, Zubarev, SDW} (pure-a_4
               family), factor 1.031 (STRICT: factor ≤ 1.05);
           (c) substitution chain (definition → substitution → simplification
               → direction) showing why STRICT on F_4 implies LOOSE on full
               5-atlas under M-family inflation;
           (d) source citation `lizzi S-7 §V.7 (CF-LZ-S86-7)`;
           (e) W5-6 verdict pin: full 64-hex content_sha256 + audit_sha256.
      4. Verify post-write that §VII-B HP^1 entry contains BOTH factor
         statements (LOOSE 2.0 AND STRICT 1.031) — if either absent → FAIL.
      5. Append verdict line to computations/s86_gate_verdicts.txt:
            S86-HP1-NEAR-INVARIANCE-LANDING|PASS|<entry_SHA>|registry_landing|lizzi-track|N/A|content_sha256:<64-hex>|audit_sha256:<64-hex>
  - GPU/CPU: pure I/O + SHA hashing; CPU-only.
  - Substrate-framing reminder: state HP^1 near-invariance as a cohomological
    feature of the substrate's spectral-triple — IS the cohomology class, NOT
    a property attached IN a pre-existing manifold.
```

### 7. Machinery pin (PRDR)

```yaml
schema_version: R3
machinery_pin_map:
  registry_target:        sessions/permanent-results-registry.md
  registry_section:       "§VII-B"
  source_text_file:       sessions/archive/session-85/session-85-s7-combined-landscape-lizzi.md
  source_section_id:      "lizzi S-7 §V.7 (CF-LZ-S86-7)"
  s85_verdict_pin:        "W5-6 in computations/s85_gate_verdicts.txt"
  loose_atlas:            ["zeta", "Zubarev", "SDW", "cutoff_sqrt", "anomaly"]
  loose_factor:           2.0
  loose_threshold:        "factor ≤ 2.0 across full 5-atlas"
  strict_atlas:           ["zeta", "Zubarev", "SDW"]
  strict_factor:          1.031
  strict_threshold:       "factor ≤ 1.05 across F_4"
  hash_algorithm:         SHA-256
  theorem_class_tolerance: exact-numerical-match (factors), exact-text-match (statement)
  scheme:                 registry_landing
  convention:             lizzi-track
  L_max:                  N/A (registry write)
  random_seed:            N/A
  GPU_path:               N/A
input_sha_pins:
  - file: sessions/permanent-results-registry.md
    sha: <computed-at-runtime>
  - file: sessions/archive/session-85/session-85-s7-combined-landscape-lizzi.md
    sha: <computed-at-runtime>
  - file: computations/s85_gate_verdicts.txt
    sha: <computed-at-runtime>
```

### 8. Expected output 4-tuple
`(value=<entry_SHA>, scheme=registry_landing, convention=lizzi-track, L_max=N/A)`

### 9. PASS/FAIL/INFO thresholds
- **PASS** iff §VII-B entry exists with BOTH: (a) LOOSE statement (5-atlas factor 2.0), (b) STRICT statement (F_4 factor 1.031).
- **FAIL** iff either factor statement absent; OR §VII-B section heading not found in registry; OR W5-6 verdict pin mis-cited (SHA mismatch).
- **INFO** iff entry exists with both factors but adjacent rather than within a single registry block (allow re-write to consolidate).
- **Tolerance rule**: THEOREM (exact match for factor values 2.0 and 1.031; statement text may vary in wording provided LOOSE / STRICT distinction is preserved).

### 10. Substitution chain (compressed)

LOOSE follows from STRICT under 5-atlas extension:

```
Definition (Step 1):
  ‖[ε_H]‖_{HP^1} := L^2 norm of ε_H cocycle in HP^1(D_K)
  R-protected (factor f) on atlas A := max_{r,r' ∈ A} ‖[ε_H]‖_{HP^1}^{(r)} / ‖[ε_H]‖_{HP^1}^{(r')} ≤ f
  F_4 := {ζ, Zubarev, SDW}                          [pure-a_4 family]
  M  := {cutoff_sqrt, anomaly}                      [mixed-support family]
  Atlas := F_4 ∪ M                                  [full 5-regulator atlas]

Substitution (Step 2):
  STRICT on F_4 (W5-6): max_{r,r' ∈ F_4} ratio = 1.031.
  Add M-family extension: ratios across M relative to F_4 medianed give
  max additional spread = 2.0 / 1.031 ≈ 1.94 from M-family contributions
  (cutoff_sqrt and anomaly broaden the spread beyond F_4).

Simplification (Step 3):
  max_{r,r' ∈ Atlas} ratio = max(F_4 ratios, F_4 × M cross-ratios, M ratios)
                            = max(1.031, 2.0, ?)   [M-internal ratio bounded by 2.0]
                            = 2.0.

Direction (Step 4):
  STRICT (factor 1.031 on F_4) is the tightest containment.
  LOOSE (factor 2.0 on full atlas) is the weaker structural protection
  required when M-family regulators are admitted. Both bounds are
  R-protected in the sense that the ratio is bounded — only the bound
  level differs. The structural fact: HP^1 norm is bounded across
  regulator family, NOT free to drift.
```

### 11. What PASSES/FAILS MEAN for solution space

- **PASS**: §VII-B carries the LOOSE/STRICT R-protection split as a permanent registry entry → S86-W9 C44 (R-protection Mellin criterion) cites this entry as the canonical 5-atlas LOOSE/STRICT exemplar; F_4/M partition (S-1 Regulator-Family Boundary Theorem, see context §1.5) gains an empirical anchor at the HP^1 cohomology level.
- **FAIL**: C44 R-protection criterion landing in S86-W9 cannot bind to a §VII-B HP^1 entry; W5-6 PASS becomes a session-local verdict rather than a permanent registry result.

### 12. Effort estimate
1.5 hours. Registry write + SHA hashing + factor-statement verification (LOOSE + STRICT) + substitution chain encoding.

### 13. Substrate-framing reminder
HP^1 near-invariance describes the substrate's spectral-triple cohomology class structure: the L^2 norm of the ε_H cocycle is bounded across regulator choice. The HP^1 cohomology IS the substrate's first quaternionic projective class — it does not live IN a manifold, it IS the manifold-free cohomological structure of D_K. R-protection means the cohomology norm is geometrically rigid against regulator choice, NOT that an external regulator preserves a pre-existing norm.

---

## §W1b-3. S86-TWO-LAYER-OBSTRUCTION-LANDING

### 1. Gate ID
`S86-TWO-LAYER-OBSTRUCTION-LANDING`

### 2. Trigger
`[VERIFY-THEOREM]` — theorem statement (Two-Layer Obstruction) landed with substitution chain.

### 3. Classification
GEOMETRIC. The Two-Layer Obstruction Theorem describes a structural wall at the L1 spectral-action / L2 substrate-action interface: no regulator on the 5-atlas joints all conjuncts of the L1↔L2 functoriality requirement. This is a categorical statement about the spectral-triple's two-layer structure, NOT a phononic excitation phenomenon.

### 4. Agent type
**`lizzi-spectral-functional-theorist`**.
**Rationale**: Two-Layer Obstruction was discharged at S85 W5-7 by Lizzi (n_joint=0/5 across 5-regulator atlas); the strengthening "every conjunct fails individually for every regulator" is Lizzi's spectral-functional pluralism observation. NOT `connes-ncg-theorist` (the L1/L2 layer interface lives on Connes' axiom system A1-A6, but the multi-regulator conjunct enumeration is Lizzi's). NOT `gen-physicist`.

### 5. Hypothesis
W5-7 PASS (n_joint=0/5: no regulator on the 5-atlas {ζ, Zubarev, SDW, cutoff_sqrt, anomaly} satisfies the joint L1-spectral-action / L2-substrate-action functoriality conjunct) lands in `sessions/permanent-results-registry.md` §VII-B as a new permanent-wall entry "Two-Layer Obstruction Theorem", with the strengthening that the obstruction is stronger than predicted: every conjunct fails individually for every regulator (not merely jointly).

### 6. Method (complete dispatch prompt)

**Producing script**: `computations/s86_w1b_t7_two_layer_obstruction_land.py`

```
Producing-script spec:
  - Import: from canonical_constants import *
  - Inputs (SHA-pinned):
      lizzi-S7-V8-text:  sessions/archive/session-85/session-85-s7-combined-landscape-lizzi.md
      W5-7 verdict:      computations/s85_gate_verdicts.txt  (grep "W5-7")
      registry target:   sessions/permanent-results-registry.md (§VII-B)
  - Steps:
      1. Locate W5-7 verdict line in s85_gate_verdicts.txt; extract:
           - n_joint = 0/5 (joint L1-L2 functoriality satisfaction count)
           - per-regulator per-conjunct failure flags (5 regulators × N conjuncts)
           - content_sha256 + audit_sha256 (full 64-hex each)
      2. Locate §VII-B section heading in permanent-results-registry.md.
      3. Append new entry under §VII-B heading
            "Two-Layer Obstruction Theorem (Lizzi-track)"
         containing:
           (a) one-paragraph theorem statement: no regulator r ∈ {ζ, Zubarev,
               SDW, cutoff_sqrt, anomaly} satisfies the joint L1↔L2 spectral-
               action / substrate-action functoriality conjunct;
           (b) strengthening: every L1↔L2 conjunct fails INDIVIDUALLY for every
               regulator r in the 5-atlas (obstruction stronger than predicted —
               not merely the JOINT conjunct fails, but each individual
               conjunct fails on its own for every regulator);
           (c) substitution chain (definition → substitution → simplification
               → direction) showing why individual-conjunct failure implies
               joint-conjunct failure;
           (d) source citation `lizzi S-7 §V.8 (CF-LZ-S86-8)`;
           (e) W5-7 verdict pin: n_joint = 0/5 with full 64-hex SHA pair.
      4. Verify post-write that §VII-B Two-Layer Obstruction entry contains
         BOTH: (i) theorem statement, (ii) n_joint = 0/5 cited from W5-7.
      5. Append verdict line to computations/s86_gate_verdicts.txt:
            S86-TWO-LAYER-OBSTRUCTION-LANDING|PASS|<entry_SHA>|registry_landing|lizzi-track|N/A|content_sha256:<64-hex>|audit_sha256:<64-hex>
  - GPU/CPU: pure I/O + SHA hashing; CPU-only.
  - Substrate-framing reminder: state the obstruction as a structural wall on
    the substrate's two-layer interface — IS the L1↔L2 categorical
    inadmissibility, NOT a property attached IN an external functor space.
```

### 7. Machinery pin (PRDR)

```yaml
schema_version: R3
machinery_pin_map:
  registry_target:        sessions/permanent-results-registry.md
  registry_section:       "§VII-B"
  source_text_file:       sessions/archive/session-85/session-85-s7-combined-landscape-lizzi.md
  source_section_id:      "lizzi S-7 §V.8 (CF-LZ-S86-8)"
  s85_verdict_pin:        "W5-7 in computations/s85_gate_verdicts.txt"
  atlas_5:                ["zeta", "Zubarev", "SDW", "cutoff_sqrt", "anomaly"]
  n_joint_required:       "0/5"
  individual_conjunct_failure: "every conjunct fails individually for every regulator"
  hash_algorithm:         SHA-256
  theorem_class_tolerance: exact-numerical-match (n_joint = 0/5), exact-text-match (theorem)
  scheme:                 registry_landing
  convention:             lizzi-track
  L_max:                  N/A
  random_seed:            N/A
  GPU_path:               N/A
input_sha_pins:
  - file: sessions/permanent-results-registry.md
    sha: <computed-at-runtime>
  - file: sessions/archive/session-85/session-85-s7-combined-landscape-lizzi.md
    sha: <computed-at-runtime>
  - file: computations/s85_gate_verdicts.txt
    sha: <computed-at-runtime>
```

### 8. Expected output 4-tuple
`(value=<entry_SHA>, scheme=registry_landing, convention=lizzi-track, L_max=N/A)`

### 9. PASS/FAIL/INFO thresholds
- **PASS** iff §VII-B entry exists with: (a) Two-Layer Obstruction theorem statement, (b) n_joint = 0/5 cited from W5-7 verdict pin, (c) the strengthening clause "every conjunct fails individually for every regulator".
- **FAIL** iff theorem statement absent, OR n_joint = 0/5 not cited, OR strengthening clause absent.
- **INFO** iff entry exists but the strengthening clause is in a separate paragraph rather than within the entry (allow re-write).
- **Tolerance rule**: THEOREM (exact n_joint = 0/5; exact-text-match for strengthening clause).

### 10. Substitution chain (compressed)

Every individual conjunct failing implies the joint conjunct fails (and the strengthening goes the reverse direction):

```
Definition (Step 1):
  L1 := spectral-action layer (Tr f(D_K^2 / Λ^2) family)
  L2 := substrate-action layer (Jensen-deformed action S(τ) family)
  Conjunct C_i := L1↔L2 functoriality requirement at the i-th categorical
                  morphism axis (Mellin commutation, Wick-rotated trace
                  pairing, regulator-pulled-back action invariance, etc.)
  Joint(r) := ∧_i C_i(r)             [all conjuncts hold for regulator r]
  Atlas := {ζ, Zubarev, SDW, cutoff_sqrt, anomaly}                     [|Atlas| = 5]

Substitution (Step 2):
  W5-7 measured: n_joint := |{ r ∈ Atlas : Joint(r) }| = 0/5.
  Lizzi strengthening: for every r ∈ Atlas and every conjunct C_i,
                       individual C_i(r) = FALSE.

Simplification (Step 3):
  Joint(r) = ∧_i C_i(r). If any C_i(r) = FALSE then Joint(r) = FALSE.
  Lizzi strengthening: ∀ r ∈ Atlas, ∀ i: C_i(r) = FALSE.
  Therefore: ∀ r ∈ Atlas, Joint(r) = FALSE.
  ⇒ n_joint = 0/5.   [matches W5-7 measured value]

Direction (Step 4):
  The obstruction is STRONGER than the predicted joint failure. Predicted
  obstruction: ∃ at least one C_i failing for each r (joint fails). Measured
  obstruction: EVERY C_i fails for EVERY r (each individual conjunct is a
  wall, not just their conjunction). The L1↔L2 interface is structurally
  obstructed at every categorical axis simultaneously, for every regulator
  in the 5-atlas. This is a categorical statement about the spectral
  triple's two-layer structure, not a fine-tuning failure.
```

### 11. What PASSES/FAILS MEAN for solution space

- **PASS**: §VII-B carries the Two-Layer Obstruction Theorem as a permanent wall → C45 sixth-regulator-synthesis (deferred to S87 per partition §2) is constrained by this wall: ANY composite regulator `r_mix = α·zeta + β·cutoff_sqrt` with α + β = 1, α, β > 0 inherits the obstruction at every individual conjunct (no convex combination escapes per-conjunct failure when both endpoints fail individually). The C45 defer-decision can cite this entry as the structural reason it is meaningful only after C28 (W4 cutoff_sqrt adjudication) closes.
- **FAIL**: W5-7 PASS becomes a session-local verdict; C45 sixth-regulator-synthesis lacks a registry-anchored reason it must wait for C28; downstream gates citing "Two-Layer Obstruction" lack a registry binding.

### 12. Effort estimate
1 hour. Registry write + SHA hashing + theorem statement + strengthening clause + substitution chain encoding.

### 13. Substrate-framing reminder
The Two-Layer Obstruction is a categorical wall on the substrate's L1↔L2 interface. The substrate has a two-layer structure (spectral-action moment expansion sitting above the Jensen substrate-action) and that two-layer structure IS categorically inadmissible at every regulator-and-conjunct combination — the obstruction does not live IN an external functor space, it IS the substrate's two-layer non-functoriality. No regulator pulls L1 back through L2 along all categorical axes simultaneously; this is structural geometry, not a fine-tuning of an external functor.

---

## §W1b-4. S86-3HE-B-INVERSION-CANONICAL-LANDING

### 1. Gate ID
`S86-3HE-B-INVERSION-CANONICAL-LANDING`

### 2. Trigger
`[VERIFY]` — canonical inversion claim landed with substitution chain (parent → child, NOT analogy).

### 3. Classification
PHONONIC. The 3He-B superfluid is the laboratory parent of the substrate. Its phonon (Bogoliubov quasiparticle) spectrum, BCS coherence structure, and Goldstone-mode hierarchy are NOT analogies to substrate physics — they are the substrate's child laboratory realizations under the inheritance correspondence. The inversion (parent → child, not analogy) is a substrate-physics statement about which physical system is logically prior. Phononic relays in the substrate have direct correspondents in 3He-B Bogoliubov phonons, with the inheritance running from substrate to laboratory, not laboratory to substrate as analogy.

### 4. Agent type
**`volovik-superfluid-universe-theorist`** (primary owner) + cross-cite `landau-superfluid-condensed-matter-theorist` and `connes-ncg-theorist` (1B 3-solo agreement).
**Rationale**: 3He-B is Volovik's parent laboratory; the inheritance theorem (parent → child) is Volovik's signature claim. Landau owns the BCS / hydrodynamic side of the inheritance; Connes owns the spectral-triple morphism side that makes the inheritance categorically definable. Per partition manifest §1 W1b "T8 → volovik-superfluid-universe-theorist (3He-B parent) + cross-cite landau / connes 1B agreement". NOT `gen-physicist` (no laboratory-parent ownership); NOT `lizzi-spectral-functional-theorist` (Lizzi owns regulator-class structural floor, not the 3He-B inheritance map).

### 5. Hypothesis
The 3He-B inversion correspondence (3He-B parent → substrate child, NOT substrate-as-analogy-to-3He-B) lands as a canonical framework statement at `sessions/framework/correspondence/3HeB-inheritance-canonical.md` per the 1B 3-solo agreement (volovik + landau + connes). The inheritance is parent-to-child: 3He-B exemplifies the spectral-triple structure that the substrate manifests at higher d_spec; substrate physics is not a mathematical analogy of 3He-B physics, it is the categorical extension whose laboratory realization is 3He-B.

### 6. Method (complete dispatch prompt)

**Producing script**: `computations/s86_w1b_t8_3heb_inheritance_land.py`

```
Producing-script spec:
  - Import: from canonical_constants import *
  - Inputs (SHA-pinned):
      gen-physicist-9A-§4.2 source: sessions/archive/session-85/session-85-gen-physicist-synthesis-w6-13.md
      1B 3-solo file:               sessions/archive/session-85/<1B-3-solo>.md
                                    (orchestrator must provide exact filename
                                     at dispatch; volovik + landau + connes
                                     1B 3-solo agreement document)
      target framework file:        sessions/framework/correspondence/3HeB-inheritance-canonical.md
      memory cross-ref target:      .claude/agent-memory/volovik-superfluid-universe-theorist/project_3heb-inheritance.md
  - Steps:
      1. Verify whether sessions/framework/correspondence/3HeB-inheritance-canonical.md
         EXISTS; if absent, CREATE it with H1 heading
            "# 3He-B Inheritance — Canonical (parent → child, NOT analogy)"
         and the standard framework-registry preamble (date, source, scope).
      2. Write framework-canonical body containing:
           (a) inheritance statement: "3He-B parent → substrate child"
               in IS-not-IN language (the substrate IS the categorical
               extension whose laboratory realization is 3He-B; 3He-B is
               NOT a metaphor for the substrate);
           (b) substitution chain (definition → substitution → simplification
               → direction) showing inheritance ≠ analogy: laboratory
               correspondence is a morphism FROM substrate TO 3He-B that
               restricts to identity on the BdG sector, NOT a parametric
               analogy mapping;
           (c) 1B 3-solo cite: volovik + landau + connes joint agreement on
               inheritance direction (parent → child); list each agent's
               specific contribution (volovik: parent identification;
               landau: BCS/hydrodynamic restriction; connes: spectral-triple
               morphism formalization);
           (d) cross-references: sessions/framework/registry/spectral-post-mortem.md,
               sessions/framework/Phononic-Penrose-Diagrams.md,
               and the relevant entry in
               .claude/agent-memory/volovik-superfluid-universe-theorist/
               MEMORY.md.
      3. Update memory cross-reference at
            .claude/agent-memory/volovik-superfluid-universe-theorist/project_3heb-inheritance.md
         to add a one-line pointer: "→ canonical at
         sessions/framework/correspondence/3HeB-inheritance-canonical.md (S86-W1b-T8)";
         per `.claude/rules/agent-standards.md` AMRI Output-target test, the
         CANONICAL location is sessions/framework/, and the agent-memory file
         carries only a pointer (not the canonical content).
      4. Compute SHA-256 of canonical-file payload (post-write); compute
         audit_sha256 from input pin map.
      5. Append verdict line to computations/s86_gate_verdicts.txt:
            S86-3HE-B-INVERSION-CANONICAL-LANDING|PASS|<file_SHA>|framework_canonical|3-solo-agreement|N/A|content_sha256:<64-hex>|audit_sha256:<64-hex>
         FAIL iff framework file absent post-write OR inheritance statement
         absent OR 3-solo cite absent.
  - GPU/CPU: pure I/O + SHA hashing; CPU-only.
  - Substrate-framing reminder: the 3He-B inheritance correspondence is the
    laboratory parent-to-child map. 3He-B is the laboratory realization of
    the substrate's spectral-triple structure at low d_spec; the substrate
    inherits its phononic excitation patterns to 3He-B as Bogoliubov
    quasiparticles. State this as IS-not-IN: 3He-B IS a child realization,
    NOT a metaphor for what the substrate IS doing.
```

### 7. Machinery pin (PRDR)

```yaml
schema_version: R3
machinery_pin_map:
  framework_target:       sessions/framework/correspondence/3HeB-inheritance-canonical.md
  file_existence_check:   "verify file exists; if absent, CREATE with standard preamble"
  source_synthesis:       sessions/archive/session-85/session-85-gen-physicist-synthesis-w6-13.md
  source_section:         "gen-physicist 9A §4.2"
  source_3solo:           "1B 3-solo (volovik + landau + connes)"
  inheritance_direction:  "parent → child (3He-B → substrate is the inverse, NOT permitted; canonical direction is substrate-extends-to-3He-B as laboratory realization)"
  forbidden_phrase:       "analogy"  (must use "inheritance" / "child realization" / "categorical extension" instead)
  memory_cross_ref:       .claude/agent-memory/volovik-superfluid-universe-theorist/project_3heb-inheritance.md
  amri_compliance:        "canonical at sessions/framework/; agent-memory is pointer-only per agent-standards.md AMRI rule"
  hash_algorithm:         SHA-256
  threesolo_witnesses:    ["volovik-superfluid-universe-theorist", "landau-superfluid-condensed-matter-theorist", "connes-ncg-theorist"]
  scheme:                 framework_canonical
  convention:             3-solo-agreement
  L_max:                  N/A
  random_seed:            N/A
  GPU_path:               N/A
input_sha_pins:
  - file: sessions/framework/correspondence/3HeB-inheritance-canonical.md
    sha: <computed-at-runtime>  # may be NEW-FILE on first write
  - file: sessions/archive/session-85/session-85-gen-physicist-synthesis-w6-13.md
    sha: <computed-at-runtime>
  - file: .claude/agent-memory/volovik-superfluid-universe-theorist/project_3heb-inheritance.md
    sha: <computed-at-runtime>
```

### 8. Expected output 4-tuple
`(value=<file_SHA>, scheme=framework_canonical, convention=3-solo-agreement, L_max=N/A)`

### 9. PASS/FAIL/INFO thresholds
- **PASS** iff `sessions/framework/correspondence/3HeB-inheritance-canonical.md` EXISTS post-run AND contains: (a) inheritance statement (parent → child, NOT analogy) in IS-not-IN language, (b) 1B 3-solo cite enumerating all three agents (volovik, landau, connes) with their specific contribution.
- **FAIL** iff framework file missing post-run, OR inheritance statement absent, OR 3-solo cite missing any of the three named agents, OR forbidden phrase "analogy" used (must be re-cast as "inheritance" / "child realization" / "categorical extension").
- **INFO** iff framework file exists and inheritance statement present but 3-solo cite is split across multiple paragraphs (allow re-write to consolidate).
- **Tolerance rule**: VERIFY (exact text-match for the canonical phrase "parent → child, NOT analogy" or the equivalent "inheritance, not analogy" with all three witness agents named).

### 10. Substitution chain (compressed: inheritance ≠ analogy)

```
Definition (Step 1):
  Substrate := spectral triple (A_K, H_K, D_K) with d_spec = 8.
  3He-B     := laboratory superfluid with BCS-paired ³He nuclei at T < T_c,
               admitting a spectral-triple realization (A_He, H_He, D_BdG)
               at d_spec = 1 (BdG sector).
  Analogy   := parametric mapping φ: P_substrate → P_He between two
               systems' parameters with no categorical morphism.
  Inheritance := categorical morphism ι: (A_He, H_He, D_BdG) →
                 (A_K, H_K, D_K)|_{BdG-restriction} that restricts the
                 substrate's spectral triple to the 3He-B BdG sector.

Substitution (Step 2):
  Direction of inheritance per 1B 3-solo agreement:
    volovik:  3He-B is the LABORATORY PARENT (the system that exemplifies
              the spectral-triple structure in the lab).
    landau:   BCS / hydrodynamic content of the substrate restricts onto
              3He-B BdG sector — restriction is the categorical morphism.
    connes:   spectral-triple morphism ι is well-defined; not a parameter
              metaphor.

Simplification (Step 3):
  Inheritance is a categorical morphism (one-way structure-preserving map);
  analogy is a parametric metaphor (no morphism, just variable identification).
  Per Connes' formalization: ι exists as a morphism; therefore the relation
  is inheritance, NOT analogy.

Direction (Step 4):
  Logical priority: substrate is logically prior to 3He-B (substrate has
  full d_spec=8 structure; 3He-B is the d_spec=1 BdG-restricted realization).
  Laboratory parent: 3He-B is the system in which substrate-physics is
  empirically accessible. The two statements are compatible: substrate is
  logically prior, 3He-B is the laboratory-parent (the experimentally
  accessible realization of the categorically-extended substrate). The
  inheritance correspondence runs from substrate (categorical) TO 3He-B
  (laboratory), restricting to the BdG sector. This is NOT analogy
  (no parametric metaphor); it IS inheritance (a categorical morphism).
```

### 11. What PASSES/FAILS MEAN for solution space

- **PASS**: `sessions/framework/correspondence/3HeB-inheritance-canonical.md` exists as canonical → ALL future agent dispatches that cite "3He-B" in any substrate context bind to the inheritance correspondence (parent → child) rather than the analogy framing. The Volovik-Landau-Connes 3-solo agreement gains a permanent registry slot. Framework's many "3He-B" citations across W7 (Hawking workshop), W8 (lab observables), W11 (lab-falsifier suite C5-C6), and the Volovik-convergence project memory now share one canonical anchor.
- **FAIL**: 3He-B citations across S86-W11 (lab-falsifier suite) and downstream sessions remain ambiguous between inheritance and analogy framings; Volovik's S58 "I CC YOU" partition (per project-context memory) lacks a registry-canonical home; the substrate-not-IN-3He-B framing is at risk of regressing to container-thinking in future sessions.

### 12. Effort estimate
0.5 wave (~3-4 hours). File existence check + framework write + 3-solo cite + substitution chain + memory cross-reference update. Higher than T5/T6/T7 because (i) the framework file may not yet exist, requiring NEW-FILE creation with preamble; (ii) the AMRI compliance check requires updating the agent-memory pointer at `.claude/agent-memory/volovik-superfluid-universe-theorist/project_3heb-inheritance.md` to refer to the canonical, not duplicate the content.

### 13. Substrate-framing reminder
3He-B is the laboratory parent — the substrate IS the categorical extension whose laboratory realization is 3He-B. Inheritance runs FROM substrate TO 3He-B (restriction to BdG sector), NOT FROM 3He-B TO substrate (which would make the substrate an analogy of a laboratory system, the WRONG direction per `.claude/rules/phononic-framing.md` "IS Space, Not IN Space" mandate). 3He-B's Bogoliubov phonons IS what the substrate's phononic excitations look like under the inheritance morphism; 3He-B is not a metaphor for substrate physics, it IS substrate-physics-restricted-to-BdG. Container-thinking error to avoid: "the substrate behaves like 3He-B" (wrong: implies analogy). Correct framing: "3He-B realizes the substrate's BdG sector" (inheritance, parent → child).

---

## §X. Wave W1b → Downstream Decision Point

W1b PASSes propagate to the following downstream gates (with binding strength noted):

| W1b PASS | Downstream gate | Binding strength | Wave |
|:---------|:----------------|:-----------------|:-----|
| T5 (Mellin Strip) | T9 `S86-ZETA-REGULATOR-STABILIZATION-THEOREM-LANDING` (REPLACEMENT-B asymptotic, conditional on C9 + C10 PASS) | strong (T9 cites Mellin strip s=4 leading residue) | W3 |
| T5 (Mellin Strip) | C45 `S86-SIXTH-REGULATOR-SYNTHESIS` (deferred to S87) | strong (C45 r_mix construction depends on Mellin-cone admissibility) | S87 |
| T6 (HP^1 LOOSE/STRICT) | C44 `S86-R-PROTECTION-MELLIN-CRITERION` (defer-eligible) | strong (C44 cites HP^1 as canonical 5-atlas R-protection exemplar) | W9 |
| T7 (Two-Layer Obstruction) | C45 `S86-SIXTH-REGULATOR-SYNTHESIS` (deferred to S87) | strong (C45 defer-decision cites two-layer obstruction as structural reason it is meaningful only after C28 closes) | S87 |
| T7 (Two-Layer Obstruction) | C28 `S86-W-4-CUTOFF-SQRT-ADJUDICATION` | medium (C28 outcome interacts with two-layer obstruction's per-conjunct strengthening when cutoff_sqrt is admitted to the atlas) | W4 |
| T8 (3He-B inheritance) | C5 `S86-LAB-SI-TRANSLATION` (lab observables to SI units) | strong (C5 translates 9 lab observables including 3He-A; the inheritance canonical anchors the parent-child framing) | W11 |
| T8 (3He-B inheritance) | C6 `S86-LAB-FALSIFIER-EVOI-TREE` | medium (C6 EVOI level assignment for 3He-B-class observables cites inheritance) | W11 |

**Decision-point note**: T7 PASS is the structural reason C45 sixth-regulator-synthesis is meaningful only AFTER C28 closes; if T7 FAILs, C45 cannot be argued for/against on structural grounds. T6 PASS gives C44 R-protection criterion its canonical exemplar; if T6 FAILs, C44 must construct its 5-atlas exemplar from scratch.

---

## §0.10. Wave W1b Machinery-Enumeration Pin

Per `.claude/rules/epistemic-discipline.md` §Pre-Registration Completeness, every gate-relevant machinery parameter is enumerated and pinned at plan-write time. W1b is REGISTRY-WRITE class; machinery parameters are I/O paths, source-section IDs, hash algorithm, theorem-class tolerance.

| Gate | Free parameter | Pin | Diagnostic-only? |
|:-----|:----------------|:----|:----------------|
| T5 | registry_target | `sessions/permanent-results-registry.md` | no |
| T5 | sibling_anchor | `ZETA-NOT-PHYSICAL-75` | no |
| T5 | source_section_id | `lizzi S-7 §V.6 (CF-LZ-S86-6)` | no |
| T5 | hash_algorithm | SHA-256 | no |
| T5 | theorem_class_tolerance | exact-text-match | no |
| T6 | registry_section | `§VII-B` | no |
| T6 | loose_atlas | `[ζ, Zubarev, SDW, cutoff_sqrt, anomaly]` | no |
| T6 | strict_atlas | `[ζ, Zubarev, SDW]` (F_4) | no |
| T6 | loose_factor | 2.0 | no |
| T6 | strict_factor | 1.031 | no |
| T6 | source_section_id | `lizzi S-7 §V.7 (CF-LZ-S86-7)` | no |
| T7 | registry_section | `§VII-B` | no |
| T7 | atlas_5 | `[ζ, Zubarev, SDW, cutoff_sqrt, anomaly]` | no |
| T7 | n_joint_required | `0/5` | no |
| T7 | individual_conjunct_failure | "every conjunct fails individually for every regulator" | no |
| T7 | source_section_id | `lizzi S-7 §V.8 (CF-LZ-S86-8)` | no |
| T8 | framework_target | `sessions/framework/correspondence/3HeB-inheritance-canonical.md` | no |
| T8 | file_existence_check | "verify; CREATE if absent" | no |
| T8 | inheritance_direction | "parent → child (substrate logically prior; 3He-B laboratory parent realization)" | no |
| T8 | forbidden_phrase | "analogy" | no |
| T8 | threesolo_witnesses | `[volovik, landau, connes]` (all three required) | no |
| T8 | memory_cross_ref | `.claude/agent-memory/volovik-superfluid-universe-theorist/project_3heb-inheritance.md` | no |
| T8 | amri_compliance | "canonical at sessions/framework/; agent-memory is pointer-only" | no |
| ALL | scheme | per gate (registry_landing / framework_canonical) | no |
| ALL | convention | per gate (lizzi-track / 3-solo-agreement) | no |
| ALL | L_max | N/A (registry write) | yes (diagnostic-only — no eigenvalue cutoff applies) |
| ALL | random_seed | N/A | yes (diagnostic-only — no stochastic sampling) |
| ALL | GPU_path | N/A (pure I/O) | yes (diagnostic-only — no linalg) |

**PRDR closure**: every free parameter that affects PASS/FAIL outcome is pinned (no "diagnostic-only" entries are gate-relevant). PRU Class 8 immune by construction.

---

## §0.11. Wave W1b Input-SHA Ledger

All input pins are computed at runtime when each script reads its inputs. The ledger here records WHICH files each gate reads, not the SHAs themselves (those are emitted to stdout in the first 20 lines per `.claude/rules/gate-verdicts.md` §Pre-Registration Protocol Step 2).

| Gate | Input file | Role |
|:-----|:-----------|:-----|
| T5 | `sessions/permanent-results-registry.md` | registry write target |
| T5 | `sessions/archive/session-85/session-85-s7-combined-landscape-lizzi.md` | source: lizzi S-7 §V.6 |
| T5 | `computations/s85_gate_verdicts.txt` | W0-S6 verdict pin |
| T6 | `sessions/permanent-results-registry.md` | registry write target |
| T6 | `sessions/archive/session-85/session-85-s7-combined-landscape-lizzi.md` | source: lizzi S-7 §V.7 |
| T6 | `computations/s85_gate_verdicts.txt` | W5-6 verdict pin |
| T7 | `sessions/permanent-results-registry.md` | registry write target |
| T7 | `sessions/archive/session-85/session-85-s7-combined-landscape-lizzi.md` | source: lizzi S-7 §V.8 |
| T7 | `computations/s85_gate_verdicts.txt` | W5-7 verdict pin |
| T8 | `sessions/framework/correspondence/3HeB-inheritance-canonical.md` | framework canonical (may be NEW-FILE) |
| T8 | `sessions/archive/session-85/session-85-gen-physicist-synthesis-w6-13.md` | source: gen-physicist 9A §4.2 (1B 3-solo cite) |
| T8 | `.claude/agent-memory/volovik-superfluid-universe-theorist/project_3heb-inheritance.md` | memory cross-reference target |

**Source-of-truth reminder**: per `.claude/rules/agent-standards.md` AMRI rules, the 3He-B inheritance canonical (T8) must live at `sessions/framework/correspondence/3HeB-inheritance-canonical.md`, NOT in agent memory. The agent-memory file at `.claude/agent-memory/volovik-superfluid-universe-theorist/project_3heb-inheritance.md` becomes a pointer to the canonical after T8 PASSes.

**Verdict-file canonical path** (per `.claude/rules/gate-verdicts.md`): all four W1b verdict lines append to `computations/s86_gate_verdicts.txt` — NOT `sessions/archive/session-86/...` and NOT `sessions/session-plan/...`.

---

**End of Wave W1b plan.** Four registry-write gates: three Lizzi-track structural theorems landed at `sessions/permanent-results-registry.md` (Mellin Strip + HP^1 LOOSE/STRICT + Two-Layer Obstruction), plus the 3He-B inheritance canonical at `sessions/framework/correspondence/3HeB-inheritance-canonical.md`. Total wave estimate 4-5 hours; LOW-effort across all four items. Dispatch in parallel with W1a, W0a, W0b, W0c, W1c, W2, W4 per Batch-1 schedule.
