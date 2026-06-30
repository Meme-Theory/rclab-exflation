# Numerical Lattice Simulations of Preheating Dynamics

**Author(s):** Anders Tranberg, Ben Garbrecht
**Year:** 2006-2014
**Journal:** Physical Review D, Journal of Cosmology and Astroparticle Physics

---

## Abstract

Tranberg performed large-scale lattice simulations of preheating and reheating dynamics, numerically integrating the classical equations of motion for interacting field systems far from equilibrium. These simulations validated Kofman-Linde-Starobinsky parametric resonance predictions and enabled detailed studies of particle spectra, backreaction, and thermalization impossible analytically.

---

## Key Methods

### Lattice Discretization

Discretize spacetime on a lattice with spacing Δx:

φ(x_i, t_n) = φ_{i,n}

Equations of motion become coupled ODEs:

d²φ_{i,n}/dt² = [φ_{i+1,n} − 2φ_{i,n} + φ_{i−1,n}] / (Δx)² − ∇V/∂φ

Integrate using leapfrog or higher-order symplectic schemes preserving energy.

### Observables

1. **Power Spectrum**: n_k(t) = |χ_k(t)|² (occupation number per mode)
2. **Energy Density**: ρ(t) = ⟨(dφ/dt)² + (∇φ)² + V(φ)⟩
3. **Entropy Production**: S(t) derived from distribution shape

---

## Key Results

1. **Resonance Validated**: Numerical spectra match Kofman-Linde-Starobinsky analytical predictions to 10% precision.

2. **Backreaction Timescale**: Confirms τ_backreaction ~ 1/√{gλ} × m_φ.

3. **Thermalization Slow**: Final drift to thermal equilibrium takes ~1000s of oscillations, much longer than resonant growth.

---

## Connection to Framework

Framework's GGE formation at the fold can be studied analogously: simulate spectral-mode evolution during τ transit using spectral-action dynamics. If numerical simulations confirm:

- n_eigenvalue(τ = 0.190) exhibits explosive growth
- Saturation at ~60 modes (matching 59.8 prediction)
- Plateau (no further growth) post-τ = 0.191

Then framework's dynamical picture is numerically validated.
