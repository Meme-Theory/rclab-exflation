# A Holographic RG Flow from the Squashed to the Round S^7

**Author(s):** Bastien Duboeuf, Michele Galli, Emanuel Malek, Henning Samtleben
**Year:** 2023
**Journal:** [Not stated in PDF, HU-EP-23/19 preprint]
**arXiv:** 2306.11789
**Relevance:** HIGH (Domain wall solution interpolating squashed/round S^7; ExFT KK couplings along RG flow; directly relevant to SU(3) deformation dynamics)

---

## Abstract

We construct and analyze the domain wall solution in D = 11 supergravity connecting the N = 1, AdS_4 x S^7_squashed vacuum to the N = 8, AdS_4 x S^7_round vacuum. This domain wall describes the holographic renormalization group flow from an Sp(2) x Sp(1) symmetric UV fixed point to the SO(8) symmetric IR fixed point. It breaks all supersymmetries which are (partially) restored at its endpoints. We show how recent techniques from exceptional field theory allow us to compute the quadratic couplings of all Kaluza-Klein fluctuations around the domain wall background, encoding all two-point correlators along the holographic RG flow.

---

## Key Arguments and Derivations

### 1. The Two S^7 Vacua (Section 2)

The D = 11 metric preserving Sp(2) x Sp(1) isometries has two scalar fields u (size) and v (squashing):

ds^2 = e^{-7u} ds^2_(4) + (1/4) e^{2u} [e^{3v}(d mu^2 + (1/4)sin^2 mu sum omega_i^2) + (1/4) e^{4v} sum (nu_i + cos mu omega_i)^2]

with 4-form flux F = Q e^{-21u} epsilon_(4). The consistent truncation gives the D = 4 Lagrangian:

|g|^{-1/2} L = R_(4) - (63/2) d_mu u d^mu u - 21 d_mu v d^mu v - V_pot

V_pot = -6 e^{-9u+4v} - 48 e^{-9u-3v} + 12 e^{-9u-10v} + 2Q^2 e^{-21u}

**Two critical points (Q = 3):**
- Round S^7: u = 0, v = 0, ell_round = 1/2
- Squashed S^7: u = u_0, v = v_0, ell_squashed = 5^{5/4}/(2 . 3^{7/4})

### 2. The Domain Wall Solution (Section 2)

The interpolating domain wall satisfies second-order flow equations:

u'' + 3A'u' = -6e^{-21u} - (12/7)e^{-9u-10v} + (48/7)e^{-9u-3v} + (6/7)e^{-9u+4v}
v'' + 3A'v' = -(20/7)e^{-9u-10v} + (24/7)e^{-9u-3v} - (4/7)e^{-9u+4v}

**Key point:** There is NO first-order superpotential formulation connecting both vacua. The potential can be written as V_pot = (16/63)(d_u W)^2 + (8/21)(d_v W)^2 - 12W^2, but only the squashed S^7 is a critical point of W (the round S^7 appears as N = 0 within this N = 1 truncation).

The flow is numerically constructed as a kink solution. The conformal dimensions of dual operators are:

O_u: Delta_UV = 6 = Delta_IR
O_v: Delta_UV = 5/3, Delta_IR = 4

The UV (squashed) endpoint is a **relevant deformation** of dimension Delta = 5/3.

### 3. Generalised Parallelisation in ExFT (Section 3)

The squashed S^7 family is embedded into E_{7(7)} ExFT via the generalized vielbein:

V(x,y) = U_round(y) S(y) W(x) S^{-1}(y)

where S(y) is the Sp(2) x Sp(1) coset representative and W(x) lives in the commutant of the denominator group H = Sp(1)_L x Sp(1)_D in E_{7(7)}.

**Scalar target space of the N = 1 truncation:**
M_scalar = SL(2)/SO(2) x SL(2)/SO(2)

(a Kahler manifold parametrized by 4 scalar fields).

The generalized frame has **y-dependent intrinsic torsion** X_{ABC}(y) (not constant, unlike the N = 8 case), reflecting the absence of a consistent truncation to N = 8.

### 4. Quadratic KK Couplings (Section 4)

The mass operator for scalar KK fluctuations is:

(M_{spin-0})_{IJ} = M^(0)_{IJ} + (N_{IJC} - N_{JIC}) d_C + d_C N_{IJC} + delta_{IJ} M_{spin-2}

with M^(0) expressed purely in terms of the intrinsic torsion X_{ABC}.

**[0,0,0] sector (4 scalars):** Reproduces the linearized potential of the N = 1 truncation. Serves as a consistency check.

**[0,1,2] sector (8 scalars):** Contains Goldstone modes that become physical scalars on the round S^7. The potential depends on only 3 of 8 fields; the remaining 5 are Goldstone modes along the entire flow.

**[0,2,4] sector (6 scalars):** Potential depends on 5 of 6 fields; 1 Goldstone mode throughout the flow.

All quadratic couplings reproduce the correct masses at both endpoints (squashed and round).

### 5. Universal Conformal Dimension Formula

At the squashed S^7 endpoint, the KK spectrum organizes into long N = 1 supermultiplets L[J, Delta] with:

Delta_{J,s} = 1 + (5/3)s + (1/3) sqrt{(3J + 2s^2)^2 + 5 C_3}

where C_3 is a combination of Sp(2) and Sp(1) quadratic Casimirs:
C_3 = C(p,q) + 3C(r) = (1/2)(p^2 + 2q^2 + 4p + 6q + 2pq) + (3/4)r(r+2)

---

## Key Results

1. **Domain wall existence**: Numerical construction of the non-supersymmetric domain wall connecting squashed (N=1, UV) to round (N=8, IR) S^7, clarifying earlier claims in the literature.

2. **No superpotential**: The flow cannot be described by first-order equations, since the round S^7 is not a critical point of the superpotential in the N = 1 truncation.

3. **ExFT embedding**: The squashed S^7 family admits a generalized parallelisation (globally well-defined generalized frame) but with non-constant intrinsic torsion.

4. **Quadratic KK couplings**: First computation of all two-point couplings for higher KK modes along a domain wall solution, using ExFT mass operators.

5. **Consistency checks**: All computed couplings reproduce correct masses at both flow endpoints.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| D=11 metric ansatz | $ds^2 = e^{-7u}ds^2_{(4)} + \frac{1}{4}e^{2u}\left[e^{3v}(d\mu^2+\frac{1}{4}\sin^2\mu\sum\omega_i^2) + \frac{1}{4}e^{4v}\sum(\nu_i+\cos\mu\,\omega_i)^2\right]$ | Eq. (2.1) |
| D=4 potential | $V = -6e^{-9u+4v}-48e^{-9u-3v}+12e^{-9u-10v}+2Q^2e^{-21u}$ | Eq. (2.4) |
| Squashed S^7 vacuum | $u_0 = \frac{5}{42}\ln 5 - \frac{1}{6}\ln 3$, $v_0 = \frac{1}{7}\ln 5$ | Eq. (2.5) |
| Flow equations | $u''+3A'u' = -6e^{-21u}-\frac{12}{7}e^{-9u-10v}+\frac{48}{7}e^{-9u-3v}+\frac{6}{7}e^{-9u+4v}$ | Eq. (2.7) |
| Universal Delta formula | $\Delta_{J,s} = 1+\frac{5}{3}s+\frac{1}{3}\sqrt{(3J+2s^2)^2+5C_3}$ | Eq. (4.3) |
| Casimir combination | $C_3 = \frac{1}{2}(p^2+2q^2+4p+6q+2pq)+\frac{3}{4}r(r+2)$ | Eq. (4.4) |
| Generalized vielbein | $\mathcal{V}(x,y) = \mathring{U}(y)\,S(y)\,\mathcal{W}(x)\,S^{-1}(y)$ | Eq. (3.20) |
| N=1 scalar target | $\mathcal{M}_{\mathrm{scalar}} = \frac{SL(2)}{SO(2)}\times\frac{SL(2)}{SO(2)}$ | Eq. (3.22) |
| Superpotential | $V = \frac{16}{63}(\partial_u W)^2+\frac{8}{21}(\partial_v W)^2-12W^2$ | Eq. (2.8) |

---

## Relevance to Phonon-Exflation

This paper provides **direct analogy and computational methods** for the framework's transit dynamics:

1. **Squashed-to-round S^7 as a deformation flow**: The domain wall interpolating between squashed (UV) and round (IR) S^7 is the D=11 supergravity analog of the Jensen deformation tau on SU(3). The squashed S^7 preserves Sp(2) x Sp(1) subset SO(8), just as the Jensen-deformed SU(3) preserves a subgroup. The flow is a holographic RG flow, and the framework's transit can be viewed in this light.

2. **No superpotential = no first-order dynamics**: The absence of a superpotential connecting both endpoints mirrors the framework's discovery (Session 37) that the instanton gas dynamics cannot be described by a simple potential well. The flow requires second-order equations, paralleling the "no stabilization mechanism" finding.

3. **Sp(2) x Sp(1) KK decomposition**: The decomposition of SO(8) reps under Sp(2) x Sp(1) identifies the scalar singlets at KK levels 0, 2, 4 (Eq. 3.15). This is directly analogous to the framework's identification of Jensen-invariant modes in the D_K spectrum.

4. **ExFT mass operators**: The universal mass formula (Eq. 3.11-3.12) for KK fluctuations around a generalized parallelisable background is the technical tool that would be needed to compute the full KK spectrum around the framework's SU(3) deformation endpoint.

5. **Non-constant intrinsic torsion**: The y-dependence of X_{ABC}(y) for the squashed S^7 parallels the tau-dependence of the framework's D_K. The "space-invader" level mixing caused by non-constant intrinsic torsion is the ExFT manifestation of the same mode-mixing seen in the framework's Dirac spectrum at different tau values.
