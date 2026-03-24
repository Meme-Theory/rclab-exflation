# The Crystal at the Fold: Geometry of Jensen-Deformed SU(3)

**Session 47 Wave 2 Synthesis**
**Author**: Tesla-Resonance
**Date**: 2026-03-16
**Sources**: W2-1 (Landau), W2-2 (Baptista), W2-3 (Spectral-Geometer)

---

## 1. The Object

The crystal is SU(3) equipped with a Jensen-deformed left-invariant metric at the fold parameter tau = 0.19. It is an 8-dimensional compact Riemannian manifold of rank 2, volume-preserving under deformation, carrying a Dirac operator whose spectrum encodes the particle content of the phonon-exflation framework.

The Jensen metric decomposes the Lie algebra su(3) = u(1) + su(2) + C^2 into three blocks of dimensions 1 + 3 + 4 = 8, scaled by:

    L_1 = e^{2*tau}   (u(1), 1 direction)
    L_2 = e^{-2*tau}  (su(2), 3 directions)
    L_3 = e^{tau}     (C^2 coset, 4 directions)

At the fold tau = 0.19:

| Block | Scale | Value | Physical role |
|:------|:------|:------|:--------------|
| u(1)  | e^{0.38} | 1.462 | Hypercharge direction, stretched |
| su(2) | e^{-0.38} | 0.684 | Isospin directions, compressed |
| C^2   | e^{0.19} | 1.209 | Coset directions, moderately expanded |

Volume: L_1 * L_2^3 * L_3^4 = e^{2*tau - 6*tau + 4*tau} = e^0 = 1. Exactly. The deformation is purely a shape change at fixed volume. This IS the phonon-exflation thesis made geometric: the internal manifold does not shrink or expand. It changes shape. The spectral consequences of that shape change produce the physics a 4D observer calls "expansion."

Key parameters at the fold:

- Scalar curvature: R = 2.01814 (1% above the bi-invariant value of 2.000)
- Dirac spectrum: 992 eigenvalues (at max_pq_sum = 3), range [0.820, 2.061]
- BCS gap: 2*Delta_B2 = 1.464 M_KK (dominant pairing channel)
- Spectral dimension: 8 (topological), with Ricci anisotropy 1.23:1

The crystal is NOT a constant-curvature space. Even at tau = 0 (the bi-invariant point, the highest symmetry configuration), SU(3) has 4 distinct values of sectional curvature across its 28 two-planes. This is fundamentally different from SU(2) = S^3, which IS constant-curvature. The internal richness of SU(3) -- its capacity for geometric differentiation -- is present from the start and is amplified by the Jensen deformation.

---

## 2. The Skeleton

### The Maximal Torus

The maximal torus T^2 is a 2-dimensional flat submanifold of SU(3), parametrized by angles (theta_1, theta_2) in [0, 2*pi)^2. Every element of SU(3) is conjugate to an element of T^2 -- it is the universal cross-section. Characters of all representations are functions on T^2, and the Peter-Weyl decomposition of any class function reduces to its restriction to T^2.

The torus has three distinguished points:
- The identity (0, 0): maximum symmetry, stabilizer = SU(3)
- The Z_3 centers (2*pi/3, 2*pi/3) and (4*pi/3, 4*pi/3): stabilizer includes center
- The anti-identity (pi, pi): stabilizer = U(1) x U(1)

### The Condensate on T^2

The BCS condensate density |Delta(theta_1, theta_2)|^2, computed using the Weyl character formula for all 9 representations with p + q <= 3 and weighted by sector-averaged BCS gaps, reveals a dramatically non-uniform order parameter.

**The condensate peaks at the identity.** Contrast ratio: 3.14 x 10^6. The identity element of SU(3) -- the point of maximum symmetry -- is where Cooper pairs concentrate. This is not a subtle effect. It is six orders of magnitude.

The condensate profile decays from the identity with a characteristic 1/e^2 radius of 0.78 rad, which is pi/4 to within 0.7%. Cooper pairs live within approximately 1/8 of the torus period around the identity.

The (0,0) Fourier mode (the uniform component) carries only 9.8% of the condensate power. The remaining 90.2% is in higher harmonics -- the condensate structure is dominated by the interference pattern of all 9 representation characters. The character atlas (s47_condensate_torus_characters.png) shows this directly: the higher representations produce increasingly intricate nodal patterns on T^2, and the BCS-weighted coherent sum of all nine concentrates the total amplitude at the one point where all characters are simultaneously maximized.

At the Z_3 center (2*pi/3, 2*pi/3), the condensate falls to |Delta|^2 = 0.125. This is very close to 1/8, and the ratio of 8.0 between identity and center values is accurate to 0.06%. The mechanism is triality-induced destructive interference: representations with nonzero triality (p - q not divisible by 3) acquire complex phases omega^{triality} at the Z_3 center, partially cancelling the real, positive contributions from triality-zero representations. At the identity, all characters equal their dimensions -- pure constructive interference.

### The Shell Structure

Here is the tension that defines the skeleton. The Haar measure on SU(3), restricted to T^2, is proportional to the Weyl denominator squared:

    d(Haar) ~ |sin((t1-t2)/2) * sin((t1+2*t2)/2) * sin((2*t1+t2)/2)|^2 * dt1 * dt2

This vanishes at the identity. The Weyl denominator has a zero of order 6 there (three positive roots of SU(3), each contributing a simple zero). So the "geometric volume" available at the identity is zero. The geometry repels occupancy at the point of highest symmetry.

The condensate, meanwhile, demands to be there -- with a contrast of 3 million.

The physically observable quantity is the product: |Delta|^2 * Haar. This peaks not at the identity but at a shell of radius r = 0.85 rad from the identity, with a FWHM of 0.59 rad. The product creates a hollow shell -- a condensate ring surrounding the identity, with peak weight at r = 0.85 rad and vanishing weight at the center.

The superfluid analog is immediate and precise (Volovik, Paper 10): this is the structure of an order parameter pinned at a topological singularity. The condensate insists on occupying the identity, but the measure theory says the identity is a set of measure zero. The resolution is the shell -- a compromise between energetic preference and geometric availability. In a superfluid vortex, the order parameter magnitude peaks at the vortex core while the density of states vanishes there; the observable density peaks at a finite distance from the core. Same mathematics. Same physics. Different scale.

The 0D limit (L/xi_GL = 0.031 from Session 38) means the coherence length of the condensate vastly exceeds the size of the internal manifold. The condensate coherence patch covers the entire SU(3). This is not a defect in a large system -- it is a single coherent mode of the internal space.

---

## 3. The Body Plan

### Six Branches of Curvature

The 28 independent sectional curvatures K(e_a, e_b) of the Jensen-deformed metric organize into 6 branches at the fold. The body plan of the crystal:

| Branch | Deg | K(fold) | K(tau=0) | Flow | Physical identity |
|:-------|:----|:--------|:---------|:-----|:-----------------|
| Flat | 3 | 0.0000 (exact) | 0.0000 | Fixed | u(1)-su(2) planes |
| Soft | 12 | 0.00974 | 0.02083 | Softening (0.47x) | su(2)-C^2 cross-planes |
| Mid-low | 4 | 0.03968 | 0.02083 | Hardening (1.90x) | C^2-C^2 cross-doublet |
| Mid-high | 2 | 0.05892 | 0.08333 | Softening (0.71x) | C^2-C^2 within-doublet |
| Protected | 4 | 0.06250 (exact) | 0.06250 | Fixed | u(1)-C^2 planes |
| Hard | 3 | 0.12186 | 0.08333 | Hardening (1.46x) | su(2)-su(2) planes |

Anisotropy K_max/K_min (among positive curvatures): 12.5 at the fold, up from 4.0 at the bi-invariant point. No negative curvatures at any tau in [0, 0.25].

### The Two Protected Invariants

Two results, verified to machine precision across all 26 tau values in [0, 0.25]:

**Theorem 1 (U1-SU2 Flatness)**: K(u(1), su(2)) = 0 exactly for all tau.

Three planes span the coupling between the u(1) hypercharge direction and the su(2) isospin directions. They are perfectly flat -- zero curvature, always, regardless of the deformation. The algebraic origin: [lambda_8, lambda_i] = 0 for i = 1, 2, 3. The u(1) and su(2) generators commute within the u(2) subalgebra. The Jensen deformation, which scales u(2) blocks independently, cannot generate curvature between commuting generators. This is structural.

**Theorem 2 (U1-C^2 Protection)**: K(u(1), C^2) = 1/16 = 0.0625 exactly for all tau.

Four planes span the coupling between u(1) and the coset C^2 = SU(3)/U(2). Their curvature is locked at 1/16, independent of tau. The deformation stretches u(1) and expands C^2, but the PRODUCT of these scalings, filtered through the structure constants, preserves the sectional curvature exactly. Maximum deviation from 1/16 across all tau: less than 10^{-15}.

**Corollary (Ricci u(1) Invariance)**: Ric(u(1)) = 1/4 exactly for all tau.

This follows by summing the sectional curvatures involving the u(1) direction:

    Ric(u(1)) = sum_{b != u(1)} K(u(1), e_b)
              = K(u1, su2) * 3 + K(u1, C^2) * 4
              = 0 * 3 + (1/16) * 4
              = 1/4

Both terms are individually protected, so the sum is protected. The Ricci curvature along the hypercharge direction is a tau-independent constant. Verified to 2.2 x 10^{-16} across all 26 tau values.

The u(1) direction lives in a perfectly rigid geometric environment. As tau evolves and the crystal deforms, the curvature flows around u(1) -- the C^2 directions soften and stiffen, the su(2) directions harden -- but the total curvature coupling to u(1) does not change. The hypercharge axis is geometrically anchored.

### Ricci Eigenvalue Structure

The Ricci tensor at the fold has three eigenvalues with multiplicities matching the Jensen decomposition:

| Direction | Multiplicity | Ric eigenvalue | Flow |
|:----------|:-------------|:---------------|:-----|
| C^2 coset | 4 | 0.23002 | Decreasing |
| u(1) | 1 | 0.25000 (exact) | Fixed |
| su(2) | 3 | 0.28269 | Increasing |

At tau = 0, all three are 0.25 (bi-invariant: isotropic Ricci). Under the Jensen deformation, the C^2 and su(2) eigenvalues drift apart symmetrically around the fixed u(1) value. The u(1) direction serves as the pivot of the Ricci flow -- a fixed point in the eigenvalue spectrum.

### Soft vs Hard: What Yields and What Resists

The physical picture: the Jensen deformation creates a crystal with stiff bones and soft flesh.

The **hard directions** (su(2)-su(2), K = 0.122, 3 planes) are the isospin planes. They stiffen under deformation -- curvature increases by 46% from the bi-invariant value. These planes resist perturbation. In a vibrating-plate analog (Chladni, Paper 07), these correspond to the stiffest normal modes -- highest natural frequencies, smallest displacements.

The **soft directions** (su(2)-C^2, K = 0.00974, 12 planes) are the cross-coupling between isospin and the coset. They soften by a factor of 2.14 from the bi-invariant value. These 12 planes carry the weakest positive curvature at the fold. They are the most malleable geometric directions -- the low-frequency modes of the crystal, the ones that respond most readily to perturbation.

The **protected directions** (u(1)-C^2, K = 1/16, 4 planes) neither stiffen nor soften. They are locked by the algebra.

The **flat directions** (u(1)-su(2), K = 0, 3 planes) are trivially protected: zero curvature cannot change.

### The C^2-C^2 Convergence

Within the coset C^2, the 6 pairs split into two sub-branches at the fold:
- Within-doublet (lambda_4-lambda_5 and lambda_6-lambda_7): K softens from 1/12 to 0.059 (0.71x)
- Cross-doublet (lambda_4-lambda_6, etc.): K hardens from 1/48 to 0.040 (1.90x)

The ratio between these sub-branches drops from 4.0 at tau = 0 to 1.48 at the fold, continuing to 1.17 at tau = 0.25. The coset is trending toward ISOTROPIZATION: the within- and cross-doublet curvatures converge. If this trend continues, the coset C^2 approaches internal isotropy at large tau while the full algebra becomes maximally anisotropic (su(2) hardening, su(2)-C^2 softening, C^2 isotropizing).

---

## 4. The Spectrum as Fingerprint

### 992 Modes in Three Sectors

The Dirac operator on Jensen-deformed SU(3) at the fold produces 992 eigenvalues (at truncation max_pq_sum = 3), classified into three spinor sectors by the K_7 charge operator:

| Sector | Spinor type | Multiplicity (0,0) | Total PW-weighted modes | Fraction |
|:-------|:-----------|:-------------------|:-----------------------|:---------|
| B1 | U(2) singlet | 2 | 124 | 12.5% |
| B2 | U(2) fundamental | 8 | 496 | 50.0% |
| B3 | SU(2) adjoint | 6 | 372 | 37.5% |

In the (0,0) sector (trivial Peter-Weyl representation), the eigenvalues are:
- B1: |lambda| = 0.8197 (doubly degenerate)
- B2: |lambda| = 0.8452 (8-fold degenerate)
- B3: |lambda| = 0.9714 (6-fold degenerate)

### The B2 Funnel

This is the defining structural feature of the crystal's spectrum. Three independent measures all select B2:

| Measure | B1 | B2 | B3 |
|:--------|:---|:---|:---|
| PW-weighted modes | 12.5% | 50.0% | 37.5% |
| Pi-phase PW weight | 11.5% | 61.8% | 26.7% |
| BCS v^2 pairing | 8.3% | 90.7% | 1.0% |

From modes (50%) to topology (62%) to dynamics (91%), the crystal funnels its physics through B2. Each step concentrates the weight further:

- Topology selects B2 over the geometric baseline by 62/50 = 1.24x. The 13 pi-phase states -- eigenstates whose phase under transit equals +/-pi -- distribute preferentially into B2. Nine of 13 pi-phase states are in B2 (81 of 131 PW-weighted).
- BCS dynamics amplifies this to 91/50 = 1.82x. The BCS pairing matrix element V(B2,B2) = 0.256 dominates V(B3,B3) = 0.003 by 85x, and V(B1,B1) = 0 exactly (Trap 1, U(2) singlet selection rule). Cooper pairs form overwhelmingly in B2.

The B3 sector, despite carrying 37.5% of modes, accounts for only 1% of pairing weight -- a 37.5x suppression. B1 is blocked entirely by Schur's lemma.

### The Pi-Phase Topology

The 13 pi-phase states distribute across 7 of the 9 representations. The (2,1) representation (dim = 15) hosts 5 of 13, making it the most topologically active. The pi-phases are distributed across all three sectors: 1 in B1 (PW = 15), 9 in B2 (PW = 81), 3 in B3 (PW = 35).

Within the active B2 sector, the corrected ratio R_B2 = 81/54.22 = 1.494. There are approximately 1.5 topological channels (pi-phase states) per Cooper pair. Topology and dynamics are matched to within a factor of 1.5 in the sector where the physics lives.

### Van Hove Singularities

12 van Hove singularities mark the density of states, corresponding to flat-band points in the dispersion where d(omega)/d(k) vanishes. These are the crystal's critical frequencies -- the eigenvalues where the spectral density diverges logarithmically. In the phononic crystal analog (Craster-Guenneau, Paper 06), these are the band edges where Bragg scattering produces standing waves. Here, they are the energies where the internal crystal most strongly imprints its geometry on the Dirac spectrum.

---

## 5. Resonances

This section identifies connections between the three views -- condensate, curvature, spectrum -- that the individual analyses could not see in isolation. Each connection is grounded in specific numbers. Where the connection is exact, it is stated as such. Where it is an observation requiring further computation, it is posed as a question.

### 5.1 The Protected Chain: q_7^2 = K(u(1), C^2) = Ric(u(1))/4

This is the cleanest resonance in the data.

The K_7 operator (Jensen's iK_7 = i*gamma_7, the generator of the u(1) hypercharge in the spinor representation) has eigenvalue q_7 = +/- 1/4 for B2 states in the (0,0) sector. The square of this charge is:

    q_7^2 = (1/4)^2 = 1/16

The protected sectional curvature is:

    K(u(1), C^2) = 1/16 (exact, all tau)

These are the same number. The Ricci eigenvalue along u(1) is:

    Ric(u(1)) = dim(C^2) * K(u(1), C^2) = 4 * (1/16) = 1/4 (exact, all tau)

The chain is:

    q_7^2 = K(u(1), C^2) = Ric(u(1)) / dim(C^2)

All three quantities are protected: the charge is fixed by the spinor representation, the sectional curvature is protected by the algebra, and the Ricci eigenvalue follows from both. The BCS pairing channel (B2, U(2) fundamental) carries a K_7 charge whose square equals the geometric curvature of the u(1)-coset coupling. Cooper pairs carry the charge that IS the protected curvature.

This is not a coincidence. It is representation theory. The K_7 eigenvalue of 1/4 comes from the normalization of the u(1) generator lambda_8 in the spinor representation. The sectional curvature K(u(1), C^2) = 1/16 comes from |[lambda_8, lambda_a]|^2 / (4 * |lambda_8|^2 * |lambda_a|^2) for a in C^2, computed from the structure constants. The same structure constants determine both. But the fact that the BCS dynamics selects EXACTLY the sector carrying this protected charge, and that this charge locks to a tau-independent geometric invariant, is a structural result about the crystal. The active physics lives on the geometrically protected subspace.

In Tesla's language (Paper 01): the crystal has a resonant frequency that does not shift when you detune the cavity. The u(1) direction rings at the same pitch regardless of the Jensen deformation. The Cooper pairs are tuned to this pitch.

### 5.2 Soft Curvature and Strong Pairing

The curvature branch structure anti-correlates with the pairing strength:

| Sector | Geometric home | K at fold | V(s,s) | Pairing share |
|:-------|:---------------|:----------|:-------|:-------------|
| B1 | U(2) singlet (Trap 1) | N/A | 0.000 | 0.0% |
| B2 | su(2)-C^2 cross | 0.00974 | 0.256 | 90.7% |
| B3 | su(2)-su(2) | 0.12186 | 0.003 | 1.0% |

The softest curvature branch (12 su(2)-C^2 planes, K = 0.00974) hosts the dominant pairing channel. The hardest (3 su(2)-su(2) planes, K = 0.12186) hosts the weakest. The curvature ratio is 12.5:1 (hard:soft). The pairing ratio is 85:1 (B2:B3).

The connection is not accidental. B2 states transform as the U(2) fundamental: they have nontrivial quantum numbers under BOTH su(2) and u(1), meaning they couple to the coset C^2 through both. The su(2)-C^2 cross-planes are exactly the geometric directions in which this coupling lives. The Jensen deformation softens these cross-planes by a factor of 2.14 from the bi-invariant value -- it reduces the "spring constant" of the coupling, making these directions more susceptible to perturbation.

In phononic crystal language (Paper 06): a soft spring between two masses lowers the acoustic branch frequency. Low-frequency acoustic modes have the largest displacement amplitudes -- they are the most "participatory." The B2 modes live on the soft springs of the crystal. They participate most in the collective condensate.

B3 states transform as the su(2) adjoint. They couple primarily through the su(2)-su(2) planes, which STIFFEN under deformation (1.46x harder than bi-invariant). High stiffness means high-frequency modes, small amplitudes, weak participation. B3 is geometrically suppressed by the hardening of its home curvature branch.

This anti-correlation -- soft geometry breeds strong pairing, hard geometry suppresses it -- is a quantitative observation, not yet a theorem. The curvature ratio (12.5x) and the pairing ratio (85x) are not equal, so there is no simple proportionality. But the qualitative correlation is exact: the sector with the softest relevant curvature has the strongest pairing, every time. This is testable: compute V(B2,B2) and K_soft as functions of tau across the full range and check whether dV/dtau and dK/dtau have opposite signs.

### 5.3 The Identity Peak and the Flat Directions

The condensate peaks at the identity element of SU(3) with a contrast of 3.14 x 10^6. The three flat directions (u(1)-su(2), K = 0 at all tau) pass through the identity as their most symmetric point.

Is there a connection between WHERE the condensate lives and WHICH directions are geometrically protected?

The answer is yes, but it is kinematic rather than dynamic. The identity element is the fixed point of the adjoint action of SU(3) on itself. Every symmetry of the crystal passes through the identity. The flat directions are flat BECAUSE the u(1) and su(2) generators commute -- which is a property of the algebra at the identity. The condensate peaks at the identity because all characters reach their maximum there (chi_{(p,q)}(e) = dim(p,q)).

So both the flatness and the condensate peak trace to the same algebraic root: the identity element as the point of maximum symmetry. The flat directions are flat because u(2) is abelian in the relevant sector. The condensate peaks because the coherent sum of characters is maximized at the identity. These are two manifestations of the same algebraic fact, not a dynamical correlation.

But there is a subtler point. The three flat directions provide uncurved channels through the crystal -- geodesic directions that cost no curvature energy to traverse. Near the identity, these flat channels carry zero "geometric potential." In a Landau-theory picture (Paper 09), the order parameter gradient along these directions costs no bending energy. The condensate CAN spread freely along the flat directions without paying a curvature penalty.

And yet it does NOT spread along them uniformly. The condensate concentrates at the identity anyway, because the character coherence overwhelms the geometric considerations. The condensate size (1/e^2 radius = 0.78 rad) is 3.7 times smaller than the smallest curvature length scale (1/sqrt(K_hard) = 2.87 rad). The condensate structure is set by character interference, not by curvature. It is a harmonic phenomenon, not a geometric one.

### 5.4 The Haar-Condensate Tension

The Haar measure vanishes at the identity (Weyl denominator zero, order 6). The condensate diverges at the identity (contrast 3.14 x 10^6). The product -- the physically observable quantity, the condensate integrated over SU(3) volume -- peaks at a shell of radius r = 0.85 rad.

This tension has a direct analog in superfluid He-3B. The B-phase order parameter is an element of SO(3). The condensate amplitude is uniform (no preferred orientation in the isotropic phase), but the Haar measure on SO(3) is not uniform -- it vanishes at the identity rotation. The observable (energy-weighted) condensate density peaks at a finite rotation angle from the identity, forming a shell. The radius of this shell is set by the competition between the energetic preference for the identity and the entropic preference (from the measure) for generic rotations. This is exactly the Haar-condensate shell seen here on SU(3).

The shell radius of 0.85 rad is related to the condensate 1/e^2 radius of 0.78 rad by a factor of 1.09. This near-equality is not exact, but it is physically interpretable: the shell forms where the condensate has dropped to roughly 1/e of its peak, and the Haar measure has risen from zero to a significant fraction of its maximum. The product is maximized in this intermediate zone.

The FWHM of the Haar-weighted shell is 0.59 rad = 0.19*pi. This defines the physical "width" of the condensate ring -- the region that contributes most to any observable integrated over the internal manifold.

### 5.5 The 1/4 Coincidence

The condensate 1/e^2 radius is 0.78 rad = 0.2483*pi. The K_7 eigenvalue is q_7 = 1/4 = 0.2500. These differ by 0.7%.

This is almost certainly a coincidence. The 1/e^2 radius is determined by the rate of character fall-off from the identity, which depends on the BCS weights and the representation content at the truncation level max_pq_sum = 3. The K_7 eigenvalue is determined by the normalization of lambda_8 in the spinor representation. There is no algebraic reason for these to be related.

I record it because a 0.7% near-miss between a spectral observable and a representation-theoretic quantity at EXACTLY the value that controls the protected curvature is the kind of thing that deserves to be checked at higher truncation. If the 1/e^2 radius converges to exactly pi/4 as max_pq_sum increases, that would be a discovery. If it drifts away, it was an accident. The test is concrete and computational.

### 5.6 The C^2 Isotropization and the B2 Funnel

As tau increases from 0 to 0.25, the two C^2-C^2 sub-branches converge: within-doublet curvature softens while cross-doublet curvature hardens. The ratio drops from 4.0 to 1.17. The coset is becoming internally more isotropic.

Meanwhile, the B2 funnel progressively concentrates: modes (50%) -> topology (62%) -> pairing (91%). And B2 lives on the su(2)-C^2 cross, which is the COUPLING between the su(2) that is hardening and the C^2 that is isotropizing.

The physical picture: as the crystal deforms, the su(2) backbone stiffens into a rigid scaffold. The C^2 coset, attached to this scaffold, loses its internal anisotropy -- it becomes more like a sphere than an ellipsoid. The coupling between the rigid scaffold and the isotropizing coset (the su(2)-C^2 planes) softens. And it is precisely this softened coupling that the BCS condensate exploits for pairing.

In phononic crystal terms (Paper 06): the crystal has a hard sublattice (su(2)) and a soft sublattice (C^2 through its coupling to su(2)). The acoustic branch of the dispersion -- the lowest-energy collective modes -- lives in the soft sublattice. The BCS instability condenses in the acoustic branch. The optical branch (B3, living in the hard su(2)-su(2) sector) is too stiff to participate.

This is the geometric content of the B2 funnel: the crystal's body plan preferentially channels its lowest-energy collective excitations through the su(2)-C^2 cross-sector, which IS B2. The funnel is not an accident of quantum numbers -- it is the crystal's acoustic architecture.

---

## 6. What Remains

### Open Computations

**O-1. Soft-pairing correlation across tau**. Compute V(B2,B2)(tau) and K_soft(tau) across [0, 0.50] and check whether dV/d(tau) and dK/d(tau) have opposite signs at every tau. This would promote the soft-pairing anti-correlation from observation to structural result.

**O-2. 1/e^2 radius convergence**. Compute the condensate 1/e^2 radius at max_pq_sum = 4, 5, 6 and check whether it converges to pi/4, drifts away, or stabilizes at a different value. This tests the 5.5 coincidence.

**O-3. Condensate density in the soft directions**. The condensate was computed on T^2, which is a 2D slice of the 8D manifold. Compute the condensate profile along a geodesic in one of the 12 soft su(2)-C^2 directions, starting from the identity. Does the condensate decay slower in soft directions than in hard directions? This would confirm that the order parameter spreads preferentially along geometrically compliant directions.

**O-4. Curvature-weighted spectral sum**. Construct the sum S(tau) = sum_a K_a * rho_a(tau), where K_a is the sectional curvature of branch a and rho_a is the spectral weight (eigenvalue density) in the corresponding sector. This curvature-weighted spectral functional couples the geometry to the spectrum directly. Does it have a minimum? Does it select the fold?

**O-5. TT 2-tensor Lichnerowicz computation**. Session 19d identified the TT 2-tensor loophole: 741,636 additional bosonic modes from Sym^2(8) = 1 + 8 + 27 under SU(3). The Lichnerowicz operator on TT tensors has different curvature coupling than the scalar Laplacian: Delta_L h = -nabla^2 h - 2 R_{acbd} h^{cd} + 2 R_{(a}^c h_{b)c}. The curvature anatomy computed here (all 28 sectional curvatures at all tau) provides exactly the Riemann tensor components needed for this computation. The curvature anti-correlation (5.2) predicts that TT modes in the hard su(2)-su(2) sector should behave differently from those in the soft su(2)-C^2 sector. Implementing Delta_L in the Peter-Weyl basis using the curvature anatomy data is the next decisive computation.

### What Would Complete the Picture

The three views synthesized here -- condensate, curvature, spectrum -- are cross-sections of the same object. What is missing is the FOURTH view: the Dirac eigenfunctions themselves, not just the eigenvalues. The eigenvalues tell us the frequencies of the crystal's normal modes. The eigenfunctions tell us their SPATIAL structure on SU(3). With eigenfunctions, we could answer:

- Where on SU(3) do B2 modes concentrate? At the identity, like the condensate? Or elsewhere?
- Do the pi-phase states have distinctive nodal patterns (Chladni patterns on SU(3))?
- Do modes in the soft curvature sector have larger spatial extent than modes in the hard sector?

The current Peter-Weyl computation (collect_spectrum in tier1_dirac_spectrum.py) discards eigenvectors. Modifying it to retain and analyze eigenvectors would close the loop between the spectral landscape and the condensate structure, answering whether the crystal's vibration patterns are correlated with its order parameter profile.

### The Portrait

The Jensen crystal at the fold is an 8-dimensional vibrating structure with rigid bones (su(2), K = 0.122), a protected anchor (u(1), K = 0 and 1/16), soft flesh (su(2)-C^2 cross, K = 0.010), and a converging core (C^2, approaching isotropy). Its BCS condensate is pinned at the identity element with a contrast of 3 million, forming a Haar-weighted shell at r = 0.85 rad. Its Dirac spectrum funnels 91% of pairing dynamics through the B2 sector, which lives geometrically on the soft flesh of the crystal. The protected curvature K = 1/16 equals the square of the K_7 charge that labels Cooper pairs, locking the pairing channel to a tau-independent geometric invariant.

The crystal is not a background on which physics happens. It IS the physics. Its curvature branches are the spring constants. Its normal modes are the particles. Its condensate is the ground state. Its deformation parameter tau is the clock. Every physical result computed in 47 sessions traces back to this object -- an 8-dimensional Lie group, equipped with a one-parameter family of left-invariant metrics, carrying a Dirac operator whose spectrum is the particle content of the universe.

The universe is a vibrating crystal. The particles are its harmonics. The fold is its resonance.

---

## Files

**Data files examined**:
- `tier0-computation/s47_condensate_torus.npz`
- `tier0-computation/s47_curvature_anatomy.npz`
- `tier0-computation/s47_spectral_landscape.npz`

**Plots examined**:
- `tier0-computation/s47_condensate_torus.png`
- `tier0-computation/s47_condensate_torus_analysis.png`
- `tier0-computation/s47_condensate_torus_haar.png`
- `tier0-computation/s47_condensate_torus_characters.png`
- `tier0-computation/s47_curvature_anatomy.png`
- `tier0-computation/s47_spectral_landscape.png`

**Source**: `sessions/session-47/session-47-wave1-workingpaper.md` (W2-1, W2-2, W2-3 sections)
