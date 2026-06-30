---
name: S28C-12D-AXIOMS prep block
description:  re-run prep for the 12D Connes axiom verification (C-6 / DP-1)
type: project
classification: GEOMETRIC
---

# Prep Block — S28C-12D-AXIOMS

## Classification
**GEOMETRIC** — this gate probes the spectral-triple structure itself
(D_K / D_can eigenvalue structure, J-operator algebra, order-one
commutator structure). It is NOT phononic (no excitation relay
patterns, no spectral moments of cosmological/observational quantities)
and NOT particle (no representation-theoretic quantum numbers of SM
fields). It operates at the level of the fabric's internal axiomatic
skeleton.

## Gate
- **Gate ID**: S28C-12D-AXIOMS
- **Script**: `computations/session-28/s28c_12d_axioms.py`
- **Pass/fail criterion** (pre-registered): all 7 Connes axioms hold
  for the 12D product (M^4 x (SU(3), g_tau, D_can)) with the A_F
  representation on C^16. PASS iff N_pass == 7.

## Pre-Registered Machinery (PRDR)
- **L_max_pin**: `L_MAX_PIN = 5` — Peter-Weyl truncation max_pq_sum
  (forwarded to axiom 1 spectral-dimension regression). 5 is sufficient
  for axiom-level testing (the axiom content is representation-theoretic,
  not spectral-asymptotic-sensitive). Axioms 3, 6, 7 are structural;
  axiom 4 is operator-level on fixed 32-dim H_F; axiom 5 is Clifford-only.
- **tau sweep**: {0.00, 0.15, 0.30} — diagnostic only. Connes axioms on
  this product are tau-independent at the algebraic level (order-one
  violation = 4.000 exact for all tau).
- **Free parameters enumerated**: max_pq_sum (pinned), tau_values
  (diagnostic sweep), Clifford basis choice (fixed by
  `dirac_spectrum.build_cliff8` convention), A_F generators (C + H
  + M_3(C), fixed in `build_AF_generators`).
- **Canonical imports**: `from canonical_constants import tau_fold`
  (provenance check only; script uses diagnostic tau sweep, not the
  fold-value exclusively). No other framework constants referenced — the
  axiom content is pure representation theory + differential geometry.

## SHA-256 Pins
- Pre-edit:  `4b8c6ec39ab671c05cc607ccf57900c829160299583d7cbaeb91ccd834726cba`
- Post-run:  `24fd130ba00291a3e391d39fd3e3ceb00a72b1b6162ad2c66d482a236ec58e30`

Changes: added OMP_NUM_THREADS=8 pre-numpy guard; canonical-constants
import; `L_MAX_PIN = 5` pre-registered; tagged `tau_values` as `# (local)`;
threaded `L_MAX_PIN` into the axiom-1 call.

## Knowledge-Base Query Results
- `trace_entity("connes_axioms")`: 1 open channel (philosophical
  discussion), 1 equation record (order-zero form noted in
  debug_jcompat7.py). No prior theorem closure.
- `search_knowledge("12D Connes axioms")`: C-6 gate FAIL recorded in
  session-28c-results.md with identical value (axiom 5 violation = 4.000).
  This re-run confirms.
- `get_constant("J_C2")`: value 0.933 (C^2 coset directions, dominant 4
  bonds M_KK). Not used — 12D axioms are structural, not J_C2-dependent.

## Value
N_pass/N_total = **6/7**

## Verdict
**FAIL** — axiom 5 (first-order / order-one condition) violated at
max norm = 4.000 (O(1), tau-independent, Clifford-algebraic).
Re-run confirms the S28c result.

## Substitution Chain
Not required — value is a pass-count and the PASS direction is pre-
registered as equality to N_total. No sign/direction/threshold claim
made in the verdict; only the axiom-by-axiom booleans are reported.

## Cross-Gate Implications
- Consistent with C-3 (order-one) FAIL in s28b_order_one.
- Supports the S36+ paradigm shift (instanton-gas / GGE, not equilibrium
  spectral-triple) — the 12D Connes spectral-triple route in the naive
  A_F on C^16 representation is closed.
- Leaves open: modified A_F embeddings, or post-transit GGE descriptions
  that do not require Connes axioms at the fundamental level.
