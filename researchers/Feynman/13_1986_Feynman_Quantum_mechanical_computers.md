# Quantum Mechanical Computers

**Author(s):** Richard P. Feynman
**Year:** 1986 (based on a plenary talk at the CLEO/IQEC Meeting in 1984)
**Journal:** Optics News, February 1986, pp. 11–20
**arXiv/DOI:** Optics News, Feb. 1986 (OSA)
**Relevance:** MEDIUM for phonon-exflation

---

## Abstract
No formal abstract is printed. The paper analyzes the physical limitations of computers due to the laws of physics, specifically those due to quantum mechanics and the uncertainty principle. Feynman argues that, aside from the obvious limitation to size if the working parts are made of atoms, there is no fundamental limit from quantum mechanics on computation, and he exhibits an explicit Hamiltonian for a quantum system that serves as a universal reversible computer.

## Key Arguments and Derivations

**Introduction (pp. 11–12).** Building on Bennett's analysis of the thermodynamics of computation, Feynman asks whether quantum mechanics imposes fundamental limits on computation. Actual transistor systems dissipate ~10^10 kT per step; Nature's DNA copying ~100 kT per bit; the Landauer/von Neumann limit kT ln(2) was thought to be absolute, but Bennett showed that with reversible primitives the minimum free energy is independent of the number of logical steps and is at most ~kT per bit of output.

**Reversible logic primitives (pp. 12–13).** Three reversible primitives suffice for a universal reversible computer (following Toffoli): (i) NOT (denoted as an X on a wire), (ii) CONTROLLED NOT (a controls, b' = b XOR a, a' = a, which also yields FAN OUT when b=0), (iii) CONTROLLED CONTROLLED NOT (Toffoli gate: a,b control, c' = c XOR (a AND b); yields AND when c=0). CONTROLLED NOTs compose to give EXCHANGE. Circuits produce "garbage" bits, but via Bennett's copy-and-uncompute trick (Fig. 6) garbage can always be reduced to a copy of the input. With k output bits and starting with k zeros, one obtains just (input, output) with all workspace returned to 0.

**Quantum mechanical computer – the construction (pp. 13–15).** Each bit is represented by a two-state "atom" with basis |0>, |1>. Gates are realized as unitary matrices built from creation/annihilation operators a, a* satisfying aa* + a*a = 1 (single-site canonical anticommutators in the two-level truncation). Key matrix forms:
- NOT: A_a = a + a*
- CONTROLLED NOT: A_{a,b} = a*a (b+b*) + aa*  (equivalently 1 + a*a (b + b* − 1))
- Toffoli (CC-NOT): A_{ab,c} = 1 + a*a · b*b · (c + c* − 1)

For a sequence of k gates A_1, ..., A_k acting on n register atoms, the desired M = A_k ... A_2 A_1 is implemented by adjoining k+1 "program counter sites" with operators q_i, q_i*, and writing the Hamiltonian

  H = Σ_{i=0}^{k-1} q_{i+1}* q_i A_{i+1} + h.c.     (Eq. H1, p. 15)

Starting with a single "cursor" occupation at site 0 and the register in ψ_in, under e^{-iHt} the cursor propagates along the program line; whenever the cursor is detected at site k, the register has been acted on by M. Cursor motion forward/backward under h.c. terms exactly preserves unitarity because A_j* A_j = 1: any backward hop multiplies by A_j and then by A_j* when re-traversed, leaving no net operator. The cursor propagation is mathematically identical to tight-binding electron / spin-wave propagation on a 1D chain.

**Imperfections and free energy loss (pp. 16–17).** With scattering probability p per step (inverse of the mean free path 1/p in lattice units), one needs an external drift. The free energy loss per logical step is

  ΔF/step ≈ kT · p · (t_min / t_actual)     (Eq. FE, p. 16)

where t_min is the ballistic time and t_actual is the time allowed. For p → 0 or t_actual → ∞, ΔF → 0. There is NO uncertainty-principle penalty depending on the number of computational steps: time-of-arrival uncertainty is a property of the I/O, not the internal dynamics. With couplings ~0.1 eV, the per-step ballistic time is ~6×10^{-15} s, about 4 orders of magnitude faster than then-contemporary transistors.

**Simplifying the implementation (pp. 17–19).** A "SWITCH" primitive using 3-body interactions suffices:

  H_switch = q* c p + r* c* p + c.c.     (Eq. Sw, p. 17)

together with NOT. The switch routes cursor from p to q if c=1, else from p to r, flipping c. All logical operations (CONTROLLED NOT, sequence, conditional, sub-routine reuse with flag registers, garbage clearing via the backward pass) are built from NOT+SWITCH. Figs. 8–16 give the explicit circuits, including an incremental 3-bit binary counter.

**Conclusions (p. 20).** The machine imitates conventional sequential digital computation; quantum parallelism is NOT exploited. Irreversible memory and classical wires/optics may be mixed in for efficiency. Bottom line: "the laws of physics present no barrier to reducing the size of computers until bits are the size of atoms, and quantum behavior holds dominant sway."

## Key Results
1. A fully-specified Hamiltonian (Eq. H1) realizes any prescribed sequence M = A_k ... A_1 of local unitary gates on an n-atom register using a (k+1)-site program line of cursor hops.
2. Reversible computation is universal: NOT + Toffoli (or NOT + SWITCH) suffices.
3. Free energy dissipation per step is bounded by kT·p·(t_min/t_actual); p=0 or infinite time → zero dissipation. The uncertainty principle imposes no per-step energy cost.
4. Program-line dynamics reduces to 1D tight-binding / spin-wave propagation, so ballistic operation is possible with a spatially extended initial wave-packet.
5. Sub-routine reuse requires a binary flag register to preserve reversibility.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| CCR | a a* + a* a = 1 | p. 14 |
| NOT | A_a = a + a* | p. 14 |
| C-NOT | A_{a,b} = 1 + a*a (b + b* − 1) | p. 14 |
| Toffoli | A_{ab,c} = 1 + a*a · b*b · (c + c* − 1) | p. 14 |
| Program Hamiltonian | H = Σ q_{i+1}* q_i A_{i+1} + h.c. | p. 15 |
| Switch term | H_sw = q* c p + r* c* p + c.c. | p. 17 |
| Free-energy/step | ΔF = kT · p · (t_min / t_actual) | p. 16 |
| Ballistic step time | ~6×10^{-15} s for 0.1 eV couplings | p. 16 |

## Relevance to Phonon-Exflation
Feynman's program-counter-cursor Hamiltonian (Eq. H1) is a prototype for the substrate's own computational capacity: a 1D chain of program sites coupled by local hopping operators q_{i+1}* q_i A_{i+1} is structurally identical to the tight-binding Hamiltonians that appear in the fabric's relay dynamics. Two framework-relevant lessons: (i) the unitarity of each A_j (gauge-invariant update) is what makes the backward hops harmless – a direct analog of the substrate's reversibility requirement at the spectral-action level; (ii) since the substrate IS the quantum system, its intrinsic evolution IS "quantum simulation" in Feynman's sense, no classical overhead is paid per degree of freedom. Practical point for the GPE code path: the GPE simulates only a single classical saddle; extracting quantum corrections at late-transit requires something like Feynman's cursor construction to track coherent histories of the relay patterns.
