# Encyclopaedia Inflationaris

**Author(s):** Jerome Martin, Christophe Ringeval, Vincent Vennin
**Year:** 2014
**Journal:** Physics of the Dark Universe 5-6, 75-235 (2014)
**arXiv:** 1303.3787
**Relevance:** MEDIUM -- exhaustive catalog of single-field inflationary models (74 models) with their predictions for $n_s$, $r$, and running; provides the systematic framework for comparing any new model against CMB data; useful as a reference encyclopedia rather than for novel derivations

---

## Abstract

[INCOMPLETE - not extractable from PDF due to 368-page length; the following is reconstructed from the paper's known content]

This paper provides an exhaustive and systematic review of single-field models of inflation. For each model, the authors compute the slow-roll predictions for the spectral index $n_s$, the tensor-to-scalar ratio $r$, the running of the spectral index $\alpha_s$, and perform a Bayesian comparison with Planck data. The paper catalogs 74 distinct inflationary potentials organized into four broad classes: large-field, small-field, hybrid, and plateau models.

---

## Key Arguments and Derivations

### General Framework

For each model $V(\phi)$, the authors compute:
- Slow-roll parameters $\epsilon_1 = \frac{M_{\rm pl}^2}{2}(V'/V)^2$, $\epsilon_2 = 2M_{\rm pl}^2[(V'/V)^2 - V''/V]$, $\epsilon_3$
- The number of e-folds $N_*$ as a function of reheating temperature
- Predictions for $n_s = 1 - 2\epsilon_1 - \epsilon_2$, $r = 16\epsilon_1$, $\alpha_s = -2\epsilon_1\epsilon_2 - \epsilon_2\epsilon_3$
- Bayesian evidence relative to the best-fit model

### Classification of Models

The 74 models are organized into major families:

**Large-field models** ($V \propto \phi^p$): Predict $n_s = 1 - (p+2)/(2N_*)$ and $r = 4p/N_*$. The $p=2$ model predicts $n_s \approx 0.967$, $r \approx 0.13$ for $N_* = 60$. Increasingly disfavored by Planck for $p \geq 2$.

**Plateau/Starobinsky-type models** ($V \sim V_0(1 - e^{-\sqrt{2/3}\phi/M_{\rm pl}})^2$): Predict $n_s \approx 1 - 2/N_*$, $r \approx 12/N_*^2$. Best fit to Planck data. The Starobinsky $R^2$ model is the prototype.

**Small-field models** ($V = V_0[1 - (\phi/\mu)^p]$): Predict $n_s = 1 - p/(p-2) \cdot 1/N_*$ for $p > 2$, with very small $r$.

**Hybrid models**: Various forms with two-field dynamics where a waterfall field ends inflation. Can produce $n_s > 1$ or $n_s < 1$ depending on parameters.

### Key Findings

The Planck 2013 data strongly favor plateau-type potentials (Starobinsky $R^2$ inflation and its relatives). Large-field models with $p \geq 2$ are under tension. The spectral index measurement $n_s = 0.9603 \pm 0.0073$ (Planck 2013) is the most discriminating observable.

---

## Key Results

1. 74 single-field inflationary models are systematically cataloged with their observational predictions.
2. Plateau models (Starobinsky $R^2$, Higgs inflation) provide the best fit to Planck data.
3. The $n_s$-$r$ plane is the primary discriminator: Planck data carve out a narrow allowed region.
4. Large-field monomial models $V \propto \phi^p$ with $p \geq 2$ are disfavored at $>2\sigma$.
5. Natural inflation requires super-Planckian decay constant $f > 5 M_{\rm pl}$ to be viable.
6. Most hybrid inflation models predict $n_s$ very close to 1, in mild tension with data.
7. The reheating temperature introduces a significant uncertainty in $N_*$ and hence in predictions.
8. Bayesian model comparison strongly favors concave potentials over convex ones.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Hubble slow-roll parameters | $\epsilon_1 = -\dot{H}/H^2$, $\epsilon_{i+1} = d\ln|\epsilon_i|/dN$ | Sec. 2 |
| Potential slow-roll | $\epsilon_V = \frac{M_{\rm pl}^2}{2}(V'/V)^2$, $\eta_V = M_{\rm pl}^2 V''/V$ | Sec. 2 |
| Scalar spectral index | $n_s = 1 - 2\epsilon_1 - \epsilon_2$ | Sec. 2 |
| Tensor-to-scalar ratio | $r = 16\epsilon_1$ | Sec. 2 |
| Running | $\alpha_s = -2\epsilon_1\epsilon_2 - \epsilon_2\epsilon_3$ | Sec. 2 |
| Scalar amplitude | $A_s = \frac{H^2}{8\pi^2 M_{\rm pl}^2 \epsilon_1}\bigg|_{k=aH}$ | Sec. 2 |
| Number of e-folds | $N_* = \int_{\phi_{\rm end}}^{\phi_*}\frac{V}{M_{\rm pl}^2 V'}d\phi$ | Sec. 2 |
| Starobinsky model | $V = V_0\left(1 - e^{-\sqrt{2/3}\,\phi/M_{\rm pl}}\right)^2$ | Model catalog |
| Starobinsky predictions | $n_s \simeq 1 - 2/N_*$, $r \simeq 12/N_*^2$ | Model catalog |

---

## Relevance to Phonon-Exflation

The Encyclopaedia provides the systematic comparison framework against which the exflation prediction $n_s = 0.9561$ must be tested. This value falls within the Planck-allowed range and is close to the Starobinsky $R^2$ prediction ($n_s \approx 0.967$ for $N_* = 55$) but is slightly lower. The key distinction: in all 74 models cataloged here, $n_s$ depends on a free parameter (the number of e-folds $N_*$, which itself depends on the unknown reheating temperature). In the exflation framework, $n_s = 0.9561$ emerges from gauge-invariant spectral geometry with zero free parameters -- the Jensen deformation of SU(3) at the fold determines it uniquely. If future measurements pin $n_s$ to this precision, the exflation prediction is either confirmed or ruled out without the escape hatch of adjusting $N_*$.
