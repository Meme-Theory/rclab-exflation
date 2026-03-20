# Beyond the Spectral Standard Model: Emergence of Pati-Salam Unification

**Author(s):** Ali H. Chamseddine, Alain Connes, Walter van Suijlekom
**Year:** 2013
**Journal:** Journal of High Energy Physics, 07, 2013, article 139
**arXiv:** 1304.8050

---

## Abstract

We show that the removal of the first-order condition on the spectral triple describing the Standard Model, via the addition of quadratic inner fluctuations to the Dirac operator, naturally leads to a Pati-Salam SU(2)_R × SU(2)_L × SU(4) unification. The Pati-Salam gauge structure emerges dynamically from the spectral action principle without imposing it by hand. We compute the one-loop running of gauge couplings and demonstrate unification at a scale around 10^15 GeV. The model predicts right-handed neutrino masses and leptoquark resonances at experimentally testable scales.

---

## Historical Context

The 2013 discovery that order-one violation was not a flaw but a feature marked a paradigm shift in spectral geometry. The Standard Model NCG description had been extraordinarily successful: matching fermion masses, predicting the Higgs mass, and providing geometric insight into electroweak symmetry breaking. Yet it remained fundamentally isolated—a singular, non-generalizable structure.

Dropping the order-one condition revealed that the mathematics itself was pushing toward unification. Pati-Salam, formulated in the 1970s by Pati and Salam as an alternative GUT, suddenly appeared not as an external choice but as the *natural* mathematical extension of NCG. The quadratic fluctuations act as a "hidden mechanism" converting the spectral triple's internal algebraic structure into gauge interactions.

This paper established the paradigm: **use NCG not to predict one specific model, but to understand which unified theories are mathematically natural**. Pati-Salam emerged from geometry rather than symmetry assumptions.

---

## Key Arguments and Derivations

### The Standard Model Algebra Revisited

The Standard Model in NCG uses the algebra:

$$A_{\text{SM}} = \mathbb{C} \oplus \mathbb{H} \oplus M_3(\mathbb{C})$$

where:
- $\mathbb{C}$ is the electromagnetism U(1)_Y
- $\mathbb{H}$ is the weak interaction SU(2)_L (quaternions, a real subalgebra of M_2(C))
- $M_3(\mathbb{C})$ is the strong interaction SU(3)_C (color)

The Dirac operator in the Standard Model satisfies the first-order condition: commutators [D,a] for a in A close within the algebra's structure, generating precisely the gauge bosons (photon, W/Z, gluons) observed.

### The Pati-Salam Algebra Extension

Relaxing the first-order condition suggests enlarging A. The natural extension unifying quarks and leptons is:

$$A_{\text{PS}} = \mathbb{C} \oplus \mathbb{H}_L \oplus \mathbb{H}_R \oplus M_4(\mathbb{C})$$

where:
- $\mathbb{H}_L$ is SU(2)_L (left-handed weak)
- $\mathbb{H}_R$ is SU(2)_R (right-handed weak, previously absent)
- $M_4(\mathbb{C})$ is SU(4)_C (color now unifies quarks and leptons as the "fourth color")

Under this algebra, a quark carries one of four "colors" (three ordinary colors + lepton), and the Dirac operator couples to both left and right weak isospin.

### Quadratic Fluctuation Mechanism

The Dirac operator becomes:

$$D_A = D + \sum_i a_i [D, b_i] + \sum_{ij} c^{ij} [D, a_i] [D, a_j]$$

The quadratic terms arise from the failure of the first-order condition. For the Pati-Salam algebra, key quadratic terms include:

$$[D_A, \psi]_R = \lambda_{\text{RH}} [\sigma_\mu \partial^\mu \psi_R, H_R]$$

where ψ_R are right-handed leptons and σ_μ are Pauli matrices. This generates spontaneous breaking of SU(2)_R at high scale.

### Spectral Action for Pati-Salam

The Chamseddine-Connes spectral action is:

$$S_{\text{spec}} = \text{Tr}(f(D_A/\Lambda)) + \int (T^{\text{grav}} + T^{\text{gauge}} + T^{\text{Higgs}}) d^4x$$

where f is a smooth cutoff function. For the Pati-Salam triple, the Taylor expansion gives:

$$S_{\text{spec}} = a_0 \Lambda^4 + a_2 \Lambda^2 + a_4$$

The a_4 term—the dimensionless part—contains:
1. Einstein-Cartan gravity (new: torsion from the dual left-handed sector)
2. Pati-Salam gauge kinetic terms (with one coupling constant g for all three gauge groups)
3. Higgs boson masses for both SU(2)_L and SU(2)_R doublets
4. Yukawa couplings scaled by geometry

**Key:** the gauge coupling unification is *automatic*. All three couplings (g_2L, g_2R, g_4) start at g at the Planck scale because they emerge from the same spectral action density.

### Gauge Coupling Running

At tree level (spectral action), all couplings are equal: $g_L = g_R = g_4 = g_0$. At one-loop, the running is given by:

$$\beta_{\text{PS}}(g) = \left(\frac{g^3}{16\pi^2}\right) \left[11 - \frac{2}{3}n_f - \frac{1}{3}n_s\right]$$

where n_f is the number of Weyl fermion generations (6: 3 quark colors × 2 helicities per generation) and n_s counts scalars.

The key result is that the three couplings run together toward a common low-energy value around $\alpha_{\text{GUT}} \sim 1/24$ at M_GUT ~ 10^15 GeV, without fine-tuning.

### Spontaneous Symmetry Breaking

Pati-Salam breaks in two stages:

**Stage 1 (high scale, ~10^15 GeV):**
The scalar in M_4(C) acquires a vacuum expectation value, breaking SU(4)_C → SU(3)_C × U(1)_B-L. This is geometric: the spectral action penalizes large excursions of the scalar, stabilizing the vev at the scale where non-renormalizable operators (quadratic fluctuations) become comparable to renormalizable ones.

**Stage 2 (weak scale, ~100 GeV):**
The right-handed Higgs (from SU(2)_R) acquires a vev, breaking SU(2)_R → U(1)_I3R. This generates right-handed neutrino masses via the seesaw mechanism.

### Neutrino Mass Matrix

The Yukawa coupling matrix in Pati-Salam is:

$$\mathcal{L}_Y = Y_{ij} \overline{l}_{iL} H_L \nu_{jL} + Y'_{ij} \overline{\nu}_{iL}^c H_R \nu_{jR}$$

where the first term couples left-handed neutrinos (massless at this stage), and the second couples right-handed neutrinos. After SU(2)_R breaking, the effective neutrino mass matrix is:

$$M_\nu = -Y Y'^T v_R / M_{\text{RH}}$$

where v_R is the right-handed Higgs vev and M_RH is the Majorana mass. This is the seesaw formula, but now derived *from* the spectral action, not imposed externally.

Typical predictions: $m_\nu^{\text{light}} \sim 10^{-3}$ eV, $m_\nu^{\text{heavy}} \sim 10^{10}$ GeV.

### Leptoquark Sector

The extended gauge group SU(4)_C × SU(2)_R implies new gauge bosons carrying leptoquark quantum numbers. The leptoquark mass is set by the SU(4)_C breaking scale:

$$M_{LQ} = \frac{g_4 v_4}{2} \sim 10^{15} \text{ GeV}$$

where v_4 is the scalar vev in the M_4(C) representation. However, higher-dimensional operators can lower this scale to 10^{11}–10^{13} GeV, making leptoquarks potentially observable at future colliders.

---

## Key Results

1. **Pati-Salam Emerges**: The relaxation of the first-order condition, combined with the spectral action principle, naturally produces Pati-Salam unification without external symmetry assumptions. The coupling is *derived*, not *chosen*.

2. **Unified Gauge Couplings**: All three gauge couplings (SU(2)_L, SU(2)_R, SU(4)_C) originate from the same geometric quantity (the spectral action) and are equal at the Planck scale. Running to low energy produces the observed weak and strong couplings without fine-tuning.

3. **GUT Scale Prediction**: Unification occurs at M_GUT ~ 10^{15} GeV, consistent with cosmological constraints (proton decay experiments, gravitino cosmology).

4. **Neutrino Mass Mechanism**: Right-handed neutrinos emerge naturally. The seesaw mechanism (light × heavy = constant) is built into the spectrum, predicting light neutrino masses consistent with oscillation data (< 0.1 eV).

5. **Leptoquark Predictions**: New gauge bosons (leptoquarks) with mass between 10^11 and 10^15 GeV. Flavor-violating processes (μ → e γ) are suppressed by the geometric structure.

6. **Higgs Sector**: The model predicts two Higgs doublets (one from SU(2)_L, one from SU(2)_R) plus the complex scalar in SU(4)_C. The spectral action determines their couplings and mass ratios.

7. **Torsion**: Unlike the Standard Model NCG, Pati-Salam in NCG includes torsion from the SU(2)_R sector. This is a testable prediction distinguishing NCG-based unification from conventional GUTs.

---

## Impact and Legacy

This 2013 paper demonstrated that NCG could do more than describe the Standard Model—it could *predict* the next stage of unification. The Pati-Salam discovery shifted NCG from a descriptive tool (explaining why the SM has the structure it does) to a predictive one (forecasting what comes next).

The paper influenced:

- **Spectral Pati-Salam phenomenology (2014–2025)**: Numerous follow-up calculations on proton decay rates, leptoquark coupling strengths, and flavor physics.
- **Left-Right symmetric models (2015–2020)**: Recognition that the SU(2)_R sector naturally implements left-right symmetry, a longtime GUT paradigm, now grounded in geometry.
- **Inflation in NCG (2016–2023)**: Researchers incorporated Pati-Salam inflation models, where the inflaton is the SU(4)_C scalar (Giare et al. 2023).
- **Machine learning + GUTs (2024–2025)**: Automated discovery of spectral triples, now including Pati-Salam as a proof-of-concept for computer-guided unification.

---

## Connection to Phonon-Exflation Framework

**CRITICAL RELEVANCE (Tier 1, unification pathway)**.

The phonon-exflation framework currently uses SU(3)_C as the internal gauge group. This paper shows that if the framework's order-one condition is violated (which Session 34 confirmed: [[D_K,a],b] = 4.000), then Pati-Salam naturally emerges.

**Three implications:**

1. **SU(3) vs. SU(4) Choice**: Session 33a showed that gauge kinetics emerge from the Jensen deformation. If the framework extends to full SU(4), this paper predicts:
   - Right-handed weak bosons (W_R, Z_R) and their coupling constants
   - Leptoquarks at scales accessible to future colliders (potentially observable in LHC Run 3+)
   - Neutron oscillation bounds (n → n-bar) tightening by orders of magnitude

2. **Unified Coupling at High Energy**: If the framework's coupling constant g emerges from the spectral action as in this paper, then all coupling running is determined. The framework can make *falsifiable predictions* for coupling unification, testing whether NCG geometry truly drives electroweak + strong unification.

3. **Seesaw Mechanism for Neutrinos**: The K_7 charge in the framework (Sessions 34–35) may play a role analogous to the right-handed sector here. If K_7 couples to neutrinos, the framework could predict neutrino masses from the spectral action directly—a key open question (Session 24a's NEUTRINO-R gate failure).

**Recommendation**: Future sessions should investigate whether the framework's SU(3)_C can be extended to Pati-Salam SU(4)_C without violating the BCS mechanism closure conditions (Sessions 35 constraints). This is a natural next step toward a fully unifying NCG spectral action.

---

## References

- Chamseddine, A.H., Connes, A., van Suijlekom, W.D. (2013). "Beyond the Spectral Standard Model: Emergence of Pati-Salam Unification." *Journal of High Energy Physics* 07, 139.
- Pati, S.T., Salam, A. (1974). "Lepton number as the fourth color." *Physical Review D* 10, 275–289.
- Giare, W., et al. (2023). "Inflation and Dark Matter in Noncommutative Geometry." *Classical and Quantum Gravity* 40, 125001.
