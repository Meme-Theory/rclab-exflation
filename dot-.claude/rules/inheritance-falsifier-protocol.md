# Inheritance Falsifier Protocol

This rule governs how laboratory falsifier protocols are designed under an **inheritance morphism** ι : (parent observable algebra) → (substrate observable algebra) when the kernel `ker(ι_*)` has rank ≥ 2.

The canonical 3He-B realization of this rule is the inheritance morphism from the substrate's spectral triple `(A_K, H_K, D_K)` (with `A_K = C ⊕ H ⊕ M_3(C)`) to the 3He-B BdG sector via the algebra projection χ : C ⊕ H ⊕ M_3(C) → M_2(C) sending M_3(C) → 0. The kernel `ker(ι_*)` carries the substrate degrees of freedom that DO NOT inherit into the laboratory parent.

## Two Test Classes

When `ker(ι_*)` has rank ≥ 2 (i.e., ≥ 2 independent generators of substrate degrees-of-freedom that DO NOT inherit), the falsifier protocol MUST pre-register BOTH of the following test classes. Either alone is structurally insufficient.

### Class A — Kernel-Signature Test

- **Form**: row-wise NULL prediction across each F-row of the falsifier inventory
- **Predicts**: For each generator [φ_a] in ker(ι_*), the laboratory observable corresponding to F_a returns NULL (no signal) when the parent inheritance is BDI-protected (or whatever the parent symmetry class)
- **Confirms**: BdG-restricted (or parent-restricted) spectrum carries no `ker(ι_*)` cocycle
- **Canonical 3He-B realization**: 5-row 3He-B falsifier table with NULL predictions on F1+F2+F5 (decisive triplet) + F3+F4 (supporting pair); each row is a kernel-signature test for one of the φ_67 (chiral pair) or φ_88 (Cartan hypercharge) generators

### Class B — Cohomology-Asymmetry Test

- **Form**: cross-cocycle ratio prediction between distinct `ker(ι_*)` generators
- **Predicts**: Substrate-derived ratio between two cocycles is **preserved INTACT** in the laboratory measurement under the common-exponent `(Δ_B/Δ_A)^p` lab-conversion
- **Confirms**: Even if a kernel-signature test fails (lab sees a non-NULL signal), the cohomology-asymmetry RATIO is still substrate-derived and falsifies the framework if the measured ratio diverges
- **Canonical 3He-B realization**: substrate-derived ratio `cocycle_norm_phi67 / cocycle_norm_phi88 = 7.324992` (Sage-exact at machine precision; 7.3250 in 4-sig-fig form); preserved INTACT in lab measurement under common (Δ_B/Δ_A)^p exponents

## Why both classes are required

Class A alone (kernel-signature only) is insufficient because:
- A non-NULL detection can be reinterpreted as parent-symmetry breakdown (other than substrate inheritance), defusing the substrate-falsification claim
- The substrate's **structural prediction** is not just "no signal" but "no signal in a specific cohomology pattern"

Class B alone (cohomology-asymmetry only) is insufficient because:
- If both lab observables return NULL, no ratio can be computed — the test is vacuous
- The substrate's **first prediction** is the kernel-signature NULL; the ratio test is the **secondary** falsifier

Together, both classes saturate the substrate's predictive content: NULL-on-rows AND ratio-on-cross-rows.

## (Δ_B/Δ_A)^p Cancellation Theorem (operational form)

The cohomology-asymmetry test relies on a structural identity (machine-precision Python verification at 0.0e+00 residual):

```
lab(F_i) / lab(F_j)  =  ‖φ_a‖ / ‖φ_b‖  ×  (f_i / f_j)
```

for common exponents `p_i = p_j = p` in the lab-conversion factors. The `(Δ_B/Δ_A)^p` factor cancels exactly between numerator and denominator. The substrate-derived ratio `‖φ_a‖ / ‖φ_b‖` is therefore **preserved INTACT** in the lab measurement, INDEPENDENT of the precise value of (Δ_B/Δ_A) or p.

This cancellation is what makes the cohomology-asymmetry test substrate-falsifying rather than lab-conversion-dependent.

## Four-Gate Structure

The four-gate falsifier structure for inheritance-morphism falsifier protocols. Future `ker(ι_*)` characterizations of rank ≥ 2 SHOULD adopt this template:

- **Gate 1**: Kernel-signature row-wise NULL test on the **decisive** F-rows. Canonical 3He-B: F1 + F2 + F5.
- **Gate 2**: Cohomology-asymmetry cross-cocycle ratio test. Canonical 3He-B: 7.3250 ± 0.1% on any non-NULL detection.
- **Gate 3**: Kernel-signature row-wise NULL test on the **supporting** F-rows. Canonical 3He-B: F3 + F4.
- **Gate 4**: Discriminating slope analysis on cocycle-degenerate rows requiring parameter-sweep. Canonical 3He-B: F4 multi-pressure slope (Jacobi-cubic vs φ_88-linear over 0–34 bar).

The four-gate structure separates **decisive** (Gate 1) from **supporting** (Gate 3) substrate-cleanness; isolates the **cohomology-asymmetry** test (Gate 2); and reserves a **slope-discrimination** gate (Gate 4) for cocycle-degenerate rows where a single (p, T) measurement cannot disambiguate cocycle contributions.

## Pre-registration discipline

For any falsifier-protocol design with `rank(ker(ι_*)) ≥ 2`:

1. **Enumerate ker(ι_*) generators** — list all independent generators [φ_a], a = 1, …, rank
2. **Build F-row table** — one row per substrate-clean generator + sub-rows for cocycle-degenerate generators
3. **Pre-register Gate 1 NULLs** — row-wise NULL prediction for each decisive F-row, with substrate-derived predicted lab S/N margin per row. Canonical 3He-B: F1 = 0.573193 M_KK².
4. **Pre-register Gate 2 ratio** — cross-cocycle ratio between any two decisive rows, with tolerance band. Canonical 3He-B: 7.3250 ± 0.1%.
5. **Pre-register Gate 3 NULLs** — row-wise NULL on supporting rows
6. **Pre-register Gate 4 slope** — for any cocycle-degenerate row, the parameter-sweep slope discrimination

Pre-registration of Gate 2 (cohomology-asymmetry) is the high-leverage discipline; the kernel-signature tests (Gates 1 + 3) without Gate 2 leave the protocol open to lab-conversion-shopping reinterpretation.

## Generalization beyond 3He-B

The canonical 3He-B realization is specific to the substrate's `(SU(3) ⊃ SO(3)_isospin)` parent and its 3He-B BdG-sector child. Future extensions to other parent theories (e.g., Pati-Salam, GUT extensions, alternative finite spectral algebras) MUST apply this rule whenever the inheritance kernel has rank ≥ 2:

- **Generic rank-2 case**: dual cocycle generators ([φ_a], [φ_b]) with substrate ratio `‖φ_a‖ / ‖φ_b‖` — apply Gates 1+2+3 directly (Gate 4 only if cocycle-degenerate row exists)
- **Higher-rank case (rank ≥ 3)**: rank-2 sub-cases for each pair of generators; the cohomology-asymmetry test class includes ALL `binomial(rank, 2)` cross-cocycle ratio predictions

## Cross-link to falsifier-master-inventory

This rule is the structural template for any new row in `sessions/framework/registry/falsifier-master-inventory.md` whose substrate prediction is NULL-by-inheritance-kernel. New rows MUST cite this rule and declare which ker(ι_*) generator the row tests.

## Canonical lab platforms (3He-B)

Two 3He-B lab platforms instantiate the four-gate structure:

- **3He-B vortex-core spectroscopy**: F1 = Caroli-Matricon ladder asymmetry, φ_67-clean, decisive; lab platforms Lancaster MCT-3 / Helsinki ROTA cells. Gate 1 NULL on F1+F2+F5; Gate 2 ratio 7.3250 ± 0.1%; Gate 3 NULL on F3+F4; Gate 4 F4 multi-pressure slope.
- **3He-A µSR**: same 4-gate structure with A-phase chirality discrimination; lab-conversion factors phase-dependent but substrate ratios identical (7.3250).

## Audit at plan-freeze

Plan-freeze validators landing an inheritance-morphism falsifier-protocol pre-registration MUST verify:

1. `ker(ι_*)` rank declared explicitly with all generators enumerated
2. Gate 1 + Gate 2 + Gate 3 + Gate 4 all pre-registered (Gate 4 may be N/A if no cocycle-degenerate row)
3. Gate 2 ratio prediction includes substrate-derived value AND tolerance band
4. (Δ_B/Δ_A)^p cancellation theorem applicability declared (which generators share common p)
5. Per-row substrate predictions (NULL or ratio) and lab S/N margin

Missing any of (1)-(5) = NEEDS-COMPUTATION block at plan-freeze.
