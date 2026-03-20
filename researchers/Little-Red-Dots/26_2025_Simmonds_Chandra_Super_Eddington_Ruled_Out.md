# Chandra Rules Out Super-Eddington Accretion Models for Little Red Dots

**Authors:** Andrea Sacchi (lead), Akos Bogdan, and collaborators

**Year:** 2025

**Journal:** *The Astrophysical Journal Letters*, accepted (arXiv:2505.09669)

---

## Abstract

We present deep Chandra X-ray stacking analysis of 55 Little Red Dots in the CDFS and COSMOS fields, accumulating 400 megaseconds of total exposure. Despite this unprecedented depth, we detect no significant X-ray signal, setting strict upper limits on 2-10 keV luminosity. These limits rule out standard super-Eddington accretion models (L_X/L_Bol ~ 10^{-2}) and instead require hydrogen column densities exceeding $N_H > 10^{25} \, \text{cm}^{-2}$ for all sources. We interpret LRDs as heavily obscured, Compton-thick AGN with accretion rates potentially sub-Eddington, resolved only through far-IR/submillimeter dust re-radiation and optical recombination lines in ionized gas envelopes. This resolves the X-ray weakness problem and tightens mass and accretion rate estimates.

---

## Historical Context

Early high-z AGN are expected to be bright X-ray sources. Standard accretion physics predicts that a black hole accreting at rate $\dot{M}$ radiates bolometric luminosity:

$$L_{\text{bol}} = \epsilon \dot{M} c^2$$

where the radiative efficiency $\epsilon \sim 0.1$ for standard thin disks. The X-ray component (hard X-rays, 2-10 keV) typically comprises 10-20% of the bolometric luminosity in optically unobscured AGN:

$$\frac{L_X}{L_{\text{bol}}} \sim 0.1 - 0.2$$

However, Little Red Dots (LRDs) exhibit a striking anomaly: they have strong optical/UV continua and broad emission lines (Hβ, Hα), which diagnostically indicate high accretion rates ($\dot{M} > \dot{M}_{\text{Edd}}$), yet appear *extremely faint* in X-rays. This X-ray weakness ratio:

$$\alpha_{ox} = \log \left( \frac{\nu L_\nu(2 \text{ keV})}{\nu L_\nu(2500 \text{ Å})} \right)$$

is 0.5-1.0 dex *below* the standard AGN $\alpha_{ox}$ relation, a 3-10× deficit.

Prior explanations invoked:

1. **Super-Eddington accretion with advection-dominated flow (ADF)**: Accretion rates $\dot{M} \gg \dot{M}_{\text{Edd}}$ produce X-ray-weak, UV-bright states analogous to tidal disruption events (TDEs). This was theoretically attractive because it explained rapid early black hole assembly.

2. **Intrinsic X-ray weakness from magnetic field suppression**: Strong magnetic fields in super-Eddington flows reduce X-ray production.

3. **Extreme dust obscuration**: High column density ($N_H > 10^{24} \, \text{cm}^{-2}$) absorbs X-rays preferentially due to the sharp photo-electric absorption edge at ~7 keV (iron K-edge).

Simmonds et al. (2025) provided the first definitive test: stacking 55 LRDs in the deepest Chandra fields (CDFS ~400 ks total, COSMOS ~150 ks total) to a combined depth of 400 Ms. The result: no X-ray detection. This *rules out* super-Eddington accretion models that predict detectable X-ray luminosity even in obscured states.

---

## Key Arguments and Derivations

### X-ray Stacking and Noise Characterization

Chandra stacking analysis assumes that faint sources below the individual detection threshold (typically $\sim 5 \sigma$ for 0.5-10 keV photons) can be recovered by co-adding flux in a manner insensitive to instrumental noise.

For $N$ objects at redshift $z$, the stacked 2-10 keV flux limit is:

$$F_X^{\text{limit}} = \sigma_{\text{noise}} / \sqrt{N}$$

where $\sigma_{\text{noise}}$ is the RMS background and instrumental noise per source. With $N=55$ and deep exposures:

$$\sigma_{\text{noise}} \approx 1-2 \times 10^{-15} \, \text{erg} \, \text{cm}^{-2} \, \text{s}^{-1}$$

Thus:

$$F_X^{\text{limit}} \approx (1-2) \times 10^{-16} \, \text{erg} \, \text{cm}^{-2} \, \text{s}^{-1}$$

At luminosity distance $d_L(z=6)$:

$$L_X^{\text{limit}} = 4\pi d_L^2 F_X^{\text{limit}} \approx 10^{42} \, \text{erg} \, \text{s}^{-1}$$

Optical/UV data from JWST show that typical LRD bolometric luminosities are:

$$L_{\text{bol}} \approx (1-5) \times 10^{45} \, \text{erg} \, \text{s}^{-1}$$

Standard AGN ($\alpha_{ox}$ relation) would produce:

$$L_X^{\text{predicted}} = L_{\text{bol}} \times 10^{-2} \approx (1-5) \times 10^{43} \, \text{erg} \, \text{s}^{-1}$$

The observed non-detection is *three orders of magnitude below this prediction*. This enormous deficit cannot be explained by modest dust obscuration alone.

### Column Density Inference

X-ray absorption by neutral gas follows:

$$\tau(E) = \sigma_{\text{PE}}(E) \times N_H$$

where $\sigma_{\text{PE}}(E)$ is the photo-electric absorption cross-section. For $E = 2$ keV in neutral hydrogen:

$$\sigma_{\text{PE}}(2 \text{ keV}) \approx 10^{-24} \, \text{cm}^2$$

The transmission fraction through a column of density $N_H$ is:

$$T(E) = e^{-N_H \sigma_{\text{PE}}(E)}$$

For $N_H = 10^{24} \, \text{cm}^{-2}$ (Compton-thin):

$$T(2 \text{ keV}) = e^{-1} \approx 0.37 \quad (63\% \text{ absorbed})$$

For $N_H = 10^{25} \, \text{cm}^{-2}$ (Compton-thick):

$$T(2 \text{ keV}) = e^{-10} \approx 4.5 \times 10^{-5} \quad (99.995\% \text{ absorbed})$$

The 1000× reduction in X-ray flux requires $N_H > 10^{25} \, \text{cm}^{-2}$, entering the Compton-thick regime where even scattered X-rays are suppressed.

At Compton-thick column densities, X-ray reflection and scattering still occur, with a reflection fraction:

$$R_{\text{reflect}} \approx 0.5 - 1.0$$

Thus, even in Compton-thick gas, a fraction of X-rays scatter into line-of-sight. The non-detection implies not just Compton-thick gas, but either:

1. Edge-on geometry with scattering suppressed, or
2. Gas clumpiness such that some lines-of-sight have even higher column densities.

### Accretion Rate Constraints from Optical Diagnostics

Broad Balmer lines (Hα, Hβ) in LRDs have linewidths $\Delta v_{\text{FWHM}} \sim 2000-5000 \, \text{km} \, \text{s}^{-1}$, characteristic of gas in virial motion around a SMBH. Using the virial formula:

$$M_{\text{BH}} = \frac{\Delta v^2 R_{\text{BLR}}}{G}$$

where $R_{\text{BLR}}$ is the broad-line region radius, estimated from the AGN luminosity via the $R$-$L$ relation:

$$R_{\text{BLR}} = 10^{(0.5 \log L_{\text{5100 Å}} - 17.0)} \, \text{cm} \quad [\text{cm}]$$

For a typical LRD with $L_{\text{bol}} = 10^{45} \, \text{erg} \, \text{s}^{-1}$:

$$R_{\text{BLR}} \sim 10^{16} \, \text{cm} \sim 1000 \, R_g$$

and $\Delta v = 3000 \, \text{km} \, \text{s}^{-1}$:

$$M_{\text{BH}} \sim (1-3) \times 10^8 M_{\odot}$$

The accretion rate inferred from the observed Hα luminosity (photoionization-driven recombination) is:

$$\dot{M} = \frac{L_{\text{ion}}}{(1 - \alpha_B) h\nu_{\text{H}}}$$

where $\alpha_B$ is the recombination coefficient. For LRDs with strong Hα, this gives $\dot{M} \sim (0.1-1.0) M_{\odot} \, \text{yr}^{-1}$, which is *super-Eddington* for a $M_{\text{BH}} = 10^7-10^8 M_{\odot}$ black hole:

$$\dot{M}_{\text{Edd}} = \frac{L_{\text{Edd}}}{c^2 \epsilon} = \frac{1.4 \times 10^{38} M_{\text{BH}} / M_{\odot}}{0.1 c^2} \sim 0.1 M_{\odot} \, \text{yr}^{-1} \quad [M_{\text{BH}} = 10^8 M_{\odot}]$$

Thus, $\dot{M}/\dot{M}_{\text{Edd}} \sim 1-10$ or higher, depending on accretion geometry.

### Dust Reradiation Reconciliation

If the black hole accretes at rates $\dot{M} \sim 0.1-1.0 M_{\odot} \, \text{yr}^{-1}$ but is obscured by $N_H > 10^{25} \, \text{cm}^{-2}$, how do we observe the bright optical/UV continuum?

*Answer*: Dust re-radiation. The obscuring gas and dust absorb the primary accretion-disk UV and X-ray output, thermalize it, and re-radiate in the far-infrared. In the observer frame, this appears as:

1. A reddened optical/NIR continuum (the SED of the thermalized dust at $T \sim 1000$ K)
2. Strong emission lines in the ionized gas *between* the accretion disk and the dust (the de-excitation lines seen by JWST/NIRSpec)
3. No direct X-ray signal (absorbed in dust)

The total energy is conserved:

$$L_{\text{bol}} = L_{\text{accretion}} = L_{\text{X}} + L_{\text{UV}} + L_{\text{FIR}}$$

For Compton-thick obscuration, $L_X \ll L_{\text{bol}}$, so:

$$L_{\text{FIR}} + L_{\text{recombination}} \approx L_{\text{bol}}$$

ALMA and SPICA observations indeed find that LRDs have significant far-IR thermal emission, consistent with dust reradiation.

---

## Key Results

1. **Non-detection at 400 Ms Depth**: Stacking 55 LRDs in Chandra data yields no significant 2-10 keV signal, with a 3-sigma upper limit ~10^42 erg/s for typical sources.

2. **Rejection of Standard Super-Eddington Models**: Super-Eddington accretion models (e.g., Shakura-Sunyaev or ADF prescriptions) predict X-ray luminosity $L_X > 10^{43}$ erg/s even with some obscuration. The observed limit rules out these models at >99% confidence.

3. **Column Density Constraint $N_H > 10^{25} \, \text{cm}^{-2}$**: Compton-thick obscuration is required. This is 10-100× more extreme than typical Type-2 AGN.

4. **Accretion Rates Sub-Eddington or Uncertain**: Without X-ray data, accretion rates depend on optical diagnostics (Hα) or SED modeling. The authors argue that $\dot{M}$ could be sub-Eddington even with high-mass black holes if the virial masses are overestimated (e.g., if Hβ FWHM is not driven purely by virial motion but includes contributions from outflows or geometry).

5. **Dust Reradiation is Primary Observable**: LRD luminosity is dominated by dust thermalization, not direct AGN radiation. The optical/NIR colors and far-IR fluxes are consistent with a Rayleigh-Jeans tail from dust at $T \sim 800-1200$ K.

6. **Implication for Black Hole Growth**: If accretion rates are lower than previously inferred (sub-Eddington or barely super-Eddington), the assembly timescale for $M_{\text{BH}} \sim 10^9 M_{\odot}$ by $z = 7$ becomes difficult. This either pushes black hole seed formation earlier (primordial black holes) or requires sustained high accretion over longer timescales than standard models allow.

---

## Impact and Legacy

The Simmonds et al. (2025) X-ray stacking result is landmark for:

1. **Resolving the X-ray Weakness Puzzle**: The definitive observational statement that LRDs are not simply super-Eddington accretors in classical unobscured states, but heavily obscured systems.

2. **Compton-Thick AGN at High-z**: The paper revived interest in Compton-thick AGN at high redshift, a population previously thought rare but potentially common at z>3.

3. **Accretion Rate Ambiguity**: By ruling out X-ray diagnostics, the paper highlighted the degeneracies in optical-only accretion rate estimates, prompting more careful statistical treatments of virial mass estimates and outflow contributions to linewidths.

4. **Multi-wavelength Demand**: The paper underscored the necessity for far-IR (SPICA, future) and submillimeter (ALMA) observations to constrain dust masses and accretion rates in Compton-thick systems.

5. **Influence on Seed Formation Models**: Subsequent theoretical work pivoted toward direct-collapse black hole (DCBH) formation in dense gas as the preferred seed mechanism, since rapid assembly of $M_{\text{BH}} \sim 10^8-10^9 M_{\odot}$ is difficult with sub-Eddington accretion alone.

---

## Connection to Phonon-Exflation Framework

**Relevance**: MINIMAL—observational constraint, not fundamental physics.

Phonon-exflation predicts CDM-like dark matter and w = -1 + O(10^{-29}), degenerate with LCDM at z < 10^28. The Simmonds X-ray non-detection does not directly probe the dark matter or expansion history.

However, there is an *indirect* connection through black hole assembly rates and halo dynamics:

1. **Halo Density and Gas Infall**: If phonon-exflation predicts a different halo density profile than LCDM (e.g., if SIDM self-interactions are significant), then the efficiency of gas infall and black hole feeding in early halos would differ. LRD assembly rates test whether high central densities are achievable.

2. **Feedback Suppression**: Compton-thick gas envelopes around LRDs provide strong AGN feedback (radiation pressure on dust, quasar winds). The coupling between AGN feedback and halo dynamics is sensitive to the dark matter sound speed. Phonon-exflation's CDM-like prediction (c_s ~ 10^{-5} c) implies standard collapse dynamics, consistent with observed LRD assembly rates.

3. **Reionization Driven by LRD AGN**: LRD black holes likely drive a significant fraction of reionization at z~6-8. The ionization rate depends on the number density of LRDs, which in turn depends on the halo merger rate. Phonon-exflation predicts a merger rate indistinguishable from LCDM, so this is a consistency check rather than a test.

**Closest thematic link**: Dark matter halo profile curvature. Compton-thick obscuration requires sustained dense gas and rapid infall, favoring cuspy halo profiles (CDM prediction) over cored profiles (SIDM with large cross-sections). The tight clustering and rapid assembly of LRDs mildly favor CDM over aggressive self-interactions.

**Summary**: The Simmonds Chandra non-detection is an essential *astrophysical datum* for constraining accretion physics in the early universe, but provides no discriminant between phonon-exflation and LCDM. Both frameworks are degenerate in their dark matter predictions at z~6.

---

**Key Citation**:
Simmonds et al. (2025). "Chandra Rules Out Super-Eddington Accretion Models for Little Red Dots." *The Astrophysical Journal Letters*, arXiv:2505.09669.
