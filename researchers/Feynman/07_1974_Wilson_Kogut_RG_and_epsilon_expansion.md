# The Renormalization Group and the ε Expansion

**Author(s):** Kenneth G. Wilson (Institute for Advanced Study, Princeton / Laboratory of Nuclear Studies, Cornell) and J. Kogut (Institute for Advanced Study, Princeton)
**Year:** 1974 (received 2 July 1973)
**Journal:** Physics Reports (Section C of Physics Letters) 12, No. 2, pp. 75–200. North-Holland Publishing Company.
**arXiv/DOI:** DOI: 10.1016/0370-1573(74)90023-4
**Relevance:** CRITICAL for phonon-exflation

---

## Abstract
"The modern formulation of the renormalization group is explained for both critical phenomena in classical statistical mechanics and quantum field theory. The expansion in ε = 4 − d is explained [d is the dimension of space (statistical mechanics) or space-time (quantum field theory)]. The emphasis is on principles, not particular applications. Sections 1–8 provide a self-contained introduction at a fairly elementary level to the statistical mechanical theory. No background is required except for some prior experience with diagrams. In particular, a diagrammatic approximation to an exact renormalization group equation is presented in sections 4 and 5; sections 6–8 include the approximate renormalization group recursion formula and the Feynman graph method for calculating exponents. Sections 10–13 go deeper into renormalization group theory (section 9 presents a calculation of anomalous dimensions). The equivalence of quantum field theory and classical statistical mechanics near the critical point is established in section 10; Sections 11–13 concern problems common to both subjects. Specific field theoretic references assume some background in quantum field theory. An exact renormalization group equation is presented in section 11; sections 12 and 13 concern fundamental topological questions."

## Key Arguments and Derivations

**§1 Introduction: RG as coherence-problem method (pp. 78–84).** The RG addresses problems where many degrees of freedom cooperate within a correlation length ξ: critical phenomena, Kondo effect, molecular binding, quantum field theory. Near a critical point ξ is macroscopic, so no local cluster expansion converges; yet hydrodynamics shows that bulk behaviour can be described by averaged "effective" variables. The RG constructs a *sequence of effective local Hamiltonians* ℋ_0 → ℋ_1 → ℋ_2 → ... by iteratively reducing the density of degrees of freedom by a linear factor of 2. Each step is the same transformation τ, so ℋ_{l+1} = τ(ℋ_l). After n iterations the spacing is 2^n L_0 ~ ξ. The key hope is locality: if ℋ_l has range a_l = 2^l L_0, then determining ℋ_{l+1} from ℋ_l requires only regions of size ~ a_{l+1}, not ξ. A fixed point ℋ* satisfies τ(ℋ*) = ℋ* (Eq. 1.2); universality classes correspond to domains of attraction of different fixed points. Historical thread: Landau (1930s hydrodynamic analogy) → Stueckelberg–Petermann [1953] and Gell-Mann–Low [1954] (field-theoretic formulation) → Kadanoff [1966] (block-spin intuition) → Anderson et al. (Kondo). Previously τ acted on a narrow interaction space; modern RG lets ℋ_l contain all possible interactions, provided only a few dominate.

**§1.2–1.3 Current references and Ising model basics (pp. 83–87).** Lists ~100 contemporary works. Ising Hamiltonian ℋ = K Σ_{n,i} s_n s_{n+î} with K = J/kT. Correlation function Γ(x) = <s_0 s_x>; effective range of correlation ξ² = ∫ x² Γ(x) d^d x / ∫ Γ(x) d^d x.

**§2 Critical-temperature scaling (pp. 87–93).** Near T_c, ξ ~ (T − T_c)^{−ν}; Γ(x) at T = T_c falls as 1/|x|^{d−2+η}. Mean-field theory gives ν = 1/2, η = 0 (wrong for d < 4). Kadanoff block-spin argument (reformed as: the 2:1 block is itself a spin with a renormalized coupling); leads to scaling laws relating six exponents (Widom).

**§3 Gaussian model — worked example of RG (pp. 94–101).** The Gaussian smoothing of the Ising δ(s² − 1) constraint gives

  ℋ = − (1/2) ∫_q (q² + r) σ_q σ_{−q}     (Eq. 3.15/3.36)

with cutoff 0 < |q| < 1. The correlation function (Eq. 3.18) is

  Γ(x) = ∫_q exp(i q·x) / (q² + r),   Γ_q = 1/(q² + r)

so ξ² ∝ 1/r and ν = 1/2. RG step (pp. 99–101): integrate out σ_q for 1/2 < |q| < 1 (the fast modes), then rescale q' = 2q and σ_q = ζ σ'_{2q} with ζ = 2^{1 + d/2} so the q² kinetic term retains unit coefficient. The result is

  ℋ' = − (1/2) ∫_{q'} (q'² + r') σ'_{q'} σ'_{−q'},   r' = 4 r     (Eqs. 3.34–3.35)

Thus τ in the Gaussian model is simply r ↦ 4r, a linear map with eigenvalue λ = 4 at the fixed point r* = 0. Then ν = ln 2 / ln λ = 1/2 (Eq. 3.42).

**§4 The s⁴ model and ε expansion (pp. 101–111).** Add a perturbation u s⁴:

  ℋ[σ] = − (1/2) ∫_q (q² + r) σ_q σ_{−q}
           − u ∫_{q_1,q_2,q_3} σ_{q_1} σ_{q_2} σ_{q_3} σ_{−q_1−q_2−q_3}     (Eq. 4.2)

Decompose σ_q = σ_{0,q} + σ_{1,q} into soft (|q|<1/2) and hard (1/2<|q|<1) modes. Integrate the hard modes out of exp(ℋ_F + ℋ_I); generate a perturbative series in u represented diagrammatically (Figs. 4.1–4.3). The hard-mode propagator is Eq. 4.16:

  <σ_{1,q} σ_{1,q'}> = (2π)^d δ^d(q + q') / (q² + r)

The one-loop (tadpole) contribution renormalizes r; the two-loop fish diagram renormalizes u. Rescaling q' = 2q and σ_{0,q} = ζ σ'_{2q}, the crucial dimension count gives the scaling of u itself: in d dimensions the coupling u has scaling dimension (4 − d) ≡ ε, so u is **marginal in d = 4** and relevant for d < 4. Expanding about d = 4 in ε = 4 − d, the nontrivial fixed point (Wilson–Fisher) sits at u* = O(ε), and the linearized RG flow gives the critical exponent

  ν = 1/2 + ε/12 + O(ε²)     (Feynman-graph calculation, §8)

For d = 3 (ε = 1) this extrapolates to ν ≈ 0.583, reproducing the measured 3D Ising exponent to within a few percent.

**§5–§6 Irrelevant variables, approximate recursion formula (pp. 111–120).** All operators O_α with scaling dimension y_α > 0 are *relevant* (grow under RG flow), y_α = 0 *marginal*, y_α < 0 *irrelevant* (decay). Universality is the statement that only relevant + marginal operators control long-distance physics; irrelevant operators vanish from ℋ_l for large l. Polyakov's approximate recursion formula (p. 117) reduces the RG step to a 1D integral which can be iterated numerically; gives critical exponents to ~1% in 3D Ising (§6.2).

**§7–§8 Feynman-graph ε-expansion of exponents (pp. 123–138).** Systematic loop expansion at the Wilson–Fisher fixed point yields ν, η, γ, α, β, δ as power series in ε. Second-order coefficients are computed; Nickel (ref. [47]) extends γ to order ε³.

**§9 Anomalous dimensions of tensor operators (pp. 138–142).** Each composite operator (σ², σ⁴, ∂σ·∂σ, ...) has its own RG eigenvalue; these feed into operator-product expansions and control correction-to-scaling exponents.

**§10 QFT ↔ statistical mechanics equivalence (pp. 143–151).** A classical d-dimensional statistical system at its critical point is equivalent to a Euclidean quantum field theory in d space-time dimensions in its massless (scale-invariant) limit. The correlation length ξ ↔ Compton wavelength 1/m; approach to T_c ↔ approach to continuum limit.

**§11 Exact RG in differential form (pp. 152–158).** Polchinski-type equation (in Wilson's original form): infinitesimal change in the cutoff Λ induces a functional differential equation on ℋ[σ], with RHS built from functional derivatives Γ² (δ²ℋ/δσ δσ) + (δℋ/δσ)². Fixed points ℋ* are stationary solutions of this functional PDE.

**§12 Topology of RG flow: fixed points, domains, universality (pp. 159–175).** Multiple fixed points generically partition the space of Hamiltonians into domains, each with its own universality class. Fixed points can be: stable, unstable in one direction (critical), unstable in two (tricritical), etc. Anomalous dimensions at the fixed point are the eigenvalues of the linearized τ.

**§13 Search for a nontrivial 4D φ⁴ fixed point (pp. 176–185).** At ε = 0 (d = 4) the φ⁴ coupling is marginal; the only known fixed point is the Gaussian one, giving a free (trivial) continuum limit. This is the "triviality problem" of φ⁴ in 4D. The search for a genuine nontrivial fixed point (required for the Higgs sector of the Standard Model as an autonomous QFT) has so far been futile.

**§14 Concluding remarks + Appendix (pp. 186–200).** Simple soluble RG examples; bibliography.

## Key Results
1. The modern RG is a map τ on the space of local Hamiltonians whose fixed points define universality classes; universality follows from domains of attraction of fixed points (Eqs. 1.1–1.2).
2. Critical exponents are eigenvalues of the linearized RG transformation at its fixed point: ν = ln 2 / ln λ (Eq. 3.42).
3. The Gaussian model r' = 4r, λ = 4 gives ν = 1/2.
4. The φ⁴ coupling u has scaling dimension ε = 4 − d: marginal in d = 4, relevant for d < 4. An ε-expansion about d = 4 locates the nontrivial Wilson–Fisher fixed point u* = O(ε) with critical exponents computable as power series in ε.
5. Irrelevant operators (negative scaling dimension) drop out of long-distance physics; this is the RG origin of universality and of the smallness of the number of relevant couplings in an EFT.
6. Classical statistical mechanics at a critical point is equivalent to Euclidean QFT in the massless limit (§10).
7. The 4D φ⁴ theory has no known nontrivial fixed point — the "triviality problem" (§13).
8. An exact differential RG equation for ℋ[σ] exists (§11) and its solutions are smooth surfaces in the space of Hamiltonians.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| RG iteration | τ(ℋ_l) = ℋ_{l+1} | Eq. 1.1 |
| Fixed-point condition | τ(ℋ*) = ℋ* | Eq. 1.2 |
| Ising Hamiltonian | ℋ = K Σ_{n,i} s_n s_{n+î} | §1.3 |
| Gaussian model | ℋ = − (1/2) ∫_q (q² + r) σ_q σ_{−q} | Eq. 3.15 |
| Gaussian propagator | Γ_q = 1/(q² + r) | Eq. 3.18 |
| Effective range | ξ² = ∫ x² Γ(x) dx / ∫ Γ(x) dx | Eq. 3.27 |
| RG rescaling | σ_q = ζ σ'_{2q}, ζ = 2^{1+d/2} | Eqs. 3.31, 3.33 |
| Gaussian recursion | r' = 4 r | Eq. 3.35 |
| Critical exponent | ν = ln 2 / ln λ | Eq. 3.42 (Gaussian λ=4 → ν=1/2) |
| φ⁴ action | ℋ = − (1/2)∫(q²+r)σσ − u ∫σσσσ | Eq. 4.2 |
| Hard-mode propagator | <σ_{1,q} σ_{1,q'}> = (2π)^d δ^d(q+q')/(q²+r) | Eq. 4.16 |
| Scaling dim. of u | [u] = 4 − d ≡ ε | §4 |
| Wilson–Fisher ν | ν = 1/2 + ε/12 + O(ε²) | §8 |
| Soft/hard split | σ_q = σ_{0,q} + σ_{1,q}; |q|<1/2 vs 1/2<|q|<1 | Eq. 4.3–4.4 |

## Relevance to Phonon-Exflation
Wilson–Kogut supplies the mathematical machinery for every regime of the framework. Three specific applications. (i) **Spectral action power counting.** The substrate's spectral action Tr f(D_K/Λ) is a non-renormalizable effective action (graviton sector, higher-curvature terms); RG dimensional analysis in ε = 4 − d (plus the heat-kernel coefficients a_{2k}) is the power-counting tool that identifies which operators survive at low energy (a_2 → Einstein–Hilbert, a_4 → Yang–Mills + Higgs) and which are irrelevant (a_6 and higher curvature invariants). This is the relevance of §§4–8 to every computation computation that uses the spectral action. (ii) **Coleman–Weinberg / effective potential.** The Gaussian + φ⁴ computation (§§3–5) IS the Coleman–Weinberg calculation of the effective potential for the Jensen deformation parameter τ; the gradient dS/dτ = +58,673 reported in framework constants is the fixed-point-neighbourhood slope, and the second derivative d²S/dτ² is the eigenvalue of the linearized τ transformation (Eq. 3.42 structure) that controls the transit physics. (iii) **Universality of the Ordered Veil.** The claim that the post-transit GGE relic is universal — independent of microscopic details — is exactly Wilson's universality (§12): only the relevant operators survive, and the integrable structure of the Ordered Veil is an irrelevant-operator observation. The ε-expansion machinery (§§4, 8) is the canonical tool for computing GGE observables order-by-order in (4−d). The triviality result of §13 is also relevant: if φ⁴ in 4D has only a Gaussian fixed point, then the Higgs mass must come from integrating out physics at a KK or Jensen scale, not from a free 4D Higgs — consistent with the framework's m_H = 131.8 GeV from KK threshold corrections.
