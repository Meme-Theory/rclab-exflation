# Spectral action with zeta function regularization

**Authors:** Maxim A. Kurkov, Fedele Lizzi, Mairi Sakellariadou, Apimook Watcharangkool
**Year:** 2015
**arXiv:** 1412.4669v3
**Journal:** Physics Letters B

---

## Abstract

We propose a novel definition of the bosonic spectral action using zeta function regularization to address renormalizability and spectral dimensions. The key innovation: **the zeta spectral action eliminates all operators of dimension higher than four**, making the theory renormalizable. Unlike the cutoff spectral action (which is non-renormalizable), the zeta formulation contains only dimension-≤4 operators. Neutrino Majorana mass terms play a fundamental role in generating lower-dimensional operators (cosmological constant, Higgs mass, Einstein-Hilbert term).

---

## Historical Context

The cutoff spectral action S_Λ = Tr[φ(D²/Λ²)] has been the workhorse of Connes-Chamseddine NCG phenomenology since Chamseddine-Connes (1997), successfully encoding the Standard Model from geometric first principles. However, it suffers three critical drawbacks:

1. **Non-renormalizability**: High-energy bosons diverge like Λ⁴/p⁴, violating locality and requiring four-fermion interactions to cancel divergences
2. **Wrong Higgs potential**: Exact calculation via Laplace transform shows V(H) = Σ B_j exp(-f_j H²/Λ²), NOT a double-well potential. A quadratic mass term must be added by hand
3. **Three dimensionful constants tuned by hand**: The cosmological constant (~Λ⁴), Higgs vev, and gravitational constant G require ad hoc normalization independent of Λ—unnatural fine-tuning at unification scales (10¹⁴-10¹⁷ GeV)

The zeta formulation directly addresses these issues.

---

## Key Arguments and Derivations

### 1. Zeta Function Definition

**The zeta spectral action** is defined via the zeta function regularization of the trace:

$$S_\zeta := \lim_{s \to 0} \text{Tr} D^{-2s} := \zeta_D(0;D^2)$$

This is the heat kernel a₄ coefficient (conformal anomaly):

$$S_\zeta = a_4(D^2) = \int d^4x\sqrt{g} \mathcal{L}(x)$$

where $\mathcal{L}(x) = a_4(D^2, x)$ is the Lagrangian density.

**Advantage over cutoff action**: For a Laplace-type operator D², the zeta function has no pole at s=0, so ζ(0,D²) is well-defined. No cutoff function φ and scale Λ are needed as inputs.

### 2. Resulting Lagrangian

The exact Lagrangian from the zeta spectral action:

$$\mathcal{L}(x) = \beta_1 M^4 + \beta_2 M^2 R + \beta_3 M^2 H^2 + \beta_4 B_{\mu\nu}B^{\mu\nu} + \beta_5 W^\beta_{\mu\nu}W_\beta^{\mu\nu} + \beta_6 G^a_{\mu\nu}G_{\mu\nu}^a + \beta_7 H\left(-\nabla^2 - \frac{R}{6}\right)H + \beta_8 H^4 + \beta_9 C_{\mu\nu\rho\sigma}C^{\mu\nu\rho\sigma} + \beta_{10} R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}$$

where M is (up to a factor) a Majorana right-handed neutrino mass from D_F.

**Key observation**: This is the **most general renormalizable Lagrangian for QFT in curved spacetime** (12 operators total). No dimension->4 operators appear. All coefficients β_i are dimensionless constants determined by the Dirac operator D_K.

### 3. Role of Majorana Mass

In the standard model Dirac operator:

$$D_0 = \gamma^\mu(\partial_\mu + \omega_\mu) \otimes I + \gamma^5 \otimes D_F$$

where D_F is a finite-dimensional matrix containing fermion masses. The zeta action naturally generates:

- M⁴ term (cosmological constant analog) -- from Majorana mass dimension
- M²H² term (Higgs quadratic) -- from coupling Majorana mass to Higgs
- M²R term (Einstein-Hilbert action) -- gravitational sector

**Critical point**: Without the Majorana mass term, these lower-dimensional operators do NOT appear in the zeta action. The Majorana mass is thus fundamental to the structure of gravity and the CC within the framework—not an ad hoc insertion.

### 4. Spectral Dimensions

Unlike the cutoff action (which gives D_s=0 for all sectors), the zeta action produces **viable spectral dimensions**:

**For matter fields (Higgs, gauge bosons):**
$$D_s = 4$$
(coincides with topological dimension)

**For gravitational sector:**
$$D_s = 2$$

(from the Weyl-squared term). This implies improved UV convergence of gravitational propagators due to fourth-derivative terms.

The running spectral dimension is:

$$\tilde{D}_s(T) = -2 \frac{\partial \log P(T)}{\partial \log T}$$

where P(T,x,x') is the heat kernel. At T→0, $\tilde{D}_s(T) \to 2$; at T→∞, $\tilde{D}_s(T) \to 4$.

---

## Key Results

1. **Renormalizability**: The zeta spectral action is local, unitary, and renormalizable. No higher-dimension operators appear. All divergent loop diagrams can be regulated with standard dimensional regularization.

2. **Correct operator content**: All 12 dimension-≤4 operators of renormalizable curved-space QFT appear with correct structure (Ricci scalar, Weyl tensor, Higgs kinetic and potential, gauge field strengths).

3. **No ad-hoc fine-tuning of three scales**: The structure of M⁴, M²H², M²R terms emerges from Majorana mass in D_F. While the numerical coefficient M still requires experimental input for renormalization, it need not be unnatural.

4. **Viable UV behavior**: Fourth-derivative gravity terms improve UV convergence, compatible with asymptotic safety scenarios.

5. **Heat kernel is an exact result**: No asymptotic expansion needed (unlike cutoff action where convergence of heat kernel expansion is ambiguous).

---

## Impact and Legacy

This paper resolves the **renormalizability crisis** of the spectral approach. The cutoff action, while phenomenologically predictive, was fundamentally flawed as an effective theory valid up to Planck scale—it's non-renormalizable and requires ad-hoc subtraction schemes.

The zeta formulation:
- Enables consistent use of spectral geometry UP TO Planck scale without effective-theory caveats
- Provides a natural explanation for why neutrino Majorana masses couple to gravitational and cosmological sectors (they generate the lower-dimensional terms)
- Opens path to dynamical scale generation (à la Coleman-Weinberg and Sakharov)
- Connects spectral NCG to conformal gravity and induced-gravity scenarios

Kurkov-Lizzi-Sakellariadou established zeta regularization as the correct choice for NCG phenomenology. Subsequent papers by the team (Kurkov-Lizzi 2012, 2014, 2018) built on this foundation to refine Higgs phenomenology and spectral dimensions.

---

## Connection to Phonon-Exflation Framework

**CRITICAL for the framework**: The zeta spectral action formally decouples the cosmological constant term a₀ from the gravity term a₂. In the cutoff formulation, both arise from the same heat kernel expansion: a₀ ~ Λ⁴ and a₂ ~ Λ²R, so their ratio is a₀/a₂ ~ Λ²/R—set by the cutoff scale.

In the zeta formulation:
- a₀ (M⁴ term) comes from the Majorana mass insertion in D_F
- a₂ (R term) comes from the fermionic trace contribution to curvature

**Implication for phonon-exflation**: If the CC problem is mapped to a₀/a₂ = 6/R (Framework claim), the zeta formulation suggests the ratio might be adjustable by modifying the Dirac operator structure—specifically, by varying how Majorana mass couples to the spectral triple. This is Lizzi's research program: **find alternative spectral functionals that decouple a₀ from a₂**.

The papers arXiv:1103.0478, 1106.3263, 1210.2663, 1001.2036 extend this by deriving spectral action from anomaly cancellation, potentially exposing additional structure in the a₀/a₂ ratio.

**Current framework status**: The zeta action alone does not solve the CC problem—the Majorana mass M must still be tuned. But it provides a cleaner mathematical foundation for future spectral modifications.
