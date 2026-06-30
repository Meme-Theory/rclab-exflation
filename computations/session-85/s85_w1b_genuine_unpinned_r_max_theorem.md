# r_max layer-interface theorem candidate — disposition

**Gate**: S85-W1b-GENUINE-UNPINNED-R_MAX-LAYER-INTERFACE-THEOREM

## Source data (S84 W2-19 carry-forward; S82 W2-2 canonical)

Row #13 r_max from S82 UNIFIED-BACKREACT-79 is layer-dependent:

| Layer | Regulator / role | r_max value |
|:------|:-----------------|:------------|
| L1 (inspection) | zeta regulator, backreaction cap | 13,322 |
| L2 (substrate action) | Zubarev, sc-saturation cap | 1.0 |
| Canonical (as reported in S82 W2-2) | zeta L1 | **13,322** |

OOM gap between L1 and L2: **4.125** (four orders of magnitude).

## Plan's layer-interface theorem candidate

**Claim**: r_max(k) = min(r_N(k), r_{N+1}(k)) across adjacent corridor layers, to machine epsilon.

**Test**:
- min(r_L1, r_L2) = min(13,322, 1.0) = **1.0**
- r_max_canonical = **13,322**
- |r_max − min| = **13,321.0**
- relative residual = 0.99992

Threshold: PASS iff |residual| < 1e-12 (THEOREM = machine epsilon). Fails by **13321** (4 OOM).

## Verdict: **FAIL** (plan's theorem candidate does not hold)

The min-adjacent-layer identity is NOT the correct structural statement
for r_max. The actual structural property (per S84 W2-19 synthesis):

> "r_max is genuinely two-valued at the layer interface."

That is: r_max takes DIFFERENT values under L1 (zeta inspection → 13322)
vs L2 (Zubarev substrate-action saturation → 1.0). It is NOT a pinned
scalar obeying a min-identity; it is a **layer-observable-multiplicity**.
Promoting this TRUE statement to a theorem requires its own registration
with the "two-valued at interface" phrasing, NOT the plan's min-identity.

## Structural inference

The S84 synthesis-collation already documents this:
> "The §VII.N theorem is anchored as L_max-independent and substrate-
> independent in scope, but with two structural exceptions
> (r_max layer-interface, a_2-cluster meta-observable)."

r_max is one of the two STRUCTURAL EXCEPTIONS to the three-layer
regulator theorem — explicitly flagged as an interface observable,
not a universal invariant. The plan's min-identity hypothesis was
trying to collapse the two-valuedness into a single invariant; the
audit shows that collapse fails by 4 OOM.

## Carry-forward

- Register the ALTERNATIVE theorem: "r_max is two-valued at L1/L2
  layer interface; canonical depends on layer choice" — a
  convention-dependent observable, not a universal invariant.
- Downstream: any gate consuming r_max must pin layer choice (L1 or L2)
  in its machinery pin.

## Provenance

- audit_sha256:   9e95f8b9b859b829340bfce8ec31003eedd313e37b70ff79027d2ad1b8399170
- content_sha256: 6024f422e73e8012db8ae9a8ae11866c18d86bae23cdb94a4cc6b0ce86b9325f
- schema_version: S84+
