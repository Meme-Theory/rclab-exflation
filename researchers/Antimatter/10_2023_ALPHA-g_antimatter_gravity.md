# ALPHA-g: First Observation of Antimatter Gravity (2023)

**Collaboration**: ALPHA
**Published**: Nature 621, 716-722 (2023)
**Title**: "Observation of the effect of gravity on the motion of antimatter"

## Abstract

The ALPHA-g experiment at CERN provides the first direct observation that antimatter (antihydrogen atoms) falls downward under Earth's gravity, consistent with the weak equivalence principle. The measured gravitational acceleration is:

    a_g = [0.75 ± 0.13 (stat.+syst.) ± 0.16 (sim.)] g

where g is the local gravitational acceleration. This rules out gravitational repulsion of antimatter at greater than 99.97% confidence.

## The Question

Does antimatter fall up or down? More precisely: is the gravitational acceleration of antimatter:
- **Attractive** (same as matter): a_g = +g
- **Repulsive**: a_g = -g
- **Zero**: a_g = 0
- **Something else**: a_g = αg, with α ≠ 1

### Theoretical Expectations
General relativity predicts the **weak equivalence principle (WEP)**: all forms of matter fall identically in a gravitational field. This applies to antimatter because:
1. E = mc² means antimatter has POSITIVE mass-energy
2. CPT invariance guarantees m(particle) = m(antiparticle) for INERTIAL mass
3. WEP equates inertial and gravitational mass

However, direct experimental verification had been lacking for 90+ years since antimatter's discovery.

### Why It Took So Long
Neutral antimatter is essential (charged particles are overwhelmed by electromagnetic forces). But:
- Antihydrogen is hard to produce (first cold H̄: 2002)
- Harder to trap (first trapped H̄: 2010)
- Even harder to release slowly enough for gravity to matter

Gravity exerts a force of ~10⁻²⁶ N on a single antihydrogen atom. The trap depth (~0.5 K) corresponds to a gravitational potential energy of ~100 K × m × g × h. The signal is tiny.

## The ALPHA-g Apparatus

### Vertical Trap Design
ALPHA-g uses a specially designed vertical magnetic minimum trap:
- **Height**: ~25 cm usable trapping region
- **Orientation**: Vertical axis aligned with gravity
- **Endcap asymmetry**: Top and bottom magnetic mirrors can be independently ramped

### Measurement Principle
1. Trap ~100 antihydrogen atoms
2. Slowly ramp down the trapping fields over 20 seconds
3. Monitor where atoms escape: top or bottom of the trap
4. If gravity pulls H̄ downward: more annihilations detected at the bottom
5. If gravity repels H̄: more annihilations at the top
6. Repeat with bias fields to map the escape probability vs. field asymmetry

### Bias Field Method
By applying different additional magnetic fields that either enhance or counteract gravity, the experiment maps:

    P_bottom(ΔB) = f(a_g, T, trap_geometry)

The gravitational acceleration a_g is extracted by fitting the escape ratio as a function of the bias field.

## Results

### Primary Finding
- **Antimatter falls DOWN** (same as matter)
- Gravitational repulsion excluded at > 99.97% confidence (> 3.5σ)
- a_g/g = 0.75 ± 0.13 ± 0.16, consistent with a_g = g

### Systematic Uncertainties
The main systematics are:
- Antihydrogen temperature distribution (affects escape dynamics)
- Magnetic field mapping (residual gradients mimic gravity)
- Annihilation vertex reconstruction (position resolution)

### Future Precision
With laser cooling (demonstrated in ALPHA-2 in 2021), the temperature can be reduced by ~10x, dramatically improving precision. Goal: test WEP for antimatter at the 1% level, eventually approaching 10⁻³.

## Competing/Complementary Experiments

| Experiment | Method | Species | Status |
|-----------|--------|---------|--------|
| ALPHA-g | Magnetic trap release | H̄ atoms | Published (2023) |
| GBAR | Free-fall timing | H̄⁺ ions → H̄ | Commissioning |
| AEgIS | Moiré deflectometer | H̄ beam | In preparation |

## Theoretical Implications

### For General Relativity
- WEP confirmed for antimatter (first direct test)
- Constrains exotic gravity theories that predict antimatter repulsion
- Dirac-Milne cosmology (matter-antimatter repulsion) RULED OUT

### For CPT
- If a_g(H̄) ≠ g, either WEP or CPT must be violated
- Since CPT is tested to ppt precision (ALPHA spectroscopy, BASE), WEP violation alone would be the interpretation
- No evidence for either violation

### For Cosmology
- Some theories proposed antimatter repulsion to explain cosmic acceleration
- ALPHA-g effectively rules these out
- The cosmological constant / dark energy problem remains

## Connection to the Framework

### 1. Equivalence Principle and KK Geometry
In the phonon-exflation framework on M⁴ × K:
- The equivalence principle applies to the FULL higher-dimensional spacetime
- After dimensional reduction, matter and antimatter both couple to the 4D metric g_μν identically
- The Jensen deformation acts on the INTERNAL metric, not the external gravity
- ALPHA-g confirms that the 4D gravitational sector is symmetric under J (particle ↔ antiparticle)

### 2. Gravitational Mass from Spectral Action
The spectral action Tr(f(D²/Λ²)) generates both the gravitational action AND the matter Lagrangian. The gravitational mass of a particle comes from the D_K eigenvalues:

    m² ∝ λ²(D_K)

Since JD_KJ⁻¹ = D_K (Baptista: D_K commutes with Killing isometries, and J is built from them), the gravitational mass of particles and antiparticles is automatically equal. ALPHA-g tests this structural prediction.

### 3. No Antigravity = No Charge Asymmetry in Internal Space
Gravitational repulsion of antimatter would require the internal Dirac operator to have sign-asymmetric eigenvalues under J. This would break the spectral triple's reality condition. ALPHA-g's null result is therefore a structural consistency check on the NCG framework.

## Key Numbers

| Quantity | Value |
|----------|-------|
| Measured a_g/g | 0.75 ± 0.13 ± 0.16 |
| Repulsion excluded | > 99.97% CL |
| Trapped atoms per cycle | ~100 |
| Release time | 20 seconds |
| Annihilation vertex resolution | ~5 mm |

## References

- E. K. Anderson et al. (ALPHA), "Observation of the effect of gravity on the motion of antimatter," Nature 621, 716 (2023)
- C. J. Baker et al. (ALPHA), "Laser cooling of antihydrogen atoms," Nature 592, 35 (2021)
