---
name: S80 W1-4 CC-Ratios-Only Theorem (alt proof)
description: Mellin-transform / heat-kernel independent proof that weight-balanced SDW-coefficient ratios are f-independent CC96 observables; multiset-vs-sum subtlety flagged for P4-D CN-EM1 refinement
type: project
---

# S80 W1-4 — CC-Ratios-Only Theorem (spectral-geometer alt)

**Why**: Primary author connes writes the CC-side proof; I derive it independently from the heat-kernel / Weyl-asymptotic side and cross-check. EVOI ~0.12 (medium); gate S80-CC-RATIOS-ONLY-THEOREM [VERIFY-THEOREM]. Result anchors the framework's §VII.I "ratios-only" observable class (single-pin {M_KK}).

**How to apply**: For any future assessment of CC96-based framework observables, dimensionless D_K-moment ratios a_m/a_n at MATCHING weight labels (w(a_n) ≡ d − n = k) are f-independent framework observables; different-weight ratios are regulator-dependent. Use binary pair-balance for unambiguous cancellation; use multiset-equality (NOT sum-equality) as the sufficient condition for monomial sibling cancellation.

---

## Derivation

CC96 eq 2.11 via heat-kernel / Mellin-Laplace duality:

    Tr f(D²/Λ²) ~ Σ_k f_k · Λ^k · a_{d−k}[D²] / Γ(k/2),
    where f_k = ∫_0^∞ f(u) · u^{k/2 − 1} du   (Mellin moment at s = k/2).

Each summand = (f-dependent) × (Λ,k-dependent) × (D-dependent / f-INDEPENDENT).

## Weight label

`w(a_n) ≡ d − n`. Binary balance: w(a_m) = w(a_n) iff m = n (pair-level).
Monomial balance (sufficient for cancellation): MULTISET {w(m_i)} = {w(n_j)}, NOT sum equality.

## Substitution chain (balanced pair)

    Step 1: R_{m,n}^{(f)} ≡ S_m^{(f)} / S_n^{(f)}.
    Step 2: = [f_k Λ^k a_m / Γ(k/2)] / [f_k Λ^k a_n / Γ(k/2)]  (m = n ⇒ same k).
    Step 3: f_k, Λ^k, Γ(k/2) cancel identity-level (arithmetic).
    Step 4: = a_m / a_n (pure geometric).

**Direction**: balanced ⇒ **f CANCELS**.

## Counterexample (unbalanced, d = 8)

    (a_2, a_4): S_{a_2}/S_{a_4} = (f_6/f_4) · Λ² · (a_2/a_4) · (Γ(2)/Γ(3)).

f_6/f_4 varies across regulators (numerics):
- f_A = e^{−u}:        f_6/f_4 = 2.00.
- f_B = (1+u)^{−2}:    f_6/f_4 ≈ −0.107 (sign flip).
- f_C = e^{−u^{0.7}}:  f_6/f_4 ≈ 4.94.

**Direction**: unbalanced ⇒ **f RETAINS**.

## Python sanity check

`computations/s80_cc_ratios_only_sanity.py`:
- Part C balanced (k=4, k=4): ratio identical to machine precision (≤ 2.22e−16) across 3 regulators.
- Part D unbalanced (k=2, k=4): ratio varies > 2 OOM across regulators (1.39e−2 to 2.00e+0).

## Key structural observation (flagged to primary)

P4-D CN-EM1 (S79 line 1810) writes monomial balance as `Σ p_i (4 − n_i) = m` (equal-sum). This is equivalent to my binary pair-balance ONLY in the binary case. For monomials with mixed weight labels: (a_4)² (weights {4,4}) and a_2·a_6 (weights {6,2}) have equal sum (8 = 8) but DIFFERENT multisets — ratio of full spectral-action contributions does NOT cancel f (verified numerically). Sufficient condition: MULTISET equality.

## Files

- `sessions/archive/session-80/theorems/cc-ratios-only-theorem-alt-spectral-geometer.md` — full alt proof (~3 pages, Lemma 1 + Lemma 2 + Theorem + Counterexample).
- `sessions/archive/session-80/session-80-results-workingpaper.md` §W1-4-alt — summary section with substitution chains.
- `computations/s80_cc_ratios_only_sanity.py` — Python sanity check (4 parts).

## Cross-check status

Primary (connes) pending. Agreement matrix pre-registered in proof file. PASS if primary agrees on binary balance + counterexample ≤ 3 pages. INFO if primary disagrees on monomial sufficiency (multiset vs sum). FAIL not anticipated (cancellation is identity-level arithmetic).

## Classification

GEOMETRIC. a_n[D²] are Weyl-asymptotic spectral invariants of D on M_4 × SU(3) substrate. f is a regulator dressing, not a substrate excitation. Theorem is about spectrum structure, not phonon dynamics.
