# CC Path G: Sector-Selective CC Relaxation

**Agent**: Quantum-Acoustics Theorist
**Date**: 2026-04-01
**Sources**: framework-cc-oom.md (Sections I, III Path G), session-63-hawking-quantum-acoustics-workshop.md (QA-E5), session-63-volovik-van-den-dungen-workshop.md (VdD Re:V1, Volovik D1, C1)

---

## 1. The Sector-Selective Structure

### 1.1. Which Modes Control Which Observables

The spectral action on the Jensen-deformed SU(3) fiber determines all low-energy physics through the Seeley-DeWitt (SDW) expansion (CC-3 from framework-cc-oom.md):

    S(tau) = f_0 Lambda^4 a_0 + f_2 Lambda^2 a_2(tau) + f_4 a_4(tau) + O(Lambda^{-2})     (G-1)

Each SDW coefficient is a spectral sum over D_K eigenvalues weighted differently. The physical content of each coefficient is:

| Coefficient | Spectral weight | Physical content |
|:------------|:----------------|:-----------------|
| a_0 = 6440 M_KK^{d-4} | Sum of d_n (multiplicities, tau-independent) | Vacuum energy density, CC |
| a_2 = 2776 M_KK^{d-6} | Sum of d_n lambda_n^{-2} R_n (curvature-weighted) | Einstein-Hilbert action, G_N |
| a_4 = 1351 M_KK^{d-8} | Sum of d_n T(p,q) lambda_n^{-4} (Dynkin-weighted) | Yang-Mills action, gauge couplings |

Source: S42 spectral action computation, canonical_constants.py. These are values at the fold tau = 0.190.

The sector-selective structure arises because these three spectral moments weight the Peter-Weyl sectors differently:

**a_0 (CC sector)**: Receives contribution from ALL sectors proportional to d(p,q)^2 alone. Every eigenvalue of D_K contributes equally (up to multiplicity). The (0,0) singlet contributes with weight d(0,0)^2 = 1^2 = 1. The (1,0) fundamental contributes with weight d(1,0)^2 = 3^2 = 9. Higher representations contribute with d(p,q)^2 growing as (p+1)(q+1)(p+q+2)/2 squared. The (0,0) sector's fractional contribution to a_0 is therefore 1/6440 = 1.6 x 10^{-4}. The CC is dominated by the HIGH-dimensional representations, not the (0,0) singlet.

**a_4 (gauge sector)**: Receives contribution only from sectors with T(p,q) > 0. The (0,0) singlet has T(0,0) = 0 identically: the trivial representation has zero Dynkin index. The gauge sector is completely blind to the (0,0) mode. This is algebraic, not perturbative: T(0,0) = 0 follows from the definition of the Dynkin index as Tr_R(T_a T_b) = T(R) delta_{ab}, and the trivial representation has T_a = 0 for all generators (VdD Re:V1, session-63-volovik-van-den-dungen-workshop.md).

**a_2 (gravity sector)**: Intermediate -- receives contribution from all sectors through curvature integrals, with non-trivial representations dominating through their larger eigenvalues.

### 1.2. The CG(24) Band Structure and Sector Selectivity

The 45-mode phonon spectrum on the CG(24) Cayley graph (PHONON-DISP-FULL-62) decomposes into three sectors:

| Sector | Mode count | Physical content | Coupling hierarchy |
|:-------|:-----------|:-----------------|:-------------------|
| A (geometric) | 36 | Bare PW eigenvalues of D_K | ||V_AB|| = 5.09 M_KK (dominant) |
| B (BCS) | 8 | BCS quasiparticle modes (4 B2 + 1 B1 + 3 B3) | ||V_AC|| = 0.010 M_KK |
| C (Leggett) | 1 | Inter-band coherence oscillation | ||V_BC|| = 1.6 x 10^{-4} M_KK |

Source: s62-phonon-dispersion-full.md.

The 8 BCS modes occupy a specific place in the spectrum. At the fold (tau = 0.190), the eigenvalues of D_K cluster by branch:

| Mode | Eigenvalue (M_KK) | GGE occupation n_k | Degeneracy origin | Isometry C_2 |
|:-----|:-------------------|:-------------------|:------------------|:-------------|
| B2[0] | 0.845 | 0.9885 | (0,0) singlet | 3 (adjoint action) |
| B2[1] | 0.845 | 0.0087 | (0,0) singlet | 3 |
| B2[2] | 0.845 | 0.0008 | (0,0) singlet | 3 |
| B2[3] | 0.845 | 0.0008 | (0,0) singlet | 3 |
| B1[0] | 0.820 | 0.0011 | (0,0) singlet | 0 |
| B3[0] | 0.971 | 1.8 x 10^{-5} | (0,0) singlet | 4/3 (fundamental) |
| B3[1] | 0.971 | 3.6 x 10^{-5} | (0,0) singlet | 4/3 |
| B3[2] | 0.971 | 2.8 x 10^{-5} | (0,0) singlet | 4/3 |

Sources: session-39-final.md (eigenvalues, occupations), W5-10 BLOCKING-GGE-63 (occupations), W6-02 GRAV-BACKREACT-63 (Casimir values).

### 1.3. The Two Casimirs: A Critical Distinction

There is a subtlety in the Casimir assignments that requires precise treatment. The B2 branch is described as "adjoint" with C_2 = 3 in the W6-02 computation, and B2[0] is described as "(0,0) singlet" in VdD's analysis (Re:V1). Both statements are correct; they refer to different things.

**Peter-Weyl sector (coupling to 4D fields)**: All 8 BCS modes reside in the (0,0) Peter-Weyl sector of D_K (confirmed session-62 Einstein-Baptista workshop: "the (0,0) sector has eigenvalues |lambda| in [0.82, 0.97] M_KK -- the B1, B2, B3 modes"). The Peter-Weyl (0,0) selection rule (KZ-NS-62) selects precisely these 16 modes (including multiplicity) as the ones coupling to the 4D zero mode. This is the Casimir relevant for gauge coupling: T(0,0) = 0, so these modes are invisible to a_4.

**Isometry representation (gravitational self-energy)**: The 4-fold degeneracy of B2 arises because the corresponding eigenvalue of D_K is degenerate under the SU(3) isometry group, transforming as the adjoint. The gravitational self-energy correction (F5 from framework-cc-oom.md):

    delta_eps_k = -(1/2) alpha_G eps_k^2 (1 + C_2^{iso}(k)/3)     (G-2)

uses the isometry Casimir C_2^{iso} = 3 (adjoint) for B2, C_2^{iso} = 0 for B1, and C_2^{iso} = 4/3 (fundamental) for B3. This determines how the emergent gravitational field couples to the geometric structure of each mode's wavefunction on SU(3).

**The sector-selective statement (VdD Re:V1)**: The BCS condensate concentrates in B2[0], which sits in the Peter-Weyl (0,0) sector. The gauge sector (a_4) is controlled by sectors with T(p,q) > 0 -- i.e., non-trivial representations. Therefore the condensate is invisible to gauge physics. This is the content of VdD's statement "the condensate lives in the sector of D_K that is invisible to the gauge couplings."

**But for the CC**: The CC is controlled by a_0, which sums over ALL sectors without Dynkin weighting. The a_0 coefficient is tau-independent (Theorem T14, volume-preserving Jensen), so the CC is dominated by the total spectral weight, not by any specific sector. The BCS condensate's modification of the (0,0) sector eigenvalues affects a_0 at the level of E_cond/S_fold = 0.137/250,361 = 5.5 x 10^{-7} (CC-1 from framework-cc-oom.md). This is negligible, but it is the only direct channel through which the condensate touches the CC.

### 1.4. The Phononic Picture of Sector Selectivity

In the phononic language: the CC is the total vibrational zero-point energy of the substrate. Every mode contributes. The gauge couplings are the Dynkin-weighted sum -- only modes carrying gauge charge contribute. Gravity is the curvature-weighted sum -- modes with larger eigenvalues (higher energy vibrations) contribute more.

The BCS condensate creates a Cooper pair in the lowest-energy (0,0) sector modes (B2 flat band). This pair is a phononic bound state in the acoustic band. It modifies the local zero-point energy (affecting a_0) but does not carry gauge charge (T(0,0) = 0, so a_4 is unaffected). The gravity sector (a_2) feels the condensate at two levels: perturbatively through the SDW expansion (delta_a2/a_2 = 1.36 x 10^{-4}, S61) and non-perturbatively through the Sakharov mechanism (delta_a2/a_2 = -0.361, S63 W6-13 BCS-SA-BRIDGE-63).

The sector selectivity thus creates a three-way decoupling:

    CC (a_0) <--(5.5e-7)--> BCS condensate <--(1.4e-4)--> Gravity (a_2) <--(0)--> Gauge (a_4)     (G-3)

The numbers are the fractional couplings at first order. The CC is weakly coupled to the condensate; the condensate is weakly coupled to gravity (perturbatively); the gauge sector is completely decoupled from both the condensate and the CC.

---

## 2. The Phonon Linewidth Hierarchy and Sector-Selective Thermalization

### 2.1. The QA-E5 Hierarchy

In the S63 Hawking-QA workshop (QA-E5), I derived the phonon linewidth hierarchy from structural constraints:

    Gamma_{B3} > Gamma_{B1} > Gamma_{B2}     (G-4)

The physical reasoning:

**B3 (dispersive optical, 3 modes)**: Maximal linewidth. B3 has the broadest bandwidth, largest group velocity, and carries 99.6% of the RPA response (S31Ca). B3 modes scatter freely with other B3 modes (intra-branch, large DOS) and with B2 modes (inter-branch, allowed by Schur). The scattering phase space is large.

**B1 (acoustic singlet, 1 mode)**: Intermediate linewidth. B1 scatters with B2 (allowed) but NOT with B3 (V[B1,B3] = 0 by selection rule, confirmed S58 V_bare). The acoustic character gives Gamma_B1 ~ (omega/omega_D)^{2d-1} for d-dimensional systems, which is moderate at the BCS mode frequencies.

**B2 (flat-band quartet, 4 modes)**: Minimal linewidth. The flat band has zero group velocity (v_g = 0). For flat-band phonons, scattering requires a dispersive partner at the same frequency. The B2-B2 channel has no energy transfer (degenerate). The B2-B3 channel requires crossing the pseudo-gap. The B1-B2 channel is allowed but B1 has only one mode (limited phase space). Prediction: Gamma_B2 is suppressed by the flat-band bottleneck.

This hierarchy is INVERTED relative to the occupation hierarchy: the B2 modes have the HIGHEST GGE occupation (lambda_B2 = 1.459, 93% of pair weight) but the SLOWEST relaxation rate. The B3 modes have the COLDEST occupation (lambda_B3 = 6.007, 0.7% weight) but the FASTEST relaxation rate.

### 2.2. Implications for Sector-Selective CC Relaxation

The linewidth hierarchy has direct consequences for how the CC would relax if integrability were broken.

**If the gravitational channel breaks integrability**: The gravitational self-energy correction (G-2) shifts eigenvalues by mode-dependent amounts proportional to (1 + C_2^{iso}/3). The shift magnitudes are:

| Branch | C_2^{iso} | 1 + C_2/3 | Relative shift |
|:-------|:----------|:-----------|:---------------|
| B2 (adjoint) | 3 | 2 | 2x baseline |
| B1 (singlet) | 0 | 1 | 1x baseline |
| B3 (fundamental) | 4/3 | 1.444 | 1.44x baseline |

So gravitational integrability breaking acts most strongly on B2 (factor 2) and least on B1 (factor 1). Combined with the linewidth hierarchy (G-4), this creates a paradox:

The modes that gravity shifts most (B2) are the modes that thermalize slowest (Gamma_B2 minimal). The modes that thermalize fastest (B3, Gamma_B3 maximal) receive intermediate gravitational shifts (1.44x). The CC, which is controlled by a_0 = sum d_n (all modes equally), would need ALL branches to thermalize for a significant change. The slowest branch (B2) sets the bottleneck.

**The B3-first thermalization scenario**: If B3 thermalizes first (as the linewidth hierarchy predicts), does the CC start relaxing through the B3 channel? The answer is NO at the level required. The B3 branch contributes only 3 of the 8 BCS modes. Even if B3's contribution to a_0 fully relaxed, the fractional change in the CC would be at most:

    delta(a_0)_B3 / a_0 = (3 x delta_eps_B3) / a_0     (G-5)

With delta_eps_B3 ~ alpha_G eps_B3^2 (1 + 4/9) ~ 9.3 x 10^{-4} x (0.971)^2 x 1.444 ~ 1.3 x 10^{-3} M_KK per mode:

    delta(a_0)_B3 / a_0 ~ 3 x 1.3 x 10^{-3} / 6440 = 6 x 10^{-7}     (G-6)

This is 6 x 10^{-7}, or -6.2 OOM. The CC gap is 114 OOM. The B3 channel, even with full thermalization, provides at most 6.2 of the required 114 orders of magnitude. The shortfall is 108 OOM.

### 2.3. The B2 Flat-Band Protection

The B2 flat band creates a phononic analog of a bound state in the continuum (BIC, identified S31Ca). The zero group velocity means B2 modes do not propagate; they are standing waves trapped by the flat dispersion. In condensed matter, flat-band modes are notoriously resistant to thermalization because momentum conservation is trivially satisfied (all momenta degenerate), so thermalization requires energy exchange with dispersive partners. The only available partners are B3 (through V[B2,B3]) and B1 (through V[B2,B1]).

The coupling magnitudes from S58 (V_bare):

| Channel | V_bare element | Status |
|:--------|:--------------|:-------|
| V[B2,B2] | Nonzero (Schur) | Intra-branch, no energy transfer (degenerate) |
| V[B2,B3] | Nonzero | Inter-branch, requires crossing pseudo-gap |
| V[B2,B1] | Nonzero | Inter-branch, allowed but 1-mode phase space |
| V[B1,B1] | 0 (Trap 1, exact) | Forbidden by symmetry |
| V[B1,B3] | 0 (selection rule, exact) | Forbidden by symmetry |

Source: S58 EPSILON-DIRECT-58, V_bare matrix structure.

The B2 thermalization rate is therefore controlled by the inter-branch channels V[B2,B3] and V[B2,B1]. Using the Fermi Golden Rule estimate (valid when the coupling is weak compared to level spacing, which it is for the inter-branch channels):

    Gamma_B2 ~ 2pi |V_{B2,B3}|^2 rho(omega_B2) + 2pi |V_{B2,B1}|^2 rho(omega_B2)     (G-7)

The DOS at the B2 frequency (omega_B2 ~ 0.845 M_KK) is dominated by the B2 flat band itself (the van Hove singularity gives rho ~ infinity formally, but the finite bandwidth W = 0.058 M_KK regularizes it to rho ~ 4/W ~ 69 modes/M_KK). However, for THERMALIZATION (not scattering), what matters is the rate of energy transfer to other branches, not the scattering rate within B2. The inter-branch rate is:

    Gamma_B2^{therm} ~ 2pi |V_{B2,B3}|^2 rho_{B3}(omega_B2)     (G-8)

and rho_{B3} at omega_B2 = 0.845 M_KK is small because the B3 band extends from 0.820 to 0.971 M_KK and the DOS is smooth (not singular) at omega_B2.

The flat-band protection of B2 means that even if gravitational integrability-breaking opens a relaxation channel, the B2 modes thermalize on a timescale set by Gamma_B2^{therm}, which is the SLOWEST rate in the system. The CC, which depends on the total a_0, cannot relax faster than the slowest branch.

---

## 3. The (0,0) Singlet Wall

### 3.1. Why the Condensate Lives in the Decoupled Sector

The BCS condensate concentrates 98.8% of its pair weight in B2[0] (BLOCKING-GGE-63, W5-10), which resides in the (0,0) Peter-Weyl sector of D_K. The (0,0) sector has:

- C_2(0,0) = (0 + 0 + 0 + 0 + 0)/3 = 0 (zero quadratic Casimir)
- T(0,0) = 0 (zero Dynkin index)
- d(0,0) = 1 (trivial multiplicity)

This means the dominant condensate mode is:
1. Invisible to the gauge sector (T = 0, no contribution to a_4).
2. Decoupled from gravitational self-energy shifts that depend on C_2 through the isometry action (but see Section 1.3 -- the isometry Casimir C_2^{iso} = 3 for B2 is nonzero).
3. Minimally weighted in a_0 (d^2 = 1 out of sum d_n^2 = 6440).

### 3.2. Accident or Structure?

The question: is the condensate's concentration in the (0,0) sector an accident of SU(3) representation theory or a structural consequence of the framework's architecture?

**Structural argument (affirmative)**: The condensate forms at the van Hove singularity of the B2 flat band. The flat band is in the (0,0) sector because the lowest eigenvalues of D_K at the fold belong to this sector. The (0,0) sector has the smallest eigenvalues because it is the identity representation -- its Casimir C_2 = 0 provides no additional energy from the gauge connection. Higher representations (1,0), (0,1), (1,1) have C_2 > 0, which lifts their eigenvalues above the (0,0) sector.

More precisely: the eigenvalues of D_K on Jensen-deformed SU(3) scale approximately as |lambda| ~ sqrt(C_2(p,q) + c_0) where c_0 is a constant set by the Jensen parameters. At the fold, the (0,0) modes sit at the bottom of the spectrum:

    |lambda_{(0,0)}| ~ 0.82-0.97 M_KK (BCS modes)
    |lambda_{(1,0)}| ~ 1.1-1.3 M_KK (first excited sector)
    |lambda_{(1,1)}| ~ 1.3-1.8 M_KK (adjoint sector)

Source: session-62 Einstein-Baptista workshop.

The BCS pairing instability occurs where the DOS diverges (van Hove singularity). The DOS diverges at the B2 flat band, which is in the lowest-energy (0,0) sector. The pairing therefore occurs in (0,0) as a STRUCTURAL consequence of three facts:

**(i)** The quadratic Casimir C_2(p,q) = (p^2 + q^2 + pq + 3p + 3q)/3 is minimized at (p,q) = (0,0).

**(ii)** D_K eigenvalues scale with C_2, so the lowest eigenvalues are in the (0,0) sector.

**(iii)** BCS pairing occurs at the van Hove singularity, which is in the lowest-energy sector.

This chain holds for ANY compact simple Lie group G as internal space: C_2(trivial) = 0 is always the minimum, so the lowest D_K eigenvalues are always in the trivial representation, and BCS pairing always concentrates there. The (0,0) singlet wall is UNIVERSAL to the spectral triple construction on compact Lie groups.

### 3.3. What Would Need to Change for (0,0) to Couple

For the (0,0) mode to couple to the gauge sector, one would need T(0,0) > 0. This is algebraically impossible: the trivial representation has T_a = 0 for ALL generators, so Tr(T_a T_b) = 0 identically. There is no deformation, perturbation, or modification of SU(3) that can make the trivial representation carry gauge charge. This is a GROUP-THEORETIC WALL, not a framework-specific one.

For the (0,0) mode to receive direct gravitational self-energy corrections proportional to C_2(0,0), one would need C_2(0,0) > 0. Again, algebraically impossible.

The only channel through which external physics affects the (0,0) condensate mode is INDIRECT: through the BCS gap equation, which couples all sectors via the self-consistency condition (Section 4 below).

### 3.4. The K-Homological Perspective

VdD's analysis (Re:V1) provides the K-theoretic formulation: the single-mode condensate concentrating in (0,0) is the K-HOMOLOGICALLY OPTIMAL configuration. It minimizes the perturbation of non-trivial sectors that carry gauge and gravitational information. The stability bound ||delta_BCS||/gap(D_K) = 0.081 < 1/2 (K-HOMOLOGY-STABILITY-61, Paper 10 Theorem 3.4) is satisfied more easily for single-mode than distributed condensation.

This means the (0,0) wall is not merely algebraic -- it is topologically reinforced. The K-homology class [D_K] is INVARIANT under the BCS ground state formation (because the perturbation is bounded). The sector selectivity is preserved to all orders in the pairing interaction.

---

## 4. Second-Order Indirect Feedback Through the BCS Gap Equation

### 4.1. The Gap Equation

The BCS gap equation in the 8-mode system is (Volovik D1, session-63-volovik-van-den-dungen-workshop.md):

    1/g = sum_{k=1}^{8} 1/(2 E_k)     (G-9)

where:
- g is the pairing coupling constant
- E_k = sqrt(epsilon_k^2 + Delta^2) is the Bogoliubov quasiparticle energy for mode k
- epsilon_k is the single-particle energy of mode k (measured from the chemical potential)
- Delta is the BCS gap (global, not mode-specific)

The gap Delta is determined self-consistently by this equation. It depends on ALL 8 epsilon_k values, not just the (0,0) mode.

### 4.2. The Gravitational Perturbation

The gravitational self-energy correction (G-2) shifts each single-particle energy:

    epsilon_k -> epsilon_k + delta_epsilon_k^{grav}     (G-10)

where:

    delta_epsilon_k^{grav} = -(1/2) alpha_G epsilon_k^2 (1 + C_2^{iso}(k)/3)     (G-11)

For the 8 modes:

| Mode | epsilon_k (M_KK) | C_2^{iso} | delta_epsilon_k (M_KK) | Fractional shift |
|:-----|:-----------------|:----------|:----------------------|:-----------------|
| B2[0-3] | 0.845 | 3 | -6.6 x 10^{-4} | -7.9 x 10^{-4} |
| B1[0] | 0.820 | 0 | -3.1 x 10^{-4} | -3.8 x 10^{-4} |
| B3[0-2] | 0.971 | 4/3 | -6.3 x 10^{-4} | -6.5 x 10^{-4} |

Source: Computed from alpha_G = 9.3 x 10^{-4}, equation (G-11), eigenvalues from session-39 MASS-39.

Note: ALL modes receive a gravitational shift, including B2. The shift is proportional to (1 + C_2^{iso}/3), which is 2 for B2, 1 for B1, and 1.44 for B3. The B2 modes receive the LARGEST shift. This is because C_2^{iso} = 3 (adjoint) is the largest isometry Casimir among the BCS modes, even though C_2(0,0) = 0 in the Peter-Weyl sense.

### 4.3. First-Order Effect: Delta Shift

Substituting the shifted energies into the gap equation:

    1/g = sum_k 1/(2 sqrt((epsilon_k + delta_epsilon_k)^2 + Delta'^2))     (G-12)

Expanding to first order in delta_epsilon_k:

    0 = sum_k (epsilon_k delta_epsilon_k) / (E_k^3)     (G-13)

(The 1/g = const constraint means the perturbation must be absorbed into Delta'.) This gives:

    delta_Delta / Delta = -(1/Delta) * [sum_k (epsilon_k delta_epsilon_k / E_k^3)] / [sum_k (1/E_k^3)]     (G-14)

All 8 modes contribute to this sum. Using the mode energies and Delta = 0.464 M_KK:

For B2 modes: E_B2 = sqrt(0.845^2 + 0.464^2) = sqrt(0.714 + 0.215) = sqrt(0.929) = 0.964 M_KK.

    epsilon_B2 * delta_epsilon_B2 / E_B2^3 = 0.845 * (-6.6e-4) / (0.964)^3 = -5.6e-4 / 0.896 = -6.2e-4     (G-15)

For B1: E_B1 = sqrt(0.820^2 + 0.464^2) = sqrt(0.672 + 0.215) = 0.942 M_KK.

    epsilon_B1 * delta_epsilon_B1 / E_B1^3 = 0.820 * (-3.1e-4) / (0.942)^3 = -2.5e-4 / 0.836 = -3.0e-4     (G-16)

For B3: E_B3 = sqrt(0.971^2 + 0.464^2) = sqrt(0.943 + 0.215) = 1.076 M_KK.

    epsilon_B3 * delta_epsilon_B3 / E_B3^3 = 0.971 * (-6.3e-4) / (1.076)^3 = -6.1e-4 / 1.247 = -4.9e-4     (G-17)

Numerator (sum over all 8 modes):

    N = 4 * (-6.2e-4) + 1 * (-3.0e-4) + 3 * (-4.9e-4) = -24.8e-4 - 3.0e-4 - 14.7e-4 = -42.5e-4     (G-18)

Denominator:

    D = 4 * (1/0.964^3) + 1 * (1/0.942^3) + 3 * (1/1.076^3)
      = 4 * 1.116 + 1 * 1.196 + 3 * 0.802 = 4.464 + 1.196 + 2.406 = 8.066     (G-19)

Therefore:

    delta_Delta / Delta = -(1/0.464) * (-42.5e-4 / 8.066) = +(1/0.464) * 5.27e-4 = +1.14e-3     (G-20)

The gap increases by 0.114% due to gravitational backreaction. This is O(alpha_G), as expected.

### 4.4. Second-Order Effect: v_{B2[0]}^2 Shift

The B2[0] occupation in the BCS ground state is:

    v_{B2[0]}^2 = (1/2)(1 - epsilon_{B2[0]} / E_{B2[0]})     (G-21)

The change in v^2 comes from both the direct epsilon shift AND the gap shift:

    delta(v^2) = (1/2) * d/d(epsilon) [epsilon/E] * delta_epsilon + (1/2) * d/d(Delta) [epsilon/E] * delta_Delta     (G-22)

Computing the derivatives:

    d/d(epsilon) [epsilon/E] = Delta^2 / E^3     (G-23)
    d/d(Delta) [epsilon/E] = -epsilon Delta / E^3     (G-24)

For B2[0] (epsilon = 0.845, Delta = 0.464, E = 0.964):

    delta(v^2)_direct = -(1/2) * (0.464^2 / 0.964^3) * 6.6e-4
                      = -(1/2) * (0.215 / 0.896) * 6.6e-4
                      = -(1/2) * 0.240 * 6.6e-4 = -7.9e-5     (G-25)

    delta(v^2)_indirect = (1/2) * (0.845 * 0.464 / 0.964^3) * delta_Delta
                        = (1/2) * (0.392 / 0.896) * 1.14e-3 * 0.464
                        = (1/2) * 0.437 * 5.3e-4 = 1.2e-4     (G-26)

    delta(v^2)_total = -7.9e-5 + 1.2e-4 = +4.1e-5     (G-27)

The net shift of the B2[0] occupation is delta(v^2) = +4.1 x 10^{-5}. This is the combined effect of:
1. The direct gravitational shift of epsilon_B2 (lowering v^2 by 7.9 x 10^{-5}).
2. The indirect gap equation feedback from ALL modes (raising v^2 by 1.2 x 10^{-4}).

The indirect effect is 1.5x larger than the direct effect and has the OPPOSITE sign. The gap equation feedback dominates.

### 4.5. Scaling of the Indirect Feedback

The indirect feedback to v_{B2[0]}^2 is O(alpha_G) -- not O(alpha_G^2) as stated in the framework-cc-oom.md Path G description.

Let me be precise about the order counting. The gravitational correction delta_epsilon_k is O(alpha_G). The gap shift delta_Delta is O(alpha_G) (from equation G-20). The occupation shift delta(v^2) is also O(alpha_G), because both the direct and indirect contributions are O(alpha_G).

Where does the alpha_G^2 claim come from? Volovik's D1 and VdD's concession C1 (session-63-volovik-van-den-dungen-workshop.md) identify O(alpha_G^2) for the "indirect feedback to (0,0)." But this appears to conflate two different questions:

**(a) Feedback to the (0,0) eigenvalue**: The Peter-Weyl (0,0) eigenvalue is not directly shifted by terms proportional to C_2(0,0) = 0 in the PETER-WEYL sense. But it IS shifted by the isometry C_2^{iso} = 3 term. The confusion arises from the two-Casimir structure.

**(b) Feedback to v_{B2[0]}^2 through the gap equation**: This is O(alpha_G), not O(alpha_G^2), as my derivation (G-25 through G-27) shows. The gap equation is a FIRST-ORDER feedback mechanism: the gravitational shift to epsilon_k enters the gap equation at O(alpha_G), and the resulting delta_Delta feeds back to v^2 at O(alpha_G).

**Resolution**: The O(alpha_G^2) statement in the framework document applies to the scenario where the B2[0] mode has C_2 = 0 (Peter-Weyl Casimir) AND the gravitational correction only enters through C_2. In that scenario, the direct shift to B2[0] is zero (C_2(0,0) = 0), and the indirect feedback through the gap equation is O(alpha_G) x O(alpha_G) = O(alpha_G^2) because:
- First order: gravity shifts B3 by O(alpha_G).
- Second order: shifted B3 energies modify Delta by O(alpha_G), which modifies v_{B2[0]}^2 by O(alpha_G).

BUT this scenario applies only if C_2^{iso}(B2) is also zero, which it is not. The isometry Casimir C_2^{iso} = 3 gives B2 modes a DIRECT gravitational shift proportional to alpha_G (1 + 3/3) = 2 alpha_G. The direct channel is O(alpha_G), not O(alpha_G^2).

**Corrected scaling**: The gravitational feedback to v_{B2[0]}^2 is O(alpha_G) ~ 10^{-3}, not O(alpha_G^2) ~ 10^{-6}. The 108-OOM shortfall identified in Path G of framework-cc-oom.md becomes a 111-OOM shortfall (114 - 3 = 111). The qualitative conclusion is unchanged -- the shortfall is enormous -- but the quantitative estimate must be corrected.

### 4.6. The 3He-B Comparison

Volovik's answer to VdD's D3-Q1 (session-63-volovik-van-den-dungen-workshop.md, lines 776-788) provides the 3He-B analog. In 3He-B:

- The spin-orbit (dipolar) interaction has Omega_B/Delta ~ 10^{-3}.
- The dominant pairing channel (J=0, Delta_0) is NOT directly coupled to the dipolar interaction because it transforms as J=2.
- The direct matrix element <J=0|H_dip|J=0> = 0 by angular momentum selection rules.
- The indirect feedback through the gap equation is at order (Omega_B/Delta)^4 ~ 10^{-12} (fourth order because angular momentum selection rules impose two additional powers).

In the framework:

- The gravitational correction has alpha_G ~ 10^{-3}.
- The B2[0] condensate mode IS directly shifted (C_2^{iso} = 3, so delta_epsilon is nonzero).
- There is no angular momentum selection rule to suppress the feedback further.
- The indirect feedback through the gap equation is at O(alpha_G) ~ 10^{-3} (first order).

The framework's cross-sector coupling is STRONGER than 3He-B by a factor of (10^{-3})/(10^{-12}) = 10^9. This is because 3He-B has angular momentum selection rules (J=2 dipolar acting on J=0 gap) that the discrete 8-mode system lacks (as Volovik noted in D1 and VdD conceded in C1).

---

## 5. SECTOR-SELECTIVE-BREAKING-64: Computation Design

### 5.1. Objective

Compute the full gravitational feedback chain from EIH self-energy corrections through the BCS gap equation to the modification of the GGE occupations and hence to the shift in E_ZP (the zero-point energy controlling the CC).

### 5.2. Inputs

From canonical_constants.py and existing computations:
- 8 BCS mode energies: epsilon_k(tau_fold) from S39 MASS-39
- Isometry Casimirs: C_2^{iso} = {3, 3, 3, 3, 0, 4/3, 4/3, 4/3} from W6-02
- alpha_G = 9.3 x 10^{-4} (from M_KK/M_Pl)
- Delta = 0.464 M_KK (BCS gap from S37)
- GGE occupations: {n_k} from S39 GGE-39
- GGE Lagrange multipliers: {lambda_k} from S39

### 5.3. Computation Steps

**Step 1**: Compute gravitational eigenvalue shifts delta_epsilon_k from equation (G-11) for all 8 modes.

**Step 2**: Solve the perturbed BCS gap equation (G-12) self-consistently for Delta' = Delta + delta_Delta. Use Newton's method with the original solution as initial guess. This gives the first-order gap shift.

**Step 3**: Compute the shifted Bogoliubov occupations v_k'^2 = (1/2)(1 - epsilon_k'/E_k') for all 8 modes with the shifted energies and gap.

**Step 4**: Compute the shifted zero-point energy:

    E_ZP' = sum_k d_k E_k'     (G-28)

and the CC shift:

    delta_Lambda = E_ZP' - E_ZP     (G-29)
    delta_Lambda / Lambda_CC = (E_ZP' - E_ZP) / 0.838     (G-30)

**Step 5**: Compute the second-order correction by iterating: use the shifted eigenvalues to recompute the gravitational self-energy (the bootstrap loop), then re-solve the gap equation. Track convergence.

**Step 6**: Compute the R-G conserved charge decomposition. The 8 Gaudin charges R_k = s_k^z + g sum_{l!=k} (s_k . s_l)/(eps_k - eps_l) have specific overlap with the zero-point energy operator:

    O_k = Tr(R_k * H_ZP) / (Tr(R_k^2) * Tr(H_ZP^2))^{1/2}     (G-31)

This overlap determines WHICH R-G charges must be broken for the CC to relax. If the charge with the largest overlap with H_ZP is the charge most strongly broken by gravity, the CC path is structurally aligned. If the overlap is concentrated on charges that gravity preserves, the path is structurally misaligned.

### 5.4. Pre-Registered Gate

**Gate**: SECTOR-SELECTIVE-BREAKING-64

**Criterion**: Compute delta_Lambda/Lambda_CC (equation G-30) from the full gravitational feedback chain.

**PASS**: |delta_Lambda/Lambda_CC| > 10^{-6} (the gravitational channel modifies the CC by more than the naive O(alpha_G^2) estimate, indicating the two-Casimir enhancement from Section 4.5 is real and the indirect feedback is stronger than previously estimated).

**FAIL**: |delta_Lambda/Lambda_CC| < 10^{-8} (the gravitational channel is doubly suppressed as originally estimated, and the sector-selective obstruction holds at the quantitative level).

**INFO**: 10^{-8} < |delta_Lambda/Lambda_CC| < 10^{-6} (intermediate regime: gravitational feedback is nonzero but insufficient on its own; requires iteration or non-perturbative treatment).

**Auxiliary diagnostic**: The R-G charge overlap vector {O_k}. If max_k O_k < 0.1 for ALL charges broken by gravity, the CC is structurally decoupled from the integrability-breaking mechanism regardless of the breaking strength. This would be a structural FAIL independent of the quantitative threshold.

### 5.5. Expected Outcome

From the analysis in Section 4, the expected result is:

    delta_Lambda ~ alpha_G * sum_k (d epsilon_k / d alpha_G) * (d E_k / d epsilon_k)     (G-32)

which is O(alpha_G) in the eigenvalue shifts but enters E_ZP linearly. The fractional change delta_Lambda/Lambda_CC ~ delta_E_ZP/E_ZP ~ alpha_G ~ 10^{-3}, so:

    delta_Lambda/Lambda_CC ~ 10^{-3}     (G-33)

This would PASS the gate but still leave a 111-OOM shortfall to the observed CC. The gate tests whether the gravitational channel is structurally open, not whether it resolves the CC on its own.

---

## 6. Assessment: Structural Obstacle or Perturbative Artifact?

### 6.1. The Three Layers of the Sector-Selective Wall

The sector-selective structure operates at three distinct levels:

**Layer 1 (Algebraic, PERMANENT)**: T(0,0) = 0. The trivial representation carries zero gauge charge. No perturbation, deformation, or non-perturbative effect can change this. The gauge sector is PERMANENTLY blind to the (0,0) condensate mode. This wall is group-theoretic and survives in any spectral triple on any compact Lie group.

**Layer 2 (Spectral, CONTINGENT)**: C_2(0,0) = 0 in the Peter-Weyl sense, but C_2^{iso} = 3 in the isometry sense. The gravitational self-energy uses the isometry Casimir, which is nonzero for B2. This means the gravitational channel DOES affect B2 directly, at O(alpha_G). The "wall" at this layer is weaker than initially claimed: it is O(alpha_G) rather than O(alpha_G^2). The Layer 2 obstruction is quantitative, not structural.

**Layer 3 (Dynamical, OPEN)**: The phonon linewidth hierarchy (G-4) means B2 thermalizes last. Even if gravity breaks integrability and opens a relaxation channel, the flat-band modes that dominate the condensate (and hence a_0) are the slowest to relax. The dynamical obstruction compounds the algebraic one: not only does gravity act weakly on the CC sector, but the CC sector is also dynamically frozen by flat-band protection.

### 6.2. Is It a Perturbative Artifact?

No. The sector selectivity is not a perturbative artifact. Here is why.

**The gauge-sector decoupling (T(0,0) = 0)** is an exact algebraic identity. It holds non-perturbatively, to all orders, at any coupling strength. No resummation can generate a nonzero Dynkin index for the trivial representation.

**The gravitational-sector coupling (C_2^{iso} = 3 for B2)** IS nonzero and operates at O(alpha_G). The framework-cc-oom.md claim that the feedback is O(alpha_G^2) conflates the two Casimirs. The corrected estimate is O(alpha_G) ~ 10^{-3}, still 111 OOM short.

**The flat-band protection** is a topological property of the B2 dispersion, not a perturbative approximation. The flat band's zero group velocity is protected by the symmetry structure that enforces the 4-fold degeneracy (Schur's lemma on the irreducible (1,1) subspace, LIED-39 S39). Perturbative corrections to the bandwidth are bounded by V_rem/W ~ 14% (S40), which cannot lift the flat band into a dispersive regime.

### 6.3. The Fundamental Obstacle

The sector-selective structure is a GENUINE structural feature of the spectral triple, not a perturbative artifact. It is the phononic expression of the same wall identified from three other directions:

1. **CC = integrability** (S56): The Richardson-Gaudin conserved charges prevent the GGE occupations from rearranging. The sector selectivity makes the rearrangement even harder by protecting the dominant mode.

2. **CC = phonon lifetime** (S57): Infinite phonon lifetime means zero energy redistribution. The flat-band protection of B2 ensures the longest-lived modes are precisely the ones controlling the CC.

3. **CC = finite-size effect** (S63 VdD-Volovik workshop): At N_pair = 1, the equilibrium theorem does not apply. The sector selectivity means that even with gravitational integrability breaking, the condensate mode is the last to thermalize.

All three statements are different projections of the same object: the ordered veil of the GGE relic, expressed in the phononic band structure of the CG(24) lattice, protects the CC from relaxation through any channel that does not modify the (0,0) sector's spectral weight directly and non-perturbatively.

### 6.4. What Would Resolve the CC Through This Path

For Path G to resolve the CC, one would need:

1. A mechanism that modifies a_0 by a factor of 10^{-114}. Since a_0 = sum d_n (multiplicities), this requires either (a) reducing the total mode count by 114 OOM (impossible for a finite spectrum) or (b) introducing a cancellation between contributions from different sectors that reduces the effective a_0.

2. Alternatively: a mechanism that makes the vacuum energy density independent of a_0. The Jacobson route (Path A) does this by treating Lambda as an integration constant unrelated to the spectral action. The transit-as-relaxation route (Path C) does this by allowing the curvature-dependent part rho_curv(tau) to decay, but faces the a_0 floor obstruction.

3. The sector-selective structure suggests a third possibility: if the CC is really controlled by a SECTOR-RESTRICTED a_0 -- i.e., if the gravitating vacuum energy is the spectral weight of only those modes that couple to the emergent metric -- then the (0,0) sector's contribution to the CC would be:

    rho_vac^{(0,0)} = (d(0,0)^2 / a_0) * rho_vac = (1/6440) * rho_vac     (G-34)

This reduces the CC by a factor of 6440, or 3.8 OOM. Useful but insufficient (114 - 3.8 = 110.2 OOM remain). And the sector-restricted trace lacks mathematical implementation within the standard spectral action principle (VdD Dissent Gap 3, Section IV.2 of framework-cc-oom.md).

### 6.5. Bottom Line

Sector selectivity is a permanent structural feature, not a perturbative artifact. It compounds the CC problem by adding flat-band protection and gauge decoupling to the existing integrability obstruction. The gravitational feedback to the (0,0) condensate mode is O(alpha_G) ~ 10^{-3} (corrected from the previously stated O(alpha_G^2) ~ 10^{-6}), yielding a 111-OOM shortfall rather than 108 OOM. The SECTOR-SELECTIVE-BREAKING-64 computation will quantify the full feedback chain and test whether the R-G charges conjugate to the CC are structurally aligned with the gravitational breaking mechanism.

The sector-selective wall does not close Path G outright. It constrains the path to require either (a) non-perturbative gravitational backreaction that accumulates over cosmological timescales (but Gamma_break/H_0 ~ 10^{56} means the breaking is instantaneous, so time does not help), or (b) a fundamentally different relationship between the spectral action and the gravitating vacuum energy (Jacobson, sector-restricted traces, or self-consistent BdG spectral triple). The path remains OPEN but with a 111-OOM shortfall that no known perturbative mechanism can bridge.

---

## Summary Table

| Section | Key Result | Structural Status |
|:--------|:-----------|:-----------------|
| 1. Sector-selective structure | CC controlled by a_0 (all modes), gauge by a_4 (T>0 modes only), gravity by a_2 (curvature-weighted) | PERMANENT (algebraic) |
| 2. Linewidth hierarchy | Gamma_B3 > Gamma_B1 > Gamma_B2. B2 thermalizes LAST. CC bottleneck = flat-band protection | Predicted (pre-registered LINEWIDTH-HIERARCHY-64) |
| 3. (0,0) singlet wall | T(0,0)=0 (gauge), C_2(0,0)=0 (Peter-Weyl), C_2^{iso}=3 (isometry). Two-Casimir structure | PERMANENT (group-theoretic) |
| 4. BCS gap equation feedback | delta(v_{B2[0]}^2) = +4.1e-5 at O(alpha_G), NOT O(alpha_G^2). Corrected from framework-cc-oom.md | To be verified (SECTOR-SELECTIVE-BREAKING-64) |
| 5. SECTOR-SELECTIVE-BREAKING-64 | PASS: |delta_Lambda/Lambda_CC| > 10^{-6}. Expected: ~10^{-3}. 111 OOM shortfall | PENDING |
| 6. Assessment | Structural obstacle, not perturbative artifact. 111 OOM gap. Path OPEN but quantitatively insufficient alone | Structural conclusion |
