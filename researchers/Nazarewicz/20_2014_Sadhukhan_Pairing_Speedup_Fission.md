# Pairing-Induced Speedup of Nuclear Spontaneous Fission

**Author(s):** Jhilam Sadhukhan, J. Dobaczewski, W. Nazarewicz, J.A. Sheikh, A. Baran
**Year:** 2014
**Journal:** Physical Review C 90, 061304(R)
**arXiv:** 1410.1264
**Relevance:** HIGH

---

## Abstract

Background: Collective inertia is strongly influenced at the level crossing at which quantum system changes diabatically its microscopic configuration. Pairing correlations tend to make the large-amplitude nuclear collective motion more adiabatic by reducing the effect of those configuration changes. Competition between pairing and level crossing is thus expected to have a profound impact on spontaneous fission lifetimes.

Purpose: To elucidate the role of nucleonic pairing on spontaneous fission, we study the dynamic fission trajectories of $^{264}$Fm and $^{240}$Pu using the state-of-the-art self-consistent framework.

Methods: We employ the superfluid nuclear density functional theory with the Skyrme energy density functional SkM* and a density-dependent pairing interaction. Along with shape variables, proton and neutron pairing correlations are taken as collective coordinates. The collective inertia tensor is calculated within the nonperturbative cranking approximation. The fission paths are obtained by using the least action principle in a four-dimensional collective space of shape and pairing coordinates.

Results: Pairing correlations are enhanced along the minimum-action fission path. For the symmetric fission of $^{264}$Fm, where the effect of triaxiality on the fission barrier is large, the geometry of fission pathway in the space of shape degrees of freedom is weakly impacted by pairing. This is not the case for $^{240}$Pu where pairing fluctuations restore the axial symmetry of the dynamic fission trajectory.

Conclusions: The minimum-action fission path is strongly impacted by nucleonic pairing. In some cases, the dynamical coupling between shape and pairing degrees of freedom can lead to a dramatic departure from the static picture. Consequently, in the dynamical description of nuclear fission, particle-particle correlations should be considered on the same footing as those associated with shape degrees of freedom.

---

## Key Arguments and Derivations

### Theoretical Framework

The SF half-life in semi-classical approximation:
$$T_{1/2} = \ln 2 / (nP)$$
where $n = 10^{20.38}$ s$^{-1}$ is the assault frequency and $P = 1/(1 + e^{2S})$ is the penetration probability. The fission action integral:
$$S(L) = \int_{s_\text{in}}^{s_\text{out}} \frac{1}{\hbar} \sqrt{2M_\text{eff}(s)(V(s) - E_0)} \, ds$$
is calculated along the fission path $L(s)$.

The collective coordinates are $\{X_i\} = \{Q_{20}, Q_{22}, \lambda^2_n + \lambda^2_p, \lambda^2_n - \lambda^2_p\}$, where $Q_{20}$ and $Q_{22}$ represent elongation and triaxiality, while $\lambda^2_\tau$ control dynamic pairing correlations through particle-number dispersion terms $\Delta\hat{N}^2_\tau$ in the constrained HFB Routhian:
$$\hat{H}' = \hat{H}_\text{HFB} - \sum_\mu \lambda_\mu \hat{Q}_{2\mu} - \sum_\tau (\lambda_\tau \hat{N}_\tau - \lambda^2_\tau \Delta\hat{N}^2_\tau)$$

The potential $V$ is obtained from HFB energy minus vibrational zero-point energy. The inertia tensor $M^C$ is computed from the nonperturbative cranking approximation to ATDHFB.

### Key Physical Mechanism

Since collective inertia roughly depends on pairing gap as $\Delta^{-2}$, by choosing a pathway with larger $\Delta$ the fissioning nucleus lowers the collective action. The pairing gap parameter $\lambda^2_\tau$ thus becomes a dynamical variable. The competing effects are: (a) larger pairing increases potential energy (departure from self-consistent minimum), but (b) larger pairing decreases collective inertia. The interplay between these opposing tendencies determines the least-action trajectory.

### Results for $^{264}$Fm

In the first step, isoscalar vs isovector pairing coordinates were compared. The isovector pairing coordinate $x_4 = (\lambda^2_n - \lambda^2_p)/\delta q_4$ has negligible effect on both $V$ and $|M^C|^{1/3}$, and the minimum action path maintains $x_4 \approx 0$. The isoscalar pairing coordinate $x_3 = (\lambda^2_n + \lambda^2_p)/\delta q_3$ significantly reduces inertia peaks at level crossings and decreases the overall inertia magnitude.

In the 3D space $(x_1, x_2, x_3)$ corresponding to $(Q_{20}, Q_{22}, \lambda^2_n + \lambda^2_p)$: triaxiality along the fission path is reduced at the expense of enhanced pairing. The SF half-life decreases by three orders of magnitude compared to the 2D calculation without pairing fluctuations.

Along the 3D path:
- The path is shorter than the 2D path
- Lower collective inertia is favored at the cost of higher potential energy
- Both 2D and 3D potentials deviate significantly from the static fission barrier
- Neutron and proton pairing gaps are enhanced along the dynamic path

### Results for $^{240}$Pu

The effect is even more dramatic. The static calculation predicts a triaxial first barrier (energy gain $\sim 2$ MeV from triaxiality). Including pairing dynamics in 3D calculations, axial symmetry is fully restored along the minimum-action path. Pairing fluctuations completely replace the role of triaxiality in reducing the effective barrier.

---

## Key Results

1. Pairing correlations are dynamically enhanced along the minimum-action fission path, reducing collective inertia
2. The collective inertia depends roughly as $\Delta^{-2}$ on the pairing gap; enhanced pairing dramatically reduces tunneling action
3. For $^{264}$Fm, including pairing dynamics reduces the SF half-life by $\sim 3$ orders of magnitude
4. Isovector pairing fluctuations ($\lambda^2_n - \lambda^2_p$) play a negligible role; isoscalar pairing dominates
5. For $^{240}$Pu, pairing fluctuations completely restore axial symmetry, replacing the role of triaxiality in reducing the fission barrier
6. The standard static picture based on saddle points is dramatically modified by dynamical pairing
7. The concept of "fission barrier" is highly limited — dynamic potential along the least-action path differs substantially from the static barrier
8. Both DPM and Ritz algorithms give consistent minimum-action paths

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| SF half-life | $T_{1/2} = \ln 2 / (nP)$, $P = 1/(1+e^{2S})$ | Text |
| Fission action | $S(L) = \int_{s_\text{in}}^{s_\text{out}} \frac{1}{\hbar}\sqrt{2M_\text{eff}(s)(V(s) - E_0)}\,ds$ | Eq. 1 |
| Constrained HFB Routhian | $\hat{H}' = \hat{H}_\text{HFB} - \sum_\mu \lambda_\mu \hat{Q}_{2\mu} - \sum_\tau (\lambda_\tau \hat{N}_\tau - \lambda^2_\tau \Delta\hat{N}^2_\tau)$ | Eq. 2 |
| Inertia-pairing relation | $M \sim \Delta^{-2}$ | Text, citing Refs. 5, 11-14 |
| Collective coordinates | $\{X_i\} = \{Q_{20}, Q_{22}, \lambda^2_n + \lambda^2_p, \lambda^2_n - \lambda^2_p\}$ | Text |

## Relevance to Phonon-Exflation

This paper provides direct evidence that pairing dynamics dramatically accelerates large-amplitude collective motion — the "pairing-induced speedup" mechanism. The framework's transit along the SU(3) fold is precisely this kind of large-amplitude motion where the collective inertia $M \sim \Delta^{-2}$ is controlled by the pairing gap. The finding that pairing fluctuations can restore symmetries broken in the static picture (axial symmetry for $^{240}$Pu) parallels the framework's result that the instanton gas dynamics during transit operates independently of the spectral action's static geometry. The 3-decade change in half-life from including pairing dynamics quantifies how strongly the framework's transit timescale depends on proper treatment of the BCS sector. The paper's conclusion that "particle-particle correlations should be considered on the same footing as shape degrees of freedom" is exactly what the framework implements by coupling the Richardson-Gaudin BCS dynamics to the geometric ($\tau$) evolution.
