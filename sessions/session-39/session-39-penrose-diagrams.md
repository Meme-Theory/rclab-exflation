# Penrose Diagrams for the Phonon-Exflation Modulus Space

**Author**: Schwarzschild-Penrose (schwarzschild-penrose-geometer)
**Date**: 2026-03-09
**Grounded in**: Session 39 results, Sessions 17-38 curvature data, Papers 01-10

Every number in these diagrams corresponds to a computed quantity. Every feature
corresponds to a proven structural result or a measured gate verdict. Sources are
cited in brackets after each quantity.

---

## Table of Contents

1. [Diagram I: Full Modulus-Space Conformal Diagram](#diagram-i)
2. [Diagram II: BCS Window Detail -- The Pair Creation Zone](#diagram-ii)
3. [Diagram III: White Hole Comparison](#diagram-iii)
4. [Diagram IV: Information Flow Through Transit](#diagram-iv)
5. [Diagram V: Fock Space Causal Structure](#diagram-v)
6. [Diagram VI: The 26-Closure Constraint Collapse](#diagram-vi)
7. [Diagram VII: B2 Spectral Horizon](#diagram-vii)
8. [Diagram VIII: Eigenvalue vs. Eigenstate Geometry](#diagram-viii)
9. [Data Reference Table](#data-reference-table)

---

<a name="diagram-i"></a>
## Diagram I: Full Modulus-Space Conformal Diagram

The modulus tau parametrizes the Jensen deformation of the internal SU(3) metric
(Paper 15, eq 3.68). The vertical axis is conformal time. The horizontal axis is
the modulus tau, conformally compactified so that tau -> infinity maps to a finite
boundary. Light cones at 45 degrees. The effective metric on the 1+1D
modulus-cosmology space is ds^2 = -dt^2 + G_mod * dtau^2, with G_mod = 5.0
[S36 modulus metric].

```
                         i+  (future timelike infinity)
                         /\
                        /  \
                       /    \
                      /      \
                     / GIBBS  \
                    / THERMAL  \
                   / S=6.70 b   \
                  / T=0.113 M_KK \      <-- post-thermalization endpoint
                 /   [MASS-39]    \         [INTEG-39, t_therm ~ 6 nat. units]
                /...................\    <-- THERMALIZATION BOUNDARY
               / t_therm/t_transit  \       (t ~ 5253 * t_transit after BCS exit)
              /    = 5,253 [W2-2]    \      [INTEG-39]
             /                        \
            / POST-TRANSIT GGE         \
           / S_ent = 0 (product state)  \   <-- S_GGE = 3.542 bits [ENT-39]
          / lambda: 1.46, 2.77, 6.01     \  <-- 3 distinct values [GGE-LAMBDA-39]
         /  [ENT-39, GGE-LAMBDA-39]       \
        /..................................\  <-- BCS WINDOW EXIT (tau ~ 0.235)
       /     BCS WINDOW                    \     [CASCADE-39, width 0.092]
      /  59.8 qp pairs created             \
     /   dwell = 3.0e-4 [FRIED-39]         |
    /    |dS/dtau| = 58,723 [FRIED-39]     |
   / ====*=========*===============*======= |  <-- FOLD tau=0.190 [CASCADE-39]
  /  BCS WINDOW ENTRY (tau ~ 0.143)        |      M_max=1.684 at tau=0.194
  |  [CASCADE-39, 1 contiguous island]     |
  |                                        |
  |   DNP CROSSING ---- tau = 0.285 ------+|  <-- TT-stability boundary [SP-5]
  |   g_FS PEAK -------- tau = 0.280 -----+|  <-- eigenstate geometry [FS-METRIC-39]
  |                                        |
  |   BCS WELL (Jensen saddle) --- 0.35 --+|  <-- 2/4 Hessian eig negative [S29]
  |                                        |
  |        NEC VIOLATION ---- tau=0.778 --+|  <-- su(2) Ricci eigenvalue = 0
  |        [S17b, S22a SP-5]              ||      Penrose theorem blocked
  |                                       ||
  |                                       ||
  |     ////// KASNER SINGULARITY //////  ||  <-- K(tau) -> inf as tau -> inf
  |     // K = (1/12)e^{4*tau} + ...  //  ||      genuine curvature singularity
  |     // [SP-2, K monotonic K'>0]   //  ||      spacelike (all timelike geodesics
  |     ////////////////////////////////  ||      reach it in finite proper time)
  |                                       ||
   \                                      /
    \                                    /
     \                                  /
      \                                /
       \       ROUND METRIC           /
        \      tau = 0               /
         \   K = 0.500 [SP-2]      /
          \ |C|^2 = 5/14 [SP-2]  /   <-- WCH minimum (conformally flattest)
           \  R = 2.000         /        DNP-unstable [SP-5]
            \  NEC HOLDS       /         ALL directions repulsive
             \                /
              \              /
               \            /
                \          /
                 \        /
                  \      /
                   \    /
                    \  /
                     \/
                     i-  (past timelike infinity)
```

### Legend

| Symbol | Meaning | Source |
|:-------|:--------|:------|
| `i+` | Future timelike infinity | Paper 03 |
| `i-` | Past timelike infinity | Paper 03 |
| `====*====` | Van Hove fold (eigenvalue minimum) | CASCADE-39 |
| `...........` | Thermalization boundary (GGE -> Gibbs) | INTEG-39 |
| `//////` | Genuine curvature singularity | SP-2 |
| `---+` | Feature at specific tau value | Various |

### Physical Interpretation

The modulus tau starts near i- (the initial state, close to the round metric
at tau = 0) and is expelled by the DNP instability toward increasing tau.
The trajectory is ballistic: the spectral action gradient |dS/dtau| = 58,723
at the fold [FRIED-39] dominates the BCS condensation energy gradient of 8.90
by a factor of 6,596x. No trapping occurs (FRIED-39 FAIL, 26th closed mechanism).

The modulus passes through the BCS window (tau in [0.143, 0.235], CASCADE-39 PASS)
in a dwell time of 3.0e-4 natural units. During this transit, 59.8 quasiparticle
pairs are created (S38 W3, Parker-type production). The post-transit state is a
GGE with S_ent = 0 exactly (product state, ENT-39). This GGE thermalizes to a
Gibbs state in t_therm ~ 6 natural units (INTEG-39 FAIL), erasing 3.159 bits
of transit information.

The Kasner singularity at tau -> infinity is a genuine curvature singularity
(K -> infinity, spacelike), but it is dynamically inaccessible: the transit
physics is complete long before the modulus reaches it. The NEC violation
boundary at tau = 0.78 [SP-5] blocks the Penrose singularity theorem (Paper 04)
from applying to the tau > 0.78 region.

---

<a name="diagram-ii"></a>
## Diagram II: BCS Window Detail -- The Pair Creation Zone

Zoomed into the BCS-active region tau in [0.143, 0.235]. The effective 1+1D
metric is ds^2 = -dt^2 + G_mod * dtau^2 with G_mod = 5.0. The transit speed
at the fold is |dtau/dt| = 26.545 [S36], giving a transit time through the
full BCS window of t_transit ~ 0.092 / 26.545 = 3.5e-3 natural units.

```
    tau = 0.235  (BCS exit)
    |
    |  B1 VH ----- tau = 0.231, M_max(cal) = 1.509 [CASCADE-39]
    |  |           lambda_B1 = 0.818 [CASCADE-39]
    |  |           DOS_B1 = 29.97 (35.6x enhancement) [CASCADE-39]
    |  |
    |  |   BCS ACTIVE REGION (M_max > 1 island, width 0.092)
    |  |   +-------------------------------------------------+
    |  |   |                                                 |
    |  |   |  rho_B2 = 14.02 (van Hove DOS) [S35a]          |
    |  |   |  V_Kosmann(B2,B2) = 0.1557 (Schur) [S34]       |
    |  |   |  E_cond = -0.1557 [FRIED-39]                   |
    |  |   |  Delta_0 = 0.7704 (GL gap) [SCHWING-PROOF-39]  |
    |  |   |  S_inst = 0.069 (dense gas) [S37]              |
    |  |   |                                                 |
    |  |   |        PAIR CREATION ZONE                       |
    |  |   |        ~~~~~~~~~~~~~~~~~~~                      |
    |  |   |   n_B2 = 0.2396  (4 modes) --+                 |
    |  |   |   n_B1 = 0.0363  (1 mode)  --+-- 59.8 qp pairs|
    |  |   |   n_B3 = 0.0017  (3 modes) --+   [S38 W3]     |
    |  |   |                                                 |
    |  |   |   BdG mass enhancement:                         |
    |  |   |   B2: 49.4x  B1: 4.3x  B3: 1.2x [GEOD-39]    |
    |  |   |                                                 |
    |  |   |        K = 0.5346 [SP-2]                        |
    |  |   |   |C|^2 = 0.3859 [SP-2]                        |
    |  |   |   72.2% Weyl, 27.2% scalar [SP-2 Bianchi]      |
    |  |   |                                                 |
    |  *===|========= B2 FOLD =============*==========*      |  tau = 0.190
    |  |   |  dE_B2/dtau = 0 (van Hove)    |          |      |  [CASCADE-39]
    |  |   |  d^2E_B2/dtau^2 = +0.85       |          |      |
    |  |   |  (minimum type) [CASCADE-39]   |          |      |
    |  |   |                                |          |      |
    |  |   |  BALLISTIC TRANSIT             |          |      |
    |  |   |  |v| = 26.545 [S36]           |          |      |
    |  |   |  dwell = 3.0e-4 [FRIED-39]    |          |      |
    |  |   |  Gradient ratio: 6,596x        |          |      |
    |  |   |  [FRIED-39]                    |          |      |
    |  |   |                                |          |      |
    |  |   |  GGE FORMATION                 |          |      |
    |  |   |  (instantaneous on transit     |          |      |
    |  |   |   timescale)                   |          |      |
    |  |   |  lambda_B2 = 1.459 (x4)       |          |      |
    |  |   |  lambda_B1 = 2.771 (x1)       |   Pair   |      |
    |  |   |  lambda_B3 = 6.007 (x3)       | creation | Post-|
    |  |   |  [GGE-LAMBDA-39]              |  zone    |transit|
    |  |   |                                |          |      |
    |  |   +-------------------------------------------------+
    |  |
    |  |   B2 GEOMETRIC PROTECTION BOUNDARY
    |  |   Xi correction vanishes within B2 (Schur)
    |  |   Casimir preserved to 3e-16 at ALL tau [LIED-39]
    |  |   = Birkhoff rigidity for the B2 quartet
    |  |
    |
    tau = 0.143  (BCS entry)
```

### Physical Interpretation

The BCS window is a single contiguous island of M_max > 1, centered on the B2
van Hove fold at tau = 0.194 [CASCADE-39]. The B1 branch has a secondary van Hove
singularity at tau = 0.231, but within the same island (no separation). B3 is
monotone increasing (no van Hove). The modulus transits through this entire
window in 3.0e-4 natural units [FRIED-39], during which 59.8 quasiparticle pairs
are created via Parker-type production [S38 W3].

The B2 geometric protection boundary (LIED-39 PASS) is not a localized feature:
it holds at ALL tau by Schur's lemma. The B2 quartet pairing structure is
Birkhoff-rigid -- no geometric correction can modify it. The BCS condensation
energy E_cond = -0.1557 is negligible compared to the spectral action value
(~250,000 at the fold), producing the gradient ratio of 6,596x that makes
trapping impossible.

---

<a name="diagram-iii"></a>
## Diagram III: White Hole Comparison

Side-by-side comparison: the standard Schwarzschild white hole (Kruskal Region IV,
Paper 07) and the exflation transit. The white hole analogy was originated in the
framework mechanism discussion and endorsed by Hawking (S39 addendum).

```
    SCHWARZSCHILD WHITE HOLE               EXFLATION TRANSIT
    (Kruskal Region IV)                    (Modulus space)
    Paper 07                               Sessions 37-39

             i+                                     i+
            /  \                                   /  \
           /    \                                 /    \
          / I+   \                               / GIBBS\
         / (null  \                             / T=0.113\
        / infinity)\                           / [MASS-39]\
       /............\                         /............\
      / EVENT        \                       / THERM BNDRY  \
     / HORIZON        \                     / t/t_tr = 5253  \
    / (null surface    \                   /  [INTEG-39]      \
   /  r = 2M)          \                 /                     \
  |                      |               |   GGE (PRODUCT STATE) |
  |  Region I            |               |   S_ent = 0 [ENT-39]  |
  |  (exterior)          |               |   3 distinct lambdas   |
  |                      |               |   [GGE-LAMBDA-39]      |
  |  Particles           |               |                        |
  |  emitted             |               |   59.8 qp pairs        |
  |  with thermal        |               |   emitted with         |
  |  spectrum            |               |   ANTI-THERMAL spectrum |
  |  T = kappa/(2pi)     |               |   (Parker, corr=+0.74) |
  |  [Paper 05]          |               |   [S29, S38 W3]        |
  |                      |               |                        |
   \                    /                 \   BCS WINDOW          /
    \ PAST HORIZON     /                   \ (pair creation      /
     \ (null surface) /                     \  zone)            /
      \              /                       \                 /
       \            /                         \               /
        \          /                           \             /
    /////\////////\/////                   =====\===========/ tau=0.190
    // PAST SINGULARITY //                 ROUND METRIC (tau=0)
    // (spacelike,      //                 WCH minimum
    //  r = 0,          //                 |C|^2 = 5/14 [SP-2]
    //  K = 48M^2/r^6   //                K = 0.500 [SP-2]
    //  -> infinity)    //                 DNP-UNSTABLE
    // [Paper 01 eq 21] //                 (all directions repulsive)
    //////////////////////                 [SP-5, tau in [0, 0.285]]
```

### Structural Comparison Table

| Property | White Hole | Exflation Transit | Source |
|:---------|:-----------|:------------------|:-------|
| Past singularity | r=0, K->inf (genuine) | tau=0, K=0.500 (regular) | Paper 01, SP-2 |
| Horizon | Past null surface (r=2M) | None | Paper 07 |
| Emission | Thermal (Planckian) | Anti-thermal (Parker) | Paper 05, S29 |
| S_ent of emitted state | Maximal (entangled with interior) | Zero (product state) | Paper 05, ENT-39 |
| Subsequent thermalization | N/A (already thermal) | t_therm ~ 6 [INTEG-39] | INTEG-39 |
| Information | Lost behind horizon | Locally preserved, then redistributed | ENT-39 |
| Energy condition | NEC satisfied (vacuum) | NEC violated at tau=0.78 | Paper 04, SP-5 |
| Mechanism | Time-reversed collapse | DNP instability ejection | SP-5, S22a |

### Physical Interpretation

The exflation transit shares the DYNAMICAL signature of a white hole: an unstable
initial state (tau = 0, DNP-repulsive; cf. past singularity) ejects matter into
an expanding region. The emitted state is a product (S_ent = 0, ENT-39),
matching the white hole's coherent emission (no tracing over a horizon). The key
difference: the white hole has a past horizon (null surface) while the modulus
space has no null structure. The white hole emits thermally; the transit emits
anti-thermally (Parker-type, spectral correlation r = +0.74, S29). Subsequent
thermalization via broken integrability (INTEG-39) produces a thermal endpoint
through a mechanism with no analog in the white hole: chaotic mixing in the
13% non-separable coupling channel of V_phys.

The "past singularity" at tau = 0 is geometrically REGULAR: K(0) = 0.500
(finite Kretschner scalar), |C|^2(0) = 5/14 (Weyl curvature at its WCH minimum).
The repulsion is not gravitational (no curvature singularity) but
representation-theoretic: the round SU(3) metric is an unstable fixed point of
the DNP flow (all TT perturbations grow exponentially for tau < 0.285, SP-5).

---

<a name="diagram-iv"></a>
## Diagram IV: Information Flow Through Transit

The flow of information (measured in bits) through the three phases: pre-transit,
transit, and post-transit. Time flows upward. Width represents entropy.

```
    TIME
     ^
     |
     |      Phase III: GIBBS THERMAL EQUILIBRIUM
     |      ==========================================
     |      ||                                      ||
     |      ||  S_Gibbs = 6.701 bits [ENT-39]       ||
     |      ||  T = 0.113 M_KK [MASS-39]            ||
     |      ||  beta = 8.872 [MASS-39]               ||
     |      ||  Determined by 2 conserved quantities: ||
     |      ||    E = 1.689, N_pair = 1 [GGE-LAMBDA] ||
     |      ||  I(pre:post) ~ 0                      ||
     |      ||  Information REDISTRIBUTED (not lost)  ||
     |      ||  Unitarity preserved within 256 states ||
     |      ==========================================
     |                      ^
     |            THERMALIZATION TRANSITION
     |            Brody beta = 0.633 [INTEG-39]
     |            Thouless g_T = 0.60 [INTEG-39]
     |            Gamma_FGR = 0.168 [INTEG-39]
     |            t_therm ~ 6 natural units
     |            Delta_S = +3.159 bits [ENT-39]
     |            (irreversible entropy production)
     |                      ^
     |      Phase II: GGE (PRODUCT STATE)
     |      ================================
     |      ||                            ||
     |      ||  S_GGE = 3.542 bits        ||
     |      ||  S_ent = 0.000 (exact)     ||
     |      ||  [ENT-39]                  ||
     |      ||                            ||
     |      ||  3 distinct lambda_k:      ||
     |      ||  B2: 1.459 (x4, 93.0%)    ||
     |      ||  B1: 2.771 (x1,  6.3%)    ||
     |      ||  B3: 6.007 (x3,  0.7%)    ||
     |      ||  [GGE-LAMBDA-39]           ||
     |      ||                            ||
     |      ||  Anti-thermal: p_B2 > p_B1 ||
     |      ||  despite E_B2 > E_B1       ||
     |      ||  T_eff(B1-B2) = -0.040     ||
     |      ||  [GGE-LAMBDA-39]           ||
     |      ||                            ||
     |      ||  rho_GGE = tensor product  ||
     |      ||  of single-mode states     ||
     |      ||  (mode-diagonal Bogoliubov)||
     |      ================================
     |                      ^
     |            PAIR CREATION (PARKER-TYPE)
     |            59.8 quasiparticle pairs [S38 W3]
     |            n_B2 = 0.2396, n_B1 = 0.0363
     |            n_B3 = 0.0017 [RG-39]
     |            Backreaction 3.7% (perturbative)
     |            No horizon, no tracing
     |                      ^
     |      Phase I: BCS GROUND STATE
     |      ====================
     |      ||                ||
     |      ||  S = 0         ||
     |      ||  (pure state)  ||
     |      ||  N_pair = 1    ||
     |      ||  [RG-39]       ||
     |      ||  B2 weight:    ||
     |      ||   93.0%        ||
     |      ||  [RG-39]       ||
     |      ====================
     |
```

### Information Budget

| Quantity | Value (bits) | Source |
|:---------|:-------------|:------|
| S(pre-transit BCS ground state) | 0.000 | Pure state |
| S(post-transit GGE) | 3.542 | ENT-39 |
| Delta_S (pair creation) | +3.542 | ENT-39 |
| S(post-thermalization Gibbs) | 6.701 | ENT-39 |
| Delta_S (thermalization) | +3.159 | ENT-39 |
| Total S increase | +6.701 | Sum |
| Entanglement at GGE | 0.000 | ENT-39 (product state) |
| Entanglement at Gibbs | 0.065 | ENT-39 (weak classical corr.) |
| Bayes factor GGE vs Gibbs | 3.17 | BAYES-39 |
| D_KL(GGE, Gibbs_opt) | 0.669 bits | BAYES-39 |

### Physical Interpretation

Information flows in one direction only: from ordered to disordered. The BCS
ground state (S = 0) generates a GGE (S = 3.542 bits) through Parker-type pair
creation, then the GGE thermalizes to a Gibbs state (S = 6.701 bits) through
chaotic mixing in the non-separable V channel. The first transition creates
diagonal (classical) entropy with zero entanglement. The second transition
creates both additional diagonal entropy and weak inter-mode correlations
(I = 0.065 bits).

The total information erasure is 6.701 bits -- every bit of structure in the
BCS ground state is eventually lost to thermal noise. This is the "spectral
Bekenstein-Hawking entropy" of the transit process.

Crucially, information is never LOST in the Hawking sense (no tracing over
inaccessible degrees of freedom). It is REDISTRIBUTED within the same 256-state
Hilbert space. Unitarity is preserved at all times.

---

<a name="diagram-v"></a>
## Diagram V: Fock Space Causal Structure

The 256-state Fock space has its own effective geometry, revealed by the level
statistics computed in INTEG-39. The N_pair sectors partition the Hilbert space
into shells. The Brody parameter beta measures the transition from integrable
(Poisson, beta = 0) to chaotic (GOE, beta = 1).

```
         N_pair = 0          N_pair = 1       N_pair = 2       N_pair = 3       N_pair = 4
         dim = 1             dim = 8          dim = 28         dim = 56         dim = 70
         <r> = N/A           <r> = 0.497      <r> = 0.503      <r> = 0.482      <r> = 0.505
         TRIVIAL             INTERMEDIATE     GOE              INTERMEDIATE     GOE (densest)
                                                                                g_T = 0.60

    +---+   +--------+   +------------------+   +--------------------+   +---------------------+
    | 1 |   | 8      |   | 28               |   | 56                 |   | 70                  |
    | . |   | states |   | states           |   | states             |   | states              |
    |   |   |        |   |                  |   |                    |   |                     |
    | P |   | I      |   | G  <-- CHAOTIC   |   | I                  |   | G  <-- MOST CHAOTIC |
    | o |   | n      |   | O      SEA       |   | n                  |   | O      (dim=70,     |
    | i |   | t      |   | E                |   | t                  |   | E      beta~0.8)    |
    | s |   | e      |   |                  |   | e                  |   |                     |
    | s |   | r      |   | level repulsion  |   | r                  |   | level repulsion     |
    | o |   | m      |   | V_rms = 0.0447   |   | m                  |   | Gamma_FGR = 0.168   |
    | n |   | e      |   | [INTEG-39]       |   | e                  |   | [INTEG-39]          |
    | . |   | d      |   |                  |   | d                  |   |                     |
    +---+   | i      |   +------------------+   | i                  |   +---------------------+
            | a      |                          | a                  |
            | t      |                          | t                  |
            | e      |                          | e                  |
            +--------+                          +--------------------+

         N_pair = 5       N_pair = 6       N_pair = 7       N_pair = 8
         dim = 56         dim = 28         dim = 8          dim = 1
         <r> = 0.488      <r> = 0.421      <r> = 0.338      <r> = N/A
         INTERMEDIATE     NEAR-POISSON     POISSON           TRIVIAL

    +--------------------+   +------------------+   +--------+   +---+
    | 56                 |   | 28               |   | 8      |   | 1 |
    | states             |   | states           |   | states |   | . |
    |                    |   |                  |   |        |   |   |
    | I                  |   | N  <-- NEARLY    |   | P      |   | P |
    | n                  |   | e      INTEGRABLE|   | o      |   | o |
    | t                  |   | a                |   | i      |   | i |
    | e                  |   | r                |   | s      |   | s |
    | r                  |   | -                |   | s      |   | s |
    | m                  |   | P                |   | o      |   | o |
    | e                  |   | o                |   | n      |   | n |
    | d                  |   | i                |   |        |   | . |
    | i                  |   | s                |   +--------+   +---+
    | a                  |   | s                |
    | t                  |   | o                |
    | e                  |   | n                |
    +--------------------+   +------------------+

    <-- EDGE (sparse, integrable) ------- CENTER (dense, chaotic) ------- EDGE (sparse, integrable) -->

    CAUCHY HORIZON INSTABILITY PATTERN:
    The perturbation (13% non-separable V_phys) is strongest where the
    level density is highest (N=2,4: dim=28,70), weakest at the sparse
    edges (N=6,7: dim=28,8). This mirrors the blueshift instability
    at a Cauchy horizon (Paper 05, Sec 4.3): perturbations amplified
    where the spectral density concentrates.
```

### Legend

| Symbol | Meaning | Source |
|:-------|:--------|:------|
| GOE | Gaussian Orthogonal Ensemble statistics | INTEG-39 |
| Poisson | Poisson statistics (integrable) | INTEG-39 |
| Intermediate | Between Poisson and GOE | INTEG-39 |
| g_T | Thouless conductance | INTEG-39 |
| V_rms | RMS perturbation matrix element | INTEG-39 |
| Gamma_FGR | Fermi Golden Rule decay rate | INTEG-39 |

### Physical Interpretation

The Fock space has a "causal structure" defined by the level statistics: the
central sectors (N = 2-5, dim = 28-70) are in the chaotic regime (GOE-like
level repulsion), while the edge sectors (N = 6-8, dim = 8-28) retain approximate
integrability (Poisson statistics). This pattern -- chaos at the center,
integrability at the edges -- is the spectral analog of a Cauchy horizon
instability (Paper 05, Sec 4.3).

The GGE state lives in the N_pair = 1 sector (dim = 8), which is in the
INTERMEDIATE regime (<r> = 0.497). The thermalization pathway proceeds through
the non-separable coupling V into the chaotic central sectors, where level
repulsion mixes the populations irreversibly. The Thouless conductance g_T = 0.60
at the center measures the rate of this mixing: it is at the metal-insulator
transition, not deep in the chaotic regime.

---

<a name="diagram-vi"></a>
## Diagram VI: The 26-Closure Constraint Collapse

Einstein (S39 collab) identified that the full moduli space for left-invariant
metrics on SU(3) is 28-dimensional: dim(GL(8,R)/O(8)) = 28 independent metric
components. The Jensen trajectory is a 1D submanifold. All 26 closures live
on this 1D trajectory. The constraint map collapses from the full 28D space
to a single surviving trajectory: ballistic transit.

```
    THE CONSTRAINT COLLAPSE
    (28D moduli space -> 0D equilibrium, 1D transit trajectory)

    DIMENSION   WHAT IS CONSTRAINED                            SESSION

    dim = 28    Full space of left-invariant metrics on SU(3)  [Einstein S39]
       |        (GL(8,R)/O(8) independent components)
       |
       |------> Jensen reduction: SO(8) -> U(2) symmetry       [Paper 15 eq 3.68]
       |        RESTRICTS TO 1D SUBMANIFOLD
       v
    dim = 1     Jensen trajectory tau in [0, infinity)
       |
       |        26 MECHANISMS CLOSED ON THIS LINE:
       |
       |   S17a  V_tree minimum (no extremum)                  ------+
       |   S18   1-loop Coleman-Weinberg                       ------+
       |   S19d  Casimir scalar+vector                         ------+
       |   S20b  Casimir with TT 2-tensors (constant-ratio)   ------+-- PERTURBATIVE
       |   S20a  Seeley-DeWitt a_2/a_4                         ------+   (all monotone
       |   S19d  Spectral back-reaction                        ------+    by theorem)
       |   S19a  Fermion condensate                            ------+
       |   S17c  Pfaffian Z_2                                  ------+
       |   S19b  Single-field slow-roll                        ------+
       |   S22b  Inter-sector coupled delta_T                  ------+-- BLOCK-DIAGONAL
       |   S22b  Inter-sector coupled V_IR                     ------+   (Birkhoff rigidity)
       |   S22c  Higgs-sigma portal (Trap 3)                   ------+
       |   S22d  Rolling quintessence (clock, 15,000x)         ------+-- OBSERVATIONAL
       |   S22d  DESI dynamical DE                             ------+
       |   S22c  Stokes phenomenon                             ------+
       |   S23a  Gap-edge self-coupling (Trap 1)               ------+-- PAIRING
       |   S24a  V_spec monotone (a_4/a_2=1000:1)             ------+
       |   S24a  Neutrino R from H_eff                         ------+
       |   S24a  Eigenvalue ratio phi in singlet               ------+
       |   S34   Canonical mu!=0 (PH forces mu=0)             ------+-- CHEMICAL
       |   S34   Grand canonical mu!=0                         ------+   POTENTIAL
       |   S37   Cutoff spectral action (structural monotonic) ------+-- SPECTRAL ACTION
       |   S37   One-loop RPA self-trapping (wrong sign)       ------+   (theorem-level)
       |   S37   (B1,B3,G1) PMNS triad (algebraic)            ------+
       |   S38   CC-through-instanton (76x margin)             ------+-- INSTANTON
       |   S39   Friedmann-BCS (133,200x shortfall)            ------+-- FRIEDMANN
       |                                                                  (FINAL)
       v
    dim = 0     EQUILIBRIUM: NO SURVIVING MECHANISM

    BUT:

    dim = 1     TRANSIT: The ballistic free-fall trajectory
                survives. Pair creation occurs during transit
                (59.8 qp pairs). Post-transit thermalizes.
                This is not a choice but a necessity:
                the constraint map leaves no alternative.


    SURVIVING SOLUTION SPACE TOPOLOGY:

    +----------------------------------------------------------+
    |                                                          |
    |  Before S39:  ~~~~~~ (1D curve with possible traps)      |
    |                                                          |
    |  After S39:   ------> (1D ballistic trajectory,          |
    |                        no traps, no stable orbits)       |
    |                                                          |
    |  Analogy: Schwarzschild radial geodesics                 |
    |           No stable circular orbits inside r = 6M        |
    |           (ISCO). Below ISCO, only infall.               |
    |           Here: no stable tau anywhere.                  |
    |           Only transit. [Paper 01 eq 43]                 |
    |                                                          |
    +----------------------------------------------------------+
```

### Physical Interpretation

The 26 closures are not failures -- they are constraints that define the walls of
the solution space. Each closure eliminates a region where equilibrium stabilization
was possible. After all 26, the equilibrium subspace has dimension zero: no
mechanism exists for holding the modulus at any fixed tau.

The surviving solution is 1-dimensional: the ballistic transit trajectory
determined by the spectral action gradient. This is analogous to the
Schwarzschild effective potential (Paper 01, eq 43): below the ISCO at r = 6M,
there are no stable circular orbits -- only infall. Here, the spectral action
potential has no minimum on the Jensen line (structural monotonicity theorem,
S37), so there are no stable "orbits" -- only transit.

Einstein identifies 27 unexplored transverse directions in the 28D moduli space.
The off-Jensen Hessian at the fold remains uncomputed (his Q1). If tachyonic
transverse modes exist, the 1D picture could break down entirely. This is the
single identified structural escape from the transit-only conclusion.

---

<a name="diagram-vii"></a>
## Diagram VII: B2 Spectral Horizon

The B2 quartet (4 modes) is exactly integrable within its own subspace
(LIED-39 PASS: Schur's lemma forces rank-1 separability). The full 8-mode
system is NOT integrable (INTEG-39 FAIL: 13% non-separable V). The question:
does B2 form a "spectral horizon" -- a protected region of Fock space where
the GGE persists despite surrounding thermalization?

```
                    FULL 8-MODE FOCK SPACE (dim = 256)
    +================================================================+
    |                                                                |
    |                    CHAOTIC SEA                                 |
    |              (GOE statistics, beta ~ 0.7)                      |
    |              (t_therm ~ 6 natural units)                       |
    |              [INTEG-39]                                        |
    |                                                                |
    |     B1 mode        +-----------------------+     B3 modes      |
    |     (1 mode)       |                       |     (3 modes)     |
    |     lambda = 2.771 |   B2 QUARTET          |     lambda = 6.007|
    |     p = 0.063      |   (4 modes)           |     p = 0.0025   |
    |     [GGE-LAMBDA]   |                       |     [GGE-LAMBDA]  |
    |                    |   lambda = 1.459 (x4) |                   |
    |     ||V(B1,B2)||   |   p = 0.2325 (x4)    |   ||V(B2,B3)||    |
    |     = 0.299        |   S_B2 = 3.129 bits   |   max = 0.099    |
    |     [GEOD-CONST]   |   (88.4% of S_GGE)   |   [GEOD-CONST]   |
    |                    |   [ENT-39]            |                   |
    |   <------coupling-->|                       |<--coupling-----> |
    |                    |   INTEGRABLE CORE      |                   |
    |                    |   V(B2,B2) = rank-1   |                   |
    |                    |   (Schur's lemma)      |                   |
    |                    |   [LIED-39 PASS]       |                   |
    |                    |                       |                   |
    |                    |   C_2 = 0.1557 [S34]  |                   |
    |                    |   Xi vanishes [LIED-39]|                   |
    |                    |   Birkhoff-rigid       |                   |
    |                    +-----------+-----------+                   |
    |                                |                               |
    |                    SPECTRAL    |                               |
    |                    HORIZON?    |                               |
    |                                v                               |
    |                    Does B2 GGE survive                         |
    |                    when B1/B3 thermalize?                      |
    |                    [OPEN QUESTION Q3]                          |
    |                                                                |
    +================================================================+

    KEY NUMBERS:

    | Subsystem | Integrable? | Coupling to B2 | GGE weight | Entropy |
    |:----------|:------------|:---------------|:-----------|:--------|
    | B2 (x4)  | YES (Schur) | --             | 93.0%      | 3.13 b  |
    | B1 (x1)  | trivial     | ||V||=0.299    |  6.3%      | 0.34 b  |
    | B3 (x3)  | approx      | ||V||=0.099    |  0.7%      | 0.07 b  |
    | Full 8   | NO          | --             | 100%       | 3.54 b  |

    THERMALIZATION SCENARIO:

    Time = 0:  B2 GGE (lambda=1.459 x4) + B1 GGE (2.771) + B3 GGE (6.007)
               S = 3.542 bits, S_ent = 0 (product state)

    Time ~ 6:  Full thermalization via B1/B3 coupling
               S = 6.701 bits, T = 0.113 M_KK
               [INTEG-39]

    Time ~ ?:  Does B2 reach thermal equilibrium LATER than B1/B3?
               If t_therm(B2) >> t_therm(full), the B2 sector
               retains 3.129 bits of transit information while
               the rest has thermalized.
               [UNCOMPUTED -- requires B2-restricted Thouless g_T]
```

### Physical Interpretation

The B2 quartet occupies a unique position: it is the dominant carrier of transit
information (93% of GGE weight, 88.4% of GGE entropy) and it is exactly
integrable within its own subspace (Schur's lemma, LIED-39 PASS). The coupling
to B1 (||V|| = 0.299) and B3 (||V|| max = 0.099) is the only channel through
which B2 can thermalize. This coupling is the analog of radiation leaking through
a partially transparent horizon.

If the B2-restricted Thouless conductance is small (g_T << 1), the B2 sector
is effectively behind a "spectral horizon": the integrability acts as a causal
barrier, protecting the B2 GGE from the surrounding chaos. The B2 information
(3.129 bits) would persist as a long-lived quasi-stationary state even as the
full system thermalizes.

This is Hawking's Q2 (S39 collab) and Einstein's Q3: the B2 subsystem
thermalization rate determines whether any non-thermal character persists after
the full-system thermalization time.

---

<a name="diagram-viii"></a>
## Diagram VIII: Eigenvalue vs. Eigenstate Geometry

Session 39 reveals that eigenvalue geometry and eigenstate geometry mark two
DISTINCT geometric events on the modulus space. This is a structural separation
not anticipated by any session prior to S39.

```
    tau
    ^
    |
    0.50 |
         |
    0.40 |                                              B3 monotone increasing
         |                                              (no VH) [CASCADE-39]
    0.35 |  BCS well (Jensen saddle, 2/4 Hessian neg.) [S29]
         |
    0.30 |
         |               DNP crossing (TT stability) ---- tau = 0.285 [SP-5]
         |                        +
    0.28 |            g_FS peak ------+------------------- tau = 0.280 [FS-METRIC-39]
         |                2% gap  |
         |                        |
    0.25 |                        |       g_FS = 0.159 [FS-METRIC-39]
         |                        |
         |     BCS WINDOW EXIT ---+----------------------- tau = 0.235 [CASCADE-39]
    0.23 |          B1 VH --------+----------------------- tau = 0.231 [CASCADE-39]
         |                        |
    0.20 |                        |
         |                        |       g_FS = 0.156 (slow variation)
         |    ****B2 FOLD**** ----+----------------------- tau = 0.190 [CASCADE-39]
    0.19 |   (dE_B2/dtau = 0)     |                       (eigenvalue extremum)
         |                        |
         |     BCS WINDOW ENTRY --+----------------------- tau = 0.143 [CASCADE-39]
    0.14 |                        |
         |                        |       g_FS = 0.151
    0.10 |                        |
         |
    0.00 +----+----+----+----+----+-----> g_FS
         0.14  0.15 0.155 0.16  0.165

              <--- g_FS profile --->
              Smooth, 5% total variation
              100% from B2+/B2- transitions
              Berry curvature F = 0 (identically)
              g_FS proportional to identity (Schur)
              [FS-METRIC-39]

    TWO DISTINCT GEOMETRIC EVENTS:

    (1) tau = 0.190: EIGENVALUE GEOMETRY
        dE_B2/dtau = 0 (van Hove singularity)
        BCS window, pair creation, M_max = 1.684
        K = 0.5346, |C|^2 = 0.3859
        Petrov type: D -> II transition [MEMORY]
        This is WHERE condensation happens.

    (2) tau = 0.280: EIGENSTATE GEOMETRY
        g_FS maximum (eigenstate rotation rate maximal)
        2% from DNP TT-stability crossing at 0.285
        Eigenstate = maximally non-adiabatic
        Internal metric transitions: TT-unstable -> TT-stable
        Berry curvature F = 0 (pure gauge)
        This is WHERE the perturbative stability changes.

    INTERPRETATION:
    The two events are connected by the SU(3) representation theory
    but are NOT causally related in the 1+1D effective spacetime.
    The fold (0.190) is inside the DNP-unstable region (tau < 0.285).
    The g_FS peak (0.280) marks the boundary of that region.
    The BCS physics occurs in the unstable regime;
    the stability transition occurs 47% later in tau.
```

### Physical Interpretation

The Fubini-Study metric g_FS measures how rapidly the eigenstates of D_K rotate
as tau varies. It peaks at tau = 0.280, NOT at the fold (tau = 0.190). This is
because g_FS is controlled by the particle-hole gap (~1.69, tau-independent),
not by the inter-branch gaps that create the van Hove singularity. Symmetry
forces all B2-B1 and B2-B3 matrix elements to vanish (FS-METRIC-39); g_FS
sees only the internal B2+/B2- structure.

The 2% proximity to the DNP crossing (0.280 vs 0.285) demands an invariant
characterization (Open Question Q2 from the collab review). If the Petrov type
transitions at this locus (analogous to the Petrov D -> II transition at the
dump point, MEMORY), the coincidence is structural. The Goldberg-Sachs theorem
(Paper 08, Sec 12.1) states that algebraically special vacuum spacetimes have
shear-free geodesic null congruences: the g_FS peak could mark the boundary
of the algebraically special region on the internal metric space.

---

<a name="data-reference-table"></a>
## Data Reference Table

All numbers used in these diagrams, with their sources.

### Modulus Space Geometry (SP-1 through SP-5)

| Quantity | Value | Source |
|:---------|:------|:------|
| Jensen metric | g_tau = 3*diag(e^{-2tau}x3, e^{tau}x4, e^{2tau}x1) | Paper 15 eq 3.68, SP-1 |
| K(0) | 0.500 | SP-2 |
| K(0.190) | 0.5346 | SP-2 |
| K'(0.190) | 0.3756 | SP-2 |
| \|C\|^2(0) | 5/14 = 0.3571 | SP-2 |
| \|C\|^2(0.190) | 0.3859 | SP-2 |
| R(0) | 2.000 | SP-2 |
| K(tau) monotonicity | K' > 0 for all tau > 0 | SP-2 (proven) |
| NEC violation | tau = 0.778 | SP-5, S17b |
| DNP crossing | tau = 0.285 | SP-5, S22a |
| Modulus metric G_mod | 5.0 (constant) | S36 |

### BCS Window (CASCADE-39)

| Quantity | Value | Source |
|:---------|:------|:------|
| BCS window | tau in [0.143, 0.235] | CASCADE-39 |
| Window width | 0.092 | CASCADE-39 |
| B2 fold | tau = 0.190 (VH minimum type) | CASCADE-39 |
| B1 fold | tau = 0.231 (VH minimum type) | CASCADE-39 |
| B3 | monotone (no VH) | CASCADE-39 |
| M_max (calibrated peak) | 1.684 at tau = 0.194 | CASCADE-39 |
| Number of M_max > 1 islands | 1 (unique) | CASCADE-39 |

### Friedmann-BCS Dynamics (FRIED-39)

| Quantity | Value | Source |
|:---------|:------|:------|
| \|dV_bare/dtau\| at fold | 58,723 | FRIED-39 |
| max \|dE_BCS/dtau\| | 8.90 | FRIED-39 |
| Gradient ratio | 6,596x | FRIED-39 |
| Dwell time (H=0) | 3.0e-4 | FRIED-39 |
| Shortfall vs dwell=40 | 133,200x | FRIED-39 |
| e-folds for dwell=40 | 2.09e8 | FRIED-39 |
| E_cond/S_full(fold) | 6.2e-7 | FRIED-39 |
| Transit speed at fold | \|dtau/dt\| = 26.545 | S36 |

### GGE and Thermalization (GGE-LAMBDA-39, INTEG-39, ENT-39)

| Quantity | Value | Source |
|:---------|:------|:------|
| lambda_B2 | 1.459 (x4 modes) | GGE-LAMBDA-39 |
| lambda_B1 | 2.771 (x1 mode) | GGE-LAMBDA-39 |
| lambda_B3 | 6.007 (x3 modes) | GGE-LAMBDA-39 |
| p_B2 | 0.2325 (per mode) | GGE-LAMBDA-39 |
| p_B1 | 0.0626 | GGE-LAMBDA-39 |
| p_B3 | 0.0025 (per mode) | GGE-LAMBDA-39 |
| S_GGE | 3.542 bits | ENT-39 |
| S_Gibbs | 6.701 bits | ENT-39 |
| Delta_S (thermalization) | 3.159 bits | ENT-39 |
| S_ent (GGE) | 0.000 (exact) | ENT-39 |
| Brody beta | 0.633 | INTEG-39 |
| Thouless g_T | 0.60 | INTEG-39 |
| t_therm | ~6 natural units | INTEG-39 |
| t_therm/t_transit | 5,253 | INTEG-39 |
| t_therm/t_Hubble | 9.0e-48 | INTEG-39 |
| T_Gibbs | 0.113 M_KK | MASS-39 |
| T_eff(B1 vs B2) | -0.040 (NEGATIVE) | GGE-LAMBDA-39 |

### Mass Spectrum (MASS-39)

| Quantity | Value | Source |
|:---------|:------|:------|
| M_B1/M_KK (tau=0.205) | 0.819 | MASS-39 |
| M_B2/M_KK (tau=0.205) | 0.845 | MASS-39 |
| M_B3/M_KK (tau=0.205) | 0.982 | MASS-39 |
| All J^P | 0^+ | MASS-39 |
| All K_7 | 0 | MASS-39 |
| BdG enhancement B2 (fold) | 49.4x | GEOD-39 |
| BdG enhancement B1 (fold) | 4.3x | GEOD-39 |
| BdG enhancement B3 (fold) | 1.2x | GEOD-39 |

### Pair Creation (RG-39, S38 W3)

| Quantity | Value | Source |
|:---------|:------|:------|
| N_pair | 1 (exact) | RG-39 |
| n_B2 (Bogoliubov) | 0.2396 (per mode) | RG-39 |
| n_B1 (Bogoliubov) | 0.0363 | RG-39 |
| n_B3 (Bogoliubov) | 0.0017 (per mode) | RG-39 |
| Total qp pairs | 59.8 | S38 W3 |
| Backreaction | 3.7% | S38 W3 |

### Quantum Metric (FS-METRIC-39)

| Quantity | Value | Source |
|:---------|:------|:------|
| g_FS at fold (tau=0.19) | 0.15578 | FS-METRIC-39 |
| g_FS peak | tau = 0.280 | FS-METRIC-39 |
| g_FS at peak | 0.15903 | FS-METRIC-39 |
| Total variation | 5.2% | FS-METRIC-39 |
| Berry curvature | 0 (identically) | FS-METRIC-39 |
| g_FS tensor structure | proportional to I_4 (Schur) | FS-METRIC-39 |
| Proximity to DNP | 2% (0.280 vs 0.285) | FS-METRIC-39 |

### B2 Geometric Protection (LIED-39)

| Quantity | Value | Source |
|:---------|:------|:------|
| Xi within B2 | 0 (identically) | LIED-39 |
| Casimir deviation | < 3e-16 at all tau | LIED-39 |
| \|\|V_8_corr - V_8_orig\|\|/\|\|V_8_orig\|\| | 25.3% | LIED-39 |
| C_2(B2) at fold | 0.2473 (corrected) | LIED-39 |

### Instanton and Schwinger (SCHWING-PROOF-39)

| Quantity | Value | Source |
|:---------|:------|:------|
| S_inst (numerical) | 0.0686 | SCHWING-PROOF-39 |
| S_inst_GL (exact analytic) | 0.2866 | SCHWING-PROOF-39 |
| S_Schwinger (S38) | 0.0703 | SCHWING-PROOF-39 |
| GL ratio | 4.08 | SCHWING-PROOF-39 |
| Shape factor kappa | 0.6533 (vs GL: 2/3) | SCHWING-PROOF-39 |
| S38 discrepancy | 2.40% | SCHWING-PROOF-39 |
| Status | Numerological coincidence | SCHWING-PROOF-39 |

---

## Methodological Note

These diagrams use the conformal compactification technique of Paper 03 (Penrose,
1963) applied to the 1+1D effective modulus-cosmology space rather than to the
physical 3+1D spacetime. The vertical direction is conformal time; the horizontal
direction is the modulus tau, conformally compactified via tau_tilde = arctan(tau).
Null rays travel at 45 degrees in the effective metric ds^2 = -dt^2 + G_mod dtau^2,
with G_mod = 5.0 (constant, tau-independent, S36).

The Penrose diagram methodology requires: (1) an exact metric (here: G_mod = 5.0,
proven constant), (2) identification of all singularities and their classification
(here: Kasner at tau -> inf, genuine, spacelike; round metric at tau = 0, regular),
(3) maximal analytic extension (here: the 26 closures exhaust all coordinate
patches), and (4) conformal boundary structure (here: i+, i- as in the standard
construction).

The diagrams are not spacetime diagrams in the GR sense -- the internal SU(3)
space is Riemannian, not Lorentzian. The "causal structure" is the modulus
dynamics in cosmological time, which inherits a Lorentzian signature from the
Friedmann equation. The Penrose diagram technique is applied by analogy, with
the modulus playing the role of a radial coordinate and cosmological time playing
the role of Kruskal time. This analogy is structural (the gradient hierarchy
6,596x is the analog of the gravitational potential), not a claim that the modulus
space is literally a Lorentzian manifold.

---

*Schwarzschild-Penrose-Geometer, 2026-03-09.*
*"Draw the diagram. The physics is in the diagram."*
*-- R. Penrose, every lecture, every time.*
