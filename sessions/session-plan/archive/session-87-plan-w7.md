# Session 87 Plan — Wave 7: IC Per-Class + UV-Cutoff + Layer-1-2 Audit

**Owner**: `lizzi-spectral-functional-theorist` (W-7 attribution from S86; CF-42..CF-46)
**Output verdict file**: `computations/s87_gate_verdicts.txt`
**Script prefix convention**: `computations/s87_w7_<slug>.py`
**Item count**: 5 (CF-42, CF-43, CF-44, CF-45, CF-46)
**Cross-cite specialists**: `transit-dynamics-theorist` (CF-42 track-discriminator co-sign); `connes-ncg-theorist` (CF-46 warrant-check head-of-queue co-sign)

---

## §0. Wave 7 Summary

Wave 7 executes the five W-7 carry-forwards from the S86 closeout, all originating from
the lizzi(+transit/+connes) reviewer triad. The wave's structural target is the
**5-class L1 partition** that S86 W-9 left as STAGE-1-CANDIDATE in the joint F_2-class
Path-(c) theorem ladder. Per `.claude/rules/joint-theorem-promotion.md` Stage 1, the
5-class partition is ELIGIBLE for citation but NOT permanent until Stage 2 verification
in S88+ (CF-59). W7 supplies the per-class numerical content that Stage 2 will need.

### Five gate-items

- **§W7-1 / CF-42** `S87-W5A-P3-IC-PER-CLASS-VERIFY` (with dual-prior footnote) —
  Re-compute `xi_E_GGE_inv` initial condition for each of 5 L1-classes at s=−1;
  track-discriminator per S86 W-9 EM-CN-R3-1. MODERATE; lizzi+transit. Dual-prior
  pre-registered per `.claude/rules/epistemic-discipline.md` §"Dual-prior pre-registration
  as track-discriminator pattern" (T1-11, W-9 RULE-5).

- **§W7-2 / CF-43** `S87-W6-C-BETA-UV-CUTOFF-3CLASS` — Test C-β UV-cutoff-choice
  immunization across {Class 1, Class 2, Class 3} = F_4 multiplier-vector sub-family
  ⊂ 5-atlas. MODERATE; lizzi.

- **§W7-3 / CF-44** `S87-W6-C-GAMMA-WEAK-PER-CLASS` — Re-evaluate C-γ-WEAK
  Weyl-rescaling Λ_anom_internal per L1-class. HEAVY; lizzi.

- **§W7-4 / CF-45** `S87-LAYER-1-2-RETROACTIVE-AUDIT-FULL-ENUMERATION` — Walk all
  S78-onward 5-atlas / regulator-class / partition citations; LAYER-tag per the
  5-stage protocol with optional Stage-2.5 sub-tag. HEAVY (1-2 wave equiv); lizzi.

- **§W7-5 / CF-46** `S87-LATENT-WARRANT-CHECK-QUEUE` (head-of-queue 4-field spec
  for the SINGLE highest-priority warrant-check from the ~26 available; remaining
  ~25 deferred to S88+ with stub specs). NARROW per CV-CN-R3-4; lizzi+connes.

### Substrate-framing direction

All five gates flow FROM the substrate (D_K eigenvalue spectrum + spectral moments
per regulator family) TOWARD emergent observables (xi_E_GGE_inv, Λ_anom_internal,
LAYER-tagging structure). The 5-class L1 partition itself is a SUBSTRATE-IS observable
(finite-L spectral-triple structure on `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})` per §VII.W
W-5 calibration); the per-class compute resolves how `xi_E_GGE_inv` and Λ_anom_internal
inherit into laboratory-IN observables. Container-thinking direction-inversions
(treating per-class observables as living "in" a pre-existing class-container) are
forbidden — the classes EMERGE from the F_2 spectral-cluster structure, they don't
pre-exist as containers for `xi_E_GGE_inv` to be "evaluated in".

### Functional-pluralism note

W7's structural target straddles three regulator schemes (per the L1-class
construction in S86 W-9): `cutoff` / `zeta` / `anomaly-derived`. CF-43's UV-cutoff
gate explicitly tests cross-regulator immunization on Classes 1-3. CF-44's
C-γ-WEAK gate evaluates Λ_anom_internal under the Weyl-rescaling family per class.
This is FUNCTIONAL-INDEPENDENCE testing in the sense of the lizzi memory entry
`feedback_reporting-framing.md` and `S70 Workshop Landau`: results that
PASS uniformly across the 3-class sub-family are STRUCTURAL-FI; results that
PASS only in some classes are SCHEME-DEPENDENT and route to the `f_conv` /
intensive-vs-extensive partition discipline (S77 Workshop R2).

---

## §0.5. Wave 7 Decision-Point Prerequisites

W7 has THREE upstream sequencing constraints. None are plan-write blockers (the W7
plan is written independently of these landings); each is checked at compute-dispatch
time and rerouted to INFO with a `<status>_pending=true` flag if the prerequisite has
not landed.

1. **W-9 STAGE-1-CANDIDATE registration of Joint F_2-Class Path-(c) Theorem (CF-54)**
   — CF-42's "5 L1-classes" are the classes registered by W-9 Stage-1 landing. If the
   STAGE-1 entry has not landed at compute time, W7-1 reads its 5-class definition
   directly from the W-9 workshop §E-R2.2 line 1097-1112 wrap-up text and emits the
   verdict line with `class_partition_pin_pending=true`. PASS still possible; the
   audit_sha256 captures the wrap-up text SHA in lieu of the registry-entry SHA.

2. **W-9 §VII.X candidate Joint Theorem clauses (a)..(f)** — CF-44's per-class
   Λ_anom_internal cites clause (e) (lizzi-side) of the Joint Theorem. If the clause
   is not yet in `permanent-results-registry.md`, the dispatch reads from W-9 workshop
   §L-CR3.3 line 1849-1858 (the amendment-to-clause-(e) pin). Late-bind SHA from
   workshop file; not registry-entry.

3. **CF-42 dual-prior Track A/Track B specification** — the dual-prior is co-authored
   by lizzi + transit at this plan-author level (see §W7-1.5 substitution chain).
   The pin is FROZEN into THIS plan file; CF-42's runtime dispatch reads the
   pre-registered Track A = 0.4, Track B = 0.6 from §0.10. Discriminator gate
   criterion mapping is in §W7-1.10 below.

These are SEQUENCING constraints, not plan-write dependencies. The W7 plan freezes
all per-gate machinery pins; the late-bind SHAs are documented in §0.11.

---

## §I. Carry-Forward Items Mapping

| Wave §-id | Carry-forward source | S87 gate ID | Item class | Effort |
|:----------|:---------------------|:------------|:-----------|:-------|
| §W7-1 | W-7 CF-1 (lizzi+transit; compute-carryforward.md CF-42) | `S87-W5A-P3-IC-PER-CLASS-VERIFY` | MODERATE | ~6-8h |
| §W7-2 | W-7 CF-2 (lizzi; compute-carryforward.md CF-43) | `S87-W6-C-BETA-UV-CUTOFF-3CLASS` | MODERATE | ~6-8h |
| §W7-3 | W-7 CF-3 (lizzi; compute-carryforward.md CF-44) | `S87-W6-C-GAMMA-WEAK-PER-CLASS` | HEAVY | ~10-14h |
| §W7-4 | W-7 CF-4 (lizzi; compute-carryforward.md CF-45) | `S87-LAYER-1-2-RETROACTIVE-AUDIT-FULL-ENUMERATION` | HEAVY (1-2 wave equiv) | ~16-24h |
| §W7-5 | W-7 CF-AVAIL-1..27 (lizzi+connes; compute-carryforward.md CF-46) | `S87-LATENT-WARRANT-CHECK-QUEUE` (head-of-queue) | NARROW per CV-CN-R3-4 | ~3-5h (head-of-queue only) |

Total wave effort: ~41-59h aggregate. CF-44 + CF-45 are the dominant cost (HEAVY each;
CF-45 alone is 1-2 wave-equivalents per the source carry-forward). The head-of-queue
discipline on CF-46 caps that line at one warrant-check; the remaining ~25 are stub
specs deferred to S88+.

---

## §W7-1. S87-W5A-P3-IC-PER-CLASS-VERIFY (CF-42)

### 1. Gate ID
`S87-W5A-P3-IC-PER-CLASS-VERIFY` (carry-forward CF-42; compute-carryforward.md W-7 CF-1
attributing lizzi+transit). Dual-prior footnote per `.claude/rules/epistemic-discipline.md`
§"Dual-prior pre-registration as track-discriminator pattern" (T1-11, W-9 RULE-5).

### 2. Trigger
`[VERIFY]` (substitution chain mandatory per `.claude/rules/math-scripts.md`
§"Double-Check Logic Before Compute" — gate makes a direction claim about
per-class IC dispersion and a track-discriminator allocation).

### 3. Classification
**PHONONIC**. `xi_E_GGE_inv` is the substrate-physics initial condition for the
GGE-relic energy-density dispersion, the canonical S86 W4 P4 commit value
`xi_E_GGE_inv = 13.642473425595973` (per `sessions/framework/registry/branch-iv-canonical.md`
§3, formula source lizzi 9A §2.2: substrate-natural anchor 59.8 · Δ_BCS / K_base).
The per-class projection at s=−1 is the per-class restriction of the GGE relic's
phononic-excitation amplitude — a substrate-spectral quantity, not a container
observable.

### 4. Agent type
**Runtime primary**: `lizzi-spectral-functional-theorist` (lead per W-7 attribution).
**Cross-cited co-sign**: `transit-dynamics-theorist` (track-discriminator origin per
EM-CN-R3-1; transit-side authorship of the dual-prior reading; consulted via input-SHA
pin from W-9 workshop wrap-up text, not spawned as collab agent).

The runtime dispatch is single-agent (lizzi); the transit cross-cite supplies the
dual-prior reading specification only.

### 5. Hypothesis
The 5 L1-classes (registered as STAGE-1-CANDIDATE at W-9 closeout per the joint F_2-class
Path-(c) theorem) admit a per-class restriction of the GGE-relic IC `xi_E_GGE_inv`,
evaluated at the s=−1 Mellin slot. The dispersion of these 5 per-class IC values is
either (Track A) tight enough to support F_2-class STRUCTURAL-PRIMACY (the 5-class
partition reduces to a single substrate-canonical IC modulo per-class noise), or
(Track B) wide enough that the 5-class partition is a per-class DIAGNOSTIC reading
only (no structural reduction; each class carries an independent IC).

### 6. Method (complete dispatch prompt for runtime)

```
Dispatch prompt for `lizzi-spectral-functional-theorist`:

You are computing the per-class restriction of xi_E_GGE_inv for each of 5 L1-classes
at the Mellin slot s=−1, per S87-W7-1 (S87-W5A-P3-IC-PER-CLASS-VERIFY, carry-forward
CF-42 from lizzi+transit, compute-carryforward.md W-7 CF-1). The dual-prior
discriminator-track pre-registration is in §0.10 of this plan; treat Track A and
Track B as separate posterior-allocation hypotheses.

Required imports:
  from canonical_constants import *
  import numpy as np
  import torch  # GPU path for D_K spectral evaluation
  import hashlib
  import json
  import os
  os.environ.setdefault('OMP_NUM_THREADS', '8')

Inputs (load + SHA-pin in first 20 lines of stdout):
  1. 5-class L1 partition definition from W-9 STAGE-1 landing:
     `sessions/permanent-results-registry.md` §Joint-F2-Class-Path-c-Theorem (or W-9
     workshop §E-R2.2 lines 1097-1112 if STAGE-1 not yet landed)
     SHA: <RUNTIME-LATE-BIND from CF-54 verdict OR W-9 workshop file>
  2. Canonical xi_E_GGE_inv = 13.642473425595973 (S86 W4 P4 commit):
     `computations/canonical_constants.py` (key: xi_E_GGE_inv)
     SHA: <CANONICAL pin SHA from canonical_constants.py at S87 plan-freeze>
  3. D_K^{≤10} spectrum cache:
     `computations/s84_spectrum_cache_L12_tau019.npz`
     SHA: <CANONICAL — read from S86 close>
  4. F_2-class spectral-cluster definition (W-7 CF-1 source):
     `sessions/archive/session-86/session-86-w7-workshop.md` §EM-CN-R3-1
     SHA: <RUNTIME-LATE-BIND from W-9 workshop file>

Computation steps:
  Step A. For each L1-class c ∈ {1, 2, 3, 4, 5}, extract the projection P_c of the
          D_K^{≤10} spectrum onto the class-c subspace per the W-9 5-class partition.
          The projection is determined by the F_2-class spectral-cluster identity
          (at the Mellin slot s=−1).
  Step B. For each class c, compute the per-class Mellin-cone moment evaluation
            xi_c = M[xi_E_GGE_inv | P_c, s=−1]
          where M[ · | P_c, s=−1] is the s=−1 Mellin-cone moment restricted to
          the class-c projection. The per-class anchor is 59.8 · Δ_BCS_c / K_base_c
          where Δ_BCS_c and K_base_c are the per-class restrictions of the
          substrate-canonical Δ_BCS and K_base.
  Step C. Compute the per-class dispersion:
            sigma_xi = std({xi_1, xi_2, xi_3, xi_4, xi_5}) / mean({xi_c})
          and the maximum pairwise relative deviation:
            delta_max = max_{c,c'} |xi_c − xi_{c'}| / max(|xi_c|, |xi_{c'}|).
  Step D. Compute the 5-class consensus value xi_consensus = mean({xi_c}) and the
          relative deviation from the canonical bare value:
            delta_canonical = |xi_consensus − xi_E_GGE_inv| / |xi_E_GGE_inv|.
  Step E. Evaluate the dual-prior discriminator:
            Track A (F_2-class STRUCTURAL-PRIMACY): prior 0.4 → posterior allocation
              if delta_max ≤ 0.05 (RATIO; tight 5-class consensus).
            Track B (per-class DIAGNOSTIC-only): prior 0.6 → posterior allocation
              if delta_max > 0.20 (RATIO; wide per-class spread, no reduction).
            INFO-band: 0.05 < delta_max ≤ 0.20 → posterior unchanged (priors retained).
  Step F. Cross-check: re-derive xi_consensus via independent pathway — re-evaluate
          the substrate-canonical xi_E_GGE_inv = 59.8 · Δ_BCS / K_base globally
          (no class restriction) and verify xi_consensus → xi_E_GGE_inv as the
          5-class projection collapses to identity (sanity-check on the partition's
          completeness).
  Step G. Compute closure SHA: SHA-256 of the ordered input-pin map
          {class_partition_sha, xi_canonical_sha, dk_spectrum_sha, f2_cluster_sha,
          mellin_slot_pin=−1, prior_a_pin=0.4, prior_b_pin=0.6}.

Decision rule (PASS/FAIL/INFO; composite collapse per gate-verdicts.md):
  sign_verdict   = PASS if xi_consensus has the same sign as xi_E_GGE_inv (positive),
                   FAIL otherwise.
  magnitude_verdict = PASS if delta_canonical ≤ 0.05 (RATIO; tight against bare),
                      INFO if 0.05 < delta_canonical ≤ 0.20,
                      FAIL otherwise.
  regime_verdict = VALID if all 5 per-class evaluations are inside the s=−1 Mellin
                   convergence cone, MARGINAL if 1-2 classes graze the boundary,
                   BREAKDOWN if ≥3 classes leave the cone.

Track posterior allocation (separate from composite verdict):
  Posterior_A = (likelihood_A · 0.4) / Z;  Posterior_B = (likelihood_B · 0.6) / Z.
  likelihood_A = Gaussian(delta_max | mu=0, sigma=0.025) — concentrated near 0.
  likelihood_B = Gaussian(delta_max | mu=0.30, sigma=0.10) — broad around per-class spread.

Verdict line append (atomic, single open("a") write, per `.claude/rules/gate-verdicts.md`):
  S87-W5A-P3-IC-PER-CLASS-VERIFY: <PASS|FAIL|INFO> -- value=<delta_max> \\
    scheme=Mellin-slot-s=-1 convention=substrate-natural-xi-E-GGE \\
    L_max=10 sha256=<64-char closure>

Plus dual-SHA companion comment row:
  # audit_sha256_short=<16> content_sha256_short=<16> # S87-W5A-P3-IC-PER-CLASS-VERIFY dual-SHA companion row

Plus S87+ schema-v2 3-tuple annotation (S87+ REQUIRED for [VERIFY] trigger):
  # sign_verdict=<PASS|FAIL|N/A> magnitude_verdict=<PASS|INFO|FAIL> \\
  # regime_verdict=<VALID|MARGINAL|BREAKDOWN> # S87-W5A-P3-IC-PER-CLASS-VERIFY 3-tuple annotation

Plus dual-prior posterior comment row (S87 introduction; pre-registered here):
  # posterior_A=<float> posterior_B=<float> # S87-W5A-P3-IC-PER-CLASS-VERIFY dual-prior allocation

Output file targets:
  computations/s87_w7_ic_per_class_verify.py
  computations/s87_w7_ic_per_class_verify.npz   (5 per-class xi_c + dispersion)
  computations/s87_w7_ic_per_class_verify.png   (5-bar comparison plot vs canonical)
  computations/s87_gate_verdicts.txt            (canonical verdict append)

GPU path: torch.linalg.eigh on RX 9070 XT for D_K^{≤10} spectrum re-derivation if
the cached spectrum file has SHA mismatch; otherwise CPU read of cache with
OMP_NUM_THREADS=8.
```

### 7. Machinery pin (PRDR — every free parameter)

| Parameter | Pin |
|:----------|:----|
| `L_max` | 10 (canonical S86 W4 P4 commit) |
| `scheme` | Mellin-slot evaluation at s=−1 (substrate-distance-1 pole convention per S86 W-9 §D-R2.3) |
| `convention` | substrate-natural-xi-E-GGE (anchored to canonical_constants.xi_E_GGE_inv) |
| `n_eval` | 5 (one per L1-class) |
| `scan_range` | N/A (5 discrete classes; no continuous scan) |
| `tolerance` | RATIO ≤ 0.05 for PASS magnitude_verdict; RATIO > 0.20 for FAIL |
| `random_seed` | None (deterministic projection arithmetic) |
| `GPU path` | `torch.linalg.eigh` on RX 9070 XT for spectrum re-derivation; CPU read of cache with `OMP_NUM_THREADS=8` otherwise |
| `mellin_slot_pin` | s = −1 (substrate-distance-1) |
| `prior_a_pin` | 0.4 (Track A: F_2-class STRUCTURAL-PRIMACY) |
| `prior_b_pin` | 0.6 (Track B: per-class DIAGNOSTIC-only) |
| `discriminator_likelihood_a_sigma` | 0.025 (Gaussian-A concentration around 0) |
| `discriminator_likelihood_b_mu` | 0.30 (Gaussian-B center around per-class spread) |
| `discriminator_likelihood_b_sigma` | 0.10 |
| `class_partition_sha` | `<RUNTIME-LATE-BIND>` from CF-54 STAGE-1 entry OR W-9 workshop file |
| `xi_canonical_sha` | `<CANONICAL>` pin SHA from canonical_constants.py xi_E_GGE_inv at S87 plan-freeze |
| `f2_cluster_sha` | `<RUNTIME-LATE-BIND>` from W-9 workshop §EM-CN-R3-1 |

PRU Class-8 status: every parameter pinned EXCEPT the two `<RUNTIME-LATE-BIND>` SHAs,
which are runtime-resolvable per the dynamic-input convention. This is acceptable per
`.claude/rules/epistemic-discipline.md` §"Pre-Registration Completeness".

### 8. Expected output 4-tuple
`(value=<delta_max>, scheme=Mellin-slot-s=-1, convention=substrate-natural-xi-E-GGE, L_max=10)`

### 9. PASS/FAIL/INFO thresholds (with tolerance rule)

- **PASS**: `delta_max ≤ 0.05` (RATIO across 5 classes) AND `delta_canonical ≤ 0.05`
  AND all 5 classes inside s=−1 Mellin convergence cone (regime_verdict=VALID).
  The 5-class IC dispersion is tight enough to support F_2-class STRUCTURAL-PRIMACY
  (Track A posterior allocated).
- **INFO**: `0.05 < delta_max ≤ 0.20` (intermediate band) OR regime_verdict=MARGINAL.
  The 5-class spread is intermediate; neither track decisively favored. Posteriors
  remain near the priors (Track A ~0.4, Track B ~0.6).
- **FAIL**: `delta_max > 0.20` (RATIO; wide per-class spread) OR regime_verdict=BREAKDOWN
  OR sign_verdict=FAIL. The 5-class partition does NOT reduce to a single
  substrate-canonical IC; Track B (per-class DIAGNOSTIC-only) posterior allocated.

Tolerance-rule class: RATIO (per `.claude/rules/gate-verdicts.md`).

### 10. Substitution chain (MANDATORY — direction claim on per-class dispersion)

```
Definition 1: xi_E_GGE_inv = 59.8 · Δ_BCS / K_base   [canonical, lizzi 9A §2.2]
              numerical value: 13.642473425595973   [canonical_constants.py, S86 W4 P4 commit]

Definition 2: P_c = projection onto L1-class c, c ∈ {1, 2, 3, 4, 5}
              [W-9 STAGE-1 partition; spectral-cluster on F_2 at s=−1]

Definition 3: xi_c = M[xi_E_GGE_inv | P_c, s=−1]
                   = 59.8 · Δ_BCS_c / K_base_c
              where Δ_BCS_c = ⟨P_c, Δ_BCS⟩, K_base_c = ⟨P_c, K_base⟩
              [per-class restriction of the substrate-natural anchor]

Definition 4: delta_max = max_{c,c'} |xi_c − xi_{c'}| / max(|xi_c|, |xi_{c'}|)
              [pairwise RATIO dispersion]

Definition 5: delta_canonical = |mean({xi_c}) − xi_E_GGE_inv| / |xi_E_GGE_inv|
              [consensus deviation from bare canonical]

Step 1 (substitute definitions into delta_max):
  delta_max = max_{c,c'} |59.8 · Δ_BCS_c / K_base_c − 59.8 · Δ_BCS_{c'} / K_base_{c'}|
              / max(|59.8 · Δ_BCS_c / K_base_c|, |59.8 · Δ_BCS_{c'} / K_base_{c'}|)

Step 2 (factor 59.8 out):
  delta_max = max_{c,c'} |Δ_BCS_c / K_base_c − Δ_BCS_{c'} / K_base_{c'}|
              / max(|Δ_BCS_c / K_base_c|, |Δ_BCS_{c'} / K_base_{c'}|)
            = max_{c,c'} dispersion(ratio_c, ratio_{c'})
  where ratio_c = Δ_BCS_c / K_base_c.

Step 3 (simplify under partition completeness):
  ∑_c P_c = 1 (5-class partition is complete; orthogonal projections sum to identity)
  ⇒  ∑_c Δ_BCS_c = Δ_BCS  AND  ∑_c K_base_c = K_base.
  Hence mean({ratio_c}) is NOT trivially equal to Δ_BCS / K_base (Cauchy-Schwarz
  inequality ⇒ mean of ratios ≥ ratio of means iff numerator-denominator are
  uncorrelated across classes).

Step 4 (read direction from canonical form):
  If Δ_BCS_c / K_base_c is APPROXIMATELY CONSTANT across c (i.e., the per-class
  numerator and denominator are proportionally distributed), then delta_max → 0
  AND delta_canonical → 0  ⇒  Track A (STRUCTURAL-PRIMACY) PASS.
  If Δ_BCS_c / K_base_c VARIES SIGNIFICANTLY across c (numerator and denominator
  are independently distributed), then delta_max grows  ⇒  Track B (DIAGNOSTIC-only)
  posterior allocation.

Conclusion: a PASS verdict establishes that the 5-class partition admits a single
substrate-canonical IC (the 5-class structure is a re-organization, not a fragmentation,
of xi_E_GGE_inv). A FAIL closes the F_2-class STRUCTURAL-PRIMACY interpretation: the
5 classes carry independent IC content, and downstream gates citing "the" xi_E_GGE_inv
must respect per-class restrictions.

Direction claim verified: delta_max ≤ 0.05 ⇒ Track A PASS; delta_max > 0.20 ⇒ Track B
posterior dominates.
```

### 11. What PASSES/FAILS MEAN for solution space

- **PASS (Track A allocation)**: Pins the 5-class L1 partition as a re-organization
  (NOT fragmentation) of xi_E_GGE_inv. F_2-class STRUCTURAL-PRIMACY supported; the
  5-class partition reduces to a single substrate-canonical IC modulo per-class noise
  ≤5%. Strengthens the W-9 Joint Theorem clause (c) JOINT-class structural reading.
  Downstream CF-44 (C-γ-WEAK Λ_anom_internal per-class) is interpretable as
  per-class refinement on a unified substrate-canonical anchor. CF-59 (S88+ Stage-2
  independent verify) inherits this PASS as upstream evidence.
- **INFO**: Intermediate dispersion. Neither Track A nor Track B decisively allocated;
  posteriors near priors. The 5-class partition is operationally meaningful but its
  STRUCTURAL-vs-DIAGNOSTIC reading is unresolved at S87. CF-54 STAGE-1 candidate
  remains STAGE-1; promotion to permanent (Stage 3) deferred until cross-axis
  evidence accumulates.
- **FAIL (Track B allocation)**: Pins the 5-class L1 partition as a per-class
  DIAGNOSTIC reading only. F_2-class STRUCTURAL-PRIMACY refuted; each class carries
  independent IC content. Downstream gates citing "the" xi_E_GGE_inv must respect
  per-class restrictions; the W-9 Joint Theorem clause (c) requires re-spec under
  per-class IC maps. Closes the "5-class partition reduces to single canonical
  IC" interpretation; the 5-class structure remains operationally meaningful but
  loses STRUCTURAL-promotion eligibility.

### 12. Effort estimate
~6-8h runtime. Dominated by D_K spectrum projection arithmetic per class (5 separate
projections; each O(155984) eigenvalues) and the dual-prior posterior computation.
GPU path on RX 9070 XT recommended for the 5-projection batch (~30 min wall-clock);
CPU fallback is ~2-3h.

### 13. Substrate-framing reminder
`xi_E_GGE_inv` is the **substrate-IS** initial condition for the GGE-relic energy-density
dispersion — not a laboratory observable evaluated "in" a class container. The 5 L1-classes
EMERGE from the F_2 spectral-cluster structure of D_K^{≤10}; they do NOT pre-exist as
containers for `xi_E_GGE_inv` to be "evaluated in". Per `.claude/rules/phononic-framing.md`
§"IS Space, Not IN Space": the per-class projection P_c is a substrate-spectral
restriction, NOT a container coordinate. The Track A reading frames the 5 classes as
ONE substrate-canonical IC reorganized by spectral-cluster structure; the Track B reading
frames them as 5 independent ICs the substrate carries simultaneously — both readings
are substrate-IS, neither is container-IN.

```yaml
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
```

---

## §W7-2. S87-W6-C-BETA-UV-CUTOFF-3CLASS (CF-43)

### 1. Gate ID
`S87-W6-C-BETA-UV-CUTOFF-3CLASS` (carry-forward CF-43; compute-carryforward.md W-7 CF-2
attributing lizzi).

### 2. Trigger
`[VERIFY]` (substitution chain mandatory — gate makes a direction claim about
UV-cutoff-choice immunization across the F_4 multiplier-vector sub-family).

### 3. Classification
**GEOMETRIC**. The C-β coefficient is a Mellin-cone substrate-distance-1 spectral
moment of D_K^{≤10}, evaluated under a UV-cutoff family parameterization. The
F_4 multiplier-vector sub-family {Class 1, Class 2, Class 3} ⊂ 5-atlas is the
spectral-triple-structure projection axis from the S86 W-8 4-channel
LAYER-2 sub-decomposition.

### 4. Agent type
**Runtime primary**: `lizzi-spectral-functional-theorist` (sole owner per W-7 attribution).

No co-sign agents (CF-43 is single-axis spectral-functional, no transit / connes
cross-axis content).

### 5. Hypothesis
The C-β UV-cutoff coefficient, when evaluated across the F_4 multiplier-vector
sub-family {Class 1, Class 2, Class 3} ⊂ 5-atlas regulators, is INVARIANT under
UV-cutoff choice (the C-β value is a substrate-canonical Mellin moment, not a
cutoff-bookkeeping artifact). PASS = `max_{c,c'} |C-β_c − C-β_{c'}| / |mean(C-β_c)|`
≤ pre-registered immunization threshold; FAIL = sub-family carries cutoff-dependence.

### 6. Method (complete dispatch prompt for runtime)

```
Dispatch prompt for `lizzi-spectral-functional-theorist`:

You are computing the C-β UV-cutoff coefficient for each of 3 classes in the F_4
multiplier-vector sub-family per S87-W7-2 (S87-W6-C-BETA-UV-CUTOFF-3CLASS,
carry-forward CF-43 from lizzi, compute-carryforward.md W-7 CF-2).

Required imports:
  from canonical_constants import *
  import numpy as np
  import torch
  import hashlib
  import json
  import os
  os.environ.setdefault('OMP_NUM_THREADS', '8')

Inputs (load + SHA-pin in first 20 lines of stdout):
  1. F_4 multiplier-vector sub-family definition (S86 W-8 4-channel LAYER-2):
     `sessions/permanent-results-registry.md` §VII.K-PROP (W-8 RULE-1 landing)
     SHA: <RUNTIME-LATE-BIND from §VII.K-PROP entry>
  2. 5-atlas regulator definitions (canonical):
     `computations/_spectral_action_regulators.py` (SCHEMATIC-tagged per
     `.claude/rules/substrate-first-canonical-sourcing.md` §iv)
     SHA: <CANONICAL>
  3. D_K^{≤10} spectrum cache:
     `computations/s84_spectrum_cache_L12_tau019.npz`
     SHA: <CANONICAL>
  4. C-β coefficient definition + canonical pre-S87 evaluations:
     `sessions/archive/session-86/session-86-w6-workshop.md` §C-β-immunization
     SHA: <RUNTIME-LATE-BIND from W-6 workshop file>

Computation steps:
  Step A. For each class c ∈ {Class 1, Class 2, Class 3} of the F_4 multiplier-vector
          sub-family, identify the regulator family R_c (from the 5-atlas definition).
  Step B. For each c, compute the C-β coefficient via Mellin-cone substrate-distance-1
          residue evaluation:
            C-β_c = Res[M_c(s); s=2] / Res[M_c(s); s=3]
          where M_c(s) is the regulator-c-weighted Mellin transform of D_K^{≤10}.
          Use `_spectral_action_regulators.py` SCHEMATIC helpers; flag SCHEMATIC
          level in convention= field per `substrate-first-canonical-sourcing.md` §iv.
  Step C. Compute the cross-class dispersion:
            delta_C_beta = max_{c,c'} |C-β_c − C-β_{c'}| / |mean({C-β_c})|.
  Step D. Cross-check (lizzi-style functional-pluralism comparison): re-evaluate
          C-β_c under TWO independent regulator schemes per class — sqrt-Heaviside
          (scheme=cutoff) and Gaussian-Mellin (scheme=zeta) — and verify
          per-class C-β_c is scheme-invariant within RATIO ≤ 1e-3 (functional-
          independence within the class).
  Step E. Compute closure SHA: SHA-256 of the ordered input-pin map
          {f4_subfamily_sha, atlas_def_sha, dk_spectrum_sha, c_beta_def_sha,
          n_classes_pin=3, regulator_family_pin=F_4_multiplier_vector}.

Decision rule (PASS/FAIL/INFO; composite collapse per gate-verdicts.md):
  sign_verdict   = N/A (no signed-direction pre-registration; C-β is a positive
                   spectral moment).
  magnitude_verdict = PASS if delta_C_beta ≤ 0.01 (RATIO; tight cross-class
                      immunization),
                      INFO if 0.01 < delta_C_beta ≤ 0.05,
                      FAIL otherwise.
  regime_verdict = VALID if all 3 classes inside Mellin substrate-distance-1
                   convergence (s=2 + s=3 residues both finite),
                   MARGINAL if 1 class grazes the boundary,
                   BREAKDOWN if ≥2 classes leave the cone.

Verdict line append (atomic):
  S87-W6-C-BETA-UV-CUTOFF-3CLASS: <PASS|FAIL|INFO> -- value=<delta_C_beta> \\
    scheme=Mellin-cone-substrate-distance-1-SCHEMATIC convention=F_4-multiplier-vector \\
    L_max=10 sha256=<64-char closure>

Plus dual-SHA companion comment row.
Plus S87+ schema-v2 3-tuple annotation.

Output file targets:
  computations/s87_w7_c_beta_uv_cutoff_3class.py
  computations/s87_w7_c_beta_uv_cutoff_3class.npz   (3 per-class C-β_c values)
  computations/s87_w7_c_beta_uv_cutoff_3class.png   (3-bar comparison plot)
  computations/s87_gate_verdicts.txt

GPU path: torch.linalg for D_K spectrum cache verification (eigenvalue re-derivation
not required if SHA matches cache); CPU sufficient for the 3-class Mellin moment
arithmetic (O(155984) sums per class).
```

### 7. Machinery pin (PRDR — every free parameter)

| Parameter | Pin |
|:----------|:----|
| `L_max` | 10 (canonical) |
| `scheme` | Mellin-cone substrate-distance-1 evaluation (s=2 / s=3 residues) |
| `convention` | F_4-multiplier-vector (3-class sub-family of 5-atlas); SCHEMATIC level per `substrate-first-canonical-sourcing.md` §iv |
| `n_eval` | 3 (one per F_4 sub-family class) |
| `scan_range` | N/A (3 discrete classes) |
| `tolerance` | RATIO ≤ 0.01 for PASS; RATIO > 0.05 for FAIL; intermediate INFO band |
| `random_seed` | None (deterministic) |
| `GPU path` | `torch.linalg.eigh` only on cache-verification re-derivation; CPU otherwise with `OMP_NUM_THREADS=8` |
| `regulator_family_pin` | F_4 multiplier-vector (sub-family of 5-atlas) |
| `n_classes_pin` | 3 (Class 1, Class 2, Class 3) |
| `cross_check_regulators` | sqrt-Heaviside (cutoff) AND Gaussian-Mellin (zeta) per class |
| `level_pin` | SCHEMATIC per substrate-first-canonical-sourcing.md §iv (uses SCHEMATIC `_spectral_action_regulators.py` helpers) |
| `f4_subfamily_sha` | `<RUNTIME-LATE-BIND>` from §VII.K-PROP |
| `atlas_def_sha` | `<CANONICAL>` from `_spectral_action_regulators.py` |
| `c_beta_def_sha` | `<RUNTIME-LATE-BIND>` from W-6 workshop file |

PRU Class-8 status: every parameter pinned; only the two SHAs are runtime-late-bind
(dynamic-input convention).

### 8. Expected output 4-tuple
`(value=<delta_C_beta>, scheme=Mellin-cone-substrate-distance-1-SCHEMATIC, convention=F_4-multiplier-vector, L_max=10)`

### 9. PASS/FAIL/INFO thresholds (with tolerance rule)

- **PASS**: `delta_C_beta ≤ 0.01` (RATIO across 3 F_4 sub-family classes) AND
  per-class scheme-invariance ≤ 1e-3 (cross-check Step D) AND regime_verdict=VALID.
  C-β is UV-cutoff-immunized across the F_4 multiplier-vector sub-family.
- **INFO**: `0.01 < delta_C_beta ≤ 0.05` (intermediate band) OR regime_verdict=MARGINAL.
  Partial immunization; one or two classes carry sub-percent cutoff-dependence.
- **FAIL**: `delta_C_beta > 0.05` OR regime_verdict=BREAKDOWN OR per-class
  scheme-invariance fails (Step D > 1e-3). The F_4 multiplier-vector sub-family
  carries cross-cutoff dispersion; C-β is NOT a substrate-canonical moment within
  this sub-family.

Tolerance-rule class: RATIO.

### 10. Substitution chain (MANDATORY — direction claim on cutoff immunization)

```
Definition 1: C-β_c = Res[M_c(s); s=2] / Res[M_c(s); s=3]
              [per-class Mellin-cone substrate-distance-1 ratio, c ∈ {1,2,3}]

Definition 2: M_c(s) = ∫_0^∞ t^{s-1} R_c(t) Tr(e^{-t·D_K^2}) dt
              [regulator-c-weighted Mellin transform; R_c is the F_4 multiplier-vector
              regulator for class c]

Definition 3: delta_C_beta = max_{c,c'} |C-β_c − C-β_{c'}| / |mean({C-β_c})|

Step 1 (substitute Mellin-cone evaluation):
  C-β_c = (Res[∫ t^{s-1} R_c(t) Z(t) dt; s=2]) / (Res[∫ t^{s-1} R_c(t) Z(t) dt; s=3])
  where Z(t) = Tr(e^{-t·D_K^2}) = ∑_λ e^{-t·λ²} is the regulator-INDEPENDENT
  heat kernel of D_K^{≤10}.

Step 2 (factor regulator from kernel):
  Res[M_c(s); s=k] = (regulator-c specific multiplier at pole s=k) · (Z-residue at s=k)
                   = μ_c(s=k) · ρ(s=k)
  where ρ(s=k) is regulator-INDEPENDENT (substrate-spectral) and μ_c is the
  regulator-c multiplier at pole s=k.

Step 3 (simplify the ratio):
  C-β_c = (μ_c(2) · ρ(2)) / (μ_c(3) · ρ(3))
        = (μ_c(2) / μ_c(3)) · (ρ(2) / ρ(3))
  Therefore: delta_C_beta = max_{c,c'} |(μ_c(2)/μ_c(3)) − (μ_{c'}(2)/μ_{c'}(3))|
                             / |mean ratios|.

Step 4 (read direction from canonical form):
  If the F_4 multiplier-vector sub-family satisfies (μ_c(2)/μ_c(3)) = const across
  c ∈ {1,2,3}, then delta_C_beta = 0 EXACTLY  ⇒  PASS-immunization.
  Empirically this holds at machine precision iff the F_4 sub-family is closed
  under the Mellin-cone substrate-distance-1 ratio operation. The S86 W-8
  4-channel LAYER-2 finding pins this as a structural prediction; W7-2 verifies
  numerically.

Conclusion: PASS ⟺ F_4 sub-family shares a single substrate-distance-1 Mellin-cone
ratio (UV-cutoff immunization). FAIL ⟺ the sub-family fails closure under the
substrate-distance-1 ratio (a cutoff-dependence remains).
```

### 11. What PASSES/FAILS MEAN for solution space

- **PASS**: F_4 multiplier-vector sub-family is UV-cutoff-immunized at the
  substrate-distance-1 Mellin-cone ratio. Pins C-β as a substrate-canonical moment
  within the F_4 sub-family. Strengthens S86 W-8 §VII.K-PROP 4-channel LAYER-2
  decomposition (the F_4 sub-family is structurally closed under Mellin-cone
  substrate-distance-1). Eligible for §VII.K-PROP cross-citation in CF-44 + CF-50
  HBW-audit downstream.
- **INFO**: Partial immunization. The F_4 sub-family is approximately closed
  but a small (sub-5%) cutoff-dependence remains. Document which class is the
  outlier; flag for L_max-extension scan in S88+.
- **FAIL**: F_4 sub-family is NOT closed under substrate-distance-1 Mellin-cone
  ratio. C-β is regulator-DEPENDENT within this sub-family. Closes the
  substrate-canonical interpretation of C-β at the F_4 level and forces re-spec
  under per-class C-β maps. CF-44 + CF-50 must respect per-class restrictions
  rather than F_4-collective claims.

### 12. Effort estimate
~6-8h runtime. Dominated by per-class Mellin-cone residue evaluation (3 classes ×
2 residue poles × ~155984 spectrum sums) plus the cross-check Step D under two
independent regulator schemes. CPU-only for the arithmetic; cache verification
GPU-accelerated.

### 13. Substrate-framing reminder
The F_4 multiplier-vector sub-family is a **substrate-IS** structural decomposition
of the 5-atlas — the 3 classes are spectral-triple-structure projections of D_K^{≤10},
NOT cutoff-prescription containers. The C-β coefficient measured per class is a
substrate-spectral moment evaluated at substrate-distance-1; the "UV cutoff" label is
a regulator-bookkeeping convention NOT a container the moment lives in. Per
`.claude/rules/phononic-framing.md` §"IS Space, Not IN Space": C-β IS the
substrate-distance-1 ratio (not "the value of C-β IN regulator c"). Cross-class
agreement establishes substrate-canonicity; cross-class disagreement establishes
that the F_4 sub-family carries internal regulator-bookkeeping fragility. Either
verdict is structural; no narrative spin.

```yaml
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
```

---

## §W7-3. S87-W6-C-GAMMA-WEAK-PER-CLASS (CF-44)

### 1. Gate ID
`S87-W6-C-GAMMA-WEAK-PER-CLASS` (carry-forward CF-44; compute-carryforward.md W-7 CF-3
attributing lizzi). HEAVY.

### 2. Trigger
`[VERIFY]` (substitution chain mandatory — gate makes direction claims about
per-class Λ_anom_internal under Weyl-rescaling).

### 3. Classification
**GEOMETRIC**. C-γ-WEAK is the Weyl-rescaling-derived anomaly-internal scale Λ_anom_internal
arising from the conformal-anomaly contribution to the spectral action. Per-L1-class
evaluation projects this onto the 5-class L1 partition of the F_2 spectral cluster.

### 4. Agent type
**Runtime primary**: `lizzi-spectral-functional-theorist` (sole owner per W-7
attribution; lizzi specialty: anomaly-derived spectral functionals per
`feedback_agent-roster.md` cross-citation).

No co-sign agents; this is single-axis spectral-functional with no transit / connes
content.

### 5. Hypothesis
Λ_anom_internal, when evaluated per L1-class under the Weyl-rescaling family,
admits one of three structural readings: (R1) class-INDEPENDENT (one anomaly
scale, the 5 classes are bookkeeping); (R2) class-FACTORIZED (Λ_anom_internal
= Λ_global · class-multiplier; 5 classes share a scale but differ by integer
multipliers); (R3) class-INDEPENDENTLY-DETERMINED (5 distinct anomaly scales).
The gate decides among R1 / R2 / R3 numerically.

### 6. Method (complete dispatch prompt for runtime)

```
Dispatch prompt for `lizzi-spectral-functional-theorist`:

You are computing the C-γ-WEAK Weyl-rescaling Λ_anom_internal for each of 5
L1-classes per S87-W7-3 (S87-W6-C-GAMMA-WEAK-PER-CLASS, carry-forward CF-44 from
lizzi, compute-carryforward.md W-7 CF-3). HEAVY effort estimate; budget ~10-14h
including the per-class Weyl-rescaling integration.

Required imports:
  from canonical_constants import *
  import numpy as np
  import torch
  import hashlib
  import json
  import os
  os.environ.setdefault('OMP_NUM_THREADS', '8')

Inputs (load + SHA-pin in first 20 lines of stdout):
  1. 5-class L1 partition definition from W-9 STAGE-1 landing (or workshop fallback):
     `sessions/permanent-results-registry.md` §Joint-F2-Class-Path-c-Theorem
     SHA: <RUNTIME-LATE-BIND from CF-54 OR W-9 workshop file>
  2. C-γ-WEAK definition (S86 W-6 source):
     `sessions/archive/session-86/session-86-w6-workshop.md` §C-γ-WEAK-Weyl-rescaling
     SHA: <RUNTIME-LATE-BIND from W-6 workshop file>
  3. D_K^{≤10} spectrum cache:
     `computations/s84_spectrum_cache_L12_tau019.npz`
     SHA: <CANONICAL>
  4. Weyl-rescaling family definition:
     `computations/_spectral_action_regulators.py` (SCHEMATIC-tagged) —
     `weyl_rescale_family(omega)` callable
     SHA: <CANONICAL>
  5. (Optional input pin from W7-1) per-class xi_E_GGE_inv values from CF-42:
     `computations/s87_w7_ic_per_class_verify.npz` if W7-1 has landed at
     compute time; otherwise compute Step A from raw partition + spectrum.
     SHA: <RUNTIME-LATE-BIND from W7-1 npz>

Computation steps:
  Step A. For each L1-class c ∈ {1,2,3,4,5}, identify the per-class restriction
          P_c of the spectrum (per W-9 STAGE-1 partition definition).
  Step B. For each c, compute the per-class Weyl-rescaling integral:
            Λ_anom_internal_c = Res[Mellin∫ t^{s-1} ω^4(t) Z_c(t) dt; s=4-pole]
                              / Res[Mellin∫ t^{s-1} ω^2(t) Z_c(t) dt; s=2-pole]
          where Z_c(t) = Tr_{P_c}(e^{-t·D_K^2}) is the per-class restriction
          of the heat kernel and ω(t) is the Weyl-rescaling profile per the
          C-γ-WEAK family definition.
  Step C. Test READING R1 (class-INDEPENDENT): compute
            R1_dispersion = std({Λ_anom_internal_c}) / mean({Λ_anom_internal_c}).
          R1 holds if R1_dispersion ≤ 0.02 (RATIO; tight 5-class consensus).
  Step D. Test READING R2 (class-FACTORIZED): for each c, compute the integer-multiplier
          fit:
            Λ_anom_internal_c = Λ_global · n_c, n_c ∈ {1,2,3,4,5,...}
          Find Λ_global, {n_c} minimizing residual; R2 holds if max residual
          ≤ 0.05 (RATIO) AND {n_c} is non-trivial (not all 1).
  Step E. Test READING R3 (independent): R3 holds if neither R1 nor R2 holds AND
          per-class values are individually well-defined (each has finite Mellin
          residue at the s=4-pole / s=2-pole).
  Step F. Cross-check: re-evaluate Λ_anom_internal_c under TWO different Weyl
          profiles ω_a(t) = exp(-t/Λ²) and ω_b(t) = (1+t/Λ²)^{-1} for each class,
          verify per-class Λ_anom_internal_c is profile-INVARIANT within RATIO
          ≤ 1e-2 (anomaly-derived scale should be profile-invariant by
          construction).
  Step G. Compute closure SHA: SHA-256 of the ordered input-pin map
          {class_partition_sha, c_gamma_def_sha, dk_spectrum_sha, weyl_family_sha,
          n_classes_pin=5, profile_a_pin, profile_b_pin}.

Decision rule (PASS/FAIL/INFO; composite collapse per gate-verdicts.md):
  sign_verdict   = N/A (Λ_anom_internal is positive by construction).
  magnitude_verdict = PASS if R1 holds (dispersion ≤ 0.02) OR R2 holds (integer
                      factorization with residual ≤ 0.05),
                      INFO if neither R1 nor R2 holds but R3 valid (5 finite,
                      independent scales),
                      FAIL if any class produces non-finite or sign-inconsistent
                      Λ_anom_internal_c.
  regime_verdict = VALID if all 5 classes' Mellin integrals converge at both
                   s=2 and s=4 poles,
                   MARGINAL if 1-2 classes graze convergence boundary,
                   BREAKDOWN if ≥3 classes fail convergence.

Verdict line append (atomic):
  S87-W6-C-GAMMA-WEAK-PER-CLASS: <PASS|FAIL|INFO> -- value=<R1_dispersion> \\
    scheme=Weyl-rescaling-Mellin convention=C-gamma-WEAK-per-L1-class \\
    L_max=10 sha256=<64-char closure>

Plus dual-SHA companion comment row.
Plus S87+ schema-v2 3-tuple annotation.

Output file targets:
  computations/s87_w7_c_gamma_weak_per_class.py
  computations/s87_w7_c_gamma_weak_per_class.npz   (5 per-class Λ_anom_internal_c)
  computations/s87_w7_c_gamma_weak_per_class.png   (5-bar comparison + R1/R2/R3 fit overlay)
  computations/s87_gate_verdicts.txt

GPU path: torch.linalg for per-class spectrum projection batches (5 projections;
recommend RX 9070 XT batch evaluation; ~1-2h wall-clock vs ~6h CPU); CPU
fallback acceptable with OMP_NUM_THREADS=8.
```

### 7. Machinery pin (PRDR — every free parameter)

| Parameter | Pin |
|:----------|:----|
| `L_max` | 10 (canonical) |
| `scheme` | Weyl-rescaling-Mellin (s=4-pole / s=2-pole ratio) |
| `convention` | C-gamma-WEAK-per-L1-class (5-class restriction; SCHEMATIC level per `substrate-first-canonical-sourcing.md` §iv) |
| `n_eval` | 5 (one per L1-class) |
| `scan_range` | N/A (5 discrete classes; Weyl profile pinned per Step F cross-check pair) |
| `tolerance` | RATIO ≤ 0.02 for R1 PASS; RATIO ≤ 0.05 for R2 PASS; profile-invariance ≤ 1e-2 for cross-check |
| `random_seed` | None |
| `GPU path` | `torch.linalg.eigh` on RX 9070 XT (recommended); CPU fallback with `OMP_NUM_THREADS=8` |
| `weyl_profile_a_pin` | ω_a(t) = exp(-t/Λ²) |
| `weyl_profile_b_pin` | ω_b(t) = (1+t/Λ²)^{-1} |
| `level_pin` | SCHEMATIC per `substrate-first-canonical-sourcing.md` §iv |
| `n_classes_pin` | 5 (L1-class partition) |
| `class_partition_sha` | `<RUNTIME-LATE-BIND>` from CF-54 OR W-9 workshop |
| `c_gamma_def_sha` | `<RUNTIME-LATE-BIND>` from W-6 workshop file |
| `weyl_family_sha` | `<CANONICAL>` from `_spectral_action_regulators.py` |

PRU Class-8 status: every parameter pinned; only the two `<RUNTIME-LATE-BIND>` SHAs
are dynamic-input (acceptable per the convention).

### 8. Expected output 4-tuple
`(value=<R1_dispersion>, scheme=Weyl-rescaling-Mellin, convention=C-gamma-WEAK-per-L1-class, L_max=10)`

### 9. PASS/FAIL/INFO thresholds (with tolerance rule)

- **PASS**: (R1 holds: `R1_dispersion ≤ 0.02`) OR (R2 holds: integer-factorization
  residual ≤ 0.05 with non-trivial {n_c}). Profile-invariance (Step F) ≤ 1e-2 and
  regime_verdict=VALID. Λ_anom_internal admits a structural per-class reading
  (one global scale or integer-factorized).
- **INFO**: Neither R1 nor R2 holds but R3 valid (5 finite, independent scales).
  The 5 classes carry independent anomaly scales; no structural reduction. Profile-
  invariance still holds. The 5-class partition is operationally meaningful but
  Λ_anom_internal is per-class-DETERMINED.
- **FAIL**: Any class produces non-finite Λ_anom_internal_c (Mellin divergence)
  OR sign-inconsistent value OR profile-invariance breaks (Step F > 1e-2)
  OR regime_verdict=BREAKDOWN. Anomaly-derived scale fails per-class consistency
  check; per-class evaluation is unreliable for this regulator family.

Tolerance-rule class: RATIO.

### 10. Substitution chain (MANDATORY — direction claim on R1 vs R2 vs R3)

```
Definition 1: Λ_anom_internal_c = Res[N_c(s); s=4] / Res[N_c(s); s=2]
              [per-class anomaly-internal scale via Weyl-rescaling Mellin moment]

Definition 2: N_c(s) = ∫_0^∞ t^{s-1} ω(t) Z_c(t) dt
              Z_c(t) = ∑_{λ ∈ P_c·spec(D_K)} e^{-t·λ²}
              [class-c Mellin-Weyl moment]

Definition 3: R1 (class-INDEPENDENT): Λ_anom_internal_c = Λ_global ∀c
Definition 4: R2 (class-FACTORIZED): Λ_anom_internal_c = Λ_global · n_c, n_c ∈ ℤ^+
Definition 5: R3 (class-INDEPENDENTLY-DETERMINED): {Λ_anom_internal_c} 5 distinct
              well-defined scales with no structural relation

Step 1 (substitute heat kernel per class):
  N_c(s) = ∫ t^{s-1} ω(t) ∑_{λ ∈ P_c·spec} e^{-t·λ²} dt
         = ∑_{λ ∈ P_c·spec} ∫ t^{s-1} ω(t) e^{-t·λ²} dt
         = ∑_{λ ∈ P_c·spec} (1/λ^{2s}) · Γ(s) · μ_ω(s)
  [factor regulator multiplier μ_ω(s) from Mellin transform of ω]

Step 2 (factor regulator from class projector):
  N_c(s) = μ_ω(s) · Γ(s) · ζ_c(2s)
  where ζ_c(2s) = ∑_{λ ∈ P_c·spec} 1/λ^{2s} is the per-class spectral zeta.

Step 3 (simplify ratio):
  Λ_anom_internal_c = Res[N_c; s=4] / Res[N_c; s=2]
                    = (μ_ω(4) Γ(4) Res[ζ_c(2s); s=4]) / (μ_ω(2) Γ(2) Res[ζ_c(2s); s=2])
                    = (μ_ω(4)/μ_ω(2)) · (Γ(4)/Γ(2)) · (Res[ζ_c(8)]/Res[ζ_c(4)])
                    = K_ω · (Res[ζ_c(8)]/Res[ζ_c(4)])
  where K_ω = (μ_ω(4)/μ_ω(2)) · 6 is regulator-dependent but class-INDEPENDENT.

Step 4 (read direction from canonical form):
  Λ_anom_internal_c / Λ_anom_internal_{c'} = Res[ζ_c(8)/ζ_c(4)] / Res[ζ_{c'}(8)/ζ_{c'}(4)]
                                            = ratio of per-class spectral-zeta ratios.
  R1 ⟺ this ratio = 1 ∀(c,c')  ⟺  per-class zeta ratios are class-INVARIANT.
  R2 ⟺ this ratio is rational with small integer numerator/denominator.
  R3 ⟺ this ratio is irrational and dispersed across 5 classes.

Conclusion: PASS-R1 ⟺ the F_2 spectral-cluster preserves the s=4/s=2 zeta-ratio
across L1 partition (strong structural integrality). PASS-R2 ⟺ the L1 partition
admits an integer-grading on the anomaly scale (weaker but still structural).
INFO-R3 ⟺ no structural relation; 5 independent scales. FAIL ⟺ Mellin breakdown
or profile dependence (anomaly-scale evaluation is unreliable).
```

### 11. What PASSES/FAILS MEAN for solution space

- **PASS-R1**: Λ_anom_internal is class-INDEPENDENT; the 5-class L1 partition is
  bookkeeping for anomaly-scale evaluation. Strongest structural reading. Eligible
  to anchor a §VII candidate "anomaly-scale F_2-class invariance theorem". Cross-cite
  from CF-54 STAGE-1 clause (e) (lizzi-side).
- **PASS-R2**: Λ_anom_internal is class-FACTORIZED with integer multipliers
  {n_c}. Structurally non-trivial; per-class anomaly scales differ by small
  integer factors. Eligible to anchor an "integer-graded anomaly multiplier"
  registry candidate. Document {n_c} integers explicitly in npz.
- **INFO-R3**: 5 independent anomaly scales with no structural relation. Operationally
  meaningful (each class has finite Λ_anom_internal_c) but no STRUCTURAL reduction.
  Sets a floor on anomaly-scale heterogeneity; CF-44 records this as a calibration
  point for any S88+ "structural anomaly-scale convergence" gate.
- **FAIL**: Anomaly-scale evaluation per-class is unreliable. Closes the per-class
  Λ_anom_internal interpretation; downstream gates citing per-class anomaly
  contributions must respect this and use the global Λ_anom_internal only.

### 12. Effort estimate
~10-14h runtime. HEAVY. Dominated by 5-class Weyl-rescaling Mellin integration
with profile-invariance cross-check (5 classes × 2 Weyl profiles × Mellin residue
extraction at 2 poles). GPU path on RX 9070 XT cuts wall-clock to ~3-4h; CPU
fallback ~8-12h.

### 13. Substrate-framing reminder
Λ_anom_internal is the **substrate-IS** internal anomaly-scale of the spectral
action — derived from the conformal anomaly's Weyl-rescaling response of the
D_K^{≤10} heat kernel. The 5 L1-classes are spectral-cluster restrictions, NOT
container-anomaly-scales. Per `.claude/rules/phononic-framing.md`: the per-class
restriction P_c·Λ_anom_internal IS the substrate-spectral content, not "the
value of Λ_anom_internal IN class c". Reading R1 frames the 5 classes as one
substrate-canonical anomaly-scale reorganized by the F_2 cluster; R2 frames
them as integer-graded refinements of one scale; R3 frames them as 5 independent
substrate-spectral content evaluations. All three readings are substrate-IS
(none are container-IN); the gate decides which structural reading the
substrate's spectrum supports.

```yaml
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
```

---

## §W7-4. S87-LAYER-1-2-RETROACTIVE-AUDIT-FULL-ENUMERATION (CF-45)

### 1. Gate ID
`S87-LAYER-1-2-RETROACTIVE-AUDIT-FULL-ENUMERATION` (carry-forward CF-45;
compute-carryforward.md W-7 CF-4 attributing lizzi). HEAVY (1-2 wave equiv).

### 2. Trigger
`[AUDIT]` — mechanical full-enumeration LAYER-tagging walk across S78-onward
citation corpus. PASS criterion is artifact-existence-with-substantive-content
(every S78-onward 5-atlas / regulator-class / partition citation receives exactly
one LAYER tag with optional Stage-2.5 sub-tag); FAIL is unclassified citations
remaining or double-tagged citations.

### 3. Classification
**NON-PHONONIC (audit)**. The gate operates on the citation corpus, not on
substrate-physics observables. The 5-stage LAYER protocol is the methodology-floor
classification scheme established by S83 W2-G14 / S86 W2-15 (three-layer regulator
synthesis: L1 zeta + L2 Zubarev + L3 per-observable + UNPINNED + L0-INT integer-
intensive). Stage-2.5 sub-tag is the Layer-2-promotable subset identified by S84
W2c-19 UNPINNED-L2-AUDIT.

### 4. Agent type
**Runtime primary**: `lizzi-spectral-functional-theorist` (sole owner per W-7
attribution; lizzi specialty: the regulator-classification framework architecture).

This is an audit gate, not a physics computation. The runtime dispatch produces
a structured JSON enumeration of every S78-onward citation with its LAYER tag.

### 5. Hypothesis
Every S78-onward 5-atlas / regulator-class / partition citation in the framework
corpus admits exactly ONE classification under the 5-stage LAYER protocol
{L0-INT, L1, L2, L3, UNPINNED} with optional Stage-2.5 (L2-PROMOTABLE) sub-tag.
No citation is double-tagged; no citation remains unclassified.

### 6. Method (complete dispatch prompt for runtime)

```
Dispatch prompt for `lizzi-spectral-functional-theorist`:

You are executing a mechanical full-enumeration LAYER-tagging walk across the
S78-onward citation corpus per S87-W7-4 (S87-LAYER-1-2-RETROACTIVE-AUDIT-FULL-
ENUMERATION, carry-forward CF-45 from lizzi, compute-carryforward.md W-7 CF-4).
HEAVY (1-2 wave equiv).

Required imports:
  from canonical_constants import *
  import re
  import json
  import hashlib
  import os
  from pathlib import Path
  os.environ.setdefault('OMP_NUM_THREADS', '4')

Inputs (load + SHA-pin in first 20 lines of stdout):
  1. S78-onward session corpus root: `sessions/archive/session-78/` ... `sessions/archive/session-86/`
     SHA: <RUNTIME-COMPUTED — directory hash of all .md files>
  2. computation corpus: `computations/s78_*.py` ... `computations/s86_*.py`
     SHA: <RUNTIME-COMPUTED — directory hash>
  3. computation verdict files: `computations/s78_gate_verdicts.txt` ...
     `computations/s86_gate_verdicts.txt`
     SHA: <CANONICAL>
  4. 5-stage LAYER protocol definition:
     `.claude/rules/regulator-pin-discipline.md` (Sage-Exact extension §T1-15)
     AND `sessions/framework/registry/three-layer-regulator-synthesis.md` (S83 W2-G14)
     SHA: <CANONICAL>
  5. Stage-2.5 sub-tag definition (L2-PROMOTABLE):
     `sessions/archive/session-84/session-84-w2c-19-unpinned-l2-audit.md` (per agent-memory
     entry S84 W2c-19 UNPINNED-L2-AUDIT)
     SHA: <CANONICAL>

Computation steps:
  Step A. Enumerate the citation corpus. For each .md / .py file in the S78-onward
          range, regex-match citations of:
            - 5-atlas regulator names: ζ, Zubarev, SDW, Pauli-Villars, Mellin, anomaly,
              cutoff_sqrt, cutoff_exp, lattice (extensible per the 5-atlas canonical)
            - regulator-class tags: a_n^{<reg>} per `.claude/rules/regulator-pin-discipline.md`
            - L1/L2/L3 LAYER tags: the existing scheme tag in scripts + plan blocks
            - partition citations: §VII.<slot>, F_2-class, F_4-class, L1-class etc.
          Build a JSON structure: {filename: [citation_records]}.
  Step B. For each citation_record, classify under the 5-stage LAYER protocol:
            L0-INT  = integer-intensive citation (no regulator family; pure
                      structural integer like rank, codimension)
            L1      = zeta-axiomatic-native citation (Connes A1-A6 zeta regulator
                      per S83 W1-G3 EN3 theorem)
            L2      = Zubarev substrate-action citation (canonical-anchored
                      effacement-preserving per `regulator-convention-lockdown.md`)
            L3      = per-observable scheme tag (each observable carries its own
                      regulator pin)
            UNPINNED = citation lacks regulator pin entirely (legacy bare-a_n or
                       missing scheme tag)
          Apply optional STAGE-2.5 sub-tag (L2-PROMOTABLE) if the UNPINNED
          citation could be promoted to L2 per S84 W2c-19 promotion criteria
          (3/5 PROMOTE-L2 patterns; remaining 2 GENUINE-UNPINNED).
  Step C. Verify ONE-TAG-PER-CITATION constraint: each citation receives exactly
          one of {L0-INT, L1, L2, L3, UNPINNED}. Count double-tagged citations
          (PASS criterion: 0).
  Step D. Verify NO-UNCLASSIFIED constraint: every regex-matched citation
          receives a tag (PASS criterion: 0 unclassified).
  Step E. Compute LAYER distribution: {L0-INT: count, L1: count, L2: count, L3: count,
          UNPINNED: count, Stage-2.5: count}. Sanity-check against S86-close
          §VII.K-META distribution (S84 W2c-19 final state: 26 L0-INT, 2 L1, 1 L2,
          11 L3, 2 UNPINNED) — count drift from this baseline reflects S85+S86
          additions.
  Step F. Cross-check: re-grep specific high-leverage citations (e.g., the
          5-atlas members in `_spectral_action_regulators.py`, the Zubarev pins
          in `regulator-convention-lockdown.md`, the §VII.K-PROP entries) and
          verify the audit's tag for each matches manual inspection.
  Step G. Compute closure SHA: SHA-256 of the ordered input-pin map
          {corpus_root_sha, computation_corpus_sha, verdict_files_sha, layer_protocol_sha,
          stage_2_5_def_sha}.

Decision rule (PASS/FAIL/INFO; composite collapse per gate-verdicts.md):
  sign_verdict   = N/A (no signed direction; audit is structural).
  magnitude_verdict = PASS if (double-tagged count = 0) AND (unclassified count = 0)
                      AND (cross-check Step F: all sampled citations match audit tags),
                      INFO if (1 ≤ unclassified count ≤ 5) OR (1 ≤ double-tagged ≤ 3)
                      (small audit residual; documents which citations need manual
                      Stage-2.5 review),
                      FAIL otherwise.
  regime_verdict = VALID if S78-onward corpus enumeration completes without missing
                   files (every expected file is read),
                   MARGINAL if 1-3 files unreadable (logged with reason),
                   BREAKDOWN if ≥4 files unreadable.

Verdict line append (atomic):
  S87-LAYER-1-2-RETROACTIVE-AUDIT-FULL-ENUMERATION: <PASS|FAIL|INFO> -- \\
    value=<unclassified_count> scheme=5-stage-LAYER-protocol \\
    convention=S78-onward-corpus-with-Stage-2.5 L_max=N/A \\
    sha256=<64-char closure>

Plus dual-SHA companion comment row.
Plus S87+ schema-v2 3-tuple annotation.

Output file targets:
  computations/s87_w7_layer_audit_full_enumeration.py
  computations/s87_w7_layer_audit_full_enumeration.json
    (full {filename: [citation_records with tag]} enumeration)
  computations/s87_w7_layer_audit_full_enumeration_summary.png
    (LAYER distribution histogram + drift from S84 W2c-19 baseline)
  computations/s87_gate_verdicts.txt

GPU path: N/A (text enumeration; no linear algebra).
```

### 7. Machinery pin (PRDR — every free parameter)

| Parameter | Pin |
|:----------|:----|
| `L_max` | N/A (audit gate; no spectral computation) |
| `scheme` | 5-stage LAYER protocol per S83 W2-G14 + S84 W2c-19 |
| `convention` | S78-onward-corpus-with-Stage-2.5 sub-tag |
| `n_eval` | full enumeration (every regex-match in S78-onward .md + .py + verdict files) |
| `scan_range` | sessions/archive/session-78/ ... sessions/archive/session-86/ + computations/s78_*.py ... computations/s86_*.py |
| `tolerance` | INTEGER 0 for PASS (exact); 1-5 for INFO; >5 for FAIL |
| `random_seed` | None (deterministic regex enumeration) |
| `GPU path` | N/A |
| `regex_pattern_set` | 5-atlas names + regulator-class tags + LAYER tags + partition citations (full pattern set in script) |
| `layer_protocol_sha` | `<CANONICAL>` from `.claude/rules/regulator-pin-discipline.md` |
| `stage_2_5_def_sha` | `<CANONICAL>` from S84 W2c-19 audit reference |
| `corpus_root_sha` | `<RUNTIME-COMPUTED>` directory hash |
| `computation_corpus_sha` | `<RUNTIME-COMPUTED>` directory hash |
| `verdict_files_sha` | `<CANONICAL>` from S78-S86 verdict files |
| `baseline_distribution_pin` | S84 W2c-19 final: {L0-INT:26, L1:2, L2:1, L3:11, UNPINNED:2} |

PRU Class-8 status: every parameter pinned; the two `<RUNTIME-COMPUTED>` directory
hashes are computed at script start and pinned in stdout (not late-bind in the
plan-author sense; they are dynamic-input-by-construction).

### 8. Expected output 4-tuple
`(value=<unclassified_count>, scheme=5-stage-LAYER-protocol, convention=S78-onward-corpus-with-Stage-2.5, L_max=N/A)`

### 9. PASS/FAIL/INFO thresholds (with tolerance rule)

- **PASS**: `unclassified_count = 0` AND `double_tagged_count = 0` AND cross-check
  Step F: all sampled citations match audit tags AND regime_verdict=VALID.
  Every S78-onward citation has exactly one LAYER tag.
- **INFO**: `1 ≤ unclassified_count ≤ 5` OR `1 ≤ double_tagged_count ≤ 3` (small
  audit residual). Documents which specific citations require manual Stage-2.5
  review; the audit JSON enumerates them. Tolerable under no-tech-debt with
  in-session manual fix path declared in the working-paper section.
- **FAIL**: `unclassified_count > 5` OR `double_tagged_count > 3` OR
  regime_verdict=BREAKDOWN (≥4 files unreadable). Indicates either (a) the
  corpus contains citations the 5-stage protocol does not cover (forces
  protocol extension) or (b) the regex pattern set is incomplete (forces
  regex extension before re-running).

Tolerance-rule class: ABSOLUTE INTEGER (count of unclassified / double-tagged).

### 10. Substitution chain (MANDATORY — direction claim on classification completeness)

```
Definition 1: C = {citations} = ⋃_f regex_match(file_f, pattern_set)
              [the full S78-onward citation corpus]

Definition 2: T(c) = LAYER tag assigned to citation c by the audit script
              T : C → {L0-INT, L1, L2, L3, UNPINNED}
              s_2_5 : C × T → {None, STAGE-2.5} sub-tag for L2-promotable

Definition 3: unclassified_count = |{c ∈ C : T(c) is undefined}|
              double_tagged_count = |{c ∈ C : |{T_a(c), T_b(c)}| ≥ 2}|

Step 1 (substitute completeness condition):
  PASS predicate P_pass = (unclassified_count = 0) ∧ (double_tagged_count = 0)
                          ∧ (Step F sample-match = 100%)
                          ∧ (regime_verdict = VALID)

Step 2 (simplify to corpus-completeness):
  P_pass ⟺ T : C → {L0-INT, L1, L2, L3, UNPINNED} is a TOTAL FUNCTION
            with each c mapping to exactly one tag.

Step 3 (simplify to protocol-coverage):
  T total ⟺ the 5-stage LAYER protocol covers every citation pattern in C.
  Direction: if the protocol is COMPLETE (covers all citation patterns) then
  PASS; if the protocol is INCOMPLETE then INFO (small residual) or FAIL
  (large residual / corpus reading breakdown).

Step 4 (read direction from canonical form):
  PASS ⟺ S78-onward corpus is FULLY classified under the 5-stage protocol.
  INFO ⟺ small residual (1-5 unclassified or 1-3 double-tagged); manual fix
       in-session per no-tech-debt rule.
  FAIL ⟺ large residual or reading breakdown; protocol or regex set requires
       extension before re-run.

Conclusion: PASS pins the 5-stage LAYER protocol as COMPLETE for the S78-onward
corpus. INFO documents specific citations requiring manual Stage-2.5 review.
FAIL forces protocol/regex extension as a Stage-3 user-trigger event per
`.claude/rules/v3-closure-recovery.md` (plan-authoring defect: missing protocol
coverage).
```

### 11. What PASSES/FAILS MEAN for solution space

- **PASS**: 5-stage LAYER protocol is COMPLETE for S78-onward corpus. Pins the
  `regulator-pin-discipline.md` framework as covering the full citation corpus.
  Strengthens the methodology-floor LAYER-functor F image at the methodology
  layer (per `.claude/rules/epistemic-discipline.md` §"Layer-Decomposition" T2-7).
  CF-72 (S87-WAVE-CLASSIFICATION-RULE-VALIDATION) inherits this PASS as upstream
  evidence that the LAYER-tag protocol is operational.
- **INFO**: Small audit residual (1-5 unclassified / 1-3 double-tagged). Documents
  specific citations the protocol does not cover; forces manual Stage-2.5 review
  in-session per no-tech-debt rule. The bulk of the protocol is operational; the
  outlier citations may indicate either (i) novel citation patterns requiring
  pattern-set extension or (ii) latent UNPINNED citations the corpus carries from
  pre-S78. Logged in audit JSON for downstream consumption.
- **FAIL**: Protocol coverage is incomplete OR corpus reading breaks. Routes to
  Stage-3 user-trigger event: either extend the 5-stage protocol with a 6th level
  (e.g., L4 for novel regulator class) or extend the regex pattern set, then
  re-run. The FAIL is structural (the methodology-floor protocol does not yet
  cover the framework's actual citation corpus).

### 12. Effort estimate
~16-24h runtime. HEAVY (1-2 wave equivalents). Dominated by the corpus enumeration
(S78-onward .md + .py files; ~1000+ files across 9 sessions) and the per-citation
regex-classification step. CPU-only. The cross-check Step F (manual sampling of
specific high-leverage citations) takes ~4-6h alone; the full enumeration ~10-18h.

### 13. Substrate-framing reminder
This is an **AUDIT** gate operating on the methodology-floor citation corpus, not
on substrate-physics observables. Per `.claude/rules/epistemic-discipline.md`
§"Layer-Decomposition" T2-7 layer-functor F: this gate's PASS predicate is the
F-image of a substrate-physics PASS predicate at the methodology layer
("artifact-existence-with-substantive-content" replaces "value < threshold").
The 5-stage LAYER protocol IS the methodology-floor structural object; the audit
verifies that S78-onward citations are correctly mapped under T : C → tags. No
container-thinking arises here because the audit operates entirely within the
methodology-layer (no substrate / laboratory direction-of-explanation question).

```yaml
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
```

---

## §W7-5. S87-LATENT-WARRANT-CHECK-QUEUE (CF-46; head-of-queue spec only)

### 1. Gate ID
`S87-LATENT-WARRANT-CHECK-QUEUE` (carry-forward CF-46; compute-carryforward.md
W-7 CF-AVAIL-1..27 attributing lizzi+connes). NARROW per CV-CN-R3-4. Head-of-queue
4-field spec is pre-registered in this plan; the remaining ~25 are stub specs
deferred to S88+ as carry-forwards.

### 2. Trigger
`[VERIFY]` for the head-of-queue warrant-check; `[AUDIT]` for the full-queue
enumeration sub-step (which is mechanical and pre-registered as INFO-only).

### 3. Classification
**MIXED** (head-of-queue is PHONONIC if it tests substrate-spectral content;
NON-PHONONIC if it tests methodology-floor structure). The classification is
determined by the head-of-queue selection in §6 below; the full-queue enumeration
is NON-PHONONIC (audit).

### 4. Agent type
**Runtime primary**: `lizzi-spectral-functional-theorist` (sole owner per W-7
attribution).
**Cross-cited co-sign**: `connes-ncg-theorist` (warrant-check origin per
CV-CN-R3-4; consulted via input-SHA pin from W-7 workshop wrap-up text, NOT
spawned as collab agent).

The runtime dispatch is single-agent (lizzi); the connes cross-cite supplies
the warrant-check candidate list (the ~26 available items per CV-CN-R3-4
NARROW scope).

### 5. Hypothesis
Of the ~26 latent warrant-check + fb_pair instantiations available per CV-CN-R3-4
NARROW scope, exactly ONE meets the head-of-queue selection rule (registry-grade
theorem + effort estimate ≤ 4h); the remaining ~25 are deferred to S88+ via
carry-forward 4-field stubs. The head-of-queue warrant-check returns a verdict
that either supports or refutes its underlying registry-grade theorem.

### 6. Method (complete dispatch prompt for runtime)

```
Dispatch prompt for `lizzi-spectral-functional-theorist`:

You are executing the head-of-queue warrant-check from the ~26 available latent
warrant-check + fb_pair instantiations per S87-W7-5 (S87-LATENT-WARRANT-CHECK-QUEUE,
carry-forward CF-46 from lizzi+connes, compute-carryforward.md W-7 CF-AVAIL-1..27).

DECISION RULE (head-of-queue selection — pre-registered in this plan):
  A warrant-check qualifies for compute-slot allocation iff:
    (a) The warrant-check tests a registry-grade theorem (i.e., the underlying
        statement is in `sessions/permanent-results-registry.md` at §VII.<slot>
        OR is a STAGE-1-CANDIDATE per `.claude/rules/joint-theorem-promotion.md`)
    AND
    (b) Effort estimate ≤ 4 hours.

  All other warrant-checks defer to S88+ with carry-forward 4-field stubs.

Required imports:
  from canonical_constants import *
  import numpy as np
  import torch  # if head-of-queue selects spectral-physics warrant
  import hashlib
  import json
  import os
  os.environ.setdefault('OMP_NUM_THREADS', '8')

Inputs (load + SHA-pin in first 20 lines of stdout):
  1. ~26 warrant-check available list from CV-CN-R3-4 NARROW scope:
     `sessions/archive/session-86/session-86-w7-workshop.md` §CV-CN-R3-4 (or equivalent
     workshop file location for the warrant-check enumeration)
     SHA: <RUNTIME-LATE-BIND from W-7 workshop file>
  2. permanent-results-registry.md (for head-of-queue selection rule (a)):
     `sessions/permanent-results-registry.md`
     SHA: <CANONICAL>
  3. canonical_constants.py (any framework constants the head-of-queue script
     consumes):
     `computations/canonical_constants.py`
     SHA: <CANONICAL>

Computation steps:
  Step A. Load the ~26 available warrant-check list. For each item, extract:
            (i)  underlying registry-target slot (§VII.<slot> or STAGE-1-CANDIDATE name)
            (ii) effort estimate (in hours)
            (iii) classification (PHONONIC / GEOMETRIC / NON-PHONONIC)
  Step B. Apply the head-of-queue selection rule:
            qualified = {w in available : (a) registry-grade AND (b) effort ≤ 4h}
            head_of_queue = argmin_w (effort(w))   over qualified
            (tie-break by registry-slot lexical order)
  Step C. Pre-register the head-of-queue warrant-check 4-field spec:
            What     : <warrant-check description>
            Inputs   : <SHA-pinned input list>
            Gate     : <PASS/FAIL/INFO criterion>
            Effort   : <≤ 4h>
          Emit this 4-field spec to the working-paper section AND
          computations/s87_w7_warrant_check_head_4field.json.
  Step D. EXECUTE the head-of-queue warrant-check itself:
            (i) Load its specific inputs (per the 4-field spec).
            (ii) Compute its specific PASS/FAIL/INFO criterion.
            (iii) Emit a SECONDARY verdict line for the warrant-check itself,
                  with gate ID `S87-WARRANT-HEAD-<slot-id>` (where <slot-id>
                  is the registry slot the warrant-check tests).
  Step E. Enumerate the remaining ~25 deferred items as 4-field stubs:
            For each item NOT selected as head-of-queue, emit a stub spec
            with all four fields populated as STUB-PENDING-S88-PLAN-AUTHOR.
            Save to computations/s87_w7_warrant_check_queue_stubs.json.
  Step F. Compute closure SHA: SHA-256 of the ordered input-pin map
          {available_list_sha, registry_sha, canonical_constants_sha,
           selection_rule_pin = "(a) registry-grade AND (b) effort ≤ 4h",
           head_of_queue_id, n_qualified, n_deferred = 25}.

Decision rule (PASS/FAIL/INFO; composite collapse per gate-verdicts.md):
  This gate's primary verdict is the QUEUE-HEAD-EXECUTION verdict:
    sign_verdict   = N/A (queue-discipline has no signed direction).
    magnitude_verdict = PASS if (n_qualified ≥ 1) AND (head-of-queue executes
                        with verdict PASS or INFO) AND (n_deferred = 25 stubs
                        emitted with all 4 fields populated),
                        INFO if (n_qualified ≥ 1) AND head-of-queue verdict is FAIL
                        but stubs correctly emitted (queue-discipline operational
                        even when warrant-check refutes its theorem),
                        FAIL if n_qualified = 0 (no item meets head-of-queue rule;
                        the entire ~26-item queue defers to S88+ as a single block)
                        OR stubs emission breaks.
    regime_verdict = VALID (queue-discipline always operational; no regime
                     boundary).

  SECONDARY verdict (for the warrant-check itself, separate gate ID
  `S87-WARRANT-HEAD-<slot-id>`):
    Per the head-of-queue 4-field spec PASS/FAIL/INFO criterion.

Verdict line append (atomic; TWO verdict lines):

  PRIMARY (queue-discipline gate):
    S87-LATENT-WARRANT-CHECK-QUEUE: <PASS|FAIL|INFO> -- value=<n_qualified> \\
      scheme=head-of-queue-rule convention=lizzi+connes-CV-CN-R3-4-NARROW \\
      L_max=N/A sha256=<64-char closure>

  SECONDARY (warrant-check execution gate):
    S87-WARRANT-HEAD-<slot-id>: <PASS|FAIL|INFO> -- value=<warrant-check value> \\
      scheme=<warrant-check scheme> convention=<warrant-check convention> \\
      L_max=<warrant-check L_max> sha256=<64-char closure-2>

Plus dual-SHA companion comment rows for both.
Plus S87+ schema-v2 3-tuple annotations for both.

Output file targets:
  computations/s87_w7_warrant_check_queue.py
  computations/s87_w7_warrant_check_head_4field.json (head-of-queue 4-field spec)
  computations/s87_w7_warrant_check_head_<slot>.npz (warrant-check data, depends on head)
  computations/s87_w7_warrant_check_queue_stubs.json (~25 deferred 4-field stubs)
  computations/s87_w7_warrant_check_queue_summary.png (queue distribution + selection)
  computations/s87_gate_verdicts.txt (BOTH verdict lines append)

GPU path: Depends on head-of-queue selection. If head selects a spectral warrant
(D_K eigenvalue check), torch.linalg on RX 9070 XT; if methodology audit, CPU only.
```

### 7. Machinery pin (PRDR — every free parameter)

| Parameter | Pin |
|:----------|:----|
| `L_max` | N/A for queue-discipline gate; head-of-queue's L_max determined by selection (likely 10) |
| `scheme` | head-of-queue-rule (selection rule pinned in §6 Step B) |
| `convention` | lizzi+connes-CV-CN-R3-4-NARROW |
| `n_eval` | ~26 available items enumerated; 1 selected as head; ~25 deferred as stubs |
| `scan_range` | N/A (discrete enumeration) |
| `tolerance` | n_qualified ≥ 1 for PASS; n_qualified = 0 for FAIL |
| `random_seed` | None (deterministic queue ordering by lexical tie-break) |
| `GPU path` | Depends on head selection; CPU sufficient for queue-discipline gate |
| `selection_rule_pin` | "(a) registry-grade AND (b) effort ≤ 4h" |
| `tie_break_pin` | registry-slot lexical order |
| `n_deferred_pin` | 25 (the ~26 items minus the head) |
| `available_list_sha` | `<RUNTIME-LATE-BIND>` from W-7 workshop file §CV-CN-R3-4 |
| `registry_sha` | `<CANONICAL>` from `permanent-results-registry.md` |
| `canonical_constants_sha` | `<CANONICAL>` |

PRU Class-8 status: queue-discipline gate's parameters fully pinned. The
head-of-queue's machinery pins are determined at Step B (after selection); the
plan-author pre-registers the selection rule, NOT the specific head-of-queue
values (which depend on the ~26 available list contents at runtime). This is a
QUEUE-DISCIPLINE pre-registration: the SELECTION RULE is plan-frozen, the
SELECTED ITEM is runtime-determined, and the runtime-determined item's full
machinery pin map is emitted in the verdict line BEFORE its execution begins.

### 8. Expected output 4-tuple
PRIMARY: `(value=<n_qualified>, scheme=head-of-queue-rule, convention=lizzi+connes-CV-CN-R3-4-NARROW, L_max=N/A)`
SECONDARY: `(value=<warrant-check value>, scheme=<head scheme>, convention=<head convention>, L_max=<head L_max>)`

### 9. PASS/FAIL/INFO thresholds (with tolerance rule)

PRIMARY (queue-discipline):
- **PASS**: `n_qualified ≥ 1` AND head-of-queue executes (its secondary verdict
  is PASS or INFO, not FAIL) AND `n_deferred = 25` stubs emitted with all 4
  fields populated.
- **INFO**: `n_qualified ≥ 1` AND head-of-queue secondary verdict is FAIL but
  stubs correctly emitted. Queue-discipline is operational even when the head
  warrant-check refutes its underlying registry theorem (a structurally
  informative outcome).
- **FAIL**: `n_qualified = 0` (no item meets selection rule; entire queue defers
  to S88+ as a block — itself a NEEDS-DECISION carry-forward) OR stubs emission
  breaks.

SECONDARY (warrant-check execution):
- Per the head-of-queue 4-field spec's specific PASS/FAIL/INFO criterion (set at
  Step C of §6).

Tolerance-rule class: PRIMARY is INTEGER (`n_qualified ≥ 1`); SECONDARY is
warrant-check-specific.

### 10. Substitution chain (MANDATORY — direction claim on queue-discipline)

```
Definition 1: A = {available warrant-check items} from CV-CN-R3-4 NARROW scope, |A| ≈ 26

Definition 2: Q(w) = qualifies(w) ⟺ registry_grade(w) ∧ (effort(w) ≤ 4h)
              [the head-of-queue selection rule]

Definition 3: head_of_queue = argmin_w effort(w) over {w ∈ A : Q(w)},
              tie-break by lexical(registry_slot(w)).

Definition 4: deferred = A \ {head_of_queue}, |deferred| ≈ 25

Step 1 (substitute selection rule):
  qualified = {w ∈ A : registry_grade(w) ∧ (effort(w) ≤ 4h)}
  n_qualified = |qualified|

Step 2 (simplify queue-discipline PASS):
  PASS_primary ⟺ (n_qualified ≥ 1) ∧ executes(head_of_queue) ∧ (|deferred| = 25)

Step 3 (simplify SECONDARY interaction):
  SECONDARY verdict is INDEPENDENT of PRIMARY (separately graded against its
  own 4-field spec). PRIMARY = INFO when SECONDARY = FAIL preserves
  queue-discipline operational pin while letting the warrant-check's
  scientific verdict route to the registry it tests.

Step 4 (read direction from canonical form):
  PRIMARY-PASS ⟺ queue-discipline operational AND head warrant-check supports
              its theorem.
  PRIMARY-INFO ⟺ queue-discipline operational AND head warrant-check refutes
              its theorem (refutation is informative).
  PRIMARY-FAIL ⟺ no item qualifies under selection rule (queue defers as
              a block; planning-defect signal at S87 plan-authorship time;
              re-routes to S88+ NEEDS-DECISION).

Conclusion: PRIMARY verdict pins queue-discipline operationality. SECONDARY
verdict pins the specific warrant-check's scientific verdict against the
registry theorem it tests. Both verdict lines are appended; both contribute
to S87 closeout.
```

### 11. What PASSES/FAILS MEAN for solution space

PRIMARY:
- **PASS**: Queue-discipline operational; one warrant-check from the ~26 available
  meets selection rule and executes with PASS/INFO verdict. Strengthens
  CV-CN-R3-4 NARROW scope as a workable queueing pattern. Logged in audit-output
  §4.3 queue with the deferred ~25 items as 4-field stubs for S88+.
- **INFO**: Queue-discipline operational but the executed warrant-check FAILED
  its scientific test (refuting its registry-grade theorem). The PRIMARY-INFO
  outcome is structurally meaningful: queue-discipline is operational EVEN WHEN
  the warrant-check refutes its theorem. The registry-target theorem's status is
  updated per the SECONDARY verdict.
- **FAIL**: No item qualifies under selection rule. The entire ~26-item queue
  defers to S88+ as a single block — flagging an S87 plan-authorship signal that
  the selection rule (registry-grade AND effort ≤ 4h) is too strict for the
  available pool. Routes to NEEDS-DECISION at S88 plan-authorship: relax the
  selection rule (e.g., effort ≤ 6h) OR accept the block-defer.

SECONDARY:
- Per the head-of-queue 4-field spec; depends on which warrant-check is selected
  and which registry theorem it tests.

### 12. Effort estimate
~3-5h runtime for queue-discipline gate (PRIMARY): enumeration + selection +
stub emission. The SECONDARY warrant-check execution is bounded at 4h by
construction (selection rule (b)). Total budget: ~7-9h combined.

### 13. Substrate-framing reminder
The queue-discipline gate is a **METHODOLOGY-floor** structural object: it operates
on the latent warrant-check pool, not on substrate-physics observables. The
head-of-queue's underlying warrant-check IS substrate-physics (per §5 hypothesis,
the head tests a registry-grade theorem). Per `.claude/rules/epistemic-discipline.md`
§"Layer-Decomposition" T2-7 layer-functor F: the queue-discipline gate is the
F-image of a substrate-physics PASS predicate at the methodology layer; the head's
SECONDARY verdict is the substrate-physics half of the dual structure. No
container-thinking arises in the queue-discipline gate (it operates on the
methodology-layer queue); the substrate-framing discipline applies to the
SECONDARY warrant-check execution per its specific PHONONIC / GEOMETRIC
classification at Step A(iii).

```yaml
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
```

---

## §0.10. Wave 7 Machinery-Enumeration Pin (PRDR top-level)

This wave-level §0.10 enumerates every free parameter across the 5 gate-blocks for
top-level audit. Per-gate pins are in each §W7-N.7 block above; this section is the
SUMS / SCHEDULES level for plan-freeze validators.

### Cross-gate pins

| Cross-gate parameter | Pin |
|:----------|:----|
| Canonical L_max | 10 (S86 W4 P4 commit; canonical_constants.xi_E_GGE_inv anchor) |
| Canonical xi_E_GGE_inv | 13.642473425595973 (canonical_constants.py; substrate-natural 59.8 · Δ_BCS / K_base anchor) |
| Canonical D_K spectrum cache | `computations/s84_spectrum_cache_L12_tau019.npz` |
| 5-class L1 partition source | W-9 STAGE-1-CANDIDATE (CF-54 entry) OR fallback W-9 workshop §E-R2.2 lines 1097-1112 |
| F_4 multiplier-vector sub-family | §VII.K-PROP entry (S86 W-8 RULE-1 landing) |
| Mellin-cone substrate-distance pole convention | s = -1 (W7-1), s = 2 + s = 3 (W7-2 ratio), s = 4 + s = 2 (W7-3 ratio) |
| Stage-2.5 sub-tag definition | S84 W2c-19 UNPINNED-L2-AUDIT |
| 5-stage LAYER protocol | S83 W2-G14 + S84 W2c-19 = {L0-INT, L1, L2, L3, UNPINNED} |
| GPU path policy | torch.linalg.eigh on RX 9070 XT for spectral re-derivation; CPU fallback OMP_NUM_THREADS=8 |
| Level pin for SCHEMATIC helpers | SCHEMATIC per `substrate-first-canonical-sourcing.md` §iv (W7-2, W7-3) |

### CF-42 dual-prior specification (frozen at this plan-author level)

Per `.claude/rules/epistemic-discipline.md` §"Dual-prior pre-registration as track-discriminator pattern" (T1-11, W-9 RULE-5):

| Field | Value |
|:----------|:----|
| Track A label | F_2-class STRUCTURAL-PRIMACY |
| Track B label | per-class DIAGNOSTIC-only |
| Prior_A | 0.4 |
| Prior_B | 0.6 |
| Likelihood_A model | Gaussian(delta_max | mu=0, sigma=0.025) — concentrated near 0 |
| Likelihood_B model | Gaussian(delta_max | mu=0.30, sigma=0.10) — broad around per-class spread |
| Discriminator gate criterion | PASS (delta_max ≤ 0.05) → Posterior_A allocated; FAIL (delta_max > 0.20) → Posterior_B allocated; INFO (intermediate) → posteriors near priors |

The dual-prior is FROZEN at S87 plan-author. CF-42's runtime dispatch reads these
pinned values; modification at runtime is a Class-3 PROHIBITED_ACTIONS violation
per `.claude/rules/v3-closure-recovery.md`.

### Per-gate machinery pin cross-reference

| Gate | n_eval | scheme | tolerance |
|:--|:--|:--|:--|
| W7-1 (CF-42) | 5 (per-class) | Mellin-slot s=-1 | RATIO ≤ 0.05 PASS |
| W7-2 (CF-43) | 3 (F_4 sub-family) | Mellin-cone substrate-distance-1 | RATIO ≤ 0.01 PASS |
| W7-3 (CF-44) | 5 (per-class) | Weyl-rescaling-Mellin (s=4/s=2 ratio) | RATIO ≤ 0.02 R1 PASS / ≤ 0.05 R2 PASS |
| W7-4 (CF-45) | full S78-onward corpus | 5-stage LAYER protocol | INTEGER 0 PASS |
| W7-5 (CF-46) | ~26 available | head-of-queue rule | INTEGER ≥ 1 PASS |

PRU cardinality status (run via `computations/_pru_cardinality_audit.py` at
plan-freeze): every gate's parameters are pinned with the runtime-late-bind
exception for upstream-source SHAs (acceptable per dynamic-input convention).

---

## §0.11. Wave 7 Input-SHA Ledger

### Static inputs (pre-S87 canonical SHAs)

| Source | Description | SHA status |
|:----------|:----|:----|
| `computations/canonical_constants.py` | xi_E_GGE_inv = 13.642473425595973 + Δ_BCS + K_base + all framework constants | `<CANONICAL>` (computed at S87 plan-freeze; pinned in each gate's npz output) |
| `computations/s84_spectrum_cache_L12_tau019.npz` | D_K^{≤10} spectrum cache | `<CANONICAL>` (S86 close artifact; pre-existing) |
| `computations/_spectral_action_regulators.py` | 5-atlas regulator definitions (SCHEMATIC-tagged) | `<CANONICAL>` (S86 close artifact) |
| `.claude/rules/regulator-pin-discipline.md` | 5-stage LAYER protocol definition | `<CANONICAL>` (S86 close artifact) |
| `.claude/rules/regulator-convention-lockdown.md` | L2 Zubarev canonical-anchored convention | `<CANONICAL>` (S86 close artifact) |
| `.claude/rules/substrate-first-canonical-sourcing.md` §iv | PRIMARY vs SCHEMATIC discipline | `<CANONICAL>` (S86 close artifact) |
| `.claude/rules/epistemic-discipline.md` §"Dual-prior" | T1-11 dual-prior rule | `<CANONICAL>` (S86 close artifact) |
| `.claude/rules/joint-theorem-promotion.md` | 4-stage joint-theorem pathway | `<CANONICAL>` (S86 close artifact) |
| `sessions/permanent-results-registry.md` | §VII.<slot> registry entries (W-1 to W-13 landings) | `<CANONICAL>` at S87 plan-freeze; per-gate sub-pins late-bind |
| S78-S86 verdict files (`computations/s78_gate_verdicts.txt` ... `s86_gate_verdicts.txt`) | LAYER-tag audit corpus (W7-4) | `<CANONICAL>` |
| S78-S86 sessions corpus (`sessions/archive/session-78/` ... `sessions/archive/session-86/`) | citation enumeration corpus (W7-4) | `<RUNTIME-COMPUTED>` directory hash |
| `sessions/archive/session-86/session-86-w7-workshop.md` (or equivalent W-7 workshop file) | CV-CN-R3-4 NARROW scope ~26 warrant-check available list (W7-5) | `<RUNTIME-LATE-BIND>` |

### Dynamic inputs (runtime-late-bind)

| Source | Used by | Late-bind reason |
|:----------|:----|:----|
| CF-54 STAGE-1-CANDIDATE entry (5-class L1 partition) | W7-1, W7-3 | CF-54 lands earlier in S87; its registry-entry SHA is computed at CF-54 verdict-line emission time |
| W-9 workshop §E-R2.2 wrap-up text | W7-1, W7-3 (fallback if CF-54 not landed) | Fallback source if CF-54 not yet landed at compute time |
| W-9 workshop §EM-CN-R3-1 (F_2 spectral-cluster definition) | W7-1 | Workshop-file SHA captured at compute time |
| W-9 workshop §L-CR3.3 (Joint Theorem clause (e) amendment) | W7-3 | Workshop-file SHA captured at compute time |
| W-6 workshop §C-β-immunization | W7-2 | Workshop-file SHA captured at compute time |
| W-6 workshop §C-γ-WEAK-Weyl-rescaling | W7-3 | Workshop-file SHA captured at compute time |
| §VII.K-PROP entry (F_4 multiplier-vector sub-family) | W7-2 | Registry-entry SHA at compute time |
| W-7 workshop file §CV-CN-R3-4 ~26 available list | W7-5 | Workshop-file SHA captured at compute time |

### Input-SHA pin discipline

Per `.claude/rules/gate-verdicts.md`:
- Static inputs SHA-256 pinned at S87 plan-freeze; pinned values appear in each gate's
  npz output and stdout first-20 lines.
- Dynamic inputs SHA-256 pinned at compute time; if upstream landing not present at
  compute time, the gate emits the workshop-file fallback SHA and flags
  `<status>_pending=true` in the verdict line.
- Closure SHA per gate is SHA-256 of the ordered input-pin map; emitted as the final
  field of the canonical verdict line.

---

## §0.12. Wave 7 → Wave 8 Decision Point

W7's outcome shapes W8's plan as follows:

1. **W7-1 PASS (Track A allocation)**: 5-class L1 partition admits STRUCTURAL-PRIMACY.
   W8 inherits this and may schedule a Stage-2 independent-verify follow-up
   (precursor for S88+ CF-59 Stage-2 Joint Theorem verify). If W7-3 (CF-44) returns
   PASS-R1 or PASS-R2 with consistent integer multipliers, the structural reading
   is doubly anchored.

2. **W7-1 INFO**: 5-class STRUCTURAL-vs-DIAGNOSTIC reading unresolved. W8 should
   NOT schedule Stage-2 follow-up; instead route the dispute to S88+ with the
   intermediate posteriors as the carry-forward state.

3. **W7-1 FAIL (Track B allocation)**: 5-class is per-class DIAGNOSTIC. W8 must
   re-spec downstream gates citing "the" xi_E_GGE_inv or "the" Λ_anom_internal
   under per-class restrictions. CF-54 STAGE-1 candidate stays at STAGE-1
   permanently (no permanent registry promotion possible without STRUCTURAL
   reading).

4. **W7-2 PASS**: F_4 multiplier-vector sub-family is UV-cutoff-immunized. W8 may
   cite C-β as substrate-canonical at the §VII.K-PROP slot; CF-50 (HBW audit
   atlas) and CF-49 (sixth-regulator promotion) may use C-β as one of their
   pre-registered discriminators.

5. **W7-2 INFO/FAIL**: F_4 sub-family is not closed under substrate-distance-1.
   W8 routes the dispute to per-class C-β maps; CF-50 / CF-49 must respect this.

6. **W7-3 PASS-R1**: Λ_anom_internal class-INDEPENDENT. Strongest structural
   reading. W8 may cite Λ_anom_internal as a substrate-canonical anomaly scale.
7. **W7-3 PASS-R2**: Class-FACTORIZED. Document {n_c} integers; W8 may anchor an
   "integer-graded anomaly multiplier" registry candidate.
8. **W7-3 INFO-R3**: Independent scales. Calibration data only; no structural
   promotion in W8.
9. **W7-3 FAIL**: Anomaly-scale per-class evaluation unreliable. W8 must use
   global Λ_anom_internal only.

10. **W7-4 PASS**: 5-stage LAYER protocol COMPLETE for S78-onward corpus. W8 may
    rely on the LAYER-tag for any cross-corpus citation discipline. CF-72
    (W8 wave-classification rule validation) inherits this PASS as evidence.
11. **W7-4 INFO**: Small audit residual. W8 schedules in-session manual
    Stage-2.5 review per no-tech-debt rule.
12. **W7-4 FAIL**: Protocol coverage incomplete. W8 routes to Stage-3 user-trigger
    event (extend protocol or regex set, then re-run).

13. **W7-5 PRIMARY-PASS**: Queue-discipline operational; head-of-queue warrant-check
    supports its theorem. W8 may cite the registry theorem at strengthened
    confidence; the SECONDARY verdict feeds the registry directly.
14. **W7-5 PRIMARY-INFO**: Queue-discipline operational; head warrant-check
    refutes its theorem. The registry theorem the head tested is updated per
    the SECONDARY-FAIL verdict; W8 routes to a NEEDS-DECISION on the registry
    theorem's status.
15. **W7-5 PRIMARY-FAIL**: No item qualifies. Selection rule too strict; W8
    NEEDS-DECISION on rule relaxation (e.g., effort ≤ 6h) for S88+ queue-discipline.

W8 plan-author: read W7's verdict file `computations/s87_gate_verdicts.txt`
for the 5 + 1-secondary verdict lines; route per the above 15-row decision-point
table.

---

## §0.13. Validator Coverage Checklist (plan-freeze; per skill §3e)

Run at plan-freeze for `session-87-plan-w7.md`:

1. ✅ `computations/_plan_upstream_pin_validator.py --json sessions/session-plan/session-87-plan-w7.md`
   → JSON to `sessions/session-plan/session-87-plan-w7-validation.json`
2. ✅ `computations/_yaml_gate_validator.py sessions/session-plan/session-87-plan-w7.md`
   (verifies `schema_version: R3` per gate; PRDR machinery checklist)
3. ✅ `computations/_source_reconciliation_audit.py` (5+1 class taxonomy; HARD-HALT at D_max ≥ 3.0)
4. ✅ `computations/_substrate_first_provenance_audit.py` (V.1 manual review until
   implementation lands; canonical xi_E_GGE_inv source = canonical_constants.py
   line entry, NOT external paper)
5. ✅ `computations/_pru_cardinality_audit.py` (cardinality pre-flight)
6. ✅ Post-dispatch grep on `computations/s86_gate_verdicts.txt` for collision
   check on S87 gate IDs (none should pre-exist)
7. ✅ Methodology-wave-allowlist check: W7 is NOT methodology-class (all 5 gates
   are COMPUTE-class with numerical or audit-integer thresholds; W7-4 is AUDIT
   but has INTEGER threshold so remains COMPUTE per `.claude/rules/wave-classification.md`
   M1 numerical-comparison test). No allowlist append needed.

End of session-87-plan-w7.md.
