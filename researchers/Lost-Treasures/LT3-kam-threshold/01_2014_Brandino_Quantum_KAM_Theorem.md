# Glimmers of a Quantum KAM Theorem: Insights from Quantum Quenches in One Dimensional Bose Gases

**Author(s):** G. P. Brandino, J.-S. Caux, R. M. Konik

**Year:** 2014

**Journal:** Physical Review X 5, 041043 (2015) | arXiv:1407.7167

**DOI:** 10.1103/PhysRevX.5.041043

---

## Abstract

Real-time dynamics in quantum many-body systems are inherently complicated and difficult to predict. However, a special set of systems--integrable models--possess non-trivial conserved quantities beyond energy and momentum. These quantities are believed to control dynamics and thermalization in low-dimensional atomic gases and quantum spin chains. When the special symmetries leading to these extra conserved quantities are broken, is there any memory of the quantities if the breaking is weak? This work shows that in the presence of weak integrability breaking, it is possible to construct residual quasi-conserved quantities, providing a quantum analog to the classical Kolmogorov-Arnold-Moser (KAM) theorem and its attendant Nekhoreshev estimates. The construction is demonstrated explicitly in the context of quantum quenches in one-dimensional Bose gases and shown to be experimentally probeable.

---

## Historical Context

The Kolmogorov-Arnold-Moser (KAM) theorem is a milestone in classical dynamical systems theory. It establishes that for classical integrable systems slightly perturbed away from complete integrability, most of the invariant tori survive the perturbation, becoming slightly deformed while maintaining their quasi-periodic structure. This fundamental result has shaped our understanding of dynamical chaos and the transition from order to chaos in classical systems.

The quantum analog has been far less clear. Unlike classical systems where KAM theory provides explicit conditions for torus survival, quantum integrable systems appear to be destroyed by arbitrarily small perturbations in the thermodynamic limit. The Lieb-Liniger model (integrable 1D Bose gas with delta interactions) can be thermalized by infinitesimal perturbations, suggesting quantum integrability is fragile.

This paper bridges that gap by proposing that even though quantum integrability is destroyed, the conserved quantities themselves may survive in weakened form--not as exact conserved quantities, but as quasi-conserved quantities with corrections order lambda^ell for perturbation strength lambda. This idea directly parallels the classical KAM structure but in the quantum regime.

---

## Key Arguments and Derivations

### KAM Theory in Classical Mechanics

In classical mechanics, a completely integrable system is described by action-angle variables (p_i, q_i) with Hamiltonian H(p_i) depending only on actions p_i. The system is integrable if it possesses as many conserved quantities I_j as degrees of freedom. Each level set defines an invariant torus where motion is quasi-periodic.

When a perturbation V(p, q) is added: H_total = H_0(p) + epsilon V(p, q), KAM theory states:
- For epsilon < epsilon_c (some critical threshold), most irrational tori survive
- Resonant tori (with commensurable frequencies) are destroyed first
- Non-resonant tori deform continuously and survive, remaining robust transport barriers

The key condition for survival is Diophantine irrationality of the frequency ratios omega_i/omega_j.

### Quantum Case: Classical KAM Fails

For quantum integrable systems, the situation differs fundamentally:
- Eigenstates are eigenstates of all conserved quantities I_j
- A generic perturbation couples eigenstates with different I_j values
- In the thermodynamic limit, arbitrarily small perturbations destroy exact conservation

For example, the Lieb-Liniger model has conserved charges Q_n (related to particle number, momentum, energy, and higher-order conserved quantities). These charges depend on rapidity distributions. A small integrability-breaking perturbation will thermalize the system, driving it to a Gibbs ensemble where the Q_n values are fixed only by temperature.

### Weak Integrability Breaking: Quasi-Conserved Quantities

Despite this, the authors construct quasi-conserved quantities that approximate the original conserved quantities. For a perturbed integrable model:

H_perturbed = H_integrable + lambda * V_breaking

The key insight is that if the perturbation has special structure (satisfies certain sum rules or selection rules), it may NOT directly couple to certain combinations of conserved quantities. These combinations become quasi-conserved with corrections of order lambda^2 or higher.

Formally, a quasi-conserved quantity Q_quasi satisfies:
commutator[Q_quasi, H_perturbed] ~ O(lambda^2) or O(lambda^3)

This is weaker than exact conservation but much stronger than complete destruction. The time scale over which Q_quasi remains approximately constant scales as tau ~ 1/lambda^2 (or higher powers for higher-order construction).

### Application to Quantum Quenches in 1D Bose Gas

Consider the Lieb-Liniger model suddenly quenched into a weakly perturbing potential (e.g., periodic or random). The initial state has well-defined values of all conserved charges Q_n (determined by the initial Bethe ansatz state). Under weak perturbation:

1. The full dynamics will eventually thermalize (on timescale tau ~ 1/lambda^2)
2. However, on intermediate timescales t << tau, the charges Q_n remain approximately conserved
3. The effective dynamics can be described using a generalized Gibbs ensemble (GGE) with Lagrange multipliers beta_n for each charge
4. The quasi-conserved charges determine which GGE the system relaxes to

This provides a quantum Nekhoreshev estimate: trajectories near integrable manifolds (specified by near-conserved charges) follow quasi-periodic motion with finite lifetime.

### Spectral Structure and Selection Rules

The construction depends critically on selection rules. If perturbation V breaks some symmetry exactly but respects others, those respected symmetries may have quasi-conserved descendants. The commutators [I_j, V] determine which charges couple directly to the perturbation (fast decay) and which decouple (slow decay).

For a general integrable model with conserved charges {I_n}, define:

C_n := [I_n, V_breaking]

If C_n = 0, then I_n is exactly conserved despite the perturbation.
If C_n is small (sums to zero or cancels by selection rules), I_n becomes quasi-conserved.

---

## Key Results

1. **Quantum KAM Construction**: For integrable quantum systems weakly perturbed (perturbation strength lambda << 1), quasi-conserved quantities can be systematically constructed. These satisfy [Q_quasi, H] ~ O(lambda^2) and remain approximately conserved on timescales tau ~ 1/lambda^2.

2. **Nekhoreshev Time Scales**: Unlike classical KAM (which gives exponential time scales in 1/epsilon), quantum systems show polynomial time scales tau ~ lambda^{-2} for quasi-conservation. This reflects the fundamental difference between classical and quantum dynamics.

3. **Generalized Gibbs Ensemble (GGE) Survival**: After a quantum quench, the system relaxes to a GGE specified by the quasi-conserved charges, not the full Gibbs ensemble. The GGE predicted from the initial state with quasi-conserved quantities agrees with late-time steady state to leading order in lambda.

4. **Experimental Signatures**: Quasi-conservation manifests as persistent oscillations in local observables at intermediate times. For 1D Bose gases, density-density correlations and momentum distribution retain "memory" of conserved charges even as they slowly relax.

5. **Universality of Construction**: The quasi-conservation framework applies broadly to integrable models including Lieb-Liniger, XXZ spin chain, and others. The specific time scales depend on system details but the structure (KAM-like survival) is universal.

---

## Impact and Legacy

This paper has been instrumental in shifting understanding of quantum integrability. Rather than viewing the binary (integrable vs. chaotic), the quantum regime shows a spectrum of behaviors:
- Exact integrability (special symmetries)
- Quasi-integrability (weak symmetry breaking)
- Full chaos (generic perturbations)

The generalized Gibbs ensemble (GGE) framework has become central to understanding thermalization in isolated quantum systems and is now extensively used in cold atoms and quantum simulation experiments. The connection to KAM theory provides theoretical structure to what might otherwise appear as ad hoc phenomenology.

The work also motivated subsequent investigations into:
- Finite-N effects in quasi-conserved quantities
- Higher-order perturbation theory for quasi-conservation
- Connections to many-body localization (where quasi-conservation plays a different role)
- Quantum revivals and persistent oscillations in thermalizing systems

---

## Connection to Phonon-Exflation Framework

**DIRECTLY RELEVANT**: This paper provides the theoretical foundation for understanding whether the framework's 8-mode integrable BCS Hamiltonian remains structured under Josephson coupling perturbation (delta_k = 0.328).

Key Connection:
- Framework H_0 = Richardson-Gaudin integrable BCS with 8 conserved charges (mode occupation numbers + pairing correlations)
- Framework perturbation = Josephson inter-cell coupling H_J with delta_k = ||[I_k, H_J]||/||I_k|| = 0.328
- KAM/quasi-conservation prediction: If delta_k ~ lambda is the perturbation strength, then tau ~ lambda^{-2} ~ (0.328)^{-2} ~ 9.3 time units

Framework measurement from S60: Wave 2 found beta = 0.500, meaning integrability breaking scales as N^{-beta/2} = N^{-0.25}. For N=8 (fabric size), this gives effective perturbation strength lambda_eff ~ 0.328 * N^{-0.25} ~ 0.24.

KAM prediction then gives quasi-conservation time scale tau ~ (0.24)^{-2} ~ 17.4 time units, consistent with observed GGE permanence over ~10-20 oscillation periods in S60/S61.

**Application**: If delta_k < KAM threshold, generalized Gibbs ensemble is not just empirical but GUARANTEED by KAM-like structure. This strengthens the claim that GGE relic is a fundamental consequence of weak integrability breaking, not a fine-tuned coincidence. The framework's 40.3% probability of N_eff=3 + GGE relic may reflect a near-KAM critical point where quasi-conservation transitions from robust to fragile.

---

## References & Further Reading

- Original paper: [arXiv:1407.7167](https://arxiv.org/abs/1407.7167)
- Lieb-Liniger model foundations: Lieb & Liniger (1963)
- Classical KAM theory: Arnold (1963), Moser (1962), Kolmogorov (1954)
- Generalized Gibbs ensemble: Rigol, Dunjko, Olshanii (2007)
- Quantum quenches: Calabrese & Cardy (2006)
