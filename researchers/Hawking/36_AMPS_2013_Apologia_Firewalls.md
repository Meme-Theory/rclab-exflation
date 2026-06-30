# An Apologia for Firewalls

**Author(s):** Ahmed Almheiri, Donald Marolf, Joseph Polchinski, Douglas Stanford, and James Sully
**Year:** 2013
**Journal:** JHEP (preprint: arXiv:1304.6483)
**arXiv:** 1304.6483
**Relevance:** MEDIUM

---

## Abstract

We address claimed alternatives to the black hole firewall. We show that embedding the interior Hilbert space of an old black hole into the Hilbert space of the early radiation is inconsistent, as is embedding the semi-classical interior of an AdS black hole into any dual CFT Hilbert space. We develop the use of large AdS black holes as a system to sharpen the firewall argument. We also reiterate arguments that unitary non-local theories can avoid firewalls only if the non-localities are suitably dramatic.

---

## Key Arguments and Derivations

### The AMPS Argument (Sec. 1, recapitulated)

Three postulates of Black Hole Complementarity (BHC):

1. **No Drama:** Infalling observers find no dramatic effects at the horizon (only exponentially small number of high-energy particles)
2. **Purity:** Hawking radiation is essentially pure (unitary evolution)
3. **EFT:** Effective field theory is valid outside the stretched horizon for macroscopic black holes

A fourth postulate: $S_{\text{BH}}$ governs the density of states.

**The conflict:** After the Page time, purity requires late Hawking mode $b$ to be entangled with early radiation $E$. But No Drama requires $b$ to be entangled with its interior partner $\tilde{b}$ (vacuum entanglement across the horizon). Quantum mechanics forbids both entanglements simultaneously (monogamy of entanglement). One postulate must fail.

**The firewall resolution:** Give up No Drama. The horizon is replaced by a "firewall" -- a surface of high-energy particles/quanta at or near the horizon of sufficiently old black holes.

### Problems with $\tilde{B} \subset E$ (Sec. 2)

The proposal that interior modes $\tilde{B}$ can be embedded in the Hilbert space of early radiation $E$ is examined and shown inconsistent. Key argument: the $\tilde{b}$ operators must commute with all operators acting on $E$ that are accessible to observers far from the black hole, but any embedding of $\tilde{b}$ in $E$ would create non-trivial commutators detectable by such observers.

### Problems with Nonlocal Interactions (Sec. 3)

Unitary nonlocal theories (NVNL: nonviolent nonlocality) are examined. The authors argue that for nonlocality to avoid firewalls, it must be dramatic enough to transfer information across the horizon at rates comparable to the Hawking emission rate. Mining experiments -- where an observer actively extracts Hawking quanta from the stretched horizon -- sharpen this requirement: the nonlocality must affect ALL modes near the horizon, not just the s-wave.

### Evaporating AdS Black Holes (Sec. 4)

Using AdS/CFT as a controlled setting:
- The black hole coupled to a bath (CFT on the boundary absorbs radiation) provides a clean evaporation model
- Purity is guaranteed by the unitarity of the boundary CFT
- Mining experiments are implementable via boundary deformations
- Remnants are excluded because $S_{\text{BH}}$ controls the density of states in the CFT

### Static AdS Black Holes (Sec. 5)

Even eternal (non-evaporating) AdS black holes have a firewall problem. The classic bulk propagation construction for interior operators fails due to trans-Planckian effects for black holes older than the fast scrambling time $t_{\text{scr}} \sim \beta \log S_{\text{BH}}$. Interior operators cannot be embedded in the finite-dimensional Hilbert space $e^{S_{\text{BH}}}$ of the CFT.

### Varieties of Complementarity (Sec. 6)

Several versions of black hole complementarity are examined:
- **Strong complementarity** (original 't Hooft-Susskind): inconsistent with purity after the Page time
- **Observer complementarity:** Each observer has a consistent description, but no single description covers both interior and exterior. AMPS show this is insufficient.
- **$A = R_B$ complementarity** (Maldacena-Susskind ER=EPR type): the interior is built from the radiation Hilbert space. Shown to have consistency issues.

---

## Key Results

1. The three postulates of BHC (No Drama, Purity, EFT) are mutually inconsistent after the Page time
2. Embedding interior modes $\tilde{B}$ in early radiation $E$ is inconsistent
3. Nonlocal theories must be "dramatically" nonlocal to avoid firewalls
4. Mining experiments extend the firewall argument to all modes near the horizon (not just s-wave)
5. Even static AdS black holes have interior description problems after the scrambling time
6. The firewall is the "simplest" resolution: give up No Drama at the horizon of old black holes

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Entanglement conflict | $b$ entangled with $\tilde{b}$ (No Drama) AND $b$ entangled with $E$ (Purity) violates monogamy | Sec. 1 |
| Planck distribution | $\|\beta\|^2 = \frac{1}{e^{\hbar\omega/k_BT_H} - 1}$ | Implicit |
| Page time | $t_{\text{Page}} \sim S_{\text{BH}} \cdot r_S$ | Sec. 1 |
| Scrambling time | $t_{\text{scr}} \sim \beta \log S_{\text{BH}}$ | Sec. 5 |
| BH density of states | $\dim(\mathcal{H}_{\text{BH}}) = e^{S_{\text{BH}}}$ | Postulate 4 |

## Relevance to Phonon-Exflation

The AMPS firewall argument is resolved trivially in the phonon-exflation framework because the framework has no horizon. The tau transit produces particles via a Parker-type (cosmological) mechanism, not a Hawking (horizon) mechanism. All three AMPS postulates -- No Drama, Purity, and EFT -- are simultaneously satisfied when there is no horizon to create the entanglement conflict. The GGE relic produced by the transit is a pure state determined by the initial conditions plus unitary evolution plus integrability, so information is preserved without the need for firewalls, islands, or complementarity. The absence of horizons is a structural feature of the framework, not an assumption imposed to avoid the paradox.
