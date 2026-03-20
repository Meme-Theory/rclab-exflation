# DESI 2024 VI: Cosmological Constraints from BAO and Redshift Space Distortions

**Author(s):** DESI Collaboration (Adame, Aguilar, Ahlen, et al.)
**Year:** 2024
**Journal:** arXiv:2404.03002

---

## Abstract

The DESI experiment presents cosmological results from baryon acoustic oscillation (BAO) measurements using 6 million extragalactic objects spanning redshift 0.1 < z < 4.2 across galaxy, quasar, and Lyman-alpha forest samples. Combined with Planck CMB and large-scale structure data, measurements constrain the Hubble constant to H₀ = 67.97 ± 0.38 km/s/Mpc and matter density Ωₘ = 0.307 ± 0.005. The equation of state w(z) shows a 2.6σ preference for dynamical dark energy with w₀ > −1, challenging ΛCDM.

---

## Historical Context

DESI DR1 (2024) represents the first major observational window into the redshift-dependent equation of state of dark energy since Planck 2018. The measurement exploits the standard ruler of the baryon acoustic oscillation scale (r_s ~ 150 Mpc) imprinted in matter correlations to measure distance-redshift relations independently of supernovae or inverse-distance-ladder systematics.

The "2.6σ anomaly" in w(z) has triggered intense scrutiny. The phonon-exflation framework predicts w = −1 + O(10⁻²⁹) across all redshifts—a static dark energy driven by internal geometry. DESI's hint of dynamical DE (w₀ = −0.55+/−0.21 from early analyses, softened to 2.6σ in BAO-alone) either signals new physics or systematic bias in large-scale structure calibration.

The S42 hypothesis (tessellation-lensing bias from the 32-cell structure of SU(3) Voronoi cells) proposes that weak-lensing magnification bias in the galaxy survey produces apparent w ≠ −1. DESI DR2 (2025) will test this with 14 million galaxies and independent photometric-spectroscopic cross-checks.

---

## Key Arguments and Derivations

### BAO as Standard Ruler

The BAO scale r_s is measured from the Planck CMB:

$$r_s = \int_0^{z_*} \frac{c_s dt}{a} = \int_0^{a_*} \frac{c_s da}{a^2 H(a)}$$

where $c_s = c/\sqrt{3(1+R_b)}$ is the sound speed in the baryon-photon fluid and z_* ≈ 1090 is the recombination epoch. Planck 2018 fixes $r_s = 147.21 ± 0.25$ Mpc.

At any redshift z, the BAO scale imprints a feature in the matter correlation function:

$$\xi(r) = \int \frac{d^3k}{(2\pi)^3} e^{i\mathbf{k}\cdot\mathbf{r}} P(k)$$

The peak at r ~ r_s is used to extract transverse and radial distances:

$$d_A(z) = \frac{c}{H_0} \int_0^z \frac{dz'}{E(z')}$$

$$H(z) = H_0 E(z)$$

where $E(z) = \sqrt{\Omega_m(1+z)^3 + (1-\Omega_m)}$ for ΛCDM.

### Multi-Tracer BAO Measurements

DESI observes three independent tracers:

1. **LRG** (Luminous Red Galaxies): 0.4 < z < 1.0, 8.5 million objects
2. **ELG** (Emission Line Galaxies): 0.8 < z < 1.6, dense sample
3. **QSO** (Quasars): 0.8 < z < 2.4, 250k objects
4. **Lyman-α forest**: 2.0 < z < 3.5, continuous absorption lines

Each tracer provides independent geometric constraints. The BAO scale is extracted by fitting a broadband power law plus a BAO bump:

$$P(k) = B^2 e^{-(k\mu)^2\sigma_v^2} (P_0(k) + P_\text{BAO}(k))$$

where $P_0$ is smooth (Eisenstein-Hu) and $P_\text{BAO}$ is the oscillatory component. The peak position yields $r_s/d_A$ (transverse) and $r_s H$ (radial).

### Equation of State Parameterization

For dynamical dark energy, w(z) is parameterized as:

$$w(z) = w_0 + w_a \frac{z}{1+z}$$

where $w_0$ is the present-day equation of state and $w_a$ characterizes redshift evolution. In ΛCDM, w = −1 exactly.

The Friedmann equation becomes:

$$H^2(z) = H_0^2 \left[ \Omega_m (1+z)^3 + \Omega_k (1+z)^2 + \Omega_\Lambda \exp\left(3 \int_0^z \frac{1+w(z')}{1+z'} dz'\right) \right]$$

For w(z) = w₀ + w_a z/(1+z):

$$\Omega_\Lambda(z) \propto (1+z)^{3(1+w_0+w_a)} \exp\left(3w_a \frac{z}{1+z}\right)$$

### Combined Constraints (DESI + Planck + Supernova)

DESI alone yields (BAO-only, flat ΛCDM):
- $\Omega_m = 0.295 ± 0.015$
- $H_0 = 68.52 ± 0.62$ km/s/Mpc

With Planck CMB prior and inverse-distance-ladder H₀ (Cepheids + SNIa):
- $\Omega_m = 0.307 ± 0.005$
- $H_0 = 67.97 ± 0.38$ km/s/Mpc

For w(z) model (w₀ + w_a parameterization):
- **DESI+CMB**: $w_0 = −0.85_{−0.13}^{+0.15}$, $w_a = −0.41_{−0.48}^{+0.46}$ (2.6σ tension with w = −1)
- **DESI+CMB+Supernova (DES)**: $w_0 = −0.72_{−0.21}^{+0.22}$, $w_a = −1.55_{−1.10}^{+0.90}$ (3.9σ tension with ΛCDM)

The Hubble tension (local ladder vs CMB) persists: H₀ ~ 73 km/s/Mpc vs 68 km/s/Mpc.

---

## Key Results

1. **BAO scale robustness**: Measurements consistent across LRG/ELG/QSO/Ly-α, validating the standard ruler
2. **H₀ geometric constraint**: DESI+CMB = 67.97 ± 0.38, tension with SH0ES remains unresolved
3. **Dynamical DE signal**: 2.6–3.9σ preference for w(z) ≠ −1 depending on dataset combination (BAO alone vs. with SNIa)
4. **Neutrino mass limit**: Σmᵥ < 0.072 eV (95% CL, DESI+CMB), consistent with oscillation measurements
5. **Void exclusion**: No evidence for KBC void or other local structures distorting the Hubble constant

---

## Impact and Legacy

DESI DR1 set the stage for precision dark energy cosmology with geometric measurements independent of astrophysical uncertainties. The preference for dynamical DE triggered the S42 tessellation-lensing hypothesis and motivated detailed weak-lensing systematics audits. DR2 (2025) with 14 million objects promises to clarify whether the w ≠ −1 signal persists or reflects observational systematics.

The framework's prediction of w = −1 + O(10⁻²⁹) is extremal but testable: any deviation from constant w falsifies the internal-compactification cosmology. DESI provides the most direct test to date.

---

## Connection to Phonon-Exflation Framework

**Direct**: The phonon-exflation model predicts **w(z) = −1 exactly at all redshifts**, driven by the monotonic spectral action encapsulating internal K_7 geometry (not dark energy field dynamics). The framework has no rolling scalar field, no quintessence, no early/late dark energy modulation. All cosmic acceleration flows from the K_7 pairing gap and the inverted Born-Oppenheimer approximation (geometry fast, gap slow).

DESI DR1's preference for w₀ ≠ −1 and w_a ≠ 0 directly challenges this prediction. The S42 hypothesis proposes a systematic explanation: 32-cell tessellation in SU(3) creates weak-lensing magnification bias that mimics dynamical DE. Alternatively, framework falsification if DESI DR2 confirms w ≠ −1.

This paper is foundational for Phase 3 (observational gates) of the Ainulindale framework validation.

