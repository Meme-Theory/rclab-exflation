# Vacuum Energy and Cosmological Constant in QFT in Curved Spacetime

**Author(s):** Joan Sola Peracaula and Cristian Moreno-Pulido
**Year:** 2024
**Journal:** Proceedings of the 17th Marcel Grossmann Meeting (MG17), Pescara, Italy, July 7-12, 2024; WSPC Proceedings
**arXiv:** 2411.06582
**Relevance:** CRITICAL

---

## Abstract

The cosmological constant term (CC), $\Lambda$, is a pivotal ingredient in the standard model of cosmology or $\Lambda$CDM, but it is a rigid quantity for the entire cosmic history. This is unnatural and inconsistent. Different theoretical and phenomenological conundrums suggest that the $\Lambda$CDM necessitates further theoretical underpinning to cope with modern observations. An interesting approach is the framework of the 'running vacuum model' (RVM). It endows $\Lambda$ with cosmic dynamics within a fundamental framework since it is based on QFT. In the RVM, the vacuum energy density (VED) appears as a series of powers of the Hubble function and its derivatives, $\rho_{\text{vac}}(H, \dot{H}, \ldots)$. In the current universe, $\rho_{\text{vac}}$ changes as $\sim H^2$. Higher order effects $O(H^4)$, on the other hand, can be responsible for a new mechanism of inflation (RVM-inflation). On the practical side the RVM can alleviate the cosmological tensions on $\sigma_8$ and $H_0$. An intriguing smoking gun signature of the RVM is that its equation of state can mimic quintessence, as recently observed by DESI, so the vacuum can be the sought-for dynamical DE. At a deeper theoretical level, the RVM-renormalized form of the VED can avoid extreme fine tuning related to the well-known cosmological constant problem. Overall, the RVM has the capacity to impinge positively on relevant theoretical and practical aspects of modern cosmology.

---

## Key Arguments and Derivations

### 1. The Cosmological Constant Problem (CCP)

The observational value of the VED is $\rho_{\text{vac}} \sim 10^{-47}$ GeV$^4$. Naive QFT estimates from the zero-point energy (ZPE) give contributions of order $m^4$ for any particle mass $m$. For the electron: $\rho_{\text{vac}}^{\text{obs}} / m_e^4 \sim 10^{-34}$. For the Higgs: $\rho_{\text{vac}}^{\text{obs}} / \langle V_{\text{eff}} \rangle \sim 10^{-56}$. This mismatch of 34-56 orders of magnitude is the CCP.

Additional problems: the cosmic coincidence problem ($\rho_{\text{vac}} \sim \rho_{\text{CDM}}$ today despite different scaling), $H_0$ tension ($\sim 5\sigma$ between CMB and distance ladder), and $\sigma_8$ tension ($\sim 2-3\sigma$ excess structure formation at low redshift).

### 2. Non-Minimally Coupled Scalar Field in FLRW

Starting from the action for a real scalar field $\varphi$ with non-minimal coupling $\xi$ to gravity:
$$S[\varphi] = -\int d^4x \sqrt{-g} \left[\frac{1}{2}g^{\mu\nu}\partial_\nu\varphi\partial_\mu\varphi + \frac{1}{2}(m^2 + \xi R)\varphi^2\right]$$

The energy-momentum tensor is:
$$T_{\mu\nu}(\varphi) = (1 - 2\xi)\partial_\mu\varphi\partial_\nu\varphi + (2\xi - 1/2)g_{\mu\nu}\partial_\sigma\varphi\partial^\sigma\varphi - 2\xi\varphi\nabla_\mu\nabla_\nu\varphi + 2\xi g_{\mu\nu}\varphi\Box\varphi + \xi G_{\mu\nu}\varphi^2 - \frac{1}{2}m^2 g_{\mu\nu}\varphi^2$$

For $\xi = 1/6$ and $m = 0$, the action has conformal symmetry. The deviation from conformal coupling is denoted $\bar{\xi} \equiv \xi - 1/6$.

### 3. Adiabatic Regularization Procedure (ARP)

Quantum fluctuations $\delta\varphi$ are expanded in Fourier modes $h_k(\tau)$ satisfying:
$$h_k'' + \Omega_k^2 h_k = 0, \quad \Omega_k^2(\tau) \equiv \omega_k^2(m) + a^2(\xi - 1/6)R$$

The WKB ansatz $h_k \sim W_k^{-1/2} \exp(i\int^\tau W_k d\tilde{\tau})$ leads to a nonlinear differential equation for $W_k$, solved by the adiabatic expansion $W_k = \omega_k^{(0)} + \omega_k^{(2)} + \omega_k^{(4)} + \ldots$ organized in even adiabatic orders (by general covariance). UV-divergent terms are present up to 4th adiabatic order.

### 4. Off-Shell Renormalization of the ZPE

The crucial innovation is off-shell ARP: the WKB expansion is performed at an arbitrary mass scale $M$ replacing $m$, with $\Delta^2 \equiv m^2 - M^2$ treated as adiabatic order 2. The renormalized ZPE is defined by subtraction:
$$\langle T_{00}^{\delta\varphi}\rangle_{\text{Ren}}(M) = \langle T_{00}^{\delta\varphi}\rangle(m) - \langle T_{00}^{\delta\varphi}\rangle^{(0-4)}(M)$$

The result, after momentum integration:
$$\langle T_{00}^{\delta\varphi}\rangle_{\text{Ren}}(M) = \frac{a^2}{128\pi^2}\left[-M^4 + 4m^2 M^2 - 3m^4 + 2m^4\ln\frac{m^2}{M^2}\right] - \bar{\xi}\frac{3\mathcal{H}^2}{16\pi^2}\left[m^2 - M^2 - m^2\ln\frac{m^2}{M^2}\right] + \bar{\xi}^2 \frac{9(2\mathcal{H}''\mathcal{H} - \mathcal{H}'^2 - 3\mathcal{H}^4)}{16\pi^2 a^2}\ln\frac{m^2}{M^2} + \ldots$$

Note: this expression still contains $\sim m^4$ terms. These are not the final VED.

### 5. Renormalized Vacuum Energy Density -- Absence of $m^4$ Terms

The full modified Einstein's equations include higher-derivative (HD) terms:
$$M_{\text{Pl}}^2(M) G_{\mu\nu} + \rho_\Lambda(M) g_{\mu\nu} + \alpha(M) H_{\mu\nu}^{(1)} = \langle T_{\mu\nu}^{\delta\varphi}\rangle_{\text{Ren}}(M)$$

Subtracting at two different scales $M$ and $M_0$ yields the running of couplings. The physical VED is:
$$\rho_{\text{vac}}(M, H) = \rho_\Lambda(M) + \frac{\langle T_{00}^{\delta\varphi}\rangle_{\text{Ren}}(M)}{a^2}$$

Subtracting at two scales $M$ and $M_0$:
$$\rho_{\text{vac}}(M, H) = \rho_{\text{vac}}(M_0, H) + \frac{3}{16\pi^2}\bar{\xi}H^2\left[M^2 - M_0^2 - m^2\ln\frac{M^2}{M_0^2}\right] + O(H^4)$$

The $m^4$ terms cancel between $\rho_\Lambda(M)$ and the ZPE contributions. No fine tuning is needed.

### 6. Running Vacuum Model (RVM) -- Canonical Form

Setting the renormalization scale $M$ to the Hubble rate $H$ at each epoch, and defining the effective running parameter:
$$\nu_{\text{eff}}(H) = \frac{1}{2\pi}\bar{\xi}\frac{m^2}{m_{\text{Pl}}^2}\left[-1 + \frac{m^2}{H^2 - H_0^2}\frac{H^2 - H_0^2}{H^2 - H_0^2}\ln\frac{H^2}{H_0^2}\right]$$

The canonical RVM formula for the VED becomes:
$$\rho_{\text{vac}}(H) = \rho_{\text{vac}}^0 + \frac{3\nu_{\text{eff}}(H)}{8\pi G_N}(H^2 - H_0^2)$$

where $\rho_{\text{vac}}^0 \equiv \rho_{\text{vac}}(H_0)$ is today's observed VED and $\nu_{\text{eff}} \sim 10^{-5} - 10^{-3}$ for GUT-scale particles. The running is logarithmically slow.

### 7. RVM-Inflation

At high energies ($H \sim m$), higher adiabatic orders ($H^4$, $H^6$, ...) become relevant. The first inflationary power appearing explicitly is $H^6$:
$$\rho_{\text{vac}}^{\text{inf}} \sim C_{\text{inf}} H^6$$

The cosmological equations yield $H(\hat{a}) = H_I(1 + \hat{a}^8)^{-1/4}$, with:
$$\rho_{\text{vac}}(\hat{a}) = \rho_I(1 + \hat{a}^8)^{-3/2}, \quad \rho_r = \hat{a}^8 \rho_{\text{vac}}(\hat{a})$$

This provides a graceful exit from inflation (vacuum decays into radiation) without an inflaton field.

### 8. Dynamical Equation of State

The quantum vacuum EoS deviates from $w = -1$ due to quantum corrections. In the matter-dominated era:
$$w_{\text{vac}}(z) \simeq -1 + \nu_{\text{eff}}\left(\frac{\Omega_m^0(1 + z)^3}{\Omega_{\text{vac}}^0 + \nu_{\text{eff}}\Omega_m^0[(1 + z)^3 - 1]}\right)$$

For $\nu_{\text{eff}} > 0$, this gives $w_{\text{vac}} > -1$ (quintessence-like behavior), consistent with DESI observations. The paper notes this is the "smoking gun signature" of the RVM.

---

## Key Results

1. The CCP is resolved within the RVM: $m^4$ terms cancel in the renormalized VED when subtracting at two scales. No fine tuning required.
2. The VED runs with the Hubble rate: $\rho_{\text{vac}}(H) = \rho_{\text{vac}}^0 + (3\nu_{\text{eff}}/8\pi G_N)(H^2 - H_0^2)$.
3. The effective running parameter $\nu_{\text{eff}} \sim 10^{-5} - 10^{-3}$ for GUT-scale particles.
4. RVM-inflation driven by $H^6$ (or $H^4$) terms provides a QFT-based alternative to inflaton-driven inflation.
5. The vacuum EoS deviates from $-1$ and mimics quintessence ($w > -1$), consistent with DESI.
6. The RVM can alleviate $H_0$ and $\sigma_8$ tensions.
7. Adiabatic regularization with off-shell subtraction at scale $M$ is the key technical innovation.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Scalar field action | $S[\varphi] = -\int d^4x\sqrt{-g}\left[\frac{1}{2}g^{\mu\nu}\partial_\nu\varphi\partial_\mu\varphi + \frac{1}{2}(m^2 + \xi R)\varphi^2\right]$ | Eq. (1) |
| Klein-Gordon equation | $(\Box - m^2 - \xi R)\varphi = 0$ | Eq. (2) |
| EMT | $T_{\mu\nu}(\varphi) = (1-2\xi)\partial_\mu\varphi\partial_\nu\varphi + (2\xi - 1/2)g_{\mu\nu}\partial_\sigma\varphi\partial^\sigma\varphi - 2\xi\varphi\nabla_\mu\nabla_\nu\varphi + \ldots$ | Eq. (3) |
| Mode equation | $h_k'' + \Omega_k^2 h_k = 0$, $\Omega_k^2 = \omega_k^2(m) + a^2(\xi - 1/6)R$ | Eq. (6) |
| WKB equation | $W_k^2 = \Omega_k^2 - \frac{1}{2}W_k''/W_k + \frac{3}{4}(W_k'/W_k)^2$ | Eq. (8) |
| Off-shell renormalized ZPE | $\langle T_{00}^{\delta\varphi}\rangle_{\text{Ren}}(M) = \frac{a^2}{128\pi^2}[-M^4 + 4m^2 M^2 - 3m^4 + 2m^4\ln(m^2/M^2)] + \ldots$ | Eq. (17) |
| Coupling running | $\delta\rho_\Lambda = \frac{1}{128\pi^2}[M^4 - M_0^4 - 4m^2(M^2 - M_0^2) + 2m^4\ln(M^2/M_0^2)]$ | Eq. (21) |
| Physical VED | $\rho_{\text{vac}}(M,H) = \rho_\Lambda(M) + \langle T_{00}^{\delta\varphi}\rangle_{\text{Ren}}(M)/a^2$ | Eq. (22) |
| Running VED (no $m^4$) | $\rho_{\text{vac}}(M,H) = \rho_{\text{vac}}(M_0,H) + \frac{3\bar{\xi}}{16\pi^2}H^2[M^2 - M_0^2 - m^2\ln(M^2/M_0^2)] + O(H^4)$ | Eq. (24) |
| Canonical RVM | $\rho_{\text{vac}}(H) = \rho_{\text{vac}}^0 + \frac{3\nu_{\text{eff}}}{8\pi G_N}(H^2 - H_0^2)$ | Eq. (27) |
| Running parameter | $\nu_{\text{eff}} \approx \frac{1}{2\pi}\bar{\xi}\frac{m^2}{m_{\text{Pl}}^2}\ln\frac{m^2}{H_0^2}$ | Eq. (28) |
| RVM inflation | $\rho_{\text{vac}}^{\text{inf}} \sim C_{\text{inf}}H^6$; $\rho_{\text{vac}}(\hat{a}) = \rho_I(1+\hat{a}^8)^{-3/2}$ | Eqs. (29)-(30) |
| Vacuum EoS | $w_{\text{vac}}(z) \simeq -1 + \nu_{\text{eff}}(\Omega_m^0(1+z)^3/[\Omega_{\text{vac}}^0 + \nu_{\text{eff}}\Omega_m^0((1+z)^3 - 1)])$ | Sec. 9 |

---

## Relevance to Phonon-Exflation

This paper is directly relevant to the framework's central open question: the cosmological constant problem. The RVM approach provides a concrete QFT mechanism for dynamical vacuum energy that avoids the $\sim m^4$ fine-tuning catastrophe through off-shell adiabatic renormalization. The framework's instanton gas and BCS-type condensate produce a vacuum energy density during the transit through the fold, and the RVM's result that $\rho_{\text{vac}}(H)$ runs as $\sim H^2$ (with no $m^4$ terms) is directly comparable to the framework's CC-ARITH hierarchy ($a_4 \gg |a_2| \gg a_0$). The RVM-inflation mechanism via $H^6$ terms provides an alternative to the framework's Kibble-Zurek paradigm for the transit. The quintessence-like EoS mimicry ($w > -1$) connects to the DESI tension and the framework's substrate-compaction-timescape hypothesis (S59), where fiber complexity variation produces apparent $w_a$ from a static framework.
