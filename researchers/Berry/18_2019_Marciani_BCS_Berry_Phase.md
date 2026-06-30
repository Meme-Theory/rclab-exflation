# Dynamic properties of superconductors: Anderson-Bogoliubov mode and Berry phase in BCS and BEC regimes

**Author(s):** Dmitry Mozyrsky, Andrey V. Chubukov
**Year:** 2019
**Journal:** arXiv preprint (cond-mat.supr-con)
**arXiv:** 1902.04588
**Relevance:** CRITICAL

---

## Abstract

We analyze the evolution of the dynamics of a neutral s-wave superconductor between BCS and BEC regimes. We consider 2d case, when BCS-BEC crossover occurs already at weak coupling as a function of the ratio of the two scales -- the Fermi energy $E_F$ and the bound state energy for two fermions in a vacuum, $E_0$. BCS and BEC limits correspond to $E_F \gg E_0$ and $E_F \ll E_0$, respectively. The chemical potential $\mu = E_F - E_0$ changes sign between the two regimes. We use the effective action approach, derive the leading terms in the expansion of the effective action in the spatial and time derivative of the slowly varying superconducting order parameter $\Delta(\mathbf{r},\tau)$, and express the action in terms of derivative of the phase $\phi(\mathbf{r},\tau)$ of $\Delta(\mathbf{r},\tau) = \Delta e^{i\phi(\mathbf{r},\tau)}$. The action contains $(\nabla\phi)^2$ and $\dot{\phi}^2$ terms, which determine the dispersion of collective phase fluctuations, and $i\pi A\dot{\phi}$ term. For continuous $\phi(\mathbf{r},\tau)$, the latter reduces to the contribution from the boundary and does not affect the dynamics. We show that this longwavelength action does not change through BCS-BEC crossover. We apply our approach to a moving vortex, for which $\phi$ is singular at the center of the vortex core, and $i\pi A_{\mathrm{vort}}\dot{\phi}$ term affects vortex dynamics. We find that this term has two contributions. One comes from the states away from the vortex core and has $A_{\mathrm{vort},1} = n/2$, where $n$ is the fermion density. The other comes from electronic states inside the vortex core and has $A_{\mathrm{vort},2} = -n_0/2$, where $n_0$ is the fermion density at the vortex core. This last term comes from the continuous part of the electronic spectrum and has no contribution from discrete levels inside the core; it also does not change if we add impurities. The total $A_{\mathrm{vort}} = (n - n_0)/2$ determines the transversal force acting on the vortex core, $\pi A_{\mathrm{vort}}\dot{\mathbf{R}} \times \hat{z}$, where $\dot{\mathbf{R}}$ is the velocity of the vortex core and $\hat{z}$ a unit vector perpendicular to the 2d sample. The difference $(n-n_0)/2$ changes through the BEC-BCS crossover as $n_0$ nearly compensates $n$ in the BCS regime, but vanishes in the BEC regime.

---

## Key Arguments and Derivations

### Section II: General Formulation

The effective action for an s-wave superconductor is obtained via Hubbard-Stratonovich transformation of a microscopic model with local four-fermion attraction $-g$. The pairing field $\Delta(\mathbf{r},\tau)$ is introduced, and after integrating over Grassmann fields using the Gorkov-Nambu spinor $\psi = [\psi_\uparrow, \bar{\psi}_\downarrow]^T$, the effective action becomes:

$$\mathcal{S}[\Delta,\Delta^*] = \int d\mathbf{r}d\tau \frac{|\Delta(\mathbf{r},\tau)|^2}{g} - Tr\log\hat{G}^{-1}$$

where $\hat{G}^{-1} = -\partial_\tau - \hat{K}(\mathbf{r}) - \hat{\Delta}(\mathbf{r},\tau)$ involves the kinetic operator and the gap matrix.

An auxiliary parameter $\lambda$ is introduced to eliminate the logarithm, yielding a form related to the Wess-Zumino action.

### Section III: Adiabatic Expansion

The action is systematically expanded in time derivatives of the slowly varying order parameter:

$$\mathcal{S} = \mathcal{S}_0 + \mathcal{S}_1 + \mathcal{S}_2 + \mathcal{S}_{\mathrm{norm}}$$

**$\mathcal{S}_0$ (zeroth order):** Contains the condensation energy and the $(\nabla\phi)^2$ term. The gap equation yields $\mu = E_F - E_0$ and $\Delta_0 = 2\sqrt{E_F E_0}$. The condensation energy is $E_{\mathrm{cond}} = -\mathcal{S}N_0\Delta_0^2/2$, independent of $E_0/E_F$. The spatial gradient term gives:

$$\mathcal{S}_{0,b} + \mathcal{S}_{0,c} = n\int d\tau\int d\mathbf{r}\frac{(\nabla\phi)^2}{8m}$$

with prefactor equal to the full density $n$.

**$\mathcal{S}_1$ (first-order Berry phase term):** From the Bogoliubov-de Gennes eigenfunctions:

$$\mathcal{S}_1 = i\int d\tau\int d\mathbf{r}\frac{n(\tau) - n_0}{2}\dot{\phi}(\mathbf{r},\tau)$$

This is cast in Wess-Zumino form. Combined with $\mathcal{S}_{\mathrm{norm}}$ (which contributes $in_0/2\int\dot{\phi}$), the total linear term becomes:

$$\mathcal{S}_1 + \mathcal{S}_{\mathrm{norm}} = \frac{i}{2}\int d\tau\, n(\tau)\int d\mathbf{r}\,\dot{\phi}(\mathbf{r},\tau)$$

**$\mathcal{S}_2$ (second-order):** After combining with the extra contribution from longitudinal gap fluctuations $\delta\Delta$:

$$\mathcal{S}_2 + \mathcal{S}_{\mathrm{extra}} = N_0\int d\tau\int d\mathbf{r}\frac{\dot{\phi}^2}{4}$$

**Full long-wavelength action:**

$$\mathcal{S}_{\mathrm{reg}} = N_0\int d\tau\int d\mathbf{r}\left[\frac{E_F}{4m}(\nabla\phi)^2 + \frac{\dot{\phi}^2}{4}\right]$$

This gives the Anderson-Bogoliubov-Goldstone mode with velocity $v_F/\sqrt{2}$, unchanged through the BCS-BEC crossover.

### Section IV: Berry Phase for Moving Vortex

For a vortex with center $\mathbf{R}(\tau) = (X(\tau), Y(\tau))$, the phase $\phi$ is singular at the core. The Berry phase term becomes:

$$\mathcal{S}_{\mathrm{Berry}}^{\mathrm{vort}} = i\pi A_{\mathrm{vort}}\int d\tau\left(X(\tau)\dot{Y}(\tau) - Y(\tau)\dot{X}(\tau)\right)$$

**$A_{\mathrm{vort},1} = n/2$ (hydrodynamic/Magnus force):** Comes from fermions far from the vortex core. The contribution is entirely determined by large-distance behavior of Bogoliubov eigenfunctions. No contribution from $r = 0$.

**$A_{\mathrm{vort},2} = -n_0/2$ (core reaction force):** Comes from fermions at the vortex core via the $\nabla\phi$ dependence of $\mathcal{S}_{\mathrm{norm}}^0$. Uses the key identity $(\partial/\partial R_x)(\partial/\partial R_y) - (\partial/\partial R_y)(\partial/\partial R_x)]\phi = 2\pi\delta(\mathbf{r} - \mathbf{R})$, which localizes the contribution to the vortex center. This term is robust against impurities.

**Total:** $A_{\mathrm{vort}} = (n-n_0)/2$. In the BCS regime ($E_F > E_0$), $n - n_0 = 2N_0 E_0 \ll n$ (near-cancellation). In the BEC regime ($E_F < E_0$), $n_0 = 0$ and $A_{\mathrm{vort}} = n/2$ (pure Magnus force).

The vortex velocity equals the superflow velocity: $\mathbf{v}_{\mathrm{vort}} = \mathbf{v}_s$ (Galilean invariance).

---

## Key Results

1. The long-wavelength effective action for phase fluctuations is universal across the BCS-BEC crossover: $\mathcal{S}_{\mathrm{cont}} \propto \sum_{q,\Omega}|\phi_{q,\Omega}|^2(\Omega^2 - q^2 v_F^2/2)$.
2. The phase velocity of collective excitations (Anderson-Bogoliubov mode) is $v_F/\sqrt{2}$, independent of $E_0/E_F$.
3. The Berry phase prefactor for the bulk is $A = n/2$ (full fermion density), unchanged through the crossover.
4. For a moving vortex, the Berry phase has two contributions: $A_{\mathrm{vort}} = A_{\mathrm{vort},1} + A_{\mathrm{vort},2} = n/2 - n_0/2$.
5. In BCS regime: $A_{\mathrm{vort}} = N_0 E_0$ (Magnus and reaction forces nearly cancel).
6. In BEC regime: $A_{\mathrm{vort}} = n/2 = N_0 E_F$ (only Magnus force, no normal fermions at core).
7. The core contribution $A_{\mathrm{vort},2} = -n_0/2$ is impurity-independent.
8. The condensation energy $E_{\mathrm{cond}} = -\mathcal{S}N_0\Delta_0^2/2$ is independent of $E_0/E_F$.
9. The gap equation gives $\mu = E_F - E_0$ and $\Delta_0 = 2\sqrt{E_F E_0}$.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Continuous phase action | $\mathcal{S}_{\mathrm{cont}} \propto \sum_{q,\Omega}\|\phi_{q,\Omega}\|^2(\Omega^2 - q^2 v_F^2/2)$ | Eq. (1) |
| Vortex Berry action | $\mathcal{S}_{\mathrm{Berry}}^{\mathrm{vort}} = i\pi A_{\mathrm{vort}}\int dt(X\dot{Y} - Y\dot{X})$ | Eq. (2) |
| Effective action | $\mathcal{S}[\Delta,\Delta^*] = \int d\mathbf{r}d\tau\frac{\|\Delta\|^2}{g} - Tr\log\hat{G}^{-1}$ | Eq. (14) |
| Inverse Green's function | $\hat{G}^{-1} = -\partial_\tau - \hat{K}(\mathbf{r}) - \hat{\Delta}(\mathbf{r},\tau)$ | Eq. (11) |
| BdG eigenproblem | $\mathcal{H}(\mathbf{r},\tau',\lambda)\|\chi_{n,\lambda}(\mathbf{r},\tau')\rangle = E_{n,\lambda}(\tau')\|\chi_{n,\lambda}(\mathbf{r},\tau')\rangle$ | Eq. (25) |
| Berry phase (S1) | $\mathcal{S}_1 = \sum_n\int d\tau[\langle\chi_n\|\partial_\tau\chi_n\rangle - \langle\chi_n^{(0)}\|\partial_\tau\chi_n^{(0)}\rangle]\theta_n$ | Eq. (38) |
| Gap equation result | $\mu = E_F - E_0$, $\Delta_0 = 2\sqrt{E_F E_0}$ | Eq. (53) |
| Spatial gradient term | $\mathcal{S}_{0,b} + \mathcal{S}_{0,c} = n\int d\tau\int d\mathbf{r}\frac{(\nabla\phi)^2}{8m}$ | Eq. (78) |
| Linear Berry term (S1) | $\mathcal{S}_1 = i\int d\tau\int d\mathbf{r}\frac{n(\tau)-n_0}{2}\dot{\phi}$ | Eq. (81) |
| Normal state contribution | $\mathcal{S}_{\mathrm{norm}} = \mathcal{S}_0 + i\frac{n_0}{2}\int d\tau\int d\mathbf{r}\dot{\phi}$ | Eq. (88) |
| Combined Berry term | $\mathcal{S}_1 + \mathcal{S}_{\mathrm{norm}} = \mathcal{S}_0 + \frac{i}{2}\int d\tau\,n(\tau)\int d\mathbf{r}\dot{\phi}$ | Eq. (89) |
| Second-order + extra | $\mathcal{S}_2 + \mathcal{S}_{\mathrm{extra}} = N_0\int d\tau\int d\mathbf{r}\frac{\dot{\phi}^2}{4}$ | Eq. (102) |
| Full action | $\mathcal{S}_{\mathrm{reg}} = N_0\int d\tau\int d\mathbf{r}[\frac{E_F}{4m}(\nabla\phi)^2 + \frac{\dot{\phi}^2}{4}]$ | Eq. (104) |
| Berry prefactor | $A = n/2 = \frac{N_0}{2}(\sqrt{\mu^2+\Delta_0^2}+\mu)$ | Eq. (106) |
| Vortex core identity | $(\frac{\partial}{\partial R_x}\frac{\partial}{\partial R_y} - \frac{\partial}{\partial R_y}\frac{\partial}{\partial R_x})\phi = 2\pi\delta(\mathbf{r}-\mathbf{R})$ | Eq. (157) |
| Vortex Berry total | $\mathcal{S}_{\mathrm{Berry}}^{\mathrm{vort}} = i\pi A_{\mathrm{vort}}(X\dot{Y} - Y\dot{X})$, $A_{\mathrm{vort}} = (n-n_0)/2$ | Eqs. (166)-(167) |
| Force balance | $A_{\mathrm{vort}}\dot{\mathbf{R}}\times\mathbf{z} - B_{\mathrm{vort}}\mathbf{v}_s\times\mathbf{z} = 0$ | Eq. (176) |
| Galilean result | $\mathbf{v}_{\mathrm{vort}} = \mathbf{v}_s$ | Eq. (178) |

---

## Relevance to Phonon-Exflation

This paper provides a microscopic derivation of the Berry phase in BCS superconductors, directly relevant to the framework's BCS mechanism chain. The key result $A_{\mathrm{vort}} = (n-n_0)/2$ shows that the Berry phase for topological defects (vortices) in BCS systems has two distinct contributions: a bulk Magnus force ($n/2$) and a core reaction force ($-n_0/2$). In the BCS limit, these nearly cancel -- consistent with the framework's finding of a quantized but small Berry phase at the BCS transition ($S_{\mathrm{inst}} = 0.069$). The crossover from BCS ($A_{\mathrm{vort}} \approx N_0 E_0$) to BEC ($A_{\mathrm{vort}} = n/2$) maps directly onto the framework's transit physics: the instanton parameter $s$ drives a BCS-BEC-like crossover where the Berry phase changes character. The impurity robustness of $A_{\mathrm{vort},2}$ is relevant to the framework's ordered veil (GGE permanence) -- the Berry phase structure survives disorder, consistent with topological protection of the transit. The connection to Volovik's work (Ref. 32, 39, 44) on the universe-in-a-helium-droplet and vortex dynamics in superfluid $^3$He is an explicit bridge to the project's Volovik convergence.
