# Self-Stabilization of Extra Dimensions

**Author(s):** K.A. Bronnikov, S.G. Rubin
**Year:** 2006
**Journal:** Published as gr-qc/0510107v2
**arXiv:** gr-qc/0510107
**Relevance:** HIGH

---

## Abstract

We show that the problem of stabilization of extra dimensions in Kaluza-Klein type cosmology may be solved in a theory of gravity involving high-order curvature invariants. The method suggested (employing a slow-change approximation) can work with rather a general form of the gravitational action. As examples, we consider pure gravity with Lagrangians quadratic and cubic in the scalar curvature and some more complex ones in a simple Kaluza-Klein framework. After a transition to the 4D Einstein conformal frame, this results in effective scalar field theories with certain effective potentials, which in many cases possess positive minima providing stable small-size extra dimensions. Estimates made in the original (Jordan) conformal frame show that the problem of a small value of the cosmological constant in the present Universe is softened in this framework but is not solved completely.

---

## Key Arguments and Derivations

### Section II: F(R) Theory in D Dimensions

The paper considers a (D = d_0 + d_1)-dimensional manifold with metric ds^2 = g_{mu nu} dx^mu dx^nu + e^{2 beta(x)} b_{ab} dx^a dx^b, where the extra dimensions form a constant-curvature space with scale factor b(x) = e^{beta}. The effective scalar field is phi(x) = R_b e^{-2 beta(x)} = k d_1(d_1-1) m_D^2 e^{-2 beta(x)}.

Integrating out the extra dimensions yields a 4D scalar-tensor theory:

S = (1/2) V_{[d_1]} m_D^2 int sqrt(4g) d^4x e^{d_1 beta} [F'(phi) R_4 + F(phi) + F'(phi) f_1 + L_m]

The slow-change approximation (each derivative carries a small parameter epsilon, terms beyond O(epsilon^2) are neglected) greatly simplifies this to an effective theory with a single scalar field phi.

After conformal transformation to the Einstein frame (g_{mu nu} -> tilde{g}_{mu nu} = |f(phi)| g_{mu nu} with f(phi) = e^{d_1 beta} F'(phi)), the action takes the form:

S = (V_{[d_1]}/2) m_D^2 int sqrt(tilde{g}) d^4x {(sign F') [tilde{R}_4 + K] - V(phi) + matter}

with kinetic term K_{Ein}(phi) and potential:

V_{Ein}(phi) = -(sign F') [|phi|/(d_1(d_1-1))]^{d_1/2} F(phi)/F'(phi)^2

### Section IV: Quadratic Gravity with Cosmological Constant

For F(phi) = phi + c phi^2 - 2 Lambda, minima of V_{Ein} are found numerically. In the range F' > 0, only AdS minima exist (V_min < 0). In the range F' < 0 (with c = 1.5, Lambda < 0), minima with V_min > 0 are found, corresponding to de Sitter cosmology with stable extra dimensions. A minimum at phi = 0 corresponds to growing (unstabilized) extra dimensions and is not promising cosmologically.

### Section V: Cubic Gravity and Extensions

For F(R) = R + c R^2 + C R^3, the potential is highly sensitive to the parameters c and C. Unlike quadratic gravity, minima with V_min > 0 can be found in the region F' > 0. Adding Ricci tensor squared R_{AB} R^{AB} and Kretschner scalar K = R_{ABCD} R^{ABCD} terms (with coefficients c_1, c_2) enriches the potential and kinetic term structure, adding more freedom for stabilization.

### Section III: Estimates in the Jordan Frame

The effective constants are m_4^2 = V_{[d_1]} m_D^{D-2} b_0^{d_1} F'_0 and Lambda_eff = -F(phi_0)/(2F'_0). The ratio Lambda_eff/m_4^2 still requires fine-tuning of about 90 orders of magnitude, though 30 orders arise naturally from the geometry. The CC problem is "softened but not solved completely."

## Key Results

1. Nonlinear multidimensional gravity with F(R) Lagrangians generates effective potentials V_{Ein}(phi) with nontrivial minima that can stabilize extra dimensions without non-geometric scalar fields.
2. Quadratic gravity (F = R + cR^2 - 2 Lambda) produces de Sitter minima only in the unusual range F' < 0.
3. Cubic gravity (F = R + cR^2 + CR^3) produces de Sitter minima in the conventional range F' > 0.
4. The slow-change approximation is valid whenever curvatures and energy densities are small compared to the D-dimensional Planck scale.
5. Higher-curvature terms (R_{AB}R^{AB}, R_{ABCD}R^{ABCD}) from quantum corrections add freedom to the potential and kinetic term, potentially enabling stabilization through kinetic-term zeros.
6. The cosmological constant problem is softened (30 orders of magnitude arise naturally) but not fully resolved.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| D-dim metric | $ds^2 = g_{\mu\nu}dx^\mu dx^\nu + e^{2\beta(x)}b_{ab}dx^a dx^b$ | Eq. 1 |
| D-dim action | $S = \frac{1}{2}m_D^{D-2}\int\sqrt{Dg}\,d^Dx\,[F(R) + L_m]$ | Eq. 5 |
| Effective scalar field | $\phi(x) = R_b e^{-2\beta(x)} = k\,d_1(d_1-1)m_D^2 e^{-2\beta(x)}$ | Eq. 8 |
| Einstein-frame potential | $V_{\rm Ein}(\phi) = -({\rm sign}\,F')\left[\frac{|\phi|}{d_1(d_1-1)}\right]^{d_1/2}\frac{F(\phi)}{F'(\phi)^2}$ | Eq. 17 |
| Kinetic term | $K_{\rm Ein}(\phi) = \frac{1}{2\phi^2}\left[6\phi^2\left(\frac{F''}{F'}\right)^2 - 2d_1\phi\frac{F''}{F'} + \frac{1}{2}d_1(d_1+2)\right]$ | Eq. 16 |
| Conformal mapping | $\tilde{g}_{\mu\nu} = |f(\phi)|g_{\mu\nu},\quad f(\phi) = e^{d_1\beta}F'(\phi)$ | Eq. 11 |
| Quadratic F(R) | $F(\phi) = \phi + c\phi^2 - 2\Lambda$ | Eq. 37 |
| Effective constants (Jordan) | $m_4^2 = V_{[d_1]}m_D^{D-2}b_0^{d_1}F'_0,\quad \Lambda_{\rm eff} = -F(\phi_0)/(2F'_0)$ | Eq. 29 |
| Extended Lagrangian | $L \supset R + cR^2 + c_1 R_{AB}R^{AB} + c_2 K - 2\Lambda$ | Eq. 47 |
| Extended potential | $V_{\rm Ein} = -({\rm sign}(1+2c\phi))\left[\frac{|\phi|}{d_1(d_1-1)}\right]^{d_1/2}\frac{c_{\rm tot}\phi^2+\phi-2\Lambda}{(1+2c\phi)^2}$ | Eq. 52 |

## Relevance to Phonon-Exflation

This paper directly addresses the stabilization of Kaluza-Klein extra dimensions through higher-curvature gravity terms, which is the geometric analog of the phonon-exflation framework's moduli stabilization challenge. The framework's spectral action generates precisely the higher-curvature invariants (R^2, R_{mu nu}R^{mu nu}) discussed here through the Seeley-DeWitt expansion a_0, a_2, a_4. The paper's finding that the a_4 >> |a_2| hierarchy (in framework language) drives stabilization mirrors the framework's Session 20a result. The effective potential V_{Ein}(phi) is structurally analogous to the framework's tau potential. However, the framework's Session 37 paradigm shift (from "what potential stabilizes tau at the fold?" to "what does the instanton gas do during transit?") represents a departure from the static-minimum approach of this paper. The paper's conclusion that the CC problem is "softened but not solved" (30 of 120 orders explained geometrically) aligns with the framework's recognition that spectral action alone cannot solve the CC (Session 37 closure of the spectral action route).
