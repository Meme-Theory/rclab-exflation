---
ARCHIVED: 2026-05-10
Last meaningful session: S41 (Fabric Discovery; superseded mid-S86)
Superseded by: sessions/framework/Phononic-Substrate-Geometry.md
Reason: Phononic-Crystal-Geometry framing replaced by Phononic-Substrate-Geometry framing post-S86 (substrate IS the spectral triple, not a crystal IN a container); per phononic-framing.md IS-not-IN substrate-direction discipline
---

# Phononic Crystal Geometry of SU(3)

**Original**: Session 47 (2026-03-16)
**Revised**: 2026-03-21 (post-Session 53 -- tight-binding reframe)
**Sources**: S47 crystal geometry + Landau/Nazarewicz/Volovik collabs + S53 results
**Author**: Tesla-Resonance (synthesis)

---

## 1. The Crystal Picture

SU(3) is an 8-dimensional compact Lie group of rank 2. The phonon-exflation framework equips it with a one-parameter family of left-invariant metrics -- the Jensen deformation -- parametrized by tau, and places a Dirac operator on it whose spectrum encodes the particle content of the theory. The framework thesis: particles are phononic excitations of this internal geometry. The Jensen deformation is the clock. The spectrum is the physics.

### The Jensen Metric

The Lie algebra decomposes as su(3) = u(1) + su(2) + C^2, with dimensions 1 + 3 + 4 = 8. The Jensen metric scales these blocks independently:

    L_1 = e^{2*tau}    (u(1), 1 direction -- hypercharge)
    L_2 = e^{-2*tau}   (su(2), 3 directions -- isospin)
    L_3 = e^{tau}       (C^2 coset, 4 directions -- SU(3)/U(2))

Volume: L_1 * L_2^3 * L_3^4 = e^{2*tau - 6*tau + 4*tau} = e^0 = 1.

This is exact at every tau. The internal manifold does not shrink or expand. It changes shape. Verified to machine epsilon across all computed tau values (S12, confirmed S53 P6). The exflationary thesis made geometric: a 4D observer experiences expansion not because the internal space contracts (as in standard KK), but because the spectral content of the Dirac operator shifts under the shape change.

At the fold tau = 0.19:

| Block | Scale | Value | Physical role |
|:------|:------|:------|:--------------|
| u(1)  | e^{0.38} | 1.462 | Hypercharge direction, stretched |
| su(2) | e^{-0.38} | 0.684 | Isospin directions, compressed |
| C^2   | e^{0.19} | 1.209 | Coset directions, moderately expanded |

Scalar curvature at fold: R = 2.018 (1% above bi-invariant R = 2.000). Dirac spectrum: 992 eigenvalues at max_pq_sum = 3, range [0.820, 2.061].

### The 32-Cell Tessellation

The BCS condensate, computed via Kibble-Zurek domain formation (S42), partitions SU(3) into 32 Voronoi cells. This number is structural: it derives from the Weyl group order |W(SU(3))| = 6, the Z_3 center, and the tessellation of the maximal torus. Each cell is a copy of the fundamental Weyl alcove, related to its neighbors by Weyl reflections and center translations.

The cells are the "atoms" of the crystal. Cooper pairs hop between cells via Josephson couplings. The inter-cell couplings are matrix elements of the Kosmann derivative between neighboring cells:

| Coupling | Direction | Value (M_KK) | Bonds per cell |
|:---------|:----------|:-------------|:---------------|
| J_C2     | C^2 coset | 0.933 | 4 (dominant) |
| J_su2    | su(2)     | 0.059 | 3 |
| J_u1     | u(1)      | 0.029 | 1 |

These are geometric quantities -- overlap integrals of Dirac eigenstates between adjacent cells. They are valid at any pair number. The 32:1 ratio between J_C2 and J_u1 reflects the curvature hierarchy: the softest geometric directions (C^2 coset, where curvature is lowest) carry the strongest inter-cell coupling.

---

## 2. The Pair as Quantum Walker

Session 53 established the defining result: N_pair = 1 exactly. The non-singlet pairing amplitudes M_max = 0.060-0.095, all far below the BCS threshold of 1. Only the (0,0) Peter-Weyl singlet pairs. The bracket [1, 59] from S52 collapsed to a single number.

This changes everything about what the "crystal" means physically.

### GL Invalid, Tight-Binding Valid

Three independent criteria show Ginzburg-Landau theory does not apply:

| Criterion | Value | Threshold | Verdict |
|:----------|:------|:----------|:--------|
| Ginzburg number Gi | 0.506 | << 1 for GL | FAIL |
| E_J / E_C | 0.818 | >> 1 for phase coherence | FAIL (Mott side) |
| L / xi_GL | 0.031 | >> 1 for bulk limit | FAIL (0D limit) |

E_J/E_C = 0.818 < 1 places the system in the charge-quantized regime. Cooper pair number (n = 0 or 1) is well-defined; phase is maximally uncertain (delta_phi = 2*pi). If this were a Josephson junction array, it would be a Mott insulator, not a superfluid. The critical ratio for phase coherence is E_J/E_C ~ z = 16 for an 8D lattice with coordination number z = 16. The system is 20x below threshold.

### Reinterpretation of GL Branches

The S52 Ginzburg-Landau 6-branch dispersion survives the N_pair = 1 reframe but changes identity. The branches are tight-binding bands for single-pair hopping on the 32-cell lattice:

| Branch | omega(K=0) (M_KK) | Bandwidth (M_KK) | t_eff = BW/4 | Identity |
|:-------|:-------------------|:------------------|:-------------|:---------|
| Goldstone | 0.000 | 0.507 | 0.127 | Pair center-of-mass kinetic energy |
| Leggett-1 | 0.138 | 0.392 | 0.098 | Inter-sector Rabi oscillation (B2-B3) |
| Leggett-2 | 0.192 | 0.325 | 0.081 | Inter-sector Rabi oscillation (B2-B1) |
| Higgs-1   | 0.378 | 0.004 | 0.001 | Pair binding amplitude oscillation |
| Higgs-2   | 1.456 | 0.052 | 0.013 | Pair binding amplitude oscillation |
| Higgs-3   | 10.37 | 2.60  | 0.650 | Breathing mode |

The "Goldstone mode" is not a Nambu-Goldstone boson of a broken U(1)_7. There is no spontaneous symmetry breaking at N_pair = 1 (definite particle number, indefinite phase). It is the pair's translational kinetic energy on the lattice -- the dispersion of a quantum walker.

### Infinite Lifetime

Gamma/omega = 0 exactly for all 6 branches (S53 W3-1, PERMANENT). A single particle on a periodic lattice with no disorder and no interactions propagates ballistically. The Bloch states |K> are exact energy eigenstates. Four scattering channels that could in principle create damping all vanish identically:

1. Pair-pair scattering: zero (N_pair = 1, no second pair).
2. Impurity scattering: zero (perfect crystal, no disorder).
3. Umklapp scattering: zero (single-band occupation at N = 1).
4. Phonon emission: zero (no thermal bath in the internal space).

The Cooper pair is a coherent quantum walker with infinite mean free path on the 32-cell lattice.

---

## 3. The Sound Speed Hierarchy

Two sound speeds define the acoustic structure of the crystal:

| Speed | Value (M_KK) | Physical origin |
|:------|:-------------|:---------------|
| c_fabric | 209.97 | Substrate phase stiffness (spectral action gradient dS/dtau) |
| c_Gold | 0.915 | Single-pair hopping speed (Goldstone band group velocity) |

The ratio c_fabric / c_Gold = 229.5.

### Origin of c_fabric

c_fabric^2 = (d^2 S / dtau^2) / rho, where S is the spectral action and rho is the effective mass density. This is the speed at which perturbations of the deformation parameter tau propagate through the M^4 x SU(3) substrate. It is analogous to the longitudinal sound speed in a crystal lattice -- set by the elastic modulus (d^2S/dtau^2) divided by the inertia (rho). Computed in S42 from the spectral action gradient.

### Origin of c_Gold

c_Gold = sqrt(2 * J_C2 / T_phase) = 0.915, where J_C2 = 0.933 is the dominant Josephson coupling (C^2 coset direction) and T_phase is the phase inertia per cell. This is the pair hopping speed -- how fast the Cooper pair traverses the lattice. In tight-binding language, c_Gold = d*omega/dK at K = 0, where omega(K) = 2J(1 - cos Ka) is the Goldstone band dispersion. In a conventional crystal, this would be the acoustic phonon velocity.

### The 229x Ratio

This hierarchy is the central acoustic fact of the framework. The substrate vibrates 229 times faster than the pair hops. In condensed matter: the Debye frequency of the lattice vastly exceeds the pair hopping rate. In cosmology: this ratio drives the acoustic e-fold count that replaces inflation.

The 229x ratio is NOT topologically protected (S53 W3-14, BDI-W-PHONON-53). The BDI classification protects the single-particle gap and the condensate stability, not the sound speeds. c_Gold varies continuously with tau (0.21% across [0, 0.35]) without closing any topological gap. This is consistent with 3He-B, where sound speeds vary with temperature and pressure without topological protection.

---

## 4. The Band Structure

### Six Branches: Symmetry Origin

The 6 branches arise from the 3 spinor sectors (B1, B2, B3) times 2 (amplitude and phase). The GL stiffness matrix is block-diagonal: amplitude and phase decouple by U(1) symmetry. Each 3x3 block has 3 eigenvalues, giving 6 total branches. This block structure is exact (not approximate) and holds at every K in the Brillouin zone.

The sectors and their geometric homes:

| Sector | Spinor type | Dim (0,0) | Pairing V(s,s) | Fraction of pairing |
|:-------|:-----------|:----------|:---------------|:-------------------|
| B1 | U(2) singlet | 2 | 0.000 (exact, Trap 1) | 0.0% |
| B2 | U(2) fundamental | 8 | 0.256 | 90.7% |
| B3 | SU(2) adjoint | 6 | 0.003 | 1.0% |

The B2 funnel: 50% of modes, 62% of pi-phase topology, 91% of BCS pairing weight. Each filter stage concentrates further. Landau identifies this as standard multi-band BCS physics -- the analog of sigma-band dominance in MgB2, where ~75% of electron count carries ~95% of gap weight. The coupling anisotropy ratio V_B2/V_B3 = 85 drives the concentration through BCS exponential sensitivity.

### Double Triviality (S53 W3-15)

All Berry phases and Zak phases vanish for all 6 bands. The band topology is trivial by two independent mechanisms:

1. **Block-diagonality**: The 6-band system decomposes into two independent 3-band systems (amplitude and phase). Cross-block matrix elements vanish exactly. The S52 "anti-crossings" are all exact crossings (V_cross = 0 by the block-diagonal theorem, S22b).

2. **Reality**: Within each 3x3 block, the matrices V and T are real symmetric positive definite. All eigenvectors are real. Berry connection Im(A_n(K)) = 0 identically at every K. Eigenvector character is locked across the entire Brillouin zone -- sector labels B1, B2, B3 never exchange.

There is no topological obstruction, no band inversion, no edge state. The crystal is an acoustic insulator with trivial topology in every sense.

---

## 5. The Mott Regime

E_J/E_C = 0.818 < 1. This is the defining diagnostic.

In a Josephson junction array, E_J/E_C < 1 means the system favors definite charge (pair number) over definite phase. The charge uncertainty delta_n ~ 0 while the phase uncertainty delta_phi ~ 2*pi. This is the Mott insulator side of the superfluid-insulator quantum phase transition.

### What This Means for the Framework

No spontaneous symmetry breaking of U(1)_7. There is no macroscopic condensate, no order parameter with a well-defined phase, no Nambu-Goldstone boson in the traditional sense. The "Goldstone mode" is kinetic energy of a localized pair, not a phase-mode of a broken symmetry.

The Ginzburg criterion Gi = 0.506 confirms this independently: fluctuations are the same size as the mean field. Mean-field BCS gives Delta = 0 at all tau (S53 P11). The canonical gap Delta = 0.77 M_KK is a beyond-mean-field effect -- it emerges from exact diagonalization of the 256-state Fock space, from the instanton gas (S37-38), and from the giant pair vibration (GPV). The gap is real but its origin is non-perturbative.

Nazarewicz's nuclear analog is precise: this is the ultrasmall-grain limit (Anderson 1959), where the single-particle level spacing exceeds the BCS gap and mean-field BCS breaks down. The nuclear benchmark: sd-shell nuclei with N_pair = 1-2, where variation-after-projection (PBCS) is required and BCS overestimates gaps by 60% (S46, PBCS/BCS = 0.63-0.64).

### What Survives

The Josephson couplings J_C2, J_su2, J_u1 are geometric overlap integrals, valid at any N_pair. The 6-branch topology (3 sectors x 2) is a symmetry property. The dispersion relations persist as tight-binding bands. The BCS pairing matrix V(s,s') is algebraic (Kosmann derivative). The protected chain q_7^2 = K(u(1), C^2) = 1/16 is representation theory, independent of condensate physics. The crystal geometry is permanent. Only its interpretation as a superfluid is revoked.

---

## 6. Acoustic Cosmology on the Crystal

### The BLV Acoustic Metric

The Barcelo-Liberati-Visser (BLV) acoustic metric for phonons propagating through a condensate with density rho and sound speed c_s, on a geometric FRW background with scale factor a_geom, is (S53 W0-1, PERMANENT):

    g_00 = -rho * c_s
    g_ij = (rho / c_s) * a_geom^2 * delta_ij

This defines an acoustic scale factor:

    a_acoustic = a_geom * sqrt(rho / c_s)

And acoustic e-folds:

    N_e^acoustic = N_e^geom + (1/2)*ln(rho_f/rho_i) - (1/2)*ln(c_sf/c_si)

This formula is exact. Verified numerically to 4.4e-15 relative error. There is no single conformal exponent alpha relating H_acoustic to H_geom -- the question "H_acoustic = H_geom * c_s^alpha" is ill-posed. The acoustic metric introduces an independent geometry.

### The 2.92 E-Folds

| Contribution | Source | N_e |
|:-------------|:-------|:----|
| Geometric | KK volume-preserving (EFOLD-MAPPING-52) | 0.1734 |
| Sound speed | c_fabric -> c_Gold (229x) | 2.7179 |
| **Total (without rho)** | | **2.8913** |

The sound speed contribution dominates by 15.7x over the geometric ceiling. The 229x hierarchy converts to 2.72 acoustic e-folds through (1/2)*ln(229.48). The geometric contribution (0.17 from the volume-preserving Jensen deformation) is a small correction.

The total 2.89 falls 0.21 short of the 3.1 threshold. S53 identified five missing factors at the ~7% level (8D BLV exponent, 32-cell coherent contribution, LK overshoot duration, rho evolution, Floquet amplification). Whether the inflationary threshold is the correct criterion for exflation is an open question -- the session reframed it as potentially inapplicable.

### Jensen Volume Preservation

The expansion is 100% acoustic. The internal volume does not change:

    det(g_tau) = L_1 * L_2^3 * L_3^4 = 1 (exact, all tau)

There is no KK volume transfer. What a 4D observer measures as "expansion" is the change in the acoustic metric -- the phonon experiences a changing effective geometry as the sound speed drops from c_fabric to c_Gold during the transit through the fold. This is exflation: expansion from internal shape change, not from volume loss.

### The Speed Bump

At tau = 0.2015, the BCS condensation energy gradient dE_cond/dtau exceeds the KK potential gradient dV_KK/dtau by 30% (S53 W3-7, PERMANENT). The van Hove singularity at the fold amplifies the energy derivative by 400x relative to the value ratio. The result: d^2V_eff/dtau^2 < 0. Both contributions are concave.

This creates a speed bump, not a trap. The modulus decelerates near the fold, then accelerates past. There is no stable minimum -- static stabilization is CLOSED (S53 W3-7). The fold is a transient, not an equilibrium. The physics IS the transit.

---

## 7. The Body Plan: Curvature Anatomy

The 28 independent sectional curvatures K(e_a, e_b) of the Jensen-deformed metric organize into 6 branches:

| Branch | Deg | K(fold) | K(tau=0) | Flow | Physical identity |
|:-------|:----|:--------|:---------|:-----|:-----------------|
| Flat | 3 | 0.0000 (exact) | 0.0000 | Fixed | u(1)-su(2) planes |
| Soft | 12 | 0.00974 | 0.02083 | Softening (0.47x) | su(2)-C^2 cross-planes |
| Mid-low | 4 | 0.03968 | 0.02083 | Hardening (1.90x) | C^2-C^2 cross-doublet |
| Mid-high | 2 | 0.05892 | 0.08333 | Softening (0.71x) | C^2-C^2 within-doublet |
| Protected | 4 | 0.06250 (exact) | 0.06250 | Fixed | u(1)-C^2 planes |
| Hard | 3 | 0.12186 | 0.08333 | Hardening (1.46x) | su(2)-su(2) planes |

Anisotropy K_max/K_min (positive curvatures): 12.5 at fold, up from 4.0 at bi-invariant point. No negative curvatures at any tau in [0, 0.25].

### Two Protected Invariants

**Theorem 1 (U1-SU2 Flatness)**: K(u(1), su(2)) = 0 exactly for all tau. Three planes, zero curvature, always. Algebraic origin: [lambda_8, lambda_i] = 0 for i = 1,2,3. The u(1) and su(2) generators commute within the u(2) subalgebra. The Jensen deformation cannot generate curvature between commuting generators.

**Theorem 2 (U1-C^2 Protection)**: K(u(1), C^2) = 1/16 = 0.0625 exactly for all tau. Four planes, locked curvature. Maximum deviation from 1/16 across all tau: less than 10^{-15}.

**Corollary (Ricci u(1) Invariance)**: Ric(u(1)) = 0*3 + (1/16)*4 = 1/4 exactly for all tau. The Ricci curvature along the hypercharge direction is a tau-independent constant. Verified to 2.2e-16 across 26 tau values.

### The Protected Chain

    q_7^2 = K(u(1), C^2) = Ric(u(1)) / dim(C^2) = 1/16

The K_7 eigenvalue q_7 = 1/4 labels the B2 sector. Its square equals the protected sectional curvature. Both derive from the same structure constants of su(3). Nazarewicz classifies this as "representation-theoretic tautology" -- an algebraic identity, not a dynamical coincidence. Volovik sees it as topological protection of the gravitational coupling constant. Both are correct. The identity is structural; the selection of B2 by BCS dynamics is dynamical.

Cooper pairs carry the charge that IS the protected curvature.

### Soft-Pairing Anti-Correlation

| Sector | Home curvature | K at fold | V(s,s) | Pairing share |
|:-------|:---------------|:----------|:-------|:-------------|
| B1 | (Trap 1) | N/A | 0.000 | 0.0% |
| B2 | su(2)-C^2 cross | 0.00974 | 0.256 | 90.7% |
| B3 | su(2)-su(2) | 0.12186 | 0.003 | 1.0% |

The softest curvature branch hosts the strongest pairing. Curvature ratio 12.5:1, pairing ratio 85:1. Landau identifies this as the phonon softening mechanism: soft springs produce the lowest-frequency modes with the largest displacement amplitudes and the strongest BCS coupling. The non-proportionality (12.5 vs 85) is expected from BCS exponential sensitivity: Delta ~ exp(-1/g*N(E_F)), so a 12.5x difference in spring constant exponentially amplifies through the gap equation.

Volovik's flat-band mechanism (Paper 18) provides the sharpest statement: the B2 sector is an exact flat band (FLATBAND-43). On flat bands, T_c scales linearly with g instead of exponentially, producing power-law enhancement from the DOS divergence.

---

## 8. Open Questions

### 8.1 The Acoustic Metric at N_pair = 1

The BLV acoustic metric requires a background condensate with density rho and sound speed c_s. At N_pair = 1, there is no macroscopic condensate. The "phonon" is a single pair hopping on a lattice. Does the BLV construction survive? The 229x hierarchy is geometric (it comes from J_C2 and dS/dtau, both structural). But the acoustic metric formalism assumes a continuous fluid, not a single quantum walker. The tight-binding band structure omega(K) = 2J(1 - cos Ka) defines a group velocity and an effective metric -- but the connection to the BLV conformal rescaling needs explicit construction on the discrete lattice. This is the framework's most urgent theoretical gap.

### 8.2 The 8D vs 3+1D BLV Exponent

The W0-1 derivation used the 3+1D BLV metric. The internal space is 8D. The conformal rescaling a_acoustic = a_geom * (rho/c_s)^{f(d)} has dimension-dependent exponents. In d spatial dimensions, the conformal factor in the acoustic metric acquires powers that depend on d. The exponent could change from 1/2 to 1/7 or another d-dependent value. This directly affects the e-fold count from the 229x hierarchy and could close (or widen) the 0.21 gap.

### 8.3 E_0(tau) Sweep

The exact diagonalization ground state energy E_0(tau) is the only remaining stabilization route (S53 synthesis). Sweep the 256-state Fock space at 50 tau values. Does E_0(tau) have a minimum? Mean-field gives Delta = 0 (no minimum). ED gives Delta = 0.77 (non-perturbative). The question is whether the non-perturbative many-body energy landscape has a minimum that the mean field cannot see. This is a computation, not a debate.

### 8.4 Tight-Binding Diagonalization on the Voronoi Graph

Replace the continuum GL extrapolation with exact diagonalization of the hopping Hamiltonian on the 32-cell Voronoi graph. The graph has known adjacency (Weyl reflections + center translations). The hopping matrix is H_ij = J_ab * delta_{<i,j>_ab}, where the Josephson coupling depends on which Lie algebra direction connects cells i and j. This gives the actual discrete spectrum, not the continuum approximation. The result determines whether the continuum c_Gold = 0.915 is an accurate representation of the pair's dynamics or a GL artifact.

### 8.5 C^2 Isotropization and Lifshitz Transition

Within C^2, the within-doublet/cross-doublet curvature ratio drops from 4.0 at tau = 0 to 1.48 at the fold to 1.17 at tau = 0.25. Volovik identifies this convergence as a Lifshitz transition precursor: when two dispersion branches merge, the DOS diverges and the Fermi surface topology changes. At what tau do the C^2-C^2 sub-branches cross? If the crossing exists, the fold sits between two phase transitions.

---

## 9. Key Numbers Reference

| Quantity | Value | Units | Provenance |
|:---------|:------|:------|:-----------|
| tau_fold | 0.19 | -- | S12 phi_paasch |
| R(fold) | 2.018 | M_KK^2 | S47 curvature anatomy |
| N_cells | 32 | -- | S42 Voronoi tessellation |
| N_pair | 1 | -- | S53 W2-6 (PERMANENT) |
| c_fabric | 209.97 | M_KK | S42 spectral action gradient |
| c_Gold | 0.915 | M_KK | S52 GL-JOSEPHSON-52 |
| c_fabric/c_Gold | 229.5 | -- | S53 P5 (PERMANENT) |
| N_e^acoustic | 2.89 | e-folds | S53 W0-1 BLV formula |
| N_e^geom | 0.1734 | e-folds | S52 EFOLD-MAPPING-52 |
| J_C2 | 0.933 | M_KK | S47/S48 Josephson coupling |
| J_su2 | 0.059 | M_KK | S47/S48 |
| J_u1 | 0.029 | M_KK | S47/S48 |
| E_J / E_C | 0.818 | -- | S53 W3-12 (Mott side) |
| Gi | 0.506 | -- | S53 W3-12 |
| V(B2,B2) | 0.256 | M_KK | S34-S35 Kosmann V matrix |
| V(B3,B3) | 0.003 | M_KK | S34-S35 |
| V(B1,B1) | 0.000 | M_KK | S22c Trap 1 (exact) |
| K(u1,su2) | 0.000 | M_KK^2 | Theorem 1 (exact, all tau) |
| K(u1,C^2) | 1/16 | M_KK^2 | Theorem 2 (exact, all tau) |
| Ric(u1) | 1/4 | M_KK^2 | Corollary (exact, all tau) |
| q_7 (B2) | 1/4 | -- | Spinor rep, S34 [iK_7,D_K]=0 |
| Delta_B2 | 0.732 | M_KK | S35 BCS gap (dominant) |
| omega_L1 | 0.070 | M_KK | S48 LEGGETT-MODE-48 (3-band) |
| omega_L2 | 0.107 | M_KK | S48 LEGGETT-MODE-48 |
| omega_att | 1.430 | M_KK | S37 pair vibration |
| phi_paasch | 1.5316 | -- | S12 m_{(3,0)}/m_{(0,0)} |
| tau_cross (omega_L2/omega_L1 = phi) | 0.2117 | -- | S50 LEGGETT-PHI-CONFIRM-50 |
| Gamma/omega | 0.000 | -- | S53 W3-1 (exact, all branches) |
| Berry/Zak phases | 0 | -- | S53 W3-15 (double triviality) |
| BLV exponent | -1/2 | -- | S53 W0-1 (in a_acoustic, not H) |

---

## 10. The Portrait

The Jensen crystal at the fold is an 8-dimensional compact Riemannian manifold tessellated into 32 Voronoi cells. It has rigid bones (su(2), K = 0.122), a protected anchor (u(1), K = 0 and 1/16 exactly), soft flesh (su(2)-C^2 cross, K = 0.010), and an isotropizing core (C^2, converging toward internal isotropy). A single Cooper pair hops between cells with infinite lifetime, its dispersion defining 6 tight-binding bands: 1 Goldstone + 2 Leggett + 3 Higgs.

The pair is a quantum walker, not a superfluid. E_J/E_C = 0.818 places the system in the Mott regime: charge-quantized, phase-uncertain, no spontaneous symmetry breaking. The "Goldstone mode" is translational kinetic energy, not a broken-symmetry phase mode. The pairing gap Delta = 0.77 M_KK is non-perturbative, emerging from exact diagonalization and the instanton gas, invisible to mean-field BCS.

The crystal's acoustic architecture funnels 91% of pairing through the B2 sector, which lives on the 12 softest curvature planes. The protected chain q_7^2 = K(u1, C^2) = 1/16 locks the pairing quantum number to a tau-independent geometric invariant. Cooper pairs carry the charge that IS the protected curvature.

The 229x sound speed hierarchy -- c_fabric = 209.97, c_Gold = 0.915 -- converts through the BLV acoustic metric into 2.72 acoustic e-folds of expansion, with the total reaching 2.89 when geometric e-folds are included. The internal volume does not change. The expansion is purely acoustic: a 4D observer measuring "distances" with phonon rulers sees the effective metric stretch as the sound speed drops during transit through the fold.

The crystal is not a background on which physics happens. It IS the physics. Its curvature branches are the spring constants. Its tight-binding bands are the particle spectrum. Its Josephson couplings are the inter-cell bonds. Its deformation parameter tau is the clock. The pair walks, the crystal rings, and the acoustic metric expands.

One fold. One pair. One song.

---

**Data provenance**: S47 (`s47_curvature_anatomy.npz`, `s47_condensate_torus.npz`, `s47_spectral_landscape.npz`), S52 (`s52_gl_josephson.npz`), S53 (`s53_blv_conformal.py`, `s53_gl_sweep.npz`, `s53_ginzburg_fabric.py`, `s53_berry_anticrossing.npz`). Constants from `computations/canonical_constants.py`.
