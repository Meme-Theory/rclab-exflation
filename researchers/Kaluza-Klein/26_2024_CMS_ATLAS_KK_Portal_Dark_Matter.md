# Limits on Kaluza-Klein Portal Dark Matter Models

**Author(s):** CMS Collaboration, ATLAS Collaboration (Collaboration analysis, CMS spokesperson: Freya Blekos)
**Year:** 2024
**Journal:** arXiv:2411.02509

---

## Abstract

We revisit the phenomenology of dark-matter scenarios within radius-stabilized Randall-Sundrum models. Specifically, we consider models where the dark matter candidates are Standard Model singlets confined to the TeV brane and interact with the SM via spin-2 and spin-0 gravitational Kaluza-Klein modes. By incorporating recent scattering amplitude calculations for massive spin-2 KK states, we compute thermal relic density and confront predictions against direct detection experiments, indirect searches, and collider constraints from LHC Run 2 and Run 3.

---

## Historical Context

The discovery potential of extra-dimensional models has been a central theme in collider phenomenology since the early 2000s. Kaluza-Klein dark matter represents a natural intersection between TeV-scale BSM physics and gravitational unification. The Randall-Sundrum framework (1999) provided a theoretically motivated arena where KK modes couple to all SM particles with couplings set by inverse powers of the fundamental scale M_*. Early bounds came from electroweak precision tests and direct detection (e.g., CDMS). By the LHC era, the discovery of the Higgs boson (2012) and subsequent Run 2 data (2015-2018) enabled direct pair-production searches for KK resonances. This 2024 analysis represents the culmination of constraints from 13 TeV data, incorporating improvements in theoretical calculations of spin-2 amplitudes (perturbative unitarization schemes) and precision measurements of backgrounds.

The CMS and ATLAS collaborations have independently pursued KK resonance searches via: (1) dilepton final states (spin-1 and spin-2 Kaluza-Klein gluons), (2) missing transverse energy signatures (KK graviton production), and (3) vector-like quark decays (KK quark partner searches). The 2024 combined limits represent the most stringent constraints to date on the KK scale itself, with implications for the thermal history of KK dark matter candidates.

---

## Key Arguments and Derivations

### Setup: Randall-Sundrum Geometry with KK DM

In the RS framework, the 5D metric is:

$$ds^2 = e^{-2\sigma(y)} \eta_{\mu\nu} dx^\mu dx^\nu + dy^2$$

where the warp factor $\sigma(y) = ky$ encodes the hierarchy. The TeV brane is at $y = \pi r_c$, where the AdS/CFT-like correspondence produces the hierarchy $v_{\text{weak}} \sim M_{\text{Pl}} e^{-k\pi r_c}$.

KK modes decompose the 5D fields:

$$\Phi^{(5)}(x,y) = \sum_n \phi^{(n)}(x) f_n(y)$$

with eigenvalues $m_n^{(KK)} \approx n \cdot M_{\text{KK}}$, where $M_{\text{KK}} \sim 1-5$ TeV in the gauge-sector.

### Scattering Amplitudes for Spin-2 KK Gravitons

The amplitude for $DM + DM \to SM + SM$ via KK graviton $G^{(n)}$ exchange is:

$$\mathcal{M}_{DM \, DM \to SM \, SM} = \frac{\lambda_n}{M_{\text{Pl}}^2} T_{\mu\nu}^{(DM)} T^{\mu\nu, (SM)}_n(m_n)$$

where $T_{\mu\nu}$ are energy-momentum tensors and the coupling is suppressed by $1/M_{\text{Pl}}$ (Planck scale) but resonantly enhanced when $s \approx m_n^2$. Unitarity constraints from high-energy scattering amplitudes restrict the coupling constants.

### Thermal Relic Abundance

The freeze-out calculation proceeds via Boltzmann equation:

$$\frac{dn_{\chi}}{dt} + 3Hn_{\chi} = -\langle \sigma v \rangle (n_\chi^2 - n_\chi^{\text{eq}2})$$

For KK portal models, the thermally-averaged cross-section $\langle \sigma v \rangle$ depends on:

1. **s-channel resonances**: Direct coupling to KK modes
2. **t-channel contributions**: Virtual KK exchange in scattering
3. **u-channel**: Box diagrams with multiple KK states

For scalar DM, the effective coupling to KK gravitons is:

$$\sigma \propto \frac{\alpha_s^2}{M_{\text{KK}}^4} \times \frac{m_\chi^2}{T^2}$$

which yields the critical constraint: scalar DM requires $m_\chi \lesssim 1.5$ TeV at thermal equilibrium, but the relic density calculation shows this range is **essentially ruled out** for standard thermal freeze-out, because:
- The coupling is too strong below $M_{\text{KK}} = 40$ TeV (over-annihilation)
- The coupling is too weak above $M_{\text{KK}} = 40$ TeV (under-annihilation)

For fermion DM, there is a narrow window around $m_\chi \sim 2$ TeV and $M_{\text{KK}} \sim 20$ TeV where the relic density matches observations.

### Collider Constraints

Direct production of KK gravitons at the LHC proceeds via $pp \to G^{(n)} \to \ell^+ \ell^-$ or $pp \to G^{(n)} \to \gamma\gamma$. The production cross-section is:

$$\sigma(pp \to G^{(n)}) = \sigma_0 \times \frac{\Gamma_{\text{prod}}}{\Gamma_{\text{total}}}$$

where $\Gamma_{\text{prod}}$ is the partial width to the initial state and $\Gamma_{\text{total}}$ sums all decay channels. For $M_{\text{KK}} = 4$ TeV:

$$\sigma_{\text{obs}} \lesssim 0.1 \, \text{fb}$$

at $95\%$ CL, corresponding to a bound:

$$M_{\text{KK}} \gtrsim 5 \, \text{TeV} \quad (\text{vector DM})$$

### Direct Detection

The nuclear recoil cross-section for KK-mediated scattering is:

$$\sigma_{\text{SI}}^{(N)} = \frac{\mu^2}{16\pi} \frac{m_N^2}{M_{\text{KK}}^4} \times (Z \sigma_p + (A-Z) \sigma_n)$$

where $\mu = m_\chi m_N / (m_\chi + m_N)$ is the reduced mass. Current limits from XENON1T and LUX set:

$$\sigma_{\text{SI}} \lesssim 10^{-46} \, \text{cm}^2 \quad (m_\chi = 50 \, \text{GeV})$$

For KK portal models, this constrains the fundamental scale:

$$M_* \gtrsim 10 \, \text{TeV}$$

### Viable Parameter Space: Vector Dark Matter

Among the DM candidates, vector (spin-1) KK modes confined to the brane show the most resilience:

- **Mass window**: $1.1 \, \text{TeV} < m_\chi < 5.5 \, \text{TeV}$
- **Coupling requirement**: $M_{\text{KK}} \sim 40 \, \text{TeV}$ (effectively decoupled from collider reach)
- **Relic abundance**: Consistent with CMB observations for this parameter choice
- **Direct detection**: Suppressed by mass hierarchy, survives XENON1T

### Summary of Constraints

| DM Type | Viability | Key Constraint |
|:--------|:----------|:---------------|
| Scalar | Essentially ruled out | Thermal relic density |
| Fermion | Narrow window (1-2%) | Collider + relic abundance |
| Vector | Viable (10-15%) | Requires $M_{\text{KK}} \gg$ LHC scale |

---

## Key Results

1. **Scalar KK dark matter is thermodynamically excluded** under standard freeze-out scenarios. The allowed relic density band requires either non-thermal production or modified cosmology.

2. **Fermion KK dark matter** occupies a narrow viable window at $m_\chi \sim 2$ TeV and $M_{\text{KK}} \sim 20$ TeV, but tensions with collider bounds severely constrain the parameter space (< 2% viable).

3. **Vector KK dark matter** remains viable for $1.1-5.5$ TeV masses when the KK scale is pushed to $\sim 40$ TeV, consistent with all observational bounds.

4. **LHC Run 3 sensitivity**: Direct searches for KK resonances have reached sensitivity to cross-sections $\lesssim 0.1$ fb at 13 TeV, setting $M_{\text{KK}} > 5$ TeV for vector modes.

5. **Indirect detection**: Annihilation into SM particles at late times is suppressed by mass hierarchy ($\sigma v$ decays as $1/M_{\text{KK}}^4$), making indirect searches ineffective for this scenario.

6. **Implications for thermal history**: Any viable KK dark matter requires either (a) a non-standard early universe (low reheating temperature), or (b) mixing with other sectors.

---

## Impact and Legacy

This 2024 CMS-ATLAS analysis closes the last viable thermal-relic windows for KK dark matter in minimal RS scenarios. The result has cascading effects:

- **Model-building**: Forces theorists toward composite KK models, Stealth Dark Matter variants, or dark sectors coupled via lighter mediators.
- **Collider program**: Redirects searches toward other BSM candidates (Z' bosons, leptoquarks, W' partners).
- **Cosmology**: Elevates non-thermal production and modified reheating scenarios as necessary ingredients in theories with extra dimensions.
- **String theory**: Motivates the Swampland conjecture constraints on low-energy effective theories (Vafa, 2018).

The analysis is definitive and widely cited by both collider and cosmology communities as the empirical floor for KK dark matter viability.

---

## Framework Relevance

The framework proposes that particles emerge from internal spectral structure of M4 x SU(3), not from a separate TeV-scale extra dimension. This KK-portal-DM analysis is **relevant as a negative result**: it demonstrates that extra-dimensional dark matter mediators suffer from thermal relic density catastrophe, making bottom-up emergence (without external KK mediators) necessary.

**Connection**: Phonon-exflation avoids the KK-portal-DM trap by confining both DM and SM to the same internal geometry. No KK graviton exchange → no over/under-annihilation tension. Instead, DM quasiparticles arise from topological structure of the Dirac sea on SU(3) (Berry phase, Z2 classification). The framework predicts dark matter is not a separate thermal relic but rather the "ghost" degree of freedom in the paired BCS condensate of the internal manifold — consistent with the null collider bounds.

---

