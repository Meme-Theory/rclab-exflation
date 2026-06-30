# Particle Masses from First Principles: A Complete Derivation of the Fermion Spectrum from the Recognition Composition Law

**Author(s):** Jonathan Washburn, Elshad Allahyarov
**Year:** 2025 (v3: 2026)
**Journal:** [INCOMPLETE - not extractable from PDF; preprint]
**arXiv:** 2506.12859
**Relevance:** HIGH

---

## Abstract

We present a first-principles derivation of the masses of all twelve known fermions — three charged leptons, six quarks, and three neutrinos — and the fine-structure constant alpha^{-1}, from a single discrete functional equation, the Recognition Composition Law (RCL), with zero continuously adjustable parameters. The mass spectrum follows from the RCL supplemented by four regularity conditions and eight structural theorems (T1-T8): the golden ratio phi = (1+sqrt(5))/2 emerges as the unique hierarchy base (T6); an 8-step period is fixed by the 3-cube Hamiltonian cycle (T7); three spatial dimensions are selected by a unique combinatorial identity (T8). All integers entering the mass formula are the six combinatorial invariants of the 3-cube Q3; none is fitted. The sole empirical input is the electron mass, which fixes an irreducible unit-conversion constant tau_0.

Predictions are confronted with PDG measurements. Charged-lepton masses are reproduced at sub-ppm accuracy for the muon and ~10^{-4} for the tau (Table 5). All six quark masses are predicted at integer level; first-generation quarks agree to better than 1%, while second/third-generation residuals of 2-16% are expected integer-precision effects (Table 6). Neutrino mass-squared splittings agree with NuFIT 5.3 within 1-2 sigma, normal ordering is predicted, and Sigma m_nu ~ 0.063 eV satisfies cosmological bounds.

All structural claims are machine-verified in Lean 4 (179 files, 0 sorry).

---

## Key Arguments and Derivations

### 1. Recognition Composition Law (RCL) (Section 3)

The master equation is a discrete functional equation (SA0) from which all structure flows. Eight structural theorems (T1-T8) are derived:
- T6: The golden ratio phi = (1+sqrt(5))/2 is the unique hierarchy base
- T7: An 8-step period is fixed by the Hamiltonian cycle on the 3-cube Q3
- T8: D = 3 spatial dimensions selected by a unique combinatorial identity

### 2. Cube Geometry at D = 3 (Section 4)

All integers in the mass formula come from the six combinatorial invariants of the 3-cube Q3: vertices (V=8), edges (E=12), faces (F=6), active edges (E_active = 9), passive edges (E_passive = 3), and the bridge identity E_passive + F = W = 9.

### 3. Master Mass Law (Section 5)

The mass formula has the structure:

m_n = M_sector * phi^{Z(n)} * Delta(n; Z)

where M_sector is a sector mass scale, phi^{Z(n)} provides the hierarchy, and Delta is a gap function. All quantities are derived from cube geometry with zero free parameters (beyond the electron mass as calibration).

### 4. Charged Leptons (Section 9)

- Electron: structural mass from closed form
- Muon: phi-based step from electron, sub-ppm accuracy
- Tau: second step, ~10^{-4} accuracy

### 5. Quarks (Section 10)

Six quark masses predicted. First-generation (u, d) agree to better than 1%. Second/third generation (s, c, b, t) have 2-16% residuals interpreted as integer-precision effects.

### 6. Neutrinos (Section 11)

Mass-squared splittings predicted within 1-2 sigma of NuFIT 5.3. Normal ordering predicted. Sum of neutrino masses ~0.063 eV.

### 7. Fine-Structure Constant

alpha^{-1} derived from the same framework (curvature tuple 103/(102 pi^5) from cube geometry).

### 8. Lean 4 Verification

All structural claims machine-verified in 179 Lean 4 files with 0 sorry statements.

## Key Results

1. All 12 fermion masses and alpha^{-1} derived from a single discrete functional equation with zero free parameters.
2. Golden ratio phi emerges as the unique hierarchy base.
3. All integers from 3-cube combinatorial invariants (V=8, E=12, F=6, etc.).
4. Muon mass reproduced at sub-ppm, tau at ~10^{-4}, quark masses at 1-16%.
5. Neutrino mass splittings within 1-2 sigma; normal ordering; sum ~0.063 eV.
6. Full Lean 4 machine verification of structural claims.
7. Complete 22-component provenance audit: 3 FORCED + 17 DERIVED + 1 calibration + 1 convention.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Master mass law | $m_n = M_{\text{sector}} \cdot \varphi^{Z(n)} \cdot \Delta(n; Z)$ | Eq. (5.5) |
| Hierarchy base | $\varphi = (1 + \sqrt{5})/2$ (golden ratio, uniquely forced by T6) | Theorem T6 |
| Cube invariants | $V=8,\;E=12,\;F=6,\;E_{\text{active}}=9,\;E_{\text{passive}}=3$ | Section 4 |
| Gap function | $\Delta(n; Z) = 1 + \frac{\ln\varphi^Z}{\ln\varphi} = 1 + Z$ [INCOMPLETE - simplified form] | Section 8 |

## Relevance to Phonon-Exflation

This paper represents a radically different approach to the mass hierarchy problem — deriving all fermion masses from combinatorial/algebraic structure of the 3-cube with zero free parameters. The golden ratio as the unique hierarchy base (T6) is a strong structural claim that could either complement or conflict with the framework's spectral action approach. The 8-step periodicity from Q3 Hamiltonian cycles is reminiscent of the framework's BDI classification and 8 Richardson-Gaudin conserved quantities. The Lean 4 verification sets a standard for rigor that any mass prediction — including phi_paasch = 1.531580 — should aspire to match. The claim of zero free parameters is maximally ambitious; the framework should evaluate whether any structural overlap exists between the Q3 invariants and the Dirac spectrum on SU(3).
