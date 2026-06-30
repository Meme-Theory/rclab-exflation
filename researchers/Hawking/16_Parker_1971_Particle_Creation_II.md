# Quantized Fields and Particle Creation in Expanding Universes. II

**Author(s):** Leonard Parker
**Year:** 1971
**Journal:** Physical Review D 3, 346-356 (1971)
**arXiv:** N/A (pre-arXiv)
**Relevance:** CRITICAL

---

## Abstract

[INCOMPLETE - pre-arXiv, no PDF available]

---

## Key Arguments and Derivations

[INCOMPLETE - pre-arXiv, no PDF available]

### Core Results (from published record)

This paper extends the Part I formalism to **spin-1/2 fields** (fermions) in expanding universes, establishing that fermionic particle creation also occurs via Bogoliubov transformations, but with critical differences from the bosonic case due to the Pauli exclusion principle.

### Fermionic Bogoliubov Transformation

For a Dirac field in an expanding FRW spacetime, the mode functions at early and late times are related by:

$$u_k^{\text{out}} = \alpha_k u_k^{\text{in}} + \beta_k v_{-k}^{\text{in}}$$

where $u_k$ are positive-frequency spinor modes and $v_k$ are negative-frequency (antiparticle) modes. The Bogoliubov coefficients now satisfy the **fermionic normalization**:

$$|\alpha_k|^2 + |\beta_k|^2 = 1$$

(Note the **plus** sign, in contrast to the bosonic minus sign, reflecting the anticommutation relations of fermionic creation/annihilation operators.)

### Fermionic Particle Number

The expected number of fermion-antifermion pairs created in mode $k$ is:

$$N_k = |\beta_k|^2$$

with the crucial constraint $N_k \leq 1$ (Pauli exclusion), enforced by the normalization $|\alpha_k|^2 + |\beta_k|^2 = 1$.

### Spin-Statistics and Particle Creation

Parker showed that the spin-statistics connection is essential for consistency of particle creation:
- **Bosons**: $|\alpha_k|^2 - |\beta_k|^2 = 1$, allowing $N_k = |\beta_k|^2$ to be arbitrarily large (stimulated emission / Bose enhancement).
- **Fermions**: $|\alpha_k|^2 + |\beta_k|^2 = 1$, restricting $N_k \leq 1$ (Pauli blocking).

### Conformal Invariance

Massless spin-1/2 fields are conformally invariant in 4D and therefore experience no particle creation in conformally flat spacetimes (just as for conformally coupled scalar fields). Mass breaks conformal invariance and enables creation.

---

## Key Results

1. **Fermionic particle creation** occurs in expanding universes via Bogoliubov transformations with fermionic normalization $|\alpha_k|^2 + |\beta_k|^2 = 1$.
2. The Pauli exclusion principle limits $N_k \leq 1$ per mode, fundamentally distinguishing fermionic from bosonic production.
3. The spin-statistics theorem is essential for consistency of the particle creation formalism.
4. Massless fermions are conformally invariant and not created in conformally flat spacetimes.
5. Massive fermions ARE created, with a rate that depends on $m/H$ (mass relative to Hubble parameter).

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Fermionic Bogoliubov | $u_k^{\text{out}} = \alpha_k u_k^{\text{in}} + \beta_k v_{-k}^{\text{in}}$ | Sec. II |
| Fermionic normalization | $\|\alpha_k\|^2 + \|\beta_k\|^2 = 1$ | Sec. II |
| Fermionic particle number | $N_k = \|\beta_k\|^2 \leq 1$ | Sec. II |
| Bosonic normalization | $\|\alpha_k\|^2 - \|\beta_k\|^2 = 1$ | Comparison |
| Dirac equation (FRW) | $(i\gamma^\mu \nabla_\mu - m)\psi = 0$ with spin connection | Sec. II |
| Conformal invariance | $m = 0$ Dirac: no creation in conformally flat spacetime | Sec. III |

## Relevance to Phonon-Exflation

The fermionic Bogoliubov formalism is directly relevant to the transit mechanism: the Dirac operator $D_K(\tau)$ on $M^4 \times SU(3)$ has both bosonic and fermionic sectors. The transit creates quasiparticle pairs from the Dirac spectrum via exactly these Bogoliubov transformations. The fermionic normalization $|\alpha|^2 + |\beta|^2 = 1$ (Pauli blocking) is the origin of the constant-ratio trap $F/B = 0.55$ in the spectral action (fermionic sector has 16 modes, bosonic 44). The BCS condensate in the B2 sector is a fermionic Cooper pair -- its creation during transit follows Parker's fermionic formalism, with the crucial addition of BCS pairing correlations (Richardson-Gaudin integrability).
