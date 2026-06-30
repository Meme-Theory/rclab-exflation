# Observation of Thermal Hawking Radiation at the Hawking Temperature in an Analogue Black Hole

**Author(s):** Juan Ramón Muñoz de Nova, Katrine Golubkov, Victor I. Kolobov, Jeff Steinhauer
**Year:** 2019
**Journal:** Nature Physics 15, 220-224 (2019)
**arXiv:** 1809.00913
**Relevance:** CRITICAL

---

## Abstract

We measure the correlation spectrum of the Hawking radiation emitted by an analogue black hole and find it to be thermal at the Hawking temperature implied by the analogue surface gravity. The Hawking radiation is in the regime of linear dispersion, in analogy with a real black hole. Furthermore, the radiation inside of the black hole is seen to be composed of negative-energy partners only. This work confirms the prediction of Hawking's theory regarding the value of the Hawking temperature, as well as the thermality of the spectrum. The thermality of Hawking radiation is the root of the information paradox. The correlations between the Hawking and partner particles imply that the analogue black hole has no analogue firewall.

---

## Key Arguments and Derivations

### 1. Analogue Black Hole Setup

The analogue black hole consists of a flowing Bose-Einstein condensate (BEC) of 8000 $^{87}$Rb atoms. The setup creates two regions separated by a sonic horizon at $x = 0$:

- **Outside** ($x < 0$): Flow velocity $v_{\text{out}} < c_{\text{out}}$ (subsonic). Corresponds to the exterior of a black hole.
- **Inside** ($x > 0$): Flow velocity $v_{\text{in}} > c_{\text{in}}$ (supersonic). Corresponds to the interior; phonons traveling toward the horizon in the comoving frame are swept away in the lab frame, unable to escape.

The condensate is confined in a focused laser beam ($\lambda = 812$ nm, waist = 3.9 $\mu$m). A blue-detuned laser ($\lambda = 442$ nm) creates a step potential (waterfall) near $x = 0$ that accelerates the flow to supersonic speeds.

### 2. Hawking Temperature Prediction

For an analogue black hole, the Hawking temperature is $\hbar g / 2\pi c$, where the analogue surface gravity is $g = c(dv/dx - dc/dx)$ evaluated at the sonic horizon. For stationary 1D flow with $nv = \text{const}$, this becomes:

$$k_B T_H = -\frac{\hbar}{2\pi}\left(\frac{c}{n}\frac{dn}{dx} + \frac{dc}{dx}\right)\bigg|_{x=0}$$

This is valid in the linear dispersion regime, analogous to massless particles from a real black hole. The experiment satisfies $k_B T_H = 0.12\, mc_{\text{out}}^2 \lesssim 0.14\, mc_{\text{out}}^2$, confirming the linear regime applies.

### 3. Speed of Sound Derivation

The speed of sound is derived from the density profile via:

$$c(x) = \sqrt{\frac{2\hbar a\, \omega_r(x)\, n(x)}{m}} \cdot \frac{\sqrt{1 + 3n(x)a/2}}{(1 + 2n(x)a)^{3/2}} - \frac{\hbar\omega_{r0}}{2U_0}$$

where $a$ is the scattering length, $\omega_{r0}$ and $U_0$ are the radial trapping frequency and potential depth at the laser focus. The first factor is the usual quasi-1D expression; the second corrects for finite density and potential depth.

### 4. Hawking/Partner Correlation Measurement

The key observable is the density-density correlation function $G^{(2)}(x, x')$, measured over 7400 experimental runs. The Hawking radiation manifests as a dark band in the correlation function extending from the horizon, representing correlations between Hawking particles (outside) and negative-energy partner particles (inside).

The Hawking/partner correlator $\langle \hat{b}_H \hat{b}_P \rangle$ is extracted via Fourier transform:

$$S_0 \langle \hat{b}_H \hat{b}_P \rangle = \sqrt{\frac{\xi_{\text{out}} \xi_{\text{in}}}{L_{\text{out}} L_{\text{in}}}} \int dx\, dx'\, e^{ik_H x} e^{ik_P x'} G^{(2)}(x, x')$$

where $S_0 = (U_{k_H} + V_{k_H})(U_{k_P} + V_{k_P})$ is the zero-temperature static structure factor.

### 5. Thermality Verification

Using the 2x2 Bogoliubov transformation $\hat{b}_H = \alpha\hat{b}_+ + \beta\hat{b}_-^\dagger$ and $\hat{b}_P = \alpha\hat{b}_- + \beta\hat{b}_+^\dagger$ with $|\beta|^2 = 1/(e^{\hbar\omega/k_B T_H} - 1)$, the predicted thermal spectrum $S_0^2(|\beta|^2 + 1)|\beta|^2$ is compared against the measured correlation spectrum. Very good agreement is found with **no free parameters**.

### 6. Dispersion Relation Measurement

The dispersion relation is measured by oscillating the step potential position with 0.5 $\mu$m amplitude, generating waves inside and outside the horizon. Fits of Bogoliubov dispersion relations (with Doppler shift) yield: $c_{\text{out}} = 0.52$ mm/s, $v_{\text{out}} = 0.23$ mm/s, $c_{\text{in}} = 0.31$ mm/s, $v_{\text{in}} = 0.90$ mm/s.

### 7. No Analogue Firewall

The measured correlations between Hawking and partner particles are of the predicted magnitude. No reduction of correlations that would indicate a firewall at the horizon is observed.

## Key Results

1. The Hawking radiation spectrum is thermal, with temperature matching the analogue surface gravity prediction $k_B T_H = 0.35$ nK = $0.12\, mc_{\text{out}}^2$.
2. Correlations lie along the Hawking/partner branch of the dispersion relation (not Hawking/copropagating), confirming the predicted mode structure.
3. The radiation operates in the linear dispersion regime, in direct analogy with massless particle emission from a real black hole.
4. No analogue firewall is observed --- correlations at the horizon are at predicted levels.
5. The agreement with Planck-distributed $|\beta|^2$ at the predicted $T_H$ has no free parameters.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Hawking temperature | $k_B T_H = -\frac{\hbar}{2\pi}\left(\frac{c}{n}\frac{dn}{dx} + \frac{dc}{dx}\right)\bigg\|_{x=0}$ | Eq. (1) |
| Correlation extraction | $S_0 \langle \hat{b}_H \hat{b}_P \rangle = \sqrt{\frac{\xi_{\text{out}}\xi_{\text{in}}}{L_{\text{out}}L_{\text{in}}}} \int dx\, dx'\, e^{ik_H x} e^{ik_P x'} G^{(2)}(x,x')$ | Eq. (2) |
| Speed of sound | $c(x) = \sqrt{\frac{2\hbar a\omega_r n}{m}} \frac{\sqrt{1+3na/2}}{(1+2na)^{3/2}} - \frac{\hbar\omega_{r0}}{2U_0}$ | Eq. (3) |
| Planck distribution | $\|\beta\|^2 = \frac{1}{e^{\hbar\omega/k_B T_H} - 1}$ | In text |
| Bogoliubov transform | $\hat{b}_H = \alpha\hat{b}_+ + \beta\hat{b}_-^\dagger$, $\hat{b}_P = \alpha\hat{b}_- + \beta\hat{b}_+^\dagger$ | In text |
| Predicted correlation | $S_0^2 \|\langle \hat{b}_H \hat{b}_P \rangle\|^2 = S_0^2(\|\beta\|^2 + 1)\|\beta\|^2$ | In text |
| Analogue surface gravity | $g = c(dv/dx - dc/dx)\big\|_{\text{horizon}}$ | Ref. [8] |
| Healing length | $\xi = \sqrt{\xi_{\text{out}}\xi_{\text{in}}}$, $\xi_{\text{out}(\text{in})} = \hbar/(mc_{\text{out}(\text{in})})$ | In text |
| Structure factor | $S_0 = (U_{k_H} + V_{k_H})(U_{k_P} + V_{k_P})$ | In text |

## Relevance to Phonon-Exflation

This paper provides the definitive experimental confirmation that phonons in a BEC reproduce Hawking radiation with a thermal spectrum at the predicted temperature. This is directly relevant to the phonon-exflation framework in three ways: (1) It validates the acoustic metric formalism where phonons propagate on an effective curved spacetime, the same conceptual foundation underlying the M4 $\times$ SU(3) substrate model. (2) The Steinhauer experiment demonstrates Parker-type cosmological particle creation in a condensed matter analog --- precisely the mechanism identified in Session 38 as the transit physics (instanton gas produces quasiparticle pairs via non-thermal pair creation, not Hawking radiation which requires a horizon). (3) The absence of an analogue firewall and the confirmed Hawking/partner entanglement structure constrain how correlations survive across the analog horizon, informing the GGE permanence results of Sessions 37-38.
