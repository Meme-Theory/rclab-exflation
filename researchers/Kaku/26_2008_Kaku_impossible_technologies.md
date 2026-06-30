# Physics of the Impossible: Traversable Wormholes, Warp Drives, and Teleportation

**Author(s):** Michio Kaku
**Year:** 2008
**Source:** "Physics of the Impossible: A Scientific Exploration Into the World of Phasers, Force Fields, Teleportation, and Time Travel" (2008)

---

## Abstract

Kaku's systematic exploration of technologies that appear "impossible" according to intuition but are not forbidden by fundamental physics. The key question is not "Is this possible?" but rather "What would it require?" For traversable wormholes, Kaku explains the Einstein-Rosen bridge and the exotic matter (negative energy density) required to keep it open. For warp drives, he covers the Alcubierre solution to general relativity—which permits FTL travel without violating relativity—and the enormous energy requirements. For teleportation, he distinguishes between theoretical quantum teleportation (which requires copying qubits, violating no-cloning theorem, yet achievable in certain contexts) and macroscopic teleportation of classical objects (exponentially harder). The treatment is grounded in known physics but frank about open problems: no one has produced negative energy density, no one has constructed a warp drive, and teleporting macroscopic objects remains speculative. Yet Kaku argues these are not violations of fundamental law—merely engineering challenges of staggering proportions.

---

## Historical Context

General relativity permits solutions (wormholes, warp drives) that seem to enable FTL travel, but these were long dismissed as physically unrealistic. In the 1980s-90s, researchers (Morris, Thorne, Alcubierre, others) began treating these solutions seriously, asking not whether they could be dismissed philosophically but what physical conditions would be required. The results were sobering but tantalizing: wormholes require exotic matter with negative energy density (unknown state of matter, possibly related to quantum fields); warp drives require even more exotic conditions (negative energy density, enormous quantities). Kaku's popularization of these results elevated them from curiosities to serious physics, framing the question as a technological and resource problem rather than a fundamental violation.

---

## Key Arguments and Derivations

### 1. Traversable Wormholes and Exotic Matter

An **Einstein-Rosen bridge** is a solution to the Einstein equations connecting two asymptotically flat spacetimes:

$$ds^2 = -dt^2 + dl^2 + (b_0^2 + l^2) d\Omega^2$$

where $l$ ranges from $-\infty$ to $+\infty$, and $b_0$ is the throat radius. A particle traveling from $l = -\infty$ to $l = +\infty$ traverses the bridge in finite proper time.

However, the classical ER bridge is a one-way trap: it collapses too quickly for anything to traverse it. To keep it open requires **exotic matter** with negative energy density:

$$\rho_{\text{eff}} = \frac{1}{8\pi G} \langle T_{\mu\nu} u^\mu u^\nu \rangle < 0$$

where $u^\mu$ is a observer's worldline tangent. Normal matter has $\rho > 0$ (positive energy density). Exotic matter violates the weak energy condition (WEC):

$$\rho_{\text{eff}} + p \geq 0 \quad \text{(WEC, often true)}$$

and potentially the null energy condition (NEC):

$$\rho_{\text{eff}} + p_i \geq 0 \quad \text{(NEC, often true)}$$

By contrast, exotic matter satisfies $\rho_{\text{eff}} + p < 0$ (violates NEC).

**Morris-Thorne wormhole**: A stable, traversable wormhole requires:

1. Exotic matter with $\rho < 0$ distributed in the throat.
2. Exact form of $\rho(l)$ to prevent causality violations and ensure stability.
3. Total exotic mass-energy: $m_{\text{exotic}} \sim m_{\text{Planck}} \times (a / 10 \text{ km})$ (for a macroscopic wormhole of size $a$).

For a wormhole of Earth-size ($a \sim 10^7$ m), the required exotic mass is approximately the mass of the observable universe! This is the key problem: exotic matter is either non-existent or requires total energy budgets beyond any conceivable technology.

### 2. Sources of Exotic Matter in Quantum Field Theory

**Casimir effect**: The quantum vacuum between two parallel conducting plates has a negative energy density:

$$\rho_{\text{Casimir}} = -\frac{\pi^2 \hbar c}{720 d^4}$$

where $d$ is the plate separation. This is positive, but the *pressure* (related to the energy density in the direction perpendicular to plates) is negative, producing an attractive force. However:

$$\int \rho_{\text{Casimir}} dV \sim -10^{-9} \text{ J}$$

(for laboratory-scale gaps). Scaling this up to astronomical distances is wildly infeasible.

**Phantom energy**: If dark energy has an equation of state $w = p / \rho < -1$ (phantom dark energy), it violates the NEC and could theoretically be harvested. But:

1. Current observations give $w \approx -0.9 \to -1.1$ (consistent with cosmological constant, $w = -1$).
2. Phantom energy density is tiny: $\rho_{\text{DE}} \sim 10^{-26}$ kg/m^3.
3. No mechanism to concentrate or harvest it.

**Hawking radiation**: Near the event horizon of a black hole, quantum effects create negative energy density (in some reference frames). But extracting it is impractical.

Conclusion: Kaku acknowledges that exotic matter remains hypothetical. Its existence is not ruled out by known physics, but no source has been identified.

### 3. The Alcubierre Warp Drive

Alcubierre (1994) found a solution to Einstein's equations permitting FTL travel **without violating relativity**:

$$ds^2 = -c^2(1 - f(r_s) v^2) dt^2 + 2v f(r_s) dx dt + (1 + f(r_s)^2 v^2) dx^2 + dy^2 + dz^2$$

where $r_s = \sqrt{(x - x_0(t))^2 + y^2 + z^2}$ is distance from the "bubble" center, $f(r_s)$ is a profile function (smooth, $f = 1$ inside, $f = 0$ outside), and $v$ is the "speed" of the bubble.

**Key feature**: The spacetime inside the bubble is flat (Minkowski), and the worldline $x_0(t) = vt$ is timelike—the bubble travels slower than light locally. However, space itself is contracting in front of the bubble and expanding behind it, allowing the bubble to move arbitrarily fast without the interior reaching light speed.

**Stress-energy requirement**:

$$T_{\mu\nu} = \frac{1}{8\pi G} (G_{\mu\nu} + \Lambda g_{\mu\nu})$$

Calculating $G_{\mu\nu}$ for the Alcubierre metric yields:

$$T_{\text{null}} \propto \frac{d^2 f}{dr_s^2}$$

which is negative. The entire spacecraft is surrounded by a shell of negative energy density:

$$\int T_{\text{null}} dV = -m_{\text{Planck}} \times (R / r_0)^3 \times v^2 / c^2$$

where $R$ is the bubble radius and $r_0$ is the width of the wall. For $R \sim 100$ m, $r_0 \sim 1$ nm, $v = 10c$:

$$\text{Exotic mass} \sim 10^{62} \text{ kg}$$

(more than $10^{30}$ times the observable universe's mass). This is Kaku's main point: warp drives are not forbidden by relativity, but the energy budget is prohibitive.

### 4. Classical Teleportation and the No-Cloning Theorem

In quantum mechanics, the **no-cloning theorem** (Wootters, Zurek) states that an unknown quantum state cannot be perfectly copied:

$$|\psi\rangle_A \to |\psi\rangle_A \otimes |\psi\rangle_B$$

is impossible for arbitrary $|\psi\rangle$ without additional information.

However, **quantum teleportation** (Bennett et al., 1993) allows transferring the quantum state from location A to location B, provided:

1. The two locations share an entangled pair (a Bell pair, $|\Phi^+\rangle = (|00\rangle + |11\rangle)/\sqrt{2}$).
2. Two classical bits of information are communicated from A to B.

The protocol:

- Alice (at A) performs a Bell measurement on her qubit and the half of the entangled pair she holds.
- The measurement result (2 classical bits) is sent to Bob (at B).
- Bob applies a unitary correction based on those 2 bits.
- The result: Bob's qubit now holds the original state $|\psi\rangle$.

**Crucially**: The original qubit is destroyed at location A (no cloning), and the state transfer requires classical communication (no FTL). Teleportation has been experimentally demonstrated with photons, atoms, and ions.

### 5. Macroscopic Teleportation and Decoherence

Teleporting a macroscopic object (a person, a spacecraft) requires:

1. Measuring all $N \sim 10^{28}$ atoms and their quantum states (position, momentum, spin).
2. Storing this information (a classical bit per atom: $2^{10^{28}}$ possible states).
3. Transmitting this information at light speed to the destination.
4. Reconstructing the object using entangled pairs distributed globally.

**Problems**:

- **Information storage**: $10^{28}$ bits of information is incomprehensibly large (universe's computational capacity $\sim 10^{120}$ bits; recording one person $\sim 10^{47}$ bits at full atomic precision).

- **Decoherence**: Atoms in a body are entangled with their environment. Measuring an atom to perfect precision requires destroying the entanglement—you cannot teleport a living, conscious person because consciousness depends on the entanglement structure.

- **Reconstruction**: Building the object atom-by-atom (assembling from blueprint) requires atomic-precision manipulators, currently far beyond capability.

- **Interpretation question**: Even if technically possible, is the reconstructed person the same individual? Does identity persist through teleportation?

Kaku frankly concludes: macroscopic teleportation remains speculative and may violate additional constraints (entropy, thermodynamics) not captured by quantum mechanics alone.

### 6. Time Travel and Closed Timelike Curves

General relativity permits **closed timelike curves** (CTCs)—spacetime trajectories that loop back in time—in certain solutions (Kerr black holes, Tipler cylinders, Alcubierre warp drives).

However, every CTC solution faces severe constraints:

**Grandfather paradox**: If I travel back in time and kill my grandfather, how do I exist to travel back? Logically paradoxical. Resolutions:

1. **Novikov self-consistency**: Events must be self-consistent (I cannot kill my grandfather; nature arranges for me to fail).

2. **Many-worlds**: Traveling to the past creates a parallel branch (no paradox, but I cannot change my timeline).

3. **Quantum decoherence**: Quantum mechanics may forbid CTCs via coherence loss (Hawking's chronology protection conjecture).

**Causality violation**: CTCs can be used to send signals to the past, enabling faster-than-light communication and causality violation in other reference frames.

**Energy conditions**: Constructing a CTC (Kerr black hole, warp drive) requires exotic matter or exotic spacetime geometry, encountering the same energy budget problems as wormholes.

Kaku argues that time travel to the past is not forbidden by known physics but faces such severe constraints (energy, causality, quantum issues) that it likely remains impossible.

### 7. Engineering Challenges and Technology Timescale

Kaku's overall assessment:

- **Traversable wormholes**: Type II-III technology (if ever possible).
- **Warp drives**: Type III technology (if possible).
- **Macroscopic teleportation**: Requires new physics; not Type II/III scaling.
- **Time travel**: Forbidden by quantum mechanics or causality, not merely engineering.

For Type I civilization, the bottleneck is energy (terawatts suffice for weather, earthquakes, not for exotic spacetimes).

For Type II civilization, energy budgets become plausible (~stellar power), but you hit quantum and thermodynamic limits.

For Type III civilization, energy is sufficient, but the underlying physics (negative energy density, causality) may pose hard limits.

---

## Key Results

1. **Wormholes require exotic matter**: Negative energy density must be concentrated in the throat, with total energy budgets exceeding plausible extraction.

2. **Alcubierre warp drives obey relativity**: FTL travel is permitted if spacetime is engineered, but energy requirements are astronomical (Type III scale).

3. **Quantum teleportation is proven**: State transfer is possible and has been experimentally demonstrated; no macroscopic objects yet.

4. **Macroscopic teleportation is speculative**: Requires atomic precision measurement, information transmission, and reconstruction; decoherence and identity issues remain.

5. **Time travel faces fundamental barriers**: CTCs are solutions to Einstein's equations but trigger paradoxes and causality violations, possibly forbidden by quantum mechanics.

6. **Energy budgets are prohibitive**: Even for Type III civilizations, exotic matter and warp drives require energy density exceeding theoretical limits.

---

## Impact and Legacy

Kaku's treatment shifted "impossible" technologies from metaphysical dismissal to physical analysis. By grounding these speculations in Einstein's equations and quantum mechanics, he showed that many proposed technologies are *not* violations of fundamental law—merely requiring resources and engineering beyond human capability. This framework is now standard in astrobiology, science fiction, and speculative physics.

---

## Connection to Phonon-Exflation Framework

**Relevance: LOW**

Phonon-exflation does not address exotic matter, warp drives, or time travel. However, there are methodological parallels:

1. **Feasibility from first principles**: Like Kaku's approach (analyzing wormholes from Einstein's equations), phonon-exflation derives observables from fundamental principles (Connes spectral action), not from phenomenological models.

2. **Energy scales**: Understanding the fundamental energy scales (Planck mass, compactification scales) informs what exotic matter or warp drive constructions would be possible. Phonon-exflation's predictions for particle masses and dark matter affect this calculation.

3. **Causality preservation**: Phonon-exflation respects causality by design (path integral over forward-time configurations, no CTCs). Unlike Alcubierre drives, the framework does not explore exotic spacetime structures that violate causality.

4. **No action-at-a-distance**: The framework is local and relativistic—no instantaneous teleportation or FTL signaling emerges.

---

## References for Further Study

- Kaku, M. "Physics of the Impossible: A Scientific Exploration Into the World of Phasers, Force Fields, Teleportation, and Time Travel" (2008).
- Thorne, K.S. "Black Holes and Time Warps: Einstein's Outrageous Legacy" (1994). [Wormholes and time travel]
- Alcubierre, M. "The Warp Drive: Hyper-Fast Travel Within General Relativity." Class. Quant. Grav. 11.5 (1994): L73. [Warp drive solution]
- Bennett, C.H., et al. "Teleporting an Unknown Quantum State via Dual Classical and Einstein-Podolsky-Rosen Channels." Phys. Rev. Lett. 70.13 (1993): 1895. [Quantum teleportation]
- Morris, M.S., Thorne, K.S. "Wormholes in Spacetime and Their Use for Interstellar Travel: A Tool for Teaching General Relativity." Am. J. Phys. 56.5 (1988): 395-412. [Traversable wormholes]

---

**Lines: 332** | **Status: COMPLETE**
