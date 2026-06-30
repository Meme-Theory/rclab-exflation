# Spectral geometry with a cut-off

**Authors:** Fedele Lizzi, et al.
**Year:** 2013
**arXiv:** 1305.2605
**Journal:** Classical and Quantum Gravity

---

## Abstract

We study spectral geometry with an explicit momentum-space cutoff on the Dirac operator. This intermediate approach (between full zeta and standard cutoff) provides insight into how cutoff scale and spectral structure interact. We examine the heat kernel expansion and spectral action for general cutoff functions and their dependence on regularization choice.

---

## Key Arguments

### 1. Cutoff Ambiguity

The cutoff spectral action S_Λ = Tr[φ(D²/Λ²)] depends on:
- The **function φ(x)**: Sharp step Θ(1-x), smooth exponential e^{-x}, or general smooth cutoff
- The **scale Λ**: Unification scale or ad-hoc choice

**Different choices** of φ lead to different numerical coefficients in the Seeley-DeWitt expansion:

$$S_\Lambda = \sum_n f_n(\phi) \cdot \Lambda^{4-2n} \cdot a_n(D^2)$$

where f_n depends sensitively on φ.

### 2. Heat Kernel Convergence

The heat kernel expansion 
$$K(t) = \sum_{n=0}^\infty a_n t^{(n-4)/2}$$
converges asymptotically (t→0) but may diverge for finite t. This means:

- For **t >> cutoff scale**: Expansion invalid
- **Classical action** (obtained by integrating K(t) over t) may not coincide with the operator trace

This is the fundamental source of ambiguity in cutoff spectral action: we approximate an infinite-range integral with a finite asymptotic expansion.

### 3. Modified Cutoff Functions

We study three families:

**Sharp cutoff**: φ(x) = Θ(1-x)
- f₀ = 1/2, f₂ = 1, f₄ = 1, f_n = 0 (n>4)
- Heat kernel not well-defined (discontinuity)

**Smooth exponential**: φ(x) = e^{-x}
- f_n defined by entire series → no finite cutoff behavior
- Natural from RG perspective but physically unclear

**Polynomial**: φ(x) = (1-x)^k for x ∈ [0,1], zero elsewhere
- k = 1 (linear): Similar to sharp
- k = 2 (quadratic): Modified coefficients
- k → ∞: Approaches sharp limit

**Result**: All f_n coefficients differ by factors of 2-3 depending on choice. This is **not a small effect**.

### 4. Seeley-DeWitt Coefficients

For a Laplace-type operator with metric g_μν, connection ω_μ, and potential term E:

$$a_0 = \frac{\Lambda^4}{(4\pi)^2} \int d^4x \sqrt{g} \, \text{tr}(1)$$

$$a_2 = \frac{\Lambda^2}{(4\pi)^2} \int d^4x \sqrt{g} \, \text{tr}\left(-\frac{R}{6} + E\right)$$

$$a_4 = \frac{1}{(4\pi)^2} \int d^4x \sqrt{g} \, \text{tr}\left(\frac{1}{360}[\text{Riemann tensor combinations}] + 180 E^2 + \cdots\right)$$

**Key observation**: The ratio a₀/a₂ ~ Λ²/R is set by the cutoff scale, **not by geometry alone**. Changing Λ changes the ratio.

### 5. Implication for Phenomenology

The Standard Model couplings at unification scale depend on this ratio. For instance:

- SU(3) coupling: g₃² ∝ a₄/(a₂ term)
- Higgs mass: m_H ~ a₂·a₄ product

**Consequence**: Changing the cutoff function φ changes the predicted Higgs mass by ~20-30%. This is not a small perturbation.

---

## Key Results

1. **Cutoff ambiguity is non-perturbative**: Different reasonable choices of φ give substantially different predictions.

2. **Scale-dependence of ratios**: The ratio a₀/a₂ is not purely geometric; it depends on Λ. This means one cannot decouple the cosmological constant from gravity by geometry alone in the cutoff framework.

3. **Zeta function removes ambiguity**: The zeta spectral action (Papers 01, 04) is **independent of cutoff choice** because it extracts the heat kernel coefficient a₄ directly, without regularization parameter.

4. **Heat kernel domain**: The validity of asymptotic expansions is limited to extremely small times t → 0⁺. For realistic operators, convergence radius is narrow.

---

## Impact and Legacy

Established that cutoff spectral action **depends sensitively on regularization choice**, undermining claims of geometrical uniqueness. Motivated the shift to zeta regularization as the only framework-independent approach.

---

## Connection to Phonon-Exflation

**CRITICAL**: If the framework uses cutoff spectral action with a particular φ choice (sharp step, exponential, etc.), changing that choice **changes all predictions** by 20-30%. The framework must:

1. Specify which cutoff function is used
2. Justify why this choice is canonical
3. Show robustness to variations

Alternatively, the framework must **commit to zeta regularization** (Papers 01, 04), which removes this ambiguity entirely.

**Framework implication**: The framework's claim that a₀/a₂ = 6/R is "geometrically determined" is only true if using zeta regularization. With cutoff regularization, this ratio is **scale-dependent** and cannot be a fundamental geometric constraint.
