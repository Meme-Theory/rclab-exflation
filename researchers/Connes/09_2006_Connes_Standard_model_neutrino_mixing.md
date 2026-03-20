# Noncommutative Geometry and the Standard Model with Neutrino Mixing

**Author:** Alain Connes
**Year:** 2006
**Journal:** Journal of High Energy Physics, 2006(11), 081 (arXiv: hep-th/0608226)
**Pages:** 35
**Significance:** The updated NCG-SM incorporating right-handed neutrinos and the seesaw mechanism

---

## 1. Historical Context: Why the Update Was Needed

### 1.1 The Original Connes-Lott Model (1990-1996)

The original noncommutative geometry approach to the Standard Model, developed by
Connes and Lott in 1990 and refined through the mid-1990s, successfully derived
the gauge group SU(3) x SU(2) x U(1) and the Higgs mechanism from the axioms of
a spectral triple on an almost-commutative geometry M_4 x F. However, this model
had a significant deficiency: neutrinos were strictly massless.

In the original formulation, the finite algebra was:

```
A_F = C + H + M_3(C)
```

and the finite Hilbert space per generation was H_F = C^{15}, consisting of:

```
Particles (per generation):
  e_R       -- right-handed electron (1)
  nu_L, e_L -- left-handed lepton doublet (2)
  u_R^c     -- right-handed up quarks, 3 colors (3)
  d_R^c     -- right-handed down quarks, 3 colors (3)
  u_L^c, d_L^c -- left-handed quark doublet, 3 colors (6)
  TOTAL: 15 Weyl fermions per generation
```

There was no right-handed neutrino nu_R because the representation theory of
A_F = C + H + M_3(C) did not require one. The neutrino was an SU(2) doublet
partner of the electron, but had no right-handed singlet. This was considered
acceptable in 1990 -- the Standard Model as of that date had massless neutrinos.

### 1.2 The Experimental Revolution (1998-2002)

Two landmark experiments demolished the massless neutrino assumption:

**Super-Kamiokande (1998):** Observed a deficit of atmospheric muon neutrinos
as a function of zenith angle, demonstrating that nu_mu oscillates into nu_tau
during propagation through the Earth. Oscillation requires a mass difference
Delta m^2 ~ 2.5 x 10^{-3} eV^2 between mass eigenstates.

**SNO (2002):** Measured the total solar neutrino flux (via neutral current) and
confirmed it matches the solar model prediction, while the electron neutrino flux
(via charged current) showed a deficit. This proved that nu_e oscillates into
nu_mu and nu_tau. The mass splitting: Delta m^2 ~ 7.5 x 10^{-5} eV^2.

Together, these experiments established that at least two of the three neutrino
mass eigenstates are massive. The original Connes-Lott model could not accommodate
this. A modification was REQUIRED, not optional.

### 1.3 Theoretical Options for Neutrino Mass

There are precisely two ways to give neutrinos mass in a gauge-invariant framework:

1. **Dirac mass only:** Add nu_R as a singlet and couple it via Yukawa to the
   Higgs, exactly like the electron. This gives m_nu = y_nu * v / sqrt(2). But
   then y_nu ~ 10^{-12} -- absurdly small compared to y_e ~ 10^{-6}. No
   explanation for why.

2. **Dirac + Majorana (seesaw):** Add nu_R AND allow it a Majorana mass M_R
   (possible because nu_R is a complete singlet under the SM gauge group). The
   mass matrix in the (nu_L, nu_R) basis is then:

   ```
   M = ( 0    m_D )
       ( m_D  M_R )
   ```

   Diagonalization gives light eigenvalue m_light ~ m_D^2 / M_R and heavy
   eigenvalue m_heavy ~ M_R. For m_D ~ 100 GeV and M_R ~ 10^{14} GeV, this
   gives m_light ~ 0.1 eV. The suppression is NATURAL.

Connes' update implements option 2 within the NCG framework.


## 2. The Enlarged Finite Space

### 2.1 The Key Change: H_F = C^{32} Per Generation

The central modification is the enlargement of the Hilbert space from C^{15} to
C^{32} per generation. The new Hilbert space includes:

```
PARTICLES (16 states per generation):
  nu_R                           -- right-handed neutrino (1)
  e_R                            -- right-handed electron (1)
  nu_L                           -- left-handed neutrino (1)
  e_L                            -- left-handed electron (1)
  u_R^{red, green, blue}         -- right-handed up quarks (3)
  d_R^{red, green, blue}         -- right-handed down quarks (3)
  u_L^{red, green, blue}         -- left-handed up quarks (3)
  d_L^{red, green, blue}         -- left-handed down quarks (3)

ANTIPARTICLES (16 states per generation):
  nu_R^c, e_R^c, nu_L^c, e_L^c  -- antileptons (4)
  u_R^c, d_R^c, u_L^c, d_L^c    -- antiquarks, 3 colors each (12)

TOTAL: 32 per generation, 96 for 3 generations
```

The doubling from 15 to 16 particles comes from adding nu_R. The further
doubling to 32 comes from including antiparticles explicitly (in the original
model, charge conjugation J mapped between particle and antiparticle sectors
within a 15+15=30 dimensional space; the new counting is 16+16=32).

### 2.2 The Algebra Remains A_F = C + H + M_3(C)

A critical point: the algebra A_F is NOT changed. It remains C + H + M_3(C).
What changes is the REPRESENTATION of this algebra on the enlarged Hilbert space.
The right-handed neutrino nu_R transforms trivially under all three factors:

```
nu_R representation:
  C factor    -> acts by multiplication (singlet)
  H factor    -> acts trivially (singlet under SU(2))
  M_3(C)      -> acts trivially (colorless)
```

This is why nu_R was "optional" in the original model -- it is a COMPLETE SINGLET.
The NCG axioms did not force its inclusion. What forces it is the REAL STRUCTURE J.

### 2.3 The Real Structure J and KO-Dimension 6

The real structure J : H_F -> H_F is an antilinear isometry satisfying:

```
J^2 = +1,   JD = +DJ,   J*gamma = -gamma*J   (KO-dimension 6 signs)
```

These signs -- the (+, +, -) pattern -- correspond to KO-dimension 6 mod 8 in
the classification of real K-theory (see Paper 05, Section 3.2). This is NOT a
free choice. The condition J*gamma = -gamma*J (charge conjugation anticommutes
with chirality) is the key constraint that forces the inclusion of nu_R.

For the algebra A_F = C + H + M_3(C), the classification of irreducible
representations satisfying all axioms (including the order-one condition for D_F)
on H_F = C^{32} was carried out by Connes. The result: the representation is
UNIQUELY determined up to equivalence. There is exactly ONE finite geometry
compatible with the axioms. And it contains nu_R.

This is the deep point: the NCG axioms do not merely ALLOW nu_R -- they REQUIRE it
once the correct KO-dimension (6) and the correct real structure are imposed. The
right-handed neutrino is not added by hand; it is demanded by the mathematics.


## 3. The Updated Dirac Operator D_F

### 3.1 Structure of D_F on C^{32}

The finite Dirac operator D_F encodes all the Yukawa couplings and mass terms
of the Standard Model. On the 32-dimensional space per generation, it has the
block structure:

```
D_F = ( S    T* )     where S acts on particles (C^{16})
      ( T    S* )           T mixes particle/antiparticle sectors
```

The operator S contains the Yukawa couplings:

```
S = ( 0        Y_nu*   0      0     )
    ( Y_nu     0       0      0     )
    ( 0        0       0      Y_e*  )
    ( 0        0       Y_e    0     )
```

acting on the lepton sector, with analogous blocks for quarks (Y_u, Y_d).

### 3.2 The Majorana Mass Term: The Key New Ingredient

The operator T contains the Majorana mass matrix M_R for right-handed neutrinos.
This is the entry that was ABSENT in the original Connes-Lott model. It connects
nu_R to its own charge conjugate nu_R^c:

```
T has a non-zero block: M_R connecting nu_R <-> J(nu_R)
```

The Majorana mass M_R is a symmetric 3x3 matrix in generation space (for 3
generations). It is the ONLY mass term in the Standard Model that is not
proportional to the Higgs vacuum expectation value. It is a bare mass, present
before electroweak symmetry breaking.

### 3.3 The Seesaw Mechanism from NCG

After electroweak symmetry breaking (Higgs acquires vev v = 246 GeV), the full
neutrino mass matrix in the (nu_L, nu_R) basis becomes:

```
M_nu = ( 0       m_D )    where m_D = Y_nu * v / sqrt(2)
       ( m_D^T   M_R )
```

For M_R >> m_D (which the NCG framework naturally accommodates since M_R is at
the unification scale Lambda ~ 10^{14}-10^{17} GeV), the light eigenvalues are:

```
m_light ~ -m_D * M_R^{-1} * m_D^T
```

This is the TYPE I SEESAW. The NCG framework does not merely allow it; the
structure of D_F on the enlarged space makes it the GENERIC case. Setting M_R = 0
would be a fine-tuning.

### 3.4 The PMNS Matrix

The Pontecorvo-Maki-Nakagawa-Sakata (PMNS) matrix arises from the mismatch
between the mass eigenstates and the flavor eigenstates in the neutrino sector,
exactly analogous to the CKM matrix for quarks:

```
U_PMNS = U_e^{dagger} * U_nu
```

where U_e diagonalizes Y_e^{dagger} Y_e and U_nu diagonalizes M_light. The PMNS
matrix is parametrized by 3 mixing angles (theta_12, theta_13, theta_23) and 1
(or 3, if Majorana) CP-violating phases.

In the NCG framework, the PMNS matrix is DETERMINED by the Dirac operator D_F.
It is not a free parameter to be fit to data -- it is encoded in the geometry of
the finite space F. However, extracting the PMNS matrix requires knowing the full
D_F, which in the phonon-exflation framework means computing D_K on the deformed
SU(3).


## 4. The Constraint Structure

### 4.1 What the Axioms Fix

The spectral triple axioms for the finite space F, combined with KO-dimension 6,
fix the following:

1. **The algebra:** A_F = C + H + M_3(C) (up to equivalence)
2. **The Hilbert space:** H_F = C^{32} per generation (unique irreducible)
3. **The gauge group:** SU(A_F) / center = SU(3) x SU(2) x U(1)
4. **The hypercharges:** Y = 0, -1, +1/3, -2/3, +2/3, -1/3, +4/3 (all correct)
5. **The existence of nu_R:** FORCED by KO-dim 6 (J*gamma = -gamma*J requires separate chirality sectors)

What the axioms do NOT fix:

1. **The number of generations:** 3 is not derived
2. **The Yukawa coupling matrices:** Y_nu, Y_e, Y_u, Y_d are free parameters
3. **The Majorana mass matrix M_R:** also free
4. **The CKM and PMNS matrices:** encoded in the Yukawas, hence free

### 4.2 The One-Loop Higgs Mass Prediction

From the spectral action at the unification scale Lambda, the quartic Higgs
coupling lambda_0 and the Yukawa couplings satisfy a BOUNDARY CONDITION:

```
lambda_0 = (g_3^2 / 4) * Tr(Y^{dagger} Y)^2 / (Tr(Y^{dagger} Y))^2
```

Running this down to the electroweak scale via the renormalization group gives
a Higgs mass prediction. In 2006, Connes obtained:

```
m_H ~ 170 GeV
```

This prediction was later reduced by threshold corrections and the inclusion of
gravitational contributions. After the Higgs discovery at 125.1 GeV in 2012, the
discrepancy prompted work by Chamseddine-Connes (2012) on the sigma field
(a singlet scalar from the Majorana sector) that modifies the running. With the
sigma field, the NCG prediction becomes compatible with 125 GeV.


## 5. Technical Details of the Finite Spectral Triple

### 5.1 The Grading Operator gamma_F

The Z/2 grading gamma_F on H_F = C^{32} implements chirality in the internal
space. The correct definition (clarified in Session 11) is gamma_F = gamma_{PA}
x gamma_{CHI} (product of particle-antiparticle and chirality gradings). Using
gamma_{PA} alone gives the wrong KO-dimension. With the correct gamma_F,
KO-dimension = 6 is confirmed and D_F anticommutes with gamma_F as required.

### 5.2 The Order-One Condition and Unimodularity

The order-one condition [[D_F, a], J b J^{-1}] = 0 constrains D_F severely:
Yukawa couplings must be diagonal in color, the Majorana mass M_R is lepton-only
(no colored Majorana masses), and the CKM/PMNS structure arises from the mismatch
between up-type and down-type diagonalization bases.

The gauge group is obtained from U(A_F) = U(1) x SU(2) x U(3) via the
unimodularity condition det(u) = 1, which reduces it to U(1)_Y x SU(2)_L x
SU(3)_c with CORRECT hypercharge assignments determined by the representation.


## 6. Connection to Phonon-Exflation Framework

### 6.1 The C^{32} Hilbert Space

The 32-dimensional Hilbert space H_F = C^{32} per generation is EXACTLY the
Hilbert space used in the Tier 0 computation (Sessions 7-8). The computational
verification confirmed:

- All SM quantum numbers emerge correctly from the A_F representation
- The commutant structure matches Connes' classification
- KO-dimension = 6 is parameter-free (no choices made)
- The R_{u(2)} representation uniquely determines the center and factor structure

This is a direct computational confirmation of the mathematical content of
this paper.

### 6.2 The Seesaw and D_K

In the phonon-exflation framework, the finite Dirac operator D_F is identified
with D_K -- the Dirac operator on the internal space K = SU(3) with Jensen
deformation parameter s. The Majorana mass term for nu_R should emerge from a
specific sector of D_K:

```
M_R <-> eigenvalues of D_K in the (1,0) or (0,1) sector of SU(3)
```

The seesaw scale M_R ~ Lambda is then determined by the geometry of the
deformed SU(3), not put in by hand. This is one of the OPEN predictions of
the framework: does D_K at the physically selected s_0 give M_R in the correct
range (10^{14}-10^{15} GeV)?

### 6.3 Neutrino Mass Constraints on s

The KATRIN experiment constrains the effective electron neutrino mass to
m_nu < 0.45 eV (90% CL, as of 2024). Combined with the seesaw formula:

```
m_nu ~ m_D^2 / M_R ~ (y_nu * v)^2 / (eigenvalue of D_K in Majorana sector)
```

This gives a LOWER BOUND on the relevant D_K eigenvalue. If the Dirac spectrum
on deformed SU(3) is known as a function of s (computed in Sessions 12-14 for
p+q <= 6), this translates to a constraint on s. The constraint is weak (any
s giving M_R > 10^{11} GeV suffices) but provides a consistency check.

### 6.4 Three Generations from Geometry

The number of generations (3) is NOT derived in this paper -- Connes
acknowledges it as an open problem. In the phonon-exflation framework, the
claim is that 3 generations emerge from Z_3 x Z_3 triality on SU(3) (Baptista
Paper 18, Appendix E). Session 17a deliverable B-4 tested a weaker version:
Z_3 = (p-q) mod 3 partitions the 28 irreps into 3 classes with O(1) splittings.
The full Z_3 x Z_3 generation structure requires spinor transport on CP^2
(Tier 1.5 computation).


## 7. Summary of Key Results

| Result | Status | Method |
|:-------|:-------|:-------|
| A_F = C + H + M_3(C) | UNIQUE | Classification of irreducibles |
| H_F = C^{32} per generation | UNIQUE | KO-dim 6: (eps,eps',eps'') = (+1,+1,-1) |
| nu_R existence | FORCED | J*gamma = -gamma*J forces particle != antiparticle chirality |
| Seesaw mechanism | NATURAL | M_R in D_F, non-zero generically |
| Hypercharges | CORRECT | Unimodularity condition |
| Higgs mass ~ 170 GeV | WRONG | Revised to ~125 GeV with sigma field |
| Number of generations | NOT DERIVED | Open problem |
| PMNS matrix | PARAMETRIC | Encoded in D_F, not predicted |

---

## References

- Connes, A. (2006). "Noncommutative Geometry and the Standard Model with
  Neutrino Mixing." JHEP 0611:081. arXiv: hep-th/0608226.
- Super-Kamiokande Collaboration (1998). "Evidence for oscillation of
  atmospheric neutrinos." Phys. Rev. Lett. 81, 1562.
- SNO Collaboration (2002). "Direct evidence for neutrino flavor transformation
  from neutral-current interactions in SNO." Phys. Rev. Lett. 89, 011301.
- Connes, A., Lott, J. (1991). "Particle models and noncommutative geometry."
  Nucl. Phys. B Proc. Suppl. 18, 29-47.
- Chamseddine, A., Connes, A. (2012). "Resilience of the Spectral Standard
  Model." JHEP 1209:104. arXiv: 1208.1030.
