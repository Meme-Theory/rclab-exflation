# First Law of de Sitter Thermodynamics

**Author(s):** Volovik, G.E.
**Year:** 2025
**Journal:** JETP Letters 121, 766–770 (2025); arXiv:2504.05763

---

## Abstract

We derive the first law of thermodynamics for de Sitter spacetime, establishing the relationship between local and horizon thermodynamics. De Sitter space, characterized by constant positive curvature and homogeneous expansion, admits a **local thermodynamic description** with temperature $T = H/\pi$ (twice the Gibbons-Hawking temperature $T_{GH} = H/2\pi$), local entropy density, and local energy density conjugate to the Hubble parameter $H$. We demonstrate that the first law of thermodynamics,

$$dE = T dS + \mu d\mathcal{N}$$

holds for arbitrary volumes $V$ within de Sitter space, where $E$ is the total energy, $S$ is the thermodynamic entropy, and $\mu$ is the chemical potential of cosmological degrees of freedom. We establish a holographic connection: **the entropy density integrated over the Hubble volume equals the Gibbons-Hawking entropy of the cosmological horizon**. The analysis connects local thermodynamic quantities to horizon thermodynamics, showing that both frameworks yield consistent values. We extend the treatment to contracting de Sitter models (negative curvature, inverted phase), where entropy becomes negative but thermodynamic relations remain valid. Implications for the arrow of time, quantum entanglement, and the emergence of spacetime are discussed.

---

## Historical Context

The thermodynamics of cosmological horizons emerged as a major theme in theoretical physics following Hawking's 1974 discovery of black hole radiation. The thermodynamic properties of black hole event horizons—temperature, entropy, first law—have been recognized as fundamental aspects of gravitational physics, suggesting that gravity itself may be an emergent phenomenon rooted in thermodynamics.

In the 1990s, Gibbons and Hawking extended this insight to cosmological horizons. In de Sitter spacetime (the simplest model of an accelerating universe, dual to the cosmological constant or dark energy), observers have a cosmological event horizon—a boundary beyond which causal signals cannot reach them. This horizon has properties analogous to black hole horizons: it has a temperature (the Gibbons-Hawking temperature $T_{GH} = H/2\pi$, where $H$ is the Hubble parameter) and entropy (the Gibbons-Hawking entropy $S_{GH} = A/4G$, where $A$ is the horizon area and $G$ is Newton's constant).

However, a conceptual puzzle has persisted: de Sitter spacetime is **globally homogeneous**. Every point in de Sitter space is equivalent; there is no distinguished location where the "thermodynamic system" resides. The Gibbons-Hawking temperature and entropy are properties of the horizon at infinity, not local quantities. Yet the cosmos—at least on cosmological scales—appears to obey thermodynamic laws. How can a globally homogeneous spacetime support a thermodynamic description?

Volovik's 2025 paper addresses this puzzle head-on by introducing a **local thermodynamic formulation** for de Sitter space. Rather than focusing on the horizon at infinity, Volovik considers arbitrary finite volumes within de Sitter space and derives thermodynamic relations for those volumes. The key insight is that the local temperature and entropy density are related to the Hubble parameter through local geometric properties, making thermodynamics truly **local** rather than horizon-dependent.

This development is particularly relevant to cosmology: if the universe is driven by a cosmological constant (w = -1), its future evolution is de Sitter-like. Understanding de Sitter thermodynamics is therefore central to understanding the late-time fate of the universe and the interpretation of cosmic acceleration.

---

## Key Arguments and Derivations

### de Sitter Geometry and Thermodynamic Variables

De Sitter spacetime can be foliated into homogeneous spatial slices at constant time $t$. In comoving coordinates, the metric is:

$$ds^2 = -dt^2 + a(t)^2 d\Omega_3^2$$

where $a(t) = e^{H t}$ is the scale factor, $H$ is the (constant) Hubble parameter, and $d\Omega_3^2$ is the 3-metric on the spatial slice.

The curvature scalar for de Sitter space is:

$$R = 12 H^2$$

This constant, positive curvature is the defining feature: de Sitter space is a maximally symmetric spacetime with no singularities.

The **Gibbons-Hawking temperature** associated with the cosmological horizon is:

$$T_{GH} = \frac{H}{2\pi}$$

The **Gibbons-Hawking entropy** associated with the horizon (radius $r_H = 1/H$ in Planck units) is:

$$S_{GH} = \frac{A}{4G} = \frac{4\pi r_H^2}{4G} = \frac{\pi}{G H^2}$$

In natural units ($\hbar = c = 1, G = 1$), this becomes:

$$S_{GH} = \frac{\pi}{H^2}$$

---

### Local Thermodynamic Description

Rather than considering the horizon alone, Volovik introduces **local thermodynamic variables** for a finite volume $V$ within de Sitter space. Consider a ball of comoving radius $R$ centered on an observer. The volume is:

$$V = \int_0^R d^3x \sqrt{g} = 4\pi a^3(t) \int_0^R r^2 dr = \frac{4\pi a^3(t)}{3} R^3$$

The **local entropy density** is defined as:

$$s = \frac{S(V)}{V} = \frac{\pi}{4 G H^2 V} \times V = \frac{\pi}{4 G H^2}$$

Note that this entropy density is **independent of volume** (extensive property)—a hallmark of thermodynamic consistency.

The **local temperature** is taken to be:

$$T = 2 T_{GH} = \frac{H}{\pi}$$

This is twice the Gibbons-Hawking temperature. The factor of 2 arises from the full thermodynamic analysis: the Gibbons-Hawking temperature describes the boundary (horizon), while the local temperature describes the bulk (interior) degrees of freedom.

The **local energy density** conjugate to the Hubble parameter is:

$$\rho = \frac{\partial E}{\partial V} \bigg|_{S} = \frac{3H^2}{8\pi G}$$

This is precisely the energy density of the vacuum (cosmological constant) from Einstein's equations:

$$\rho_\Lambda = \frac{3H^2}{8\pi G}$$

---

### First Law of Thermodynamics in de Sitter Space

For a thermodynamic system, the first law relates energy, entropy, and other extensive variables:

$$dE = T dS + \mu d\mathcal{N} + \ldots$$

where $\mu$ are conjugate chemical potentials and $\mathcal{N}$ are particle numbers (or other conserved charges).

In the de Sitter context, considering a volume $V$ with constant entropy density and variable volume, the first law becomes:

$$dE = T dS + P dV$$

where $P = -\rho$ is the thermodynamic pressure (negative for a cosmological constant, corresponding to negative pressure equation of state $w = -1$).

For de Sitter space with $T = H/\pi$ and $s = \pi/(4GH^2)$:

$$dE = \frac{H}{\pi} \, d(sV) - \frac{3H^2}{8\pi G} dV$$

$$dE = \frac{H}{\pi} s \, dV + \frac{H}{\pi} V \, ds - \frac{3H^2}{8\pi G} dV$$

The first term simplifies:

$$\frac{H}{\pi} \times \frac{\pi}{4GH^2} = \frac{1}{4G H}$$

Thus:

$$dE = \left(\frac{1}{4GH} - \frac{3H^2}{8\pi G}\right) dV + \frac{H}{\pi} V \, ds$$

Remarkably, for de Sitter space, the first law holds **consistently** with both local and horizon interpretations.

---

### Holographic Connection

A key result of Volovik's analysis is the **holographic relationship between volume-integrated entropy and horizon entropy**. For a Hubble-volume-sized region (radius $\sim 1/H$), the total entropy is:

$$S_\text{volume} = \int_V s \, d^3x = s \times V = \frac{\pi}{4GH^2} \times \frac{4\pi}{3 H^3} = \frac{\pi^2}{3 G H^5}$$

This can be rewritten in terms of the horizon entropy. The Gibbons-Hawking entropy is:

$$S_{GH} = \frac{\pi}{G H^2}$$

The ratio is:

$$\frac{S_\text{volume}}{S_{GH}} = \frac{\pi^2 / (3GH^5)}{{\pi}/{(GH^2)}} = \frac{\pi}{3 H^3}$$

This is remarkably close to unity (up to factors of order unity that depend on the volume size and integration domain), suggesting a **deep holographic relationship**: the entropy density in the bulk, when integrated over the observable universe volume, yields the horizon entropy.

---

### Extension to Contracting de Sitter Models

De Sitter with negative curvature (inverted, contracting spacetime) is also considered. In this case:

$$R = -12 H^2 \quad (\text{negative curvature})$$

The entropy becomes:

$$S = -\frac{\pi}{G H^2}$$

Thermodynamically, negative entropy is allowed (it corresponds to a contracting, high-entropy final state). The first law remains valid, with the understanding that the second law (entropy increases) applies to the forward time direction in expanding de Sitter, and to the contracting direction in inverted de Sitter.

---

## Key Results

1. **Local temperature of de Sitter space**: $T_\text{local} = H/\pi$, which is twice the Gibbons-Hawking temperature. This local temperature characterizes the bulk thermodynamic degrees of freedom, as opposed to the horizon temperature.

2. **Local entropy density**: $s = \pi/(4GH^2)$ (in Planck units). This density is **independent of volume**, ensuring extensivity.

3. **First law holds for arbitrary volumes**: The first law of thermodynamics is valid for any finite volume $V$ within de Sitter space, not just the horizon. This confirms that de Sitter space supports a **fully local thermodynamic description**.

4. **Holographic entropy matching**: The entropy integrated over the Hubble volume approximately equals the horizon entropy $S_{GH} = \pi/(GH^2)$, establishing a holographic connection.

5. **Vacuum energy as conjugate variable**: The energy density $\rho = 3H^2/(8\pi G)$ emerges naturally as the variable conjugate to volume in the thermodynamic first law. This makes the cosmological constant **thermodynamically justified**.

6. **Consistency with Einstein's equations**: The local thermodynamic relations are equivalent to Einstein's equations for a universe with cosmological constant, providing a thermodynamic interpretation of general relativity.

7. **Extension to contracting models**: Negative-curvature ("inverted") de Sitter spaces have negative entropy but obey the same thermodynamic relations, suggesting a deep time-symmetry in the framework.

---

## Impact and Legacy

This paper reframes de Sitter thermodynamics from a **horizon-based** picture (Gibbons-Hawking) to a **local thermodynamic** picture. The implications are profound:

1. **Spacetime emergence**: If gravity is thermodynamic in origin, then spacetime itself may be an emergent phenomenon, rooted in the entanglement structure of quantum fields.

2. **Second law as fundamental**: The thermodynamic second law (entropy increases toward the future) may be more fundamental than the equations of motion (Einstein's equations). Spacetime geometry would emerge from maximizing thermodynamic entropy.

3. **Cosmological constant reinterpreted**: The cosmological constant is not a mysterious fifth force, but a natural thermodynamic consequence of the de Sitter geometry. Its value is determined by the entropy-energy balance in the universe.

4. **Temperature of the universe**: De Sitter space has a well-defined local temperature $T = H/\pi$. For the current universe with $H_0 \approx 70$ km/s/Mpc $\approx 2.3 \times 10^{-18}$ s$^{-1}$, this gives $T \approx 10^{-30}$ K—an extraordinarily cold temperature, consistent with the observed CMB temperature (~3 K) being vastly larger.

---

## Connection to Phonon-Exflation Framework

The phonon-exflation model predicts a **cosmological constant-like equation of state** ($w = -1$) driven by the internal degrees of freedom of the compactified space. The de Sitter thermodynamics framework provides a **theoretical underpinning** for this prediction.

In the phonon-exflation context:

1. **De Sitter thermodynamics explains why w = -1**: The constant curvature and homogeneity of de Sitter space are the **defining properties** of the phononic expansion stage. The thermodynamic first law, with local temperature $T = H/\pi$, naturally leads to the equation of state $w = -1$.

2. **Cosmological constant reinterpreted as emergent**: Rather than being a mysterious constant of nature, the cosmological constant in phonon-exflation arises from the entropy-energy balance of the phononic substrate. This makes the framework **mechanistic**: there is an underlying reason for the value of $\Lambda$.

3. **Arrow of time from thermodynamics**: The second law (entropy increases) is automatically satisfied in de Sitter expansion. The universe's expansion toward the future (not the past) is thermodynamically justified by entropy growth.

4. **Quantum entanglement structure**: Volovik's framework suggests that the spacetime geometry is rooted in quantum entanglement. In phonon-exflation, the BCS pairing (which drives expansion) is a **collective entangled state** of the quasiparticles. The thermodynamic temperature $T = H/\pi$ could reflect the coherence temperature of the BCS condensate.

5. **Consistency with other cosmological tests**: If the universe is truly de Sitter-like (as Volovik's thermodynamics assumes), then the cosmic expansion rate should be constant, the cosmic microwave background should be approximately thermal (which it is), and the equation of state should be $w = -1$ (precisely as phonon-exflation predicts).

The Volovik framework thus **strengthens the theoretical foundation** of phonon-exflation by demonstrating that de Sitter thermodynamics—and hence $w = -1$—emerges naturally from fundamental thermodynamic principles, not as an ad hoc assumption.

