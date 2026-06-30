# Compactified Extra Dimension and Entanglement Island as Clues to Quantum Gravity

**Author(s):** Tran N. Hung and Cao H. Nam
**Year:** 2023
**Journal:** Physical Review D (preprint: arXiv:2303.00348)
**arXiv:** 2303.00348
**Relevance:** HIGH

---

## Abstract

We show that the compactified extra dimension and the emergence of the island can provide clues about quantum gravity because their combination can solve the deepest puzzles of black hole physics. Suppose that the time dimension and the extra dimension compactified on a circle are symmetric under double Wick rotation, the curvature singularity would be removed due to the end of spacetime as a smooth bubble hidden behind the event horizon. The smooth bubble geometries can also be interpreted as microstates leading to the Bekenstein-Hawking entropy because the smooth bubble geometries live in the same region of mass and charge as the black string. In addition, by applying the quantum extremal surface prescription, we show the emergence of the island at late times of the black string evaporation where it is located slightly outside the event horizon. Due to the dominant contribution of the island configuration, the entanglement entropy of the radiation grows no longer linearly in time but it reaches a finite value that is twice the Bekenstein-Hawking entropy at the leading order. This transition shows the information preservation during the black string evaporation. Furthermore, we calculate the Page time which determines the moment of the transition between the linearly growing and constant behaviors of the entanglement entropy as well as the scrambling time corresponding to the information recovery time of the signal falling into the black string.

---

## Key Arguments and Derivations

### Black String Without Singularity (Sec. II)

Starting from the 5D Einstein-Maxwell system with the extra dimension compactified on $S^1$ with radius $R_y$, the metric ansatz is:
$$ds^2 = -f_S(r)dt^2 + f_B(r)dy^2 + \frac{dr^2}{h(r)} + r^2(d\theta^2 + \sin^2\theta\,d\phi^2)$$
with magnetic flux $F = P\sin\theta\,d\theta \wedge d\phi$.

Two vacuum solutions ($P = 0$) exist: (i) 4D Schwarzschild $\times S^1$ with $f_S = h = 1 - r_S/r$, $f_B = 1$; (ii) a smooth bubble of nothing at $r = r_B$ with $f_B = h = 1 - r_B/r$, $f_S = 1$.

**Double Wick rotation symmetry:** Imposing $(t, y, r_S, r_B) \to (iy, it, r_B, r_S)$ requires turning on magnetic flux with $h(r) = f_B(r)f_S(r)$ and $P = \frac{1}{\kappa_5}\sqrt{\frac{3r_Sr_B}{2}}$. The resulting solution has a smooth bubble behind the horizon that ends spacetime, removing the singularity.

### Island Calculation (Secs. III-IV)

Applying the island formula:
$$S(R) = \min \operatorname{ext}_I \left[\frac{A(\partial I)}{4G_N} + S_{\text{mat}}(R \cup I)\right]$$

**Without island:** The entanglement entropy grows linearly in time: $S_{\text{no-island}} \sim \frac{c}{6}\frac{t}{r_S}$

**With island:** The island emerges at late times, located slightly outside the event horizon. The entropy saturates at:
$$S_{\text{island}} \approx 2S_{\text{BH}} = \frac{A_H}{2G_N}$$
at leading order.

### Page Time and Scrambling Time (Sec. V)

The Page time (transition between linear growth and saturation):
$$t_{\text{Page}} \sim \frac{12 S_{\text{BH}}}{c} r_S$$

The scrambling time (information recovery time):
$$t_{\text{scr}} \sim r_S \log S_{\text{BH}}$$

---

## Key Results

1. Double Wick rotation between time and compactified extra dimension removes the curvature singularity via a smooth bubble behind the horizon
2. Smooth bubble geometries serve as microstates for Bekenstein-Hawking entropy (same mass/charge regime as black string)
3. Entanglement island emerges at late times, located slightly outside the event horizon of the black string
4. Page curve is reproduced: entropy saturates at $2S_{\text{BH}}$ (information preservation)
5. Compactified extra dimensions + islands together resolve all three deepest puzzles of black hole physics (singularity, entropy microstates, information loss)

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| 5D Einstein-Maxwell action | $S = \int d^5x \sqrt{-g}\left[\frac{1}{2\kappa_5^2}R - \frac{1}{4}F_{\mu\nu}F^{\mu\nu}\right]$ | Eq. (2) |
| Double Wick metric function | $h(r) = f_B(r)f_S(r) = (1-r_S/r)(1-r_B/r)$ | Eq. (7) |
| Island formula | $S(R) = \min\operatorname{ext}_I\left[\frac{A(\partial I)}{4G_N} + S_{\text{mat}}(R \cup I)\right]$ | Eq. (1) |
| Magnetic flux | $P = \frac{1}{\kappa_5}\sqrt{\frac{3r_Sr_B}{2}}$ | Eq. (8) |
| Page time | $t_{\text{Page}} \sim \frac{12 S_{\text{BH}}}{c}\,r_S$ | Sec. V |

## Relevance to Phonon-Exflation

This paper demonstrates that compactified extra dimensions naturally host entanglement islands that resolve the information paradox for black strings. In the phonon-exflation framework with M4 x SU(3) geometry, the compactified SU(3) fiber provides precisely the internal structure needed for island emergence. The double Wick rotation between time and the compact dimension mirrors the framework's Euclidean-time structure of the instanton gas. The smooth bubble resolution of the singularity parallels the framework's cold Big Bang scenario where the initial state is a smooth geometric maximum rather than a singular point.
