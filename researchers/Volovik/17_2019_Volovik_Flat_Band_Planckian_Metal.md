# Flat band and Planckian metal

**Author(s):** G.E. Volovik
**Year:** 2019
**Journal:** Pis'ma v ZhETF (submitted)
**arXiv:** 1907.11515
**Relevance:** HIGH

---

## Abstract

We discuss the recent extension of the Sachdev-Ye-Kitaev (SYK) microscopic model, which demonstrates the characteristic features of the Khodel-Shaginyan fermion condensate -- the existence of the finite region of momenta, where the energy of electrons is exactly zero (the flat band). The microscopic derivation of the flat band in this interacting model supports the original idea of Khodel and Shaginyan based on the phenomenological approach. It also suggests that it is the flat band, which is responsible for the linear dependence of resistivity on temperature in "strange metals".

---

## Key Arguments and Derivations

### Khodel-Shaginyan Fermion Condensate
From Landau Fermi liquid theory, variation of the energy functional over occupancy $n(\mathbf{p})$ gives two solutions:
1. $\delta n(\mathbf{p}) = 0$ (i.e., $n = 0$ or $n = 1$) — conventional Fermi liquid
2. $\epsilon(\mathbf{p}) = 0$ — the Khodel-Shaginyan flat band

In weak interaction, solution (2) holds only on the Fermi surface. In strong interaction, it holds in a finite region of momentum space $p_1 < p < p_2$, where $0 < n(p) < 1$.

### Connection to SYK/Planckian Metal
The Patel-Sachdev lattice extension of the SYK model produces:
- A finite region where $0 < n(p) < 1$ (Fig. 2a of Patel-Sachdev)
- Zero quasiparticle energy in this region (Fig. 3a of Patel-Sachdev)

These are precisely the signatures of the KS flat band. The model also produces universal linear-$T$ resistivity, suggesting the flat band is responsible for "strange metal" / Planckian dissipation behavior.

### Variational Principle
The Landau functional variation:

$$\delta E\{n(\mathbf{p})\} = \int \epsilon(\mathbf{p}) \, \delta n(\mathbf{p}) \, d^dp = 0$$

admits the flat band solution $\epsilon(\mathbf{p}) = 0$ in a finite momentum region when interaction is strong enough. This provides singular density of states and:
- $T_c \propto \lambda$ for superconductivity (linear, not exponential)
- $\rho \propto T$ for resistivity (Planckian dissipation)

## Key Results

1. The extended SYK model microscopically realizes the Khodel-Shaginyan flat band
2. The flat band is responsible for linear-$T$ resistivity in strange metals
3. Two solutions of Landau theory ($\delta n = 0$ and $\epsilon = 0$) distinguish conventional Fermi liquid from flat band state
4. In the flat band region, $0 < n(p) < 1$ with $\epsilon(p) = 0$ identically
5. This supports flat band as the origin of Planckian dissipation

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Landau variation | $\delta E = \int \epsilon(\mathbf{p}) \, \delta n(\mathbf{p}) \, d^dp = 0$ | Fig. 1 |
| Flat band condition | $\epsilon(\mathbf{p}) = 0$ for $p_1 < p < p_2$ | KS theory |
| Planckian dissipation | $\rho \propto T$ | Patel-Sachdev |

## Relevance to Phonon-Exflation

- The flat band as interaction-driven phenomenon connects to the framework's BCS ground state: when coupling is strong enough, the conventional Fermi surface gives way to a fundamentally different state
- The singular DOS at zero energy parallels the framework's Van Hove singularity driving the BCS instability
- Planckian dissipation ($\rho \propto T$) in the flat band regime suggests the transit phase may exhibit similar universal transport
- The SYK connection provides a quantum-gravity analog: SYK models have been connected to AdS$_2$/nearly-AdS$_2$ holography, suggesting the flat band physics has gravitational dual
