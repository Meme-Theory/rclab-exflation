# Heat kernel expansion: user's manual

**Author(s):** D.V. Vassilevich
**Year:** 2003
**Journal:** Physics Reports (preprint submitted to Elsevier Science); lectures/review
**arXiv/DOI:** hep-th/0306138v3
**Relevance:** CRITICAL

---

## Abstract

The heat kernel expansion is a very convenient tool for studying one-loop divergences, anomalies and various asymptotics of the effective action. The aim of this report is to collect useful information on the heat kernel coefficients scattered in mathematical and physical literature. We present explicit expressions for these coefficients on manifolds with and without boundaries, subject to local and non-local boundary conditions, in the presence of various types of singularities (e.g., domain walls). In each case the heat kernel coefficients are given in terms of several geometric invariants. These invariants are derived for scalar and spinor theories with various interactions, Yang-Mills fields, gravity, and open bosonic strings. We discuss the relations between the heat kernel coefficients and quantum anomalies, corresponding anomalous actions, and covariant perturbation expansions of the effective action (both "low-" and "high-energy" ones).

**Key words:** heat kernel, functional determinants, effective action, boundary conditions, anomalies.
**PACS:** 04.62.+v, 11.10.-z, 02.40.-k.

---

## Key Arguments and Derivations

**Section 1 (Introduction).** Historical origin attributed to Fock (1937, proper-time representation of Green functions) and Schwinger (1951, manifest gauge-covariant renormalization in external fields); DeWitt later made the heat kernel the core tool of covariant QFT and quantum gravity. The heat kernel is the fundamental solution $K(t;x,y;D)$ of the heat equation $(\partial_t + D_x) K = 0$ with $K(0;x,y;D)=\delta(x,y)/\sqrt{g}$. For $D_0 = -\nabla_\mu\nabla^\mu + m^2$ on flat $\mathbb{R}^n$, the kernel is the Gaussian $(4\pi t)^{-n/2}\exp(-(x-y)^2/4t - tm^2)$. On general curved spaces, subleading corrections appear as a power series in $t$ with coefficients $b_k(x,y)$ (Seeley–DeWitt / Gilkey coefficients). The effective action is $W=\tfrac12 \ln\det D = -\tfrac12 \int_0^\infty (dt/t)\, K(t,D)$; its UV divergences are controlled by $b_k(x,x)$ with $k\le n$, and its large-mass ($1/m$) expansion is controlled by $b_k$ with $k>n$.

**Section 2 (Spectral functions).** Operators of Laplace type: $D = -(g^{\mu\nu}\partial_\mu\partial_\nu + a^\sigma\partial_\sigma + b)$ is canonically rewritten as $D = -(g^{\mu\nu}\nabla_\mu\nabla_\nu + E)$ with a unique bundle connection $\omega$ (built from $a^\sigma$) and endomorphism $E$ (built from $b$). Field strength $\Omega_{\mu\nu} = \partial_\mu\omega_\nu - \partial_\nu\omega_\mu + [\omega_\mu,\omega_\nu]$. Trace-class heat operator: $K(t,f,D) = \operatorname{Tr}_{L^2}(f e^{-tD}) \sim \sum_{k\ge0} t^{(k-n)/2} a_k(f,D)$. Zeta function $\zeta(s,f,D) = \operatorname{Tr}(fD^{-s}) = \Gamma(s)^{-1}\int_0^\infty dt\, t^{s-1} K(t,f,D)$ with $a_k(f,D) = \operatorname{Res}_{s=(n-k)/2} \Gamma(s)\zeta(s,f,D)$ and $a_n(f,D) = \zeta(0,f,D)$. Zeta-regularized effective action: $W^{\mathrm{ren}} = -\tfrac12\zeta'(0,D) - \tfrac12 \ln(\mu^2)\zeta(0,D)$.

**Section 3 (Relevant operators and boundary conditions).** For each fundamental field the quadratic fluctuation operator is brought to Laplace form and $\omega$, $E$ are given explicitly. Scalar: $\omega_\mu = G_\mu$ (gauge), $E = -\tfrac12 U''(\bar\Phi) - \xi R$; conformal value $\xi = (n-2)/[4(n-1)]$. Bosonic string (non-linear sigma model with $B$-field and boundary $A$-field): $\omega$ gets a contribution from $H_{ABC}$, and oblique (tangential-derivative) boundary conditions arise on Dirichlet branes. Spinor: square of Dirac with $V$- and $A$-connections produces $E = -\tfrac14 R + \tfrac14 [\gamma^\mu,\gamma^\nu]F_{\mu\nu} + i\gamma^5 D^\mu A^5_\mu - (n-2)A^5_\mu A^{5\mu} + \ldots$; bag boundary conditions with chiral phase. Vector (Yang–Mills in the gauge $\nabla^\mu A^\alpha_\mu = 0$): $(\omega_\mu)^{\alpha\rho}_{\nu\beta} = B^\gamma_\mu c^\alpha_{\gamma\beta}\delta^\rho_\nu - \Gamma^\rho_{\mu\nu}\delta^\alpha_\beta$, $(E)^{\alpha\rho}_{\nu\beta} = -R^\rho_\nu\delta^\alpha_\beta + 2F(B)^{\gamma\rho}_\nu c^\gamma_{\beta\alpha}$; absolute vs. relative boundary conditions. Graviton (York-type decomposition around Einstein background): conformal-factor problem; non-local boundary conditions required.

**Section 4 (Heat kernel on closed manifolds).** The $a_k$ are integrals of universal local invariants. Gilkey's functorial method (product manifold, scale variation, heat kernel on $S^1$) fixes all undetermined coefficients. Leading results listed below. Flat-space plane-wave evaluation (geodesic waves on curved spaces) independently confirms $a_0,\ldots,a_4$. Coefficients $a_0\ldots a_4$ are in [Gilkey 1984, De Witt]; $a_6$ is computed in Gilkey (1975); $a_8$ by Amsterdamski et al. (scalar) and Avramidi (general Laplace-type); $a_{10}$ by van de Ven.

**Section 5 (Boundaries).** Dirichlet, Neumann/Robin, and mixed (projector-decomposed) boundary conditions produce half-integer powers of $t$. Boundary contributions involve the extrinsic curvature $L_{ab}$ and the Neumann endomorphism $S$. Oblique boundary conditions (tangential derivatives) lead to loss of strong ellipticity at the "critical electric field" of string physics.

**Section 6 (Singularities).** Conical singularities (with explicit conical-deficit contributions), domain walls and brane-world scenarios, non-smooth boundaries, dielectric bodies.

**Section 7 (Anomalies).** Conformal (trace) anomaly: $\langle T^\mu_\mu \rangle$ is proportional to $a_n(x,D)$ at coincidence, with the universal combination $bC^2 + b'E_4$ in $n=4$. Chiral anomaly emerges from the difference of kernels for chiral projections. Remarks on the Atiyah–Singer index theorem.

**Section 8 (Resummations).** Modified large-mass expansion, covariant perturbation theory (Barvinsky–Vilkovisky), low-energy R-summed expansion: the $R$-dependent terms (excluding derivatives) re-sum to $\exp(sR/6)$, giving the $R$-summed Schwinger–DeWitt series with $\bar a_1 = 0$, $\bar a_2 = (R_{\alpha\beta\gamma\delta}R^{\alpha\beta\gamma\delta} - R_{\alpha\beta}R^{\alpha\beta})/180 + \Box R/30$. Heat kernel on homogeneous spaces (exact spectra).

**Section 9 (Exact effective actions).** Polyakov action in 2D, duality symmetry between effective actions in dual theories.

## Key Results

1. Every one-loop effective action in QFT can be reduced to a heat kernel computation for a Laplace-type operator plus a boundary-condition prescription.
2. The heat kernel coefficients $a_k$ are integrals of universal local invariants of $R_{\mu\nu\rho\sigma}$, $E$, $\Omega_{\mu\nu}$ and their derivatives, with coefficients independent of the dimension $n$ up to an overall $(4\pi)^{-n/2}$.
3. Gilkey's functorial method (product manifold, scale variation) fixes all the coefficients.
4. Explicit $a_0, a_2, a_4, a_6$ on manifolds without boundary; $a_0,\ldots,a_4$ with local boundary conditions.
5. Conformal anomaly in $n=4$ is carried by $a_4$ and takes the universal form $bC^2 + b'E_4$ (plus matter terms).
6. Covariant perturbation theory and low-energy ($R$-summed) expansions give controlled non-local pieces of the effective action.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| heat-eq | $(\partial_t + D_x) K(t;x,y;D) = 0$, $K(0;x,y;D)=\delta(x,y)/\sqrt{g}$ | (1.10)–(1.11) |
| flat-ker | $K(t;x,y;D_0) = (4\pi t)^{-n/2}\exp\!\big(-(x-y)^2/(4t) - tm^2\big)$ | (1.12) |
| sub-exp | $K(t;x,y;D) = K(t;x,y;D_0)\big(1 + tb_2(x,y) + t^2 b_4(x,y) + \cdots\big)$ | (1.13) |
| W-int | $W = -\tfrac12 \int_0^\infty (dt/t)\, K(t,D)$ | (1.18) |
| UV-div | $W^{\mathrm{div}}_\Lambda = -(4\pi)^{-n/2}\int d^nx\sqrt{g}\!\left[\sum_{2(j+l)<n}\!\Lambda^{n-2j-2l} b_{2j}\tfrac{(-m^2)^l l!}{n-2j-2l} + \sum_{2(j+l)=n}\!\ln\Lambda (-m^2)^l l!\, b_{2j}\right]$ | (1.21) |
| Laplace-canon | $D = -(g^{\mu\nu}\nabla_\mu\nabla_\nu + E)$ with $\omega_\delta = \tfrac12 g_{\nu\delta}(a^\nu + g^{\mu\sigma}\Gamma_{\mu\sigma}^{\ \ \nu} I_V)$, $E = b - g^{\nu\mu}(\partial_\mu\omega_\nu + \omega_\nu\omega_\mu - \omega_\sigma\Gamma_{\nu\mu}^{\ \ \sigma})$ | (2.2)–(2.4) |
| Omega | $\Omega_{\mu\nu} = \partial_\mu\omega_\nu - \partial_\nu\omega_\mu + \omega_\mu\omega_\nu - \omega_\nu\omega_\mu$ | (2.10) |
| trace-asy | $\operatorname{Tr}_{L^2}(f e^{-tD}) \sim \sum_{k\ge0} t^{(k-n)/2} a_k(f,D)$ | (2.21) |
| zeta-def | $\zeta(s,f,D) = \Gamma(s)^{-1}\int_0^\infty dt\, t^{s-1} K(t,f,D)$ | (2.24) |
| zeta-res | $a_k(f,D) = \operatorname{Res}_{s=(n-k)/2} \Gamma(s)\zeta(s,f,D)$, $a_n(f,D)=\zeta(0,f,D)$ | (2.26)–(2.27) |
| W-ren | $W^{\mathrm{ren}} = -\tfrac12 \zeta'(0,D) - \tfrac12 \ln(\mu^2)\zeta(0,D)$ | (2.32) |
| a0 | $a_0(f,D) = (4\pi)^{-n/2}\int_M d^nx\sqrt{g}\,\operatorname{tr}_V\{f\}$ | (4.26) |
| a2 | $a_2(f,D) = (4\pi)^{-n/2} 6^{-1}\int_M d^nx\sqrt{g}\,\operatorname{tr}_V\{f(6E+R)\}$ | (4.27) |
| a4 | $a_4(f,D) = (4\pi)^{-n/2} 360^{-1}\int_M d^nx\sqrt{g}\,\operatorname{tr}_V\{f(60E_{;kk}+60RE+180E^2+12R_{;kk}+5R^2-2R_{ij}R^{ij}+2R_{ijkl}R^{ijkl}+30\Omega_{ij}\Omega^{ij})\}$ | (4.28) |
| R-sum | $K(x,x;s) = (4\pi s)^{-n/2} e^{Rs/6}\big(\bar a_0 + \bar a_1 s + \bar a_2 s^2 + \cdots\big)$, $\bar a_1=0$, $\bar a_2 = (R_{\alpha\beta\gamma\delta}R^{\alpha\beta\gamma\delta}-R_{\alpha\beta}R^{\alpha\beta})/180 + \Box R/30$ | (8.x) |
| scalar-E | (Scalar) $E = -\tfrac12 U''(\bar\Phi) - \xi R$, $\xi_{\mathrm{conf}} = (n-2)/[4(n-1)]$ | (3.5)–(3.6) |
| spinor-E | (Dirac) $E = -\tfrac14 R + \tfrac14[\gamma^\mu,\gamma^\nu]F_{\mu\nu} + i\gamma^5 D^\mu A^5_\mu - (n-2)A^5_\mu A^{5\mu} - \tfrac14(n-3)[\gamma^\mu,\gamma^\nu][A^5_\mu, A^5_\nu]$ | (3.27) |

## Relevance to Phonon-Exflation

This paper is the master reference for every Seeley–DeWitt computation in the project. All computation heat-kernel evaluations on the Jensen-deformed SU(3) fibre rely on the Gilkey normalisation $a_0, a_2, a_4$ listed here: $a_0$ fixes the cosmological-constant moment of the spectral action; $a_2 \sim R$ reproduces Einstein–Hilbert (the "second spectral moment" identified in the constraint map); $a_4$ supplies Yang–Mills, Weyl$^2$, and Higgs-potential contributions that underlie the S36/S42 spectral-action closures and the 28-dimensional bare spectral-action monotonicity (W4 wall). Reference for Computation A (heat kernel at finite density / finite-temperature expansion of $\operatorname{Tr} f(D/\Lambda)$). The $R$-summed series is the technical tool used in Parker/Wondrak-type gravitational particle-creation estimates confronted in S74/S79.
