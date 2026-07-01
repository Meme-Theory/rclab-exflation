# Mellin-Balance Pre-Declaration Template

**Origin**: S84 W6-71 (`S84-OBSERVABLE-MELLIN-BALANCE-TEMPLATE` meta-gate).
**Status**: MANDATORY for all S84+ cluster-test gates.
**Motivation**: Prevents recurrence of S83 G15/G28/G34 ad-hoc cluster-membership
failures by forcing pre-registration of the Mellin-moment balance BEFORE any
scan is run.

## When to Use This Template

Paste the snippet (see below) into the gate block in
`sessions/session-plan/session-{N}-plan-w*.md` whenever the gate's verdict
depends on a measured "cluster" (regulator-span) of an observable ratio, and
the gate classifies that observable as R-protected / balanced-Mellin /
Mellin-balanced or otherwise claims that the numerator and denominator sample
the same spectral-moment grading.

Applicable gate classes:

- `S84-*-CONV-*-PROPAGATION-*` (regulator-convention propagation across ratios)
- `S84-*-R-PROTECTED-*` (atlas membership by R-balance)
- `S84-*-BALANCED-RATIO-*` (direct Mellin-balance claim on ratio observable)
- `S84-*-MELLIN-*-ATLAS` (observable-atlas with per-entry Mellin labels)
- `S84-*-K-*-CANONICAL-RANGE` (slot-k cluster scan under canonical convention)
- `S84-*-SLOT-SPAN-*` (slot-span scaling with Mellin grade assumption)
- `S84-*-LEDGER-LINEARITY-*` (linearity of the balanced-Mellin ledger)
- any future gate that asserts "cluster < threshold" based on a balance claim

Not applicable to: absolute-amplitude gates (A_s, m_H, etc.) where no
ratio/cluster is tested; detector-projection gates (sigma forecasts); pure
dimensional-analysis threshold gates.

## Substrate Interpretation

Mellin labels are the substrate's integer grading of spectral moments of the
Dirac operator `D_K` on Jensen-deformed `SU(3)`. A "balanced" ratio is one
whose numerator and denominator both sample the same Seeley-DeWitt coefficient
`a_k^R`, so that regulator-scheme dependence cancels at leading order. An
"unbalanced" ratio samples two different spectral moments and therefore
inherits regulator-scheme variation from both, producing a cluster span
typically `>= 2.5`.

## Mandatory Snippet (copy verbatim into gate block)

```markdown
## Mellin-Balance Pre-Declaration (REQUIRED for S84+ cluster-test gates)

**Observable**: O = <explicit definition — algebraic form of the ratio or
                    scalar being tested, with all fields/coefficients named>

**Numerator (f_num)**: Mellin label k_num = <integer>
  **Reason**: <which spectral moment is being sampled, e.g., "a_2^R
               Seeley-DeWitt coefficient (second heat-kernel grade)">

**Denominator (f_den)**: Mellin label k_den = <integer>
  **Reason**: <which spectral moment is being sampled>

**Balance condition**: k_num == k_den → <TRUE|FALSE>

**Classification (PRE-SCAN)**:
  - If k_num == k_den → CLAIMED-R-PROTECTED → predicted cluster < 1.5
  - If k_num != k_den → CLAIMED-NOT-R-PROTECTED → predicted cluster >= 2.5

**Predicted cluster**: cluster_predicted = <numeric>
  **Derivation**: via CC-5 identity,
    cluster(O) = span(f_num)^|p_num| * span(f_den)^|p_den|
  where p_num, p_den are the multiplicative exponents with which f_num,
  f_den enter the observable O.

**Post-scan measured cluster**: <filled after run — leave as "PENDING" in
                                 pre-registration>

**Agreement check**:
    |cluster_measured - cluster_predicted| / cluster_predicted < 0.01
    → TEMPLATE PASS

**PRU check**: Did this Mellin-balance pre-declaration appear in the plan
    BEFORE any scan was run on this observable?
    <yes|no — must be yes for PASS>
```

## PASS / FAIL Semantics (per-gate)

The per-gate application of the template is PASS if:

1. `k_num`, `k_den`, `cluster_predicted`, and the pre-scan CLAIMED
   classification are all present in the plan gate block BEFORE the script
   is executed;
2. the measured cluster from the run satisfies the relative-error threshold
   `|cluster_measured - cluster_predicted| / cluster_predicted < 0.01`;
3. the PRU check answers "yes".

The per-gate application is FAIL if:

1. the snippet is missing from the gate block; OR
2. the relative-error exceeds 5%; OR
3. the PRU check answers "no" (post-hoc predicted-cluster back-fitting).

The per-gate application is INFO if compliance is clean but the relative
error is in `[0.01, 0.05)` — the template structure works, but NLO
corrections exist (useful diagnostic for L_max extrapolation).

## Meta-Gate (W6-71) PASS Rule

Meta-gate `S84-OBSERVABLE-MELLIN-BALANCE-TEMPLATE` is PASS iff:

- 100% of S84 cluster-test gate blocks contain the snippet
  (`compliance_fraction == 1.0`);
- every gate that has already been run satisfies `|measured -
  predicted| / predicted < 0.01`.

FAIL if any cluster-test gate reports a verdict without the snippet.

INFO if coverage is 100% but at least one gate has NLO-level deviation
(`0.01 <= rel_err < 0.05`).

## Retroactive Application

The snippet is applied retroactively as an audit tool to S83 cluster-test
gates (G14, G15, G26, G28, G34). The retroactive audit does not change
those gates' historical verdicts; it classifies the failure mode:

- **G15, G28, G34** (S83 FAIL cluster verdicts): post-audit, these
  would have been classified CLAIMED-NOT-R-PROTECTED ex ante under the
  template — the failures correspond to ad-hoc CLAIMED-R-PROTECTED
  classification that the template would have blocked pre-scan.
- **G14, G26** (S83 PASS cluster verdicts): post-audit, these were
  implicitly balanced; under explicit pre-declaration, their cluster
  values align with CC-5 prediction, confirming the template reproduces
  the correct verdict by construction.

## Enforcement

1. Every S84+ cluster-test gate block in `session-{N}-plan-w*.md` must
   contain the snippet. The `s84_w6_mellin_balance_template_audit.py`
   script enumerates S84 cluster-test gates and reports per-gate
   snippet-presence.

2. `/weave --update` should check for template presence in every
   cluster-test gate block (future hook).

3. New cluster-test gates added in S85+ are PRU-non-compliant unless
   they include the snippet at plan-write time.
