# The Spectral Action Principle

**Author(s):** Ali H. Chamseddine and Alain Connes
**Year:** 1996
**Journal:** (preprint; later Commun. Math. Phys. 186, 731 (1997))
**arXiv/DOI:** hep-th/9606001v1 (3 Jun 1996)
**Relevance:** CRITICAL

---

## Abstract

We propose a new action principle to be associated with a noncommutative space $(\mathcal{A}, \mathcal{H}, D)$. The universal formula for the spectral action is $(\psi, D\psi) + \operatorname{Trace}(\chi(D/\Lambda))$ where $\psi$ is a spinor on the Hilbert space, $\Lambda$ is a scale and $\chi$ a positive function. When this principle is applied to the noncommutative space defined by the spectrum of the standard model one obtains the standard model action coupled to Einstein plus Weyl gravity. There are relations between the gauge coupling constants identical to those of $SU(5)$ as well as the Higgs self-coupling, to be taken at a fixed high energy scale.

---

## Key Arguments and Derivations

**Section 1 (Introduction).** Classical Riemannian data $(M, g_{\mu\nu})$ with line element $ds^2 = g_{\mu\nu} dx^\mu dx^\nu$ are replaced by a spectral triple $(\mathcal{A},\mathcal{H},D)$: an involutive algebra $\mathcal{A}$ of operators on Hilbert space $\mathcal{H}$ and a self-adjoint unbounded operator $D$ whose inverse plays the role of $ds$ (the fermion propagator). Points of $M$ are recovered as characters of $\mathcal{A}$; geodesic distance is $d(x,y) = \sup\{|a(x)-a(y)|\,:\, a\in\mathcal{A}, \|[D,a]\|\le1\}$. $\mathbb{Z}/2$ grading $\gamma$ and real structure $J$ (antilinear isometry) are subject to $J^2=\varepsilon$, $JD=\varepsilon' DJ$, $J\gamma=\varepsilon''\gamma J$ with signs determined by $n\bmod 8$.

**Core principle:** the physical action depends only on the spectrum $\Sigma$ of $D$ (isospectral invariance, stronger than diffeomorphism invariance). Diff$(M)$ is replaced by $\operatorname{Aut}(\mathcal{A})$ which contains the normal subgroup $\operatorname{Int}(\mathcal{A})$ of inner automorphisms, matching the semidirect product $G = \mathcal{U} \rtimes \operatorname{Diff}(M)$ of Standard-Model gauge transformations with diffeomorphisms. Inner fluctuations of the metric, $D \to D_0 + A + JAJ^{-1}$ with $A = \sum_i a_i[D_0,b_i]$, generate exactly the bosonic gauge and Higgs fields. The product geometry $M\times F$ with $\mathcal{A} = C^\infty(M)\otimes\mathcal{A}_F$, $\mathcal{A}_F = \mathbb{C}\oplus\mathbb{H}\oplus M_3(\mathbb{C})$, and finite-dimensional $\mathcal{H}_F$ labelled by SM fermions, with $D_F$ the Yukawa matrix, reproduces the SM fermion content and couplings; the fermionic action is $\langle\psi,D\psi\rangle$.

**Section 2 (Einstein–Yang–Mills test case).** For $\mathcal{A} = C^\infty(M) \otimes M_N(\mathbb{C})$ with $D = \partial\!\!\!/_M\otimes 1$, inner fluctuations yield an $SU(N)$ Yang–Mills field $A$ (with the $U(1)$ part killed by $A + JAJ^*$). Squaring $D$ produces a Laplace-type operator $P = D^2 = -(g^{\mu\nu}\partial_\mu\partial_\nu \cdot \mathbb{I} + \mathbb{A}^\mu\partial_\mu + \mathbb{B})$ whose heat-kernel expansion uses Seeley–DeWitt coefficients $a_0, a_2, a_4$ with $E = \tfrac14 R\otimes\mathbb{I}_4\otimes\mathbb{I}_N + \tfrac{i}{4}\gamma^{\mu\nu}\otimes g F^i_{\mu\nu} T^i$ and $\Omega_{\mu\nu} = \tfrac14 R^{ab}_{\mu\nu}\gamma_{ab}\otimes\mathbb{1}_N - \tfrac{i}{2}\mathbb{I}_4\otimes g F^i_{\mu\nu} T^i$. The trace $\operatorname{Tr}\chi(D^2/m_0^2) \simeq \sum_n f_n a_n(P)$ with moments $f_0 = \int_0^\infty\chi(u) u\,du$, $f_2 = \int_0^\infty\chi(u)\,du$, $f_{2(n+2)} = (-1)^n\chi^{(n)}(0)$ for $n\ge 0$. Using the Gauss–Bonnet identity and Weyl-tensor decomposition the bosonic bare action becomes
$$I_b = \int d^4x\sqrt{g}\Big[\tfrac{1}{2\kappa_0^2}R + e_0 + a_0 C_{\mu\nu\rho\sigma}C^{\mu\nu\rho\sigma} + c_0 R^*R^* + d_0 R_{;\mu}^{\ \mu} + \tfrac14 F^i_{\mu\nu}F^{\mu\nu i}\Big]$$
with $a_0 = -3N/(80 g_0^2)$, $c_0 = -\tfrac23 a_0$, $d_0 = -\tfrac{11}{3} a_0$, $e_0 = N m_0^4 f_0/(4\pi^2)$. In flat space, the action reduces to $\tfrac14 F^i_{\mu\nu}F^{\mu\nu i} + (\psi, D\psi)$, which has $N=1$ global SUSY (N=2, N=4 from 6D/10D Dirac operators).

**Section 3 (Spectral action for the Standard Model).** The finite geometry has $\mathcal{A}_2 = \mathbb{C}\oplus\mathbb{H}\oplus M_3(\mathbb{C})$ with basis of elementary fermions $Q = (u_L, d_L, d_R, u_R)^T$, $L = (\nu_L, e_L, e_R)^T$ and Dirac operator $D_2 = \operatorname{diag}(Y, \bar Y)$ with Yukawa $Y = Y_q\otimes 1_3 \oplus Y_\ell$ containing $k_0^d, k_0^u, k_0^e$ family mixing matrices and $H_0 = \mu(0,1)^T$, $\tilde H_0 = i\sigma_2 H_0$. After taking inner fluctuations the quark Dirac operator $D_q$ contains the $U(1)$, $SU(2)_w$ and $SU(3)_c$ gauge fields $B_\mu$, $A^\alpha_\mu$, $V^i_\mu$ with bare couplings $g_{01}, g_{02}, g_{03}$, and the Higgs doublet $H$. The computation of the bosonic spectral action gives
$$I = \tfrac{9m_0^4 \cdot (5/4)}{\pi^2} f_0 \int\!\sqrt{g}\, d^4x + \tfrac{3 m_0^2}{4\pi^2} f_2 \int\!\sqrt{g}\big[\tfrac54 R - 2y^2 H^*H\big] d^4x + \tfrac{f_4}{4\pi^2}\int\!\sqrt{g}\big[\ldots + 3y^2(D_\mu H^* D^\mu H - \tfrac16 R H^*H) + g_{03}^2 G^i_{\mu\nu}G^{\mu\nu i} + g_{02}^2 F^\alpha_{\mu\nu}F^{\mu\nu\alpha} + \tfrac53 g_{01}^2 B_{\mu\nu}B^{\mu\nu} + 3 z^2 (H^*H)^2 - y^2 (H^*H)_{;\mu}^{\ \ \mu}\big]$$
with $y^2 = \operatorname{Tr}(|k_0^d|^2 + |k_0^u|^2 + \tfrac13 |k_0^e|^2)$ and $z^2 = \operatorname{Tr}((|k_0^d|^2 + |k_0^u|^2)^2 + \tfrac13 |k_0^e|^4)$.

**Unification at scale $\Lambda$.** Normalising Einstein and Yang–Mills terms gives $15 m_0^2 f_2 /(4\pi^2) = 1/\kappa_0^2$, $g_{03}^2 f_4/\pi^2 = 1$, and the SU(5)-type relation $g_{03}^2 = g_{02}^2 = \tfrac53 g_{01}^2$. After rescaling the Higgs by $H\to (2g_{03}/3)(1/y) H$ one gets a Higgs mass term with $\mu_0^2 = 4/(3\kappa_0^2)$, minimal conformal coupling $\xi_0 = 1/6$, and $\lambda_0 = \tfrac43 g_{03}^2 z^2/y^4$. Running via SU(5)-type RGEs, with PDG values $\alpha_{\mathrm{em}}^{-1}(M_Z) = 128.09$ and $0.110 \le \alpha_3(M_Z) \le 0.123$, one obtains $9.14\times10^{14} \le \Lambda \le 4.44\times10^{14}$ GeV and $0.206 \le \sin^2\theta_w \le 0.210$ (about 10% low vs. experimental 0.2325). Assuming top-Yukawa dominance, the Higgs quartic boundary condition $\lambda(\Lambda) = (16\pi/3)\alpha_3(\Lambda) \simeq 0.402$ plus RG running produces a Higgs mass in the range $160$–$180$ GeV.

**Section 4 (Conclusions).** The spectral action unifies Einstein+Weyl gravity with the full SM action from a single universal formula, at the price of an $R^2$ counterterm appearing on renormalisation (absent in the bare action due to conformal invariance of $a_4$). The $\sim 10\%$ $\sin^2\theta_w$ shortfall and the too-large Newton constant signal that the SM spectrum must be modified between electroweak and unification scales (e.g., supersymmetry, or noncommutative refinements of spacetime itself).

## Key Results

1. Universal action formula $S = \operatorname{Tr}\chi(D/\Lambda) + \langle\psi, D\psi\rangle$.
2. Inner fluctuations of the metric on $M \times F$ reproduce all SM bosons (photon, $W^\pm$, $Z$, 8 gluons, Higgs doublet) and all their couplings.
3. Heat-kernel computation of $\operatorname{Tr}\chi(D^2/\Lambda^2)$ yields Einstein–Hilbert + cosmological + Weyl$^2$ + topological + Yang–Mills + Higgs kinetic + Higgs potential + $-\tfrac16 R|H|^2$ conformal coupling.
4. SU(5)-type boundary condition at $\Lambda$: $\alpha_3(\Lambda) = \alpha_2(\Lambda) = (5/3)\alpha_1(\Lambda)$.
5. Unification scale $\Lambda \sim 10^{15}$ GeV; $\sin^2\theta_w \sim 0.21$ (10% low); Higgs mass $\sim$ 160–180 GeV.
6. Bare cosmological constant relation $e_0 = e + \Lambda^4\cdot 62/(32\pi^2) + \cdots$ where 62 = (fermionic dof 90) $-$ (bosonic dof 28).

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| spectral-action | $\operatorname{Tr}\chi(D/\Lambda) + \langle\psi, D\psi\rangle$ | (1.28) |
| inner-fluct | $D = D_0 + A + JAJ^{-1}$, $A = \sum_i a_i[D_0, b_i]$, $A=A^*$ | (1.23) |
| product-geom | $\mathcal{A} = C^\infty(M)\otimes\mathcal{A}_F$, $\mathcal{A}_F = \mathbb{C}\oplus\mathbb{H}\oplus M_3(\mathbb{C})$, $\mathcal{H} = L^2(M,S)\otimes\mathcal{H}_F$, $D = \partial\!\!\!/_M\otimes 1 + \gamma_5 \otimes D_F$ | (1.16)–(1.19) |
| D-square | $P = D^2 = -(g^{\mu\nu}\partial_\mu\partial_\nu \mathbb{I} + \mathbb{A}^\mu\partial_\mu + \mathbb{B})$ | (2.7) |
| heat-trace | $\operatorname{Tr}\chi(P) \simeq \sum_{n\ge 0} f_n a_n(P)$ | (2.14) |
| moments | $f_0 = \int_0^\infty\chi(u) u\, du$, $f_2 = \int_0^\infty\chi(u)\, du$, $f_{2(n+2)} = (-1)^n \chi^{(n)}(0)$ | (2.15) |
| SDW-coeffs | $a_0 \propto \operatorname{tr}(\mathbb{I})$; $a_2\propto\operatorname{tr}(-R/6\,\mathbb{I} + E)$; $a_4$ is the standard combination with $-12 R_{;\mu}^{\ \mu}+5R^2 -2R_{\mu\nu}R^{\mu\nu}+2R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}$ coefficients plus $E$ and $\Omega_{\mu\nu}\Omega^{\mu\nu}$ terms | (2.16) |
| YM-Einstein | $a_4(P) = \tfrac{N}{48\pi^2}\int d^4x\sqrt{g}\big[-\tfrac{3}{20}C^2 + \tfrac{1}{120}(11 R^*R^* + 12 R_{;\mu}^{\ \ \mu}) + (g^2/N)F^i_{\mu\nu}F^{\mu\nu i}\big]$ | (2.24) |
| bare-consts | $a_0 = -3N/(80 g_0^2)$, $c_0 = -\tfrac23 a_0$, $d_0 = -\tfrac{11}{3}a_0$, $e_0 = N m_0^4 f_0/(4\pi^2)$ | (2.29) |
| GUT-boundary | $\alpha_3(\Lambda) = \alpha_2(\Lambda) = (5/3)\alpha_1(\Lambda)$ | (3.26) |
| sin2-prediction | $\sin^2\theta_w = \tfrac38 [1 - (109/(18\pi))\alpha_{\mathrm{em}}\ln(\Lambda/M_Z)]$, $\ln(\Lambda/M_Z) = (2\pi/67)(3\alpha_{\mathrm{em}}^{-1}(M_Z) - 8\alpha_3^{-1}(M_Z))$ | (3.27) |
| Higgs-BC | $\lambda_0 = (4/3) g_{03}^2 z^2/y^4$; top-dominance limit $\lambda(\Lambda) = (16\pi/3)\alpha_3(\Lambda)$, giving $\lambda_0 \simeq 0.402$ | (3.30)–(3.31) |
| bare-cc | $e_0 = e + \Lambda^4 \cdot 62/(32\pi^2) + \ldots$, $62 = 90 - 28$ (fermionic minus bosonic dof) | (3.23) |
| Higgs-mass-bound | $160 < m_H < 200$ GeV (triviality bound at $\Lambda \simeq 10^{15}$ GeV) | (3.34) |

## Relevance to Phonon-Exflation

This is the founding paper of the spectral action principle on which the entire phonon-exflation framework rests. Every computation of the Standard Model from the Jensen-deformed SU(3) spectral triple uses the Chamseddine–Connes formula $S = \operatorname{Tr}\chi(D/\Lambda) + \langle\psi,D\psi\rangle$ to extract SM gauge couplings, Higgs potential, Einstein–Hilbert + Weyl$^2$ from the Seeley–DeWitt coefficients $a_0$ (cosmological constant / S_fold zero-moment), $a_2$ (Einstein–Hilbert / Newton's constant as second spectral moment — the two-layer-gravity identification in S50–S51 atlas), and $a_4$ (Yang–Mills + Higgs quartic + $-\tfrac16 R|H|^2$). The SU(5)-type boundary condition and the Higgs prediction $160$–$180$ GeV set the precedent for the S42 computation $m_H = 131.8$ GeV from KK-threshold corrections to this framework. Connes (ref [4] here, hep-th/9603053) is the companion paper whose KO-dimension axioms underwrite the 155,984-eigenvalue D_K spectrum.
