# What Physics Does The Charged Lepton Mass Relation Tell Us?

**Author(s):** Yoshio Koide
**Year:** 2018 (v3: 2019)
**Journal:** Talk presented at "7th Workshop on Flavour Symmetries and Consequences in Accelerators and Cosmology" (FLASY 2018)
**arXiv:** 1809.00425
**Relevance:** HIGH

---

## Abstract

The story begins from a charged lepton mass relation K = (m_e + m_mu + m_tau) / (sqrt(m_e) + sqrt(m_mu) + sqrt(m_tau))^2 = 2/3. The formula predicted a tau lepton mass m_tau^pred = 1776.97 MeV in 1982, when the observed value was 1784.2 +/- 3.2 MeV. Ten years later (1992), an accurate value m_tau^new = 1776.99 MeV was reported, excellently coincident with the prediction. The talk reviews the field-theoretical derivation and the Sumino mechanism that explains why the relation is satisfied by pole masses rather than running masses.

---

## Key Arguments and Derivations

### 1. The Mass Relation and Its Prediction (Section 0)

The Koide formula K = 2/3 predicted m_tau = 1776.97 MeV in 1982. The observed value at the time was 1784.2 +/- 3.2 MeV (disagreement). By 1992, the experimental value was updated to 1776.99 MeV — in stunning agreement with the prediction. The formula was NOT fitted to data; it genuinely predicted the tau mass.

Current experimental confirmation: K(m_obs) = (2/3) x (0.999989 +/- 0.000014).

### 2. The Running Mass Problem (Section 1)

In a field-theoretical model, the "mass" in K = 2/3 should be the running mass, not the pole mass. Using running masses at mu = m_Z: K(m_run) = (2/3) x (1.00189 +/- 0.00002) — agreement is much worse (~0.2% deviation). This is a serious theoretical problem.

### 3. Derivation from U(3) Family Symmetry (Section 2)

A scalar Phi (nonet of U(3) family symmetry) has VEV <Phi> = v_0 diag(z_1, z_2, z_3) with z_1^2 + z_2^2 + z_3^2 = 1. The charged lepton mass matrix is quadratic: M_e = k_e <Phi><Phi>.

The scalar potential V = mu^2[PhiPhi] + lambda[PhiPhiPhiPhi] + lambda'[Phi_8 Phi_8][Phi]^2 leads to:

dV/dPhi = 0 gives: [PhiPhi] - (2/3)[Phi]^2 = 0, which is precisely K = 2/3.

The relation is independent of the potential parameters mu and lambda.

A second formula is also derived: kappa = det(Phi)/[Phi]^3 = sqrt(m_e m_mu m_tau)/(sqrt(m_e)+sqrt(m_mu)+sqrt(m_tau))^3 = 1/486.

### 4. Sumino Mechanism (Section 3)

Sumino (2009) proposed U(3) family gauge bosons (FGBs) A^j_i with masses (M_ij)^2 proportional to (m_i + m_j). The logarithmic QED correction term log(m_i/mu)^2 in the running mass is canceled by the FGB radiative term log(M_ii/mu)^2, restoring K = 2/3 for pole masses.

### 5. Modified Sumino Model (Section 4)

To avoid anomaly problems in Sumino's original model (which assigned e_L and e_R to 3 and 3* of U(3)), Koide and Yamashita proposed a modified model with (e_L, e_R) = (3, 3) and an inverted mass hierarchy M^2_ii proportional to (m_i)^{-1}. This gives:

log M^2_ii proportional to -log m_i, providing the necessary minus sign for cancellation.

The lightest FGB is A^3_3 (tau family). With inverted family number assignment for quarks, FGB masses can be as low as a few TeV, enabling LHC phenomenology.

### 6. Recent Development (Section 5)

The K and kappa relations are re-derived in a SUSY scenario, where the non-renormalization theorem protects against radiative corrections to the scalar potential.

## Key Results

1. K = 2/3 predicted m_tau = 1776.97 MeV in 1982, confirmed to 1776.99 MeV in 1992.
2. K(pole masses) = (2/3)(0.999989 +/- 0.000014) — remarkable 10^{-5} precision.
3. K(running masses at m_Z) = (2/3)(1.00189) — 0.2% deviation, indicating the relation holds for pole masses specifically.
4. The Sumino mechanism with family gauge bosons explains why K = 2/3 holds for pole masses.
5. A second relation: kappa = det(Phi)/[Phi]^3 = 1/486.
6. Modified Sumino model predicts family gauge bosons potentially accessible at LHC.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Koide formula | $K = \frac{m_e + m_\mu + m_\tau}{(\sqrt{m_e} + \sqrt{m_\mu} + \sqrt{m_\tau})^2} = \frac{2}{3}$ | Eq. (0.1) |
| Experimental value | $K(m^{\text{obs}}) = \frac{2}{3} \times (0.999989 \pm 0.000014)$ | Eq. (0.2) |
| Predicted tau mass | $m_\tau^{\text{pred}} = 1776.97\;\text{MeV}$ | Eq. (0.3) |
| Running mass deviation | $K(m^{\text{run}}) = \frac{2}{3} \times (1.00189 \pm 0.00002)$ | Eq. (1.1) |
| Mass matrix | $M_e = k_e \langle\Phi\rangle \langle\Phi\rangle$ (quadratic in VEV) | Eq. (2.2) |
| VEV condition | $[\Phi\Phi] - \frac{2}{3}[\Phi]^2 = 0$ | Eq. (2.7) |
| Second formula | $\kappa = \frac{\det\Phi}{[\Phi]^3} = \frac{\sqrt{m_e m_\mu m_\tau}}{(\sqrt{m_e}+\sqrt{m_\mu}+\sqrt{m_\tau})^3} = \frac{1}{486}$ | Eq. (2.8) |
| FGB mass (Sumino) | $(M_{ij})^2 \propto (m_i + m_j)$ | Section 3 |
| Inverted hierarchy | $M^2_{ii} \propto (m_i)^{-1}$ | Eq. (4.1) |

## Relevance to Phonon-Exflation

Koide's formula provides the gold standard for charged lepton mass relations. The 10^{-5} precision agreement with pole masses, combined with the field-theoretical derivation from a U(3) family nonet potential, establishes a benchmark that any spectral mass prediction must address. The fact that K = 2/3 holds for pole masses (not running masses) and requires the Sumino mechanism to explain this is a subtle point: the framework's spectral action predictions are presumably at the compactification scale and must be RG-evolved to compare with pole masses. The quadratic mass matrix M_e proportional to <Phi><Phi> has a structural parallel to the framework's Dirac operator squared giving eigenvalue-squared mass matrices. The second formula kappa = 1/486 provides an additional constraint that the framework should attempt to reproduce.
