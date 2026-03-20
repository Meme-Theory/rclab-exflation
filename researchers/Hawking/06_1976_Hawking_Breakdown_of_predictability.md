# Breakdown of Predictability in Gravitational Collapse

**Authors**: Stephen W. Hawking
**Year**: 1976
**Journal**: *Physical Review D*, **14**, 2460--2473

---

## Abstract (Analytical Summary)

Hawking argues that the formation and evaporation of a black hole leads to an irreversible loss of quantum information, violating the unitarity of quantum mechanics. A pure quantum state describing collapsing matter evolves, through the formation and complete evaporation of a black hole, into a mixed state of thermal radiation. This process cannot be described by a unitary S-matrix; instead, Hawking proposes a "superscattering operator" $\$$ that maps density matrices to density matrices. This paper is the founding document of the black hole information paradox, which has been the central problem in theoretical physics for five decades and has driven developments from AdS/CFT to the island formula.

---

## Historical Context

### The Problem After Hawking Radiation

With the 1974--1975 discovery that black holes emit thermal radiation, two immediate questions arose:

1. Does the black hole evaporate completely?
2. If so, what happens to the information that fell in?

The first question is addressed by the negative heat capacity: $T \propto 1/M$ means the black hole heats up as it shrinks, radiating ever more intensely. Barring a stable remnant (which has problems of its own), the black hole evaporates completely.

The second question is the subject of this paper. If the initial state is pure (a specific quantum state of the collapsing matter) and the final state is thermal radiation (a mixed state described by a density matrix), then the evolution is non-unitary. Hawking embraced this conclusion and argued that it is a fundamental feature of quantum gravity.

### The Unitarity Principle

In standard quantum mechanics, time evolution is unitary: a pure state evolves to a pure state, and the von Neumann entropy $S = -\text{Tr}(\rho \ln \rho)$ is conserved. In scattering theory, the S-matrix $S: |i\rangle \to |f\rangle = S|i\rangle$ is unitary: $S^\dagger S = I$. This ensures that probabilities are conserved and that the past can, in principle, be reconstructed from the future.

Hawking's claim was that gravity violates this principle. Not approximately, not in some limit, but fundamentally.

---

## Key Arguments and Derivations

### The Setup: Collapse and Evaporation

Consider a quantum field theory of matter coupled to gravity. The initial state $|i\rangle$ is a pure state on a spacelike surface $\Sigma_1$ before the collapse. After the black hole forms and completely evaporates, the final state is defined on a spacelike surface $\Sigma_2$ to the future of the evaporation event.

The Penrose diagram of the process has:
- $\mathscr{I}^-$: past null infinity (ingoing matter)
- The collapsing star, forming a black hole
- The singularity at $r = 0$ inside the black hole
- The event horizon, which shrinks as the black hole evaporates
- $\mathscr{I}^+$: future null infinity (outgoing Hawking radiation)
- The evaporation endpoint (where the horizon shrinks to zero size)

### The Information Loss Argument

**Step 1: Thermal radiation carries no information.** The Hawking radiation has a thermal spectrum, $\rho_{\text{out}} \propto e^{-H/T}$, which depends only on the temperature (and hence only on $M$, $J$, $Q$). Two black holes formed from completely different initial configurations (e.g., a collapse of iron vs. a collapse of hydrogen) of the same mass will produce identical radiation. The "which state" information is lost.

**Step 2: The information is inside the black hole.** During evaporation, the interior of the black hole still contains a record of the initial state. But the interior is causally disconnected from the exterior by the event horizon.

**Step 3: The black hole disappears.** If the evaporation is complete, the interior (and the singularity) disappear. There is no remnant to store the information. The information is simply *gone*.

**Step 4: The final state is mixed.** The evolution from $\Sigma_1$ to $\Sigma_2$ maps:

$$|i\rangle\langle i| \to \rho_f = \text{Tr}_{\text{interior}} |0_{\text{out}}\rangle\langle 0_{\text{out}}|$$

The trace over the interior (which no longer exists) produces a mixed state. The von Neumann entropy has increased:

$$S(\rho_f) > S(|i\rangle\langle i|) = 0$$

### The Superscattering Operator $\$$

Since the evolution is not unitary ($|i\rangle \to |f\rangle$ with $S^\dagger S \neq I$), Hawking proposes replacing the S-matrix with a "superscattering operator" $\$$:

$$\rho_f^{AB} = \$^{AB}{}_{CD} \, \rho_i^{CD}$$

where $\rho_i$ is the initial density matrix and $\rho_f$ is the final density matrix. The $\$$ operator is:

- **Linear**: $\$(\lambda_1 \rho_1 + \lambda_2 \rho_2) = \lambda_1 \$(\rho_1) + \lambda_2 \$(\rho_2)$
- **Completely positive**: preserves positivity of density matrices
- **Trace-preserving**: $\text{Tr}(\rho_f) = \text{Tr}(\rho_i) = 1$

But it is NOT of the form $\$(\rho) = S \rho S^\dagger$ for any operator $S$. The $\$$ operator is sometimes written as $\$: \mathcal{H}_{\text{in}} \otimes \mathcal{H}_{\text{in}}^* \to \mathcal{H}_{\text{out}} \otimes \mathcal{H}_{\text{out}}^*$ (mapping the initial Hilbert space tensor its dual to the final Hilbert space tensor its dual).

In the factored form, a unitary S-matrix gives:
$$\$^{AB}{}_{CD} = S^A{}_C \, (S^*)^B{}_D$$

Hawking's claim is that in the presence of black holes, $\$$ does not factorize in this way.

### Energy Conservation and CPT

Hawking addresses the objection that information loss would violate energy conservation or CPT symmetry:

**Energy conservation**: $\$$ is still energy-conserving in the sense that $\text{Tr}(H \, \rho_f) = \text{Tr}(H \, \rho_i)$ (the expectation value of energy is preserved). What is lost is the *correlations* in the state, not the total energy.

**CPT**: The process is not CPT-invariant -- the time-reverse of an evaporating black hole is not another evaporating black hole (it would require a white hole, which is excluded by the second law). Hawking argues that CPT is violated in quantum gravity, but only in exponentially small amounts for processes not involving black holes.

### Banks, Susskind, and Peskin Objections (1984)

Banks, Susskind, and Peskin later argued that any $\$$ operator that is not unitary leads to violations of either energy conservation or locality (or both) -- a "non-unitary catastrophe" where even virtual black holes would cause energy non-conservation at observable levels. This argument was a major reason why most string theorists rejected information loss. The counterargument (by Hawking and by Unruh and Wald) was that the BSP argument assumes a factorization that may not hold in quantum gravity.

---

## Physical Interpretation

### What Is Lost?

The information that is lost is not energy, charge, or angular momentum -- these are conserved and appear in the Hawking radiation through global conservation laws. What is lost is the *detailed quantum state* -- the phases, the correlations, the entanglement structure. Two different pure states of the same energy, charge, and angular momentum produce the same mixed thermal state. The many-to-one map is the essence of non-unitarity.

### The Analogy with Burning a Book

Hawking's information loss is fundamentally different from the apparent information loss in burning a book. When a book burns, the information is scrambled into the smoke and ash, but it is in principle recoverable (the process is unitary, just chaotic). Hawking claims that black hole evaporation is genuinely irreversible -- the information is not scrambled, it is *destroyed*.

### Quantum Gravity as the Culprit

Hawking identifies the singularity as the seat of information destruction. The classical singularity theorems guarantee that curvature diverges inside the black hole. Whatever quantum gravity does to resolve the singularity, Hawking argues, it does not restore unitarity. This is a claim about quantum gravity, not just about semiclassical physics.

---

## Impact and Legacy

### The Information Paradox Industry

This paper launched what is arguably the most productive problem in theoretical physics. Major responses include:

1. **Information is preserved (unitarity wins)**: The position of most string theorists. Information is encoded in subtle correlations in the Hawking radiation. Mechanisms include:
   - Black hole complementarity (Susskind, Thorlacius, Uglum, 1993)
   - AdS/CFT (Maldacena, 1997): the boundary CFT is manifestly unitary
   - Fuzzball program (Mathur, 2005): the horizon is replaced by a stringy microstate
   - Island formula (2019): semiclassical gravity itself, when properly interpreted, gives a unitary Page curve

2. **Information is lost (Hawking wins)**: A minority position, but one with serious proponents (Unruh, Wald). Requires modifying quantum mechanics.

3. **Remnants**: The evaporation stops at the Planck mass, leaving a stable or long-lived remnant containing the information. Problems: the remnant must have an enormous number of internal states (the entropy of the original black hole), leading to infinite pair-production rates (the "remnant problem").

4. **Baby universes**: The information escapes into a disconnected baby universe. This is Hawking's later position (1988). Problems: it is empirically indistinguishable from information loss for observers in our universe.

### The Bet with Preskill

Hawking famously bet John Preskill (and Kip Thorne, who sided with Hawking) that information is lost. Hawking conceded the bet in 2004 (see the analysis of the 2005 paper). Thorne never conceded.

### The AMPS Firewall Argument (2012)

Almheiri, Marolf, Polchinski, and Sully (AMPS) sharpened the paradox by showing that three reasonable assumptions -- (1) unitarity, (2) effective field theory outside the horizon, (3) no drama at the horizon for infalling observers -- are mutually inconsistent. One of them must be wrong. This "firewall paradox" reignited the information loss debate.

### The Island Formula Resolution (2019)

Penington (2019) and Almheiri, Engelhardt, Marolf, and Maxfield (2019) showed that the gravitational path integral, computed using the replica trick, includes saddle points ("islands") inside the black hole. These islands contribute to the entanglement entropy of the radiation, causing it to follow the Page curve. In this picture, information is preserved without violating any of the AMPS assumptions (when properly formulated) -- the resolution involves a subtle modification of assumption (2).

---

## Connections to Modern Physics

1. **AdS/CFT and unitarity**: In AdS/CFT, the bulk black hole is dual to a thermal state in the boundary CFT. Since the CFT is unitary, the bulk evolution must also be unitary. This is the strongest argument against information loss, but it applies only in AdS -- its extension to asymptotically flat spacetimes (our universe) is an open question.

2. **Quantum error correction**: The AdS/CFT correspondence can be understood as a quantum error-correcting code (Almheiri, Dong, Harlow, 2015). Bulk information is encoded redundantly in the boundary CFT. This provides a concrete mechanism for how information survives in the radiation.

3. **Complexity and scrambling**: Black holes are the fastest scramblers in nature (Sekino and Susskind, 2008). The scrambling time $t_s \sim M \ln M$ (in Planck units) is the time after which information is thoroughly mixed into the Hawking radiation. This connects to quantum information theory and computational complexity.

4. **Entropy budgets in cosmology**: The information paradox has a cosmological cousin: if the universe has a cosmological event horizon (as in de Sitter space), does information pass through it and get lost? The Gibbons--Hawking temperature of the de Sitter horizon may imply an analogous problem.

5. **For the exflation framework**: In a Kaluza--Klein framework, the internal dimensions provide additional degrees of freedom that participate in the Hawking process. Information that appears lost in the 4D projection may be stored in the internal space. This is structurally similar to the "island" resolution, where information is stored in a region that is not naively accessible. The exflation mechanism (evolution of internal geometry) could provide a natural "island" structure.
