# Overview of Seniority Isomers

**Author(s):** Bhoomika Maheshwari, Kosuke Nomura
**Year:** 2022
**Journal:** Preprint (submitted to Elsevier)
**arXiv:** 2212.06258
**Relevance:** MEDIUM

---

## Abstract

Nuclear isomers are the metastable excited states of nuclei. The isomers can be categorized into a few classes including spin, seniority, K, shape and fission isomers depending upon the hindrance mechanisms. In this paper, we aim to present an overview of seniority isomers, which is a category related to the seniority quantum number. The discussion is mainly based on the concepts of seniority and generalized seniority. Various aspects of seniority isomers and their whereabouts have been covered along with the situations where seniority mixing prevents the isomerism.

---

## Key Arguments and Derivations

### Section 2: Quasi-Spin Algebra (Single-j and Multi-j)

Seniority $v$ counts unpaired nucleons (not pair-coupled to $J=0$). The pair creation operator $S^+_j = \sqrt{(2j+1)/2}\, A^+(jj; J=0, M=0)$ and its conjugate $S^-_j$ satisfy SU(2) quasi-spin algebra with $[S^+_j, S^-_j] = \hat{n}_j - \Omega = 2S^0_j$, where $\Omega = (2j+1)/2$ is the pair degeneracy. The pairing Hamiltonian $H_{\mathrm{pair}} = -2G S^+_j S^-_j$ has eigenvalues $-G \frac{n-v}{2}(2\Omega + 2 - n - v)$, with quasi-spin $s = (\Omega - v)/2$.

For odd-tensor single-particle operators (rank $k$ odd): these are quasi-spin scalars, connecting only states with $\Delta v = 0$. Matrix elements are particle-number independent. For even-tensor operators: these are $\kappa = 0$ components of quasi-spin vectors ($s=1$), connecting states with $\Delta v = 0$ or $\Delta v = \pm 2$. The $\Delta v = 0$ matrix elements contain a factor $(\Omega - n)/(\Omega - v)$, producing parabolic behavior in $B(EL)$ that vanishes at mid-shell $n = \Omega$.

### Generalized Seniority (Multi-j)

For multi-j shells, $S^+ = \sum_j (-1)^{l_j} S^+_j$ with the phase factor $(-1)^{l_j}$ crucial for electromagnetic selection rules. In the multi-j case, magnetic transitions are seniority-preserving for both even and odd multipoles (quasi-spin scalars when $l + l' + L$ is odd). Electric transitions exhibit parabolic behavior for both even and odd multipoles ($l + l' + L$ always even for electric). This opens a novel class of odd-electric seniority isomers in multi-j shells, identified in 2016.

### Seniority Reduction Formulae

For $\Delta v = 0$ electric transitions:
$\langle \tilde{j}^n v\, l\, J_f || \sum_i r^L_i Y^L || \tilde{j}^n v\, l'\, J_i \rangle = \frac{\Omega - n}{\Omega - v} \langle \tilde{j}^v v\, l\, J_f || \cdots || \tilde{j}^v v\, l'\, J_i \rangle$

For $\Delta v = 2$ electric transitions:
$\langle \tilde{j}^n v\, l\, J || \cdots || \tilde{j}^n\, v-2,\, l'\, J' \rangle = \sqrt{\frac{(n-v+2)(2\Omega+2-n-v)}{4(\Omega+1-v)}} \langle \tilde{j}^v v || \cdots || \tilde{j}^v\, v-2 \rangle$

### Section 3-4: Seniority Isomers in Various Mass Regions

The paper surveys seniority isomers across the nuclear chart:
- **Ca isotopes** (f$_{7/2}$): 6$^+$ isomers in $^{42}$Ca and $^{46}$Ca; mid-shell $^{44}$Ca lacks isomer due to Berry phase allowing $\Delta v = 4$ mixing
- **Ni isotopes** (g$_{9/2}$): 8$^+$ isomers in $^{70,76}$Ni; absent in $^{72,74}$Ni due to seniority mixing
- **Sn isotopes** (h$_{11/2} \oplus d_{3/2} \oplus s_{1/2}$): 10$^+$ and 27/2$^-$ isomers with half-lives peaking at $N = 73$ (half-filled subshell); generalized seniority with $\Omega = 9$ explains all spectroscopic features
- **Pb isotopes** (i$_{13/2} \oplus f_{7/2} \oplus p_{3/2}$): 12$^+$ isomers; g-factors require GSSM (Generalized Seniority Schmidt Model)
- **N=50, N=82, N=126 isotones**: systematic 8$^+$, 10$^+$ isomers with parabolic B(E2)

Key finding: seniority mixing destroys isomerism at mid-shell when $\Delta v = 4$ interactions lower a competing state (Berry phase effect in $^{44}$Ca, $^{136}$Sn).

## Key Results

1. Seniority quantum number $v$ governs isomerism via cancellation of electric matrix elements at half-filled shells
2. Odd-tensor operators preserve seniority ($\Delta v = 0$); even-tensor operators allow $\Delta v = 0, \pm 2$
3. In multi-j shells, generalized seniority extends all single-j selection rules with phase factor $(-1)^{l_j}$
4. Novel class of odd-electric ($E1, E3, \ldots$) decaying seniority isomers predicted in multi-j shells (2016)
5. Generalized Seniority Schmidt Model (GSSM) explains g-factors without additional fitting
6. Seniority isomers probe effective interactions and shell structure at extreme isospin
7. Berry phase at mid-shell can destroy seniority isomers by enabling $\Delta v = 4$ transitions
8. Energy gap between identical generalized seniority states is particle-number independent

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Pair creation operator | $S^+_j = \sum_{m>0} (-1)^{j-m} a^+_{jm} a^+_{j,-m}$ | Eq. (1) |
| Quasi-spin commutator | $[S^+_j, S^-_j] = \hat{n}_j - \Omega = 2S^0_j$ | Eq. (5) |
| Pairing Hamiltonian | $H_{\mathrm{pair}} = -2G S^+_j S^-_j$ | Eq. (6) |
| Pairing eigenvalues | $E_{\mathrm{pair}}(n,v) = -G \frac{n-v}{2}(2\Omega + 2 - n - v)$ | Eq. (7) |
| Odd-tensor reduction | $\langle j^n v\, l\, J\, M | T^{(k=\mathrm{odd})} | j^n v'\, l'\, J'\, M' \rangle = \langle j^v v\, l\, J\, M | T^{(k=\mathrm{odd})} | j^v v'\, l'\, J'\, M' \rangle \delta_{v,v'}$ | Eq. (9) |
| Even-tensor $\Delta v = 0$ reduction | $\langle j^n v || Y^L || j^n v \rangle = \frac{\Omega - n}{\Omega - v} \langle j^v v || Y^L || j^v v \rangle$ | Eq. (13) |
| Even-tensor $\Delta v = 2$ reduction | $\langle j^n v || Y^L || j^n\, v{-}2 \rangle = \sqrt{\frac{(n-v+2)(2\Omega+2-n-v)}{2(2\Omega+2-2v)}} \langle j^v v || Y^L || j^v\, v{-}2 \rangle$ | Eq. (14) |
| Generalized pair creation | $S^+ = \sum_j (-1)^{l_j} S^+_j$ | Eq. (18) |
| B(EL) in multi-j | $B(EL) = \frac{1}{2J_i+1} |\langle \tilde{j}^n v\, l\, J_f || \sum_i r^L_i Y^L(\theta_i,\phi_i) || \tilde{j}^n v'\, l'\, J_i \rangle|^2$ | Eq. (19) |
| GSSM g-factor | $g = \frac{1}{\tilde{j}}[\frac{1}{2}g_s + (\tilde{j} - \frac{1}{2})g_l]$ for $\tilde{j} = \tilde{l} + 1/2$ | Eq. (24) |
| Energy gap independence | $E(\tilde{j}^n; v{=}2, J) - E(\tilde{j}^n; v{=}0, J{=}0) = \mathrm{constant}$ | Eq. (26) |

## Relevance to Phonon-Exflation

Seniority conservation in the framework's BCS treatment maps directly onto this paper's quasi-spin algebra. The $v = 2$ states correspond to one broken Cooper pair in the Richardson-Gaudin language, and the seniority quantum number is a conserved quantity of the integrable BCS Hamiltonian (S38: 8 conserved Richardson-Gaudin integrals). The parabolic vanishing of $B(EL)$ at half-filling parallels the vanishing of certain matrix elements at the Jensen-symmetry point $[iK_7, D_K] = 0$ (S34). The Berry phase destroying seniority isomers at mid-shell ($^{44}$Ca, $^{136}$Sn) is the nuclear analog of the BDI winding number transition identified in S17c. The GSSM multi-j extension validates extending single-sector seniority arguments to the full multi-representation BCS treatment on SU(3).
