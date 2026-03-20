# Apparent Weight of Photons

**Authors:** Robert V. Pound, Glen A. Rebka Jr.
**Year:** 1959 (letter); full results 1960
**Journal:** *Physical Review Letters*, **3**(9), 439--441 (1959); *Physical Review Letters*, **4**(7), 337--341 (1960)

---

## Abstract

Pound and Rebka performed the first terrestrial measurement of the gravitational redshift of photons, confirming the prediction of general relativity that a photon climbing out of a gravitational potential well loses energy (and hence decreases in frequency). Using the Mossbauer effect to achieve spectral resolution better than 1 part in $10^{12}$, they measured the frequency shift of 14.4 keV gamma rays from $^{57}$Fe traveling vertically through 22.5 meters in the Jefferson Tower at Harvard University. The measured shift agreed with the GR prediction $\Delta\nu/\nu = gh/c^2$ to within 10% (later improved to 1% by Pound and Snider in 1965). This experiment provided the first direct measurement of the gravitational redshift in a controlled laboratory setting and confirmed that photons have "weight" -- they gain or lose energy in a gravitational field exactly as predicted by the equivalence principle.

---

## Historical Context

### The Gravitational Redshift Prediction

The gravitational redshift is one of the three "classical tests" of general relativity (along with the perihelion advance of Mercury and the deflection of light by the Sun). Einstein predicted it as early as 1907, even before the full development of GR, using only the equivalence principle.

The argument is straightforward: consider a photon emitted at height $h$ in a uniform gravitational field $g$. By the equivalence principle, this is equivalent to a photon emitted in an accelerating elevator. During the time the photon travels to the floor ($t \approx h/c$), the floor has gained velocity $v \approx gt \approx gh/c$. The photon is therefore Doppler-shifted:

$$\frac{\Delta\nu}{\nu} = -\frac{v}{c} = -\frac{gh}{c^2}$$

The negative sign indicates a blueshift for a photon falling downward (gaining energy) and a redshift for a photon climbing upward (losing energy).

In the full GR treatment, the redshift between two static observers at different positions in a Schwarzschild geometry is:

$$\frac{\nu_{receiver}}{\nu_{emitter}} = \sqrt{\frac{g_{00}(r_{emitter})}{g_{00}(r_{receiver})}} = \sqrt{\frac{1 - r_s/r_{emitter}}{1 - r_s/r_{receiver}}}$$

For weak fields ($r_s/r \ll 1$) and small height differences $h = r_{receiver} - r_{emitter}$:

$$\frac{\Delta\nu}{\nu} \approx -\frac{gh}{c^2}$$

recovering the equivalence-principle result.

### Why It Took So Long

The gravitational redshift on Earth is extremely small. For $h = 22.5$ m:

$$\frac{\Delta\nu}{\nu} = \frac{9.8 \times 22.5}{(3\times10^8)^2} = 2.45 \times 10^{-15}$$

This is about 2.5 parts in $10^{15}$ -- far smaller than the natural linewidth of any atomic transition measured by conventional spectroscopy. No technique available before 1958 had the spectral resolution to detect such a tiny shift.

### Astronomical Attempts

Prior attempts focused on astronomical observations. The gravitational redshift at the surface of the Sun (relative to Earth) is:

$$\frac{\Delta\nu}{\nu} = \frac{GM_\odot}{R_\odot c^2} \approx 2.1 \times 10^{-6}$$

This is much larger than the terrestrial value, and several groups attempted to measure it using solar spectral lines. However, systematic effects -- convective motions in the solar atmosphere (the "limb shift"), pressure broadening, and line blending -- made the measurements ambiguous. The results were inconclusive.

The gravitational redshift of the white dwarf Sirius B ($\Delta\nu/\nu \sim 3 \times 10^{-4}$) was observed by Adams (1925), but the measurement was rough and model-dependent.

### The Mossbauer Effect (1958)

The breakthrough came with Rudolf Mossbauer's discovery (1958) that certain nuclear transitions in solids emit and absorb gamma rays with negligible recoil, resulting in spectral lines with widths determined by the natural lifetime of the nuclear excited state rather than by thermal Doppler broadening.

For the 14.4 keV transition in $^{57}$Fe:

- **Natural linewidth:** $\Gamma = \hbar/\tau$ where $\tau = 141$ ns is the excited state lifetime, giving $\Gamma \approx 4.7 \times 10^{-9}$ eV.
- **Fractional width:** $\Gamma/E_\gamma = 4.7 \times 10^{-9}/14.4 \times 10^3 = 3.3 \times 10^{-13}$.

This fractional width is smaller than the gravitational redshift over 22.5 m by a factor of about 7, meaning the shift is in principle resolvable. Mossbauer received the 1961 Nobel Prize for this discovery.

---

## Key Arguments and Derivations

### I. Experimental Setup

**Source:** $^{57}$Co (which decays to $^{57}$Fe*) embedded in an iron foil, mounted at the top (or bottom) of the Jefferson Physics Laboratory tower at Harvard University.

**Absorber:** A $^{57}$Fe-enriched iron foil at the other end of the 22.5 m tower, acting as a resonant absorber.

**Detector:** A scintillation counter behind the absorber, measuring the transmitted gamma-ray intensity.

**Geometry:** The gamma rays travel vertically through the interior of the tower. The experiment alternates between "source at top" (photons fall, blueshift expected) and "source at bottom" (photons rise, redshift expected) to cancel systematic effects.

### II. The Mossbauer Technique

When the source and absorber are at rest and at the same gravitational potential, the emitted gamma rays are resonantly absorbed by the $^{57}$Fe absorber, resulting in a dip in the transmitted count rate.

When the gravitational potential difference introduces a frequency shift $\Delta\nu_{grav}$, the emission and absorption lines no longer overlap perfectly, and the absorption decreases.

To measure the shift, Pound and Rebka modulated the source frequency by Doppler shifting -- moving the source with a known velocity $v$. The Doppler shift is:

$$\frac{\Delta\nu_{Doppler}}{\nu} = \frac{v}{c}$$

By scanning $v$ and measuring the transmission as a function of $v$, they traced out the Mossbauer resonance curve. The gravitational redshift appears as a displacement of the resonance center from $v = 0$.

The velocity corresponding to the gravitational shift is:

$$v_{grav} = \frac{gh}{c} = \frac{9.8 \times 22.5}{3\times10^8} = 7.35 \times 10^{-7}\;\text{m/s} = 0.735\;\mu\text{m/s}$$

This is an absurdly small velocity -- about 2.3 mm per hour -- but the Mossbauer technique can resolve velocities at this level.

### III. The Modulation Technique

Pound and Rebka used a sinusoidal velocity modulation (by mounting the source on a loudspeaker cone) and detected the count rate at the modulation frequency using a lock-in technique. This converts the DC measurement (absolute count rate) into an AC measurement (count rate modulation), which is far less susceptible to drifts and systematic effects.

The transmitted count rate as a function of source velocity $v$ near resonance is approximately:

$$N(v) = N_0\left[1 - f\frac{(\Gamma/2)^2}{(\Delta E - E_0 v/c)^2 + (\Gamma/2)^2}\right]$$

where $f$ is the Mossbauer fraction (recoil-free fraction), $\Gamma$ is the natural linewidth, and $\Delta E = E_\gamma g h/c^2$ is the gravitational energy shift.

### IV. Systematic Effects

The major systematic effects were:

**Temperature difference:** A temperature difference $\Delta T$ between source and absorber produces a second-order Doppler shift (time dilation due to thermal atomic velocities):

$$\frac{\Delta\nu}{\nu}\bigg|_{thermal} = -\frac{3k_B\Delta T}{2mc^2}$$

where $m$ is the mass of the $^{57}$Fe nucleus. For $\Delta T = 1$ K, this is $\sim 2.4 \times 10^{-15}$, comparable to the gravitational shift. Pound and Rebka monitored temperatures carefully and applied corrections.

**Source and absorber tilts:** Any tilt introduces a horizontal component that changes the effective height difference.

**Electronic drifts:** Addressed by the lock-in modulation technique and by frequently alternating the source and absorber positions.

### V. Results

**1959 (Pound and Rebka):**

$$\frac{\Delta\nu}{\nu}\bigg|_{measured} = (5.13 \pm 0.51) \times 10^{-15}$$

$$\frac{\Delta\nu}{\nu}\bigg|_{predicted} = 4.905 \times 10^{-15}$$

The measured value was $(1.05 \pm 0.10)$ times the predicted value -- agreement to 10%.

**1965 (Pound and Snider):**

Using improved techniques (better temperature control, longer integration):

$$\frac{\Delta\nu}{\nu}\bigg|_{measured} = (0.9990 \pm 0.0076) \times \frac{\Delta\nu}{\nu}\bigg|_{predicted}$$

Agreement to better than 1%.

---

## Physical Interpretation

### Photons Have Weight

The experiment directly demonstrates that photons are affected by gravity -- they gain energy (blueshift) when falling and lose energy (redshift) when climbing. In the language of the equivalence principle, a photon in a gravitational field behaves as if it has mass $m = E/c^2 = h\nu/c^2$. It gains kinetic energy $mgh = h\nu \cdot gh/c^2$ when falling through height $h$, corresponding to a frequency increase $\Delta\nu = \nu gh/c^2$.

### Gravitational Time Dilation

An equivalent interpretation: the gravitational redshift reflects the fact that clocks run at different rates at different heights in a gravitational field. A clock at the bottom of the tower runs slower (by the fraction $gh/c^2$) than a clock at the top. The gamma-ray photon acts as a clock (its frequency is its "tick rate"), and the observed frequency shift is the difference in clock rates.

This interpretation connects directly to the metric: the proper time interval at height $h$ is:

$$d\tau = \sqrt{-g_{00}}\,dt \approx \left(1 + \frac{gh}{c^2}\right)dt$$

Clocks at higher gravitational potential run faster.

### The Equivalence Principle Confirmed

The Pound-Rebka experiment tests the **weak equivalence principle** (universality of free fall applied to photons) and the **Einstein equivalence principle** (equivalence of gravity and acceleration for all non-gravitational physics). The 1% agreement with GR provides strong evidence that gravity couples universally to energy, not just to mass.

---

## Impact and Legacy

### Precision Gravitational Redshift Tests

The Pound-Rebka/Snider experiments opened the field of precision gravitational redshift measurements:

**Gravity Probe A (1976):** Vessot and Levine launched a hydrogen maser clock on a suborbital rocket to 10,000 km altitude and compared its frequency with a ground-based maser. Result: $(1.000 \pm 0.0002)$ times the GR prediction -- agreement to 0.02%.

**Optical clocks (2010s-2020s):** Modern optical lattice clocks have frequency stability of $\sim 10^{-18}$, sufficient to detect the gravitational redshift over a height difference of 1 cm on Earth. Bothwell et al. (2022) measured the gravitational redshift across a single atomic sample with millimeter-scale resolution.

### GPS and Everyday Technology

The Global Positioning System relies on atomic clocks aboard satellites at altitude $\sim 20,200$ km. The gravitational blueshift of the satellite clocks (relative to ground) is $\sim 5.2 \times 10^{-10}$, corresponding to about 45 microseconds per day. Without correcting for this GR effect (and the special-relativistic time dilation of -7 microseconds/day for the satellite's orbital velocity), GPS positions would drift by $\sim 10$ km per day.

### Tests of the Equivalence Principle

The gravitational redshift is one of the three pillars of the Einstein equivalence principle (along with the universality of free fall and local position invariance). Precision redshift tests constrain violations of local position invariance -- the possibility that the outcome of a non-gravitational experiment depends on where and when it is performed. Current bounds from atomic clock comparisons constrain such violations at the $10^{-7}$ level.

---

## Connections to Modern Physics

### Quantum Clocks and Gravitational Entanglement

Modern proposals aim to observe gravitational effects on quantum superpositions. If a quantum clock is placed in a superposition of two heights, the gravitational time dilation produces a relative phase:

$$\Delta\phi = \frac{mc^2}{\hbar}\int\left(\sqrt{-g_{00}(h_1)} - \sqrt{-g_{00}(h_2)}\right)dt \approx \frac{mg\Delta h}{\hbar}t$$

This phase is observable interferometrically and represents a genuinely quantum-gravitational effect (Zych et al., 2011). Atom interferometry experiments have already measured this phase, confirming the quantum-mechanical response to gravitational time dilation.

### Gravitational Redshift in Strong Fields

For compact objects (neutron stars, black holes), the gravitational redshift is large. A photon emitted from the surface of a neutron star ($M \sim 1.4\,M_\odot$, $R \sim 10$ km) is redshifted by:

$$z = \frac{1}{\sqrt{1 - r_s/R}} - 1 \approx 0.3$$

This $\sim 30\%$ redshift is directly observable in X-ray spectroscopy of neutron stars and is used to constrain the nuclear equation of state (which determines $R$ for a given $M$).

At the event horizon of a black hole ($r = r_s$), the redshift diverges: $z \to \infty$. This is the physical basis for the "frozen star" appearance of a collapsing object (Oppenheimer-Snyder, Paper 12).

### The Unruh Effect and Gravitational Redshift

The equivalence principle connects the gravitational redshift to the Unruh effect: an accelerating detector in flat spacetime sees thermal radiation at temperature $T = \hbar a/(2\pi c k_B)$. This is the "acceleration radiation" analog of the gravitational redshift -- both arise from the equivalence of gravity and acceleration. The Unruh effect has not been directly observed (the required acceleration is enormous: $T = 1$ K requires $a \sim 2.5 \times 10^{20}$ m/s$^2$), but analog experiments in BEC systems and superconducting circuits are approaching the relevant regime.

### Mossbauer Effect and Phonon Physics

The Mossbauer effect itself is fundamentally a phonon phenomenon: recoil-free emission occurs because the recoil momentum is absorbed by the entire crystal lattice (zero-phonon transition) rather than by the emitting nucleus alone. The probability of recoil-free emission (the Lamb-Mossbauer factor) is:

$$f = \exp\left(-\frac{E_\gamma^2 \langle x^2\rangle}{\hbar^2 c^2}\right)$$

where $\langle x^2\rangle$ is the mean-squared displacement of the nucleus in the lattice. This connection between nuclear physics and lattice dynamics (phonons) is a concrete example of how collective excitations of a structured medium mediate fundamental physical measurements.
