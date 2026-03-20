# Induced Gravity in Superfluid 3He

**Author(s):** Grigory E. Volovik
**Year:** 1994
**Journal:** Journal of Low Temperature Physics, 104, 1-26
**arXiv:** cond-mat/9307009

---

## Abstract

This foundational paper demonstrates that superfluid 3He-A, a macroscopic quantum fluid, exhibits all the key phenomena of general relativity: event horizons, curved spacetime, Hawking radiation, and gravitational induction. The core result is that **fermionic excitations (quasiparticles) in 3He-A propagate in an effective curved metric** determined by the texture and flow of the superfluid.

The key findings are:

- The effective metric experienced by quasiparticles has signature $(-,+,+,+)$ (Minkowski) with curvature tensor nonzero when the superfluid texture varies.
- Horizons form in superfluid flows (moving singular structures); beyond the horizon, no quasiparticle can escape.
- The temperature associated with such horizons gives an analog of Hawking radiation with thermal spectrum.
- The effective gravitational constant emerges from the quasiparticle density of states.
- The Unruh effect (inertial observers detecting a thermal bath) has an exact analog in superfluid flows.

This paper opened the field of **analog gravity** and provided experimental access to phenomena previously thought exclusively gravitational. It is the direct ancestor of later proposals for black hole analogs in BEC, ions, and photons.

---

## Historical Context

By the 1990s, it was understood that:

1. **GR is scale-invariant near the Hawking radius**: Quantum field theory in curved spacetime predicts a horizon has temperature $T_H = \frac{\hbar c}{4\pi k_B G M}$ (Hawking, 1974). But the derivation assumes a classical background metric — quantum gravity corrections might destroy the result.

2. **No laboratory test of Hawking radiation was possible**: Black hole horizons require extreme spacetime curvature, inaccessible to experiment.

3. **Effective theories can mimic gravitational phenomena**: In the 1980s, Unruh proposed that accelerated detectors "see" a thermal bath analogous to black hole radiation. But this was abstract — could it be made concrete?

Volovik's insight was revolutionary: **Take a well-understood condensed matter system (3He superfluid) with completely calculable microscopic physics, and show that its quasiparticles obey an effective Einstein equation.**

This allows:
- Calculation of the effective metric from first principles (no phenomenological parameters).
- Experimental observation of analog horizons and Hawking radiation.
- Testing the robustness of gravitational phenomena to trans-Planckian details.

---

## Key Arguments and Derivations

### Part I: Quasiparticle Spectrum in Superfluid 3He-A

#### Order Parameter and Texture

Superfluid 3He-A is a p-wave paired state with order parameter:

$$\Delta_{\alpha i}({\bf r}) = d_\alpha \ell_i({\bf r})$$

where $\alpha$ is the spin index (up or down), $i$ is the orbital index, $d_\alpha$ is the gap amplitude, and $\ell_i({\bf r})$ is the **orbital-angular-momentum vector** (texture).

The texture $\ell_i$ varies with position ${\bf r}$, describing how the Cooper pair orbital is oriented. A superfluid flow induces a spatially varying texture, which modulates the quasiparticle spectrum.

#### Quasi-Particle Spectrum

The energy of a quasiparticle near the gap node is:

$$E({\bf r}, \mathbf{p}) = \sqrt{(\mathbf{v}_F \cdot \mathbf{p})^2 + (v_\Delta \ell_i p_i)^2}$$

where $\mathbf{v}_F$ is the Fermi velocity and $v_\Delta$ is related to the gap amplitude. The direction of $\ell_i$ couples to the momentum $\mathbf{p}$, creating an anisotropic spectrum.

In a moving superfluid with flow velocity $\mathbf{v}({\bf r})$, the spectrum is Doppler-shifted:

$$E({\bf r}, \mathbf{p}) \to E({\bf r}, \mathbf{p} - m_3 \mathbf{v}({\bf r}))$$

where $m_3$ is the effective mass.

### Part II: Emergent Metric

#### Painleve-Gullstrand Coordinates

In a fluid flow, the effective spacetime metric for quasiparticles is:

$$ds^2 = -c_0^2 dt^2 + (dx_i - v_i dt)(dx_i - v_i dt)$$

where $c_0$ is the "speed of light" (sound velocity for phonons, group velocity near Fermi surface for fermions) and $\mathbf{v}({\bf r})$ is the flow velocity field.

In Cartesian coordinates:

$$g_{\mu\nu} = \begin{pmatrix}
-c_0^2 + v^2 & -v_x & -v_y & -v_z \\
-v_x & 1 & 0 & 0 \\
-v_y & 0 & 1 & 0 \\
-v_z & 0 & 0 & 1
\end{pmatrix}$$

This is the Painleve-Gullstrand metric — a slicing of Schwarzschild spacetime. It is **curved** with nonzero Riemann tensor:

$$R_{\mu\nu\rho\sigma} \propto \nabla^2 \mathbf{v} + \nabla \nabla^T \mathbf{v}$$

The curvature is determined entirely by the gradient of the flow velocity.

#### Effective Einstein Equation

The Einstein equation in 3+1 dimensions is:

$$G_{\mu\nu} = R_{\mu\nu} - \frac{1}{2} R g_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu}$$

In the analog gravity setting, the "stress-energy tensor" $T_{\mu\nu}$ is the contribution from quasiparticle excitations and vortices. If the superfluid is perfectly uniform (no excitations), then $T_{\mu\nu} = 0$ and $G_{\mu\nu} = 0$, implying flat spacetime.

Volovik showed that the condition $G_{\mu\nu} = 0$ corresponds to the **hydrodynamic equilibrium condition** for the superfluid — the momentum balance equation. Thus:

**Hydrodynamic equilibrium $\Leftrightarrow$ Flatness of effective spacetime**

### Part III: Horizons in Superfluid Flow

#### Ergoregion and Event Horizon

In a rotating superfluid (such as a vortex), the flow velocity exceeds the speed of quasiparticles in some region. Near the vortex axis, define the radius $r_* = v_\phi / c_0$, where $v_\phi$ is the azimuthal velocity and $c_0$ is the speed of sound.

At $r = r_*$, the flow velocity equals the sound speed: $v_\phi(r_*) = c_0$. This is an **event horizon**. Quasiparticles outside this radius can escape to infinity; those inside cannot.

For $r < r_*$, the metric has $g_{00} = -c_0^2 + v_\phi^2 < 0$ everywhere, meaning time-like geodesics cannot reach infinity. This is a **black hole analog**.

#### Hawking Temperature

At the horizon, Hawking's derivation applies. The temperature of the outgoing radiation is:

$$T_H = \frac{\hbar c_0 \kappa}{2\pi k_B}$$

where $\kappa = \frac{d(c_0 - v_\phi)}{dr}|_{r=r_*}$ is the **surface gravity** — the gradient of the flow velocity at the horizon.

For a quantized vortex in 3He-A, $\kappa \sim \Delta / (m_3 v_F \xi)$ where $\Delta$ is the gap, $\xi$ is the coherence length, and $m_3$ is the effective mass. The typical temperature is:

$$T_H \sim \frac{\hbar \Delta}{k_B} \times \text{dimensionless O(1) factors}$$

With $\Delta \sim 1$ mK for 3He at saturating pressure, we get $T_H \sim 10^{-4}$ K — experimentally accessible.

### Part IV: Fermionic Induction of Gravity

#### Effective Gravitational Constant

The coupling strength of the quasiparticle stress-energy to the metric (the effective $8\pi G / c^4$) is determined by the quasiparticle density of states:

$$\frac{1}{G_{eff}} \propto N(E_F)$$

where $N(E_F)$ is the density of fermionic states at the Fermi surface.

In 3He-A, $N(E_F) \sim 10^{23}$ states/cm$^3$/eV — a macroscopic number. Thus $G_{eff}$ is extremely small, explaining why gravitational interactions among quasiparticles are weak.

This mechanism is the condensed matter realization of Sakharov's idea: gravity is **induced** by quantum loops of fermionic matter. The gravitational coupling strength is not fundamental but determined by the matter content.

### Part V: Unruh Effect

#### Accelerated Detectors

An observer accelerating with acceleration $a$ in flat spacetime experiences an effective thermal bath of temperature (Unruh effect):

$$T_U = \frac{\hbar a}{2\pi c k_B}$$

In 3He-A, an excitation propagating through an accelerating superfluid flow experiences an analogous effect. The quasiparticle sees a Doppler-shifted and curved effective metric, giving rise to a thermal spectrum.

The analogy is precise: the Unruh temperature in quasiparticle language is:

$$T_U = \frac{\hbar \nabla^2 v({\bf r})}{2\pi c_0 k_B}$$

where $\nabla^2 v$ is the "acceleration" of the fluid element. Experimental measurement of this temperature confirms the Unruh effect in a quantum system.

---

## Key Results

1. **3He-A quasiparticles obey an effective curved spacetime metric**: The metric is the Painleve-Gullstrand form, with curvature determined by the superfluid texture and flow.

2. **Horizons exist in superfluid vortices**: The vortex core is an event horizon for quasiparticles, with observable Hawking-like radiation.

3. **Hawking temperature is calculable from first principles**: $T_H$ depends on the surface gravity $\kappa$, which is a derivative of the flow velocity — no free parameters.

4. **Gravity is induced by fermionic excitations**: The effective coupling $G_{eff}$ scales inversely with the density of states, realizing Sakharov's mechanism.

5. **The Unruh effect is observable**: Accelerated flows produce thermal spectra for quasiparticles, confirming relativistic quantum field theory in curved spacetime predictions.

6. **Lorentz violation is absent**: 3He-A at low energy has exact Lorentz symmetry to the precision of microscopic physics (trans-Planckian details are invisible).

---

## Impact and Legacy

This paper initiated the field of analog gravity. Major subsequent developments:

- **BEC analogs** (2010s): Hawking radiation observed in laboratory condensates (Steinhauer et al. at Technion, 2016).

- **Ion and photonic analogs** (2010s-2020s): Quantum simulators and photonic systems exhibiting analogs of black holes, white holes, and other GR phenomena.

- **Rotating cylinder black hole analogs** (2010s): Rotating flows in condensates creating ergoregions and Penrose process analogs.

- **Quantum simulation of cosmology**: Expanding condensates as analogs of an expanding universe, allowing tests of inflation and particle creation.

- **Experimental hawking temperature measurements** (Steinhauer 2016, others): Direct observation of thermal spectrum from an analog horizon.

---

## Connection to Phonon-Exflation Framework

The superfluid 3He-A model is the **direct physical blueprint for phonon-exflation**:

1. **Order parameter texture = internal geometry**: In phonon-exflation, the K_7 BCS condensate on SU(3) has an order parameter whose texture encodes the internal geometry. Like 3He-A, this texture modulates the quasiparticle spectrum.

2. **Emergent metric from quasiparticles**: Just as 3He-A fermions induce an effective metric via their coupling to texture, phonon-exflation's particles (phononic excitations) induce the 4D metric via the spectral action.

3. **Horizons and particle creation**: The cosmological horizon in phonon-exflation (the boundary of the observable universe) is analogous to the quasiparticle horizon in a vortex. Expansion (changing scale of the internal geometry) creates particles, like Hawking radiation from an expanding horizon.

4. **Unruh effect = expansion**: The acceleration of cosmic expansion plays the role of the accelerating observer in the Unruh effect. The GGE relic (permanent non-thermal state) is the analog of the Unruh spectrum.

5. **Three dimensions of internal space = three spatial dimensions**: The K_7 condensate on SU(3) has 3 dimensions of internal structure; this emerges as the 3 spatial dimensions of 4D spacetime, exactly as 3He-A's 3D fermionic system produces 3+1 dimensional effective spacetime.

6. **Fermionic induction of gravity**: The spectral action is Volovik's mechanism: gravity (curvature) emerges from the density of fermionic states. In phonon-exflation, the Dirac spectrum's density of states determines the cosmological constant and expansion rate.

---

## References

- Volovik, G. E. (1994). "Induced gravity in superfluid 3He." *Journal of Low Temperature Physics*, 104(1), 1-26. arXiv:cond-mat/9307009.

- Hawking, S. W. (1974). "Black hole explosions?" *Nature*, 248(5443), 30-31.

- Unruh, W. G. (1976). "Notes on black-hole evaporation." *Physical Review D*, 14(4), 870.

- Steinhauer, J. (2016). "Observation of quantum Hawking radiation and its entanglement in an analogue white-hole black-hole pair." *Nature Physics*, 12(10), 959-965.
