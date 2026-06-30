# Hartree-Fock-Bogoliubov Solution of the Pairing Hamiltonian in Finite Nuclei

**Author(s):** J. Dobaczewski and W. Nazarewicz
**Year:** 2013 (published in "Fifty Years of Nuclear BCS", World Scientific)
**Journal:** Chapter in "Fifty Years of Nuclear BCS" (World Scientific, 2012)
**arXiv:** 1206.2600
**Relevance:** CRITICAL

---

## Abstract

We present an overview of the Hartree-Fock-Bogoliubov (HFB) theory of nucleonic superfluidity for finite nuclei. After introducing basic concepts related to pairing correlations, we show how the correlated pairs are incorporated into the HFB wave function. Thereafter, we present derivation and structure of the HFB equations within the superfluid nuclear density functional formalism and discuss several aspects of the theory, including the unitarity of the Bogoliubov transformation in truncated single-particle and quasiparticle spaces, form of the pairing functional, structure of the HFB continuum, regularization and renormalization of pairing fields, and treatment of pairing in systems with odd particle numbers.

---

## Key Arguments and Derivations

### 1. Basics of Pairing Correlations (Section 2)

The paper begins with a measurement-theoretic definition of pairing. The pairing correlation between states $\mu$ and $\nu$ is the excess probability:

$$P_{\mu\nu} = v^2_{\mu\nu} - v^2_\mu v^2_\nu$$

This is the excess of finding two fermions simultaneously over finding them independently. No pairing correlations exist in a Slater determinant. The BCS ansatz provides a model N-fermion state with explicit pairing:

$$|\Phi_N\rangle = \mathcal{N}_N \left(\sum_{\mu>0} s_\mu z_\mu a^\dagger_{\tilde\mu} a^\dagger_\mu\right)^{N/2} |0\rangle$$

The particle-number mixed (Thouless) state is:

$$|\Phi\rangle = \mathcal{N} \exp\left(\sum_{\mu>0} s_\mu z_\mu a^\dagger_{\tilde\mu} a^\dagger_\mu\right)|0\rangle$$

For this state, the pairing correlations are $P_{\mu\nu} = v^2_\mu u^2_\nu \delta_{\tilde\mu\nu}$ with $v^2_\mu = z^2_\mu/(1+z^2_\mu)$ and $u^2_\nu = 1/(1+z^2_\nu)$. The most general pair-condensate (Thouless state) has the form:

$$|\Phi\rangle = \mathcal{N}\exp\left(\frac{1}{2}\sum_{\nu\mu} Z^*_{\nu\mu} a^\dagger_\nu a^\dagger_\mu\right)|0\rangle$$

The Bloch-Messiah-Zumino theorem guarantees that canonical pairs always exist in any Thouless state -- they can be made visible by a basis transformation.

### 2. HFB Theory (Section 3)

The HFB equation in matrix representation:

$$\begin{pmatrix} T+\Gamma & \Delta \\ -\Delta^* & -T^*-\Gamma^* \end{pmatrix} \begin{pmatrix} U & V^* \\ V & U^* \end{pmatrix} = \begin{pmatrix} U & V^* \\ V & U^* \end{pmatrix} \begin{pmatrix} E & 0 \\ 0 & -E \end{pmatrix}$$

where $\Gamma_{\mu\nu} = \sum V_{\mu\mu';\nu\nu'}\rho_{\nu'\mu'}$ is the particle-hole mean field and $\Delta_{\mu\mu'} = \frac{1}{2}\sum V_{\mu\mu';\nu\nu'}\kappa_{\nu\nu'}$ is the particle-particle mean field (pairing field), obtained by averaging two-body matrix elements with respect to the density matrix $\rho$ and pairing tensor $\kappa$.

The quasiparticle-quasihole symmetry: for each quasiparticle state $\chi_\alpha$ with energy $E_\alpha$, there exists a quasihole state $\phi_\alpha$ with energy $-E_\alpha$. This produces a spectrum unbounded from below -- the "Bogoliubov sea" -- in analogy with the Dirac sea.

Within DFT, the mean fields are functional derivatives: $\Gamma_{\mu\nu} = \partial E/\partial\rho_{\nu\mu}$ and $\Delta_{\mu\mu'} = \partial E/\partial\kappa^*_{\mu\mu'}$. Constrained variations are mandatory: one minimizes the Routhian $E' = E + C(\rho)$ with penalty functional ensuring correct particle number.

### 3. The Bogoliubov Sea and Truncation (Section 4)

The Bogoliubov sea extends from minus infinity (unlike the finite Fermi sea). In truncated quasiparticle space (keeping K states), the matrix $\mathcal{P} = \mathcal{U}\mathcal{U}^+$ becomes projective but not identity. When the sum is performed over a truncated set, the pairing tensor may acquire a symmetric part -- violating the Pauli principle. The resolution: use quasiparticle truncation to define the appropriate s.p. cutoff (the "natural basis" of 2K states), then solve HFB in this truncated space to obtain an exactly antisymmetric pairing tensor.

The spectrum of P divides into three regions: (i) $p_\nu = 1$ states, (ii) paired states with $0 < p_\nu < 1$ arranged in pairs $p_{\tilde\nu} = 1 - p_\nu$, and (iii) $p_\nu = 0$ states (null space of P). The non-vanishing matrix elements of Q in region (ii) are $Q_{\nu\tilde\nu} = q_\nu = \sqrt{p_\nu(1-p_\nu)}$.

### 4. Pairing Functional (Section 5)

The commonly used zero-range pairing force with density-dependent form factor:

$$f_{pair}(r) = V_0\left\{1 + x_0\hat{P}_\sigma - \left[\eta\frac{\rho_0(r)}{\rho_c}\right]^\alpha (1+x_3\hat{P}_\sigma)\right\}$$

where $\eta = 0, 0.5, 1$ correspond to volume, mixed, and surface pairing. The isoscalar pairing field $\breve{h}_0(r) = \breve{\Sigma}_0 \cdot \hat{\sigma}$ is the projection of the quasiparticle's spin on the proton-neutron pairing field. The isoscalar pairing field is solenoidal with vanishing third component for axial symmetry.

### 5. HFB Continuum (Section 6)

Bound HFB solutions exist only for $|E_i| \leq -\lambda$. The quasiparticle continuum ($|E_i| > -\lambda$) consists of non-resonant continuum and quasiparticle resonances. Deep-hole states couple to unbound particle states through pairing, generating quasiparticle resonances with finite width.

The pairing-antihalo effect: pairing correlations in weakly-bound even-particle systems change the asymptotic behavior of particle density, reducing radial extension. Pairing coupling to positive-energy states can significantly lower the neutron chemical potential, extending the range of bound nuclei.

### 6. Regularization of Local Pairing (Section 7)

The abnormal density for zero-range pairing diverges as $1/|x|$:

$$\tilde{\rho}(r-x/2, r+x/2) \sim -\frac{\tilde{h}(r)M^*(r)}{4\pi\hbar^2|x|}\bigg|_{x\to 0}$$

Regularization uses a counterterm from the Thomas-Fermi approximation to the local s.p. Green's function. The hybrid technique divides the high-energy continuum into non-resonant part (integrated out via TF approximation) and deep-hole states (treated separately).

### 7. Pairing in Odd-Mass Nuclei (Section 8)

The one-quasiparticle state for odd nuclei: $|\Phi\rangle^{(\alpha)}_{odd} = \mathcal{N}\alpha^\dagger_\alpha \exp(\frac{1}{2}\sum Z^*_{\nu\mu}a^\dagger_\nu a^\dagger_\mu)|0\rangle$. The blocked density matrix:

$$\rho^{(\alpha)}_{\mu\nu} = (V^*V^T)_{\mu\nu} + U_{\mu\alpha}U^*_{\nu\alpha} - V^*_{\mu\alpha}V_{\nu\alpha}$$

The equal filling approximation (efa) fills both time-reversed states $\chi_\alpha$ and $\chi_{\bar\alpha}$ with equal weight. The "alispin" formalism describes arbitrary unitary mixing of time-reversed quasiparticle states; blocking depends on the orientation of the alignment vector.

---

## Key Results

1. Pairing correlations are defined measurement-theoretically as excess probability, independent of coherence or symmetry breaking
2. The Bloch-Messiah-Zumino theorem guarantees canonical pairs exist in any Thouless state
3. Truncation of the Bogoliubov sea can violate the Pauli principle through symmetric components of the pairing tensor
4. The natural basis method resolves the Pauli violation by adapting the s.p. space to the quasiparticle truncation
5. The pairing-antihalo effect limits spatial extension of drip-line nuclei
6. Zero-range pairing requires regularization/renormalization; the cutoff and strength together define the interaction
7. The equal filling approximation is equivalent to exact blocking when time-odd EDF fields are zero

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Pairing correlation | $P_{\mu\nu} = v^2_{\mu\nu} - v^2_\mu v^2_\nu$ | Eq. (1) |
| BCS N-particle state | $\|\Phi_N\rangle = \mathcal{N}_N(\sum_{\mu>0} s_\mu z_\mu a^\dagger_{\tilde\mu}a^\dagger_\mu)^{N/2}\|0\rangle$ | Eq. (2) |
| Thouless state | $\|\Phi\rangle = \mathcal{N}\exp(\frac{1}{2}\sum Z^*_{\nu\mu}a^\dagger_\nu a^\dagger_\mu)\|0\rangle$ | Eq. (6) |
| BCS form | $\|\Phi\rangle = \prod_{\mu>0}(u_\mu + s_\mu v_\mu a^\dagger_{\tilde\mu}a^\dagger_\mu)\|0\rangle$ | Eq. (5) |
| HFB equation | $\mathcal{H}\mathcal{U} = \mathcal{U}\mathcal{E}$ (matrix form) | Eq. (7) |
| Generalized density | $\mathcal{R} = \begin{pmatrix}\rho & \kappa \\ -\kappa^* & 1-\rho^*\end{pmatrix}$, $\mathcal{R}^2 = \mathcal{R}$ | Eq. (9) |
| Projective property | $P^+ = P$, $P^2 = P$ | Eq. (10) |
| Canonical Q elements | $Q_{\nu\tilde\nu} = q_\nu = \sqrt{p_\nu(1-p_\nu)}$ | Eq. (13) |
| Pairing force | $f_{pair}(r) = V_0\{1+x_0\hat{P}_\sigma - [\eta\rho_0(r)/\rho_c]^\alpha(1+x_3\hat{P}_\sigma)\}$ | Eq. (15) |
| UV divergence | $\tilde\rho(r-x/2,r+x/2) \sim -\tilde{h}(r)M^*(r)/(4\pi\hbar^2\|x\|)$ as $x\to 0$ | Eq. (17) |
| Odd-nucleus state | $\|\Phi\rangle^{(\alpha)}_{odd} = \mathcal{N}\alpha^\dagger_\alpha\exp(\frac{1}{2}\sum Z^*_{\nu\mu}a^\dagger_\nu a^\dagger_\mu)\|0\rangle$ | Eq. (19) |
| Blocked density | $\rho^{(\alpha)}_{\mu\nu} = (V^*V^T)_{\mu\nu} + U_{\mu\alpha}U^*_{\nu\alpha} - V^*_{\mu\alpha}V_{\nu\alpha}$ | Eq. (21) |
| Equal filling approx. | $\rho^{(\alpha),efa}_{\mu\nu} = (V^*V^T)_{\mu\nu} + \frac{1}{2}(U_{\mu\alpha}U^*_{\nu\alpha} - V^*_{\mu\alpha}V_{\nu\alpha} + U_{\mu\bar\alpha}U^*_{\nu\bar\alpha} - V^*_{\mu\bar\alpha}V_{\nu\bar\alpha})$ | Eq. (22) |

---

## Relevance to Phonon-Exflation

This paper is the most direct nuclear analog to the framework's BCS mechanism on the SU(3) fiber. The HFB formalism -- with its Bogoliubov transformation, quasiparticle-quasihole symmetry, and pairing tensor -- maps directly onto the framework's BCS pairing at the fold point. Specific connections: (1) The Bogoliubov sea (spectrum unbounded from below) has the same structure as the negative-energy sector of $D_K(\tau)$ -- the framework exploits this in the BdG spectral action. (2) The Pauli principle violation from truncation parallels the framework's need for careful treatment of the quasiparticle space when computing $F_{pert}$ (Perturbative Exhaustion Theorem). (3) The pairing-antihalo effect -- where pairing modifies asymptotic densities -- parallels the framework's finding that BCS condensation affects the large-distance behavior of the spectral action. (4) The regularization/renormalization of zero-range pairing is the nuclear precedent for the framework's UV sensitivity in the spectral action sums. (5) The Richardson-Gaudin integrability of the framework's BCS Hamiltonian is the exact solution of the pairing Hamiltonian that underlies this entire HFB treatment.
