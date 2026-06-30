# The pervasiveness of shape coexistence in nuclear pair condensates

**Author(s):** Y. Lei, J. Qi, Y. Lu, H. Jiang, Z.Z. Qin, D. Liu, C.W. Johnson
**Year:** 2024
**Journal:** [INCOMPLETE - not extractable from PDF]
**arXiv:** 2402.11276
**Relevance:** MEDIUM

---

## Abstract

We investigate nuclear shape coexistence for a wide range of even-even nuclides. By varying general pair condensates, which include Slater determinants as a limit but also allow for arbitrary pairing channels, we frequently find multiple coexisting minima, and often more than two. This is consistent with recent experimental results. In order to measure general pairwise correlations beyond a simple Slater determinant, we introduce a novel entropy-like measure, which is smallest mid-shell and largest near shell closures; this is consistent with a picture of pairing-like behavior dominating near closed shells and deformation mid-shell. After surveying nuclides spanning from the sd shell to nuclides between magic numbers 50 and 82, we focus on the six lightest nuclei with shape coexistence. Angular-momentum projected variational pair condensate (PVPC) calculations identify band structures, including two newly proposed coexisting bands in 26Si/Mg and 24Si/Ne.

---

## Key Arguments and Derivations

### Variational Pair Condensate (VPC) framework

The VPC ansatz is a general pair condensate: (Omega^dag)^N |0>, where Omega^dag = (1/2) sum_{ij} omega_{ij} a^dag_i a^dag_j. The structure coefficients omega_{ij} are optimized variationally to minimize the energy. This is more general than particle-number-projected HFB (which requires time-reversal invariance of the pair), and includes pure Slater determinants (Hartree-Fock) as a limit.

### One-body entropy measure

To quantify pairing correlations beyond independent particles, the authors introduce:

S_{1b} = S_pi + S_nu, where S_sigma = -sum_i lambda^sigma_i ln(lambda^sigma_i) / [N_sigma ln(M_sigma/N_sigma)]

Here lambda^sigma_i are eigenvalues of the one-body density matrix. For a Slater determinant, eigenvalues are 0 or 1 and S_{1b} = 0. Maximum S_{1b} = 2 corresponds to seniority-zero.

### Pervasiveness of coexistence

Across sd, pf, 20-50/50-82, and 50-82 valence spaces, the majority of nuclei exhibit two or more VPC minima. Key findings:
- VPC yields more minima than TRVPC or HF (more pairing channels = more coexisting shapes)
- "Super-coexistence" (4-5 minima) occurs in several Zr, Mo, Ru, Te, Ba, Ce, Sm, Dy isotopes
- Entropy is largest near shell closures (pairing dominates) and smallest mid-shell (deformation dominates)
- The lowest minimum typically has the largest entropy (strongest pairing)

### PVPC band structures for light nuclei

Detailed angular-momentum projected calculations for 28Si, 26Si/Mg, 24Si/Ne, and 24Mg identify coexisting band structures with B(E2) values in reasonable agreement with experiment. New coexisting bands are proposed for 26Si/Mg (triaxial-prolate) and 24Si/Ne (triaxial-oblate with shape mixing).

---

## Key Results

1. Shape coexistence is pervasive: most nuclei in the surveyed mass range have 2+ VPC minima
2. Including all pairing channels (VPC) reveals more coexisting shapes than time-reversal-constrained pairing (TRVPC) or no pairing (HF)
3. One-body entropy S_{1b} is largest near shell closures and smallest mid-shell
4. The lowest VPC minimum has the strongest pairing correlation
5. 28Si exhibits prolate-oblate coexistence with energy difference ~7 MeV
6. 24Mg has near-prolate (gamma ~ 10 deg) and oblate coexistence with oblate band possibly terminating at 6+
7. New coexistence proposals for 26Si/Mg and 24Si/Ne

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| VPC ansatz | $(\Omega^\dagger)^N |0\rangle$, $\Omega^\dagger = \frac{1}{2}\sum_{ij}\omega_{ij}a^\dagger_i a^\dagger_j$ | Eq. (1)-(2) |
| Variational condition | $\delta \frac{\langle (\Omega)^N | \hat{H} | (\Omega^\dagger)^N \rangle}{\langle (\Omega)^N | (\Omega^\dagger)^N \rangle} = 0$ | Eq. (3) |
| Projected HFB | $\hat{P}_N |HFB\rangle = \frac{1}{N!}(\sum_k \frac{u_k}{v_k} c^\dagger_k c^\dagger_{\bar{k}})^N |0\rangle$ | Eq. (4) |
| Time-reversal constraint | $\omega_{j_im_i,j_jm_j} = (-1)^{j_i-m_i+j_j-m_j}\omega_{j_i-m_i,j_j-m_j}$ | Eq. (6) |
| One-body entropy | $S_{1b} = -\sum_i \frac{\lambda_i^\sigma \ln \lambda_i^\sigma}{N_\sigma \ln(M_\sigma/N_\sigma)}$ | Eq. (9) |
| Pairing energy gain | $\Delta E_{\text{pair}} = \langle \hat{H} \rangle_{\text{approx.HF}} - \langle \hat{H} \rangle_{\text{VPC}}$ | Eq. (11) |
| Shape difference | $\Delta\text{Shape} = [(\beta_1\cos\gamma_1-\beta_2\cos\gamma_2)^2 + (\beta_1\sin\gamma_1-\beta_2\sin\gamma_2)^2]^{1/2}$ | Eq. (12) |

## Relevance to Phonon-Exflation

Shape coexistence in nuclear pair condensates directly parallels the framework's tau-dependent potential landscape on SU(3): multiple local minima in the (beta, gamma) deformation space correspond to the framework's multiple competing ground states at different tau values. The finding that all pairing channels are needed to reveal coexistence supports the framework's requirement for the full K_7 BCS channel (not just singlet pairing) to capture the physics. The one-body entropy measure could be adapted to quantify the deviation of the framework's GGE relic state from a simple product state.
