# Event Horizons and Ergoregions in 3He

**Author(s):** T.A. Jacobson, G.E. Volovik
**Year:** 1998
**Journal:** Physical Review D (submitted); cond-mat/9801308
**arXiv:** cond-mat/9801308
**Relevance:** HIGH

---

## Abstract

Event horizons for fermion quasiparticles naturally arise in moving textures in superconductors and Fermi superfluids. We discuss the example of a planar soliton moving in superfluid 3He-A, which is closely analogous to a charged rotating black hole. The moving soliton will radiate quasiparticles via the Hawking effect at a temperature of about 5 $\mu$K, and via vacuum polarization induced by the effective 'electromagnetic field' and 'ergoregion'. Superfluid 3He-A thus appears to be a useful system for experimental and theoretical simulations of quantum effects related to event horizons and ergoregions.

---

## Key Arguments and Derivations

### Relativistic Fermions in 3He-A (Section II)

In superfluid 3He-A, the spontaneous symmetry breaking is characterized by the unit vector $\hat{l}$ (direction of spontaneous angular momentum of Cooper pairs). The Bogoliubov-Nambu quasiparticle spectrum near the two nodal points $\mathbf{p} = e\mathbf{A}$ (with $\mathbf{A} = p_F\hat{l}$ and $e = \pm 1$) becomes that of a charged, massless, relativistic particle in curved spacetime with electromagnetic vector potential:
$$g^{\mu\nu}(p_\mu - eA_\mu)(p_\nu - eA_\nu) = 0$$

The components (in the coordinate system at rest w.r.t. the superfluid) are:
- $(p_0, p_i) = (-E, p_i)$
- $(A_0, A_i) = (0, p_F l_i)$
- $g^{00} = -1$, $g^{0i} = 0$, $g^{ik} = c_\perp^2(\delta^{ik} - l_il_k) + c_\parallel^2 l_i l_k$

The "speeds of light" are highly anisotropic: $c_\perp = \Delta_A/p_F \approx 3$ cm/s (transverse) and $c_\parallel = v_F \approx 55$ m/s (parallel to $\hat{l}$), giving $c_\perp \approx 0.5 \times 10^{-3}c_\parallel$. The relativistic approximation holds for $E \ll m^*c_\perp^2 \sim 0.5$ $\mu$K.

The quasiparticles satisfy the curved-spacetime Weyl equation for massless charged chiral spinors.

### Moving Soliton: Analogue of Charged Rotating Black Hole (Section III)

A topologically stable "splay soliton" (vierbein domain wall) moving with velocity $v$ in the $z$-direction has the $\hat{l}$-profile $\hat{l} = -\hat{z}\tanh(z/d) + \hat{x}\,\mathrm{sech}(z/d)$ (thickness $d \sim \xi_D \sim 10$ $\mu$m).

In the comoving frame, the inverse metric has components:
$$g^{00} = -1,\quad g^{0z} = v,\quad g^{yy} = c_\perp^2,\quad g^{zz} = c_\perp^2\sin^2\alpha + v_F^2\cos^2\alpha - v^2$$
$$g^{xx} = c_\perp^2\cos^2\alpha + v_F^2\sin^2\alpha,\quad g^{zx} = (v_F^2 - c_\perp^2)\sin\alpha\cos\alpha$$

and the vector potential $A_0 = vp_F\cos\alpha$, $A_x = p_F\sin\alpha$, $A_z = p_F\cos\alpha$.

### Schwinger Pair Production (Section IV)

The moving soliton's electromagnetic field has $F_{zx} = p_F\partial_z\sin\alpha$ and $F_{0z} = vp_F\partial_z\cos\alpha$. The invariant $B^2 - E^2 \propto v_F^2 c_\perp^2 F_{zx}^2(1 - v^2\cos^2\alpha/v_F^2)$ vanishes at two planes $\cos^2\alpha(z_p) = v^2/v_F^2$, between which $E^2 > B^2$ and Schwinger pair production occurs. This causes friction on the soliton even at $T = 0$.

### Event Horizons (Section V)

Horizons occur where $g^{zz} = 0$, i.e.:
$$c_\perp^2\sin^2\alpha(z_h) + v_F^2\cos^2\alpha(z_h) = v^2$$

This means $c_z(z_h) = v$ where $c_z$ is the speed of light in the $z$-direction. The region between the two horizons $\pm z_h$ traps quasiparticles (they cannot propagate faster than the soliton). The leading horizon is a black hole, the trailing is a white hole.

Horizons exist for $v > c_\perp$. The condition is physically reasonable since $c_\perp \approx 3$ cm/s while texture velocities can approach $v_F \approx 55$ m/s.

### Ergoregion (Section V)

The ergoregion boundary (ergoplanes) occurs where $g_{tt} = 0$:
$$\cos^2\alpha(z_e) = \frac{1 - c_\perp^2/v^2}{1 - c_\perp^2/v_F^2}$$

An ergoregion exists if and only if there is an event horizon ($v > c_\perp$). The ergoplanes lie outside the event horizons (and outside the Schwinger pair region) for $v$ not too close to $c_\perp$.

### Transverse Velocity and Surface Gravity

The horizon has a "transverse velocity" $w$ (analogous to the rotational velocity of a rotating BH):
$$w = v_F\sqrt{\frac{1 - v^2/v_F^2}{1 - c_\perp^2/v^2}}$$

The horizon-generating Killing field is $\chi = \partial_t + w\partial_x$.

The surface gravity:
$$\kappa = \frac{dg^{zz}/dz}{2v}\bigg|_h = (dc_z/dz)|_h = \frac{v_F}{d}(1 - v^2/v_F^2)\sqrt{\frac{1 - c_\perp^2/v^2}{1 - c_\perp^2/v_F^2}}$$

### Hawking Radiation (Section VI)

The Hawking temperature:
$$T_H = \frac{\hbar\kappa}{2\pi k_B}$$

For $v$ not too close to $c_\perp$ or $v_F$: $\kappa \approx v_F/d$, giving $T_H \approx 5$ $\mu$K. This is an order of magnitude below the lowest confirmed temperature in 3He experiments but an order above the temperature where nonrelativistic corrections become important.

The Hawking flux for fermions: $\Gamma[e^{(E - \mu)/k_BT_H} + 1]^{-1}$ with chemical potential $\mu = p_x w + eA_0(z_h)$ (analogous to $\mu = J\Omega + e\Phi$ for a rotating charged BH).

---

## Key Results

1. A moving soliton (vierbein domain wall) in 3He-A is closely analogous to a charged, rotating black hole for fermionic quasiparticles.
2. Event horizons form when the soliton velocity exceeds $c_\perp \approx 3$ cm/s (the transverse "speed of light").
3. Three dissipation mechanisms operate simultaneously: Schwinger pair production (electromagnetic), ergoregion pair production, and Hawking radiation.
4. The Hawking temperature is $T_H \approx 5$ $\mu$K, determined by $\kappa \approx v_F/d$.
5. The ergoregion exists if and only if there is an event horizon (unlike Kerr black holes where the ergosphere exists even for non-rotating BHs with charge).
6. The superfluid condensate remains at rest (no Landau critical velocity violation), while the texture moves superluminally -- resolving the obstacle of condensate collapse.
7. The "chemical potential" for Hawking radiation includes both transverse velocity (angular momentum analog) and electromagnetic potential contributions.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Quasiparticle dispersion | $E(\mathbf{p}) = \pm\sqrt{v_F^2(p-p_F)^2 + (\Delta_A^2/p_F^2)(\hat{l}\times\mathbf{p})^2}$ | Eq. (2.1) |
| Covariant dispersion | $g^{\mu\nu}(p_\mu - eA_\mu)(p_\nu - eA_\nu) = 0$ | Eq. (2.2) |
| Inverse metric (rest frame) | $g^{ik} = c_\perp^2(\delta^{ik} - l_il_k) + c_\parallel^2 l_il_k$ | Eq. (2.3c) |
| Speeds of light | $c_\perp = \Delta_A/p_F \approx 3$ cm/s; $c_\parallel = v_F \approx 55$ m/s | Text |
| Soliton profile | $\hat{l} = -\hat{z}\tanh(z/d) + \hat{x}\,\mathrm{sech}(z/d)$ | Eq. (3.2) |
| Moving frame metric | $g^{zz} = c_\perp^2\sin^2\alpha + v_F^2\cos^2\alpha - v^2$ | Eq. (3.4) |
| Schwinger invariant | $B^2 - E^2 \propto (1 - v^2\cos^2\alpha/v_F^2)$ | Eq. (4.3) |
| Horizon condition | $c_\perp^2\sin^2\alpha + v_F^2\cos^2\alpha = v^2$ | Eq. (5.1) |
| Ergoplane condition | $\cos^2\alpha(z_e) = (1 - c_\perp^2/v^2)/(1 - c_\perp^2/v_F^2)$ | Eq. (5.3) |
| Transverse velocity | $w = v_F\sqrt{(1-v^2/v_F^2)/(1-c_\perp^2/v^2)}$ | Eq. (5.5) |
| Surface gravity | $\kappa = (v_F/d)(1-v^2/v_F^2)\sqrt{(1-c_\perp^2/v^2)/(1-c_\perp^2/v_F^2)}$ | Eq. (5.7) |
| Hawking temperature | $T_H = \hbar\kappa/(2\pi k_B)$ | Eq. (6.1) |
| Hawking chemical potential | $\mu = p_x w + eA_0(z_h)$ | Eq. (6.3) |

---

## Relevance to Phonon-Exflation

This paper demonstrates that fermionic quasiparticles in 3He-A experience event horizons, ergo-regions, and Hawking radiation from moving textures -- establishing that the full machinery of curved-spacetime QFT applies to condensed matter systems with fermionic, not just bosonic, excitations. For the phonon-exflation framework, this is significant because: (1) the quasiparticle dispersion near Fermi points is that of chiral Weyl fermions in curved spacetime with gauge fields, directly paralleling the framework's claim that SM fermions are fermionic excitations of the M4 x SU(3) substrate; (2) the resolution of the condensate collapse problem (texture moves while condensate stays at rest) maps to the framework's mechanism where the fiber modulus changes while the spatial manifold remains static; (3) the simultaneous appearance of gravitational (horizon), electromagnetic (Schwinger), and rotational (ergoregion) effects from a single texture demonstrates the unified emergence of multiple forces from substrate dynamics. The anisotropic "speeds of light" ($c_\perp/c_\parallel \sim 10^{-3}$) foreshadow the framework's anisotropic effective metrics from the SU(3) fiber geometry.
