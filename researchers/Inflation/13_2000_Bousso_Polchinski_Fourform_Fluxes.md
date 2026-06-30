# Quantization of Four-form Fluxes and Dynamical Neutralization of the Cosmological Constant

**Author(s):** Raphael Bousso, Joseph Polchinski
**Year:** 2000
**Journal:** JHEP 0006:006,2000 (SU-ITP-00-12, NSF-ITP-00-40)
**arXiv:** hep-th/0004134
**Relevance:** CRITICAL — for a project studying phonon-exflation cosmology where the CC overshoot is the key open problem

---

## Abstract

A four-form gauge flux makes a variable contribution to the cosmological constant. This has often been assumed to take continuous values, but we argue that it has a generalized Dirac quantization condition. For a single flux the steps are much larger than the observational limit, but we show that with multiple fluxes the allowed values can form a sufficiently dense 'discretuum'. Multiple fluxes generally arise in M theory compactifications on manifolds with non-trivial three-cycles. In theories with large extra dimensions a few four-forms suffice; otherwise of order 100 are needed. Starting from generic initial conditions, the repeated nucleation of membranes dynamically generates regions with $\lambda$ in the observational range. Entropy and density perturbations can be produced.

---

## Key Arguments and Derivations

### Section 1: Introduction

Three mechanisms by which the CC becomes a dynamical variable:
1. A four-form field strength $F_4$ (equation of motion requires it be constant, no local dynamics, but contributes positive energy density that can cancel a negative bare CC).
2. Spacetime topology fluctuations (wormholes) converting all constants into dynamical variables.
3. Naked singularities in compactified dimensions with undetermined boundary conditions.

The paper focuses on the four-form mechanism. Key new point: the four-form field strength is quantized (generalized Dirac quantization condition), ruling out continuous cancellation of the bare CC. However, with multiple four-forms from M-theory compactifications, the allowed values form a dense "discretuum."

### Section 2: Four-form Quantization

**2.1 Four-form energetics**: The action for gravity with bare vacuum energy plus four-form kinetic term is given with $F_4 = dA_3$. On shell, $F^{\mu\nu\rho\sigma} = c\,\epsilon^{\mu\nu\rho\sigma}$ where $c$ is constant, giving $F_4^2 = -24c^2$. The effective cosmological constant is $\lambda = \lambda_{\text{bare}} + Zc^2/2$, where $Z$ is the kinetic normalization. Only $\lambda$ is observable -- $\lambda_{\text{bare}}$ and the four-form cannot be observed separately.

**2.2 Four-form quantization**: The generalized Dirac quantization condition requires $\int_X F_4 = 2\pi n/e$ for $n \in \mathbb{Z}$, arising from single-valuedness of membrane amplitudes (membranes couple to $A_3$ with charge $e$). Across a membrane the value of $c$ jumps by $\Delta c = e/Z$. The actual value of $c$ is quantized: $c = en/Z$ for $n \in \mathbb{Z}$. This follows from quantization of the dual zero-form $*F_4 = F_0$. When the 4D theory is embedded in M-theory (compactification on seven-manifold $K$), the 11D action gives $F_0 = n/(M_{11}^6 V_7)$ with $e = 2\pi M_{11}^3$ (M2-brane tension).

**2.3 Discussion -- The "gap problem"**: For a single four-form, the step size $d\lambda/dn = 2ne^2/Z$ is enormously larger than the observational bound. The final value of $\lambda$ lies within bounds only if $e|\lambda_{\text{bare}}|^{1/2}Z^{-1/2} < 10^{-120}\kappa_4^{-4}$. Even in the large-dimension scenario (TeV-scale $M_{11}$), the step size is $10^{-75}\kappa_4^{-4}$ -- far too large. This is the "gap problem" of Brown-Teitelboim.

**2.4 Multiple four-forms -- The discretuum**: With $J$ four-form fluxes, $\lambda = \lambda_{\text{bare}} + \frac{1}{2}\sum_{i=1}^J n_i^2 q_i^2$. The problem reduces to finding grid points $(n_1, \ldots, n_J)$ sufficiently close to a $(J-1)$-sphere of radius $|2\lambda_{\text{bare}}|^{1/2}$ in a $J$-dimensional lattice with spacings $q_i$. The typical minimum spacing in the CC spectrum is $\Delta\lambda_{\min} = D\prod q_i / (\omega_{J-1}|2\lambda_{\text{bare}}|^{J/2 - 1})$, where $D$ is the degeneracy. For $J \sim 100$ with charges $q_i^{1/2} \sim 1/6$ (in Planck units), the discretuum is sufficiently dense. Crucially, the $q_i$ need not be exceedingly small if $J > 2$; for fixed charges, cancellation actually becomes easier with larger $|\lambda_{\text{bare}}|$.

**2.5 M-theory compactification**: On a seven-manifold $K$ with $N_3$ nontrivial three-cycles, the total number of fluxes is $J = N_3 + 1$. For a seven-torus, $N_3 = \binom{7}{3} = 35$. The charges are $q_i = (2\pi)^{1/2}M_{11}^{3/2}V_{3,i}/V_7^{1/2}$ for wrapped fluxes, and $q_i^2 = 2\kappa_4^2 \tau_i^2$ in general.

**2.6 Small charges from large dimensions**: In the large extra dimension scenario ($M_{11} \sim$ TeV), the gauge hierarchy produces small membrane charges. With $J' = 4$ four-forms, the condition $(2^{-1/2}\kappa_4 M_{11})^{J'+4} \lesssim 10^{-120}\omega_{J'-1}/(\pi D)$ is satisfied. This reduces both the gauge hierarchy problem and the CC problem to the single problem of stabilizing large radii.

### Section 3: Cosmology

**3.1 Brown-Teitelboim mechanism generalized**: Starting from $\lambda_{\text{bare}} < 0$ and $n$ large so $\lambda > 0$, de Sitter space nucleates membrane bubbles. Inside each bubble, $n$ decreases by 1, lowering $\lambda$. With multiple four-forms, this becomes diffusion through a $J$-dimensional grid. Every grid point with $\lambda > 0$ is populated via many paths, including those with $\lambda$ in the observational range. Membrane nucleation to increase $n$ is vastly suppressed and can be neglected.

**3.2 The empty universe problem**: Membrane nucleation is highly suppressed and takes exponentially long, so all fields reach their vacua and particles are diluted away. Two solutions are proposed:
- **Kicking the inflaton** (GUT scale): The Gibbons-Hawking temperature $T = H/(2\pi)$ of pre-final de Sitter space induces Brownian motion of the inflaton. For $M_{11}/M_{\text{Pl}} \gtrsim 10^{-1.3}$ (unification at $10^{17}$ GeV or higher), the random walk displaces the inflaton sufficiently to produce 60 e-foldings after the final membrane nucleation.
- **Trapping the inflaton** (low scale): If the inflaton potential has a false vacuum, Coleman-De Lucia tunnelling after $\lambda \approx 0$ is reached drives inflation and reheating.

**3.3 Vacuum selection**: The Weinberg window $-10^{-120}M_{\text{Pl}}^4 < \lambda < 10^{-118}M_{\text{Pl}}^4$ selects regions where structure (galaxies) can form. Anthropic selection applies in the weakest sense: different regions have different CC values, and observers exist only where the CC is small.

**3.4 Stability**: The tunnelling action for membrane nucleation from a $\lambda \approx 0$ vacuum is $B \approx 27\pi^{3/2}J^{3/2}/(16\sqrt{2}(M_{11}/M_{\text{Pl}})^3)$. In the large dimension case $B \sim 10^{46}$; in the Witten GUT scenario $B \sim 10^8$. Tunnelling is negligible in both cases. Vacuum stability requires $M_{11}/M_{\text{Pl}} < 0.6$.

### Section 4: Conclusions

The mechanism simultaneously addresses both "Why is the CC not huge?" and "Why is the CC not zero?" A residual CC is inevitable due to flux quantization, naturally explaining the small but nonzero observed value. The main unsolved problem is moduli stabilization.

## Key Results

1. Four-form field strengths in 4D have a generalized Dirac quantization condition $F_0 = en/Z$ ($n \in \mathbb{Z}$), ruling out continuous cancellation of the bare CC.
2. A single four-form has steps far too large to achieve the observed CC (the "gap problem"). Even in the large-dimension scenario the step size is $10^{-75}\kappa_4^{-4}$ vs. the required $10^{-120}\kappa_4^{-4}$.
3. Multiple four-forms with incommensurate charges form a dense "discretuum" of CC values. With $J \sim 100$ fluxes and charges $q_i^{1/2} \sim 1/6$ (Planck units), the spectrum is dense enough. With large extra dimensions, $J' = 4$ suffices.
4. The Brown-Teitelboim membrane nucleation mechanism, generalized to multiple four-forms, dynamically populates the discretuum starting from generic initial conditions.
5. The Weinberg anthropic window selects regions with small CC; the observed $\lambda \approx 10^{-120}M_{\text{Pl}}^4$ is natural within this framework.
6. The $\lambda \approx 0$ vacuum is stable against tunnelling ($B \sim 10^{46}$ for large dimensions, $B \sim 10^8$ for GUT scale).
7. The empty universe problem is solved either by de Sitter thermal kicks to the inflaton (GUT scale) or by trapping in a false vacuum (low scale).

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Four-form + gravity action | $S = \int d^4x\sqrt{-g}\left(\frac{1}{2\kappa_4^2}R - \lambda_{\text{bare}} - \frac{Z}{2\cdot 4!}F_4^2\right) + S_{\text{branes}}$ | Eq. (2.1) |
| On-shell four-form | $F^{\mu\nu\rho\sigma} = c\,\epsilon^{\mu\nu\rho\sigma}$ | Eq. (2.4) |
| Effective CC | $\lambda = \lambda_{\text{bare}} + \frac{Zc^2}{2}$ | Eq. (2.5) |
| Dirac quantization | $\int_X \mathbf{F_4} = \frac{2\pi n}{e},\quad n \in \mathbb{Z}$ | Eq. (2.6) |
| Membrane charge jump | $\Delta c = \frac{e}{Z}$ | Eq. (2.8) |
| Flux quantization | $c = \frac{en}{Z},\quad n \in \mathbb{Z}$ | Eq. (2.9) |
| Zero-form quantization | $\mathbf{F_0} = \frac{en}{Z},\quad n \in \mathbb{Z}$ | Eq. (2.11) |
| 11D M-theory action | $S = 2\pi M_{11}^9\int d^{11}X\sqrt{-g_{11}}\left(R - \frac{1}{2\cdot 4!}F_4^2\right) + S_{\text{branes}}$ | Eq. (2.12) |
| 4D flux quantization from M-theory | $F_0 = \frac{n}{M_{11}^6 V_7},\quad n \in \mathbb{Z}$ | Eq. (2.17) |
| Gap problem bound | $e|\lambda_{\text{bare}}|^{1/2}Z^{-1/2} < 10^{-120}\kappa_4^{-4}$ | Eq. (2.19) |
| Multiple four-form CC | $\lambda = \lambda_{\text{bare}} + \frac{1}{2}\sum_{i=1}^J n_i^2 q_i^2$ | Eq. (2.21) |
| Discretuum density condition | $\frac{D}{\omega_{J-1}}\prod_{i=1}^J \frac{q_i}{\lvert 2\lambda_{\text{bare}}\rvert^{1/2}} \lesssim \frac{\Delta\lambda}{\lvert 2\lambda_{\text{bare}}\rvert}$ | Eq. (2.25) |
| Minimum CC spacing | $\Delta\lambda_{\min} = \frac{D\prod_{i=1}^J q_i}{\omega_{J-1}\lvert 2\lambda_{\text{bare}}\rvert^{J/2-1}}$ | Eq. (2.26) |
| Effective CC with inflaton | $\lambda_{\text{eff}}(\phi) = \lambda_{\text{bare}} + \frac{1}{2}\sum_{i=1}^J n_i^2 q_i^2 + V(\phi)$ | Eq. (3.2) |
| Gibbons-Hawking temperature | $T(\phi) = \frac{H(\phi)}{2\pi}$ | Eq. (3.4) |
| Weinberg window | $-10^{-120}M_{\text{Pl}}^4 < \lambda < 10^{-118}M_{\text{Pl}}^4$ | Eq. (3.13) |
| Tunnelling action (large $n_j$) | $B = \frac{27\pi^2}{2(n_j - 1/2)^3(2M_{\text{Pl}}^{-2}q_j)^2}$ | Eq. (3.15) |
| Tunnelling action estimate | $B \approx \frac{27\pi^{3/2}J^{3/2}}{16\sqrt{2}(M_{11}/M_{\text{Pl}})^3}$ | Eq. (3.17) |

## Relevance to Phonon-Exflation

The Bousso-Polchinski discretuum provides the canonical string-landscape approach to the CC problem -- the same problem that the phonon-exflation framework faces as its key open challenge (DILUTION-CC). The spectral action on the $M^4 \times K$ spectral triple produces vacuum energy as the zeroth Seeley-DeWitt coefficient $a_0$, which overshoots by ~120 OOM. The BP approach requires ~$10^{100}$ or more vacua from multiple flux sectors to land near the observed CC by statistical accident (anthropic selection). By contrast, the spectral triple formalism has a SINGLE internal geometry -- the Jensen-deformed SU(3) fiber -- with no landscape of vacua. The CC ($a_0$) and gravity ($a_2$) are different spectral moments of the same Dirac operator, structurally linked rather than independently tunable. This means the exflation framework CANNOT use the BP discretuum mechanism: there is no analog of multiple incommensurate four-form fluxes. Instead, the CC dilution must emerge from a structural mechanism within the single spectral triple -- either through the tau-dependent spectral reorganization at the fold, or through the effacement/impedance mismatch channel. The BP paper thus sharpens what any non-landscape CC solution must accomplish: it must explain the 120 OOM cancellation without access to $10^{100}$ vacua.
