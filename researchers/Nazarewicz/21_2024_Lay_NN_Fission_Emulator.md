# Neural Network Emulation of Spontaneous Fission

**Author(s):** Daniel Lay, Eric Flynn, Samuel A. Giuliani, Witold Nazarewicz, Leo Neufcourt
**Year:** 2024
**Journal:** Physical Review C (submitted)
**arXiv:** 2310.01608
**Relevance:** MEDIUM

---

## Abstract

Background: Large-scale computations of fission properties are an important ingredient for nuclear reaction network calculations simulating rapid neutron-capture process (the r-process) nucleosynthesis. Due to the large number of fissioning nuclei potentially contributing to the r-process, a microscopic description of fission based on nuclear density functional theory (DFT) is computationally challenging. Purpose: We explore the use of neural networks (NNs) to construct DFT emulators capable of predicting potential energy surfaces and collective inertia tensors across the whole nuclear chart, starting from a minimal set of DFT calculations. Methods: We use constrained Hartree-Fock-Bogoliubov (HFB) calculations to predict the potential energy and collective inertia tensor in the axial quadrupole and octupole collective coordinates, for a set of nuclei in the r-process region. We then employ NNs to emulate the HFB energy and collective inertia tensor across the considered region of the nuclear chart. Least-action pathways characterizing spontaneous fission half-lives and fragment yields are then obtained by means of the nudged elastic band method. Results: The potential energy predicted by NNs agrees with the DFT value to within a root-mean-square error of 500 keV, and the collective inertia components agree to within an order of magnitude. These results are largely independent of the NN architecture. The exit points on the outer turning line are found to be well emulated. For the spontaneous fission half-lives the NN emulation provides values that are found to agree with the DFT predictions within a factor of 10^3 across more than 70 orders of magnitude. Conclusions: Neural networks are able to emulate the potential energy and collective inertia well enough to reasonably predict physical observables.

---

## Key Arguments and Derivations

### Section II: Spontaneous Fission within Nuclear DFT

Spontaneous fission (SF) is modeled adiabatically using collective variables describing nuclear shape. The SF half-life is computed as $t_{1/2} = \ln 2 / n P_{\mathrm{fis}}$, where $n$ is the assault frequency and $P_{\mathrm{fis}}$ is the WKB tunneling probability through the fission barrier. The collective action integral along the least-action path (LAP) determines tunneling probability. Nuclear configurations are obtained via constrained HFB using the Gogny D1S interaction, with axial quadrupole ($Q_{20}$) and octupole ($Q_{30}$) as collective coordinates. The collective inertia tensor is computed within the ATDHFB non-perturbative scheme.

### Section III: Neural Networks

Feedforward NNs take input $(A, Z, Q_{20}, Q_{30})$ and output either $V$ or components of $M_{\mu\nu}$. Separate NNs are trained for the PES and each inertia component. The inertia tensor is decomposed via eigenvalue decomposition $M = U \Sigma U^T$, and the NN is trained on the log of eigenvalues plus the Euler angle $\theta$, which avoids problems from the many-orders-of-magnitude variation. 194 nuclei were computed on a $(Q_{20}, Q_{30})$ grid, split into training (~70%), combining, and validation sets. Committee averaging across multiple NNs reduces prediction error.

### Section IV: Neural Network Quality

PES RMSE is $\sim 500$ keV for most nuclei, with some outliers at $\sim 1.5$ MeV on the chart boundary. Performance is stable across architectures (2-7 hidden layers). Input normalization to $[0,1]$ improves convergence. Diagonal inertia components ($M_{22}$, $M_{33}$) align well along the diagonal in reference-vs-NN plots; the off-diagonal component $|M_{23}|$ is poorly learned below $\sim 10^{-4}$ MeV$^{-1}$b$^{-5/2}$ due to the $\sim 10$ orders of magnitude variation.

### Section V: Impact on Observable Quantities

Exit points (proxy for fragment yields) are reproduced within $(\Delta Q_{20}, \Delta Q_{30}) = (2\,\mathrm{b}, 1\,\mathrm{b}^{3/2})$ for most nuclei. SF half-lives agree within 3 orders of magnitude across $\sim 80$ orders of magnitude span. Disagreement increases for long-lived nuclei with wide barriers (cumulative inertia error). In the r-process relevant range ($10^{-5}$--$10^{10}$ s), agreement is tight.

## Key Results

1. NN emulates PES to RMSE ~500 keV, largely architecture-independent
2. Collective inertia diagonal components reproduced within ~1 order of magnitude; off-diagonal $M_{23}$ poorly reproduced at small values
3. Exit points (fragment yield proxy) well-reproduced, dominant fission mode correctly identified for most nuclei
4. SF half-lives reproduced within factor $10^3$ over 70+ orders of magnitude
5. Largest discrepancies arise from cumulative inertia emulation error along wide fission barriers
6. PES emulation is sufficient even for nuclei with large RMSE (errors concentrate at deformations away from fission path)
7. Input normalization provides general improvement; NN depth has minimal impact on validation performance
8. Future directions: active learning, additional collective coordinates (dynamic pairing, triaxiality)

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| WKB tunneling probability | $P_{\mathrm{fis}} = \frac{1}{1 + \exp(2S(L))}$ | Eq. (1) |
| Collective action | $S(L[s]) = \frac{1}{\hbar} \int_{s_{\mathrm{in}}}^{s_{\mathrm{out}}} \sqrt{2 M_{\mathrm{eff}}(s)(V(s) - E_0)}\, ds$ | Eq. (2) |
| HFB Routhian | $\hat{H}' = \hat{H}_{\mathrm{HFB}} - \sum_\tau \lambda_\tau \hat{N}_\tau - \sum_\mu \lambda_\mu \hat{Q}_{\mu 0}$ | Eq. (3) |
| Quadrupole moment operator | $\hat{Q}_{20} = \hat{z}^2 - \frac{1}{2}(\hat{x}^2 + \hat{y}^2)$ | Eq. (4a) |
| ATDHFB inertia tensor | $M_{\mu\nu} = \frac{\hbar^2}{2\dot{q}_\mu \dot{q}_\nu} \sum_{\alpha\beta} \frac{F^{\mu*}_{\alpha\beta} F^\nu_{\alpha\beta} + F^\mu_{\alpha\beta} F^{\nu*}_{\alpha\beta}}{E_\alpha + E_\beta}$ | Eq. (5) |
| Driving term | $F^\mu / \dot{q}_\mu = A^\dagger \frac{\partial\rho}{\partial q_\mu} B^* + A^\dagger \frac{\partial\kappa}{\partial q_\mu} A^* - B^\dagger \frac{\partial\rho^*}{\partial q_\mu} A^* - B^\dagger \frac{\partial\kappa^*}{\partial q_\mu} B^*$ | Eq. (6) |
| Effective inertia | $M_{\mathrm{eff}} = \sum_{\mu\nu} M_{\mu\nu} \frac{dq_\mu}{ds} \frac{dq_\nu}{ds}$ | Eq. (7) |
| Eigenvalue decomposition | $M = U \Sigma U^T$ | Eq. (8) |
| PES RMSE | $\Delta V(A,Z)^2 = \frac{1}{n} \sum_{Q_{20},Q_{30}} [V_{\mathrm{DFT}} - V_{\mathrm{NN}}]^2$ | Eq. (9) |

## Relevance to Phonon-Exflation

The NN emulation methodology for collective inertia tensors across parameter space is directly relevant to the framework's need to evaluate ATDHFB-like collective masses across the SU(3) fiber moduli space. The paper's ATDHFB inertia tensor (Eq. 5) is the nuclear analog of the collective inertia $M_{\mathrm{ATDHFB}} = 1.695$ computed in S40 for the phonon-exflation transit. The finding that inertia emulation error accumulates along wide barriers parallels the sensitivity analysis needed for the tau-transit action integral. The eigenvalue-decomposition trick for training on multi-scale tensor components could be applied to emulate the BCS gap function or spectral action across the fold.
