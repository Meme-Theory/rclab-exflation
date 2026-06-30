# Intro to Effective Field Theories and Inflation

**Author(s):** C.P. Burgess
**Year:** 2018 (lectures July 2017)
**Journal:** Prepared for JHEP (Les Houches Summer School lecture notes)
**arXiv:** 1711.10592
**Relevance:** MEDIUM

---

## Abstract

These notes present an introduction to inflationary cosmology with an emphasis on some of the ways effective field theories are used in its analysis. Based on lectures prepared for the Les Houches Summer School Effective Field Theory in Particle Physics and Cosmology, July 2017.

---

## Key Arguments and Derivations

### Section 1: Cosmology -- Background

A pedagogical review of standard LCDM cosmology: FRW geometries (eq. 1.1), Friedmann equations $H^2 + \kappa/a^2 = \rho/(3M_p^2)$ (eq. 1.11), energy conservation $\dot\rho + 3H(p+\rho) = 0$ (eq. 1.12), equations of state $p = w\rho$ (eq. 1.14) for nonrelativistic matter ($w=0$), radiation ($w=1/3$), and cosmological constant ($w=-1$). The horizon problem, flatness problem, and monopole problem motivate an early accelerated epoch. Simple single-field inflationary models are reviewed, including slow-roll conditions $\epsilon = M_p^2(V'/V)^2/2 \ll 1$ and $\eta = M_p^2 V''/V \ll 1$.

### Section 2: Cosmology -- Fluctuations

Structure formation in LCDM from amplification of primordial perturbations. Linear evolution of metric-inflaton fluctuations in slow-roll. The curvature perturbation $\zeta$ is conserved outside the horizon. Quantum origin of fluctuations via the Bunch-Davies vacuum. The scalar power spectrum $\Delta_\zeta^2 = H^4/(4\pi^2\dot\phi^2) = H^2/(8\pi^2\epsilon M_p^2)$ (eq. 2.78) and spectral index $n_s - 1 = -6\epsilon + 2\eta$ (eq. 2.82). Tensor fluctuations and the consistency relation $r = 16\epsilon$.

Section 2.3 ("Flies in the ointment") raises key concerns: the eta problem (why is the inflaton mass so much lighter than $H$?), the trans-Planckian problem (modes observed in the CMB had sub-Planckian wavelengths early in inflation), and sensitivity to initial conditions.

### Section 3: EFT Issues (the core contribution)

**3.1.1 GREFT (General Relativity Effective Field Theory):** GR is treated as the leading term in a derivative expansion, analogous to a nonlinear sigma model. The GREFT Lagrangian is:

$$-\frac{\mathcal{L}_{\rm GREFT}}{\sqrt{-g}} = \lambda + \frac{M_p^2}{2}R + c_{41}R_{\mu\nu}R^{\mu\nu} + c_{42}R^2 + c_{43}R_{\mu\nu\lambda\rho}R^{\mu\nu\lambda\rho} + c_{44}\Box R + \frac{c_{61}}{M^2}R^3 + \ldots$$

The cosmological constant $\lambda$ is the only zero-derivative term. The four-derivative terms ($R^2$, $R_{\mu\nu}R^{\mu\nu}$, $R_{\mu\nu\lambda\rho}R^{\mu\nu\lambda\rho}$) can all be eliminated by the Gauss-Bonnet identity (eq. 3.5) and field redefinitions using the leading-order EOM $R_{\mu\nu} = 0$, so the first nontrivial correction to pure gravity involves six or more derivatives (curvature-cubed).

**3.1.2 Power counting (gravity only):** The graviton scattering amplitude at $L$ loops with vertices $V_{id}$ ($d$ derivatives, $i$ gravitons) scales as:

$$\mathcal{A}_E(q) \sim q^2 M_p^2 \left(\frac{1}{M_p}\right)^E \left(\frac{q}{4\pi M_p}\right)^{2L} \prod_i \prod_{d>2} \left[\frac{q^2}{M_p^2}\left(\frac{q}{M}\right)^{d-4}\right]^{V_{id}}$$

The semiclassical expansion parameter is $q^2/(4\pi M_p)^2$; the semiclassical approximation IS the low-energy approximation. For cosmology with $q \sim H$, this requires $H \ll 4\pi M_p$ for semiclassical methods to be valid.

**3.1.3 Power counting (scalar-tensor theories):** Including $N$ dimensionless scalars $\theta^i = \phi^i/M_p$ with potential $V = v^4 U(\theta)$, the scalar-tensor EFT Lagrangian (eq. 3.7) introduces a potential energy scale $v$ with $H^2 M_p^2 \sim v^4 \ll M^4 \ll M_p^4$. The potentially dangerous zero-derivative (potential) vertices contribute factors $\lambda_n(v^4/(H^2 M_p^2))^{V_n}$, but using $H \simeq v^2/M_p$ these reduce to order-unity factors $\lambda_n^{V_n}$ (eq. 3.13). The final power-counting formula (eq. 3.14) shows:

1. The loop expansion parameter remains $(H/(4\pi M_p))^{2L}$ -- the semiclassical expansion holds for $H \ll M_p$.
2. Trans-Planckian field values ($\phi \sim M_p$) do NOT threaten the derivative expansion -- what matters is low energies, not small fields. The expansion is in derivatives ($\partial\phi$), not in $\phi$ itself.
3. Slow-roll parameters $\epsilon$ further suppress corrections via $\lambda_n \simeq \epsilon^{N_n/2}\hat\lambda_n$ (eq. 3.15).

**3.2 Conceptual issues for EFTs with time-dependent backgrounds:**

*Adiabatic approximation (Sec. 3.2.1):* The time dependence of the background introduces a new scale $\dot H/H^2 \sim \epsilon$. The adiabatic approximation (treating the background as slowly varying) is justified when $\epsilon \ll 1$.

*Predicting background evolution (Sec. 3.2.2):* EFTs can predict the background evolution because the leading contribution is classical ($L=0$), which is just solving the classical field equations of GR + inflaton.

*EFT for inflationary fluctuations (Sec. 3.2.3):* References to the Cheung et al. construction and the EFT of inflation in unitary gauge.

*Open systems (Sec. 3.2.4):* Discusses how the EFT treatment must be modified when the system of interest (long-wavelength modes) is coupled to an environment (short-wavelength modes that have crossed the horizon), leading to decoherence and open-system EFT methods.

---

## Key Results

1. GR should be regarded as the leading term in GREFT -- a derivative expansion in curvature invariants. All four-derivative terms are redundant for pure gravity in 4D.

2. The semiclassical expansion parameter for gravity is $(H/(4\pi M_p))^2 \sim 10^{-10}$ during inflation -- semiclassical methods are extraordinarily well-controlled.

3. Trans-Planckian field values do not invalidate the EFT: the expansion is in derivatives (energies), not field values.

4. The scalar potential's zero-derivative vertices are tamed by the Friedmann relation $H \sim v^2/M_p$, so they contribute order-unity factors rather than breaking the derivative expansion.

5. Slow-roll parameters provide additional suppression of quantum corrections, with each vertex contributing $\epsilon^{N_n/2}$.

6. The quality of the semiclassical expansion favours inflationary models over alternatives (bouncing cosmologies) that require $H \sim M_p$ at the bounce.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| GREFT Lagrangian | $-\mathcal{L}/\sqrt{-g} = \lambda + \frac{M_p^2}{2}R + c_{41}R_{\mu\nu}R^{\mu\nu} + c_{42}R^2 + c_{43}R_{\mu\nu\lambda\rho}R^{\mu\nu\lambda\rho} + \ldots$ | Eq. (3.4) |
| Gauss-Bonnet combination | $\sqrt{-g}\,X = \sqrt{-g}(R_{\mu\nu\lambda\rho}R^{\mu\nu\lambda\rho} - 4R_{\mu\nu}R^{\mu\nu} + R^2)$ | Eq. (3.5) |
| Graviton power counting | $\mathcal{A}_E(q) \sim q^2 M_p^2(1/M_p)^E(q/(4\pi M_p))^{2L}\prod_{d>2}[(q^2/M_p^2)(q/M)^{d-4}]^{V_{id}}$ | Eq. (3.6) |
| Scalar-tensor EFT | $-\mathcal{L}/\sqrt{-g} = v^4 V(\theta) + \frac{M_p^2}{2}g^{\mu\nu}[W(\theta)R_{\mu\nu} + G_{ij}(\theta)\partial_\mu\theta^i\partial_\nu\theta^j] + \ldots$ | Eq. (3.7) |
| Cosmological power counting | $\mathcal{B}_E(H) \simeq \frac{M_p^2}{H^2}\left(\frac{H^2}{M_p}\right)^E\left(\frac{H}{4\pi M_p}\right)^{2L}\prod_{d_n=0}\lambda_n^{V_n}\prod_{d_n\geq4}[g_n(H/M_p)^2(H/M)^{d_n-4}]^{V_n}$ | Eq. (3.14) |
| Slow-roll suppression | $\lambda_n \simeq \epsilon^{N_n/2}\hat\lambda_n$ | Eq. (3.15) |
| Friedmann equation | $H^2 + \kappa/a^2 = \rho/(3M_p^2)$ | Eq. (1.11) |
| Scalar power spectrum | $\Delta_\zeta^2 = H^4/(4\pi^2\dot\phi^2) = H^2/(8\pi^2\epsilon M_p^2)$ | Eq. (2.78) |
| Spectral index | $n_s - 1 = -6\epsilon + 2\eta$ | Eq. (2.82) |
| Two-point estimates | $\langle hh\rangle \sim \langle\phi\phi\rangle \sim H^2$; $\langle\phi h\rangle \sim \sqrt\epsilon\,H^2$ | Eq. (3.17) |

---

## Relevance to Phonon-Exflation

Burgess's treatment of UV sensitivity in the gravitational EFT maps directly onto the question of whether the spectral action's $\Lambda$ cutoff introduces hierarchy problems analogous to those in standard inflation. The power-counting formula (eq. 3.14) identifies $(H/(4\pi M_p))^2$ as the loop-counting parameter -- this is the same ratio that governs whether the spectral action's Seeley-DeWitt expansion (which IS a derivative expansion in curvature invariants) is under perturbative control. The GREFT Lagrangian (eq. 3.4) is structurally identical to the spectral action's heat kernel expansion: $a_0 \sim \lambda$, $a_2 \sim M_p^2 R$, $a_4 \sim R^2 + R_{\mu\nu}R^{\mu\nu} + \ldots$, making explicit that the spectral action IS a GREFT with coefficients determined by the spectrum of $D_K$. Burgess's argument that trans-Planckian field values do not invalidate the EFT (the expansion is in derivatives, not fields) is relevant to the exflation framework where the Jensen deformation parameter $\tau$ traverses a large range but the spectral action remains a controlled derivative expansion throughout.
