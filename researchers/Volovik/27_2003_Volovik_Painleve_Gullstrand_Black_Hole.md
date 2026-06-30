# Simulation of Painleve-Gullstrand black hole in thin 3He-A film

**Author(s):** G.E. Volovik
**Year:** 1999
**Journal:** JETP Lett. 69, 705-713 (1999)
**arXiv:** gr-qc/9901077
**Relevance:** HIGH

---

## Abstract

The quasi-stationary superfluid state is constructed, which exhibits the event horizon and Hawking radiation.

---

## Key Arguments and Derivations

### A. Introduction

The paper establishes that gravitational fields can be simulated in condensed matter by the motion of liquid: propagation of perturbations in moving liquid obeys the same equation as propagation of relativistic particles in a gravitational field. These perturbations are sound waves in normal fluids and quasiparticles in superfluids (phonons in superfluid 4He and low-energy Bogoliubov fermions in superfluid 3He-A).

For radial, spherically symmetric fluid motion, the effective metric is:

ds^2 = -(c^2 - v^2(r)) dt^2 + 2v(r) dr dt + dr^2 + r^2 d(Omega)^2

Choosing a velocity field v^2(r) = 2GM/r = c^2 r_h/r yields the Painleve-Gullstrand form of the Schwarzschild geometry. When v(r) < 0 (inward flow), this reproduces a black hole horizon at r_h where |v| = c.

Previous proposals (Unruh's sonic black hole, moving solitons, draining bathtub) all suffered from practical drawbacks: fluid accumulation, finite lifetime, or friction-dominated dissipation. Volovik proposes a scenario avoiding these problems where the superfluid motion becomes quasi-stationary and the lifetime of the superluminal flow is determined by intrinsic mechanisms, particularly Hawking radiation.

### B. Simulation of 2D black hole

The construction uses a superfluid 3He-A film moving toward the center of a disk, where it escapes to a third dimension through an orifice. For constant film thickness, the flow velocity increases as v(r) = a/r, reaching the "speed of light" c at r = r_h = a/c. The effective metric experienced by Bogoliubov quasiparticles is:

ds^2 = -(c^2 - v^2(r)) dt^2 + 2v(r) dr dt + dr^2 + r^2 d(phi)^2 + (c^2/v_F^2) dz^2

The "speed of light" for in-plane quasiparticles is c ~ 3 cm/sec, much smaller than the Fermi velocity v_F for propagation normal to the film, and much smaller than the sound speed in 3He-A (so the flow does not affect liquid density).

A key design element: the 3He-A film is placed on top of a superfluid 4He film. This screens the interaction with the solid substrate and prevents collapse of the superluminal flow. The 4He is not excited even at superluminal 3He-A velocities because c for 3He-A is far below the Landau velocity for 4He (~50 m/sec).

The superflow can be closed using toroidal geometry: both 4He and 3He-A circulate around meridians of a torus with integer circulation quanta N_4 and N_3 (kappa_4 = 2pi hbar/m_4 and kappa_3 = pi hbar/m_3). If the inner radius is small enough, both black hole and white hole horizons appear.

### C. Vacuum in comoving and rest frames

Two reference frames are analyzed:

(i) **Comoving frame**: Local superfluid velocity is zero, E_com = +/- cp. The vacuum (filled Dirac sea) is the counterpart of the Minkowski vacuum, but is only locally defined. The comoving frame cannot be determined globally, and for the comoving observer the velocity field v(r,t) is time-dependent, preventing correct energy determination.

(ii) **Rest (laboratory) frame**: The system is stationary (metric time-independent) so energy is conserved. The energy is Doppler-shifted: E_rest = +/- cp + p_r v(r).

Outside the horizon, or in the absence of a horizon, occupied/empty states are the same in both frames. Behind the horizon (|v| > c), the branch E_rest = (v+c)p_r has reversed distribution: negative energy states are empty, positive energy states are occupied, corresponding to temperature T = -0.

Since energy is conserved in the rest frame, fermions can tunnel across the horizon from occupied to empty states at the same energy, creating particle-hole pairs: the quasiparticle appears outside, the quasihole inside. This simulates the Hawking radiation from a black hole.

### D. Hawking radiation

The tunneling rate is computed semiclassically. The branch E_rest = (v(r) - c)p_r describes incoming particles with p_r < 0, propagating through the horizon without singularity. Their trajectories are p_r(r) = -E_rest/(c - v(r)).

The branch E_rest = (v(r) + c)p_r contains two disconnected pieces:

- r > r_h: p_r = E_rest/(c + v(r)) > 0 (outgoing particles, positive energy in both frames)
- r < r_h: p_r = E_rest/(c + v(r)) < 0 (particles within horizon; positive rest-frame energy but negative comoving energy -- belongs to Minkowski vacuum)

The classical trajectory is disrupted at the horizon. Quantum tunneling connects the two pieces with amplitude:

w ~ exp(-2S), where S = Im integral(dr p_r(r)) = pi E_rest / |v'(r)|_{r=r_h}

The exponential energy dependence yields a thermal spectrum with the Hawking temperature:

T_Hawking = hbar |v'(r)|_{r=r_h} / (2 pi)

The radiation causes quantum friction: linear momentum of the flow decreases continuously until the superfluid Minkowski vacuum between horizons is exhausted and a phase slip event occurs, reducing the circulation quantum number N_3. This process repeats until the two horizons merge.

### E. Negative temperature for chiral 1+1 fermions

For 1+1 dimensional chiral fermions in a vortex core, there is only one branch E = omega_0(phi) L, where L is angular momentum and omega_0(phi) is the minigap (angle-dependent for non-axisymmetric cores). If the vortex core rotates with angular velocity Omega exceeding the minimum minigap, a horizon forms. In the corotating frame, E_corotating = (omega_0(phi) - Omega) L.

Behind this horizon, the Minkowski vacuum (T = +0 in the lab frame) becomes a state with T = -0 in the corotating frame, and vice versa. This symmetry between vacua suggests that a heat bath at T = T_Hawking at infinity would create a metastable steady state with T = -T_Hawking behind the horizon.

### F. Discussion

The event horizon / Hawking radiation description applies only for low-energy fermions with relativistic spectrum. At higher energies, the "horizon" persists (at the surface where superflow exceeds the Landau critical velocity) but additional mechanisms become important. Radiated particles with energies outside the relativistic region can be Andreev scattered back into the black hole. Both partners (particle and hole) of the Hawking radiation then remain within the horizon.

This means particle creation in a high gravity field can disturb the Minkowski vacuum inside the horizon without any radiation to the exterior. Such pair creation inside the horizon may be more important for dissipation of the supercritical superflow than Hawking radiation itself.

---

## Key Results

1. A quasi-stationary superfluid configuration exhibiting an event horizon can be realized using a 3He-A film on top of a 4He film, in either draining-bathtub or toroidal geometry
2. The effective metric for Bogoliubov quasiparticles is the Painleve-Gullstrand form of the Schwarzschild geometry
3. The Hawking temperature for this analog system is T_Hawking = hbar |v'(r)|_{r_h} / (2 pi)
4. Behind the horizon, the Minkowski vacuum has reversed population (negative temperature T = -0) as viewed from the rest frame
5. Pair creation inside the horizon via Andreev scattering may dominate over Hawking radiation for dissipation of supercritical flow
6. The 4He substrate film screens wall interactions, enabling superluminal 3He-A flow without Cherenkov collapse
7. For chiral 1+1 fermions in rotating vortex cores, the negative temperature behind the horizon is well-defined and leads to a T = -T_Hawking metastable steady state

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| PG metric (3+1) | ds^2 = -(c^2 - v^2(r)) dt^2 + 2v(r) dr dt + dr^2 + r^2 d(Omega)^2 | Eq. (1) |
| Velocity-gravity map | v^2(r) = 2GM/r = c^2 r_h/r | Eq. (2) |
| Bogoliubov spectrum | (E - p.v)^2 = c^2(p_x^2 + p_y^2) + v_F^2(p_z -/+ p_F)^2 | Eq. (3) |
| 2D effective metric | ds^2 = -(c^2 - v^2) dt^2 + 2v dr dt + dr^2 + r^2 d(phi)^2 + (c^2/v_F^2) dz^2 | Eq. (4) |
| Comoving spectrum | E_com = +/- cp | Eq. (5) |
| Rest frame energy | E_rest = +/- cp + p_r v(r) | Eq. (6) |
| Incoming trajectory | p_r(r) = -E_rest/(c - v(r)) < 0 | Eq. (7) |
| Outgoing (exterior) | p_r = E_rest/(c + v(r)) > 0, E_com = cp_r > 0 | Eq. (8) |
| Outgoing (interior) | p_r = E_rest/(c + v(r)) < 0, E_com = cp_r < 0 | Eq. (9) |
| Tunneling amplitude | w ~ exp(-2S) | Eq. (10) |
| Tunneling action | S = Im integral(dr p_r) = pi E_rest / |v'(r)|_{r=r_h} | Eq. (11) |
| Hawking temperature | T_Hawking = hbar |v'(r)|_{r=r_h} / (2 pi) | Eq. (12) |

---

## Relevance to Phonon-Exflation

1. **Superfluid vacuum as spacetime**: The paper provides the concrete mapping between superfluid flow and Painleve-Gullstrand coordinates -- the same coordinate system natural for the phonon-exflation framework where geometry emerges from the superfluid substrate.

2. **Hawking radiation as pair creation via tunneling**: The semiclassical tunneling derivation (Eqs. 10-11) directly parallels the Schwinger-instanton duality identified in Session 38. Both describe pair creation at a horizon/barrier via WKB tunneling in Euclidean time. The tunneling action S = pi E/|v'| has the same structure as the instanton action S_inst = 0.069.

3. **Negative temperature behind horizon**: The reversed population behind the horizon (T = -0) is structurally identical to the inverted distribution in the post-transit GGE state of the phonon-exflation framework. The Minkowski vacuum inside the horizon "looks thermal" from outside but is actually the ground state seen from a different frame.

4. **Pair creation without radiation**: The discussion that Andreev scattering can trap both partners of Hawking radiation inside the horizon (Section F) is directly relevant to the framework's finding that pair creation during transit produces a non-thermal GGE relic with no radiation to the 4D exterior. The pair creation disturbs the vacuum without exterior radiation -- the "ordered veil."

5. **Superluminal flow stability via screening**: The 4He screening mechanism that prevents Cherenkov collapse of superluminal flow is an analog of the integrability protection that prevents thermalization of the post-transit state. Both rely on a separation of energy scales (c for 3He-A << Landau velocity for 4He) to maintain a metastable non-equilibrium state.

6. **Phase slip events**: The horizon-driven phase slip (reduction of N_3 circulation quanta) maps to the framework's tau-transit, where the topological charge changes as the system passes through a quantum phase transition.
