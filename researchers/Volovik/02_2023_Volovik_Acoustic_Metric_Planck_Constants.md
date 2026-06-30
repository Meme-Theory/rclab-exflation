# Acoustic metric and Planck constants

**Author(s):** G.E. Volovik
**Year:** 2023
**Journal:** [INCOMPLETE - not extractable from PDF]
**arXiv:** 2302.08894
**Relevance:** HIGH

---

## Abstract

Based on Akama-Diakonov (AD) theory of emergent tetrads, it was suggested that one can introduce two Planck constants, hbar and h-bar, which are the parameters of the corresponding components of Minkowski metric, g^{Mink}_{mu nu} = diag(-hbar^2, h-bar^2, h-bar^2, h-bar^2). In the AD theory, the interval ds is dimensionless, as a result the metric elements and thus the Planck constants have nonzero dimensions. The Planck constant hbar has dimension of time, and the Planck constant h-bar has dimension of length. It is natural to compare h-bar with the Planck length l_P. However, this connection remains an open question, because the microscopic (trans-Planckian) physics of the quantum vacuum is not known. Here we study this question using the effective gravity emerging for sound wave quanta (phonons) in superfluid Bose liquid, where the microscopic physics is known, and the elements of the effective acoustic metric are determined by the parameters of the Bose liquid. Since the acoustic interval is dimensionless, one may introduce the effective "acoustic Planck constants". The acoustic Planck constant h-bar_ac has dimension of length and is on the order of the interatomic distance. This supports the scenario in which h-bar ~ l_P. We also use the acoustic metric for consideration of dependence of hbar on the Hubble parameter in expanding Universe.

---

## Key Arguments and Derivations

### I. Dimensionless Physics

In the Akama-Diakonov theory of quantum gravity, the fundamental objects are fermionic fields and spin connection gauge fields. Gravitational tetrads emerge as vacuum expectation values of bilinear combinations of fermionic field operators:

E^a_mu = <E-hat^a_mu>, where E-hat^a_mu = (1/2)(Psi-dagger gamma^a partial_mu Psi - Psi-dagger partial_mu gamma^a Psi)

The metric becomes g_{mu nu} = eta_{ab} E^a_mu E^b_nu. The tetrads have dimensions [E^a_0] = 1/[t] and [E^a_i] = 1/[L], making the interval ds dimensionless. All diffeomorphism invariant quantities become dimensionless: action S, cosmological constant Lambda, Hawking temperature, scalar curvature R, particle masses M, etc.

### II. Two Planck Constants as Elements of Minkowski Metric

The non-relativistic wave equation in Minkowski space takes the form of the Schrodinger equation with TWO distinct Planck constants:

i hbar partial_t psi = -(h-bar^2 / 2M) nabla^2 psi

where sqrt(-g^{00}_{Mink}) = hbar (dimension of time) and g^{ik}_{Mink} = h-bar^2 delta^{ik} (dimension of length squared). The Planck length l_P = sqrt(h-bar * G), and since both h-bar and G have dimension of length, the natural suggestion is h-bar ~ l_P.

### III. Acoustic Planck Constants

For phonons in superfluid 4He, the acoustic action is:

S_ph = (m/2hbar) integral d^3x dt n [(nabla Phi)^2 - (1/s^2)(Phi-dot - v . nabla Phi)^2]

The corresponding acoustic Minkowski metric at v=0 is:

g^{00} = hbar n s / m, g^{ik} = (hbar n / ms) delta^{ik}

The effective acoustic Planck constants are:

hbar_ac^2 = m/(hbar n s), h-bar_ac^2 = m s/(hbar n)

These satisfy [hbar_ac] = [t] and [h-bar_ac] = [L].

### IV. UV Length Scale Connection

The acoustic h-bar_ac ~ interatomic distance a = n^{-1/3}. For the idealized quantum liquid where all UV scales coincide (m s a = hbar), one gets h-bar_ac = a exactly. This supports the conjecture that in the relativistic quantum vacuum, h-bar ~ l_P.

### V. Variation of Planck Constants in Expanding Universe

In de Sitter expansion, the vacuum pressure causes deviations from vacuum values:

Delta(h-bar)/h-bar ~ Delta(hbar)/hbar ~ hbar^2 H^2 ~ T^2_GH << 1

The Planck constants are effectively constant throughout the history of expansion, unlike many varying-speed-of-light theories.

---

## Key Results

1. The Akama-Diakonov theory naturally leads to two distinct Planck constants: hbar (dimension time) and h-bar (dimension length)
2. Both appear as elements of the Minkowski metric in dimensionless physics
3. The acoustic analog in superfluid 4He gives h-bar_ac ~ interatomic distance a
4. This supports h-bar ~ l_P in relativistic vacuum
5. In expanding Universe, corrections to Planck constants are proportional to T^2_GH, negligibly small
6. The Tolman temperature for phonons T_0 coincides with the background liquid temperature expressed as frequency
7. Hawking temperature T_0 = v'/(2pi) is the same in both microscopic and macroscopic descriptions

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Two Planck constants | $\sqrt{-g^{00}_{\text{Mink}}} = \hbar,\quad g^{ik}_{\text{Mink}} = \bar{h}^2\delta^{ik}$ | Eq.(5) |
| Acoustic action | $S_{\text{ph}} = \frac{m}{2\hbar}\int d^3x\,dt\,n\left[(\nabla\Phi)^2 - \frac{1}{s^2}(\dot\Phi - \mathbf{v}\cdot\nabla\Phi)^2\right]$ | Eq.(7) |
| Acoustic interval | $ds^2 = \frac{\hbar n}{ms}\left[-s^2 dt^2 + (dx^i - v^i dt)\delta_{ij}(dx^j - v^j dt)\right]$ | Eq.(8) |
| Acoustic Planck constants | $\hbar_{\text{ac}}^2 = \frac{m}{\hbar n s},\quad \bar{h}_{\text{ac}}^2 = \frac{ms}{\hbar n}$ | Eq.(15) |
| Tolman law | $T(\mathbf{r}) = \frac{T_0}{\sqrt{-g_{00}(\mathbf{r})}}$ | Eq.(16) |
| Hawking temperature | $T_0 = \frac{v'}{2\pi}$ | Eq.(18) |
| de Sitter interval (PG form) | $ds^2 = -\frac{1}{\hbar^2}dt^2 + \frac{1}{\bar{h}^2}\left[(dr - Hr\,dt)^2 + r^2 d\Omega^2\right]$ | Eq.(23) |
| Variation with expansion | $\frac{\Delta\bar{h}}{\bar{h}} \sim \frac{\Delta\hbar}{\hbar} \sim \hbar^2 H^2 \sim T_{\text{GH}}^2 \ll 1$ | Eq.(25) |

---

## Relevance to Phonon-Exflation

1. **Dimensionless physics and emergent tetrads**: The Akama-Diakonov framework where tetrads emerge from fermionic bilinears is closely related to the framework's emergent vierbein from the Dirac operator on SU(3). The dimensionless interval ds parallels the framework's use of the spectral action where the Dirac operator eigenvalues are the fundamental objects.

2. **Acoustic Planck constants as UV probe**: The identification h-bar_ac ~ interatomic distance establishes that the effective Planck scale of the emergent theory is set by the UV structure of the underlying medium. In the phonon-exflation framework, the "Planck scale" is set by the SU(3) fiber geometry, not by fundamental constants.

3. **Stability of constants during expansion**: The result that Planck constants vary only as T^2_GH during de Sitter expansion supports the framework's assumption that the geometric parameters of M4 x SU(3) are effectively constant during the post-transit evolution.

4. **Two-world structure**: The connection between microscopic (atomic) and macroscopic (phononic) physics through the Tolman law parallels the framework's two-level description: microscopic (full M4 x SU(3) Dirac spectrum) and macroscopic (effective 4D physics).
