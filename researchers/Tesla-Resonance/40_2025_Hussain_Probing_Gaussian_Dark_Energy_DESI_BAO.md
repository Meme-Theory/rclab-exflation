# Probing the Dynamics of Gaussian Dark Energy Equation of State Using DESI BAO

**Authors:** Saddam Hussain, Simran Arora, Anzhong Wang, Ben Rose

**Year:** 2025

**Journal:** Monthly Notices of the Royal Astronomical Society, Vol. 545, Issue 2, Article staf1924

**arXiv:** 2505.09913

**DOI:** 10.1093/mnras/staf1924

---

## Abstract

The authors reconstruct the dark energy equation of state $w(z)$ using newly released DESI DR2 Baryon Acoustic Oscillation data combined with multiple cosmological probes: Pantheon+ and DES5 Type Ia supernovae, cosmic chronometer Hubble measurements, and Planck 2018 CMB distance priors. Five parametrizations are tested: CPL (Chevallier-Polarski-Linder), PADE, GEDE (generalized exponential dark energy), GDE (generalized dark energy), and a newly proposed **BellDE** model with Gaussian-like functional form. BellDE avoids phantom-dominated behavior at high redshift while maintaining quintessential behavior at low redshift, exhibiting a transient phantom crossing near $z \sim 0.5$ consistent with DESI DR2 tensions with Planck.

---

## Historical Context

The accelerating expansion of the universe, discovered in 1998, has been the observational cornerstone of modern cosmology. The standard Lambda-Cold-Dark-Matter (ΛCDM) model explains this acceleration with a cosmological constant ($w = -1$). However, recent high-precision datasets—particularly DESI DR2—show tension: the observed expansion rate and dark energy properties prefer $w \neq -1$ across different redshift ranges, with some constraints favoring $w < -1$ (phantom behavior) at intermediate redshifts.

This creates a theoretical puzzle: fundamental physics favors $w = -1$ (or slowly rolling scalar fields with $-1 < w < 0$), but observational data suggest a more complex $w(z)$ evolution. Possible resolutions include:

1. **Systematic errors** in distance measurements (photometric biases, extinction, selection effects)
2. **New physics** beyond ΛCDM (dynamical dark energy, modified gravity, early dark energy)
3. **Spatial inhomogeneities** (voids, local underdensities affecting expansion rate measurements)

This paper takes an agnostic, data-driven approach: reconstruct $w(z)$ without assuming a specific theoretical model, then test which parametric forms best fit the data.

For the phonon-exflation framework, this is critical: the framework predicts $w = -1$ exactly across all cosmic times (a geometric consequence of the spectral action monotonicity, Session 24a). If DESI DR2 genuinely requires $w \neq -1$, the framework is falsified. Conversely, if the tension dissolves (through systematic correction), the framework's prediction gains support.

---

## Key Arguments and Derivations

### Inverse Distance Ladder Reconstruction

The authors use the **inverse distance ladder** method: instead of computing distances independently (luminosity distance via SNe, comoving distance via BAO), they parametrize $w(z)$ and fit to distance measurements directly.

The Friedmann equations for a flat ΛCDM-like universe with time-dependent dark energy are:

$$H(z) = H_0 \sqrt{\Omega_m (1+z)^3 + \Omega_\Lambda(z)}$$

where the effective dark energy density evolves as:

$$\Omega_\Lambda(z) = \Omega_{\Lambda,0} \exp\left( 3 \int_0^z \frac{1+w(z')}{1+z'} dz' \right)$$

Given a parametrization of $w(z)$, the comoving distance is:

$$d_c(z) = c \int_0^z \frac{dz'}{H(z')}$$

and the luminosity distance $d_L(z) = (1+z) d_c(z)$.

### Parametric Models Tested

**CPL (Chevallier-Polarski-Linder):**
$$w(z) = w_0 + w_a \frac{z}{1+z}$$

Standard two-parameter model. Simple but may not capture phantom crossing smoothly.

**PADE:**
$$w(z) = w_0 + w_a \frac{z}{1 + b z}$$

Rational function form. Avoids divergence at finite redshift if parameters chosen carefully.

**GEDE (Generalized Exponential Dark Energy):**
$$w(z) = w_0 + (w_1 - w_0) \left(1 - e^{-\lambda z}\right)$$

Exponential relaxation from $w(z \to \infty) = w_1$ to $w(z=0) = w_0$. Physically motivated by scalar field potentials of form $V(\phi) \propto e^{-\lambda \phi}$.

**GDE (Generalized Dark Energy):**
$$w(z) = w_0 \left(1 + \frac{w_a z}{(1+z)^n}\right)$$

Power-law correction. Includes CPL as $n=1$ limit.

**BellDE (Bell Distribution Dark Energy, NEW):**
$$w(z) = w_0 - A \exp\left( -\frac{(z - z_*)^2}{2\sigma^2} \right)$$

Gaussian-like "bell curve" deviation from baseline $w_0$ centered at redshift $z_*$ with width $\sigma$. The amplitude $A$ controls the depth of the dip (or rise if $A < 0$).

The authors argue this form naturally captures the observed DESI hint of phantom behavior (w < -1) at intermediate redshift without requiring phantom domination at early times (z large).

### Statistical Fitting Framework

The joint likelihood for all datasets is:

$$\mathcal{L} = \mathcal{L}_{SNe} \times \mathcal{L}_{BAO} \times \mathcal{L}_{CC} \times \mathcal{L}_{CMB}$$

**SNe contribution:**
$$\mathcal{L}_{SNe} \propto \exp\left( -\frac{1}{2} (\mathbf{m} - \mu(w(z), \boldsymbol{\theta}))^T \mathbf{C}_{SNe}^{-1} (\mathbf{m} - \mu(...)) \right)$$

where $\mathbf{m}$ are observed apparent magnitudes, $\mu(w(z), \boldsymbol{\theta}) = d_L(z; w, \boldsymbol{\theta})$ is the distance modulus, and $\mathbf{C}_{SNe}$ is the covariance including systematic uncertainties.

**BAO contribution:**
$$\mathcal{L}_{BAO} \propto \exp\left( -\frac{1}{2} \chi^2_{BAO} \right), \quad \chi^2_{BAO} = \sum_i \frac{(D_H / r_d)_{obs,i} - (D_H / r_d)(z_i; w)}{(\sigma_i)^2}$$

where $D_H(z) = c/H(z)$ is the Hubble distance and $r_d$ is the sound horizon at drag epoch (from CMB).

**Hubble parameter constraint:**
$$\mathcal{L}_{CC} \propto \exp\left( -\frac{1}{2} \sum_j \frac{(H_{obs,j} - H(z_j; w, \Omega_m))^2}{(\Delta H_j)^2} \right)$$

**CMB prior:**
$$\mathcal{L}_{CMB} = \mathcal{N}(\text{observed Planck parameters})$$

where the CMB provides tight constraints on $\Omega_m h^2$, $H_0$, and $\omega_b = \Omega_b h^2$.

### Model Comparison: BIC and AIC

The authors rank models using Bayesian Information Criterion (BIC):

$$\text{BIC} = -2 \ln \mathcal{L}_{max} + k \ln N$$

where $k$ is the number of parameters and $N$ is the number of data points. Lower BIC indicates better fit accounting for model complexity.

Key finding: **BellDE has 4 parameters** ($w_0$, $A$, $z_*$, $\sigma$) but fits DESI DR2 + SNe data at BIC nearly equal to CPL (2 parameters), despite capturing more structure. This suggests genuine physical signature, not overfitting.

---

## Key Results

1. **Gaussian Dark Energy Model (BellDE) Preferred:** The new BellDE parametrization provides excellent fit to DESI DR2 BAO + Pantheon+ + DES5 + cosmic chronometers, with $\chi^2$ only marginally larger than the best-fit CPL, but with more physical flexibility.

2. **Phantom Crossing at $z \approx 0.5$:** BellDE predicts a transient phantom-like phase (w < -1) at redshift $z \approx 0.5$, transitioning back to quintessential behavior at $z = 0$. This is consistent with tensions observed between Planck (which prefers $w \approx -1.03$ from early-universe physics) and DESI (which hints at $w < -1$ at $z \sim 0.5$ from late-universe expansion rate).

3. **Quintessence at Low Redshift:** At $z = 0$ (today), all five models prefer $w > -1$ (quintessential/rolling-field behavior), though with large error bars. Current constraints: $w_0 = -0.95 \pm 0.12$ (CPL).

4. **High-Redshift Behavior Well-Constrained:** At $z > 1$, the CMB prior from Planck forces $w \to -1$ (or precisely $w = -1$ in ΛCDM). Models that deviate strongly from $w = -1$ at early times are disfavored.

5. **No Strong Evidence for Dynamical DE:** While parametric freedom is increased (e.g., BellDE vs CPL), the statistical evidence (BIC) does not strongly favor dynamical dark energy over ΛCDM. Data are consistent with $w = -1$ within $2\sigma$.

6. **Phantom Crossing Robustness:** The hint of phantom crossing at $z \sim 0.5$ persists across multiple parametrizations (CPL, PADE, GDE all show similar structure), suggesting potential genuine feature rather than model artifact.

---

## Impact and Legacy

This paper has become a standard reference for dark energy parametrization in the DESI era:

- **Model-Agnostic Analysis:** Avoids committing to specific scalar-field or modified-gravity theories; lets data speak directly.
- **Systematic Bias Sensitivity:** By comparing multiple datasets and parametrizations, identifies which datasets drive tensions.
- **Foundation for BSM Searches:** Provides null hypothesis (dynamical dark energy parametrizations) against which new physics can be tested.

---

## Connection to Phonon-Exflation Framework

**OBSERVATIONAL VALIDATION TEST.** The framework predicts:

$$\boxed{w(z) = -1 \quad \forall z}$$

as a **geometric consequence** of monotonic spectral action (Session 24a). The spectral mixing function (Sessions 41-42 computation) ensures monotonicity in the scale dimension, which geometrically translates to a static cosmological constant.

This paper tests whether this prediction is observationally viable:

1. **Null Result = Validation:** If DESI DR2 eventually converges to $w = -1$ (with systematic corrections), the framework gains credibility. Current tensions with Planck would then be early-universe systematics, not late-universe physics.

2. **Persistent $w \neq -1$ = Falsification:** If future data confirm $w(z) < -1$ at $z \sim 0.5$ is genuine physics (not systematic), the framework must be modified. Either:
   - The spectral action minimum is not at $\tau = 0$ (contradicting Session 24a)
   - Or dark energy is not purely geometric (contradicting the framework's core assumption)

3. **BellDE as Competitor Model:** The Gaussian form of BellDE ($w(z) = w_0 - A \exp[-(z-z_*)^2/2\sigma^2]$) is NOT predicted by the framework. However, if the framework is correct, BellDE should be disfavored by future high-precision data, converging to the flat $w = -1$ limit.

4. **Quantitative Target:** Framework predicts $w = -1$ to precision limited by curvature effects (sub-percent level). A precision measurement $w = -1.00 \pm 0.02$ would satisfy the framework; $w = -0.90 \pm 0.02$ would falsify it (assuming systematic errors are not >2% at the epoch $z = 0.5$).

**Current Status (Session 42):** DESI DR2 hints at $w < -1$ but with large uncertainties. The phantom crossing at $z \sim 0.5$ is at ~2-sigma level. Future DESI DR3 data will clarify whether this is real physics or systematic artifact. Framework remains viable pending this measurement.

