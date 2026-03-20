# The Four Laws of Black Hole Mechanics

**Authors**: James M. Bardeen, Brandon Carter, Stephen W. Hawking
**Year**: 1973
**Journal**: *Communications in Mathematical Physics*, **31**, 161--170

---

## Abstract (Analytical Summary)

Bardeen, Carter, and Hawking establish four laws governing stationary black holes in general relativity that are in exact structural correspondence with the four laws of thermodynamics. The zeroth law states that the surface gravity $\kappa$ is constant over the event horizon of a stationary black hole. The first law relates changes in mass to changes in area, angular momentum, and charge. The second law is Hawking's area theorem. The third law conjectures that $\kappa = 0$ cannot be achieved in finite operations. Despite this perfect formal analogy, the authors argue that the correspondence is *merely* an analogy -- a position that Hawking himself would overthrow one year later.

---

## Historical Context

### From Area Theorem to Thermodynamic Analogy

By 1973, Bekenstein had already proposed (1972, 1973) that black hole area is proportional to entropy, $S_{\text{BH}} \propto A$. Hawking, Carter, and Bardeen were aware of this proposal and explicitly addressed it in the paper, ultimately rejecting it as physically meaningful. Their argument: a classical black hole has zero temperature because it absorbs everything and emits nothing. If $T = 0$, then the thermodynamic analogy breaks down at the quantitative level, even if the formal structure is suggestive.

This turned out to be wrong -- but the formal structure they established was exactly right, and it became the scaffolding for all subsequent work in black hole thermodynamics.

### The State of Black Hole Physics

The uniqueness theorems (Israel 1967, Carter 1971, Robinson 1975) were establishing the "no-hair" characterization of stationary black holes by mass $M$, angular momentum $J$, and electric charge $Q$. The Kerr--Newman solution provided the explicit metric. Smarr (1973) independently derived a mass formula for Kerr--Newman black holes. The stage was set for a systematic treatment.

---

## Key Arguments and Derivations

### Definitions and Setup

Consider a stationary, axisymmetric black hole spacetime (Kerr--Newman family). The spacetime admits a timelike Killing vector $\xi^a = (\partial/\partial t)^a$ and an axial Killing vector $\psi^a = (\partial/\partial \phi)^a$. On the event horizon $\mathcal{H}$, the Killing vector that is null on the horizon is:

$$\chi^a = \xi^a + \Omega_H \psi^a$$

where $\Omega_H$ is the angular velocity of the horizon. The **surface gravity** $\kappa$ is defined by:

$$\chi^b \nabla_b \chi^a = \kappa \, \chi^a \quad \text{on } \mathcal{H}$$

This says that $\chi^a$ is not affinely parameterized on the horizon; $\kappa$ measures the failure of affine parameterization, or equivalently, the "acceleration" needed for a static observer to hover just above the horizon (which diverges, but $\kappa$ is the appropriately redshifted limit).

For Schwarzschild: $\kappa = 1/(4M)$. For Kerr: $\kappa = \sqrt{M^2 - a^2} / (2M(M + \sqrt{M^2 - a^2}))$. For extremal Kerr ($a = M$): $\kappa = 0$.

### Zeroth Law

**Theorem**: The surface gravity $\kappa$ is constant over the event horizon of a stationary black hole.

The proof uses Einstein's equations and the dominant energy condition. There are two distinct proofs:

**Proof 1 (Bardeen--Carter--Hawking)**: For a stationary, axisymmetric black hole, one can show from the Killing vector identity:

$$\nabla_a \nabla_b \chi_c = R_{bcad} \chi^d$$

that $\kappa$ is constant along each generator of $\mathcal{H}$ (using the Killing equation). The constancy *across* generators (i.e., in the angular directions) follows from the dominant energy condition and the structure of the Einstein equations on the horizon.

**Proof 2 (Kay and Wald, 1991)**: A more elegant proof shows that $\kappa$ is constant on any bifurcate Killing horizon, purely from the geometry, without energy conditions.

**Thermodynamic analogue**: This is the analogue of the zeroth law of thermodynamics: in thermal equilibrium, the temperature $T$ is uniform throughout the system. The mapping is $T \leftrightarrow \alpha \kappa$ for some constant $\alpha$.

### First Law

**Theorem**: For a perturbation between nearby stationary black hole solutions (Kerr--Newman family):

$$\delta M = \frac{\kappa}{8\pi} \delta A + \Omega_H \, \delta J + \Phi_H \, \delta Q$$

where:
- $M$ is the total mass (ADM mass)
- $A$ is the horizon area
- $J$ is the angular momentum
- $Q$ is the electric charge
- $\Omega_H$ is the angular velocity of the horizon
- $\Phi_H$ is the electrostatic potential on the horizon

**Derivation**: The proof proceeds by considering a variation of the Kerr--Newman solution. The Smarr formula (integral version) is:

$$M = \frac{\kappa A}{4\pi} + 2\Omega_H J + \Phi_H Q$$

This can be derived from Komar integrals. The mass is expressed as a surface integral at infinity:

$$M = -\frac{1}{8\pi} \oint_{S^2_\infty} \nabla^a \xi^b \, dS_{ab}$$

Using Stokes' theorem and the Einstein equations, this can be related to a horizon integral:

$$M = \frac{\kappa A}{4\pi} + 2\Omega_H J + \Phi_H Q + \int_\Sigma (\text{matter terms})$$

For vacuum (electrovac), the matter terms contribute through the electromagnetic stress-energy. The factor of 2 multiplying $\Omega_H J$ in the Smarr formula (vs. 1 in the first law) reflects the scaling dimension: $M$, $J$, $Q$, and $A$ scale differently under $M \to \lambda M$.

The differential first law is then obtained by varying the Smarr formula, carefully accounting for the scaling. Alternatively, it can be derived directly by considering the effect of throwing a small particle into the black hole and computing the changes in $M$, $J$, $Q$, and $A$.

**Thermodynamic analogue**: This is the first law of thermodynamics:

$$dE = T \, dS + \text{work terms}$$

with the identification:
$$T \leftrightarrow \frac{\kappa}{2\pi}, \qquad S \leftrightarrow \frac{A}{4}$$

(The factors of $2\pi$ and $4$ were determined only after Hawking's 1974 discovery; at this stage, only the proportionality was established.)

The work terms $\Omega_H \, \delta J + \Phi_H \, \delta Q$ are analogous to $-p \, dV + \mu \, dN$ in ordinary thermodynamics. The angular velocity $\Omega_H$ is like a chemical potential for angular momentum, and $\Phi_H$ is a chemical potential for charge.

### Second Law

**Theorem** (Hawking, 1971): In any classical process,

$$\delta A \geq 0$$

This was proved in Hawking's 1971 paper (see the previous analysis). It requires the null energy condition and cosmic censorship.

**Thermodynamic analogue**: The second law of thermodynamics, $\delta S \geq 0$.

### Third Law

**Conjecture**: It is impossible to reduce $\kappa$ to zero by a finite sequence of physical operations.

This is stated as a conjecture, not a theorem. Israel (1986) later provided a rigorous proof under certain assumptions. The physical content is that one cannot create an extremal black hole ($\kappa = 0$, i.e., $a = M$ for Kerr or $Q = M$ for Reissner--Nordstrom) by any finite process.

**Argument**: To make a Kerr black hole extremal, one would need to add angular momentum without adding enough mass. But each particle that falls in increases both $J$ and $M$, and the cosmic censorship conjecture prevents $J$ from exceeding $M^2$. As $a \to M$, the energy cost of increasing $J$ further diverges -- it takes an infinite number of steps.

More precisely, for a near-extremal Kerr black hole:
$$\kappa = \frac{\sqrt{M^2 - a^2}}{2M r_+} \approx \frac{\sqrt{M^2 - a^2}}{2M^2}$$

To reduce $\kappa$ by a factor of 2, one must reduce $M^2 - a^2$ by a factor of 4. The process is asymptotic: $\kappa \to 0$ is approached but never reached.

**Thermodynamic analogue**: The third law of thermodynamics (Nernst's theorem): $T = 0$ cannot be achieved in finite steps. More precisely, as $T \to 0$, the entropy approaches a constant (zero for a perfect crystal). For black holes, as $\kappa \to 0$, the extremal black hole has $A = 8\pi M^2 > 0$ (Kerr) -- a nonzero "ground state entropy."

This last point (nonzero extremal entropy) is actually in tension with the *strong* form of the third law and is connected to deep questions about the microscopic description of extremal black holes.

---

## Physical Interpretation

### The Table of Correspondences

| Thermodynamics | Black Hole Mechanics |
|---|---|
| Temperature $T$ | Surface gravity $\kappa / 2\pi$ |
| Entropy $S$ | Area $A / 4\ell_P^2$ |
| Energy $E$ | Mass $M$ |
| Pressure $\times$ Volume, $p \, dV$ | $\Omega_H \, dJ + \Phi_H \, dQ$ |
| Zeroth law: $T$ uniform in equilibrium | $\kappa$ uniform on horizon |
| First law: $dE = T \, dS + \text{work}$ | $dM = \frac{\kappa}{8\pi} dA + \ldots$ |
| Second law: $\delta S \geq 0$ | $\delta A \geq 0$ |
| Third law: $T = 0$ unattainable | $\kappa = 0$ unattainable |

### Why BCH Rejected the Physical Identification

Bardeen, Carter, and Hawking argued that $\kappa$ cannot literally be a temperature because:

1. A classical black hole absorbs everything and emits nothing, so its "temperature" should be zero.
2. If $T \propto \kappa$ and $S \propto A$, then a black hole of one solar mass has $S \sim 10^{77} k_B$ -- far larger than the entropy of the matter that formed it. Where does this entropy come from?
3. The second law (area increase) is a theorem of differential geometry, not statistical mechanics. It requires no notion of microstates.

These objections were all answered by Hawking's 1974--1975 work: quantum effects *do* cause black holes to radiate at temperature $T = \hbar \kappa / 2\pi k_B$, the entropy *is* $A/4\ell_P^2$ (and reflects the information hidden behind the horizon), and the area theorem is the classical limit of a fundamentally quantum-statistical law.

---

## Impact and Legacy

### Foundation of Black Hole Thermodynamics

This paper, along with Bekenstein (1973) and Hawking (1974, 1975), constitutes the foundation of black hole thermodynamics. The four laws have been generalized to:

- **Higher-dimensional black holes** (Myers and Perry, 1986)
- **Black holes in AdS** (Hawking and Page, 1983)
- **Black holes in string theory** (Strominger and Vafa, 1996)
- **Dynamical horizons** (Ashtekar and Krishnan, 2003)
- **Holographic entanglement entropy** (Ryu and Takayanagi, 2006)

### Wald's Generalization

Wald (1993) generalized the first law to arbitrary diffeomorphism-covariant theories of gravity (not just Einstein's). The entropy is no longer $A/4$ but is given by the Noether charge:

$$S = -2\pi \oint_{\mathcal{H}} \frac{\partial \mathcal{L}}{\partial R_{abcd}} \, \hat{\epsilon}_{ab} \hat{\epsilon}_{cd} \, dA$$

where $\hat{\epsilon}_{ab}$ is the binormal to the horizon. For Einstein gravity ($\mathcal{L} = R/16\pi G$), this reduces to $A/4G$.

### Extended Black Hole Thermodynamics

In 2009, Kastor, Ray, and Traschen introduced "extended" black hole thermodynamics where the cosmological constant $\Lambda$ is treated as a thermodynamic variable (pressure: $P = -\Lambda/8\pi$). This gives black holes a $PV$ term and allows the study of phase transitions analogous to van der Waals fluids. The Hawking--Page transition (1983) between thermal AdS and large AdS black holes was reinterpreted as a liquid--gas phase transition.

---

## Connections to Modern Physics

1. **AdS/CFT**: The black hole thermodynamic laws, when applied to AdS black holes, are dual to thermodynamic properties of the boundary CFT. The Hawking--Page transition corresponds to the deconfinement transition in large-$N$ gauge theory (Witten, 1998).

2. **Entanglement thermodynamics**: The first law of entanglement entropy in CFT, $\delta S = \delta \langle H_{\text{mod}} \rangle$, is dual to the linearized gravitational first law via the Ryu--Takayanagi formula. This is a key entry in the "gravity from entanglement" program.

3. **Microstate counting**: String theory provides explicit microstate counting for certain extremal and near-extremal black holes (Strominger and Vafa, 1996), reproducing $S = A/4\ell_P^2$ exactly. This is the strongest evidence that the BCH laws are truly thermodynamic in origin.

4. **Phonon analogues**: In analogue gravity (Unruh, 1981), acoustic black holes in superfluids have horizon-like structures where the four laws have direct analogues. The surface gravity is related to the gradient of flow velocity at the sonic horizon. This connection is especially relevant for BEC-based phonon models.

5. **For the exflation framework**: If the internal Kaluza--Klein dimensions participate in horizon formation, the first law acquires additional "work terms" for the moduli fields (internal geometry parameters). The exflation mechanism (internal space evolution) would modify the black hole thermodynamics by coupling the horizon area to the compactification scale $\sigma$, potentially providing observable signatures in primordial black hole evaporation.
