# Analog of gravitational anomaly in topological chiral superconductors

**Author(s):** G.E. Volovik
**Year:** 2021
**Journal:** Pis'ma v ZhETF (JETP Letters)
**arXiv:** 2104.01020
**Relevance:** HIGH

---

## Abstract

It is known that the contribution of torsion to the equation for the chiral Weyl fermions can be equivalently considered in terms of the axial U(1) gauge field. In this scenario the gravitational field transforms to the U(1) gauge field. Here we show that in chiral superconductors the opposite scenario takes place: the electromagnetic U(1) field serves as the spin connection for the Bogoliubov fermionic quasiparticles. As a result the electromagnetic field gives rise to the gravitational anomaly, which contains the extra factor 1/3 in the corresponding Adler-Bell-Jackiw equation as compared with the conventional chiral anomaly. We also consider the gravitational anomaly produced in neutral Weyl superfluids by the analog of the gravitational instanton, the process of creation and annihilation of the 3D topological objects -- hopfions. The gravitational instanton leads to creation of the chiral charge.

---

## Key Arguments and Derivations

### I. Introduction
Topological materials with Weyl fermions allow study of quantum anomalies. The ABJ chiral anomaly has been experimentally probed in superfluid $^3$He-A. This paper considers the opposite direction: how the electromagnetic field in chiral superconductors acts as spin connection, producing a gravitational anomaly.

### II. From Gauge Field to Spin Connection
The Hamiltonian for Bogoliubov quasiparticles in p-wave superfluid $^3$He-A contains two Weyl points at $\mathbf{p}_\pm = \pm p_0\hat{l}$. The space-time dependence of Weyl points produces an effective electromagnetic field $\mathbf{A}_{\text{eff}}(\mathbf{r},t) = p_0\hat{l}(\mathbf{r},t)$.

For a charged superconductor, the real electromagnetic field enters through $\tau_3$ (particle-hole matrix). Since $\tau_3 = \frac{1}{2i}(\tau_1\tau_2 - \tau_2\tau_1)$, the electromagnetic vector potential becomes the spin connection:

$$C^{12}_i = -C^{21}_i = 2A_i(\mathbf{r},t), \quad C^{12}_0 = -C^{21}_0 = 2A_0(\mathbf{r},t)$$

The curvature tensor components are: $R^{12}_{\mu\nu} = 2F_{\mu\nu}$.

### III. Gravitational Anomaly from Electromagnetic Field
The gravitational anomaly equation for a single Weyl node:

$$\partial_\mu J^\mu_5 = \frac{1}{768\pi^2}e^{\mu\nu\rho\sigma}R^{ab}_{\mu\nu}R^{cd}_{\rho\sigma}\eta_{ad}\eta_{bc}$$

Substituting $R^{12}_{\mu\nu} = 2F_{\mu\nu}$:

$$\partial_\mu J^\mu_5 = \frac{1}{96\pi^2}e^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma} = \frac{1}{3}\frac{1}{32\pi^2}e^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}$$

The extra factor 1/3 compared with the conventional ABJ anomaly is the hallmark of the gravitational anomaly.

### IV. Gravitational Anomaly in Neutral Superfluid and Hopfions
In neutral superfluids, $\mathbf{A} \to m\mathbf{v}_s$. The gravitational anomaly:

$$\partial_\mu J^\mu_5 = \frac{m^2}{24\pi^2}\partial_t\mathbf{v}_s \cdot (\nabla \times \mathbf{v}_s)$$

This anomaly is produced by creation/annihilation of hopfions (3D skyrmions described by $\pi_3(S^2) = \mathbb{Z}$ topological charge). The hopfion topological charge density is expressed through helicity of superfluid velocity. The gravitational instanton (change of topological charge) creates 6 chiral fermions per hopfion -- the gravitational analog of Kuzmin-Rubakov-Shaposhnikov electroweak baryogenesis.

### V. Higher Topological Invariants
For Weyl points with topological charge $N$, the Hamiltonian represents an analog of Horava gravity. The gravitational anomaly retains the 1/3 factor:

$$\partial_\mu J^\mu_{5,\text{tot}} = \frac{N}{48\pi^2}e^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma} = \frac{1}{3}\frac{N}{16\pi^2}e^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}$$

---

## Key Results

1. In chiral superconductors, the electromagnetic U(1) field serves as spin connection for Bogoliubov quasiparticles
2. The gravitational anomaly in superconductors has an extra factor 1/3 vs. the conventional ABJ chiral anomaly
3. In neutral superfluids, the gravitational instanton creates/annihilates hopfions (3D topological objects)
4. Creation of a single hopfion is accompanied by creation of 6 chiral fermions (gravitational baryogenesis analog)
5. The 1/3 factor persists for higher-order Weyl points with topological charge $N$
6. The Hamiltonian for higher-order Weyl points represents an analog of Horava gravity

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Spin connection | $C^{12}_\mu = -C^{21}_\mu = 2A_\mu$ | Eq. (6) |
| Curvature from EM | $R^{12}_{\mu\nu} = 2F_{\mu\nu}$ | Eq. (11) |
| Gravitational anomaly | $\partial_\mu J^\mu_5 = \frac{1}{3}\frac{1}{32\pi^2}e^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}$ | Eq. (13) |
| Neutral anomaly | $\partial_\mu J^\mu_5 = \frac{m^2}{24\pi^2}\partial_t\mathbf{v}_s \cdot (\nabla \times \mathbf{v}_s)$ | Eq. (15) |
| Hopfion charge density | $n^0_H = \frac{m^2}{4\pi^2}(\mathbf{v}_s \cdot (\nabla \times \mathbf{v}_s))$ | Eq. (16) |
| Chiral/hopfion relation | $\partial_\mu J^\mu_5 = \frac{1}{6}\partial_\mu n^\mu_H$ | Eq. (19) |
| Higher-N anomaly | $\partial_\mu J^\mu_{5,\text{tot}} = \frac{N}{48\pi^2}e^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}$ | Eq. (26) |

---

## Relevance to Phonon-Exflation

1. **Gauge-gravity duality in BCS**: The electromagnetic field acting as spin connection in chiral superconductors is a concrete realization of the gauge-gravity interplay that the framework exploits in the BCS condensate on $SU(3)$.

2. **Anomaly factor 1/3**: The extra 1/3 in the gravitational anomaly may be relevant to the framework's treatment of the anomalous transport in the instanton gas during the tau-transit.

3. **Hopfion creation = baryogenesis**: The gravitational instanton creating 6 chiral fermions per hopfion provides a concrete condensed-matter model for how the framework's transit could generate matter-antimatter asymmetry.

4. **Horava gravity analog**: The connection between higher-order Weyl points and Horava gravity reinforces the framework's Lifshitz-type scaling near the fold point.
