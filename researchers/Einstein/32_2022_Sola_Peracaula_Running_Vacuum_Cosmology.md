# The Cosmological Constant Problem and Running Vacuum in the Expanding Universe

**Author(s):** Joan Solà Peracaula
**Year:** 2022
**Journal:** Philosophical Transactions of the Royal Society A, vol. 380, no. 2230, art. 20210182
**arXiv:** 2203.13757

---

## Abstract

We address the fundamental cosmological constant problem: quantum field theory predicts an enormous vacuum energy density that is wildly inconsistent with observations. We propose that the cosmic vacuum density is not truly constant but rather evolves mildly with the Hubble parameter through a "running vacuum model" (RVM). Using adiabatic renormalization in curved spacetime quantum field theory, we show that quantum matter effects induce a dynamical component of order $H^2$ in the vacuum density. This mechanism naturally alleviates tensions in present-day cosmology (H₀ and σ₈ tensions) and provides an alternative to dark energy scenarios requiring exotic fields.

---

## Historical Context

### The Cosmological Constant Problem

The cosmological constant problem, identified by Weinberg and others, is perhaps the most severe fine-tuning problem in physics:

1. **Quantum Field Theory Prediction**: In the Standard Model, the vacuum energy density (zero-point energy of all quantum fields) is:

$$\rho_{\text{vac}}^{\text{QFT}} = \sum_{\text{fields}} \int \frac{d^3 k}{(2\pi)^3} \frac{1}{2} \sqrt{k^2 + m^2}$$

Regularized with a hard UV cutoff $\Lambda_{\text{UV}} \sim M_{\text{Planck}}$, this integral diverges quadratically:

$$\rho_{\text{vac}}^{\text{QFT}} \sim M_{\text{Planck}}^4$$

This yields $\rho_{\text{vac}}^{\text{theory}} \sim 10^{113}$ J/m³.

2. **Observational Reality**: The actual dark energy density observed from supernovae and CMB is:

$$\rho_{\text{vac}}^{\text{obs}} \sim 10^{-9}$ J/m³

The ratio is $10^{122}$—the worst theoretical prediction in physics.

3. **The Fine-Tuning Paradox**: Either:
   - The QFT calculation is missing crucial physics (e.g., supersymmetry, which would cancel fermion and boson contributions).
   - The cosmological constant is not a fundamental constant but rather a derived quantity that varies.

### Historical Context of RVM

Joan Solà Peracaula has pioneered the "running vacuum model" (RVM) since the 1990s as an alternative to the cosmological constant problem. The RVM approach borrows ideas from QFT renormalization group flow: quantities that appear "constant" at one scale flow with the scale at another scale.

In cosmology, the natural "scale" is the Hubble parameter $H$. Thus, the vacuum density could flow with $H$:

$$\rho_{\text{vac}}(H) = \rho_0 + \nu (H^2 - H_0^2)$$

where $\nu$ is a small coefficient (typically $|\nu| < 10^{-3}$) that captures quantum matter corrections.

This idea has gained traction with the discovery of H₀ tension (different measurements of the Hubble constant disagree at 4-5σ) and σ₈ tension (matter clustering is weaker than ΛCDM predicts), both of which RVM can alleviate.

---

## Key Arguments and Derivations

### Adiabatic Renormalization in Curved Spacetime

The fundamental derivation begins with quantum field theory in curved spacetime. The stress-energy tensor for a scalar field $\phi$ is:

$$T_{\mu \nu} = \partial_\mu \phi \partial_\nu \phi - \frac{1}{2} g_{\mu \nu} (\partial \phi)^2 - m^2 g_{\mu \nu} \phi^2 / 2$$

In a cosmological background with scale factor $a(t)$, the vacuum expectation value of the stress-energy tensor acquires corrections from loop diagrams. These corrections diverge and must be renormalized.

**Adiabatic Renormalization Prescription**:

The vacuum energy is split into adiabatic orders:

$$\langle T_{\mu \nu} \rangle = \langle T_{\mu \nu} \rangle^{(0)} + \langle T_{\mu \nu} \rangle^{(2)} + \langle T_{\mu \nu} \rangle^{(4)} + \ldots$$

where the superscript denotes the adiabatic order (related to how rapidly $a(t)$ changes).

**Zeroth Order**: The classical stress tensor.

**Second Order** ($O(H^2)$): Quantum loop corrections from matter fields, proportional to $H^2$ (the leading curvature invariant in cosmology).

**Fourth Order** ($O(H^4)$): Higher-loop corrections involving Riemann tensor components.

### Leading Quantum Correction: The H² Term

For a massive scalar field of mass $m$ in a Friedmann universe, the adiabatic second-order renormalization yields:

$$\langle T_{00} \rangle^{(2)} = \frac{\hbar}{16\pi^2} \left[ m^4 \log(m^2/\mu^2) + \frac{m^2 H^2}{6} + O(H^4) \right]$$

where $\mu$ is the renormalization scale.

The term linear in $H^2$ is the key result:

$$\Delta \rho_{\text{vac}} \sim \frac{\hbar m^2}{16\pi^2} H^2$$

Summing over all Standard Model fields (massive and massless):

$$\rho_{\text{vac}}(H) = \rho_0 + c H^2$$

where:

$$c \approx \frac{\hbar}{16\pi^2} \sum_{\text{all fields}} m^2 \approx 10^{-3} \times (\text{Planck scale})^2$$

The coefficient $c$ is remarkably small because of natural cancellations (massive particles contribute positively, but massless field loop corrections and renormalization conventions reduce the net effect).

### Running Vacuum Model (RVM) Equations

The RVM Friedmann equations become:

$$H^2 = \frac{8\pi G}{3} \left[ \rho_m + \rho_r + \rho_0 + \nu (H^2 - H_0^2) \right]$$

where $\nu$ parameterizes the $H^2$ correction:

$$\nu \approx \frac{c}{M_{\text{Planck}}^2}$$

Rearranging:

$$H^2 (1 - 8\pi G \nu / 3) = \frac{8\pi G}{3} [\rho_m + \rho_r + \rho_0 - \nu H_0^2]$$

In the limit $\nu \ll 1$ (valid for $|\nu| < 10^{-3}$):

$$H^2 \approx \frac{8\pi G}{3(1 - 8\pi G \nu/3)} [\rho_m + \rho_r + \rho_{\Lambda,\text{eff}}]$$

where the effective cosmological constant is:

$$\rho_{\Lambda,\text{eff}}(t) = \rho_0 - \nu H_0^2 + \nu H^2(t)$$

**Key Insight**: The vacuum density evolves as $H$ changes. At early times ($H > H_0$), $\rho_{\text{vac}} > \rho_0$; at late times ($H < H_0$), $\rho_{\text{vac}} < \rho_0$. This mild evolution has no observational impact on inflation (where $H \gg H_0$) but affects dark energy dynamics (where $H \sim H_0$).

### Equation of State in RVM

The effective equation of state parameter is:

$$w_{\text{eff}}(a) = \frac{p_{\text{eff}}}{\rho_{\text{eff}}} = \frac{-\rho_\Lambda(a)}{\rho_m(a) + \rho_r(a) + \rho_\Lambda(a)}$$

At early times (matter/radiation domination):
$$w_{\text{eff}} \approx 0 \text{ or } 1/3$$

At late times (dark energy dominated):
$$w_{\text{eff}} \approx -1 + \frac{\nu H_0^2}{\rho_0}$$

Thus, RVM naturally produces a **dynamical dark energy** with $w \neq -1$, and the deviation is controlled by the microscopic parameter $\nu$.

### Higher-Order Terms: O(H⁴) Contributions

Beyond the leading $H^2$ correction, there are higher-order terms:

$$\rho_{\text{vac}}(H) = \rho_0 + \nu_1 H^2 + \nu_2 H^4 + \ldots$$

The $O(H^4)$ term arises from:
1. Two-loop graphs with quartic couplings.
2. One-loop graphs involving the Riemann tensor $R_{\mu \nu \rho \sigma}$.

In inflation, the $H^4$ term becomes important:

$$\rho_{\text{vac}}^{\text{inf}} = \rho_0 + \nu_1 H_{\text{inf}}^2 + \nu_2 H_{\text{inf}}^4$$

This can trigger early-universe inflation without an explicit inflaton field (pure vacuum dynamics).

---

## Key Results

1. **Quantum Origin of Dynamical Dark Energy**: RVM provides a natural UV completion for dynamical dark energy, grounded in adiabatic renormalization, avoiding ad hoc quintessence fields.

2. **Alleviates H₀ Tension**: By allowing $w(z) \neq -1$, RVM accommodates higher early-universe expansion rates (derived from CMB data) while still fitting the local Hubble tension (lower $H_0$ from SNe).

3. **Alleviates σ₈ Tension**: The slower growth of structure in RVM (due to time-varying dark energy) reduces the matter clustering compared to ΛCDM, bringing observations into agreement.

4. **Natural Inflation**: The $O(H^4)$ contributions can drive inflation in the early universe from vacuum dynamics alone, without inflaton.

5. **Running of Constants**: RVM naturally incorporates running of the Fine Structure Constant and other couplings, predicted but unconstrained by ΛCDM.

6. **Particle Physics Connection**: The parameter $\nu$ is directly tied to Standard Model couplings and masses through renormalization group equations, connecting cosmology to collider physics.

7. **Observational Distinguishability**: RVM produces distinct predictions for CMB polarization, matter power spectrum, and BAO that differ from ΛCDM at the 1-2σ level, allowing tests with upcoming surveys (DESI, LSST).

---

## Impact and Legacy

Solà Peracaula's RVM program has catalyzed several research directions:

- **Renormalization Group Cosmology**: Extensions of RVM incorporating full renormalization group flow at all scales.
- **Trace Anomaly Cosmology**: Connection of RVM to the trace anomaly of the energy-momentum tensor in QFT.
- **Unification with Scalar Tensor Theories**: Some authors have shown RVM is equivalent to specific Brans-Dicke theories.
- **Quantum Cosmology**: Application of RVM to Wheeler-DeWitt equation and minisuperspace models.
- **Observational Programs**: DESI, Planck+ACT, and other collaborations now routinely test RVM constraints alongside ΛCDM.

---

## Connection to Phonon-Exflation Framework

**Relevance: HIGH — τ-Dependent Spectral Action as Running Vacuum**

The phonon-exflation framework predicts that the cosmological "constant" is **not constant**: it is the spectral action of the Dirac operator on M4 × SU(3), and this action depends on the K7 structure parameter τ.

**Structural Isomorphism**:

1. **RVM Vacuum Density**:
$$\rho_{\text{vac}}(H) = \rho_0 + \nu(H^2 - H_0^2)$$

2. **Phonon-Exflation Spectral Action**:
$$S_{\text{spec}}(\tau) = \int_0^\infty \frac{ds}{s} a_0(s) e^{-s\lambda_n(\tau)}$$

where $\lambda_n(\tau)$ are the eigenvalues of the Dirac operator (which depend on τ through the K7 curvature).

The effective cosmological constant emerges as:
$$\Lambda_{\text{eff}}(\tau) = \frac{S_{\text{spec}}(\tau)}{M_{\text{Planck}}^2 \cdot V_{\text{spacetime}}}$$

**Session 24b Result** (Monotonicity): The spectral action is **monotone** in τ:

$$\frac{dS_{\text{spec}}}{d\tau} > 0$$

This monotonicity is structurally equivalent to RVM's $\nu > 0$: both predict that the effective vacuum energy increases as the system evolves (as H decreases in cosmology, as τ increases in phonon-exflation's internal dynamics).

**Equivalence Mapping**:

| RVM Parameter | Phonon-Exflation | Physical Meaning |
|:---|:---|:---|
| $H$ | $\tau$ or $d\tau/dt$ | Expansion rate / structure change rate |
| $\rho_0$ | $S_{\text{spec}}(\tau=0)$ | Vacuum energy at fundamental scale |
| $\nu$ | $dS_{\text{spec}}/d\tau / M^2$ | Quantum correction strength |
| $w_{\text{eff}} \approx -1 + O(\nu)$ | $w = -1$ | Near-de Sitter equation of state |

**Key Prediction**:
- RVM predicts $w(z)$ evolves smoothly, with DESI detecting $w \approx -0.9$ to $-1.1$ at intermediate redshifts.
- Phonon-exflation predicts **exactly** $w = -1$ (monotonic spectral action → constant energy density → de Sitter), but with a **geometric source** (K7 dynamics), not dynamical fields.

**Distinguishing Test** (Session 42 Prediction):
- If DESI DR2 shows $w = -1$ (not varying), this supports phonon-exflation's geometric rigidity.
- If DESI DR2 shows $w(z) \neq -1$ significantly, this favors RVM's field-theoretic mechanism.

**DESI DR2 Status** (March 2025 Reality):
Recent DESI DR2 results show a **3.1σ hint** of dynamical dark energy ($w_0 \sim -0.72$, phantom crossing). This is intermediate: not fully ruled out by phonon-exflation's $w = -1$ prediction, but tension-creating.

**Reconciliation Strategy**:
The framework's S42 hypothesis proposes that DESI's $w \neq -1$ signal is a **lensing bias** from the 32-cell tessellation geometry (the SU(3) compactification), not true dynamical evolution. If confirmed, this would unify phonon-exflation (exact $w = -1$) with DESI (apparent $w \neq -1$), vindicating Peracaula's insight that running vacuum effects are geometric artifacts of internal structure.

**Status**: Peracaula's RVM is the strongest competing theory for dynamical dark energy. Phonon-exflation can now be positioned as the **geometric** completion of RVM: the "running" is not from quantum fields but from topological transitions of the internal fiber.
