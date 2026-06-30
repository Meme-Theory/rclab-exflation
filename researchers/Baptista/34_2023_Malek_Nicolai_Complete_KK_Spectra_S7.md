# The Complete Kaluza-Klein Spectra of N = 1 and N = 0 M-theory on AdS_4 x (squashed S^7)

**Author(s):** Joel Karlsson and Bengt E.W. Nilsson
**Year:** 2023 (revised 2024)
**Journal:** [Prepared for submission to JHEP]
**arXiv:** 2305.00916
**Relevance:** HIGH (Complete KK spectrum including spin-3/2; N = 1 supermultiplet assignment; boundary conditions and marginal operators for stability)

---

## Abstract

The squashed seven-sphere operator spectrum is completed by deriving the spectrum of the spin-3/2 operator. The implications of the results for the AdS_4 N = 1 supermultiplets obtained from compactification of eleven-dimensional supergravity are analysed. The weak G_2 holonomy plays an important role when solving the eigenvalue equations on the squashed sphere. Here, a novel and more universal algebraic approach to the whole eigenvalue problem on coset manifolds is provided. Having obtained full control of all the operator spectra, we can finally determine the irreps D(E_0, s) for all supermultiplets in the left-squashed vacuum. This includes an analysis of possible boundary conditions. By performing an orientation flip on the seven-sphere, we also obtain the full spectrum for the non-supersymmetric right-squashed compactification which is of interest in the swampland context and in particular for the AdS swampland conjecture.

---

## Key Arguments and Derivations

### 1. The Squashed S^7 Eigenvalue Problem (Section 2)

The squashed S^7 is a coset manifold Sp(2) x Sp(1) / Sp(1) x Sp(1) with weak G_2 holonomy. The key operators whose spectra are needed are:

| Operator | Description |
|:---------|:------------|
| Delta_0 | Scalar Laplacian |
| /D_{1/2} | Dirac operator on spinors |
| Delta_1 | Hodge-de Rham on 1-forms |
| /D_{3/2} | Spin-3/2 operator on vector-spinors |
| Delta_2 | Hodge-de Rham on 2-forms |
| Delta_L | Lichnerowicz Laplacian on TT 2-tensors |
| Q | Operator on 3-forms |

**Universal Laplacian (Eq. 2.9):**
Delta = -Box - [D_a, D_b] Sigma^{ab} = -Box - R_{abcd} Sigma^{ab} Sigma^{cd}

This acts on any tensor field, not just p-forms, and becomes the Lichnerowicz operator on TT symmetric 2-tensors.

**Coset master equation (Eq. 2.15):**
D_a Y + (1/2) f_{abc} Sigma^{bc} Y = -T_a Y

This algebraizes the differential eigenvalue problem, converting Laplacians to algebraic expressions in group generators.

### 2. Improved Methodology (Section 2.2)

The paper derives a **universal group-theoretic formula for Weyl tensor eigenvalues** acting on any isotropy irrep. For a normal homogeneous coset, the Riemann tensor is:

R^{cd}_{ab} = f^{cd}{}_i f_{iab} + (1/2) f^{cd}{}_e f_{eab} + (1/2) f_{[c|a|e} f_{d]eb}

The Weyl tensor action on each H-irrep is computed via the coset master equation, avoiding case-by-case analysis.

### 3. Complete Operator Eigenvalue Spectra (Section 3)

**All operators except spin-3/2** (Section 3.1): Rederived using the improved algebraic formalism. Key results for the Einstein-squashed case:

- Scalar: Delta_0 eigenvalues labeled by Sp(2) x Sp(1) irreps (p,q;r) with explicit formula
- Dirac: eigenvalues of i/D_{1/2} with two branches
- 1-form: Delta_1 eigenvalues with transverse projection
- 2-form: Delta_2 eigenvalues with transverse and co-transverse projections
- Lichnerowicz: Delta_L eigenvalues on TT symmetric 2-tensors

**Spin-3/2 spectrum** (Section 3.2): The novel result of this paper. The spin-3/2 operator on the squashed S^7 is:

(i/D_{3/2} + (3m/2)) psi_a  eigenvalues

solved using the algebraic approach with weak G_2 structure. The gamma-trace constraint eliminates non-physical modes.

**Summary (Section 3.3):** Complete eigenvalue spectrum for all operators on the squashed S^7, organized by Sp(2) x Sp(1) representations (p,q;r).

### 4. Eigenmodes and Isometry Irreps (Section 4)

Explicit construction of eigenmodes for 1-forms, spinors, and 2-forms. Key finding: certain pairs of eigenvalues are **degenerate** (same eigenvalue, different eigenmodes), leading to ambiguities in the supermultiplet assignment.

**Two-form modes** (Section 4.2): Complete construction of all two-form Laplacian eigenmodes on the squashed S^7. This is done for the first time, revealing the degeneracy pattern.

### 5. N = 1 and N = 0 Spectra (Section 5)

**Mass-energy relations (Table 2):** For AdS_4 fields of spin s and mass M:

- s = 2: E_0 = 3/2 + (1/2)sqrt{(M/m)^2 + 9}
- s = 3/2: E_0 = 3/2 + (1/2)|M/m - 2|
- s = 1: E_0 = 3/2 + (1/2)sqrt{(M/m)^2 + 1}
- s = 1/2: E_0 = 3/2 +/- (1/2)|M/m|
- s = 0: E_0 = 3/2 +/- (1/2)sqrt{(M/m)^2 + 1}

**Mass operators (Table 3):** Relations between mass M and internal operator eigenvalues for Freund-Rubin compactifications:

- Spin-2: M^2 from Delta_0
- Spin-3/2: M from i/D_{1/2} or i/D_{3/2}
- Spin-1: M^2 from Delta_1 or Delta_2
- Spin-1/2: M from i/D_{1/2} or i/D_{3/2}
- Spin-0: M^2 from Delta_0, Delta_L, or Q operator

### 6. Supermultiplet Content (Section 5.1)

The N = 1 left-squashed S^7 spectrum contains:

- 1 x graviton multiplet (max spin 2)
- 6 x gravitino multiplets (max spin 3/2)
- 6 x vector multiplets type B (max spin 1-)
- 8 x vector multiplets type A (max spin 1+)
- 14 x Wess-Zumino multiplets (max spin 1/2)

Each multiplicity refers to the number of infinite towers. All supermultiplets are verified to have consistent E_0 values across all spins.

### 7. Boundary Conditions and Marginal Operators (Section 5.2)

**Skew-whiffing** (Section 5.2.1): Orientation reversal S^7_left -> S^7_right changes sign of the Freund-Rubin flux. The right-squashed spectrum is obtained by specific modifications of the E_0 formulas.

**Boundary conditions** (Section 5.2.2): For both N = 1 and N = 0 vacua, there exist multiple choices of boundary conditions that respect the BF bound. In the N = 1 case, some choices also respect supersymmetry.

**Marginal operators** (Section 5.2.3): Key finding for stability:

In the left-squashed (N = 1) vacuum: Boundary conditions can be chosen to eliminate ALL marginal single-trace operators.

In the right-squashed (N = 0) vacuum: After appropriate boundary condition choice, all marginal operators can also be eliminated, supporting perturbative stability against the AdS swampland conjecture.

---

## Key Results

1. **Complete spin-3/2 spectrum**: First derivation of the full spin-3/2 operator eigenvalues on the squashed S^7, completing the operator spectral analysis.

2. **Universal algebraic method**: Novel approach to eigenvalue problems on coset manifolds using group-theoretic Weyl tensor formula, applicable beyond the squashed S^7.

3. **Complete supermultiplet assignment**: All N = 1 supermultiplets identified with definite E_0 values (up to boundary condition choices).

4. **Marginal operator elimination**: Boundary conditions exist that remove ALL marginal single-trace operators in both N = 1 and N = 0 vacua.

5. **Right-squashed (N = 0) spectrum**: Complete spectrum for the non-supersymmetric vacuum, relevant for the AdS swampland conjecture. This is the only known non-supersymmetric AdS flux compactification not yet shown to be unstable.

6. **Eigenvalue degeneracies**: Identification of unexpected degeneracies in the spectrum, with implications for the Higgs/de-Higgs mechanism connecting squashed and round S^7 spectra.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Universal Laplacian | $\Delta = -\square - R_{abcd}\Sigma^{ab}\Sigma^{cd}$ | Eq. (2.9) |
| Coset master equation | $D_a Y+\frac{1}{2}f_{abc}\Sigma^{bc}Y = -T_a Y$ | Eq. (2.15) |
| Riemann from structure constants | $R^{cd}{}_{ab} = f^{cd}{}_i f_{iab}+\frac{1}{2}f^{cd}{}_e f_{eab}+\frac{1}{2}f_{[c|a|e}f_{d]eb}$ | Eq. (2.14) |
| Lichnerowicz operator | $\Delta_L h_{ab} = -\square h_{ab}-2W_{acbd}h^{cd}+14m^2 h_{ab}$ | Eq. (2.8) |
| Dirac on spinors | $(i\not{D})^2\psi = \Delta\psi+\frac{21}{4}m^2\psi$ | Eq. (2.11) |
| Dirac on vector-spinors | $(i\not{D})^2\psi_a = \Delta\psi_a-\frac{3}{4}m^2\psi_a$ | Eq. (2.11) |
| E_0 for spin 2 | $E_0 = \frac{3}{2}+\frac{1}{2}\sqrt{(M/m)^2+9}$ | Table 2 |
| E_0 for spin 0 | $E_0 = \frac{3}{2}\pm\frac{1}{2}\sqrt{(M/m)^2+1}$ | Table 2 |
| Lichnerowicz mass | $M^2(0^+) = \Delta_L-4m^2 = (\Delta_L-3m^2)-m^2$ | Table 3 |
| Supermultiplet content | 1 graviton + 6 gravitino + 6 vector B + 8 vector A + 14 WZ towers | Eqs. (2.1)-(2.5) |
| Bosonic Lagrangian | $2\kappa\mathcal{L} = R-\frac{1}{12}F^2+\frac{8}{12^4}\epsilon^{M_1\ldots M_{11}}A_{M_1 M_2 M_3}F_{M_4\ldots M_7}F_{M_8\ldots M_{11}}$ | Eq. (2.6) |

---

## Relevance to Phonon-Exflation

This paper is **the definitive reference for the complete KK spectrum on squashed S^7**, directly relevant to the framework:

1. **Complete operator spectrum as benchmark**: The framework computes the Dirac spectrum D_K(tau) on SU(3) numerically. The complete analytical spectrum on the squashed S^7 (a closely related space) provides the benchmark: if the framework's numerical methods reproduce the known S^7 results, they can be trusted for the SU(3) case.

2. **Spin-3/2 and gravitino sector**: The novel spin-3/2 spectrum is needed for the framework's analysis of fermionic KK modes. The gravitino multiplets (6 towers) carry the N = 1 supersymmetry information that determines whether the deformation preserves any SUSY.

3. **Lichnerowicz operator and stability**: Table 3 gives Delta_L - 4m^2 as the mass-squared for scalar modes from the Lichnerowicz operator. This is the KK translation of the Lichnerowicz stability analysis from Papers 28-30: a tachyonic Delta_L mode (below the BF bound) would destabilize the compactification.

4. **Marginal operator elimination**: The paper's finding that boundary conditions can eliminate all marginal operators is the S^7 analog of what the framework would need for its SU(3) compactification. If analogous boundary conditions exist on SU(3), the perturbative stability of the Jensen endpoint could be established.

5. **Weak G_2 holonomy structure**: The squashed S^7 has weak G_2 holonomy, which plays a role analogous to the SU(3) structure on the framework's internal space. The G_2 decomposition of the spectrum (into representations of the holonomy group) mirrors the framework's decomposition of D_K eigenvalues into SU(3) representation sectors.

6. **Swampland context**: The paper directly addresses the AdS swampland conjecture for the non-supersymmetric right-squashed S^7. The framework's fold endpoint (if it exists as a non-supersymmetric vacuum) faces the same question: is it stable against all perturbative and non-perturbative decay modes?
