# Equations of Motion for Compact Binary Systems in General Relativity: Do They Depend on the Bodies' Internal Structure at the Third Post-Newtonian Order?

**Author(s):** Clifford M. Will
**Year:** 2025
**Journal:** [INCOMPLETE - not extractable from PDF; arXiv preprint]
**arXiv:** 2503.03189
**Relevance:** HIGH

---

## Abstract

We present and discuss the possibility, derived from work carried out 20 years ago, that the equations of motion for compact binary neutron stars at the third post-Newtonian (3PN) order in general relativity might actually depend on the internal structure of the bodies. These effects involve integrals over the density and internal gravitational potentials of the bodies that are independent of the mass and radius of the bodies, but dependent on their equations of state. These effects could alter the coefficients in the 3PN equations derived using "point mass" methods by as much as 100 percent. They were found in independent calculations done at Washington University using the Direct Integration of the Relaxed Einstein Equations (DIRE) approach, and at the Institut d'Astrophysique de Paris using the Multipolar post-Minkowskian (MPPM) approach. Neither calculation was completed because of the enormous complexity of the algebraic computations and the limitations of software of the day (Maple, Mathematica), and because of an assumption that the effects would somehow cancel or be removable by some transformation. This assumption was rooted in the Strong Equivalence Principle (SEP), which would suppress such effects up to the stage where tidal interactions become important, effectively 5PN order for compact bodies. SEP was well supported at lower PN orders and in special examples. We argue that this assumption needs to be verified by actual calculations. If the results show that these structure-dependent terms exactly cancel or can be absorbed into renormalized masses or shifted positions of each body, this would provide remarkable support for the Strong Equivalence Principle of general relativity. But if they do not cancel and are not incorporated into gravitational waveforms, they could severely impact efforts using next-generation gravitational-wave interferometers to extract information about the equation of state for neutron star matter from gravitational-wave signals from binary neutron star or black hole-neutron star mergers.

---

## Key Arguments and Derivations

### 1. The DIRE Method

The DIRE (Direct Integration of the Relaxed Einstein Equations) approach defines the field $h^{\alpha\beta} \equiv \eta^{\alpha\beta} - (-g)^{1/2}g^{\alpha\beta}$. In harmonic coordinates, Einstein's equations become:
$$\Box h^{\alpha\beta} = -16\pi\tau^{\alpha\beta}$$
where $\tau^{\alpha\beta}$ includes the material stress-energy $T^{\alpha\beta}$, the Landau-Lifshitz pseudotensor, and the "harmonic" pseudotensor. The formal solution is an integral over the past null cone.

Unlike point-mass methods, DIRE treats each body as a finite ball of self-gravitating fluid of characteristic size $s$, expands fields about each body's center of mass in powers of $s$, and: (i) discards terms scaling as negative powers of $s$ (self-energy corrections, analogous to "infinities" in dimensional regularization), (ii) discards terms scaling as positive powers of $s$ (smaller as body shrinks), (iii) retains terms scaling as $s^0$.

### 2. The Zoo of Post-Newtonian Potentials

At increasing PN order, increasingly complex multi-point potentials appear:
- **Two-point potentials** (Newtonian through 3PN): $\Sigma(f) = \int \rho^*(t,x')f(t,x')/|x - x'|\,d^3x'$
- **Triangle (three-point) potentials** (from 2PN): $G(A,B,C) = (4\pi)^{-1}\int d^3x'/|x_A - x'||x_B - x'||x_C - x'|$
- **Quadrangle (four-point) potentials** (from 2PN): $H(A,B;C,D)$ involving double integrals with no known analytic form
- At 3PN: additional **triangle superpotentials** $F(A,B;C)$, **quadrangle potentials** $J(A,B,C,D)$, $K(A,B;C;D)$, $L(A,B;C,D)$, and **megasuperpotentials** $Z(f)$

### 3. Structure-Dependent Terms at 3PN Order

The key finding: at 3PN order, non-linear combinations of potentials produce terms that scale as $s^0$ -- independent of the body's size but dependent on its internal density distribution and equation of state.

Mechanism: The potential from a companion body, expanded in a multipolar series about the center of mass of the body under study (positive powers of $s$), is multiplied by a "self-energy" potential of that body (negative powers of $s$). The product can yield terms independent of $s$ but dependent on internal structure.

At 1PN: these terms cannot appear (gravity not sufficiently non-linear).
At 2PN: such terms could appear but vanish identically by a subtler symmetry.
At 3PN: the cancellation no longer occurs.

### 4. Structure Coefficients

By the time the DIRE project was paused in 2004, 40 distinct "structure coefficients" had been identified (Table I in the paper). These are dimensionless integrals over the density and internal gravitational potentials of each body. They are independent of mass and radius but depend on the equation of state. Examples include:
$$\Lambda_1 = \frac{4\pi}{m} \int_0^R \rho r^2 U_{\text{int}}(r)\,dr$$
$$\Lambda_2 = \frac{4\pi}{m} \int_0^R \rho r^2 U_{\text{int}}^2(r)\,dr$$

Numerical evaluation for various neutron star equations of state (SLy, APR, BSK21, WFF1, GM1, soft polytrope, incompressible fluid, and Newtonian polytropes $n = 0, 1, 3$) shows these coefficients range from $\sim 0.3$ to $\sim 1.5$ and vary significantly with EOS.

### 5. The Unresolved Question

The MPPM group (Blanchet, Esposito-Farese) independently found the same structure-dependent terms but conjectured they would be eliminated by a coordinate transformation. The Itoh-Futamase "Strong-Field Point-Particle Limit" approach appeared to give structure-independent 3PN equations, but their method took the point-particle limit ($\epsilon \to 0$), which may suppress or overlook the finite-size structure effects.

The paper argues this assumption must be verified by explicit calculation. If the structure-dependent terms exactly cancel, it would be "remarkable support for the Strong Equivalence Principle." If they do not, next-generation interferometers (Einstein Telescope, Cosmic Explorer) attempting to extract the nuclear equation of state from gravitational wave signals could be severely impacted.

---

## Key Results

1. 40 distinct structure-dependent coefficients identified at 3PN order in the DIRE approach.
2. Coefficients are dimensionless integrals over body density and internal potentials, independent of mass/radius but EOS-dependent.
3. Could alter 3PN waveform coefficients by up to 100%.
4. At 1PN and 2PN: structure-dependent terms vanish (SEP verified). At 3PN: cancellation not proven.
5. Complete continuum equations of motion through 3PN displayed for the first time (Appendix A).
6. Numerical values of key structure coefficients computed for 10 different NS equations of state.
7. If not cancelled, these effects would appear two PN orders earlier than conventional tidal effects (3PN vs 5PN).

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Relaxed Einstein equations | $\Box h^{\alpha\beta} = -16\pi\tau^{\alpha\beta}$ | Eq. (2.1) |
| Formal solution | $h^{\alpha\beta}(t,\mathbf{x}) = 4\int_C \tau^{\alpha\beta}(t - |\mathbf{x} - \mathbf{x}'|, \mathbf{x}')/|\mathbf{x} - \mathbf{x}'|\,d^3x'$ | Eq. (2.2) |
| Near-zone expansion | $h_N^{\alpha\beta}(t,\mathbf{x}) = 4\sum_{m=0}^\infty \frac{1}{m!}\frac{\partial^m}{\partial t^m}\int_M \tau^{\alpha\beta}(t,\mathbf{x}')|\mathbf{x} - \mathbf{x}'|^{m-1}\,d^3x'$ | Eq. (2.3) |
| Continuum EOM | $dv^i/dt = U_{,i} + a^i_{\text{PN}} + a^i_{\text{2PN}} + a^i_{\text{2.5PN}} + a^i_{\text{3PN}} + a^i_{\text{3.5PN}}$ | Eq. (2.9) |
| Triangle potential | $G(A,B,C) = -\ln\Delta(ABC) + 1$, $\Delta(ABC) = |x_A - x_B| + |x_A - x_C| + |x_B - x_C|$ | Eqs. (2.15)-(2.16) |
| Quadrangle potential | $H(A,B;C,D) = (4\pi)^{-2}\int\int \frac{d^3x'\,d^3x''}{|x' - x''| \cdot |x_A - x'||x_B - x'||x_C - x''||x_D - x''}$ | Eq. (2.18) |
| Structure coefficient $\Lambda_1$ | $\Lambda_1 = (4\pi/m)\int_0^R \rho r^2 U_{\text{int}}(r)\,dr$ | Sec. III |
| Body acceleration | $a_A^i = (1/m_A)\int_A \rho^* (dv^i/dt)\,d^3x$ | Eq. (2.24) |

---

## Relevance to Phonon-Exflation

This paper raises a fundamental question about whether GR's Strong Equivalence Principle holds at 3PN order -- whether gravitational dynamics is truly independent of internal structure. For the phonon-exflation framework, this is directly relevant: the SU(3) fiber constitutes the "internal structure" of matter, and the framework predicts exact effacement (all structure-dependent terms cancel). If the 3PN structure coefficients in GR do not cancel, it would suggest that even in GR the SEP has subtler limits than assumed, which would complicate the framework's effacement prediction. Conversely, if they do cancel, it strengthens the case that the SU(3) fiber coupling is exactly effaced from gravitational dynamics, consistent with the block-diagonal theorem for $D_K$.
