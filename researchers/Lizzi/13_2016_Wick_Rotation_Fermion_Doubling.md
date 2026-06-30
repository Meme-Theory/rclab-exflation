# Wick Rotation and Fermion Doubling in Noncommutative Geometry

**Authors:** F. D'Andrea, M.A. Kurkov, Fedele Lizzi
**Year:** 2016
**arXiv:** 1605.03231v2

---

## Abstract

The spectral action formalism requires Wick rotation from Euclidean (computational) spacetime to Lorentzian (physical) spacetime. This rotation is coupled to the fermion doubling problem—NCG naturally introduces mirror fermions. We show how to simultaneously solve both issues: proper Wick rotation eliminates spurious fermionic degrees of freedom, recovering the physical Fock space with the correct fermion count.

---

## Key Arguments

### 1. Fermion Doubling Origins
In NCG, the fermionic Hilbert space has **twice as many fermions** as observed. For each Standard Model fermion:
- Physical particle: e, ν, u, d, ...
- Mirror partner: e', ν', u', d', ...

Total: 192 fermion degrees of freedom (vs. 96 physical).

### 2. Wick Rotation Complexity
Standard Wick rotation: $t_E = it_L$

For **spinors**, this is ambiguous:
- Euclidean spinors: SO(4) representations
- Lorentzian spinors: SO(3,1) representations
- Spinor transformation NOT unique

### 3. Eliminating Doubling via Wick Rotation
D'Andrea-Kurkov-Lizzi show: **Proper Wick rotation automatically projects out mirror fermions**.

The **Euclidean Pfaffian**:
$$\text{Pf}(D_E) = \det(D_E)$$

when Wick-rotated to Lorentzian:
$$\text{Pf}(D_L) = e^{-iS_\text{WZW}} \cdot \text{(physical fermions only)}$$

The Wess-Zumino-Witten (WZW) phase automatically **projects the doubled spectrum** to the physical sector.

### 4. Technical Details
The projection happens at the **Spin structure level**:
- Euclidean: Spin(4) = SU(2) × SU(2) (4 independent spinor components per point)
- Lorentzian: Spin(3,1) = SL(2,ℂ) (2 independent spinor components per point—Weyl fermions)

The Wick rotation $SO(4) \to SO(3,1)$ reduces the representation dimension by half.

### 5. Higgs as Regulator
The Higgs vev plays a crucial role:
- At high energies (above electroweak scale): fermion doubling is present
- At low energies (below vev): Higgs Yukawa coupling breaks the doubling symmetry
- **Result**: Only physical fermions couple to low-energy Higgs

---

## Key Results

1. **Doubling is NOT spurious**: Mirror fermions are necessary for mathematical consistency of Euclidean formulation.

2. **Wick rotation solves it**: Proper analytic continuation to Lorentzian signature eliminates doubling as side effect.

3. **WZW phase essential**: Wess-Zumino-Witten topological phase in path integral enforces correct fermion elimination.

4. **No ad hoc projection needed**: Previous approaches required manually projecting out mirror fermions. D'Andrea-Kurkov-Lizzi show this happens **automatically**.

---

## Connection to Phonon-Exflation

**Framework implication**: If framework uses Euclidean formulation for internal geometry:
- Must implement proper Wick rotation at transition point (van Hove fold)
- WZW phase may provide the mechanism for _acoustic white hole_ causality inversion
- Mirror fermion degrees of freedom might couple to dark sector (speculative)

This paper provides the **mathematical machinery** for Wick rotation in framework computations.
