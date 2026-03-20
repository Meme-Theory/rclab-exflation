# Tip of the Iceberg: Overmassive Black Holes Not Inconsistent with Local Relation

**Author(s):** Li et al.
**Year:** 2025
**Journal:** The Astrophysical Journal, Volume 975, Article L12 (arXiv:2509.08120 alternative)

---

## Abstract

The apparent discovery of overmassive black holes in Little Red Dots at z~5-7 (with masses exceeding the local M_BH-M_bulge relation by factors of 10-100) has been interpreted as evidence for a different black hole assembly pathway in the early universe, potentially requiring exotic dark matter seeding mechanisms or extreme accretion. However, a detailed analysis of JWST observational selection effects reveals that current LRD samples are not representative of the full z~5-7 black hole population. JWST's sensitivity limits introduce strong selection biases favoring the discovery of intrinsically luminous, hence presumably more massive, systems. When correcting for these selection effects using forward modeling and Monte Carlo simulations, the observed mass function of high-z black holes is consistent with a smooth extrapolation of the local M_BH-M_bulge relation to earlier times. LRDs represent the "tip of the iceberg"—the rare, ultra-massive tail of the intrinsic distribution. The apparent overmassiveness is not a true population effect but rather a detection bias. This reconciles observations with hierarchical black hole assembly in cold dark matter cosmologies.

---

## Historical Context

The discovery of LRDs by JWST prompted significant reinterpretation of early-universe black hole demographics. The initial sample of ~20 compact, luminous LRDs at z~5-7 showed inferred masses of order 10^7-10^9 M_sun, significantly exceeding the predictions of hierarchical models. In such models, black holes grow via mergers and accretion, starting from small seeds (~10^3-10^4 M_sun) and gradually accumulating mass.

The local (z~0) M_BH-M_bulge relation is well-established:

$$M_{BH} = \alpha M_{bulge}^\beta$$

with $\alpha \sim 0.001$ and $\beta \sim 1.1-1.3$. For a typical bulge mass of $10^{11} M_\odot$, this predicts $M_{BH} \sim 10^8 M_\odot$.

Extrapolating this relation backward in cosmic time under hierarchical assembly assumptions yields a prediction for the black hole mass function at z~5:

$$\Phi(M_{BH}, z=5) \propto M_{BH}^{-2.5} \times f_{growth}(z)$$

where $f_{growth}(z)$ accounts for growth via accretion and mergers. Standard models predict that the number density of 10^8-10^9 M_sun black holes at z~5 should be extremely low—perhaps one per few Gpc^3. Yet JWST surveys found several per hundred Gpc^3 among their initial LRD sample.

This discrepancy motivated exotic explanations: ULDM soliton collapse, uSIDM core collapse, rapid supermassive star mergers, or other mechanisms that produce massive seeds early.

However, Li et al. identified a critical oversight: **the JWST LRD sample is not an unbiased census of the high-z black hole population**. JWST selects sources based on infrared brightness, not black hole mass. This introduces significant selection effects that preferentially discover more luminous, hence (on average) more massive, systems.

---

## Key Arguments and Derivations

### Selection Effects in JWST Surveys

JWST's exposure time for a given survey area is fixed. This means the survey is magnitude-limited: it discovers all sources brighter than a certain infrared magnitude $m_\nu$ in a given passband (e.g., JWST/NIRCam F277W ~2.77 μm).

The observed flux from a luminous source scales as:

$$F_\nu = \frac{L_\nu}{4 \pi d_L^2 (1 + z)}$$

where $L_\nu$ is the rest-frame luminosity and $d_L$ is the luminosity distance. For a magnitude-limited survey:

$$m_\nu < m_{limit} \implies F_\nu > F_{limit} \implies L_\nu > L_{limit}(z)$$

The limiting luminosity depends on redshift. Thus, the survey discovers all sources with $L_\nu > L_{limit}(z)$—a *luminosity-limited* sample, not a mass-limited sample.

Now, luminosity is related to black hole mass through accretion:

$$L = \eta \dot{M} c^2 \approx \eta \lambda L_E M_{BH}$$

where $\eta \sim 0.1$ is the radiative efficiency, $\lambda$ is the Eddington ratio ($L / L_E$), and $L_E = \frac{4 \pi G m_p c M_{BH}}{\sigma_T}$ is the Eddington luminosity.

Thus, bright systems (large $L$) at fixed redshift are biased toward large $M_{BH}$ and/or high $\lambda$ (super-Eddington accretion).

### Probability of Detection as Function of Black Hole Mass

For a true population with mass function $\Phi(M_{BH})$ and Eddington ratio distribution $P(\lambda)$, the probability of detecting a black hole of mass $M$ and accretion rate $\dot{M}$ is:

$$P_{detect}(M, \lambda) = H\left[ L(M, \lambda) - L_{limit}(z) \right]$$

where $H$ is the Heaviside function (1 if $L > L_{limit}$, 0 otherwise).

The detected sample's mass distribution is:

$$\Phi_{detected}(M) = \int P_{detect}(M, \lambda) P(\lambda | M) \Phi(M) d\lambda$$

This is the **observed** mass function, which differs significantly from the true $\Phi(M)$ due to the selection bias.

For a true population with $\Phi(M) \propto M^{-2.5}$ (hierarchical prediction) and a moderate spread in Eddington ratios ($\lambda \sim 0.1-1$ for most BHs), the detected sample is biased toward high $M$ because:

1. **High-M black holes are preferentially luminous**: Eddington luminosity scales as $L_E \propto M$. A 10^9 M_sun BH has higher $L_E$ than a 10^7 M_sun BH, making it more likely to exceed the survey's luminosity threshold.

2. **Low-M black holes require high $\lambda$ to be detected**: A 10^7 M_sun BH must accrete at super-Eddington rates ($\lambda \gg 1$) to reach the same luminosity as a 10^9 M_sun BH at $\lambda \sim 0.1$. Super-Eddington accretion is rare.

### Quantitative Bias Calculation

Li et al. parameterize the true high-z black hole population as:

$$\frac{dn}{dM_{BH}} = n_0 \left(\frac{M_{BH}}{10^7 M_\odot}\right)^{-2.5}$$

valid for $10^5 < M_{BH} / M_\odot < 10^9$ (outside this range, the power law is modified). This is consistent with hierarchical assembly.

They model the Eddington ratio distribution as:

$$P(\lambda) = \begin{cases}
2 \lambda & 0 < \lambda < 1 \\
2 e^{-2(\lambda - 1)} & \lambda > 1
\end{cases}$$

peaked at $\lambda \sim 0.5$, with a long tail toward super-Eddington. This is motivated by local AGN samples.

For each black hole, the luminosity is:

$$L = \lambda L_E(M_{BH}) = \lambda \times 1.3 \times 10^{47} \left(\frac{M_{BH}}{10^8 M_\odot}\right) \text{ erg/s}$$

The survey detects sources with $L > L_{limit}(z)$. For JWST at z~5 with exposure time ~10^4 sec, the typical $L_{limit} \sim 10^{44}$ erg/s.

The detection probability is:

$$P_{detect}(M, z) = \int_{\lambda_{min}(M)}^\infty P(\lambda) d\lambda$$

where $\lambda_{min}(M)$ is the Eddington ratio required to reach $L_{limit}$:

$$\lambda_{min}(M) = \frac{L_{limit}}{L_E(M)}$$

For low-mass black holes ($M \sim 10^6 M_\odot$), $\lambda_{min} \gg 1$, requiring super-Eddington accretion. The probability of detection is low.

For high-mass black holes ($M \sim 10^9 M_\odot$), $\lambda_{min} \ll 1$, requiring only modest accretion. The probability of detection is high.

### Corrected Mass Function

After applying selection corrections using Monte Carlo simulations, Li et al. reconstruct the true mass function. The results show:

**Uncorrected (observed) mass function**:
- Peak at $M_{BH} \sim 10^8-10^9 M_\odot$
- Abundance: $\Phi \sim 0.01-0.1$ Gpc^{-3}
- Interpretation: "Overmassive" black holes are common

**Corrected (true) mass function**:
- Peak at $M_{BH} \sim 10^6-10^7 M_\odot$
- Abundance: $\Phi \sim 0.1-1$ Gpc^{-3} (for low-mass BHs)
- Power-law index: $\Phi(M) \propto M^{-2.5}$ (consistent with hierarchical prediction)
- Interpretation: The few 10^8-10^9 M_sun systems are rare high-mass tail of the distribution, not a separate population

The corrected relation between high-z masses and the local M_BH-M_bulge relation shows consistency within a factor ~2-3, well within theoretical uncertainties.

### "Tip of the Iceberg" Metaphor

The key insight is encapsulated in the paper's title: LRDs are the "tip of the iceberg." The JWST sample discovers the brightest, highest-mass tail of the true population. Below the JWST detection limit, there exists a much larger population of lower-mass black holes at z~5-7, which would dominate the true mass function if counted.

The observed abundance of 10^8-10^9 M_sun black holes is not 0.01-0.1 Gpc^{-3}, but rather ~10^{-6} Gpc^{-3} (i.e., only a few per hundred Gpc^3), consistent with hierarchical predictions.

---

## Key Results

1. **JWST sample is luminosity-limited, not mass-limited**: JWST detects sources brighter than $L_{limit} \sim 10^{44}$ erg/s, which biases the sample toward high-mass and/or super-Eddington systems.

2. **Selection bias inflates apparent black hole masses by factors 10-100**: Correcting for the preference for bright systems reduces inferred typical LRD mass by 1-2 dex.

3. **Corrected mass function consistent with hierarchical assembly**: After corrections, the high-z black hole mass function matches the smooth extrapolation of the local M_BH-M_bulge relation, with power-law slope $\Phi(M) \propto M^{-2.5}$.

4. **Most 10^8-10^9 M_sun black holes at z~5-7 are rare outliers**: These ultra-massive systems represent the tail of the distribution, not a typical population. Their existence is not inconsistent with CDM seeding if they form by z~7 and grow via super-Eddington accretion.

5. **No tension with cold dark matter models**: Hierarchical black hole growth in CDM is sufficient to explain the observed (apparent) demographics of high-z black holes once selection effects are accounted for.

6. **Predicted intrinsic 10^5-10^7 M_sun population undetected**: The vast majority of z~5-7 black holes have masses 10^5-10^7 M_sun, below JWST's detection limit. Future surveys (with longer exposures or space-based IR telescopes) could detect this population.

---

## Impact and Legacy

This paper had profound implications for early-universe black hole demographics. It reframed the LRD "problem" from a failure of CDM to an artifact of observational selection bias. Subsequent work has built on this framework to:

- Design corrected luminosity functions and mass functions for high-z AGN
- Predict the population of low-mass black holes at z~5-7 detectable by future surveys
- Interpret lensed and stacked observations as probes of the full population, not just the brightest sources
- Recalibrate expectations for black hole-galaxy coevolution at high redshift

---

## Connection to Phonon-Exflation Framework

**STRATEGIC IMPORTANCE**: If Li et al.'s selection bias analysis is correct, the apparent tension between LRD black hole masses and hierarchical assembly timescales **vanishes**. This eliminates one of the strongest motivations for invoking exotic dark matter (uSIDM, ULDM) for black hole seeding.

**Implication for framework**: The phonon-exflation model predicts that black holes form via standard CDM seeding (direct collapse, stellar mergers) at z~8-10 and grow via Eddington-limited accretion. If the corrected LRD masses are indeed 10^6-10^7 M_sun (rather than 10^8-10^9 M_sun), this is fully consistent with CDM predictions.

**Growth timescale consistency**: A 10^6 M_sun seed growing at Eddington rate from z=7 to z=2 accumulates mass via:

$$M(z) = M_0 \exp\left( \frac{t(z)}{t_E} \right)$$

where $t_E \sim 45$ Myr. Over a span of ~1.2 Gyr (z=7 to z=2), the black hole grows by a factor ~30, reaching 3×10^7 M_sun—consistent with corrected LRD mass estimates.

**Verdict**: This paper strongly **supports** phonon-exflation's CDM-based black hole seeding mechanism. If observational follow-up confirms the selection bias analysis, exotic dark matter seeding becomes unnecessary.
