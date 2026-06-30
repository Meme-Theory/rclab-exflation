# Runaway Dilaton Models: Improved Constraints from the Full Cosmological Evolution

**Author(s):** Leo Vacher, Nils Schoneberg, J.D.F. Dias, C.J.A.P. Martins, Francisco Pimenta
**Year:** 2023
**Journal:** Physical Review D (inferred from arXiv metadata)
**arXiv:** 2301.13500
**Relevance:** MEDIUM

---

## Abstract

One of the few firm predictions of string theory is the existence of a massless scalar field coupled to gravity, the dilaton. In its presence, the value of the fundamental constants of the universe, such as the fine-structure constant, will vary with the time-dependent vacuum expectation value of this field, in direct violation of the Einstein equivalence principle. The runaway dilaton proposed by Damour, Piazza, and Veneziano provides a physically motivated cosmological scenario which reconciles the existence of a massless dilaton with observations, while still providing nonstandard and testable predictions. Furthermore, the field can provide a natural candidate for dynamical dark energy. While this model has been previously constrained from local laboratory experiments and low-redshift observations, we provide here the first full self-consistent constraints, also including high redshift data, in particular from the cosmic microwave background. We consider various possible scenarios in which the field could act as quintessence. Despite the wider parameter space, we make use of recent observational progress to significantly improve constraints on the model, showing that order unity couplings (which would be natural in string theory) are ruled out.

---

## Key Arguments and Derivations

### Section II: Phenomenology of the Coupled Runaway Dilaton

The dilaton field phi appears in the Einstein-frame Lagrangian as:

L = R/(16 pi G) + (1/(8 pi G))(g^{mu nu} partial_mu phi partial_nu phi - V(phi)) - (1/4) B_F(phi) F^a_{mu nu} F^{a mu nu} - B_psi(phi) psi-bar D psi + ...

The coupling functions B_i(phi) approach finite limits as B_i(phi) = C_i + O(e^{-phi}), reconciling a massless dilaton with observations through the attractor mechanism.

The field's Klein-Gordon equation includes coupling to all massive species:

phi'' + 3H phi' = -(4 pi G) dV/dphi + sum_i alpha_i(phi)(3P_i - rho_i)

where alpha_i(phi) = d ln m_i(phi)/d phi quantifies the coupling to each species. The coupling to hadrons and dark matter follows alpha_h(phi) = alpha_{h,0} e^{-(phi - phi_0)} and alpha_m(phi) = alpha_{m,0} e^{-(phi - phi_0)}.

### Attractor Behavior

The field exhibits attractor behavior: regardless of initial velocity, Hubble friction causes the field to settle onto a trajectory determined by its couplings to massive species. The overall field displacement is most significant around matter domination, where coupling acceleration dominates over friction.

### Section II.A: Impact on Observations

The fine-structure constant variation is linked to the dilaton via:

(1/H)(alpha-dot/alpha_0) ~ alpha_h(phi)/(40) phi'

yielding the redshift dependence:

Delta alpha/alpha_0(z) = (alpha_{h,0}/40)[1 - e^{-(phi(z) - phi_0)}]

Constraints also come from the Eotvos parameter eta ~ 5.2 x 10^{-5} alpha_{h,0}^2 and the Eddington parameter gamma - 1 ~ -2 alpha_{h,0}^2.

### Section IV: Results

**Scenario 1 (V = 0, Lambda = 0):** The dilaton decoupled from a cosmological constant. Constraints: alpha_{h,0} = (0.24 +/- 4.67) x 10^{-6}, alpha_{m,0} = (-1.33 +1.92/-6.09) x 10^{-2}. Strong correlation between alpha_{m,0} and today's field value phi_0 and velocity phi'_0.

**Scenario 2 (V = 0, alpha_Lambda != 0):** Constant coupling to dark energy. Without the prior on phi'_0, alpha_Lambda can take large values with strong degeneracy with phi'_0. alpha_{h,0} is constrained 2x more tightly without the phi'_0 prior (Bayesian projection effect).

**Scenario 3 (Exponential potential):** V(phi) = A_x e^{c_x(phi - phi_0)}. The field energy Omega_phi = 0.688 +/- 0.006 shows strong degeneracy with H_0. Unlike the Lambda-coupled case, H_0 can only decrease in this scenario (because dOmega_phi/d ln a < 0 when the potential dominates). Constraints: alpha_V = (0.04 +/- 1.20) x 10^{-1}.

### Constraints Summary

MICROSCOPE provides the strongest constraint on alpha_{h,0} through eta < 10^{-15}. Atomic clock data constrain (1/H_0)(alpha-dot/alpha_0)|_{z=0} = (0.014 +/- 0.015) x 10^{-6}. Oklo reactor constrains Delta alpha/alpha_0(z = 0.14) = (0.005 +/- 0.061) x 10^{-6}. Order unity couplings (natural in string theory) are ruled out in all scenarios.

## Key Results

1. First full self-consistent constraints on the runaway dilaton model including high-redshift CMB data, improving alpha_{h,0} constraints by one order of magnitude over previous studies (due to MICROSCOPE).
2. Order unity dilaton couplings (natural in string theory) are ruled out for all considered scenarios.
3. The dilaton exhibits attractor behavior: initial field velocity is irrelevant for a wide range of initial conditions.
4. When coupled to dark energy (alpha_Lambda != 0), the dilaton can increase H_0 to 68.2 +/- 0.58 km/s/Mpc (without phi'_0 prior), partially addressing the Hubble tension.
5. With an exponential potential (quintessence), H_0 can only decrease, not increase.
6. Constraints: |alpha_{h,0}| < ~5 x 10^{-6}, |alpha_{m,0}| < ~8 x 10^{-2}, |alpha_Lambda| < ~0.5, Omega_phi = 0.688 +/- 0.006.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Einstein-frame Lagrangian | $\mathcal{L} = \frac{R}{16\pi G} + \frac{1}{8\pi G}(g^{\mu\nu}\partial_\mu\phi\partial_\nu\phi - V(\phi)) - \frac{1}{4}B_F(\phi)F^a_{\mu\nu}F^{a\mu\nu} - B_\psi(\phi)\bar{\psi}D\psi$ | Eq. 2 |
| Field density and pressure | $\rho_\phi = \frac{1}{8\pi G}[\dot{\phi}^2 + V(\phi)],\quad P_\phi = \frac{1}{8\pi G}[\dot{\phi}^2 - V(\phi)]$ | Eqs. 3-4 |
| Klein-Gordon source | $\ddot{\phi} + 3H\dot{\phi} = -4\pi G\frac{\partial V}{\partial\phi} + \sum_i \alpha_i(\phi)(3P_i - \rho_i)$ | Eq. 6 |
| Coupling function | $\alpha_i(\phi) = \frac{\partial\ln m_i(\phi)}{\partial\phi}$ | Eq. 7 |
| Hadron coupling | $\alpha_h(\phi) = \alpha_{h,0}e^{-(\phi-\phi_0)}$ | Eq. 8a |
| Dark matter coupling | $\alpha_m(\phi) = \alpha_{m,0}e^{-(\phi-\phi_0)}$ | Eq. 8b |
| Fine-structure variation | $\frac{\Delta\alpha}{\alpha_0}(z) = \frac{\alpha_{h,0}}{40}\left[1 - e^{-(\phi(z)-\phi_0)}\right]$ | Eq. 10 |
| Eotvos parameter | $\eta \approx 5.2\times 10^{-5}\alpha_{h,0}^2$ | Eq. 12a |
| Eddington parameter | $\gamma - 1 \approx -2\alpha_{h,0}^2$ | Eq. 12b |
| MICROSCOPE constraint | $\eta = (-1.5\pm 2.7)\times 10^{-15}$ | Eq. 13 |
| Atomic clock constraint | $\frac{1}{H_0}\frac{\dot{\alpha}}{\alpha_0}\bigg|_{z=0} = (0.014\pm 0.015)\times 10^{-6}$ | Eq. 14 |

## Relevance to Phonon-Exflation

The tau modulus in the phonon-exflation framework is a geometric dilaton: it parameterizes the volume/shape of the SU(3) fiber, precisely as the string dilaton parameterizes the string coupling. The constraints on dilaton couplings obtained here (alpha_{h,0} < 5 x 10^{-6}, Omega_phi < 0.02 in the quintessence regime) apply directly to any observable tau-modulus coupling to Standard Model fields. The framework's clock constraint (d alpha/alpha = -3.08 tau_dot from Session 22d) maps onto equation (9) of this paper, with alpha_h playing the role of the geometric coupling. The MICROSCOPE constraint eta ~ 5.2 x 10^{-5} alpha_{h,0}^2 < 10^{-15} bounds alpha_{h,0} < ~4 x 10^{-6}, which constrains how strongly the tau modulus can couple to hadrons. The Brans-Dicke parameter omega_BD > 500 (implied by gamma - 1 < 4 x 10^{-5} from Cassini) sets a lower bound on how weakly the tau field gravitates. The finding that the dilaton attractor mechanism operates regardless of initial conditions parallels the framework's finding that the instanton-gas transit is integrable and path-independent.
