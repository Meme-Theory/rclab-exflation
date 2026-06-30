# Flat band and Planckian metal

**Author(s):** G. E. Volovik
**Year:** 2019
**Journal:** JETP Letters 110, 352-353 (2019)
**arXiv:** 1907.11515
**Relevance:** CRITICAL

---

## Abstract

We discuss the recent extension of the Sachdev-Ye-Kitaev (SYK) microscopic model by Patel and Sachdev in arXiv:1906.03265, which demonstrates the characteristic features of the Khodel-Shaginyan fermion condensate -- the existence of the finite region of momenta, where the energy of electrons is exactly zero (the flat band). The microscopic derivation of the flat band in this interacting model supports the original idea of Khodel and Shaginyan based on the phenomenological approach. It also suggests that it is the flat band, which is responsible for the linear dependence of resistivity on temperature in "strange metals".

---

## Key Arguments and Derivations

### 1. The Khodel-Shaginyan Fermion Condensate
Volovik connects the Patel-Sachdev (PS) lattice extension of the SYK model to the 1990 prediction by Khodel and Shaginyan (KS) of a "fermion condensate" -- a state where the quasiparticle energy $\varepsilon(p)$ is exactly zero over a finite region of momentum space, forming a flat band.

The KS flat band arises from the Landau theory of Fermi liquids. Variation of the energy functional over occupancy $n(p)$ yields two solutions:
1. $\varepsilon(p) = 0$ (flat band region)
2. $\delta n(p) = 0$ (meaning $n(p) = 0$ or $n(p) = 1$)

$$\delta E\{n(p)\} = \int \varepsilon(p)\,\delta n(p)\,d^dp = 0$$

### 2. Weak vs. Strong Interaction Regimes

**Weak interaction (Landau Fermi liquid):** The solution $\varepsilon(p) = 0$ holds only on the Fermi surface (a single momentum $p_F$). Outside: $n(p) = 0$ or $n(p) = 1$ (sharp step function).

**Strong interaction (Khodel-Shaginyan):** The solution $\varepsilon(p) = 0$ extends over a finite region $[p_1, p_2]$ of momentum space. In this region, $0 < n(p) < 1$ -- the occupancy is neither 0 nor 1. This is the flat band / fermion condensate.

### 3. Connection to Patel-Sachdev SYK Model
Volovik identifies that the PS paper's Figure 2a shows $n(p)$ exhibiting the characteristic KS behavior: a finite region where $0 < n(p) < 1$. Their Figure 3a shows the electron spectral density with $\varepsilon(p) = 0$ in this region -- exactly the KS flat band.

The extended SYK model thus provides a **microscopic derivation** of the KS fermion condensate, supporting the original phenomenological argument.

### 4. Consequences for Superconductivity
The flat band has singular density of states. As a result:
- The superconducting gap $\Delta$ is **proportional** to the coupling constant (not exponentially suppressed as in BCS)
- The transition temperature $T_c \propto g$ (linear in coupling, following Belyaev's 1961 result for nuclear systems)
- This replaces the standard BCS relation $T_c \propto \exp(-1/gN(0))$

### 5. Flat Band as Origin of Planckian Metal / Strange Metal
The universal linear-in-$T$ resistivity observed in "strange metals" (bad metals) -- including overdoped cuprates, pnictides, and magic-angle graphene -- is a characteristic signature of Planckian dissipation: $\tau^{-1} \sim k_B T/\hbar$.

Volovik argues that in the PS model, the linear-$T$ resistivity emerges precisely in the regime where the KS flat band signatures are transparent. Therefore, the **flat band is responsible for Planckian dissipation**.

### 6. Multiple Sources of Flat Bands
Volovik notes diverse origins for electronic flat bands:
- **Electron-electron interaction** (Khodel-Shaginyan, 1990; microscopically via SYK model)
- **Geometry/topology**: Kagome lattice, topological surface states, nodal line semimetals
- **Twist engineering**: magic-angle twisted bilayer graphene (where interaction further flattens the spectrum beyond geometric flattening)
- **Rigorous derivation**: Yudin et al. (2014) near van Hove singularities in the Hubbard model on triangular lattice
- **Black hole analog**: Lee (2009), charged black hole gives "critical Fermi ball"
- **Experimental**: merging of Landau levels in strongly-interacting 2D electron systems in silicon (Shashkin et al. 2014; Melnikov et al. 2017)

## Key Results

1. The Patel-Sachdev lattice SYK model microscopically realizes the Khodel-Shaginyan fermion condensate (flat band)
2. The flat band is responsible for Planckian (linear-$T$) resistivity in strange metals
3. Superconducting gap and $T_c$ are **linear** in coupling constant for flat-band systems (not exponentially suppressed)
4. The extended SYK model validates the 1990 Khodel-Shaginyan phenomenological prediction
5. Evidence accumulates from multiple directions (SYK, twisted graphene, silicon 2DEG) that interaction-driven flat bands are generic in strongly correlated systems

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Energy functional variation | $\delta E\{n(p)\} = \int \varepsilon(p)\,\delta n(p)\,d^dp = 0$ | Fig. 1 |
| Two solutions | $\varepsilon(p) = 0$ or $\delta n(p) = 0$ | Fig. 1 |
| KS flat band condition | $\varepsilon(p) = 0$ for $p \in [p_1, p_2]$, with $0 < n(p) < 1$ | Fig. 1 (right) |
| Flat-band $T_c$ scaling | $T_c \propto g$ (linear in coupling, not exponential) | Ref. 8 (Belyaev) |
| Flat-band $\Delta$ scaling | $\Delta \propto g$ (proportional to coupling constant) | Text |
| Planckian dissipation | $\tau^{-1} \sim k_B T/\hbar$ | Refs. 17-20 |
| Standard BCS (for contrast) | $T_c \propto \exp(-1/gN(0))$ | Implicit |

## Relevance to Phonon-Exflation

This paper is a critical bridge between Volovik's superfluid cosmology program and the framework's BCS mechanism on SU(3). The key insight: interaction-driven flat bands (fermion condensate) produce $T_c \propto g$ instead of the exponentially suppressed BCS result. The framework's Dirac spectrum on SU(3) at the fold has near-degenerate gap-edge modes (the constant-ratio trap) that constitute an approximate flat band. The Khodel-Shaginyan mechanism shows that even without geometric flat bands, **strong interactions alone** can flatten the spectrum and produce divergent DOS -- precisely what the framework's RPA + van Hove chain achieves. The connection to Planckian dissipation ($\tau^{-1} \sim k_BT/\hbar$) links to the framework's GGE post-transit state: if the emergent 4D matter inherits flat-band characteristics from the SU(3) BCS, it would naturally exhibit strange-metal phenomenology. Volovik's program (superfluid universe $\to$ flat band $\to$ Planckian metal) maps directly onto the framework's chain (SU(3) BCS $\to$ van Hove flat band $\to$ emergent matter).
