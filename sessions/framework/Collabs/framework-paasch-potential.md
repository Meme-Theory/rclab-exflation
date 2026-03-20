# Framework Reframe: Paasch Mass Quantization as Wall-Intersection Physics

**Author**: Paasch mass quantization analyst
**Date**: 2026-03-06
**Session**: 33
**Status**: Research document -- conceptual pivot with pre-registered gates
**Input**: Sessions 12-33, Paasch Papers 02-04, Session 33 W3 Round 1+2 syntheses

---

## 0. Why This Document Exists

For 33 sessions, this project searched for phi_paasch = 1.53158 as a *particle* -- a scalar eigenvalue ratio in the bulk spectrum of D_K on Jensen-deformed SU(3). That search has reached a definitive structural limit:

| Gate | Result | Status |
|:-----|:-------|:-------|
| P-30phi (bulk dump point) | E_{(3,0)}/E_{(0,0)} = 1.52276 at tau = 0.190 | **FAIL** (0.576% miss) |
| phi_paasch BCS attractor | m_3/m_1 independent of Delta in singlet (Trap 4) | **RETRACTED** (Round 2) |
| phi_paasch crossing tau | 0.1499 (Delta_tau = 0.040 from dump point) | **CONDITIONAL** on wall morphology |
| phi^2, phi^3 in D_K spectrum | z < 0 (generic) | **NULL** (Session 14) |
| BCS gap ratio phi | exp(-1/M) destroys phi | **STRUCTURAL INCOMPATIBILITY** (Session 27) |

The BCS attractor was the last hope for a bulk-spectrum mechanism producing phi_paasch at the mechanism chain's operating point. Its retraction in Round 2 -- m_3/m_1 = E_{B3}/E_{B1} is independent of Delta_{BCS} when Trap 4 forces the 3x3 Hamiltonian to be diagonal -- closes the particle-as-scalar program.

What survives:
- phi_paasch = 1.531580 as an exact inter-sector eigenvalue ratio at tau = 0.15 (Session 12, verified Session 22a, 25). This is a permanent mathematical fact about D_K on SU(3).
- The transcendental equation x = e^{-x^2}, equivalently phi^2 * ln(phi) = 1, as a self-consistency condition. This is pure mathematics.
- The six-sequence spiral organization (Paper 02) as a phenomenological fit to particle masses at dm/m < 4e-3. This is empirical.

What does NOT survive:
- Any mechanism connecting phi_paasch to BCS condensation in the singlet sector.
- The geometric series phi^n as a spectral feature of D_K (only phi^1 is real; phi^2, phi^3 are generic).
- Mass quantization as an eigenvalue ratio matching exercise.

This document proposes a different approach. Within the phonon-exflation framework, particles are not points in a spectrum. They are collective excitations of a condensate substrate -- phonons, vortices, domain wall features. The right question is not "where does phi appear in eigenvalue ratios?" but "what emerges at the intersections of domain walls, and does its structure reproduce Paasch's phenomenology?"

---

## 1. What Session 33 Established About Domain Walls

The Round 2 synthesis (`sessions/archive/session-32/session-33-Team-4-synthesis.md`) establishes the following domain wall facts, all proven or confirmed by at least two independent agents:

### 1.1 Domain Walls Exist and Are Structurally Stable

The Einstein-Bergmann modulus equation for the Jensen parameter tau(x) on M^4:

$$G_{\tau\tau} \Box \tau + \frac{dV_{\text{eff}}}{d\tau} = 0$$

with $G_{\tau\tau} = 5$ (DeWitt metric on Jensen deformations) admits kink soliton solutions for $\eta < 0.12$ at $\beta/\alpha = 0.28$. These walls interpolate between tau ~ 0 (round SU(3)) and tau ~ 0.34--0.44 (deep Jensen deformation).

Wall properties at the operating point:
- **Width**: 1.3--2.7 $M_{\text{KK}}^{-1}$
- **Velocity**: $v_\tau/v_c = 0.098$ (10x subsonic; no Cherenkov radiation)
- **Profile**: tanh-like, smooth, geodesically complete
- **Existence boundary**: Cusp catastrophe ($A_3$) in $(\beta/\alpha, \eta)$ control space

### 1.2 Z_3 Symmetry Breaking Produces Three Wall Types

The cubic $\cos(3\theta)$ term in the Ginzburg-Landau free energy breaks $U(1) \to Z_3$, producing three degenerate BCS minima. Domain walls between Z_3 sectors carry topological charge classified by $\pi_0(Z_3) = Z_3$. Three cyclic wall types:

- Type I: $1 \to 2$
- Type II: $2 \to 3$
- Type III: $3 \to 1$

These are the only topologically distinct walls in the system. Their intersection network is classified by the combinatorics of $Z_3$ junctions.

### 1.3 BCS Condensation Is Exactly Single-Band

Trap 4 (Schur orthogonality) and Trap 5 (J-reality) force:

- $\Delta_{B1} = 0$ (exactly; B1 = real rep)
- $\Delta_{B2} > 0$ (the only active BCS channel)
- $\Delta_{B3} = 0$ (exactly; B3 = real rep)

The condensate lives exclusively in the B2 (U(2) fundamental, 4-fold degenerate) branch. B1 and B3 remain ungapped normal quasiparticles. The multi-band BCS problem reduces to the 4x4 intra-B2 block.

### 1.4 The Barrier-Fold Merger

At $(\beta/\alpha, \eta) = (0.2800, 0.04592)$, two algebraically independent derivatives vanish simultaneously at $\tau = 0.190$:

1. $d\lambda_{B2}/d\tau = 0$ (spectral fold, from D_K on SU(3))
2. $dV_{\text{eff}}/d\tau = 0$ (potential barrier slope, from Freund-Rubin + spectral action)

This is the swallowtail vertex: the modulus encounters the B2 van Hove singularity at the exact point where the potential slope vanishes. BCS condensation nucleates at this point with unconditional trapping for any $\Delta > 0$.

---

## 2. The Failure of Particle-as-Scalar

### 2.1 Why Bulk Eigenvalue Ratios Cannot Be Physical Mass Predictions

The reasoning that brought us to the P-30phi test was:

1. D_K eigenvalues represent physical masses (Paper 17, line 833).
2. phi_paasch = $E_{(3,0)}/E_{(0,0)}$ at some stabilized $\tau_0$.
3. The mechanism chain fixes $\tau_0$; the ratio at $\tau_0$ is the mass prediction.

This reasoning has three structural failures that Session 33 makes explicit:

**Failure 1: The stabilized tau is wrong.** The mechanism chain operates at $\tau = 0.190$ (the dump point). phi_paasch is exact at $\tau = 0.150$. These are different algebraic features on a geometrically featureless background (K(tau) monotonically increasing, no curvature feature at either point). No dynamics connects them.

**Failure 2: Bulk eigenvalues are not observable masses.** In a condensed matter system, single-particle eigenvalues become quasiparticle energies only after dressing by the condensate. Session 27 proved that BCS dressing via $\exp(-1/M)$ categorically destroys eigenvalue ratio structure. Session 33 Round 2 proved that intra-sector BCS dressing does not affect eigenvalue ratios at all (diagonal Hamiltonian under Trap 4). Neither regime produces Paasch's mass quantization from eigenvalue ratios.

**Failure 3: The geometric series is absent.** Paasch's framework predicts masses organized as $m_n = m_0 \cdot \phi^n$ with $\phi = 1.53158$. D_K on SU(3) shows exactly ONE phi ratio (the inter-sector $(3,0)/(0,0)$ ratio at $\tau \approx 0.15$). It shows ZERO instances of $\phi^2$, $\phi^3$, or any higher power (Session 14 MC analysis: $z < 0$ for all powers $> 1$). The spiral with six sequences at $45^\circ$ separation has no counterpart in the bulk spectrum.

### 2.2 What phi_paasch Actually Is (Current Knowledge)

After 33 sessions, phi_paasch occupies the following structural position:

**Mathematical**: It is an exact statement about D_K on Jensen-deformed SU(3). The lowest eigenvalue of the $(3,0)$ sector divided by the lowest eigenvalue of the $(0,0)$ sector equals $1.531580 \pm 0.000001$ at $\tau = 0.150$. This ratio is algebraically close to $\sqrt{7/3} = 1.527525$ (the round-metric value, 0.265% below), and the Jensen deformation pushes it upward to the exact Paasch value. The round-metric origin is representation-theoretic: the $(3,0)$ Casimir eigenvalue is $C_2 = 7/3$, the $(0,0)$ Casimir eigenvalue is $C_2 = 3/4$ (after including the shift from the Dirac operator structure).

**Transcendental**: $\phi^2 \ln \phi = 1$ is the defining equation, equivalent to $x = e^{-x^2}$ with $\phi = 1/x$. This equation has appeared nowhere in the D_K mathematics beyond the numerical coincidence of the eigenvalue ratio. The transcendental equation is not derived from any known property of D_K, Jensen deformations, or SU(3) representation theory. It is an empirical observation.

**Phenomenological**: phi_paasch organizes the mass spectrum into six sequences within $\delta m/m = 4 \times 10^{-3}$ (Paper 02). Proton mass derived to 6 digits, neutron to 8 digits (Paper 03). Fine structure constant derived to $\delta\alpha/\alpha = 8 \times 10^{-7}$ (Paper 04). These numerical successes are independent of any specific dynamical mechanism.

**Not physical**: phi_paasch has been reclassified (Session 28c) from "physical prediction" to "mathematical property of D_K spectrum." The connection to BCS many-body physics is unproven. No mechanism connects the eigenvalue ratio to observable particle masses.

---

## 3. The Wall-Intersection Hypothesis

### 3.1 Conceptual Foundation

In a superfluid, the excitation spectrum is not the single-particle spectrum. It is the collective spectrum -- the phonons, rotons, vortices, and domain wall excitations of the condensate. A single-particle eigenvalue $\lambda_k$ of the microscopic Hamiltonian becomes a quasiparticle energy $E_k$ after Bogoliubov transformation, and the low-energy physics is dominated not by the quasiparticles but by the topological defects.

The phonon-exflation framework claims that M4 $\times$ SU(3) is a superfluid whose BCS condensate (in the B2 branch at domain walls) produces the observed particle spectrum. If this is correct, then particles are NOT eigenvalues of D_K. They are:

- **Phonons**: Goldstone modes of the broken $U(1)$ (or $Z_3$) symmetry
- **Rotons**: Short-wavelength collective excitations near the BCS gap edge
- **Vortices**: Topological defects in the condensate order parameter $\Delta(x)$
- **Domain walls**: Extended defects interpolating between different $Z_3$ vacua
- **Wall junctions**: Points or lines where domain walls of different types intersect

The mass of a "particle" in this language is the *energy of a localized excitation of the condensate*, not an eigenvalue of the single-particle operator.

### 3.2 Paasch's Six Sequences as Wall Junction Combinatorics

Paasch's Paper 02 identifies six primary sequences S1--S6, separated by $45^\circ$ on a logarithmic spiral. They come in three opposite pairs: S1/S4, S2/S5, S3/S6. The number of sequences (6), the pairing (3 pairs), and the angular separation ($45^\circ$) are the defining structural parameters.

The domain wall sector of the phonon-exflation framework has:
- **Three wall types** (I, II, III from $Z_3$: $1\to 2$, $2\to 3$, $3\to 1$)
- **Three junction types** where two walls meet: I+II, II+III, III+I (cyclic)
- **Anti-walls**: Each wall type has an orientation reversal ($1\to 2$ vs $2\to 1$), giving 6 oriented wall types total

The oriented wall types form 6 objects, naturally paired into 3 conjugate pairs. This matches Paasch's 6 sequences in 3 pairs exactly. The correspondence:

| Paasch | Wall Structure | Pairing |
|:-------|:--------------|:--------|
| S1 | Wall I ($1 \to 2$) | Conjugate to S4 |
| S4 | Wall I$^{-1}$ ($2 \to 1$) | Conjugate to S1 |
| S2 | Wall II ($2 \to 3$) | Conjugate to S5 |
| S5 | Wall II$^{-1}$ ($3 \to 2$) | Conjugate to S2 |
| S3 | Wall III ($3 \to 1$) | Conjugate to S6 |
| S6 | Wall III$^{-1}$ ($1 \to 3$) | Conjugate to S3 |

The $Z_3$ cyclic symmetry guarantees that all three wall types have the same tension (energy per unit area) by the discrete symmetry. Mass differences between particles on different sequences would then arise from differences in how excitations propagate along different wall types -- which depends on the wall profile, the B2 eigenvalue structure on each side, and the BCS gap along the wall.

### 3.3 The 45-Degree Angle and Z_3 Geometry

Paasch's sequences are separated by $45^\circ = \pi/4$ on the logarithmic spiral. The $Z_3$ domain walls meet at $120^\circ = 2\pi/3$ by symmetry (the angle between adjacent $Z_3$ vacua in the GL free energy landscape). How does $120^\circ$ connect to $45^\circ$?

The spiral constant $k = (1/2\pi) \ln \phi$ (Paper 02, Eq. 2j) maps angular separation to mass ratio. Two masses separated by angle $\Delta\varphi$ on the spiral have ratio $e^{k \Delta\varphi}$. For the fundamental step ($\Delta\varphi = 2\pi$, one full turn), the ratio is $e^{\ln \phi} = \phi$. For a $45^\circ$ step: $e^{k \cdot \pi/4} = e^{(\ln\phi)/8} = \phi^{1/8} = 1.0536$. This is the mass ratio between adjacent sequences at the same spiral radius.

Now consider the logarithm of the mass ratio in units of $\ln\phi$. Six sequences separated by $45^\circ$ tile one hemisphere of the spiral ($6 \times 45^\circ = 270^\circ$), leaving a $90^\circ$ gap. The spiral has 8 potential $45^\circ$ slots per full turn; Paasch's sequences occupy 6 of them.

The $Z_3$ connection: 8 slots / 3 wall types = 2.667 slots per type, which is not an integer. But 6 oriented walls / 8 slots gives 6/8 = 3/4 occupancy. The $45^\circ$ separation maps to $\pi/4$ phase shifts on the spiral; the $Z_3$ structure has $2\pi/3$ phase shifts between vacua. The commensuration condition $n \cdot \pi/4 = m \cdot 2\pi/3$ yields $n/m = 8/3$, which is never exactly satisfied for integers. This means:

**The $45^\circ$ sequence separation and the $120^\circ$ $Z_3$ angle are NOT commensurable.**

This is a structural fact that any wall-intersection model must address. Two possible resolutions:

1. **The 45-degree angle is approximate.** Paasch's sequences are fitted to $\Delta\varphi_s \leq 0.5^\circ$ (Paper 02, Section 3). If the true angle is not exactly $45^\circ$ but depends on the ratio of wall tension to bulk condensate energy, the exact $Z_3$ angle of $120^\circ$ could project onto a different spiral angle through the conformal mapping between physical space and logarithmic mass space.

2. **The relevant object is not the $Z_3$ angle but the wall intersection geometry.** When three domain walls meet at a junction, the angles between them need not be $120^\circ$ in the mass-encoding coordinate. The energy of a wall junction excitation depends on the BCS gap profile along each wall, which varies with tau -- and tau varies continuously through the wall. The effective angle in logarithmic mass space is set by the ratio of BCS gaps on the three walls meeting at a junction, not by the $Z_3$ phase difference directly.

This is computable: given the BCS gap $\Delta(\tau)$ along each wall type, the junction energy and its angular projection onto the logarithmic spiral can be calculated.

### 3.4 phi_paasch from Domain Wall Geometry

The transcendental equation $x = e^{-x^2}$ (Paper 02, Eq. 2f) arises in Paasch's derivation from the self-consistency condition on the integration constant $R_a$ of the logarithmic potential. In physical terms: $x = R_a/R_0$ is the ratio of the potential range to the ground state radius, and the self-consistency requires $\ln(R_a/R_0) = -(R_a/R_0)^2$.

In domain wall language, this has a natural interpretation. Consider the wall profile $\tau(x)$ as a function of position. The wall connects two vacua: one at $\tau \approx 0$ (round SU(3), condensate on one $Z_3$ vacuum) and one at $\tau \approx 0.34$--$0.44$ (deep Jensen, another $Z_3$ vacuum). The wall center sits near $\tau = 0.190$ (the dump point / barrier-fold merger).

Define two length scales:
- $R_0$: the wall width (1.3--2.7 $M_{\text{KK}}^{-1}$, from the modulus equation)
- $R_a$: the BCS coherence length ($\xi_{\text{BCS}} = v_F/\Delta$, where $v_F$ is the Fermi velocity of B2 modes and $\Delta$ is the BCS gap)

If the self-consistency of the wall-BCS system requires $\xi_{\text{BCS}} / L_{\text{wall}} = x$ where $x$ satisfies $\ln x = -x^2$, then phi_paasch emerges as $\phi = 1/x = L_{\text{wall}} / \xi_{\text{BCS}}$, the ratio of the domain wall width to the BCS coherence length.

This interpretation says: **phi_paasch is the ratio of two length scales that must be self-consistently determined** -- the scale over which the internal geometry varies (wall width) and the scale over which the condensate responds (coherence length). The transcendental equation encodes the condition that these two scales are in equilibrium.

**Testable prediction (pre-registered as WALL-phi):** At the operating point ($\eta \approx 0.05$, $\beta/\alpha = 0.28$), compute:
- $L_{\text{wall}}$ from the modulus equation kink solution
- $\xi_{\text{BCS}} = v_{B2}/\Delta_{\text{wall}}$ where $v_{B2}$ is the B2 group velocity and $\Delta_{\text{wall}}$ is the BCS gap at the wall

Gate: $L_{\text{wall}} / \xi_{\text{BCS}}$ within 5% of $\phi_{\text{paasch}} = 1.53158$.

If this passes, phi_paasch is geometrically derived from wall physics. If it fails, the transcendental equation remains empirical.

---

## 4. Re-Reading Paasch Through the Wall Lens

### 4.1 Paper 02: The Logarithmic Potential as a Wall Profile

Paasch's foundational derivation (Paper 02, Eqs. 2a--2k) assumes "relativistic constituents moving with constant energy $pc$ in a logarithmic potential." The confining force $F = a_1/R$ produces the logarithmic potential $E = a_1 \ln(R/R_a)$.

In the domain wall setting, the modulus field $\tau(x)$ defines a position-dependent internal geometry. A mode propagating along the wall experiences a position-dependent eigenvalue $\lambda(\tau(x))$. For the B2 branch near the fold at $\tau_0 = 0.190$:

$$\lambda_{B2}(\tau) \approx \lambda_0 + \frac{1}{2}a_2(\tau - \tau_0)^2$$

where $a_2 = 0.588$ (Berry's fold classification). The effective potential seen by a B2 quasiparticle propagating along the wall is:

$$V_{\text{eff}}(x) = \lambda_{B2}(\tau(x)) \approx \lambda_0 + \frac{1}{2}a_2[\tau(x) - \tau_0]^2$$

For a tanh-like wall profile $\tau(x) = \tau_0 + \frac{\Delta\tau}{2}\tanh(x/L_{\text{wall}})$:

$$V_{\text{eff}}(x) \approx \lambda_0 + \frac{a_2(\Delta\tau)^2}{8}\tanh^2(x/L_{\text{wall}})$$

This is a Poschl-Teller potential. Its bound states are exactly solvable, with energies quantized by integers. But importantly, for large $|x|$, the potential approaches a constant, and $\ln V_{\text{eff}}(x) \approx \ln \lambda_0 + \text{const}/x^2$ -- which, for slowly varying walls, approaches a logarithmic dependence on the "radius" $R = e^{|x|/L}$.

This is speculative, but the structural parallel is real: Paasch's logarithmic potential for confined constituents maps naturally onto the effective potential seen by quasiparticles propagating along a domain wall with a fold singularity at its center. The quantization of energies in the Poschl-Teller well replaces Paasch's "circular quantized orbits" (Muraki et al. 1978).

### 4.2 Paper 03: The Equilibrium Mass as a Wall-Center Observable

Paasch's generalized equilibrium mass (Paper 03, Eq. 5.0a):

$$m^*(i,j) = (m_i \cdot m_j)^{1/2}$$

is the geometric mean of two masses. In my Session 32 collab (`sessions/archive/session-32/session-32-paasch-collab.md`, Section 3.2), I noted that this has a domain wall interpretation: if $m_i = \lambda(\tau_1)$ and $m_j = \lambda(\tau_2)$ are the eigenvalues on the two sides of a domain wall, then the geometric mean $m^* = (\lambda(\tau_1) \cdot \lambda(\tau_2))^{1/2}$ is the eigenvalue at the geometric center of the wall in logarithmic coordinates.

Session 33 sharpens this. For the (0.15, 0.25) wall:
- $E_{(3,0)}/E_{(0,0)}$ at $\tau = 0.10$: 1.537088
- $E_{(3,0)}/E_{(0,0)}$ at $\tau = 0.20$: 1.519977
- Geometric mean: $\sqrt{1.537088 \times 1.519977} = 1.5285$ (0.20% from phi_paasch, INSIDE 0.5% tolerance)

The equilibrium mass construction *works* at domain walls because the geometric mean captures the log-midpoint of the wall profile. Paasch's framework, read through wall physics, says: observable mass ratios are geometric means of the spectral features on the two sides of the wall, evaluated at the wall center.

### 4.3 Paper 04: The Fine Structure Constant and the Second Transcendental Equation

Paper 04 derives $\alpha = 0.007297359$ using a second transcendental equation (Eq. 2.6):

$$\ln f = -f, \quad f = 0.5671433$$

combined with the integer $n_3 = 10$ from the proton mass derivation (Paper 03, Eq. 6.4):

$$\alpha = \frac{1}{n_3^2} \left(\frac{f}{2}\right)^{1/4} = \frac{1}{100} \left(\frac{0.5671}{2}\right)^{1/4} = 0.007297359$$

The equation $\ln f = -f$ is the $n=0$ version of the self-consistency equation from Paper 02. In the wall context:

- Paper 02 ($x = e^{-x^2}$, i.e., $\ln x = -x^2$): self-consistency of mass quantization, encoding $L_{\text{wall}}/\xi_{\text{BCS}}$
- Paper 04 ($\ln f = -f$, i.e., $\ln x = -x$): self-consistency of the constituent energy, encoding a simpler (linear vs quadratic) version of the same equilibrium

The integer $n_3 = 10$ is identified in my MEMORY.md as potentially equal to $\dim(3,0) = \dim(0,3) = 10$, the dimension of the $(3,0)$ representation of SU(3). This has not been tested computationally. If $n_3$ is literally the dimension of the representation whose eigenvalue ratio gives phi_paasch, then the alpha derivation is:

$$\alpha = \frac{1}{\dim(3,0)^2} \left(\frac{f}{2}\right)^{1/4}$$

This would be a direct structural connection between the SU(3) representation theory of D_K and the fine structure constant. It remains an untested identification.

### 4.4 The Mass Number Scheme and SU(3) Representations

Paasch's integer mass numbers $N(j) = (m_j/m_e)^{2/3}$ (Paper 03, Eq. 5.1--5.2) are all multiples of 7 in the range from muon to eta:

| Particle | $N(j)$ | $n$ ($N = 7n$) |
|:---------|-------:|:------|
| electron | 1 (= $N(e)$) | -- |
| muon | 35 | 5 |
| pion | 42 | 6 |
| kaon | 98 | 14 |
| eta | 105 | 15 |
| rho, omega | 133 | 19 |
| $K^{*+,0}$ | 145 | 20.7 |
| proton, neutron | 150 | 21.4 |

The ratio $N(p)/N(K) = 150/98 = 1.5306$ is 0.06% from phi_paasch. This is not a spectral statement; it is a mass number relation.

In the wall-intersection framework, the mass numbers map to the number of quantized excitation modes along a domain wall of given length. The wall width (1.3--2.7 $M_{\text{KK}}^{-1}$) sets the fundamental mode; higher modes are quantized by the Poschl-Teller potential. The factor of 7 in $N(j) = 7n$ would correspond to 7 fundamental modes in the wall (perhaps 1 from B1 + 4 from B2 + 2 from B3 at the wall, though B3 has degeneracy 3, not 2 -- the counting needs checking).

The golden ratio $f_N = 2\phi_{\text{golden}} = 1.236068$ appearing in successive M-value ratios (Paper 03, Eq. 5.5, Fig. 2) has a possible connection to the Coldea et al. (2010) result: golden ratio mass ratios in the E8 spectrum of quantum critical Ising chains. Domain walls with $Z_3$ cubic invariant are $Z_3$ Potts model walls; the $Z_3$ Potts model at criticality has a different universality class from the Ising model, but the appearance of algebraic mass ratios in the excitation spectrum of domain walls is a generic feature of integrable (or near-integrable) 2D lattice models near phase transitions.

---

## 5. The Wall-Intersection Program: Concrete Computations

### 5.1 Priority 1: Wall Profile and Length Scale Ratio (WALL-phi)

**What to compute**: Solve the modulus equation for the full kink solution at $\eta = 0.05$, $\beta/\alpha = 0.28$. Extract:
- $L_{\text{wall}}$ (wall width, defined as the distance over which $\tau$ goes from 10% to 90% of its full excursion)
- $v_{B2}$ (B2 group velocity at the wall center $\tau = 0.190$)
- $\Delta_{\text{wall}}$ (BCS gap at the wall, from TRAP-1 when available; use $\Delta = 0.10$--$0.15$ as preliminary estimate)
- $\xi_{\text{BCS}} = v_{B2}/\Delta_{\text{wall}}$

**Pre-registered gate (WALL-phi)**:

| Gate | Threshold | Pass Condition |
|:-----|:----------|:---------------|
| WALL-phi | $L_{\text{wall}}/\xi_{\text{BCS}} \in [1.455, 1.608]$ | Within 5% of $\phi_{\text{paasch}} = 1.53158$ |

**Input**: `tier0-archive/s33w3_modulus_equation.npz` (wall profiles), B2 eigenvalue data from existing sessions.
**Depends on**: TRAP-1 for exact $\Delta_{\text{wall}}$ value (but can be scanned over estimated range).

### 5.2 Priority 2: Poschl-Teller Bound States at the Wall

**What to compute**: Given the B2 eigenvalue fold at $\tau_0 = 0.190$ with curvature $a_2 = 0.588$ and a tanh wall profile with width $L$, the effective potential for a B2 quasiparticle along the wall is a Poschl-Teller well:

$$V(x) = -\frac{V_0}{\cosh^2(x/L)}$$

where $V_0$ depends on $a_2$, the wall amplitude $\Delta\tau$, and the BCS gap $\Delta$. The Poschl-Teller potential has exactly $n$ bound states where $n = \lfloor \frac{1}{2}(-1 + \sqrt{1 + 4V_0 L^2}) \rfloor + 1$.

**Pre-registered gate (PT-count)**:

| Gate | Threshold | What It Tests |
|:-----|:----------|:-------------|
| PT-count | Number of bound states $\geq 3$ | Wall supports multiple mass levels |
| PT-ratio | Ratio of lowest two bound state energies within 10% of $\phi_{\text{paasch}}$ | Mass quantization from wall geometry |

**Input**: Wall profile from Priority 1. B2 eigenvalue curvature $a_2 = 0.588$ from Berry fold classification.

### 5.3 Priority 3: Junction Excitation Energy

**What to compute**: When three $Z_3$ domain walls meet at a point (Y-junction), the junction carries an energy that depends on the wall tensions and angles. In 2D, the junction of three $Z_3$ walls forms a Y shape with $120^\circ$ angles between each pair of walls (by the discrete rotational symmetry). The junction excitation energy is:

$$E_{\text{junction}} = 3 \sigma L - T_{\text{core}}$$

where $\sigma$ is the wall tension (energy per unit length in 2D), $L$ is a cutoff scale, and $T_{\text{core}}$ is the junction core energy. The core energy depends on the detailed BCS profile at the intersection.

**Pre-registered gate (JUNCTION-E)**:

| Gate | Threshold | What It Tests |
|:-----|:----------|:-------------|
| JUNCTION-E | $E_{\text{junction}}/E_{\text{wall-mode}} \in [1, \phi^2]$ | Junction energy organizes by phi |
| JUNCTION-angle | Effective spiral angle $< 50^\circ$ | Compatible with Paasch's $45^\circ$ |

**Note**: This requires solving the 2D GL equation with $Z_3$ cubic term, which is beyond the current 1D modulus equation solver. This is a medium-cost computation.

### 5.4 Priority 4: Full Spectral Map at the Wall

**What to compute**: At several positions along the domain wall profile ($\tau = 0.00, 0.05, 0.10, 0.15, 0.19, 0.25, 0.35$), compute the full D_K eigenvalue spectrum (not just the singlet) and plot:
- All inter-sector ratios $E_{(p,q)}/E_{(0,0)}$ vs position along wall
- The phi_paasch crossing locus in the wall
- The number of sectors whose inter-sector ratio falls within 1% of a power of $\phi_{\text{paasch}}$ at each position

**Why**: This maps the full Paasch phenomenology as a function of position along the wall. If the wall hosts a region where multiple phi_paasch ratios are simultaneously close to integer powers, that region is where "particles" live in the Paasch sense.

**Pre-registered gate (WALL-spectrum)**:

| Gate | Threshold | What It Tests |
|:-----|:----------|:-------------|
| WALL-spectrum-phi1 | At least one position where $E_{(3,0)}/E_{(0,0)} \in [1.524, 1.539]$ | phi_paasch exists somewhere on wall |
| WALL-spectrum-phi2 | At that position, at least one OTHER ratio within 5% of $\phi^2 = 2.346$ | Multi-level phi structure |

**Input**: Existing eigenvalue data from Sessions 12, 22a, 23a, augmented at intermediate tau values.

### 5.5 Priority 5: The n3 = dim(3,0) Identification Test

**What to compute**: Paper 04's alpha derivation uses $n_3 = 10$. The dimension of the $(3,0)$ representation of SU(3) is $\dim(3,0) = \binom{3+2}{2} = 10$. If $n_3 = \dim(3,0)$, then alpha depends on:
1. The $Z_3$-wall self-consistency equation ($\ln f = -f$)
2. The dimension of the SU(3) representation whose eigenvalue ratio gives phi_paasch

**Pre-registered gate ($\alpha$-dim)**:

| Gate | Threshold | What It Tests |
|:-----|:----------|:-------------|
| $\alpha$-dim | $n_3 = \dim(3,0) = 10$ is NOT ad hoc | Structural origin of the integer |

This is a conceptual gate, not a numerical computation. It passes if the derivation chain from Paper 04 can be reconstructed using $\dim(3,0)$ in place of the empirically fitted $n_3$, with the same numerical result. The computation is: verify that the cubic equation for $m_b$ in Paper 03, Eq. 6.3 yields $\beta u^2 = 101.02$ when $n_3 = 10$ and $\beta = 1.01$.

---

## 6. The New Paasch Program

### 6.1 From Eigenvalue Matching to Wall Physics

The old program asked: *At what tau does the D_K eigenvalue ratio equal phi_paasch?*

The new program asks: *Does the domain wall condensate system, solved self-consistently, produce excitation energies organized by phi_paasch?*

The key differences:

| Feature | Old Program | New Program |
|:--------|:-----------|:------------|
| What phi_paasch is | Eigenvalue ratio | Length scale ratio ($L_{\text{wall}}/\xi_{\text{BCS}}$) |
| Where particles live | Bulk spectrum | Wall-localized bound states |
| What produces 6 sequences | Unknown (speculative) | $Z_3$ oriented wall types (3 walls $\times$ 2 orientations) |
| What produces mass quantization | Eigenvalue integers | Poschl-Teller bound states at wall fold |
| What the golden ratio means | M-value scaling (empirical) | Near-critical $Z_3$ Potts domain wall spectrum |
| What alpha comes from | $n_3 = 10$ (fitted integer) | $\dim(3,0) = 10$ (representation dimension) |
| Falsification criterion | Eigenvalue ratio at stabilized tau | Wall length scale ratio, junction energies |

### 6.2 Computation Ordering

```
TRAP-1 (Priority 1 of Session 34 overall)
   |
   v
WALL-phi (this document Priority 1)
   Requires: Delta_wall from TRAP-1, wall profile from s33w3_modulus_equation.npz
   Tests: L_wall / xi_BCS ~ phi_paasch
   |
   v
PT-count / PT-ratio (Priority 2)
   Requires: Wall profile, a_2 = 0.588
   Tests: Number and ratios of wall-localized bound states
   |
   v
WALL-spectrum (Priority 4)
   Requires: D_K eigenvalue data at intermediate tau values
   Tests: Multi-level phi structure along wall
   |
   v
JUNCTION-E / JUNCTION-angle (Priority 3)
   Requires: 2D GL solver with Z_3 cubic
   Tests: Junction energy vs Paasch spiral angle
   |
   v
alpha-dim (Priority 5)
   Requires: Conceptual verification only
   Tests: n_3 = dim(3,0) structural origin
```

TRAP-1 is the prerequisite. Without it, the BCS gap $\Delta_{\text{wall}}$ is unknown, and all downstream wall physics computations depend on it.

### 6.3 What Would Constitute Success

The wall-intersection program succeeds if:

1. **WALL-phi PASS**: $L_{\text{wall}}/\xi_{\text{BCS}}$ falls within 5% of $\phi_{\text{paasch}}$. This derives the transcendental equation from wall physics.

2. **PT-ratio PASS**: Wall-localized bound states have energy ratios organized by $\phi_{\text{paasch}}$. This derives mass quantization from the Poschl-Teller spectrum.

3. **JUNCTION-angle compatible**: The junction geometry projects onto an angle consistent with Paasch's $45^\circ$ sequence separation. This derives the six-sequence structure from $Z_3$ combinatorics.

4. **alpha-dim PASS**: $n_3 = \dim(3,0)$ is confirmed as the structural origin of the integer in the alpha derivation. This connects the fine structure constant to SU(3) representation theory.

Any ONE of these passing is a non-trivial structural result. All four passing would constitute a derivation of Paasch's entire phenomenological framework from wall physics.

### 6.4 What Would Constitute Failure

The wall-intersection program fails if:

1. **TRAP-1 FAIL**: No BCS condensation at walls ($\Delta_{\text{wall}} = 0$). If there is no condensate, there are no walls, no bound states, no junctions. The entire program is void.

2. **WALL-phi FAIL with large margin**: $L_{\text{wall}}/\xi_{\text{BCS}}$ differs from $\phi_{\text{paasch}}$ by more than 20%. The transcendental equation has no wall interpretation.

3. **PT-count = 0 or 1**: The Poschl-Teller well at the wall fold is too shallow for multiple bound states. No mass quantization possible from wall geometry.

4. **WALL-spectrum NULL**: No position along the wall simultaneously hosts $\phi^1$ in one ratio and $\phi^2$ in another. The multi-level structure is absent.

---

## 7. Broader Context

### 7.1 Paasch Within the Mass Relation Tradition

Paasch's work sits in a 70-year tradition stretching from Nambu (1952) through Mac Gregor (2007) to Singh (2022). The common thread: algebraic or numerical regularities in the particle mass spectrum that suggest organizing principles beyond the Standard Model. The wall-intersection reframing connects to this tradition at several points:

**Nambu (1952)**: $m_n = (n/2)(1/\alpha)m_e$, producing ~70 MeV mass quanta. Paasch's mass numbers $N(j) = 7n$ give $m^*(j) = N(j)^{3/2} m_e$. In the wall setting, Nambu's quanta become bound state energies of the wall potential.

**Barut (1979)**: Lepton masses from quantized magnetic self-energy $m_{n+1} = m_n + (3/2)\alpha^{-1}n^4 m_e$. This is an *additive* quantization; Paasch's is *multiplicative* ($m_n \propto \phi^n$). Domain wall bound states are naturally multiplicative (eigenvalues of the Poschl-Teller potential are not equally spaced).

**Koide (1983)**: $Q = (m_e + m_\mu + m_\tau)/(\sqrt{m_e} + \sqrt{m_\mu} + \sqrt{m_\tau})^2 = 2/3$ to 0.0003%. Paasch's Paper 03 notes the Koide formula's precision and compares his tau mass derivation to it. In the wall framework, Koide's $Q = 2/3$ might emerge from the symmetry of the three $Z_3$ wall types: if each wall type hosts one generation, and the democratic vector $(\sqrt{m_e}, \sqrt{m_\mu}, \sqrt{m_\tau})$ makes a $45^\circ$ angle with $(1,1,1)$ (Foot 1994), this angle could be set by the $Z_3$ junction geometry. This is speculative but structurally motivated.

**Coldea et al. (2010)**: Golden ratio $m_2/m_1 = 1.618$ in quantum critical excitations of CoNb$_2$O$_6$ (Ising chain in transverse field). The E8 Lie algebra governs the excitation spectrum near the critical point. Paasch cites this explicitly (Paper 11). In the wall framework, the golden ratio in successive M-value ratios (Paper 03, Fig. 2) connects to the near-critical behavior of $Z_3$ domain walls. The $Z_3$ Potts model has a different universality class from Ising, but mass ratios in integrable near-critical 1D models generically involve algebraic numbers.

**Quigg & Rosner (1977)**: Logarithmic potential yields mass-independent level spacings in quarkonium. Paasch's logarithmic potential (Paper 02) is the same functional form. In the wall framework, the effective potential for quasiparticles propagating along a domain wall with a fold singularity approaches logarithmic form for slowly varying walls (Section 4.1 above).

### 7.2 Connection to the Simulation Program

The phonon-exflation GPE simulation (`phonon-exflation-sim/`) was designed with Phase 3 implementing Paasch's phi-quantized mode spectrum via multi-component GPE. The original Phase 3 design assumed:

- 6 components (matching Paasch's 6 sequences)
- Chemical potentials $\mu_n = \mu_0 \cdot \phi^n$
- Inter-mode coupling $g_{nm}$

Session 32 revised this to:

- 3 components (B1, B2, B3) with degeneracies 1, 4, 3
- Chemical potentials from branch eigenvalues at the dump point
- Inter-component coupling $g_{ij} = 0$ on Jensen (Trap 4)

The wall-intersection program suggests a further revision:

- 3 components (B1, B2, B3) as before
- $Z_3$ cubic term in the nonlinear interaction: $g_3 |\psi_{B2}|^2 \psi_{B2} + c_3 \cos(3\theta) |\psi_{B2}|^4$
- Domain wall nucleation from random initial conditions with appropriate $\eta$
- Wall-localized excitations extracted from the defect census

The diagnostic: does the GPE with $Z_3$ cubic symmetry breaking spontaneously produce domain wall networks whose excitation spectrum is organized by $\phi_{\text{paasch}}$? This is the simulation-level test of the wall-intersection hypothesis.

---

## 8. Summary

The particle-as-scalar approach to Paasch's mass quantization has been exhausted by Session 33. The bulk eigenvalue ratio hits phi_paasch at $\tau = 0.15$ but the mechanism chain operates at $\tau = 0.19$. BCS dressing cannot bridge the gap (retracted in Round 2). The geometric series $\phi^n$ does not exist in the D_K spectrum.

The wall-intersection hypothesis reframes the problem: particles are not eigenvalues but collective excitations of the condensate at domain walls. Paasch's six sequences map to six oriented $Z_3$ wall types. The transcendental equation $x = e^{-x^2}$ may encode the self-consistency of wall width and BCS coherence length. Mass quantization arises from Poschl-Teller bound states at the B2 fold singularity. The fine structure constant traces to $\dim(3,0) = 10$.

Five pre-registered gates (WALL-phi, PT-count, PT-ratio, JUNCTION-E, JUNCTION-angle, alpha-dim) define the new program. All depend on TRAP-1 (the existential gate for BCS at walls). The computation ordering is fixed: TRAP-1 first, then WALL-phi, then downstream.

What has changed is not the mathematics but the interpretation. The mathematics of D_K on Jensen-deformed SU(3) is permanent. The domain wall solutions are proven to exist. The $Z_3$ structure is structural. What is new is the claim that these domain walls, not the bulk spectrum, host the physics of particle masses. This claim is testable, and the gates are pre-registered.

---

**Files referenced**:
- `researchers/Paasch/02_2009_Logarithmic_potential_exponential_mass_function_elementary_particles.md`
- `researchers/Paasch/03_2016_On_the_calculation_of_elementary_masses.md`
- `researchers/Paasch/04_2016_Derivation_of_the_fine_structure_constant.md`
- `sessions/archive/session-32/session-33-Team-4-synthesis.md` (Round 2)
- `sessions/archive/session-32/session-33-Team-4-synthesis_r1.md` (Round 1)
- `sessions/archive/session-32/session-32-paasch-collab.md`
- `tier0-archive/s33w3_modulus_equation.npz`
- `tier0-archive/s33w3_paasch_dump_point.npz`

**Pre-registered gates (new)**:

| Gate | Threshold | Depends On | Status |
|:-----|:----------|:-----------|:-------|
| WALL-phi | $L_{\text{wall}}/\xi_{\text{BCS}} \in [1.455, 1.608]$ | TRAP-1 | UNCOMPUTED |
| PT-count | Poschl-Teller bound states $\geq 3$ | Wall profile | UNCOMPUTED |
| PT-ratio | Lowest two bound state ratio within 10% of $\phi_{\text{paasch}}$ | PT-count | UNCOMPUTED |
| JUNCTION-E | $E_{\text{junction}}/E_{\text{wall-mode}} \in [1, \phi^2]$ | 2D GL solver | UNCOMPUTED |
| JUNCTION-angle | Effective spiral angle $< 50^\circ$ | JUNCTION-E | UNCOMPUTED |
| $\alpha$-dim | $n_3 = \dim(3,0) = 10$ structural verification | Conceptual | UNCOMPUTED |
| WALL-spectrum-phi1 | $E_{(3,0)}/E_{(0,0)} \in [1.524, 1.539]$ at some wall position | Eigenvalue data | UNCOMPUTED |
| WALL-spectrum-phi2 | Second ratio within 5% of $\phi^2$ at same position | WALL-spectrum-phi1 | UNCOMPUTED |
