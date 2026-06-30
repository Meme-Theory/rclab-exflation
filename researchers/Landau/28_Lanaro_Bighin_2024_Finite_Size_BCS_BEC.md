# Finite-size effects in the two-dimensional BCS-BEC crossover

**Author(s):** M. Lanaro, G. Bighin, L. Dell'Anna, L. Salasnich
**Year:** 2024
**Journal:** [INCOMPLETE - not extractable from PDF]
**arXiv:** 2401.06054
**Relevance:** MEDIUM

---

## Abstract

We study the finite-size effects on the BCS-BEC crossover in two dimensions, occurring in confined fermionic superfluids. We analyze several thermodynamic properties, such as the chemical potential, the energy gap and the superfluid density, taking into account unavoidable quantum fluctuations, and, by means of renormalization group procedure, we detect the putative Berezinskii-Kosterlitz-Thouless phase transition at finite-size.

---

## Key Arguments and Derivations

### Theoretical Framework

The binding energy $\epsilon_B$ of Cooper pairs parameterizes the BCS-BEC crossover in 2D. In contrast to 3D, in 2D Cooper pairs always form a bound state. The ratio $\mu/\Delta$ ranges from $-\infty$ (BEC, $\epsilon_B \to +\infty$) to $+\infty$ (BCS, $\epsilon_B \to 0$). The crossover regime is approximately $\mu/\Delta \in (-1, 1)$.

Finite-size effects are introduced through an infrared cutoff $k_{\min}$ in momentum space, corresponding to a maximum wavelength $L = 2\pi/k_{\min}$ (the system size). The key parameter is $L\sqrt{n}$, the ratio of system size to inter-particle distance.

### Mean-Field with Finite-Size

The regularized gap equation with infrared cutoff gives:
$$\epsilon_B = \sqrt{(\epsilon_{\min} - \mu)^2 + \Delta^2} - (\epsilon_{\min} + \mu)$$

where $\epsilon_{\min} = \hbar^2 k_{\min}^2/(2m)$. The chemical potential $\mu/\epsilon_F = 1 - \epsilon_B/(2\epsilon_F)$ is size-independent at mean-field level, while the gap $\Delta = \sqrt{(2\epsilon_B + 4\epsilon_{\min})\epsilon_F}$ is enhanced by finite-size effects.

### Beyond Mean-Field: Gaussian Fluctuations

Gaussian quantum fluctuations are included through the grand potential $\Omega_{GF} = \frac{1}{2\beta}\sum_{q,m}\ln(\det M(q, i\Omega_m))$, where $M(q, i\Omega_m)$ is the inverse pair fluctuation propagator (a $2\times 2$ matrix). The chemical potential beyond mean-field is obtained by maximizing the energy density $E(\mu) = \Omega(\mu) + \mu n$ at given density.

The superfluid density includes both single-particle and collective contributions:
$$n_s = n - n_{sp} - n_{col}$$

where $n_{col}$ comes from bosonic collective modes with dispersion $E_{col}(k) \approx \hbar c_s k$.

### BKT Transition at Finite Size

The BKT transition is characterized by the universal jump in superfluid density, which is smoothed out at finite size. The Kosterlitz RG equations govern the flow:
$$\frac{d}{dl}K_l^{-1}(T) = 4\pi^3 y_l^2(T), \quad \frac{d}{dl}y_l(T) = [2 - \pi K_l(T)]y_l(T)$$

where $K = J/(k_B T)$ involves the phase stiffness $J = \hbar^2 n_s/(4m)$, and $y = \exp(-\mu_c/(k_B T))$ relates to the vortex core energy. The maximum RG flow parameter is $l_{\max} = \ln(L\sqrt{n})$.

Two criteria are proposed for identifying $T_{BKT}$ at finite size: (1) the temperature-axis intercept of the tangent at the inflection point of $n_s(T)$, and (2) the temperature coordinate of the inflection point itself.

### Main Findings

At finite size ($L\sqrt{n} = 5, 10, 100$):
- The gap $\Delta$ is enhanced (shifted to larger values in the BCS regime)
- The superfluid density is promoted (finite-size suppresses both $n_{sp}$ and $n_{col}$)
- The universal jump in $n_s$ at $T_{BKT}$ is replaced by a smooth crossover
- $T_{BKT}/T_F$ is systematically enhanced at smaller system sizes

## Key Results

1. The energy gap $\Delta$ is enhanced by finite-size effects due to the infrared cutoff, while the mean-field chemical potential is size-independent.
2. Gaussian fluctuations are crucial in 2D and modify both $\mu$ and the superfluid density significantly.
3. The BKT universal jump in superfluid density disappears at finite size, replaced by a smooth crossover.
4. $T_{BKT}/T_F$ is enhanced for smaller systems, with the effect being most pronounced in the BEC regime.
5. Collective excitations further suppress the superfluid density, but this suppression is less effective for finite-size systems.
6. The finite-size parameter $L\sqrt{n}$ provides a dimensionless measure of confinement effects.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Binding energy relation | $\epsilon_B/\epsilon_F = 2\sqrt{1+(\mu/\Delta)^2} - (\mu/\Delta)\sqrt{1+(\mu/\Delta)^2} + \mu/\Delta$ | Eq. (1) |
| Gap with cutoff | $\Delta = \sqrt{\epsilon_B^2 + 2(\epsilon_{\min} + \mu)\epsilon_B}$ | Eq. (2) |
| Superfluid density | $n_s = n - n_{sp} - n_{col}$ | Eq. (4) |
| Collective mode dispersion | $E_{col}(k) \approx \hbar c_s k$ | Eq. (6) |
| KT RG equations | $dK_l^{-1}/dl = 4\pi^3 y_l^2$; $dy_l/dl = (2 - \pi K_l)y_l$ | Eq. (10) |
| Phase stiffness | $J = \hbar^2 n_s/(4m)$ | Eq. (12) |
| Max RG parameter | $l_{\max} = \ln(L\sqrt{n})$ | Eq. (16) |
| MF gap (finite-size) | $\Delta/\epsilon_F = \sqrt{2\epsilon_B/\epsilon_F + 4\epsilon_{\min}/\epsilon_F}$ | Eq. (31) |
| MF chemical potential | $\mu/\epsilon_F = 1 - \epsilon_B/(2\epsilon_F)$ | Eq. (30) |
| Gaussian grand potential | $\Omega_{GF} = \frac{1}{2\beta}\sum_{q,m}\ln(\det M(q,i\Omega_m))$ | Eq. (3)/(36) |

## Relevance to Phonon-Exflation

The finite-size effects analyzed here are directly relevant to the phonon-exflation framework, where the compactified SU(3) fiber has a finite volume $L^6$ that evolves during the fold transit. The finding that finite-size enhances the pairing gap and promotes superfluidity supports the framework's mechanism where BCS instability on a compact manifold is strengthened (not weakened) by the fiber's finite extent. The smoothing of the BKT transition at finite size is also relevant to understanding how the 4D observer perceives the transit-induced phase transition on the internal space, where the effective system size $L\sqrt{n}$ maps onto the fiber volume parameter $\tau$.
