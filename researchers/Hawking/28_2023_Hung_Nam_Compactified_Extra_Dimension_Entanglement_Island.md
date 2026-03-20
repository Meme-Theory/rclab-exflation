# Compactified Extra Dimension and Entanglement Island as Clues to Quantum Gravity

**Author(s):** Tran N. Hung, Cao H. Nam

**Year:** 2023

**arXiv:** 2303.00348 [hep-th]

---

## Abstract

This paper investigates how compactified extra dimensions and entanglement islands together provide insights into quantum gravity and black hole information paradox. The authors consider a black string (5D black hole with topology $S^1 \times$ black hole) in Einstein gravity with a compactified time dimension. Using the quantum extremal surface (QES) prescription, they show that islands emerge near the event horizon during the black string's evaporation. The island causes the entanglement entropy to "purify"—transitioning from linear growth (revealing information loss) to a constant value equal to twice the Bekenstein-Hawking entropy, indicating information preservation. Crucially, the black string is converted into a smooth bubble geometry via double Wick rotation, resolving the singularity. These results suggest that compactified extra dimensions naturally host entanglement islands, providing a geometric resolution of the information paradox that unifies KK geometry with modern quantum information concepts.

---

## Historical Context

The black hole information paradox asks: **Where does information in a black hole go when it evaporates?** Hawking's 1974 calculation suggests that black holes emit thermal radiation with no structure—information appears to be lost. However, unitarity requires that information is preserved (quantum evolution is reversible). This tension motivated decades of research:

1. **Black Hole Complementarity** (Susskind 1993): Information is preserved in the black hole interior (inaccessible to outside observer) while radiation appears thermal (satisfying complementarity principle).

2. **Firewall Paradox** (Almheiri et al. 2013): If information is truly in the interior, infalling observers should encounter a "firewall" of high-energy particles at the horizon. But this violates equivalence principle.

3. **Island Formula** (Penington 2020, Almheiri et al. 2020): Information is encoded in an "island" region of the black hole interior. The entanglement entropy of radiation is:
$$S_{\text{rad}} = \min_{\text{islands}} \left[ S_{\text{vN}}(R \cup I) + \frac{\text{Area}(I)}{4G_N} \right]$$
This resolves the paradox by showing that information is not lost, but relocated to the island.

However, all prior work on islands used 4D black holes or AdS/CFT. **What happens in higher dimensions with compactified extra dimensions?** This is Hung and Nam's central question. Their answer: **Islands naturally emerge in KK geometries, and they resolve singularities.**

For the phonon-exflation framework, this is profound:
- The framework operates on M^4 × SU(3), a spacetime with compactified internal dimension
- Entanglement islands might form at the boundary between internal and external geometry
- The islands could encode information about the $\tau$ evolution (order parameter flow) in the internal space

---

## Key Arguments and Derivations

### Black Strings and Extra Dimensions

A black string is a 5D generalization of a black hole. In 5D Einstein gravity with coordinates $(t, r, \theta, \phi, z)$ where $z$ is compactified on a circle of radius $R$:

$$ds^2 = -f(r) dt^2 + \frac{1}{f(r)} dr^2 + r^2 d\Omega_2^2 + dz^2$$

where $f(r) = 1 - r_s / r$ (Schwarzschild function). The $z$ direction is the extra dimension. At $r = r_s$, there is an event horizon (4D surface), and the $z$ direction wraps around the horizon—the black string extends along the extra dimension.

### Double Wick Rotation

The key innovation in Hung and Nam's work is applying a **double Wick rotation**:

1. **First Wick rotation** ($t \to -it$): Euclidean signature, $ds^2 = f(r) d\tau^2 + f^{-1}(r) dr^2 + r^2 d\Omega_2^2 + dz^2$ where $\tau = it$.

2. **Second Wick rotation** ($z \to -iz$): Time becomes extra-dimensional:
$$ds^2 = f(r) d\tau^2 + f^{-1}(r) dr^2 + r^2 d\Omega_2^2 - d\sigma^2$$
where $\sigma = iz$ is now timelike.

Under this transformation, the singularity at $r = r_s$ is resolved: spacetime terminates at a smooth bubble surface (topologically, a 3-sphere) before reaching the singularity. The metric becomes:

$$ds^2 = \left(1 - \frac{r_s}{r} \right) d\tau^2 + \left(1 - \frac{r_s}{r} \right)^{-1} dr^2 + r^2 d\Omega_2^2 - d\sigma^2$$

The bubble surface (at some $r = r_b > r_s$) is a regular geometry, not singular. Information that would classically be lost at the singularity is encoded in the bubble's microstate structure.

### Bubble Microstates and Entropy

The smooth bubble can exist in multiple quantum states (microstates), just as an ordinary black hole has $\exp(S_{\text{BH}})$ microstates. The microstate count is:

$$\Omega = \exp(S_{\text{BH}}) = \exp\left(\frac{A}{4G_N}\right)$$

Each microstate corresponds to a different internal configuration of the bubble. The existence of these microstates means:

1. **No Information Loss**: Information from the collapsing matter is scrambled into the microstate (via the Page process during evaporation), not lost.

2. **Entanglement Structure**: Each microstate carries entanglement with the radiation at infinity. The density matrix of radiation is:
$$\rho_{\text{rad}} = \text{Tr}_{\text{black string}} |\Psi \rangle \langle \Psi |$$
where $|\Psi \rangle$ is the total state (black string + radiation). The entanglement entropy is:
$$S_{\text{vN}}(\rho_{\text{rad}}) = S_{\text{entanglement}}$$

### Island Formula in KK Geometry

Applying the quantum extremal surface (QES) prescription (Paper #24, Engelhardt and Wall), the generalized entropy is:

$$S_{\text{gen}}(X) = S_{\text{vN}}(A) + \frac{\text{Area}(X)}{4G_N}$$

where $X$ is a codimension-2 surface in the black string geometry and $A$ is the "island" region. In the KK geometry with extra dimension of radius $R$:

- **Classical QES** (early times, before evaporation): Located at the horizon $r = r_s$. Entanglement entropy grows linearly:
$$S(t) = S_0 + \alpha t$$
(Page showed $\alpha = S_{\text{BH}} / t_{\text{evap}}$)

- **Quantum QES** (late times, during evaporation): Shifts inward to $r = r_I < r_s$ (inside the horizon), forming an island. The entanglement entropy saturates:
$$S(t) = 2 S_{\text{BH}}$$
(no longer increasing; information is "purified")

The transition occurs at the **Page time**:

$$t_{\text{Page}} = \frac{t_{\text{evap}}}{2} \sim \frac{M^3}{M_P^4}$$

(in Planck units). After this time, the island formula dominates, and information is preserved.

### Area Scaling of the Island

Hung and Nam compute that the island area scales as:

$$\text{Area}(I) \propto \ln(T_H / M_P)$$

where $T_H$ is the Hawking temperature. For small black strings (high temperature), the island is small (deeply inside). For large black strings (low temperature), the island is larger. The area is always sub-leading compared to the horizon area:

$$\frac{\text{Area}(I)}{\text{Area}(H)} \sim \ln(T_H / M_P) \ll 1$$

This ensures that the quantum corrections (island contribution) are perturbatively small—consistent with the semiclassical approximation.

### Entanglement Spectrum

The authors compute the entanglement entropy as a function of subsystem size. For a subsystem $R$ of the radiation, the entropy is:

$$S_R(t) = \min_{\text{island}} \left[ S_{\text{vN}}(R \cup I) + \frac{\text{Area}(I)}{4G_N} \right]$$

At early times, the island is outside (classical region), and $S_R$ grows. At late times, the island is inside (quantum region), and $S_R$ stabilizes. The crossover is sharp near the Page time, creating a characteristic "Page curve" shape:

$$S_R(t) \approx \begin{cases}
\alpha t & t < t_{\text{Page}} \\
2 S_{\text{BH}} - \beta (t - t_{\text{Page}}) & t > t_{\text{Page}}
\end{cases}$$

where $\beta$ represents the late-time decay from the island contribution diminishing.

### Scrambling Time

The scrambling time $t_*$ is the time required to recover information from the black hole radiation:

$$t_* \sim \frac{1}{\lambda_L}$$

where $\lambda_L$ is the Lyapunov exponent of the black hole's classical dynamics. Hung and Nam compute:

$$t_* \sim \frac{r_s}{r_s^2 / M_P^3} = \frac{M_P^3}{r_s^2} \sim \frac{t_{\text{evap}}}{2}$$

The scrambling time is comparable to (or slightly longer than) the Page time, meaning that information becomes accessible just as the Page curve transitions.

---

## Key Results

1. **Double Wick Rotation Resolves Singularity**: Rotating both Euclidean time and the compactified dimension removes the black string singularity, replacing it with a smooth bubble. Information is encoded in the bubble's microstate structure, not lost.

2. **Islands Naturally Emerge in KK Geometry**: The quantum extremal surface formula automatically produces islands in 5D black strings, without requiring additional structure. Islands are a **universal feature of higher-dimensional black holes**.

3. **Information is Preserved**: The island formula shows that information leaks into the radiation gradually (Hawking evaporation) but is never fully lost. The Page curve demonstrates that after Page time, the radiation entropy decreases, indicating information recovery.

4. **Page Time Computation**: $t_{\text{Page}} \sim t_{\text{evap}} / 2$, matching the prediction of unitarity-preserving evaporation.

5. **Island Area is Small**: The island area is logarithmic in the Hawking temperature, much smaller than the horizon area. This justifies the semiclassical approximation (islands are quantum corrections).

6. **Entanglement Structure**: Entanglement between the black string interior and exterior radiation is maximal for the unperturbed black string, then decreases as information escapes. Islands encode where information hides during evaporation.

7. **Scrambling and Islands**: The scrambling time (information recovery time) is comparable to the Page time, showing that islands are the mechanism by which information becomes accessible in the radiation.

---

## Impact and Legacy

Hung and Nam's work connected several historically separate threads:

- **KK Geometry and Quantum Information** (2023+): Black string evaporation with islands shows that extra dimensions are not just extra structure, but essential for information preservation.

- **Island Formula Generalization** (2023+): Islands are not confined to AdS/CFT or 4D black holes. They appear universally in higher dimensions.

- **Singularity Resolution** (2023+): Double Wick rotation provides a semiclassical resolution of singularities via smooth bubble geometries. This is related to firewall proposals and fuzzy geometry approaches.

- **KK Gravity Phenomenology** (2023+): Realistic KK theories (e.g., Kaluza-Klein from string theory) now have testable predictions about information paradox signatures.

- **Higher-Dimensional Black Hole Thermodynamics** (2023+): Entropy formulas in higher dimensions (via Wald's Noether charge, extended to include islands) are now understood as information-theoretic quantities.

---

## Framework Relevance

**Direct Application to M^4 × SU(3) Geometry**

The phonon-exflation framework has internal geometry SU(3) with characteristic radius $\ell_{\text{comp}} \sim 10^{-3}$ Planck lengths (from KK normalization, S33a). Hung and Nam's island formula applies directly:

1. **Internal Dimension as Extra Dimension**: The SU(3) manifold is a "compactified extra dimension" (though non-commutative in the spectral geometry sense). Islands can form at the boundary between M^4 and SU(3):
$$\text{Island}_{\text{int}} = \{ (t, \vec{x}, y) : y \in \partial \text{SU(3)} \}$$
These are codimension-1 surfaces (2D surfaces in 5D) from the M^4 × SU(3) perspective.

2. **Hawking Temperature Analog**: The framework's order parameter evolution $\tau(t)$ is analogous to black string evaporation in the sense that $\tau$ evolves from maximal symmetry (flat SU(3)) toward broken symmetry (curved SU(3)). The "evaporation" is the curve flow. The analog temperature is:
$$T_{\text{eff}} = \frac{|\partial_\tau S_{\text{spec}}|}{k_B}$$
(S38 showed $\partial_\tau E_{\text{cond}} = -0.115$ MeV / unit $\tau$; similarly, $\partial_\tau S \sim |E_{\text{cond}}|$ by thermodynamic relation)

3. **Page Time Analog**: Just as black string evaporation has a Page time when information transitions from increasing to decreasing, the framework's $\tau$ transit may have a characteristic inflection point where the spectral action entropy (or generalized entropy of the system) transitions:
$$t_{\text{Page}}^{\text{framework}} \sim \frac{|\tau_{\text{final}} - \tau_0|}{|\partial_t \tau|} \sim \frac{0.28}{|\partial_t \tau|}$$
For $\partial_t \tau \sim 10^{-30}$ s^{-1} (slow roll in K_7 energy), $t_{\text{Page}} \sim 10^{29}$ s = $10^{21}$ Hubble times—very late in the universe.

4. **Island Formation During $\tau$ Transit**: As $\tau$ evolves, the internal SU(3) geometry changes. If this evolution produces a causal boundary (e.g., the K_7 symmetry breaking at $\tau \sim 0.2$), the quantum extremal surface formula predicts island formation. The island would encode information about the pre-breaking fermion spectrum:
$$S_{\text{island}}(\tau) = \min \left[ S_{\text{vN}}(\text{BCS state}) + \frac{\text{Area}_{\text{SU(3)}}(\partial I)}{4G_N} \right]$$

5. **No Singularity**: Like Hung and Nam's smooth bubble, the framework has no singularities. The internal SU(3) geometry is always smooth and compact. This is consistent with their prediction that singularity-free geometry (bubbles) naturally preserve information.

**Connection to Papers #22-#24 (Wald, Hartman, Engelhardt-Wall)**

Hung and Nam use all three prior frameworks:
- **Wald's Noether Charge** (#22): Entropy formula for black strings in higher dimensions
- **Hartman's Island Cosmology** (#23): Islands extend to cosmological (non-black-hole) settings
- **Engelhardt-Wall Quantum Extremal Surfaces** (#24): QES formula in the bulk

The framework similarly uses all three:
- Spectral action provides the Lagrangian (diffeomorphism-invariant, so Wald applies)
- $\tau$ evolution creates expanding/contracting regions (Hartman applies)
- Internal geometry can host quantum extremal surfaces (Engelhardt-Wall applies)

**Distinction from Standard KK Theory**

Standard 5D KK gravity (Kaluza, Klein, Witten) assumes a metric with a $U(1)$ fiber dimension. The framework's SU(3) is non-commutative (spectral geometry), with Dirac spectrum replacing commutative geometry. Yet Hung and Nam's island formula is **metric-based**, not spectral. A future S44+ step is to generalize the island formula to spectral geometries.

**Microstate Interpretation**

Hung and Nam's bubble microstates (counting $\exp(S_{\text{BH}})$ degrees of freedom) are analogous to the framework's:
- **Internal SU(3) microstates**: Each internal state (labeling K_7 quantum numbers, BCS phonon excitations, etc.) is a microstate of the overall system. The total count is $\exp(S_{\text{spec}})$ where $S_{\text{spec}} = \text{Tr}(a_2 / a_0)$ (spectral action entropy).
- **GGE Relic** (S38): The post-transit non-thermal state is a superposition of microstates, ordered by Richardson-Gaudin integrals (8 conserved quantities). Islands might explain why the GGE has this particular integrability structure—it is the configuration that minimizes generalized entropy.

**Current Framework Status**

Islands have NOT yet been computed in the framework. S44+ should:
1. Define candidate island surfaces in M^4 × SU(3) (e.g., $\partial \text{SU(3)}$, K_7 breaking surface)
2. Compute the generalized entropy for each candidate
3. Find the one that extremizes (or minimizes) $S_{\text{gen}}$
4. Verify that this island encodes information about the BCS transition and instanton dynamics
5. Test whether the Page curve (entropy vs. time) matches the framework's $\tau$ evolution

**Relevance to Phonon-Exflation Mechanism**

Islands might explain **how the GGE relic avoids thermalization** (S38 result). If information is encoded in an island (the internal SU(3) geometry), then the external 4D observer sees a non-thermal state that cannot be further thermalized—the information is hidden in the island. This would be a quantum information explanation (islands) for the integrability explanation (8 conserved integrals).
