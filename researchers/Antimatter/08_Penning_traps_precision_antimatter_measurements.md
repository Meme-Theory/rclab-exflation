# Penning Traps and Precision Antimatter Measurements

**Key Experiments**: TRAP, BASE, ATRAP
**Location**: CERN Antiproton Decelerator (AD) / ELENA
**Key Figures**: Gerald Gabrielse, Stefan Ulmer, Klaus Blaum

## Overview

Penning traps use static electric and magnetic fields to confine individual charged particles indefinitely, enabling the most precise measurements of fundamental particle properties. Applied to antimatter, they provide the most stringent tests of CPT symmetry.

## Penning Trap Principles

### Configuration
A Penning trap consists of:
1. **Uniform magnetic field B₀**: Constrains radial motion (cyclotron orbits)
2. **Quadrupole electric field**: Confines axial motion between endcap electrodes

The resulting particle motion decomposes into three independent oscillations:

| Mode | Frequency | Typical Range |
|------|-----------|---------------|
| Modified cyclotron | ν₊ ≈ eB₀/(2πm) | ~30 MHz |
| Axial | ν_z = √(eV₀/md²)/(2π) | ~600 kHz |
| Magnetron | ν₋ ≈ ν_z²/(2ν₊) | ~10 kHz |

The **true cyclotron frequency** is reconstructed via the invariance theorem:

    ν_c² = ν₊² + ν_z² + ν₋²

This gives the charge-to-mass ratio q/m with extraordinary precision.

### Key Innovation: Single-Particle Detection
The trapped particle induces image currents in the electrodes. At cryogenic temperatures (~100 mK), these currents can be detected with superconducting resonant circuits, enabling non-destructive measurement of a SINGLE trapped antiproton.

## BASE Collaboration Results

### Charge-to-Mass Ratio
The Baryon Antibaryon Symmetry Experiment (BASE) at CERN measures:

    (q/m)_p̄ / (q/m)_p = 1.000000000000 ± 0.000000000016

**Precision: 16 parts per trillion (ppt)** — the most precise test of CPT in the baryon sector.

### Magnetic Moment
The antiproton magnetic moment:

    μ_p̄ = -2.7928473441(42) μ_N

compared to the proton:

    μ_p = +2.79284734462(82) μ_N

**Agreement to 1.5 parts per billion** — consistent with CPT invariance.

### Measurement Technique
BASE uses a multi-trap system:
1. **Reservoir trap**: Stores antiprotons from AD/ELENA
2. **Precision trap**: Single-antiproton cyclotron frequency measurement
3. **Analysis trap**: Spin-flip detection for magnetic moment
4. **Monitoring trap**: Tracks magnetic field stability

The spin state is determined by the **continuous Stern-Gerlach effect**: a magnetic bottle couples the spin orientation to the axial frequency, creating a measurable frequency shift:

    Δν_z = (μ·B₂)/(2π²mν_z)

where B₂ is the magnetic bottle gradient.

## The Electron/Positron g-2

Penning traps also provide the most precise measurement of the electron and positron anomalous magnetic moments:

    a_e = (g-2)/2 = 0.001 159 652 180 59(13)    (Fan et al., Harvard 2023)

This agrees with QED predictions to 12 significant figures, making it the most precisely tested prediction in all of physics.

For the positron:

    a_{e⁺}/a_{e⁻} - 1 = (-0.5 ± 2.1) × 10⁻¹²

Consistent with CPT at the parts-per-trillion level.

## BASE-STEP: Transportable Traps

In 2025, the BASE-STEP project demonstrated the first transport of a trapped proton cloud from CERN's antimatter factory using a cryogenic, superconducting, autonomous Penning trap system. The goal is to eventually transport antiprotons to off-site laboratories for measurements in controlled environments.

## Connection to the Framework

### 1. CPT as Structural Anchor
Every precision CPT test validates the J operator in the NCG spectral triple. The 16 ppt q/m agreement means:
- The particle and antiparticle sectors of H_F are symmetric to extraordinary precision
- J² = +1 (KO-dim 6) is empirically anchored
- Any framework modification that breaks J's defining properties is immediately falsifiable

### 2. Magnetic Moment and Dirac Operator
The anomalous magnetic moment a = (g-2)/2 arises from radiative corrections (virtual particle loops). In the NCG framework, these corrections involve the full Dirac operator D = D_M ⊗ 1 + γ₅ ⊗ D_F, and the internal geometry contributes through the spectral action.

### 3. Mass Equality and V_eff
If the Jensen deformation parameter s stabilizes at s₀, the mass spectrum from D_K(s₀) must produce EQUAL masses for particles and antiparticles. This is guaranteed if J commutes with D_K — which Baptista Papers 17/18 show follows from D_K commuting with the Killing isometries of the deformed SU(3).

## Key Numbers

| Measurement | Precision | Experiment |
|-------------|-----------|------------|
| q/m ratio (p̄/p) | 16 ppt | BASE (2022) |
| Magnetic moment (p̄) | 1.5 ppb | BASE (2017) |
| Electron g-2 | 0.24 ppb | Harvard (2023) |
| e⁺/e⁻ g-2 comparison | 2.1 ppt | UW/Harvard |
| Antiproton lifetime | > 10⁷ years | LEAR |

## References

- S. Ulmer et al., "High-precision comparison of the antiproton-to-proton charge-to-mass ratio," Nature 524, 196 (2015)
- C. Smorra et al., "A parts-per-billion measurement of the antiproton magnetic moment," Nature 550, 371 (2017)
- X. Fan et al., "Measurement of the Electron Magnetic Moment," Phys. Rev. Lett. 130, 071801 (2023)
- G. Gabrielse et al., "New Measurement of the Electron Magnetic Moment and the Fine Structure Constant," Phys. Rev. Lett. 97, 030802 (2006)
- M. Borchert et al., "A 16-parts-per-trillion measurement of the antiproton-to-proton charge-to-mass ratio," Nature 601, 53 (2022)
