# Resurrecting Kaluza-Klein Dark Matter with Low-Temperature Reheating

**Author(s):** Multiple authors (non-standard cosmology collaboration)
**Year:** 2025
**Journal:** arXiv:2602.12154

---

## Abstract

Universal Extra Dimensions (UED) with Kaluza-Klein dark matter candidates have been severely constrained by the combination of relic abundance calculations and LHC bounds. We demonstrate that non-standard cosmological scenarios featuring low reheating temperatures can resurrect previously excluded parameter space. Specifically, entropy injection during a prolonged inflaton decay phase dilutes the dark matter relic abundance by orders of magnitude, allowing KK DM masses and coupling scales previously ruled out to become viable. We analyze consistency with direct detection, indirect searches, collider constraints, and BBN/CMB observations, finding a wide viable window for $m_{KK} \sim 500 - 1500$ GeV at $T_R \sim 1 - 10$ MeV.

---

## Historical Context

The UED framework (Appelquist, Cheng, Dobrescu 2000-2001) proposed that the Standard Model is embedded in a 5D spacetime with all fields propagating in the extra dimension. The lowest-lying KK mode ($n=1$) of the gauge boson serves as a stable dark matter candidate, automatically providing the observed relic abundance through thermal freeze-out. Early predictions (2000-2005) were promising: $m_{KK}^{DM} \sim 1-2$ TeV, naturally matching the WIMP miracle scale.

However, LHC constraints on KK resonances (particularly the $W^{(1)}$ and $Z^{(1)}$ modes) began to narrow the allowed window by 2010. By 2020, the combination of Run 2 bounds and precision electroweak constraints had effectively excluded minimal UED in the simplest thermal history scenario. The discovery of the Hubble tension (2019+) and new DESI results motivating dynamical dark energy (2023-2025) have opened interest in non-standard thermal histories.

This 2025 analysis resurrects KK DM by exploiting an underutilized degree of freedom: the reheating temperature after inflation. By allowing $T_R$ to be much lower than the standard GUT-scale value of $\sim 10^9$ GeV, entropy production during reheating can dilute the DM relic abundance post-freeze-out, re-opening parameter space.

---

## Key Arguments and Derivations

### Standard UED Thermal History

In the canonical scenario, reheating completes at $T_R \sim 10^9$ GeV, and the thermal bath contains all SM particles plus KK modes. Freeze-out occurs when the KK DM annihilation rate drops below the Hubble rate:

$$n_\chi \langle \sigma v \rangle \approx H(T_f)$$

At freeze-out temperature $T_f \sim m_\chi / 25$, the relic abundance is:

$$\Omega_\chi h^2 \approx \frac{3 \times 10^{-27} \, \text{cm}^3 \text{s}^{-1}}{\langle \sigma v \rangle (T_f)}$$

For UED KK DM with $m_\chi \sim 1$ TeV, the annihilation cross-section into SM pairs is:

$$\langle \sigma v \rangle \sim \frac{\alpha^2}{m_\chi^2} \times \frac{1}{(M_{\text{KK}}^2/m_\chi^2)^2}$$

This yields $\Omega_\chi h^2 \sim 0.15$ — too large by a factor of 2-3 compared to CMB measurements ($0.12 \pm 0.001$). Collider bounds simultaneously push $m_\chi > 1.2$ TeV, exacerbating the over-abundance.

### Non-Standard Reheating: Entropy Dilution

The key innovation is to allow a long period of inflaton decay characterized by a low reheating temperature $T_R \ll 10^9$ GeV. During this phase:

$$\rho_\text{radiation} \ll \rho_\text{inflaton}$$

and the scale factor grows exponentially:

$$a(t) \propto e^{H_\text{inf} t}$$

where $H_\text{inf}$ is the Hubble parameter during inflation. After freeze-out (which occurs above $T_R$), if the reheating completes at $T_R$, the entropy density jumps:

$$s = \frac{2\pi^2}{45} g_* T_R^3 \quad (\text{final})$$

versus what it would have been in standard reheating:

$$s = \frac{2\pi^2}{45} g_* T_R^{\text{std}3}$$

The dilution factor is:

$$\mathcal{D} = \frac{T_R^{\text{std}}}{T_R} = \frac{10^9 \, \text{GeV}}{10 \, \text{MeV}} \sim 10^{17}$$

However, dark matter particles are decoupled by $T_R$, so their comoving number density is fixed. The result is:

$$\Omega_\chi h^2_{\text{new}} = \mathcal{D}^{-1} \times \Omega_\chi h^2_{\text{standard}}$$

With $\mathcal{D} \sim 10$ to $100$ (more realistic low-R scenarios), the relic abundance drops to the observed value.

### Viable Parameter Space

The new window opens when $T_R$ is chosen such that:

$$10 \, \text{MeV} < T_R < 100 \, \text{MeV}$$

This permits:
- **KK mass**: $m_\chi = 500 - 1500$ GeV (below LHC exclusion limits in standard scenarios)
- **Freeze-out**: Still occurs above $T_R$ (KK is relativistic at $T_R \sim 10$ MeV)
- **Relic abundance**: Naturally matches CMB via entropy dilution

### Direct Detection Constraints

Nuclear recoil cross-sections for KK-nucleon scattering via $Z^{(1)}$ exchange:

$$\sigma_{\text{SI}} = \frac{\mu^2}{16\pi} \frac{g_Z^4}{m_{Z^{(1)}}^4} F(q^2)$$

where $\mu$ is the reduced mass and $F(q^2)$ is the nuclear form factor. For $m_\chi \sim 1$ TeV and $m_{Z^{(1)}} \sim 2-3$ TeV:

$$\sigma_{\text{SI}} \sim 10^{-47} - 10^{-46} \, \text{cm}^2$$

This is at the edge of current XENON1T sensitivity but can be probed by future generation experiments (LUX-ZEPLIN, DARWIN).

### BBN Consistency

Big Bang Nucleosynthesis constrains the effective number of light degrees of freedom at $T \sim 1$ MeV:

$$N_{\text{eff}} = 3.046 + \Delta N_\nu^{\text{BSM}}$$

In the low-reheating scenario, **KK modes are already heavy and decoupled** by the time of BBN (at $T \sim 1$ MeV). The only BSM contribution is from neutrinos and any light scalar fields. The paper shows that DESI BAO and BBN constraints together allow:

$$N_{\text{eff}} < 3.5 \quad (95\% \, \text{CL})$$

consistent with the framework if KK modes decouple at $T_R \sim 10$ MeV.

### Collider Viability

LHC searches for KK resonances set lower bounds:

$$m_{W^{(1)}} > 3 \, \text{TeV}$$
$$m_{Z^{(1)}} > 2.5 \, \text{TeV}$$

In the low-reheating scenario, the KK scale can be pushed to $\sim 3-5$ TeV (instead of the standard $\sim 1-2$ TeV), precisely at the edge of LHC Run 3 sensitivity but not yet excluded. This contrasts sharply with standard reheating, which would require $m_{KK} > 5$ TeV to satisfy thermal relic constraints — beyond current reach.

---

## Key Results

1. **Entropy dilution by low reheating resurrects KK DM**: A reheating temperature of $T_R \sim 1-100$ MeV (vs. standard $10^9$ GeV) can dilute the relic abundance by factors of $10^1$ to $10^2$, matching observations.

2. **Viable mass window**: $m_{\chi}^{KK} \sim 500-1500$ GeV, previously excluded, becomes allowed. The KK scale $m_{KK} \sim 2-5$ TeV remains within LHC reach.

3. **Direct detection**: Spin-independent scattering cross-sections in the range $10^{-47}-10^{-46}$ cm$^2$ are predicted, testable by next-generation experiments.

4. **BBN consistency**: Low-reheating cosmologies with KK DM remain consistent with CMB ($N_{\text{eff}} < 3.5$) provided KK modes decouple before BBN.

5. **Mechanism is generic**: The entropy-dilution principle works for any relic that freezes out above $T_R$ — applicable to UED, warped extra dimensions, and other BSM scenarios.

6. **Collider-cosmology synergy**: LHC Run 3 and future direct-detection experiments can close remaining viable space or confirm the low-reheating KK-DM scenario.

---

## Impact and Legacy

This work demonstrates that theoretical constraints (viability of KK DM) are not immutable but depend critically on cosmological assumptions. The revival of KK DM through low-reheating scenarios has several implications:

- **Model space revisited**: Minimal UED, once thought excluded, can be resurrected with simple modifications to the thermal history.
- **Collider program**: Focuses searches in the $2-5$ TeV range rather than exclusively above $5$ TeV, reducing the required luminosity for discovery.
- **Astroparticle physics**: Encourages searches for KK modes via cosmic ray signatures (indirect detection).
- **Early universe**: Provides concrete constraints on inflation models — only inflaton decay with low $T_R$ is consistent with KK DM.

The paper exemplifies how obscure model parameters (reheating temperature) can dramatically alter the phenomenology of fundamental BSM theories.

---

## Framework Relevance

The phonon-exflation framework operates at a fundamentally different cosmological regime: the internal compactification drives expansion directly through spectral dynamics, not through scalar field potential energy. The comparison to low-reheating KK DM is instructive:

**Similarities**: Both scenarios require non-standard early-universe physics. Both dilute the KK-scale particle abundance via geometric or entropic effects.

**Differences**:
- KK-portal-DM still treats dark matter as a separate external relic (a particle in extra dimensions). Phonon-exflation derives DM from internal Dirac-sea structure.
- Low reheating requires a *tuned* inflaton decay rate. Phonon-exflation requires only that the SU(3) fiber emerges (automatic via instanton dynamics, Session 38).
- KK DM freezes out above $T_R$ and is then "frozen in." Phonon-exflation's DM density evolves continuously with the fiber topology (no freeze-out asymmetry).

**Connection to framework**: The demonstration that low-$T_R$ reheating is cosmologically consistent validates the operating regime. Phonon-exflation proposes an even lower effective reheating: the transition from $\tau=0$ (unified) to $\tau > 0$ (unfolded SU(3)) occurs at Planck scales, with no subsequent entropy production. BBN and structure formation see only the final-state low-energy physics.

---

