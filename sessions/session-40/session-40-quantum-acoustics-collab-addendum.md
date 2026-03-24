# Quantum Acoustics -- Diagram Addendum: S40 Structural Cartography

**Author**: Quantum Acoustics | **Date**: 2026-03-11
**Updates**: S39 Penrose diagrams with S40 gates and substrate principle

---

## Diagram A: Acoustic Horizon at the B2 Fold

Updates S39 Diagram VII. The fold IS an acoustic horizon (Barcelo-Liberati-Visser),
with geometric temperature matching T_Gibbs to 0.7% [T-ACOUSTIC-40].

```
    m^2_B2(tau) NEAR THE FOLD                   ACOUSTIC LINE ELEMENT:
                                                 ds^2 = -dt^2 + (1/v_B2^2) dtau^2
    m^2                                          v_B2 = alpha*(tau - tau_fold)
    ^                                            = RINDLER PROFILE
    0.74 |                              .
         |                           .           m^2 = 0.7144 + (1/2)(1.987)(tau-0.190)^2
    0.72 |                    .                  quadratic residual: 3.0e-6
    0.715|          .  *  .                      dm/dtau at fold = 5.1e-18 (machine zero)
    0.714|  .          |          .
         +---------|---+---|----------|----> tau
         0.16    0.175  0.190  0.205    0.22
                         |
                    B2 FOLD (v_group = 0) [CASCADE-39]

    +-------------------------------------------+
    | Prescription   | T (M_KK) | T/T_Gibbs    |
    |----------------|----------|--------------|
    | Rindler        | 0.158    | 1.400  (40%) |
    | Acoustic metric| 0.112    | 0.993  (0.7%)|  <-- CORRECT
    | T_Gibbs        | 0.113    | 1.000        |
    +-------------------------------------------+
    kappa_a = sqrt(1.987)/2 = 0.705;  T_a = kappa_a/(2*pi) = 0.112 M_KK

    Rindler uses kappa_R = alpha/2 (constant acceleration).
    Acoustic metric uses kappa_a = sqrt(alpha)/2 (conformal factor from
    det(g_acoustic)). The fold is a dispersive medium, not a uniform
    accelerator. [Barcelo et al. 2005, T-ACOUSTIC-40]
```

**Caption**: The B2 fold is an acoustic horizon. The acoustic metric prescription
gives T_a/T_Gibbs = 0.993 with zero free parameters. Strongest quantitative
entry in the phonon-NCG dictionary: geometry determines thermodynamics.

---

## Diagram B: Substrate State Before / During / After Transit

The substrate principle (Einstein Addendum 1): particles are the substrate
changing its breathing pattern. Three phases of the SAME substrate.

```
    TIME ^
     |
     |  PHASE III: THERMAL SUBSTRATE (Gibbs)
     |  ==========================================
     |  || T=0.113 M_KK, S=6.701 bits [MASS-39] ||
     |  || 8 breathing frequencies [QRPA-40]:     ||
     |  || B1:1.632  B2:3.245  B3:1.894-2.096    ||
     |  || Effacement: 6,596x [FRIED-39]          ||
     |  || "The lattice vibrates at the same       ||
     |  ||  frequencies regardless of phonon mode" ||
     |  ==========================================
     |         ^ DEPHASING: t=0.922, 93.0%->89.1% B2, PR=3.17 [B2-DECAY-40, PAGE-40]
     |  PHASE II: GGE (frozen excitation pattern)
     |  ==========================================
     |  || B2: n=0.2325 x4 (93.1%)               ||
     |  || B1: n=0.0626 x1 (5.9%)                ||
     |  || B3: n=0.0025 x3 (1.0%)                ||
     |  || S_GGE=3.542 bits, S_ent=0 exact        ||
     |  || CC shift: 2.85e-6 of S_fold             ||
     |  || [CC-TRANSIT-40, ENT-39]                 ||
     |  ==========================================
     |         ^ PARKER CREATION: 59.8 qp pairs, backreaction 3.7% [S38 W3]
     |  PHASE I: BCS SUBSTRATE (breathing instanton gas)
     |  ==========================================
     |  || S_inst=0.069, Z_2 balance=0.998 [S37]  ||
     |  || omega_tau=8.27, Kapitza=0.030 [S38]     ||
     |  || Each nexus oscillates +/-Delta_0        ||
     |  || "The instanton gas IS the geometry"     ||
     |  ==========================================
```

**Caption**: Three states of the same substrate. The transit is not particle
motion through a fold but the substrate changing breathing patterns. CC shift
= 2.85e-6 of S_fold: the substrate is 99.9997% indifferent to its excitations.

---

## Diagram C: Fock Space -- The Compound Nucleus (S40 Update)

Updates S39 Diagrams V and VII. B2 quasi-integrable island fully characterized.

```
    +================================================================+
    |            256-STATE FOCK SPACE                                 |
    |  N=0   N=1        N=2            N=3          N=4              |
    |  d=1   d=8        d=28           d=56         d=70             |
    | +--+  +------+  +----------+  +----------+ +----------+       |
    | |  |  | B2   |  | WEAKLY   |  |          | | DENSEST  |       |
    | |  |  |ISLAND|  | CHAOTIC  |  |          | | SECTOR   |       |
    | |  |  |<r>=  |  | <r>=0.503|  | <r>=0.482| |          |       |
    | |  |  |0.401 |  |[INTEG-39]|  |          | |          |       |
    | |  |  |g_T=  |  +----------+  +----------+ +----------+       |
    | +--+  |0.087 |                                                 |
    |       |[B2-  |  B2 INTERNAL:                                   |
    |       |INTEG]|  V(B2,B2): 86% rank-1 / 14% anharmonic         |
    |       +------+  ||[S^2,H]||/norms = 0.022 [B2-INTEG-40]       |
    |                                                                |
    |  DEPHASING [B2-DECAY-40]:                                      |
    |  t=0: 93.0% --t=0.92--> 89.1% diagonal ensemble (permanent)   |
    |  Mechanism: incommensurate precession, NOT FGR (Naz 7x fast)   |
    |                                                                |
    |  QRPA [QRPA-40]: all omega^2>0, margin 3.1x, V_rem^odd=0     |
    |  97.5% EWSR in B2 collective (omega=3.245)                    |
    |  Near-resonance: omega_B2 ~ 2*omega_B1 (0.6%) -> 3-phonon    |
    +================================================================+
```

**Caption**: B2 is a near-integrable island (Poisson, g_T=0.087, 86% rank-1)
that dephases to 89.1% retention [B2-DECAY-40]. QRPA confirms local stability;
the omega_B2 ~ 2*omega_B1 near-resonance identifies the 3-phonon decay channel.

---

## Diagram D: 28D Moduli Landscape (HESS-40)

Updates S39 Diagram VI. Jensen fold = local minimum in ALL 22 tested directions.

```
    HESSIAN EIGENVALUE HIERARCHY AT tau = 0.190 [HESS-40]

    H=20233 |||||||||||||||||||||||||||||||||||||||||  diag u(2) rearrangement
    H=18396 |||||||||||||||||||||||||||||||||||||||    diag u(2) complement
    H=15893 |||||||||||||||||||||||||||||||||          Jensen tangent
    H=14225 ||||||||||||||||||||||||||||               diag complement splits
    H=10435 ||||||||||||||||||||||||                   off-diag su(2)-su(2)
    H= 4703 ||||||||||||||                             off-diag u(2)-compl [max]
    H= 3652 ||||||||||                                 off-diag su(2)-u(1)
    H= 2055 ||||||                                     off-diag compl-compl
    H= 1572 |||||   <--- SOFTEST (g_73: u(1)-complement mixing)
    --------|------------------------------------------------
    H=    0 |                                 INSTABILITY THRESHOLD

    22/22 positive. Condition number 12.87. Margin 1.57e7.

    Symmetry structure:
    HARDEST  (18k-20k): diagonal u(2) rearrangements
    MEDIUM   (14k-15k): complement internal
    SOFT      (2k-5k): off-diagonal cross-sector
    SOFTEST    (1572): u(1)-complement mixing -- still 10^7 above noise

    COMBINED: Along Jensen monotonic [SA-37] + transverse minimum [HESS-40]
              + BCS 6,596x [FRIED-39] + instanton 2-68x [CC-INST-38]
              + RPA wrong sign 93x [F.5-37]
              = 27 TOTAL CLOSURES. dim(equilibrium) = 0.
```

**Caption**: The dynamical matrix is positive definite in all 22 tested
transverse directions. The Jensen lattice geometry is mechanically stable.
27th equilibrium closure: no direction in 28D can trap the modulus [HESS-40].

---

## Diagram E: GSL -- The Impedance-Graded Channel

Updates S39 Diagram IV. Structural result: v_min = 0, all three entropy
terms individually non-decreasing [GSL-40].

```
    S (bits)
    ^
  10 |                                        .....S_total
     |                                  .....
     |                           .....
     |                    .....  S_condensate: 77% (+1.986 bits)
   8 |             .....
     |       .....
     |  ....   S_total at fold = 9.840 bits
     |
     |         S_particles: 22% (+0.565 bits)
   2 |         S_spectral:   1% (+0.025 bits)
     |
   0 +---|---------|---------|---------|----> tau
     0.10  0.143   0.190   0.235   0.30
           entry    fold    exit

    STRUCTURAL: v_min = 0. Zero negative steps / 499. [GSL-40]

    Acoustic interpretation: IMPEDANCE-GRADED CHANNEL
    tau=0.10 ======> tau=0.190 ======> tau=0.30
    Z_low ----------> Z_fold ----------> Z_high
                      (v=0)
    No reflecting interface. Waves pass through.
    [S32 Z_wall = 1/pi universality]

    GSL holds at ANY v > 0. Faster = more qp = more entropy.
    Bogoliubov unitarity: 2.2e-16 at all tau. [GSL-40]
```

**Caption**: The GSL is structural: all three terms non-decreasing for any
transit speed. In the acoustic picture, the BCS manifold is an impedance-graded
channel -- the fold (v=0) is an impedance extremum, not a reflective barrier.

---

## Diagram F: Energy Partition -- Substrate Indifference

Hawking's energy budget: 6,596:1 geometry-to-particles [FRIED-39].

```
    SPECTRAL ACTION GRADIENT          BCS PAIR CREATION
    |dS/dtau| = 58,723                |dE_BCS/dtau| = 8.90
    ||||||||||||||||||||||||||||||||    |
    ||||||||||||||||||||||||||||||||    |   ratio = 6,596x
    ||||||||||||||||||||||||||||||||    |
    S_fold = 250,360.677               E_cond = -0.156

    CC shift: delta_Lambda/S_fold = 2.85e-6 = 1 part in 350,000
    [CC-TRANSIT-40]

    SUBSTRATE PRINCIPLE [Einstein Addendum 1]:
    +-------------------------------------------------------+
    | Ratio 6,596 = substrate indifference.                  |
    | A phonon cannot hold the lattice in place.             |
    | Spectral action = substrate self-energy.               |
    | BCS = excitation energy. Effacement = 1/6596.          |
    | The substrate is 99.985% indifferent to excitations.   |
    +-------------------------------------------------------+

    CRANKING MASS INVERSION [M-COLL-40]:
    Expected: B2 dominates (93% condensate)
    Actual: B1 dominates (71% of M_ATDHFB=1.695)
    B2: v=0 + large gap (Delta/eps=2.44) --> suppressed
    B1: v!=0 + moderate gap --> controls inertia
    sigma_ZP=0.026 << delta_tau=0.09: CLASSICAL transit
```

**Caption**: Energy flows 6,596:1 into geometry over particles. The CC shift
is 1 part in 350,000. The cranking mass inversion (B1 controls inertia, not
B2) confirms the acoustic picture: nonzero velocity, not condensate weight,
determines collective inertia at the van Hove singularity [M-COLL-40].

---

## S40 Data Reference (additions to S39 table)

| Quantity | Value | Source |
|:---------|:------|:------|
| alpha_B2 | 1.9874 | T-ACOUSTIC-40 |
| T_a / T_Gibbs | 0.993 | T-ACOUSTIC-40 |
| `<r>` B2-only | 0.401 (Poisson) | B2-INTEG-40 |
| V(B2,B2) rank-1 | 86% | B2-INTEG-40 |
| B2 diagonal ensemble | 89.1% | B2-DECAY-40 |
| t_decay(B2) | 0.922 | B2-DECAY-40 |
| v_min (GSL) | 0 (structural) | GSL-40 |
| dL/S_fold | 2.85e-6 | CC-TRANSIT-40 |
| min H (Hessian) | +1572 | HESS-40 |
| M_ATDHFB | 1.695 (0.34x G_mod) | M-COLL-40 |
| sigma_ZP | 0.026 | M-COLL-40 |
| min(omega^2) QRPA | 2.665 | QRPA-40 |
| omega_B2 coll | 3.245 | QRPA-40 |
| PR | 3.17 | PAGE-40 |

---

*Grounded in S40 gates: T-ACOUSTIC-40, B2-INTEG-40, GSL-40, CC-TRANSIT-40,
HESS-40, QRPA-40, PAGE-40, B2-DECAY-40, M-COLL-40, SELF-CONSIST-40,
NOHAIR-40. Substrate principle: Einstein Addenda 1-2. Format: S39 Penrose
diagrams (Schwarzschild-Penrose).*
