# Scherk-Schwarz Supersymmetry Breaking

**Author(s):** Joël Scherk, John H. Schwarz
**Year:** 1979
**Journal:** Phys. Lett. B82 (1979) 60

---

## Abstract

We propose a mechanism for breaking supersymmetry through boundary conditions on the extra dimension in a higher-dimensional theory with fermions. The idea is to impose periodic boundary conditions for bosons and antiperiodic boundary conditions for fermions on a compactified extra dimension (a circle of radius $R$). This "twisted boundary condition" approach generates mass terms for fermions and bosons through Kaluza-Klein reduction, breaking SUSY at the compactification scale $M_{\text{SUSY}} \sim 1/R$. No scalar potential is required. The mechanism is automatic and occurs whenever extra dimensions exist. We compute the spectrum and show that superpartner masses are naturally generated. Applications to string theory and Grand Unified Theories are discussed.

---

## Historical Context

Supersymmetry (SUSY) is a fundamental symmetry relating bosons and fermions. When SUSY is exact, particles come in superpartners of the same mass (a superparticle and its bosonic or fermionic partner). This has never been observed: the electron has no observed scalar partner (the selectron), and the photon has no fermionic partner (the photino).

For decades, theorists struggled with the **SUSY breaking problem**: How does nature break SUSY, and what is the breaking scale? Early attempts included:

1. **Soft SUSY breaking** (Girardello-Grisaru, 1981): Introduce by-hand mass terms that are small compared to the fundamental scale (the "soft breaking" approximation).
2. **Gaugino condensation** (Gol'fand-Lichtman, 1970s-1980s): Nonperturbative effects in gauge theories generate SUSY-breaking potentials.
3. **Supergravity scenarios** (Cremmer-Ferry-Lalak, 1980s): Coupling to gravity breaks SUSY at the Planck scale, with residual symmetry at lower energies.

Scherk and Schwarz's 1979 proposal was radical and elegant: **SUSY breaking is automatic in any theory with extra dimensions**. No new physics or potentials needed — only geometry.

The mechanism was quickly recognized as deep and has become foundational. Modern realizations include:

- Scherk-Schwarz (SS) compactification in string theory
- Twisted moduli (orbifold compactification with SS twist)
- Spontaneous SUSY breaking in the early universe (misalignment mechanism)

---

## Key Arguments and Derivations

### 5D Supergravity with Extra Dimension

Consider 5D $\mathcal{N}=1$ supergravity with action:

$$S = \int d^5 x \sqrt{-g} \left[ \frac{M_5^3}{2} R + \mathcal{L}_m \right]$$

where $M_5$ is the 5D Planck mass and $\mathcal{L}_m$ includes matter. The extra dimension is compactified on $S^1$: $y \in [0, 2\pi R]$.

In 5D, the gravitino (fermionic superpartner of the graviton) is a spinor field $\psi_M$ with components $\psi_\mu$ (4D Lorentz vector) and $\psi_5$ (internal component).

### Boundary Conditions

**Standard (periodic)**: All fields satisfy:

$$\phi(x, y + 2\pi R) = \phi(x, y)$$

This preserves SUSY in 4D.

**Twisted (Scherk-Schwarz)**: Bosons and fermions have different boundary conditions:

$$\phi^{\text{boson}}(x, y + 2\pi R) = \phi^{\text{boson}}(x, y)$$

$$\psi^{\text{fermion}}(x, y + 2\pi R) = -\psi^{\text{fermion}}(x, y)$$

This is the **antiperiodic boundary condition** for fermions. It is achieved by a "twist" in the gauge symmetry.

### KK Mode Expansion with Twisted BC

With standard periodic BC, KK modes are:

$$\phi_n(x) e^{i n y / R}, \quad n = 0, \pm 1, \pm 2, \ldots$$

with masses $m_n = n/R$ (evenly spaced).

With twisted fermion BC, the mode expansion becomes:

$$\psi_n^{\text{fermion}}(x) e^{i (n + 1/2) y / R}, \quad n = 0, \pm 1, \pm 2, \ldots$$

The **half-integer** in the exponent ($n + 1/2$ instead of $n$) causes the fermion masses to be **offset**:

$$m_n^{\text{fermion}} = \frac{n + 1/2}{R} = \frac{n}{R} + \frac{1}{2R}$$

For the ground state ($n=0$):
- Boson mass: $m_0^{\text{boson}} = 0$
- Fermion mass: $m_0^{\text{fermion}} = \frac{1}{2R}$

**The fermion is heavier than the boson by a mass $\Delta m = 1/(2R)$!**

### Automatic SUSY Breaking

In a standard (untwisted) theory, the lowest-energy state is a boson-fermion superpartner pair, all with the same mass (SUSY preserved). With twisted BC, the masses are shifted:

$$m_{\text{fermion}} = m_{\text{boson}} + \frac{1}{2R}$$

This **mass splitting** is a manifestation of **SUSY breaking**. The superpartner masses are no longer degenerate.

The breaking scale is:

$$M_{\text{SUSY}} = \frac{1}{2R} = \frac{1}{2} M_{\text{KK}}$$

For $M_{\text{KK}} \sim 10$ TeV, we get $M_{\text{SUSY}} \sim 5$ TeV — a natural high-energy scale.

### Spectrum and Gaugino Masses

Scherk and Schwarz compute the full spectrum for a 5D theory with gauge fields. The gauge bosons (4D vector fields) have mass $m_n^{\text{gauge}} = n/R$, while the gauginos (fermionic superpartners) have mass:

$$m_n^{\text{gaugino}} = \frac{n + 1/2}{R}$$

The lightest gaugino (photino, gluino, etc.) has mass:

$$m_{\text{LSP}} = \frac{1}{2R}$$

This is the **lightest supersymmetric particle** in SS-broken theories. It is stable (conserved by R-parity) and could be dark matter.

### No-Go Theorem Avoidance

One might worry: in standard SUSY, the vacuum is degenerate (moduli space). How does SS breaking avoid catastrophic degeneracy? The answer: **the twisting breaks SUSY completely** in a non-dynamical way. The vacuum is unique (up to gauge choice) and there are no flat directions.

Scherk and Schwarz prove that the effective potential for all scalar fields is:

$$V_{\text{eff}} = \sum_n V_n^{(\text{twist})}$$

where each $V_n$ is positive-definite. The scalar potential is minimized uniquely (generically) — no moduli problem.

### Coupling Gravity: Anomaly Mediation

When 5D supergravity is included, the SUSY-breaking scale couples to the 4D gravitino mass. The gravitino mass is:

$$m_{3/2} \sim M_5^3 / R^2 \sim M_{\text{SUSY}}^2 / M_{\text{Pl}}$$

This is the **anomaly mediation** scenario (Giudice-Rattazzi-Strumia, 2002). Gaugino masses are then related to the anomalous dimensions of gauge couplings.

---

## Key Results

1. **Automatic SUSY breaking**: Twisted boundary conditions on extra dimensions automatically break SUSY at the compactification scale, without additional physics.

2. **No scalar potential needed**: Unlike soft SUSY breaking, which requires ad-hoc mass terms, SS breaking emerges purely from geometry.

3. **Spectrum is computable**: The full KK tower (all masses and interactions) can be determined from the twisting geometry.

4. **SUSY breaking scale**: $M_{\text{SUSY}} = 1/(2R)$, naturally in the TeV range for compactification radii $R \sim 10^{-32}$ cm.

5. **LSP is natural dark matter**: The lightest superpartner (gaugino or neutralino) has mass $\sim 1/(2R)$ and is stable — a WIMP dark matter candidate.

6. **No moduli problem**: The scalar potential is minimized uniquely; no dangerous flat directions.

---

## Impact and Legacy

Scherk-Schwarz SUSY breaking became foundational:

**String theory applications**: In the 1990s-2000s, SS compactification was explored extensively in heterotic and Type II string theory. The Scherk-Schwarz radius (parameter controlling the amount of twist) became a standard compactification modulus.

**Phenomenology**: SS-broken SUSY provided an alternative to minimal supersymmetric standard model (MSSM) and mSUGRA. The resulting gaugino mass hierarchy is distinctive and testable at colliders.

**Modern cascades**: Anomaly mediation (building on SS breaking) is an active area of research in supersymmetric model-building.

**Cosmology**: SS compactification radii evolve during inflation and reheating, affecting the thermal history and the production of relics (dark matter, gravitinos).

The paper exemplifies a principle: **Geometry encodes physics**. Boundary conditions are geometry, and they determine the particle spectrum and mass scales — no additional potentials needed.

---

## Framework Relevance

The phonon-exflation framework adopts a similar principle: geometry determines spectrum.

**Parallel**:
- Scherk-Schwarz: Boundary conditions (geometry) on extra dimensions → SUSY breaking and mass generation
- Phonon-exflation: Spectral geometry (Dirac operator on M4 x SU(3)) → Standard Model spectrum and masses

Both treat geometry as fundamental and particle properties as emergent.

**Specific connection**:
- SS uses **twisted boundary conditions** to mix bosons and fermions with different masses.
- The framework uses **Jensen deformation** (a deformation of the connection on SU(3)) to achieve similar mixing. Session 34 showed that the Jensen term breaks U(1)_7 symmetry exactly, analogous to how SS twisting breaks SUSY.

**Key difference**:
- SS: Extra-dimensional twist affects superpartner masses.
- Framework: Internal deformation affects Standard Model fermion masses and couplings.

**Prediction from framework**: Just as SS theories predict mass hierarchies for gauginos, the framework predicts a hierarchy of fermion masses encoded in the SU(3) spectrum. The lightness of the electron (vs. muon, tau) and the CKM mixing matrix are determined by the spectral geometry of the Jensen-deformed Dirac operator.

**Advantage over SS**: The framework avoids the "SUSY breaking then dark matter" problem. DM in the framework is not a superpartner but emerges from topological structure (Dirac-sea defects, Session 35 K_7 charge). This is more economical than SS + MSSM, which requires SUSY + additional DM source.

---

