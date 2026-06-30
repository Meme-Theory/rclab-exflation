# Simulating Physics with Computers

**Author(s):** Richard P. Feynman (Department of Physics, California Institute of Technology)
**Year:** 1982
**Journal:** International Journal of Theoretical Physics, Vol. 21, Nos. 6/7, pp. 467–488
**arXiv/DOI:** DOI: 10.1007/BF02650179 (keynote talk, MIT, May 1981)
**Relevance:** MEDIUM for phonon-exflation

---

## Abstract
No formal abstract is printed. The paper is Feynman's keynote at the First Conference on the Physics of Computation (MIT, 1981). He asks whether physics can be exactly simulated by a universal computer with local interactions and computer resources scaling only with the space-time volume of the system simulated. He concludes: classical physics can be so simulated in principle; probabilistic classical physics can be imitated by a probabilistic classical computer; quantum physics cannot be imitated by any local classical probabilistic computer (because the simulating "probabilities" must go negative); a genuinely quantum computer built from 2-state elements can, however, serve as a universal simulator of quantum physics. The paper introduces the idea of the quantum computer.

## Key Arguments and Derivations

**§1 Introduction (pp. 467–468).** Feynman states the ground rules for what counts as a "simulation": (i) by a universal computer with locally interconnected elements; (ii) with the number of computer elements scaling linearly (polynomially) in the space-time volume of the physical system; (iii) exactly, not approximately. Continuous space + infinite sums are not allowed; thus "if this proposition is right, physical law is wrong." Discretizing space to a simple lattice would produce anisotropies in the speed of light, bounded experimentally (lithium atom test).

**§2 Simulating time (pp. 469–470).** Time is taken discrete (conservatively < 10^{-27} s). Two notions: (a) cellular-automaton-style imitation in which the state at t+1 depends on the state at t in a neighborhood; (b) a space-time view in which the state s_i at spacetime point i satisfies s_i = F_i(s_j, s_k, ...) with j,k in a 4D neighborhood. If F depends on future as well as past (positrons = electrons backwards in time), can an organized algorithm still solve it? Open question; classical physics is causal and adaptable.

**§3 Simulating probability (pp. 471–474).** A diffusing particle satisfies ∂P/∂t = −∇²P. Discretizing, one needs k digits per configuration. For R particles at N lattice points one needs N^R configurations; for local field theory R ~ N so ~ N^N configurations — too many to STORE. Therefore one cannot simulate by calculating the probability; one must IMITATE by running a probabilistic computer many times and reading off the output frequency. A local probabilistic cellular-automaton update is

  P_{t+1}({s}) = Σ_{s'} [Π_i m(s_i | s'_j, s'_k, ...)] P_t({s'})     (Eq. 3.*, p. 473)

where m(s_i | neighbors) is a transition probability depending only on a local neighborhood. Such a local probabilistic automaton correctly imitates probabilistic classical nature.

**§4 Quantum computers — universal quantum simulators (pp. 474–476).** A quantum computer built from 2-state sites (occupied/unoccupied, spin-1/2) with canonical operators

  a = (σ_x − iσ_y)/2,  a* = (σ_x + iσ_y)/2,  n = a*a = (1 + σ_z)/2

and local Hermitian couplings can imitate any Bose field theory on a discrete lattice. Feynman states "I know, almost certainly, that we could do that for any quantum mechanical system which involves Bose particles. I'm not sure whether Fermi particles could be described by such a system." — leaving Fermi simulation open (later solved by Jordan–Wigner etc.).

**§5 Probabilistic simulation of quantum by classical (pp. 476–478).** Cannot imitate ψ directly (too many variables). Try instead the density matrix ρ(x,x') = ψ*(x)ψ(x') or the Wigner function W(x,p) = ∫ ρ(x+y/2, x−y/2) exp(ipy) dy, which has the marginals ∫W dp = |ψ|² (probability at x) and ∫W dx = probability at p. For spin-1/2 one represents the system by four "probabilities" f_{++}, f_{+−}, f_{−+}, f_{−−} (sum = 1). Real physical probabilities (spin-z-up, spin-x-up, spin-y-up, etc.) come out as linear combinations of the f's and are always ≥ 0.

**§6 Negative probabilities (pp. 479–480).** The transition equation for the spin-model "probability" F({s_1,...,s_N}) has the same form as the classical probabilistic update

  F_{t+1}({s}) = Σ_{s'} [Π_i M(s_i | s'_j, s'_k, ...)] F_t({s'})     (Eq. 6.*, p. 480)

BUT now M (and F itself) need not be non-negative. Example: f_{++}=0.6, f_{+−}=−0.1, f_{−+}=0.3, f_{−−}=0.2. All physically measurable probabilities (sums of two f's) are positive, but individual f's are not. No classical probabilistic computer can sample from a distribution that takes negative values.

**§7–§8 Photon polarization and two-photon EPR (pp. 481–484).** For a single calcite, the probabilities cos²φ and sin²φ are classical. For the two-photon correlation experiment (the Aspect-type EPR test) quantum theory predicts P_OO = P_EE = (1/2) cos²(φ_2 − φ_1) and P_OE = P_EO = (1/2) sin²(φ_2 − φ_1). At φ_1 = φ_2 one always gets matched outcomes, so any hidden-variable model must deterministically assign O/E at every angle.

**§8 (Bell-type bound, pp. 484–485).** Choose angles that are multiples of 30°. For every hidden-variable dot-pattern on the six angles (3 white + 3 black, complementary at 180°), the probability of a match at relative angle 30° averaged over the 8 distinct patterns is at most 2/3. Quantum theory predicts cos²(30°) = 3/4 > 2/3, and experiment agrees. So quantum mechanics cannot be imitated by any local classical probabilistic computer. This is Feynman's compressed restatement of Bell's inequality.

**§9 Discussion (pp. 486 onward).** Feynman remarks that the many-worlds picture is possible "but I'm not very happy with it," and notes that "nature isn't classical, dammit, and if you want to make a simulation of nature, you'd better make it quantum mechanical."

## Key Results
1. Locality + polynomial scaling of computer elements with space-time volume are the natural rules for "exact simulation."
2. Classical probabilistic physics is imitable by a local probabilistic cellular automaton with update Π m(s_i | neighbors).
3. Quantum physics is NOT imitable by any local classical probabilistic computer — the Wigner-function "probabilities" f take negative values, equivalently the two-photon correlation gives cos²(30°)=3/4 exceeding the classical bound 2/3.
4. A 2-state-per-site quantum machine with local Hermitian couplings is a universal quantum simulator for Bose systems (Fermi case left open).
5. First explicit articulation that quantum computers, as a new model of computation, are required to simulate quantum physics efficiently.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Diffusion | ∂P(x,t)/∂t = − ∇² P(x,t) | p. 471 |
| Classical update | P_{t+1}({s}) = Σ_{s'} [Π_i m(s_i | s'_j, s'_k, ...)] P_t({s'}) | p. 473 |
| Density matrix | ρ(x,x') = ψ*(x) ψ(x') | p. 477 |
| Wigner function | W(x,p) = ∫ ρ(x+y/2, x−y/2) exp(ipy) dy | p. 478 |
| Site algebra | a = (σ_x − iσ_y)/2, a* = (σ_x + iσ_y)/2, n = a*a = (1+σ_z)/2 | p. 475 |
| "Neg-prob" update | F_{t+1}({s}) = Σ_{s'} [Π_i M(s_i | s'_j,s'_k,...)] F_t({s'}) | p. 480 |
| EPR predictions | P_OO = P_EE = (1/2) cos²(φ_2−φ_1); P_OE = P_EO = (1/2) sin²(φ_2−φ_1) | p. 482 |
| Bell-type bound | P_match(30°) ≤ 2/3 (classical local HV) vs. cos²(30°) = 3/4 (QM) | pp. 484–485 |

## Relevance to Phonon-Exflation
This paper is the foundational argument that quantum systems cannot be efficiently classically simulated — directly relevant to the GPE simulation, which is the classical saddle of a path integral and drops negative-probability Wigner structure. Three concrete implications: (i) the substrate's intrinsic evolution is a "universal quantum simulator" in Feynman's §4 sense, so any emergent physics it produces is by construction quantum-consistent without extra machinery; (ii) the GPE simulation captures only the classical mean field, missing precisely the negative-"probability" sector (§6) responsible for EPR-type correlations — these must come back in through the spectral-action moments and the Leggett/GGE channels, not through c-number fields; (iii) the 2-state operator algebra (Eq. site algebra) is isomorphic to the spin-1/2 building blocks of the Dirac operator D_K on Jensen-deformed SU(3), validating the fabric-as-substrate-simulator picture at the level of local operator content.
