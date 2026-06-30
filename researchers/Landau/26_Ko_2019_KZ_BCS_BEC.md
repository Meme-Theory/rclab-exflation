# Kibble-Zurek universality in a strongly interacting Fermi superfluid

**Author(s):** Bumsuk Ko, Jee Woo Park, Y. Shin
**Year:** 2019
**Journal:** [INCOMPLETE - not extractable from PDF; submitted to Science-family journal based on format]
**arXiv:** 1902.06922
**Relevance:** HIGH

---

## Abstract

Near a continuous phase transition, systems with different microscopic origins display universal dynamics if their underlying symmetries are compatible. In a thermally quenched system, the Kibble-Zurek mechanism for the creation of topological defects unveils this universality through a characteristic power-law exponent, which captures the dependence of the defect density on the quench rate. Here, we report the observation of the Kibble-Zurek universality in a strongly interacting Fermi superfluid. As the system's microscopic description is tuned from bosonic to fermionic, the quench formation of vortices reveals a constant scaling exponent arising from the U(1) gauge symmetry of the system. For rapid quenches, destructive vortex collisions lead to the saturation of their densities, whose values can be universally scaled by the interaction-dependent area of the vortex cores.

---

## Key Arguments and Derivations

### Experimental Setup

An equal mixture of ultracold $^6$Li atoms in two hyperfine states near a broad s-wave Feshbach resonance at 832 G is prepared in a highly oblate trap. About $2.0 \times 10^6$ atoms per spin state are initially prepared at $1.15 T_c$, then evaporatively cooled by linearly reducing the optical dipole trap (ODT) depth across the superfluid transition. Quench times $t_q$ range from 0.2 s to 2.6 s across four interaction strengths spanning the BEC-BCS crossover ($-1/k_F a = -1.53$ to $0.70$).

### Kibble-Zurek Scaling

The central prediction of KZ theory is a universal power-law relationship between defect density and quench rate. For a linear temperature quench, the defect density has the form $N_v \propto t_q^{-\alpha_{KZ}}$, where $\alpha_{KZ}$ depends on the critical exponents $\nu$ and $z$ of the transition.

For a homogeneous system, $\alpha_{KZ} = (D-d)\nu/(1+\nu z)$, where $D$ is the system dimensionality and $d$ is the defect dimensionality. For an inhomogeneous (harmonically trapped) system, the modified exponent is:

$$\alpha_{KZ} = (D-d)\frac{1+2\nu}{1+\nu z}$$

With $D-d = 2$ for vortices in 3D and mean-field values ($\nu = 1/2$, $z = 2$), this gives $\alpha_{KZ} = 2$ for the trapped case; with F-model (renormalization group) values ($\nu = 2/3$, $z = 3/2$), one obtains $\alpha_{KZ} = 7/3$.

### Key Observation: Constant Exponent Across Crossover

The measured KZ exponents remain constant across the entire BEC-BCS crossover at $\alpha_{KZ} = 2.24(9)$, consistent with the prediction for a harmonically trapped system with U(1) symmetry breaking. This universality arises because, despite dramatic changes in microscopic properties (pair size, critical temperature, critical velocity), the underlying U(1) gauge symmetry of the normal-to-superfluid transition is preserved throughout the crossover.

### Vortex Saturation

For rapid quenches ($t_q < t_{\text{sat}}$), vortex numbers saturate due to destructive vortex-antivortex collisions. The saturated number scales as $N_{\text{sat}} = (R_{TF}/f\xi_h)^2$, where $R_{TF}$ is the Thomas-Fermi radius, $\xi_h$ is the healing length, and $f \approx 40$ is a geometric scaling factor. This allows collapse of all data across the crossover to a single universal curve when plotting $N_v/N_{\text{sat}}$ versus $t_q/t_{\text{sat}}$.

An empirical model $N_v = N_{\text{sat}}[1 + (t_q/t_{\text{sat}})^{2\beta_{KZ}}]^{-1/2}$ fits the data well across all interaction regimes.

## Key Results

1. First observation of Kibble-Zurek universality across the BEC-BCS crossover in a single physical system.
2. Measured KZ exponent $\alpha_{KZ} = 2.24(9)$, constant across all interaction strengths, consistent with inhomogeneous KZ predictions for U(1) symmetry breaking.
3. Up to 50 spontaneously created vortices observed at unitarity, an order of magnitude more than previous atomic BEC experiments.
4. Vortex saturation at short quench times explained by destructive vortex-antivortex collisions with effective range set by the interaction-dependent healing length.
5. Universal data collapse achieved by rescaling vortex numbers by $N_{\text{sat}}$ and quench times by $t_{\text{sat}}$.
6. The saturation time $t_{\text{sat}}$ is approximately constant across the crossover ($\sim 0.5$ s).

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| KZ exponent (homogeneous) | $\alpha_{KZ} = \frac{(D-d)\nu}{1+\nu z}$ | Main text |
| KZ exponent (trapped) | $\alpha_{KZ} = (D-d)\frac{1+2\nu}{1+\nu z}$ | Eq. (1) |
| Correlation length divergence | $\xi = \xi_0 |{(T-T_c)/T_c}|^{-\nu}$ | Main text |
| Relaxation time divergence | $\tau = \tau_0 |{(T-T_c)/T_c}|^{-\nu z}$ | Main text |
| Saturation model | $N_v = N_{\text{sat}}[1 + (t_q/t_{\text{sat}})^{2\beta_{KZ}}]^{-1/2}$ | Main text |
| Saturated vortex number | $N_{\text{sat}} = (R_{TF}/f\xi_h)^2$, $f \approx 40$ | Main text |
| Healing length | $\xi_h = \hbar/(m v_c)$ | Supp. Sec. 5 |
| Superfluid velocity (vortex) | $v_s = (\hbar/m)(n/r)$ | Supp. derivation |

## Relevance to Phonon-Exflation

This paper provides direct experimental verification of Kibble-Zurek universality across the BCS-BEC crossover, which is the precise regime relevant to the phonon-exflation fold transit. The constant KZ exponent despite dramatic changes in pairing character (from tight molecules to extended Cooper pairs) confirms that topological defect production during symmetry-breaking phase transitions is governed by symmetry class alone, not microscopic details. This supports the framework's identification of transit-induced particle creation as Parker-type (cosmological) rather than Hawking-type, and validates the KZ scaling laws used to estimate defect densities during the SU(3) fold transit.
