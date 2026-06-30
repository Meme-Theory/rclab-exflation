# On the Origin of Gravity and the Laws of Newton

**Author(s):** Erik Verlinde
**Year:** 2010
**Journal:** JHEP (preprint: arXiv:1001.0785)
**arXiv:** 1001.0785
**Relevance:** MEDIUM

---

## Abstract

Starting from first principles and general assumptions Newton's law of gravitation is shown to arise naturally and unavoidably in a theory in which space is emergent through a holographic scenario. Gravity is explained as an entropic force caused by changes in the information associated with the positions of material bodies. A relativistic generalization of the presented arguments directly leads to the Einstein equations. When space is emergent even Newton's law of inertia needs to be explained. The equivalence principle leads us to conclude that it is actually this law of inertia whose origin is entropic.

---

## Key Arguments and Derivations

### Entropic Force (Sec. 2)

An entropic force arises in any system where a macroscopic variable (position) has a conjugate entropy gradient. The force is:
$$F \Delta x = T \Delta S$$

### Holographic Screens and Entropy (Sec. 3.1)

A holographic screen stores information about matter on one side. When a particle of mass $m$ approaches the screen by one Compton wavelength $\Delta x = \hbar/(mc)$, the entropy change is:
$$\Delta S = 2\pi k_B$$

This specific entropy change is chosen to reproduce the second law of Newton via the Unruh temperature.

### Newton's Second Law (Sec. 3.1)

Using the Unruh temperature $k_B T = \frac{\hbar a}{2\pi c}$ for a screen experiencing acceleration $a$, combined with $F\Delta x = T\Delta S$ and $\Delta S = 2\pi k_B \frac{mc\Delta x}{\hbar}$:
$$F = ma$$

### Newton's Law of Gravity (Sec. 3.2)

For a closed spherical screen of area $A = 4\pi R^2$, the number of bits on the screen is $N = A c^3/(G\hbar)$. Using the equipartition rule:
$$E = \frac{1}{2}N k_B T$$
with $E = Mc^2$ and the entropy postulate:
$$F = \frac{GMm}{R^2}$$

Newton's law of gravitation is recovered from holographic thermodynamics.

### Relativistic Generalization (Secs. 4-5)

The argument generalizes to curved spacetime. For a general timelike Killing vector $\xi^a$ with redshift $e^\Phi = \sqrt{-\xi^a\xi_a}$:
- Temperature: $T = \frac{\hbar}{2\pi k_B}\frac{e^\Phi N^a \nabla_a e^{-\Phi}}{c}$ (Tolman-Unruh)
- Entropy postulate: $\nabla_a S = 2\pi \frac{mc}{\hbar} N_a$
- Entropic force: $F_a = T\nabla_a S = me^\Phi \nabla_a \Phi$ (correct relativistic gravitational force)

The Einstein equations are derived from the first law of thermodynamics applied to screens:
$$\delta Q = T dS \quad \Rightarrow \quad R_{ab} - \frac{1}{2}g_{ab}R + \Lambda g_{ab} = 8\pi G\,T_{ab}$$

### The End of Gravity as a Fundamental Force (Sec. 6.1)

Verlinde argues that gravity is not fundamental but emergent: "It is time we not only notice the analogy, and talk about the similarity, but finally do away with gravity as a fundamental force."

---

## Key Results

1. Newton's law $F = ma$ derived from Unruh temperature + entropy postulate on holographic screens
2. Newton's gravitational law $F = GMm/R^2$ derived from holographic screen area + equipartition
3. Einstein equations derived from the first law of thermodynamics on general holographic screens
4. Gravity is an entropic force: $F\Delta x = T\Delta S$
5. The cosmological constant $\Lambda$ appears naturally in the relativistic derivation
6. Space and gravity are both emergent from the same holographic information dynamics

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Entropic force | $F\Delta x = T\Delta S$ | Sec. 2 |
| Entropy postulate | $\Delta S = 2\pi k_B \frac{mc}{\hbar}\Delta x$ | Eq. (3.6) |
| Unruh temperature | $k_B T = \frac{\hbar a}{2\pi c}$ | Eq. (3.8) |
| Equipartition | $E = \frac{1}{2}N k_B T$ | Eq. (3.11) |
| Newton's gravity | $F = \frac{GMm}{R^2}$ | Eq. (3.13) |
| Relativistic force | $F_a = m e^\Phi \nabla_a \Phi$ | Eq. (5.30) |

## Relevance to Phonon-Exflation

Verlinde's entropic gravity proposal is structurally consistent with the phonon-exflation framework's spectral action = free energy picture. In the framework, the spectral action functional plays the role of a thermodynamic free energy, and geometric changes (tau evolution, compactification) are driven by entropy considerations of the underlying many-body system. The entropic force $F\Delta x = T\Delta S$ maps onto the spectral action gradient that drives the geometry through the fold. However, the framework goes further than Verlinde by specifying the microscopic degrees of freedom (phononic excitations of M4 x SU(3)) rather than leaving them abstract.
