# Moments of inertia in light deformed nuclei: pairing and mean-field impacts

**Author(s):** V.O. Nesterenko, M.A. Mardyban, P.-G. Reinhard, A. Repko, J. Kvasil
**Year:** 2023 (revised 2024)
**Journal:** [INCOMPLETE - not extractable from PDF]
**arXiv:** 2304.10873
**Relevance:** MEDIUM

---

## Abstract

The dependence of the moment of inertia J on the pairing and axial quadrupole deformation beta in 24Mg and 20Ne was investigated. The study is based on quadrupole-constrained calculations with three cranking approaches for J (Inglis-Belyaev, Thouless-Valatin, adiabatic time-dependent Hartree-Fock) and a representative set of Skyrme forces (SVbas, SkM*, SLy6). At variance with macroscopic collective models, the calculations predict the specific regime dJ/dbeta < 0 at beta >= 0.5 (24Mg) and beta >= 0.6 (20Ne), where the pairing breaks down. This regime is explained by two effects: full break up of the pairing and specific evolution of a single dominant particle-hole (1ph) configuration with beta. The analysis of experimental data for the ground-state rotational bands in 24Mg and 20Ne shows that such regime is possible at low spins.

---

## Key Arguments and Derivations

### Three cranking models

The paper compares macroscopic (rigid-body RB, hydrodynamical HD) with microscopic (Inglis-Belyaev IB, Thouless-Valatin TV, adiabatic TDHF) expressions for the moment of inertia. Macroscopic models always give dJ/dbeta > 0. The Inglis-Belyaev formula is:

J_IB = 2 sum_{q,q'>0} |<qq'|I_x|tilde{0}>|^2 / (epsilon_q + epsilon_{q'})

where |tilde{0}> is the quasiparticle vacuum and epsilon_q are quasiparticle energies.

### Pairing collapse drives regime change

At beta > 0.5 (24Mg) and > 0.6 (20Ne), the pairing collapses (Delta -> 0). This makes the energy denominator in the IB formula decisive. In the unpaired regime, the dominant 2qp configuration [211-up, 202-up] has its energy gap increasing with beta while the matrix element |<q|I_x|q'>|^2 remains approximately constant, leading to decreasing J.

### Single-configuration dominance

A single proton-neutron pair ([211-up, 202-up] in 24Mg, [220-up, 211-up] in 20Ne) dominates the moment of inertia. Just two 2qp configurations (one proton, one neutron) reproduce the main dJ/dbeta < 0 effect. This is a pure mean-field effect, enabled by pairing collapse.

### Experimental evidence

Analysis of experimental data for ground-state rotational bands shows dJ/dI * dQ_0^2/dI < 0 at I = 2-6 in 24Mg and I = 2-4 in 20Ne, consistent with the predicted dJ/dbeta < 0 regime.

---

## Key Results

1. All microscopic models (IB, TV, ATDHF) predict dJ/dbeta < 0 at large deformations in 24Mg and 20Ne, contradicting macroscopic models
2. The anomalous regime is driven by pairing collapse at beta ~ 0.4-0.5, after which mean-field shell effects dominate
3. A single 1ph configuration controls the behavior of J(beta) in the unpaired regime
4. The effect is more pronounced for Skyrme forces with small effective mass m*/m (SkM*, SLy6)
5. Experimental data at low spins are consistent with the predicted regime

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Rotational energy | $E_I = \frac{\hbar^2}{2\mathcal{J}} I(I+1)$ | Eq. (1) |
| Rigid-body | $\mathcal{J}_{\text{RB}} = \frac{2}{5}MR^2(1 + \frac{1}{2}\sqrt{\frac{5}{4\pi}}\beta + \frac{25}{32\pi}\beta^2)$ | Eq. (2) |
| Hydrodynamical | $\mathcal{J}_{\text{HD}} \approx \mathcal{J}_{\text{RB}} \frac{45}{16\pi}\beta^2$ for $\beta < 0.4$ | Eq. (4) |
| Inglis cranking | $\mathcal{J}_{\text{Ing}} = 2\sum_i \frac{|\langle i|I_x|0\rangle|^2}{E_i}$ | Eq. (5) |
| Inglis-Belyaev | $\mathcal{J}_{\text{IB}} = 2\sum_{q,q'>0} \frac{|\langle qq'|I_x|\tilde{0}\rangle|^2}{\epsilon_q + \epsilon_{q'}}$ | Eq. (6) |
| Thouless-Valatin | $\mathcal{J}_{\text{TV}} = 2\sum_\nu \frac{|\langle \nu|I_x|\tilde{\tilde{0}}\rangle|^2}{E_\nu}$ | Eq. (7) |
| ATDHF | $[\Theta_x(\beta), H(\beta)] = -i\hbar I_x(\beta)$ | Eq. (8) |
| Individual contribution | $\mathcal{J}_{qq'} = 2\frac{|f_{qq'}u_{qq'}|^2}{\epsilon_{qq'}}$ | Eq. (10) |

## Relevance to Phonon-Exflation

The pairing collapse mechanism at large deformation is directly relevant to the framework's tau-transit: as tau evolves from 0 to the fold, the effective deformation of the SU(3) fiber changes, and at certain tau values the K_7 BCS gap may collapse, analogous to the pairing breakdown at beta > 0.5 in 24Mg. The single-configuration dominance finding supports the framework's observation that a small number of spectral modes control the dynamics (Session 38: single dominant 2qp configuration [211-up, 202-up] parallels the B2 sector dominance).
