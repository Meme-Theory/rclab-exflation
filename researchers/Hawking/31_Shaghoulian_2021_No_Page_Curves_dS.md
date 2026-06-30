# No Page Curves for the de Sitter Horizon

**Author(s):** Joshua Kames-King, Evita M. H. Verheijden, and Erik P. Verlinde
**Year:** 2021 (revised 2022)
**Journal:** JHEP (preprint: arXiv:2108.09318)
**arXiv:** 2108.09318
**Relevance:** MEDIUM

---

## Abstract

We investigate the fine-grained entropy of the de Sitter cosmological horizon. Starting from three-dimensional pure de Sitter space, we consider a partial reduction approach, which supplies an auxiliary system acting as a heat bath both at $\mathcal{I}^+$ and inside the static patch. This allows us to study the time-dependent entropy of radiation collected for both observers in the out-of-equilibrium Unruh-de Sitter state, analogous to black hole evaporation for a cosmological horizon. Central to our analysis in the static patch is the identification of a weakly gravitating region close to the past cosmological horizon; this is suggestive of a relation between observables at future infinity and inside the static patch. We find that in principle, while the meta-observer at $\mathcal{I}^+$ naturally observes a pure state, the static patch observer requires the use of the island formula to reproduce a unitary Page curve. However, in practice, catastrophic backreaction occurs at the Page time, and neither observer will see unitary evaporation.

---

## Key Arguments and Derivations

### JT Gravity from dS$_3$ (Sec. 2)

Starting from 3D pure de Sitter space, dimensional reduction along one spatial direction yields 2D JT gravity on dS$_2$ with an auxiliary system. The reduced theory has:
- Dynamical JT gravity with dilaton $\Phi$ on dS$_2$
- A boundary action encoding the dynamics of the reduced direction
- Conformal matter (CFT with central charge $c$) added to model radiation

### Unruh-de Sitter State (Sec. 3)

The Unruh-de Sitter state is the analog of the Unruh state for black holes: only outgoing modes are excited, modeling an out-of-equilibrium evaporation process. The stress tensor is:
$$\langle T_{++} \rangle = 0, \quad \langle T_{--} \rangle = \frac{c}{48\pi\ell^2}$$
where $\ell$ is the dS radius.

### de Sitter Lifetime Estimate (Sec. 3.2)

The Page time for the dS horizon (when entropy of emitted radiation equals half the dS entropy):
$$t_{\text{Page}} = \frac{6\ell}{cG}$$

### Fine-Grained Entropy Calculations (Sec. 5)

**Meta-observer at $\mathcal{I}^+$:** Naturally sees a pure state. The entropy of radiation is zero at all times.

**Static patch observer:** Uses the island formula:
$$S_{\text{QG}}[\text{Rad}] = \min_I \operatorname{ext}_I \left[S_{\text{SCG}}[\text{Rad} \cup I] + \frac{\text{Area}(\partial I)}{4G}\right]$$

An island appears near the past cosmological horizon, producing a Page curve in principle.

### Catastrophic Backreaction (Sec. 5.3)

At the Page time, a trapped region forms. The bulk dilaton solution at $\sigma = 1/2$ (Page time) shows:
$$t > t_{\text{trapped}} = \frac{6\ell}{cG} = t_{\text{Page}}$$
The trapped region prevents radiation from reaching either the static patch observer or the meta-observer at $\mathcal{I}^+$. A quantum singularity forms at future infinity.

---

## Key Results

1. Meta-observer at $\mathcal{I}^+$ naturally sees a pure state (no Page curve needed)
2. Static patch observer requires the island formula to reproduce a unitary Page curve in principle
3. In practice, catastrophic backreaction occurs at the Page time, forming a trapped region
4. Neither observer actually sees unitary evaporation due to backreaction
5. The Page time coincides with the de Sitter destabilization time: $t_{\text{Page}} = 6\ell/(cG)$
6. The weakly gravitating region near the past cosmological horizon is identified as the natural location for island emergence

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Island formula | $S_{\text{QG}} = \min_I \operatorname{ext}_I\left[S_{\text{SCG}}[\text{Rad} \cup I] + \frac{\text{Area}(\partial I)}{4G}\right]$ | Eq. (1.1) |
| Unruh-dS stress tensor | $\langle T_{--} \rangle = \frac{c}{48\pi\ell^2}$ | Sec. 3.1 |
| Page time | $t_{\text{Page}} = \frac{6\ell}{cG}$ | Eq. (3.18) |
| Trapped region condition | $\partial_\pm \Phi < 0$ | Eq. (5.11) |
| Trapped time | $t_{\text{trapped}} = t_{\text{Page}} = \frac{6\ell}{cG}$ | Eq. (5.13) |

## Relevance to Phonon-Exflation

This paper is in direct tension with Paper 30 (Teresi): Teresi finds islands and Page curves for dS, while Kames-King, Verheijden, and Verlinde find that backreaction renders the Page curve unphysical before it completes. The phonon-exflation framework does not resolve this debate directly, as it has no horizon (transit dynamics, not static patch). However, the catastrophic backreaction at the Page time parallels the framework's finding that the BCS condensate is completely destroyed during transit ($P_{\text{exc}} = 1.000$) -- the analog of "catastrophic" change to the quantum state that prevents a simple thermodynamic description.
