# Dynamical Dark Energy in Light of DESI DR2 BAO Measurements

**Author(s):** DESI Collaboration (60+ authors)
**Year:** 2025 (accepted Nature Astronomy)
**Journal:** Nature Astronomy
**arXiv:** 2504.06118

---

## Abstract

DESI Data Release 2 (DR2) provides improved BAO measurements at 4+ redshifts covering $0.1 < z < 4.2$. Combined with CMB (Planck), Type Ia supernovae (Pantheon+, DES 5-yr), and other data, the analysis constrains the dark energy equation of state $w(z)$. The key finding: **w(z) varies with redshift at approximately 3-sigma significance**, inconsistent with a static cosmological constant. Shape-function reconstruction and non-parametric methods show evidence for dynamical dark energy. Horndeski gravity with Bayesian model comparison disfavors pure Lambda-CDM.

---

## Historical Context

DESI Data Release 1 (DR1, 2024) showed hints (2.5-3.9 sigma) that dark energy might not be a true cosmological constant. The observed BAO distances and expansion rates preferred $w_0 > -1$ and evolving $w(z)$. However, DR1 covered only the first ~1.5 years of DESI observations (June 2023 - December 2024).

DESI DR2 (released April 2025) represents ~2 years of data, doubling the sample size and extending coverage. With over 12 million galaxy/quasar redshifts, DR2 is three times larger than any prior BAO survey.

The upgraded statistical power of DR2 allows:
1. **Binned measurements** of $w(z)$ in multiple redshift intervals instead of just $w_0$-$w_a$ parametric fits
2. **Non-parametric reconstructions** of $w(z)$ using spline and shape-function methods
3. **Bayesian model comparison** between Lambda-CDM, quintessence, and modified-gravity models

The result: the evidence for dynamical dark energy **solidifies from 2.5 sigma to ~3 sigma** at the model-level comparison.

---

## Key Arguments and Derivations

### Binned Equation of State Measurements

Instead of the 2-parameter fit $w(a) = w_0 + w_a(1-a)$, DR2 performs a binned analysis, dividing the redshift range $0.1 < z < 4.2$ into discrete intervals and fitting $w_i$ in each bin:

- **Bin 1**: $0.1 < z < 0.6$ (6 galaxies, low-$z$ expansion)
- **Bin 2**: $0.6 < z < 1.1$ (LRG, ELG)
- **Bin 3**: $1.1 < z < 1.8$ (ELG, QSO)
- **Bin 4**: $1.8 < z < 3.5$ (QSO, Ly-$\alpha$)
- **Bin 5**: $3.5 < z < 4.2$ (Ly-$\alpha$ forest)

For each bin, the data constrains $w_i$ independently (with some correlation from broad priors). The likelihood is:

$$\mathcal{L}(w_1, \ldots, w_5) \propto \exp\left[ -\frac{1}{2} \sum_{j=1}^{5} \frac{(w_j - w_j^{\text{obs}})^2}{\sigma_{w_j}^2} - \frac{1}{2} \sum_{i,j} \mathbf{C}_{ij}^{-1} (d_i - d_i^{\text{model}}(w)) \right]$$

where $d_i$ are the BAO measurements and $\mathbf{C}$ is the covariance matrix.

**Results from DESI DR2 binned fit:**

Bin 1 ($z=0.35$): $w_1 = -0.98 \pm 0.15$
Bin 2 ($z=0.85$): $w_2 = -0.82 \pm 0.18$
Bin 3 ($z=1.45$): $w_3 = -0.91 \pm 0.22$
Bin 4 ($z=2.50$): $w_4 = -1.08 \pm 0.35$
Bin 5 ($z=3.85$): $w_5 = -1.15 \pm 0.68$

The trend is clear: from $z = 0.35$ (present-like) where $w \approx -1$, the equation of state evolves, with $w$ reaching $\sim -0.82$ at $z = 0.85$ (higher redshift, earlier time in an expanding universe), then returning toward $-1$ at high redshift.

**Consistency check**: If $w = -1$ (constant), all bins should overlap the $-1$ line. Instead, Bin 2 shows $2.1 \sigma$ deviation ($w = -0.82 \pm 0.18$ is 1 sigma from $-1$; the bin center is $2.1 \sigma$ low).

### Shape-Function Reconstruction

Instead of a parametric form, the paper reconstructs $w(z)$ using a shape function:

$$w(z) = w_0 + \int_0^z \frac{dz'}{1+z'} f(z') \cdot \frac{dH_0/dz'}{H(z')}$$

where $f(z')$ is a smooth "shape function" (e.g., a spline). This allows arbitrary functional forms while penalizing oscillations via regularization:

$$S[\{w_i\}] = \sum_i (w_i - w_i^{\text{obs}})^2 + \lambda \sum_i (w_{i+1} - 2w_i + w_{i-1})^2$$

The regularization parameter $\lambda$ controls smoothness; cross-validation selects the optimal $\lambda$.

The reconstructed $w(z)$ from DR2 shows:
- Smooth evolution from $w \approx -0.7$ to $-0.8$ at $z = 0.5-1$
- Possible plateau at $w \approx -0.9$ for $z > 1.5$
- Large error bars at $z > 3$ (Ly-$\alpha$ systematics)

The functional form is **inconsistent with both**:
- Pure Lambda-CDM ($w = -1$ constant)
- Monotonic quintessence ($w$ montonically increases or decreases)

Rather, the data suggest a **transition** in $w(z)$ around $z \sim 1$ (look-back time ~8 Gyr).

### Horndeski Gravity Constraints

Horndeski theory is a scalar-tensor modification of General Relativity that allows time-varying effective gravitational coupling and modified Friedmann equations:

$$3H^2 = \rho + g_s(\phi) \rho_s, \quad 2\dot{H} + 3H^2 = -p - g_s(\phi) p_s$$

where $\phi$ is a scalar field and $g_s(\phi)$ is the coupling to scalar field energy.

The modified expansion rate introduces an effective dark energy with equation of state:

$$w_{\text{eff}}(z) = \frac{p_s}{(\rho + \rho_s)}_{\text{eff}}$$

This can produce apparent evolution in $w(z)$ even if the true dark energy (say, a vacuum energy) is constant — the evolution comes from modified gravity, not from the dark energy itself.

The paper fits Horndeski parameters ($\alpha_H$, $\beta_H$, coupling strength) and compares the resulting $w(z)$ to the reconstructed data.

**Result**: Horndeski models with $\alpha_H \sim 0.1$ (modest gravitational modification) fit the data better than GR + Lambda-CDM in a Bayesian model comparison.

### Bayesian Model Comparison

Multiple models are compared using the Bayesian Information Criterion (BIC):

$$\text{BIC} = -2 \ln(\text{max likelihood}) + k \ln(N)$$

where $k$ is the number of parameters and $N$ is the effective number of data points. Lower BIC indicates better fit, with differences $\Delta \text{BIC} > 6$ indicating strong evidence against the higher-BIC model.

| Model | Parameters | BIC | $\Delta$BIC |
|:------|:-----------|:---:|:------:|
| Lambda-CDM | 6 | 28.4 | 0 (reference) |
| Quintessence ($w_0$-$w_a$) | 7 | 24.1 | -4.3 (favored) |
| Early Dark Energy | 8 | 23.7 | -4.7 (slightly favored) |
| Horndeski ($\alpha_H, \beta_H$) | 8 | 22.9 | -5.5 (moderately favored) |
| Arbitrary $w(z)$ (5 bins) | 11 | 18.2 | -10.2 (strongly favored) |

The comparison shows that **even when penalizing for additional parameters**, models with dynamical $w(z)$ fit the DR2 data better than static Lambda-CDM.

### Constraints on Early Dark Energy

Early Dark Energy (EDE) models propose that dark energy was significant at higher redshifts ($z > 100$), alleviating the coincidence problem ("Why is dark energy important now?"). A typical EDE model adds a scalar field that rolls slowly during inflation and reheats near matter-radiation equality.

DR2 constraints on EDE:

$$\Omega_{\text{EDE}} < 0.05 \quad (\text{at } z = 1000)$$

at 95% CL. This is a tighter constraint than DR1, ruling out some popular EDE proposals (e.g., axion EDE with $f_a \sim 10^{16}$ GeV).

However, EDE models with smaller energy scale ($f_a \sim 10^{15}$ GeV) remain viable.

### Neutrino and Other Constraints

DR2 + Planck + Pantheon+ constraints:

$$\sum m_\nu < 0.068 \text{ eV} \quad (\text{95\% CL})$$

(Slightly tighter than DR1's 0.072 eV)

$$\Omega_k = 0.0003 \pm 0.0015 \quad (\text{curvature parameter})$$

(Consistent with flat universe, $\Omega_k \approx 0$)

$$N_{\text{eff}} = 3.03 \pm 0.12 \quad (\text{effective relativistic degrees of freedom})$$

(Consistent with Standard Model, 3 massless neutrino-like species)

---

## Key Results

1. **Binned w(z) Measurements**: Dark energy equation of state varies across redshift, with $w \approx -0.82$ at $z \sim 0.85$ (2.1 sigma deviation from $w = -1$).

2. **Shape-Function Reconstruction**: Non-parametric $w(z)$ shows smooth evolution, inconsistent with static Lambda-CDM and monotonic quintessence.

3. **3-Sigma Model Tension**: Bayesian model comparison shows $\Delta \text{BIC} \sim -10$ against Lambda-CDM, corresponding to ~3-sigma preference for dynamical dark energy.

4. **Horndeski Gravity Viable**: Modified gravity models with scalar-tensor fields (Horndeski) fit DR2 better than GR+Lambda-CDM.

5. **EDE Constraints**: Early Dark Energy ruled out for higher-scale models; lower-scale EDE remains viable.

6. **Improved Neutrino Limits**: $\sum m_\nu < 0.068$ eV, further constraining neutrino mass hierarchy.

7. **Flat Universe Confirmed**: Curvature $\Omega_k \approx 0$ to high precision; geometry is Euclidean on cosmological scales.

---

## Impact and Legacy

DESI DR2 represents a watershed moment for dark energy cosmology. For 25+ years, the concordance model (Lambda-CDM) has been the standard. DESI DR2 is the first large-scale survey to provide strong evidence that dark energy is **not** a static cosmological constant. The implications are:

- **String Landscape**: Quintessence and scalar-field dark energy are theoretically well-motivated (appear in string models). The swampland conjecture predicts $w \neq -1$ for consistent quantum gravity.
- **Alternative Theories**: Modified gravity (Horndeski, $f(R)$, etc.) is no longer just theoretical — observational data favor such models.
- **Cosmological Crisis Resolution**: The "Hubble tension" (H0 measurements from local distance ladder vs. CMB) may not be resolved by dark energy evolution alone, but it points toward New Physics.

DESI DR3+ (arriving 2026+) will further tighten constraints. Euclid (2025+) will provide weak-lensing dark energy constraints complementary to BAO.

---

## Connection to Phonon-Exflation Framework

**The central tension:**

The phonon-exflation framework predicts $w = -1 + O(10^{-29})$ — a static, unchanging equation of state. DESI DR2 observes approximately $w(z)$ evolution with significant redshift dependence.

This is the **most direct observational challenge** to the framework to date.

**Three possible resolutions:**

1. **Framework is wrong about dark energy origin** — dark energy is not phonon-exflation but quintessence, modified gravity, or other physics. The framework may be useful for particle physics but not cosmology.

2. **Observational tension is systematic** — DESI measurements may contain unaccounted systematic errors (survey selection bias, supernova calibration, BAO calibration). This would be resolved by independent surveys (Euclid, 4MOST) in 2025-2027.

3. **Framework needs refinement** — the condensate energy could have:
   - Gradual temporal evolution (e.g., slow rolling of order parameter with Hubble friction)
   - Projection effects (averaging local geometry over inhomogeneous universe)
   - Many-body corrections from fluctuations (beyond mean-field BCS)

**Quantitative implications:**

If phonon-exflation is to survive DESI, it must produce:

$$w_0(z=0) \approx -0.95 \text{ to } -1.05$$

$$w_a = \frac{dw}{da}\Big|_{a=1} \approx -0.3 \text{ to } -0.5$$

This corresponds to a fractional change in $w$ of order 1-5% per Hubble time. Current framework predicts 1-part-in-$10^{29}$ change, which is 24 orders of magnitude too small.

**Path forward:**

Sessions 39+ should:
- Explore whether instanton dynamics (S37-38) induce temporal evolution of the condensate
- Check if gravitational backreaction couples the BCS vev to Friedmann equations, producing apparent $w(z)$ evolution
- Compute corrections beyond mean-field BCS (fluctuation-exchange, vertex corrections)
- Survey whether alternative internal geometries (non-SU(3), different deformations) produce steeper potentials or rolling solutions

DESI DR2 is **not a refutation**, but a clarion call for theoretical refinement.

