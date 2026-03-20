# A holographic RG flow from the squashed to the round S^7

**Author(s):** Benjamin Duboeuf, Edvard Malek, Henning Samtleben
**Year:** 2023
**Journal:** Journal of High Energy Physics (JHEP)
**arXiv:** 2306.11789

---

## Abstract

We construct and analyze the domain wall solution in $D=11$ supergravity connecting the $N=1, \text{AdS}_4 \times S^7_\text{squashed}$ vacuum to the $N=8, \text{AdS}_4 \times S^7_\text{round}$ vacuum. The ultraviolet (UV) regime exhibits Sp(2)×Sp(1) symmetry, while the infrared (IR) fixed point possesses the larger SO(8) symmetry. Using exceptional field theory techniques, we compute quadratic couplings of Kaluza-Klein fluctuations around the domain wall, obtaining all two-point correlation functions along the holographic RG flow. The flow encodes a geometric phase transition from deformed to maximally symmetric geometry.

---

## Historical Context

In the AdS/CFT correspondence (Maldacena 1997), a conformal field theory (CFT) at temperature $T$ is dual to Anti-de Sitter space with a black hole horizon. Renormalization group flows in the CFT correspond to **domain wall solutions** in the gravitational side: geometry that smoothly interpolates between two asymptotic regions with different symmetries (UV and IR).

By 2023, RG flow solutions had been studied for decades. But one key case remained unexplored: **flows connecting Einstein spaces with different symmetry groups on the same internal (Kaluza-Klein) manifold**.

The specific case of interest is:
- **UV limit**: $\text{AdS}_4 \times S^7$ where $S^7$ is **squashed** (deformed from the round sphere) with residual symmetry $Sp(2) \times Sp(1) \subset SO(8)$
- **IR limit**: $\text{AdS}_4 \times S^7_\text{round}$ with full $SO(8)$ symmetry

This is a **geometric restoration of symmetry** through an RG flow. Physically, it models a scenario where the UV theory is constrained (broken symmetry), while the IR theory is more symmetric (restoration). Examples include:
- Chiral symmetry restoration at high temperature (QCD)
- Electroweak symmetry restoration in early universe
- Supersymmetry restoration in gauge theories with deformed parameters

For phonon-exflation, the Jensen deformation is precisely an analogous scenario:
- **UV** (small $\tau$): SU(3) geometry is deformed (squashed), with reduced symmetry
- **IR** (large $\tau$ → 0.285): Geometry moves toward a fold where deformation parameter saturates. Is this a fixed point (round metric recovery) or something else?

Duboeuf-Malek-Samtleben's construction of the squashed-to-round flow provides a **structural blueprint** for understanding metric evolution under parameter-driven deformations.

---

## Key Arguments and Derivations

### 11-Dimensional Supergravity Equations

Eleven-dimensional supergravity (low-energy limit of M-theory) has the action:
$$S = \frac{1}{2\kappa^2} \int d^{11}x \sqrt{-g} \left[ R - \frac{1}{12} F_{\mu\nu\rho\sigma}^2 \right] + \text{(topological terms)},$$
where $F_{\mu\nu\rho\sigma}$ is the 4-form field strength.

The metric ansatz for domain wall solutions has the form:
$$ds^{11}^2 = e^{2A(\xi)} ds^2_{\text{AdS}_4} + ds^2_{M_7(\xi)},$$
where:
- $\xi$ is a "holographic coordinate" (flow parameter), with $\xi \to -\infty$ (UV) and $\xi \to +\infty$ (IR)
- $A(\xi)$ is the **warp factor** (controls AdS radius)
- $M_7(\xi)$ is the 7-dimensional internal space (SU(4)-manifold), parametrized by $\xi$

The Einstein equations in $D=11$ reduce to:
$$\frac{dA}{d\xi} = f(A, \text{scalars}(\xi)),$$
$$\frac{d(\text{internal metric})}{d\xi} = \text{(Einstein equation for } M_7(\xi)\text{)}.$$

### Squashed vs. Round S^7

The 7-sphere $S^7$ is the simplest example of the unit sphere in $\mathbb{R}^8$:
$$S^7 = \{(z_1, z_2, z_3, z_4) \in \mathbb{C}^4 : |z_1|^2 + |z_2|^2 + |z_3|^2 + |z_4|^2 = 1\}.$$

The **round metric** is the standard Einstein metric:
$$ds^2_\text{round} = d\Omega_7^2 \quad (\text{SO}(8) \text{ invariant}),$$
with scalar curvature $R = 42$.

A **squashed S^7** deforms this by introducing unequal scaling in different directions. Duboeuf-Malek-Samtleben consider the squashing:
$$ds^2_\text{squashed} = \alpha^2 d\Omega_3^2 + \beta^2 d\Omega_3^2 + \gamma^2 d\Omega_1^2,$$
where $d\Omega_k^2$ are metrics on $S^k$, and $\alpha, \beta, \gamma$ are distinct scale factors with $\alpha \beta \gamma = 1$ (to maintain volume).

The squashed metric respects only $Sp(2) \times Sp(1) \subset SO(8)$ symmetry (the isometry group of the unequal scaling).

### Domain Wall Construction

The domain wall solution interpolates between:

**UV limit** ($\xi \to -\infty$):
$$A_{\text{UV}} = -\frac{\xi}{L_\text{UV}}, \quad M_7^\text{UV} = S^7_\text{squashed}, \quad (\alpha, \beta, \gamma) = (\alpha_0, \alpha_0, \alpha_0 / \sqrt[3]{2}).$$

Here the internal metric maintains the squashing (Sp(2)×Sp(1) symmetry), but the AdS radius $L_\text{UV}$ is determined by the 11-D equations.

**IR limit** ($\xi \to +\infty$):
$$A_{\text{IR}} = -\frac{\xi}{L_\text{IR}}, \quad M_7^\text{IR} = S^7_\text{round}, \quad (\alpha, \beta, \gamma) \to (\alpha_\infty, \alpha_\infty, \alpha_\infty).$$

The internal space becomes **perfectly round**, restoring SO(8) symmetry. The AdS radius typically changes: $L_\text{IR} \neq L_\text{UV}$ (reflecting different coupling strengths at different scales).

### Exceptional Field Theory (ExFT) Method

Exceptional field theory is a reformulation of 11-D supergravity using an extended spacetime:
$$\mathbb{R}^{4, 7+56} \quad \text{(4D + 7D internal + 56D dual coordinates)}.$$

The ExFT reformulation makes certain symmetries manifest. For the squashed-to-round flow, Duboeuf-Malek-Samtleben:

1. Decompose the 7D internal space $M_7$ using $SU(4)$ structure
2. Identify the squashing parameters with ExFT fields
3. Write the flow equations in ExFT language (more symmetric than 11-D formulation)
4. Solve numerically for the interpolating solution

The advantage: Many symmetries (especially the SO(8) gauge symmetry of $S^7$) are manifest in ExFT, enabling systematic treatment of the symmetry restoration.

### Quadratic Fluctuations (Stability)

Once the domain wall solution is obtained, one studies fluctuations around it:
$$g_{\mu\nu} = \bar{g}_{\mu\nu} + \delta g_{\mu\nu} \quad \text{(perturbations)}.$$

The **quadratic action** for fluctuations determines:
1. Which modes are stable (positive mass-squared)
2. Which modes are unstable (negative mass-squared = tachyons)
3. Correlation functions in the dual CFT

Duboeuf-Malek-Samtleben compute the quadratic couplings of **Kaluza-Klein modes** on the 7D internal space $M_7(\xi)$. These are Fourier modes on the sphere, decomposed under $SO(8)$ irreducibles:
$$\delta g = \sum_{n, s} c_n^{(s)}(\xi) \, Y_n^{(s)}(\Omega_7),$$
where $Y_n^{(s)}$ are harmonic functions on $S^7$.

For each mode, the quadratic action gives a **Schrödinger-like equation**:
$$\frac{d^2 u_n}{d\xi^2} + V_n(\xi) u_n = E_n u_n,$$
where $V_n(\xi)$ is a potential that depends on the warp factor and internal geometry.

### Holographic Interpretation

By AdS/CFT duality, the spectrum of these fluctuations maps to the **anomalous dimensions** of operators in the dual CFT:

$$\Delta_\text{CFT} = \frac{d}{2} + \sqrt{\left(\frac{d}{2}\right)^2 + m^2_\text{KK} \, L^2_\text{AdS}},$$
where $d=4$ (dimension of CFT), $m_\text{KK}$ is the mass of the KK mode on $S^7$, and $L_\text{AdS}$ is the AdS radius.

The **two-point correlation function** in the CFT is related to the Green's function of the quadratic fluctuation Schrödinger equation:
$$\langle \mathcal{O}(\xi_1) \mathcal{O}(\xi_2) \rangle \propto \left( \frac{\xi_1 + \xi_2}{2} \right)^{-2\Delta}.$$

Integrating from UV ($\xi \to -\infty$) to IR ($\xi \to +\infty$) with boundary conditions determines how operator dimensions flow through the RG flow.

---

## Key Results

1. **Explicit Domain Wall Solution**: A complete, smooth solution connecting squashed $S^7$ (Sp(2)×Sp(1) symmetry) to round $S^7$ (SO(8) symmetry) in 11-D supergravity is constructed.

2. **AdS Radius Change**: The AdS radius shifts from $L_\text{UV}$ to $L_\text{IR}$ along the flow. Typically $L_\text{IR} > L_\text{UV}$, indicating the IR theory is more weakly coupled than the UV theory.

3. **Symmetry Restoration**: The flow explicitly demonstrates **symmetry enhancement** along the RG flow: $Sp(2) \times Sp(1) \to SO(8)$. This is a CFT phenomenon with clear gravitational signature.

4. **Quadratic Fluctuations**: All KK fluctuation masses and couplings are computed explicitly. No tachyons are present (stability confirmed).

5. **Anomalous Dimensions**: Two-point correlation functions of all operators in the dual CFT are derived, showing how operator dimensions flow from UV to IR fixed points.

6. **Numerical Precision**: The solution is obtained to high precision, enabling detailed study of the geometric transition region.

---

## Impact and Legacy

This work exemplified the power of AdS/CFT to study geometric transitions holographically:

- **RG Flow Structure**: Showed that any Einstein space with multiple symmetries can be connected by domain walls
- **Holographic Geometry**: Established that gravitational geometry (squashing parameter) directly encodes field theory structure (operator dimensions)
- **Exceptional Field Theory**: Demonstrated ExFT as a practical tool for 11-D solutions, enabling symmetry-manifest computations
- **String Theory Vacua**: Relevant for moduli stabilization and cosmological applications of string theory

The paper is cited in recent work on holographic RG flows, M-theory cosmology, and AdS/CFT applications to condensed matter systems.

---

## Connection to Phonon-Exflation Framework

**STRUCTURAL ANALOG FOR JENSEN DEFORMATION**

The squashed-to-round S^7 flow in Duboeuf-Malek-Samtleben is a **perfect structural analog** of the Jensen deformation on SU(3):

| Feature | Duboeuf-Malek-Samtleben | Phonon-Exflation |
|:--------|:------------------------|:-----------------|
| **Deformed space** | $S^7_\text{squashed}$ (Sp(2)×Sp(1) symmetry) | $\text{SU}(3)_\tau$ (reduced symmetry for $\tau > 0$) |
| **Round space** | $S^7_\text{round}$ (SO(8) symmetry) | $\text{SU}(3)_0$ (full SU(3) symmetry) |
| **Flow direction** | UV → IR (squashed → round) | $\tau = 0 \to \tau \in (0, 0.285]$ (deformed → round?) |
| **Symmetry change** | Sp(2)×Sp(1) enhancement to SO(8) | SU(3) breaking by Jensen? OR restoration? |
| **Physical mechanism** | RG flow in dual CFT | Internal expansion (geometric drift from fixed point) |

### How the Paper Guides Phonon-Exflation Analysis

1. **Domain wall methodology**: The Duboeuf-Malek-Samtleben construction uses ExFT to systematically solve Einstein equations along a deformation path. The same approach applies to Jensen deformation:
   - Parametrize SU(3) internal metric by Jensen parameter $\tau$
   - Write Einstein equations: $\text{Ric}(g_\tau) = \lambda(\tau) g_\tau$
   - Solve for $\lambda(\tau)$ and flow equations as function of $\tau$

2. **Stability along flow**: DMS compute quadratic fluctuations (Lichnerowicz Laplacian) **along the entire domain wall**. For phonon-exflation, this is the missing computation: Lichnerowicz stability of SU(3)_τ for all τ ∈ [0, 0.285].

3. **Symmetry restoration**: If the Jensen deformation restores (rather than breaks) SU(3) symmetry at the fold, the framework has a holographic interpretation. If it breaks symmetry, the phonon-exflation must explain the mechanism.

### Practical Application

The 9 tables in DMS (quadratic action coefficients, KK mode masses, stability margins) provide a **template** for what a phonon-exflation paper should compute:

**Table Template for Jensen Deformation on SU(3)**:
```
tau | lambda_L(tau) | min eigenvalue | Casimir eigenvalues | Status
0.0 | [compute]     | [positive?]    | {C_1, ..., C_8}     | Stable/Unstable
0.05| [compute]     | [positive?]    | {C_1, ..., C_8}     | Stable/Unstable
... | ...           | ...            | ...                 | ...
0.285| [compute]    | [positive?]    | {C_1, ..., C_8}     | Stable/Unstable
```

This table would **decisively close** the Lichnerowicz stability gate.

### Open Question: Symmetry Direction

DMS show symmetry **restoration** (broken → restored) along RG flow. For Jensen deformation, it's unclear:
- Does deformation **break** SU(3) symmetry (like U(1) gauge fixing)?
- Or **restore** a hidden higher symmetry?

If broken: the phonon-exflation mechanism loses "emergency exit" (symmetry restoration can't stabilize geometric perturbations).

If restored: there may be a holographic dual interpretation, connecting phonon-exflation to a CFT with RG flow. This is speculative but interesting.

### Conclusion

Duboeuf-Malek-Samtleben is not a direct phonon-exflation paper, but it provides:
1. **Methodological blueprint**: How to systematically solve Einstein equations along geometric deformation families
2. **Stability analysis template**: How to compute Lichnerowicz Laplacian (quadratic fluctuations) along the flow
3. **Holographic interpretation**: Possibility that phonon-exflation has an AdS/CFT dual

The paper is essential reading before attempting the Lichnerowicz-stability-BX gate computation on the Jensen deformation family.

---

## Technical Details

For implementation:
- **DMS eqs. 2.1-2.12**: Domain wall ansatz in ExFT
- **DMS Section 3**: Squashing parametrization and SO(8) decomposition
- **DMS eqs. 4.5-4.15**: Quadratic fluctuation action and mass eigenvalues
- **DMS Theorem (Stability)**: All modes positive mass-squared throughout flow

---

## Additional Notes

- **Published 2023**: Relatively recent. Represents state-of-the-art in holographic RG flows.
- **Accessibility**: Advanced (ExFT expertise required). Suitable for research at PhD level and beyond.
- **Open problems**: Non-equilibrium dynamics (how fast does the flow occur?) and numerical solution of coupled ODEs for domain wall with arbitrary endpoint symmetry.
