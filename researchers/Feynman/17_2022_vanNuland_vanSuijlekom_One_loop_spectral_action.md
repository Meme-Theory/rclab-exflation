# One-loop corrections to the spectral action

**Author(s):** Teun D.H. van Nuland and Walter D. van Suijlekom
**Year:** 2021/2022
**Journal:** (preprint; later published)
**arXiv/DOI:** arXiv:2107.08485v2 [hep-th] (13 Oct 2021)
**Relevance:** CRITICAL

---

## Abstract

We analyze the perturbative quantization of the spectral action in noncommutative geometry and establish its one-loop renormalizability in a generalized sense, while staying within the spectral framework of noncommutative geometry. Our result is based on the perturbative expansion of the spectral action in terms of higher Yang–Mills and Chern–Simons forms. In the spirit of random noncommutative geometries, we consider the path integral over matrix fluctuations around a fixed noncommutative gauge background and show that the corresponding one-loop counterterms are of the same form so that they can be safely subtracted from the spectral action. A crucial role will be played by the appropriate Ward identities, allowing for a fully spectral formulation of the quantum theory at one loop.

---

## Key Arguments and Derivations

**Section 1 (Introduction).** Motivates perturbative quantization of the Chamseddine–Connes spectral action in a way that keeps the output spectral (in the sense of noncommutative geometry), rather than passing to standard field-theoretic renormalization at the cost of losing the spectral organising principle. Background-field method over matrix fluctuations in the spirit of random noncommutative geometries (Barrett–Glaser, Khalkhali–Pagliaroli, Azarfar–Khalkhali). Two main physical settings: hermitian matrix models, and almost-commutative geometries $M\times F$ where $V = a_j \partial\!\!\!/ b_j + \gamma_5 a_j [D_F, b_j]$ splits into Yang–Mills $\mathbb{A}$ and Higgs $\Phi$ pieces.

**Section 2 (Diagrammatic expansion of the spectral action).** Key input from the companion paper [40] (van Nuland–van Suijlekom, "Cyclic cocycles in the spectral action"): the spectral action $\operatorname{Tr} f(D+V) - \operatorname{Tr} f(D)$ expands as $\sum_n (1/n)\langle V,\ldots,V\rangle$ with brackets
$$\langle V_1,\ldots,V_n\rangle = \operatorname{Tr}\oint \frac{dz}{2\pi i} f'(z) V_1 (z-D)^{-1}\cdots V_n(z-D)^{-1}$$
visualised as a one-loop diagram with $n$ external legs. The brackets are cyclic: $\langle V_1,\ldots,V_n\rangle = \langle V_n, V_1,\ldots,V_{n-1}\rangle$. A fundamental Ward identity holds for the fermion propagator:
$$(z-D)^{-1} a - a(z-D)^{-1} = (z-D)^{-1}[D,a](z-D)^{-1}$$
$\Rightarrow \langle aV_1,\ldots,V_n\rangle - \langle V_1,\ldots,V_n a\rangle = \langle [D,a], V_1,\ldots,V_n\rangle$. The brackets are then written as noncommutative integrals $\int_{\phi_n} a^0 da^1\cdots da^n$ over higher Yang–Mills/Chern–Simons forms. Cyclicity + Ward identity $\Rightarrow$
$$S_D[V] = \sum_{k=1}^\infty \Big(\int_{\psi_{2k-1}} \mathrm{cs}_{2k-1}(A) + \frac{1}{2k}\int_{\phi_{2k}} F^k\Big)$$
with higher Chern–Simons forms $\mathrm{cs}_{2k-1}(A) = \int_0^1 A(t\,dA + t^2 A^2)^{k-1} dt$ and curvature $F = dA + A^2$. Here $\phi_{2k}$ are even cyclic cocycles and $\psi_{2k-1}$ odd cyclic cocycles.

**Section 3 (Loop corrections).** Adopts the background-field method: backgrounds are bosonic gauge fields $V = a_j[D,b_j]$, while the path integral is over ensembles of finite $N\times N$ hermitian matrices (the dimension $N$ acts as the regularizing cutoff, sent to $\infty$ at the end). Divided differences $f'[\lambda_k,\lambda_l] = (f'(\lambda_k) - f'(\lambda_l))/(\lambda_k - \lambda_l)$ define the quadratic form; under the technical assumption that $f'[\lambda_k,\lambda_l] > 0$ on the $N$ relevant eigenvalues (positive divided difference) one can do the Gaussian integral directly without ghosts, obtaining propagator $\overline{Q_{kl} Q_{mn}} = \delta_{kn}\delta_{lm} G_{kl}$ with $G_{kl} = 1/f'[\lambda_k,\lambda_l]$ (bounded inverse propagator — a regularising property absent from ordinary local QFT).

**Quantum Ward identity for the gauge propagator** (analogue of the fermion Ward identity) follows directly from divided-difference identities:
$$\overline{Q_{ik}Q_{lm}} a_{mn} - a_{im}\overline{Q_{mk}Q_{ln}} = -\overline{Q_{ik}Q_{rp}} a_{pq}(\lambda_p-\lambda_q)\overline{Q_{qr}Q_{ln}} f'[\lambda_p,\lambda_q,\lambda_r]$$
(diagrammatic form: as in the fermion case but with a sign flip from the closed gauge loop).

**Two-point amplitudes at one loop (Table 1).** Three topologies with two external wavy lines. The first is finite as $N\to\infty$ and is not a counterterm. The second ("fish") has amplitude $\sum_{i,j,k} (V_1)_{ij}(V_2)_{ji} G_{ik} G_{kj} f'[\lambda_i,\lambda_j,\lambda_k]^2$ and is potentially divergent. The third ("seagull") has amplitude $\sum_{i,j,k}(V_1)_{ij}(V_2)_{ji} G_{jk} f'[\lambda_i,\lambda_j,\lambda_j,\lambda_k]$, also potentially divergent. Figure 2 plots summands for explicit $f(x) = (1+ax^2)\Phi(bx)$ on the circle at $N=61$, confirming the slow decay that produces the divergence as $N\to\infty$.

**Section 3.3 (One-loop counterterms).** The quantum Ward identity at $n+1$ legs,
$$\langle\!\langle aV_1,\ldots,V_n\rangle\!\rangle^{1L} - \langle\!\langle V_1,\ldots,V_n a\rangle\!\rangle^{1L} = \langle\!\langle [D,a], V_1,\ldots,V_n\rangle\!\rangle^{1L},$$
together with cyclicity, replicates line-by-line the derivation of the Chern–Simons + Yang–Mills expansion at the classical level. The divergent part of the quantum effective spectral action therefore takes the identical form as the classical expansion:
$$\sum_n \frac{1}{n}\langle\!\langle V,\ldots,V\rangle\!\rangle^{1L}_{\infty} = \sum_{k=1}^\infty\Big(\int_{\widetilde\psi_{2k-1}} \mathrm{cs}_{2k-1}(A) + \frac{1}{2k}\int_{\widetilde\phi_{2k}} F^k\Big).$$
Renormalization at one loop is therefore realised by the shift $\phi \mapsto \phi - \widetilde\phi$, $\psi \mapsto \psi - \widetilde\psi$ in the space of noncommutative (cyclic cocycle) integrals — a purely spectral operation. This establishes one-loop renormalizability in the generalized sense of Gomis–Weinberg [26] (allowing infinitely many counterterms that nonetheless all fit the same structural template).

**Section 4 (Conclusions).** The spectral action becomes a candidate "quantum effective spectral action" (sum of all 1PI diagrams), opening a route to re-derive the physical SM Lagrangian at low energies within the same noncommutative framework, instead of handing off to conventional RG. Extension to higher loops and to noncommutative scalar field theory (Grosse–Wulkenhaar) is flagged for future work.

## Key Results

1. Classical expansion: $S_D[V] = \sum_{k=1}^\infty\big(\int_{\psi_{2k-1}}\mathrm{cs}_{2k-1}(A) + \tfrac{1}{2k}\int_{\phi_{2k}} F^k\big)$ with $F = dA + A^2$.
2. Cyclicity of the bracket $\langle V_1,\ldots,V_n\rangle$ and the fermion Ward identity $\langle aV_1,\ldots\rangle - \langle\ldots V_n a\rangle = \langle [D,a],V_1,\ldots,V_n\rangle$ suffice to produce the Yang–Mills/Chern–Simons form.
3. Bounded gauge propagator $G_{kl} = 1/f'[\lambda_k,\lambda_l]$ under the positivity assumption $f'[\lambda_k,\lambda_l] > 0$.
4. Quantum Ward identity for the gauge propagator obtained from the divided-difference identity for $f'$.
5. One-loop divergent part of the effective spectral action is of the same Chern–Simons/Yang–Mills form, with modified cocycles $\widetilde\phi, \widetilde\psi$. This gives one-loop renormalizability in the generalized sense.
6. The counterterms do not take the theory out of the spectral-action framework — quantization is intrinsic to noncommutative geometry.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| expansion | $S_D[V] = \operatorname{Tr}(f(D+V) - f(D)) = \sum_{n=1}^\infty \frac{1}{n}\langle V,\ldots,V\rangle$ | (1) |
| bracket | $\langle V_1,\ldots,V_n\rangle = \operatorname{Tr}\oint\frac{dz}{2\pi i} f'(z) V_1(z-D)^{-1}\cdots V_n (z-D)^{-1}$ | (2) |
| ward-fermion | $(z-D)^{-1}a - a(z-D)^{-1} = (z-D)^{-1}[D,a](z-D)^{-1}$ | (3) |
| phi-n-integral | $\int_{\phi_n} a^0 da^1\cdots da^n := a^0[D,a^1]\text{-circle with }[D,a^i]$ decorations | (4) |
| one-form | $\langle V\rangle = \int_{\phi_1} A$, $A := a_j db_j$ (universal gauge form) | (5) |
| psi-shift | $\int_{\psi_{2k-1}}\omega = \int_{\phi_{2k-1}}\omega - \tfrac12 \int_{\phi_{2k}} d\omega$ | (6) |
| classical | $S_D[V] = \sum_{k=1}^\infty\big(\int_{\psi_{2k-1}}\mathrm{cs}_{2k-1}(A) + \tfrac{1}{2k}\int_{\phi_{2k}} F^k\big)$ | (7) |
| higher-cs | $\mathrm{cs}_{2k-1}(A) = \int_0^1 A (t\, dA + t^2 A^2)^{k-1}\, dt$ | (8) |
| brackets-mat | $\tfrac12\langle Q,Q\rangle = \tfrac12\sum_{k,l} Q_{kl}Q_{lk} f'[\lambda_k,\lambda_l]$; $\tfrac13\langle Q,Q,Q\rangle = \tfrac13\sum_{k,l,m} Q_{kl}Q_{lm}Q_{mk} f'[\lambda_k,\lambda_l,\lambda_m]$ | §3 |
| propagator | $\overline{Q_{kl} Q_{mn}} = \delta_{kn}\delta_{lm} G_{kl}$, $G_{kl} = 1/f'[\lambda_k,\lambda_l]$ | §3 |
| ward-gauge | $\overline{Q_{ik}Q_{lm}} a_{mn} - a_{im}\overline{Q_{mk}Q_{ln}} = (G_{ik}-G_{nk})\delta_{kl} a_{in}$, reproduced from divided-difference identity $G_{ik}G_{nk}(f'[\lambda_k,\lambda_n] - f'[\lambda_i,\lambda_k])$ | (9) |
| twopt-fish | $\sum_{i,j,k}(V_1)_{ij}(V_2)_{ji} G_{ik} G_{kj} f'[\lambda_i,\lambda_j,\lambda_k]^2$ | (11) |
| twopt-seagull | $\sum_{i,j,k}(V_1)_{ij}(V_2)_{ji} G_{jk} f'[\lambda_i,\lambda_j,\lambda_j,\lambda_k]$ | (12) |
| quantum-ward | $\langle\!\langle V_1,\ldots,aV_j,\ldots,V_n\rangle\!\rangle^{1L} - \langle\!\langle V_1,\ldots,V_{j-1}a,\ldots,V_n\rangle\!\rangle^{1L} = \langle\!\langle V_1,\ldots,V_{j-1},[D,a],V_j,\ldots,V_n\rangle\!\rangle^{1L}$ | §3.3 |
| counterterm | $\sum_n \tfrac1n\langle\!\langle V,\ldots,V\rangle\!\rangle^{1L}_\infty = \sum_{k=1}^\infty\big(\int_{\widetilde\psi_{2k-1}}\mathrm{cs}_{2k-1}(A) + \tfrac{1}{2k}\int_{\widetilde\phi_{2k}} F^k\big)$ | §3.3 |

## Relevance to Phonon-Exflation

This is the only existing construction of a one-loop quantum spectral action that stays within the noncommutative-geometry framework — it is the key reference for Computation C (quantum spectral action on Jensen-deformed SU(3)). It shows that the S36/S42 bare-spectral-action matches to SM can, in principle, be extended to a quantum effective action without losing the spectral organising principle. The bounded inverse propagator $G_{kl} = 1/f'[\lambda_k,\lambda_l]$ is directly applicable to the $L_{\max}=10$, 155,984-eigenvalue spectrum of $D_K$; the positivity assumption on divided differences is a testable condition on the cutoff function $\chi$ used in the computation runs. The higher-Chern–Simons/Yang–Mills form of the counterterms implies that phonon-exflation's S40–S55 post-transit EFT cocycle structure (odd cyclic cocycles $\psi_{2k-1}$ and even $\phi_{2k}$) should be preserved under quantum corrections — directly relevant to the W4 monotonicity wall and the spectral Josephson structure. Cites [38] van Suijlekom's earlier Yang–Mills-sector renormalization of the spectral action.
