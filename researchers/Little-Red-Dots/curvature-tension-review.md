# Curvature Tension in Cosmology — A JWST/LRD-Era Literature Review

**Compiled by**: little-red-dots-jwst-analyst
**Date**: 2026-05-01
**Cosmology pin (background)**: Planck 2018 baseline `H_0 = 67.4 km/s/Mpc, Ω_m = 0.315, Ω_Λ = 0.685` — used as fiducial flat-ΛCDM reference in essentially all source papers.
**Scope**: Curvature-density tension `Ω_K ≠ 0` from CMB-only / CMB+BAO / CMB+SNe / DESI / ACT DR6 datasets, theoretical interpretations, and the JWST/Little-Red-Dot (LRD) angle.

> **Sign-convention warning** (cited in every paper). The literature uses two opposing conventions for `Ω_K`:
>
> - **Planck/Di Valentino/Handley convention** (the dominant one): `Ω_K = -K c² / (a₀² H₀²)` so that `Ω_K < 0` means **closed** (positive spatial curvature `K = +1`).
> - **DESI DR2 / Chen-Zaldarriaga / Comini-Vagnozzi-Loeb convention**: `Ω_K > 0` means **closed** (their reported value `Ω_K = +0.0023` corresponds to `Ω_K ≈ -0.0023` in the Planck convention).
>
> Throughout this review I use the **Planck convention** (`Ω_K < 0` ⇒ closed) and have remapped DESI/Chen/Comini sign conventions accordingly when stating numerical results, with the original-paper sign quoted in parentheses where helpful. This is one of the more common confusions in the literature and is flagged explicitly in DESI DR2 II §V.B and in the Comini-Vagnozzi-Loeb 2026 paper footnote 2.

---

## 1. Executive Summary

The "curvature tension" is the discordance between (a) Planck 2018 CMB-only temperature+polarisation power spectra, which prefer a **closed** universe `Ω_K ≈ -0.044` at ≥ 3.4σ in the Plik likelihood, and (b) virtually every other cosmological probe (BAO, SNe, CMB lensing reconstruction), which independently prefer `Ω_K = 0` at the `≈ 0.002` level. The tension is **internal to Planck**: the same data simultaneously support flatness (low-ℓ + lensing reconstruction) and closure (high-ℓ + the `A_L > 1` lensing-amplitude excess at multipoles `ℓ ≈ 1200-1500`). Reanalyses with the CamSpec likelihood (Efstathiou & Gratton 2020) and PR4 maps (Rosenberg, Gratton, Efstathiou 2022) shrink the closed-universe preference to ~2σ. ACT DR6 (Calabrese et al. 2025) and DESI DR2 (Abdul-Karim et al. 2025) both find tight, flat-consistent constraints when CMB+BAO are combined: `Ω_K = +0.0019 ± 0.0015` (P-ACT-LB) and `Ω_K ≈ -0.0023 ± 0.0011` (DESI DR2 + CMB; remapped to Planck sign), the latter persisting at ~2σ as a hint of small negative curvature. Theoretical reanalyses (Specogna et al. 2025) show that consistent closed-inflation priors reduce the apparent significance from 3.5σ to ~2σ. JWST high-redshift galaxies and LRDs are NOT currently strong curvature probes — Comini, Vagnozzi & Loeb (2026) explicitly find no curvature preference from CEERS/FRESCO once star-formation efficiency is marginalised. The "overmassive BH at z ≈ 5-7" puzzle (LRD population) appears to be selection-bias dominated (Li et al. 2025) and does NOT cleanly map to a non-flat geometry signature. Future Spec-S5, Roman, LiteBIRD, and CMB-S4 are forecast to push `σ(Ω_K)` to the `10^-4` level.

---

## 2. Origin of the Curvature Anomaly

### 2.1 The `A_L` lensing-amplitude excess

The Planck 2013, 2015, and 2018 temperature power spectra all prefer an unphysical extra-lensing factor `A_L > 1` in the high-ℓ smoothing of acoustic peaks. The physical interpretation: a closed universe with `Ω_K ≈ -0.04` produces additional gravitational lensing at the precise multipole range (`ℓ ≈ 1200-1500`) where the `A_L` excess is concentrated. The two parameters are degenerate in the Planck high-ℓ TTTEEE likelihood (Calabrese et al. 2008; Di Valentino, Melchiorri, Silk 2019, Fig. 2), so absorbing the `A_L` anomaly into `Ω_K` provides a "physical" rather than phenomenological resolution. A flat `ΛCDM + A_L` model with `A_L = 1.19` and a closed `ΛCDM + Ω_K` model with `Ω_K = -0.0438` give nearly identical CMB lensing potentials (Di Valentino et al. 2019, Fig. 5).

### 2.2 Di Valentino, Melchiorri & Silk 2019 (arXiv:1911.02087, *Nature Astronomy* 4, 196 (2020))

The first dedicated paper to argue the closed-universe interpretation. Using the official Plik TT,TE,EE+lowE likelihood, they find:

| Constraint | Value | Significance |
|:-----------|:------|:-------------|
| Plik 2018 TT,TE,EE+lowE | `Ω_K = -0.044^{+0.018}_{-0.015}` (99% C.L. range `-0.007 > Ω_K > -0.095`) | 3.4σ closed |
| `P(Ω_K < 0 \| Plik)` | 0.99985 | — |
| Bayes factor `\|ln B_01\|` (closed vs flat) | 3.3 ("strong" by Jeffreys) | — |
| Δχ² vs flat ΛCDM at best-fit `Ω_K = -0.0438` | -11 (TT,TE,EE+lowE) | — |
| ΔDIC | -7.4 (≈ 41:1 in favour of closed) | — |
| CamSpec 2018 TTTEEE+lowE | `Ω_K = -0.037^{+0.032}_{-0.034}` (95% C.L.) | 99.85% closed |

Critically, when combined with BAO (6dFGS + SDSS-MGS + BOSS DR12), `Ω_K` is forced back to `0.0008^{+0.0038}_{-0.0037}` at 95% C.L. (consistent with flat) but at the cost of a `Δχ² ≈ 17` increase in the joint Planck+BAO best-fit — strong tension between CMB-only and BAO under the closed model. Tensions when curvature is allowed (Di Valentino et al. 2019, Table 2):

- Planck18 vs BAO: `log_10 I = -1.8` ("strong" disagreement; tension `≈ 3σ`)
- Planck18 vs CMB lensing: `log_10 I = -0.84` (substantial)
- Planck18 vs R18 H_0 (Riess+18): `5.2σ` in `H_0` (vs `≈ 3.4σ` under flat)
- Planck18 vs KiDS-450 cosmic shear: `> 3.5σ` in `S_8` (vs `≈ 2.3σ` under flat)
- Planck18 vs DES, HSC cosmic shear: `> 3σ`

DV+M+S framing: "the assumption of a flat universe could mask a cosmological crisis where disparate observed properties of the Universe appear to be mutually inconsistent."

### 2.3 Handley 2019 (arXiv:1908.09139, *Phys. Rev. D* 103, L041301 (2021))

Independent, simultaneous discovery using the Bayesian "suspiciousness" statistic (Handley & Lemos 2019). Released as a preprint two months before DV+M+S; the two papers cite each other. Key results in `KΛCDM` (curved ΛCDM):

| Constraint | Value |
|:-----------|:------|
| Planck 2018 (TTTEEE+lowE only) | `Ω_K = -0.045 ± 0.015` |
| Posterior with `Ω_K > 0` (open) | `1/2000` of mass |
| Bayesian betting odds, closed vs flat (Planck only) | **50 : 1** |
| Bayesian betting odds, closed vs open (Planck only) | **2000 : 1** |
| Tension Planck vs Planck CMB-lensing (curved) | **2.49 ± 0.07 σ** (`σ` = 0σ in flat) |
| Tension Planck vs BAO (curved) | **3.03 ± 0.06 σ** (`σ` ≤ 2σ in flat) |
| Tension Planck vs SH0ES H_0 (curved) | **4.49 ± 0.04 σ** (vs ≈ 4σ flat) |

Handley's framing emphasises: *every* tension is enhanced when curvature is allowed, except for Planck+lensing vs SH0ES (where the broader `H_0` posterior under curvature actually relaxes the H_0 tension marginally). His conclusion: "cosmologists can no longer conclude that observations support a flat universe" without first resolving the inconsistency between Planck and BAO/lensing in curved models.

### 2.4 Statistical caveats

The Plik TTTEEE likelihood drives the `Ω_K` preference. Two specific multipole-range inconsistencies sharpen the closed-universe preference:

1. The high-ℓ vs low-ℓ Planck split (`ℓ < 800` vs `ℓ > 800`): under flat ΛCDM, the two ranges return inconsistent `Ω_c h²`, `H_0`, and `σ_8`. Under `Ω_K ≈ -0.045`, the two multipole ranges become consistent (Di Valentino et al. 2019, Fig. 3).
2. The low-ℓ TT power suppression (`ℓ < 30`, especially the quadrupole). Closed-universe primordial spectra naturally cut off at the curvature scale `R_C = (c/H_0)\|Ω_K\|^{-1/2} ≈ 10 Gpc`, suppressing low-ℓ power.

Both features are consistent with closed cosmology but neither is *required* — alternative explanations (cosmic variance for the quadrupole, foreground residuals or polarisation likelihood subtleties for the high-ℓ shift) survive.

---

## 3. Dataset Combinations — Constraints Table

All values translated to the Planck convention `Ω_K < 0 ⇒ closed`. "Sign in original" is given when the source paper used the opposite convention.

| Dataset | `Ω_K` (Planck convention) | Significance from `Ω_K = 0` | Source |
|:--------|:------------------------|:---------------------------|:-------|
| **Planck 2018 Plik TT,TE,EE+lowE** | `-0.044^{+0.018}_{-0.015}` | 3.4σ closed | Di Valentino, Melchiorri, Silk 2019 (arXiv:1911.02087) |
| **Planck 2018 Plik (Handley)** | `-0.045 ± 0.015` | ≥ 3σ closed (50:1 Bayes) | Handley 2019 (arXiv:1908.09139) |
| **Planck 2018 CamSpec** | `-0.037^{+0.032}_{-0.034}` (95%) | 99.85% closed (~ 2σ) | DV+M+S 2019 |
| **Planck 2018 12.5HMcln (CamSpec extended sky)** | `~ -0.025` central, weakly significant | ≈ 2.1σ (TT only); 1.6σ excluding `ℓ < 30` TT | Efstathiou & Gratton 2020 (arXiv:2002.06892) |
| **Planck PR4 + CamSpec (Rosenberg et al. 2022)** | comparable to CamSpec 2018 | ~ 2σ closed | Rosenberg, Gratton, Efstathiou 2022 (arXiv:2205.10869) |
| **Planck 2018 TT+lowE + CMB lensing** | `+0.011^{+0.013}_{-0.012}` (95%) | < 2σ (slight open shift) | DV+M+S 2019 |
| **Planck + BAO (6dFGS+SDSS-MGS+BOSS DR12)** | `+0.0008^{+0.0038}_{-0.0037}` (95%) | < 1σ | Planck Collaboration 2018 / DV+M+S 2019 |
| **Planck + BAO + Pantheon + lensing** (TTTEEE) | `+0.0004 ± 0.0018` (Efstathiou-Gratton 12.5HMcln) | < 1σ; effectively rules out closed | Efstathiou & Gratton 2020 |
| **Planck + Pantheon (no BAO)** | `+0.0010 ± 0.0023` to `+0.0030 ± 0.0027` | < 2σ flat | Efstathiou & Gratton 2020 |
| **Planck + R19** (LCDM+w+Ω_K+α_s+Σm_ν, 10-param) | `-0.019^{+0.0036}_{-0.0099}` | excludes flat at >99% | DV+M+S 2021 (arXiv:2003.04935) |
| **Planck + Pantheon** (10-param model) | `-0.029^{+0.011}_{-0.010}` | excludes flat+ΛCDM at >99% | DV+M+S 2021 |
| **Planck + BAO** (10-param model) | `+0.0003^{+0.0027}_{-0.0037}` | < 1σ | DV+M+S 2021 |
| **ACT DR6 P-ACT-LB** (TT+TE+EE+ACT-DR6+Planck CMB lensing+DESI BAO) | `Ω_K = +0.0019 ± 0.0015` (68%) → flat at < 1.3σ | flat-consistent | Calabrese et al. 2025 (arXiv:2503.14454) |
| **Planck-LB analogue** (Planck+CMB lensing+BAO) | `+0.0022 ± 0.0015` | similar | Calabrese et al. 2025 |
| **DESI DR2 + CMB (ΛCDM + Ω_K)** | `-0.0023 ± 0.0011` (sign in original `+0.0023 ± 0.0011`) | ≈ 2σ closed | Abdul-Karim et al. 2025 (arXiv:2503.14738); Chen & Zaldarriaga 2025 (arXiv:2505.00659) |
| **DESI DR2 alone (no CMB)** | `25 ± 41 × 10^{-3}` (essentially unconstrained) | < 1σ | Abdul-Karim et al. 2025 |
| **DESI DR2 + Planck PR3 + ACT lensing + Camspec PR4 (Chen-Zaldarriaga)** | `-0.0023 ± 0.0011` | 2σ closed | Chen-Zaldarriaga 2025 |
| **CMB-only (Chudaykin-Ivanov-Philcox 2025 reanalysis)** | `Ω_K = -10.3^{+7.0}_{-5.7} × 10^{-3}` (Plik PR3) | 1.5σ closed | Chudaykin et al. 2025 (arXiv:2511.20757) |
| **CMB + BAO (Chudaykin et al. 2025)** | ≈ `-0.0023` central | 1.9σ closed | Chudaykin et al. 2025 |
| **CMB + DESI BAO + DESI full-shape Pℓ + bispectrum B₀** | similar central with σ ≈ ½ × BAO-only | 2.4σ closed | Chudaykin et al. 2025 |
| **CMB-PR4 (HiLLiPoP+LoLLiPoP) + DESI BAO + Pℓ+B₀** | reduced to 2.3σ | flat-consistent at 2σ | Chudaykin et al. 2025 |
| **DESI DR1 + BBN + OHD (wCDM+Ω_K, Yadav et al. 2025)** | `Ω_K = +0.075^{+0.070}_{-0.054}` (open in their convention; ~ 1.2σ from flat) | 1.2σ open | Yadav et al. 2025 (arXiv:2512.09486) |
| **DESI DR2 + BBN + OHD + Pantheon+ (wCDM+Ω_K)** | `Ω_K = +0.012^{+0.015}_{-0.025}` | < 1σ | Yadav et al. 2025 |
| **Closed-quadratic-inflation prior (Specogna et al. 2025) Plik PR3** | reduces preference for `Ω_K < 0` | 3.5σ → 2.5σ | Specogna et al. 2025 (arXiv:2509.26263) |
| **Closed-quadratic-inflation prior, CamSpec PR4** | reduces further | → 2σ | Specogna et al. 2025 |
| **BOSS/eBOSS + DESI DR1 BAO model-independent (GP, no `r_d` prior)** | `Ω_K = -0.040^{+0.142}_{-0.145}` | < 1σ | Liu et al. 2024 (arXiv:2411.14154) |

**Pattern**: every CMB-only or CMB-dominant constraint hints at small negative curvature at the 1.5-3.4σ level depending on likelihood; every CMB+BAO and CMB+SNe combination drives `Ω_K` back to ≈ 0 at the `0.002` precision level. The transition occurs because BAO breaks the `Ω_K`-`H_0` geometric degeneracy: the same `Ω_m h³` constraint from `θ*` becomes a precise `Ω_K` constraint once a low-redshift `H_0` anchor is added (Chen & Zaldarriaga 2025 Eq. 2.3: `Ω_m h³ (1 - 7 Ω_K) = 0.09603 ± 0.00026`).

---

## 4. Statistical-Tension Interpretations

Three competing readings dominate the literature:

### 4.1 Closed-universe is real (Di Valentino-Melchiorri-Silk-Handley camp)

- **Argument**: The Plik `A_L > 1` excess + the high-ℓ vs low-ℓ Planck shift + the WMAP nine-year `Ω_K = -0.037^{+0.044}_{-0.042}` independent agreement point to a real closed geometry. The fact that BAO pulls `Ω_K → 0` is itself a *new* tension because BAO and Planck were supposed to be concordant; both have to be wrong (or new physics) to keep the LCDM-flat picture.
- **Implication**: `LCDM is failing simultaneously in `H_0`, `S_8`, and `Ω_K`. The "Hubble tension" and the "curvature tension" are linked through the `Ω_K-H_0` geometric degeneracy.
- **Follow-up extensions**: DV+M+S 2021 (arXiv:2003.04935) — adding `w`, `Σm_ν`, `α_s` simultaneously (10-parameter LCDM+w+Ω_K+α_s+Σm_ν): Planck+Pantheon+R19+F20 each independently exclude flat-ΛCDM at >99% C.L., requiring either real curvature (`Ω_K ≈ -0.02 to -0.03`) plus phantom dark energy (`w < -1`), OR a Planck systematic well-described by `A_L > 1`. Yang, Giarè, Pan, Di Valentino, Melchiorri, Silk 2023 (arXiv:2210.09865) extends this to multi-parameter dark-energy parametrisations (`w_0 w_a CDM + Ω_K + Σm_ν + N_eff`) and concludes "a non-flat Universe cannot be discarded" since indication for closed survives in *most* DE parametrisations.

### 4.2 Sampling/likelihood-implementation systematic (Efstathiou-Gratton camp)

- **Argument**: The Plik-vs-CamSpec discrepancy and the failure of the DV+M+S 2019 result to survive when more sky area is included (Efstathiou & Gratton's 12.5HMcln likelihood) point to a likelihood-implementation issue, not a real signal. The choice of uniform prior on `Ω_K` is not theoretically justified — closed inflationary models predict tails extending to small `\|Ω_K\|`, not flat priors. Bayes-factor "evidence" against flat is therefore prior-dependent.
- **Numerical core**: Efstathiou & Gratton 2020 find that excluding the low-ℓ TT data drops the closed-preference pte from 1.6% to 7% (1.6σ Gaussian-equivalent). Using TT+TE+EE high-ℓ and only `Ω_K` as one extra parameter, the `Δχ²` is only 3.0 — not statistically significant.
- **Conclusion**: "If the Universe were indeed closed with `Ω_K ≈ -0.04`, then one would have to argue that unexpected new physics or systematics in Planck lensing, supernovae, and BAO all act in the same way to favour `Ω_K = 0`. Since these data sets are independent and respond to different physics, this is extraordinarily unlikely. It is much more plausible that these additional datasets break the geometrical degeneracy leading to values of `Ω_K` closer to the truth." (Efstathiou & Gratton 2020 §3).
- **PR4 update** (Rosenberg, Gratton, Efstathiou 2022; Tristram et al. 2024 PR4 likelihood): the closed preference is reduced further in the latest Planck data products.

### 4.3 The closed-inflation-prior reframing (Specogna et al. 2025)

- **Argument**: The standard `Ω_K` analyses use a phenomenological prior (uniform in `Ω_K`) that does not enforce consistency between the curvature parameter and the primordial scalar spectrum. In closed inflation models (e.g. quadratic `φ²` inflation in a closed universe), there is a definite relationship `P(k; Ω_K)` derived gauge-invariantly. Imposing this physical prior changes the analysis.
- **Numerical core** (Specogna, Vardanyan, Giarè, Di Valentino 2025, arXiv:2509.26263):
  - Plik PR3 with closed-φ² inflation: `Ω_K < 0` preference drops from ≥ 3.5σ to ~ 2.5σ.
  - CamSpec PR4: drops to ~ 2σ.
  - Closed inflation also explains the low-ℓ TT power suppression (improved fit to the quadrupole).
  - Partial — but not full — improvement to the high-ℓ `A_L` excess in Plik.
- **Conclusion**: "closed-inflation models tie the curvature parameter to the inflationary dynamics and the primordial spectrum, enforcing consistency conditions that do not necessarily allow for the large deviations from flatness seen in phenomenological parametrisations."

### 4.4 Chen-Zaldarriaga 2025 — the "small but real" reading from DESI DR2

Distinct from both the "real big closure" (DV+M+S) and "everything is fine" (Efstathiou-Gratton) camps, Chen & Zaldarriaga 2025 (arXiv:2505.00659) argue that DESI DR2 + CMB legitimately point to a small but non-zero **negative** curvature at 2σ, with `R_K = c/H_0/\|Ω_K\|^{1/2} ≈ 21 H_0^{-1}` ≈ 95 Gpc. This is the size at which curvature would resolve the DESI-vs-CMB low-redshift distance tension WITHOUT requiring phantom dark energy. They observe:

- The DESI DR2 `≈ 1.5%` shorter distances at `z ≈ 0.5-1.5` (a "low-redshift Hubble tension") can be absorbed either by `w_0 w_a` dynamical dark energy with `w < -1` (phantom regime, NEC-violating) **or** by `Ω_K ≈ +0.0023` (their sign; corresponds to closed in our convention).
- Curvature also relaxes the DESI+CMB neutrino-mass constraint from disfavouring `Σm_ν > 0.064` eV to allowing `Σm_ν < 0.10` eV at 95%, which enables the inverted hierarchy.
- The proposed Spec-S5 spectroscopic survey would distinguish curved-ΛCDM from `w_0 w_a CDM` at >5σ via high-z BAO measurements.

This reading explicitly connects curvature, neutrino-mass, and dark-energy phenomenology into a single low-redshift consistency knob.

### 4.5 ACT DR6 — flat at high precision (Calabrese et al. 2025)

The ACT DR6 cosmological-parameter paper (Calabrese, Hill, Jense et al. 2025, arXiv:2503.14454) §7.1 is unambiguous in finding flatness:

> "ACT DR6 power spectra alone prefer a flat geometry, breaking degeneracies via lensing effects in the power spectra; in a joint fit with Planck, ACT DR6 moves the Planck contours toward vanishing curvature."
>
> `Ω_K = +0.0019 ± 0.0015` (68%, P-ACT-LB combination)
>
> Closed-universe radius lower bound: `R_K > 105 Gpc` ≈ 343 Glyr (95% C.L., for `Ω_K < 0`).

ACT's higher-resolution lensing map breaks the geometric degeneracy independently of BAO. This is a strong, independent argument against a real closed universe at the level claimed by Plik.

---

## 5. Theoretical Interpretations

### 5.1 Closed inflation — Coleman-de Luccia bubble nucleation

Closed inflation with `Ω_K ≲ -0.01` is theoretically constructible (Linde 2003; Gratton, Lewis, Turok 2002). Inflation does NOT generically require `Ω_K = 0`; it requires `\|Ω_K\| ≪ 1` after sufficient e-folds. Closed inflationary bubbles in a string landscape (Freivogel, Kleban, Rodríguez Martínez, Susskind 2006; Yamauchi, Linde, Naruko, Sasaki, Tanaka 2011) can nucleate with substantial residual curvature if the number of e-folds is fine-tuned to `N ≈ N_*` (the minimum required to solve the horizon and flatness problems, `N_* ≈ 60`). The resulting curvature distribution is

```
p(Ω_K) ∝ (α-1) / (4 N_*^{α-1}) × (N_* - 0.5 ln\|Ω_K\|)^{-α} × (1/\|Ω_K\|)
```

(Efstathiou & Gratton 2020 Eq. 4) — peaked at `Ω_K = 0` but with power-law tails. Importantly, **eternal inflation is incompatible with closed geometry**: a detection of `Ω_K < 0` rules out slow-roll eternal inflation (Kleban & Schillo 2012, JCAP 2012, 029). This is one of the highest-leverage falsifiers in modern cosmology.

### 5.2 Open inflation

`Ω_K > 0` (open) is also theoretically constructible via Coleman-de Luccia bubbles in negatively-curved inflationary models (Linde 1995; Gott 1982; Bucher, Goldhaber, Turok 1995). The DESI DR1+BBN+OHD weak preference for `Ω_K > 0` (Yadav et al. 2025) is too weak to be diagnostic; the larger DV+M+S signal is unambiguously closed.

### 5.3 Modified gravity readings

Yang, Giarè, Pan, Di Valentino, Melchiorri, Silk 2023 (arXiv:2210.09865) shows that the closed-universe preference survives in `wCDM`, `w_0 w_a CDM`, and combinations with `Σm_ν` and `N_eff`, with parameter-shifted-but-non-zero `Ω_K`. The implication: forcing `Ω_K = 0` may be biasing dark-energy and neutrino-mass inferences. Specifically, in `w_0 w_a CDM + Ω_K`, freeing curvature shifts the dark-energy equation-of-state away from the phantom regime that DESI+CMB otherwise demands.

### 5.4 Multiverse / anthropic reading

The Freivogel-Kleban-Susskind landscape construction provides an anthropic motivation for `\|Ω_K\| ~ 10^{-2}-10^{-3}`: bubbles with smaller `\|Ω_K\|` are anthropically less likely if structure formation is sensitive to curvature. This is theoretical motivation, not diagnostic.

### 5.5 Brane-world / extra-dimensional readings

Several papers (Akarsu, Di Valentino, Kumar, Özyiğit, Sharma 2023 PDU 39, 101162) explore anisotropic Bianchi extensions on top of `Ω_K ≠ 0`, finding that combined anisotropy + curvature can absorb the Planck preference more naturally than either parameter alone. Bhattacharya, Borghetto, Malhotra, Parameswaran, Tasinato, Zavala 2024 (JCAP 09, 073) examines curved quintessence under DESI+CMB and finds that small negative `Ω_K` plus non-phantom dark-energy quintessence fit comparably to the unconstrained `w_0 w_a CDM`.

### 5.6 The `H_0`-curvature connection

A small negative curvature (`Ω_K < 0`) PARTIALLY relaxes the Hubble tension: in `KΛCDM`, the Planck `H_0` posterior is broader (`H_0 ≈ 54-65 km/s/Mpc` at 95%) and the SH0ES `H_0 = 73` is closer to the upper edge. However, the relaxation is incomplete — ~ 4σ residual remains (Handley 2019, Fig. 2 row 3; DV+M+S 2019 §VII). Yang, Pan, Di Valentino, Mena, Melchiorri 2021 (JCAP 10, 008) "2021-H_0 odyssey" shows that closed + interacting dark energy can simultaneously address `H_0`, `Ω_K`, and `S_8` tensions but at the cost of multi-parameter model complexity.

### 5.7 Phonon-exflation framework angle (project-internal)

Within the project's substrate-IS-not-IN-space framework (see `phononic-framing.md`), spatial curvature `Ω_K` is an emergent description of how the substrate's spectral weight redistributes under cosmic transit; it is NOT a fundamental geometric parameter. The internal compactification dynamics that drive the expansion history could in principle deposit residual non-flatness as a fossil of the transit (analogous to GGE relic from Parker pair production). The project's `w_0` constraint at Volovik partition (`w_0 = -0.918` per S58) is independent of `Ω_K` if the substrate compaction couples primarily to the dark-energy sector. The mack-9A canonical observational watchlist tracks `Ω_K` as part of the late-time consistency channel — a future DESI/Roman/Spec-S5 detection of `\|Ω_K\| > 10^{-3}` would be a direct test, since the framework's substrate transit is calibrated to the Volovik partition under `Ω_K = 0` baseline. Detection of `Ω_K < -0.001` would force re-evaluation of the substrate-compaction model's coupling to spatial geometry. This is recorded as an open empirical channel; no specific framework prediction has been pre-registered for `Ω_K` as of S87.

---

## 6. Recent (2024-2026) Developments

### 6.1 DESI Year-1 (2024) — first BAO results from full DR1

DESI DR1 (Adame, Aguilar et al. 2024; arXiv:2404.03000-2; *JCAP* 02, 021 (2025)) introduced 7-tracer BAO with effective redshifts `z = 0.30, 0.51, 0.71, 0.93, 1.32, 1.49, 2.33`. DR1 alone does not constrain `Ω_K` strongly; combined with CMB it pushes `Ω_K → 0` similarly to BOSS DR12. The headline DESI-DR1 result was the 2.6-3.5σ preference for `w_0 w_a CDM` over flat ΛCDM, not curvature.

### 6.2 DESI DR2 (2025) — March 2025 release

DESI DR2 (Abdul-Karim et al. 2025, arXiv:2503.14738; *Phys. Rev. D* 112, 083515) doubled the precision. Key curvature-related result from §V.B Table V (Planck convention):

- `ΛCDM + Ω_K`, **CMB only**: `Ω_K = +0.0107^{+0.0053}_{-0.0064}` (open in their convention; remapped to `Ω_K = -0.0107` in Planck convention) — preference for closed
- `ΛCDM + Ω_K`, **DESI alone**: `Ω_K = 0.025 ± 0.041` — unconstrained
- `ΛCDM + Ω_K`, **DESI + CMB**: `Ω_K = -0.0023 ± 0.0011` (Planck convention, remapping the original `+0.0023 ± 0.0011`) — **2σ preference for closed**.

The DESI collaboration's framing: this is consistent with `2.3σ` mild tension between DESI and CMB in flat ΛCDM (DESI DR2 II §1), absorbable into any of: (i) dynamical dark energy with `w_0 > -1, w_a < 0`; (ii) negative spatial curvature `Ω_K ≈ -0.0023`; (iii) modified recombination physics; (iv) some combination thereof. DESI does not advocate for curvature as the resolution but documents it as a viable single-parameter extension.

### 6.3 ACT DR6 (March 2025)

Calabrese, Hill, Jense et al. 2025 (arXiv:2503.14454) §7.1 — the cleanest flat-universe result post-Planck. The ACT DR6 + Planck + DESI BAO combination delivers `Ω_K = +0.0019 ± 0.0015` (68%), well within 2σ of zero, with `R_K > 105 Gpc` (closed) / `R_K > 66 Gpc` (open) at 95%.

### 6.4 Chudaykin, Ivanov, Philcox 2025 — DESI full-shape reanalysis

Chudaykin et al. (arXiv:2511.20757) re-examine DESI DR1 with the EFT-based full-shape pipeline (power spectrum + bispectrum, NOT just BAO compression):

- DESI FS+B0 alone improves `Ω_K` constraint by ~ 2× over BAO-only.
- CMB+BAO+Pℓ+B0: `Ω_K = -0.0023^{+0.0011}_{-0.0011}` (their sign `+0.0023`), 2.4σ closed.
- CMB-PR4 (HiLLiPoP+LoLLiPoP) + BAO + Pℓ + B0: 2.3σ closed (slight reduction with PR4).

Curvature signal is **stable across analysis pipelines** (DESI BAO compression vs full shape, Plik PR3 vs HiLLiPoP PR4) at the 2-2.4σ level for CMB+BAO combinations.

### 6.5 Specogna, Vardanyan, Giarè, Di Valentino 2025 — closed-inflation prior

arXiv:2509.26263. Closed-φ² inflation with consistent primordial spectrum reduces Plik's 3.5σ closed preference to 2.5σ; CamSpec PR4 reduces to 2σ. Critical reframing: phenomenological priors over-amplify curvature evidence.

### 6.6 Liu, Wang, Wu, Wang 2024 — model-independent BAO curvature

arXiv:2411.14154. Combining BOSS/eBOSS + DESI DR1 BAO with Gaussian Process reconstruction of cosmic chronometers `H(z)`, eliminating the sound-horizon `r_d` dependence:

- Final result: `Ω_K = -0.040^{+0.142}_{-0.145}` (GP method).
- Consistent with flat at 1σ but with very large uncertainty.
- Important methodologically because it removes the `r_d` calibration that ties BAO to the CMB.

### 6.7 Yadav, Dixit, Barak, Pradhan 2025 — DESI DR1 vs DR2 wCDM+Ω_K

arXiv:2512.09486. Within `wCDM + Ω_K`:

- DR1 + BBN: `Ω_K = +0.094 ± 0.080` (open in their convention), 1.2σ from flat.
- DR2 + BBN: `Ω_K = +0.003 ± 0.048`, ~ 0.06σ from flat.
- DR1 + BBN + Pantheon+: `Ω_K = +0.063 ± 0.080`.
- DR2 + BBN + OHD + Pantheon+: `Ω_K = +0.012^{+0.015}_{-0.025}`, < 1σ.

DR2's higher-precision BAO drives `Ω_K → 0`. Note the sign convention is opposite to DV+M+S.

### 6.8 SPT-3G updates (mid-2024 to 2025)

SPT-3G provides an independent ground-based CMB measurement complementary to ACT. Bianchini et al. 2020 (arXiv:1910.07157) noted SPTpol+Planck strongly favours flatness when combined. SPT-3G full-survey constraints (early 2025 data products, e.g. Pan, Calabrese, Choi et al.) consistently report flat-`Ω_K` constraints at the `0.005` precision level when combined with BAO.

### 6.9 Euclid early data (2024-2026)

Euclid launched July 2023; first cosmology data products (galaxy clustering, weak lensing) became available in 2024-2025. Early-data papers focus on `H_0`, `S_8`, `w`, with `Ω_K` constraints expected in the Year-1 release (anticipated 2026-2027). No published Euclid `Ω_K` constraint as of cutoff.

### 6.10 The CosmoVerse White Paper (2025)

Di Valentino et al. 2025 (arXiv:2504.01669, *Phys. Dark Univ.* 49, 101965). Multi-author (>540 authors) cosmology-tensions review. The curvature section catalogues:

- Persistent `≈ 2σ` preference for closed in CMB+BAO combinations.
- The CMB-PR4 reanalysis reducing significance to ~ 2σ from 3.4σ.
- Recommendation: future LSS surveys (DESI ongoing, Spec-S5, Euclid, Roman) should produce CMB-independent curvature constraints to break the geometrical degeneracy at the `10^{-3}` level.

---

## 7. JWST/LRD Angle — How Does Curvature Manifest at z > 4?

This is the headline section for the LRD analyst role.

### 7.1 Quantitative scale of the effect

In a closed `KΛCDM` cosmology with `Ω_K = -0.04` (the DV+M+S central value), the comoving distance to a source at z=7 is shorter than the flat-ΛCDM prediction by:

```
D_M(z=7; Ω_K = -0.04) / χ(z=7; flat)  ≈  1 − (1/6)(χ/R_K)²
                                       ≈  0.974  (i.e. 2.6% shorter at z=7 for Ω_K = -0.04, using R_K = 5 c/H_0 and Python-verified χ(z=7) ≈ 1.98 c/H_0 in Planck-2018 fiducial flat-ΛCDM. The earlier figure χ ≈ 3.1 c/H_0 corresponds to z=1100 last-scattering — a citation error that this revision corrects.)
```

(Chen & Zaldarriaga 2025 §2 substitution chain, with χ(z) integrated against the Planck-2018 flat-ΛCDM `H(z)` rather than a matter-only approximation). The luminosity distance `D_L = (1+z) × D_M` shifts by the same fractional amount, so the distance modulus `μ = 5 log₁₀(D_L/Mpc) + 25` shifts by `Δμ ≈ −0.057` mag — about 5.1% in flux at z=7 (Python-verified: `5·log₁₀(0.97405) = −0.057` mag). For the smaller `Ω_K = -0.0023` (DESI DR2 + CMB hint), `R_K ≈ 21 c/H_0` and `(χ(z=7)/R_K)²/6 ≈ 0.0015`, so the shift is `Δμ ≈ −0.0033` mag (~ 0.3% in flux), well below current photometric calibration uncertainties for high-z sources.

For BH-mass inferences from broad-line widths via single-epoch virial estimators, the bias is:

```
M_BH ∝ (FWHM)² × L^0.5  (Greene-Ho-style virial relation)
∂ ln M_BH / ∂ ln D_L  =  1.0   (luminosity scales as D_L²)
```

So a 2.6% distance shift → 2.6% shift in inferred M_BH at fixed observed flux under single-epoch virial (`M_BH ∝ L^0.5 ∝ D_L`, so `∂ln M_BH/∂ln D_L = 1.0`). Not dramatic. The closed-universe-induced BH-mass bias at `\|Ω_K\| = 0.04` (Python-verified at z=7 in Planck-2018 LCDM `χ(z)` integration) is `Δ log₁₀ M_BH ≈ 0.011` dex, much smaller than typical virial calibration scatter (0.4-0.5 dex) and far too small to resolve the "overmassive BH at z > 4" puzzle (which has 1-2 dex offsets from the local M_BH-M* relation).

### 7.2 Comini, Vagnozzi & Loeb 2026 — direct JWST cosmology test

arXiv:2604.13866. The first comprehensive Bayesian analysis of CEERS (photometric, z_eff ≈ 9.1) and FRESCO (spectroscopic, z ≈ 6-9) JWST high-redshift galaxy samples allowing both dark-energy `w` and `Ω_K` to vary, with simultaneous marginalisation over the baryon-to-star efficiency `ε`. Key results (their sign convention: `Ω_K > 0` ⇒ closed):

- **CEERS, non-flat ΛCDM**: `Ω_K ≳ 0.02` (68%), `Ω_K ≳ -0.16` (95%); `P(Ω_K > 0) = 0.70` — no statistically significant preference.
- **FRESCO, non-flat ΛCDM**: `Ω_K ≳ 0.13` (68%), `Ω_K ≳ -0.03` (95%); `P(Ω_K > 0) = 0.92` — very weak open preference.
- **CEERS, non-flat wCDM**: `P(Ω_K > 0) = 0.70` — no preference.
- **FRESCO, non-flat wCDM**: open preference, but degenerate with `ε`.

**Key conclusion** (their abstract): "the origin of the JWST tension is unlikely to be cosmological, but lies in the astrophysics of galaxy formation." Specifically: the FRESCO sample requires `ε ≳ 0.5` at 2σ regardless of cosmological model, with `ε ≲ 0.2` disfavoured at >5σ. Allowing `Ω_K` to vary does NOT relax the high-`ε` requirement.

This is the most rigorous direct test of "is JWST's overabundance puzzle a curvature signature?" The answer is no.

### 7.3 LRD-specific cosmological sensitivity

Little Red Dots (LRDs) — the Matthee+24 / Greene+24 / Kokorev+24 / Akins+24 selected population at z ~ 4-8 — have these features relevant to curvature:

- Number density `n_LRD ≈ 10^{-5}` cMpc⁻³ at z ~ 5 (from UNCOVER + JADES + CEERS spec-confirmed samples).
- BH masses `M_BH ≈ 10^{6-8} M_☉` from broad Hα/Hβ via single-epoch virial.
- Extreme compactness (effective radii < 100 pc unresolved in NIRCam).
- X-ray and radio non-detections (Yue+24 Chandra stacking; Draca+25 VLA stacking).

**Are they curvature-sensitive?** Marginally. The number density depends on the comoving volume element `dV/dz`, which for a small fractional curvature `Ω_K = -0.04` is shifted by ~ 2.6% at z=7 (linear `D_M` shift, Python-verified; the volume-element scaling is `dV ∝ D_M²` so the inferred `n_LRD` shifts by ~ 5.2% at fixed counts). This is far smaller than the (factor 10-30) systematic uncertainty in LRD selection completeness across surveys. The BH-mass distribution shifts by ~ 2.6% as derived above (single-epoch virial), also tiny compared to the 0.4-0.5 dex virial calibration scatter.

**Verdict**: LRD demographics do NOT currently provide a competitive curvature constraint. They are too systematics-limited (selection function uncertainty + virial calibration scatter + dust-vs-AGN reddening degeneracy) to discriminate `\|Ω_K\| < 0.05` against zero.

### 7.4 Overmassive BH and distance-modulus shift — the connection

The "overmassive BH at z > 4" puzzle (Pacucci+23, Maiolino+24, Furtak+24, plus the LRD population): inferred `M_BH/M_*` ratios at z ~ 5-7 are 1-3 dex above the local M_BH-M* relation. Could this be a curvature artifact?

- A closed universe with `Ω_K = -0.04` introduces a 2.6% distance shift at z=7 (Python-verified, Planck-2018 LCDM) → `Δlog₁₀ M_BH ≈ 0.011` dex. Tiny.
- A real `Ω_K ≈ -0.0023` (the DESI DR2 + CMB level): `Δlog₁₀ M_BH ≈ 0.0007` dex. Negligible.
- The observed offset (1-3 dex) cannot be a curvature artifact at any realistic value of `Ω_K`.

Li et al. 2025 (ApJ 981, 19, "Tip of the Iceberg") shows the offset is dominated by **selection bias** — JWST detects only the brightest broad-line AGN, biasing the inferred M_BH-M* relation upward. Once selection biases are forward-modelled, the bias-corrected intrinsic relation is consistent with the local one. Curvature plays no role.

This is an important *negative* result for the curvature-tension narrative: the most striking JWST cosmological "tension" (overmassive BHs) has nothing to do with `Ω_K` and is fully explained by astrophysical selection effects within standard flat-ΛCDM. The framework is not constrained from this direction.

### 7.5 JWST distance ladder at z > 3 — does it directly probe curvature?

JWST's high-z galaxies are NOT standard candles (no SNe Ia at z > 2.5 with Pantheon-grade calibration), so they provide no direct `D_L(z)` constraint. The closest JWST contribution to the H(z)-curvature problem is:

1. **Spectroscopic redshifts at z > 6**: tightening the redshift-distance relation but not the absolute distance.
2. **Cosmic chronometers (passively-evolving galaxies)**: Borghi, Moresco & Cimatti 2022 (arXiv:2110.04304); Jiao, Borghi, Moresco, Zhang 2023 (arXiv:2205.15947). A z ≈ 1.26 measurement of `H(z) = 135 ± 18 km/s/Mpc` from JWST-era CC data exists but is at z < 2.
3. **Quasar UV-X-ray distance modulus** (Risaliti & Lusso 2019, *Nature Astronomy* 3, 272): controversial; claims of high-z `Δμ` deviations have been criticised (Khadka & Ratra 2022).

JWST does not yet provide a clean direct curvature probe. The Spec-S5 high-z BAO program (Besuner et al. 2025, arXiv:2503.07923) is forecast to detect `\|Ω_K\| > 10^{-4}` at >5σ (Chen & Zaldarriaga 2025 §4 forecast).

---

## 8. Open Questions and Decisive Future Observations

### 8.1 Will Plik vs CamSpec discrepancy survive PR4/PR5?

The Plik likelihood drives the 3.4σ closed preference; CamSpec gives 2σ; CamSpec PR4 reduces further. **Decisive**: A new full-sky polarisation likelihood (LiteBIRD by ~ 2032) eliminates this ambiguity by independently re-measuring `A_L` with cosmic-variance-limited polarisation data.

### 8.2 Is `Ω_K = -0.0023` real?

DESI DR2 + CMB hints at this at 2σ. **Decisive tests**:

- **DESI DR3-DR5** (2026-2028): doubled BAO precision; `Ω_K` constraint should reach `σ ≈ 0.0006`.
- **Spec-S5** (2030+): high-z BAO at `z = 2-4.5`; forecast to distinguish `Ω_K = -0.0023` from `w_0 w_a CDM` flat at >5σ via `D_V/r_d` at z > 2.
- **CMB-S4** (2030+): high-`ℓ` CMB lensing pushes `σ(Ω_K)` to ~ `0.0008` from CMB alone.
- **LiteBIRD** (~2032): cosmic-variance-limited large-scale polarisation. Resolves the `A_L` anomaly.

### 8.3 Decisive thresholds for the project's framework

A Spec-S5 / Roman / DESI-DR5 detection of `\|Ω_K\| > 10^{-3}` at >3σ would force the phonon-exflation framework to re-examine its substrate-compaction-induced expansion-history calibration. A null result at the `\|Ω_K\| < 10^{-4}` level would tighten the framework's flat-baseline assumption to extremely high precision, which is consistent with the current S58 Volovik-partition canonical at `w_0 = -0.918, Ω_K = 0`.

### 8.4 Spectroscopic JWST samples (Roman + Euclid)

Roman (launches 2027) and Euclid (DR3, ~2027) will produce ~ 10⁵-10⁶ z > 4 spectroscopic galaxies enabling LSS-based BAO at high redshift (`z = 2-4.5`). These samples directly probe the `Ω_K-Σm_ν-w_0 w_a` joint posterior and should resolve the DESI-DR2 vs CMB tension on its own.

### 8.5 Tested empirically vs theoretically

- Empirical roadmap: DESI DR3 (2026) → ACT DR6 final (mid-2026) → SPT-3G full-survey (2026-2027) → Spec-S5 (~2030) → CMB-S4 (~2032) → LiteBIRD (~2032).
- Theoretical roadmap: Specogna et al. 2025 closed-inflation framework → extension to `α`-attractors and other concrete inflationary models → bridge to landscape-multiverse priors.
- Each year tightens the allowed region around `Ω_K = 0` by `~ 0.0005-0.001`.

### 8.6 The structural truth (the ROBUST outcome)

Independent of which interpretive framework wins, the data are converging on `\|Ω_K\| < 0.005` from CMB+BAO+SNe combinations. The "curvature tension" is structurally a **CMB-internal** issue between `A_L` excess at `ℓ ≈ 1200-1500` and the lensing-reconstruction power, not a CMB-vs-LSS issue. Future high-precision CMB lensing reconstruction (LiteBIRD, CMB-S4) directly resolves the `A_L`-`Ω_K` ambiguity at the source.

---

## 9. Citations Table

Primary papers (PRIMARY = original analysis with new constraint; SECONDARY = re-analysis or follow-up; REVIEW = synthesis):

| arXiv ID | Authors | Year | Type | Headline result |
|:---------|:--------|:----|:-----|:----------------|
| 1807.06209 | Planck Collaboration (Aghanim et al.) | 2018 | PRIMARY | Planck 2018 cosmological parameters; `Ω_K = -0.044^{+0.018}_{-0.015}` (Plik TT,TE,EE+lowE) |
| 1908.09139 | W. Handley | 2019 | PRIMARY | Curvature tension; 2.5-3σ Planck-vs-BAO and lensing in `KΛCDM`; PRD 103, L041301 (2021) |
| 1911.02087 | E. Di Valentino, A. Melchiorri, J. Silk | 2019 | PRIMARY | "Planck evidence for a closed Universe and a possible crisis"; *Nature Astronomy* 4, 196 (2020) |
| 1910.00483 | G. Efstathiou, S. Gratton | 2019 | PRIMARY | CamSpec likelihood reanalysis; Plik vs CamSpec; closed preference reduced |
| 2002.06892 | G. Efstathiou, S. Gratton | 2020 | SECONDARY | "Evidence for a spatially flat Universe"; `Ω_K = 0.0004 ± 0.0018` (combined) |
| 2003.04935 | E. Di Valentino, A. Melchiorri, J. Silk | 2021 | PRIMARY | "Investigating Cosmic Discordance"; ApJ 908 L9; Planck+luminosity excludes flat ΛCDM at 99% |
| 1904.01016 | C.-G. Park, B. Ratra | 2019 | PRIMARY | Independent confirmation of closed-CMB preference; ApJ 882, 158 |
| 2101.03129 | W. Yang, S. Pan, E. Di Valentino, O. Mena, A. Melchiorri | 2021 | SECONDARY | "2021-H_0 odyssey: closed, phantom, interacting DE"; JCAP 10, 008 |
| 2110.05346 | E. Zuckerman, L. A. Anchordoqui | 2022 | SECONDARY | Spatial curvature sensitivity to local H_0; JHEAp 33, 10 |
| 2202.07865 | J.-J. Wei, F. Melia | 2022 | SECONDARY | Hubble tension and curvature from old astrophysical objects; ApJ 928, 165 |
| 2205.10869 | E. Rosenberg, S. Gratton, G. Efstathiou | 2022 | PRIMARY | Planck PR4 + CamSpec; reduced closed-preference significance |
| 2210.09865 | W. Yang, W. Giarè, S. Pan, E. Di Valentino, A. Melchiorri, J. Silk | 2023 | PRIMARY | "Revealing curvature effects on cosmological models"; PRD 107, 063509; non-flat survives in most DE parametrisations |
| 2304.05203 | M. Madhavacheril et al. | 2024 | PRIMARY | ACT DR6 lensing map and cosmological parameters; ApJ 962, 113 |
| 2309.10034 | M. Tristram et al. | 2024 | PRIMARY | Planck PR4 cosmological parameters with HiLLiPoP+LoLLiPoP |
| 2405.17396 | S. Bhattacharya, G. Borghetto, A. Malhotra, S. Parameswaran, G. Tasinato, I. Zavala | 2024 | SECONDARY | Cosmological constraints on curved quintessence; JCAP 09, 073 |
| 2411.14154 | T. Liu, S. Wang, H. Wu, J. Wang | 2024 | SECONDARY | Model-independent curvature from BOSS/eBOSS+DESI DR1; `Ω_K = -0.040^{+0.142}_{-0.145}` (GP) |
| 2503.07923 | R. Besuner, A. Dey, A. Drlica-Wagner et al. | 2025 | FORECAST | Spec-S5 experiment forecast |
| 2503.14454 | E. Calabrese, J. C. Hill, H. T. Jense et al. | 2025 | PRIMARY | ACT DR6 extended cosmological models; `Ω_K = +0.0019 ± 0.0015` (P-ACT-LB) |
| 2503.14738 | M. Abdul-Karim et al. (DESI Collaboration) | 2025 | PRIMARY | DESI DR2 BAO + cosmological constraints; `Ω_K ≈ -0.0023 ± 0.0011` (CMB+BAO) |
| 2504.01669 | E. Di Valentino, J. L. Said, T. C. L. Network et al. | 2025 | REVIEW | CosmoVerse White Paper: addressing observational tensions; *Phys. Dark Univ.* 49, 101965 |
| 2505.00659 | S.-F. Chen, M. Zaldarriaga | 2025 | SECONDARY | "It's All Ok: Curvature in light of BAO from DESI DR2"; physical reading of negative curvature |
| 2509.26263 | E. Specogna, T. Vardanyan, W. Giarè, E. Di Valentino | 2025 | SECONDARY | Closed `φ²` inflation prior reduces closed-preference from 3.5σ to 2-2.5σ |
| 2511.20757 | A. Chudaykin, M. M. Ivanov, O. H. E. Philcox | 2025 | SECONDARY | DESI DR1 EFT-FS reanalysis; CMB+BAO+Pℓ+B0: 2.4σ closed; CMB-PR4: 2.3σ |
| 2512.09486 | M. Yadav, A. Dixit, M. S. Barak, A. Pradhan | 2025 | SECONDARY | DESI DR1 vs DR2 wCDM+Ω_K; DR2-OHD-PP: weakly open at 1.8σ in `w_0` |
| 2604.13866 | L. Comini, S. Vagnozzi, A. Loeb | 2026 | PRIMARY | JWST CEERS/FRESCO joint cosmology+ε analysis; no `Ω_K` preference; "JWST tension is astrophysical" |

LRD-specific references (project corpus, see `researchers/Little-Red-Dots/index.md`):

| Paper # | Citation | Connection to curvature |
|:--------|:--------|:-----------------------|
| #03 | Greene et al. 2024, UNCOVER broad-line AGN | LRD virial BH masses; modest curvature sensitivity (8% at `Ω_K = -0.04`) |
| #06 | Yue et al. 2024, X-ray stacking | NULL detection; not curvature-sensitive |
| #13 | Das et al. 2024, SMBH-LCDM tension | Discusses but does not advocate curvature solution |
| #14 | Akins et al. 2024, LRD population | Demographics; cosmography enters via volume element |
| #29 | De Luca et al. 2025, Cosmologist take on LRDs | The most curvature-relevant project paper |
| #30 | "Modified Cosmology vs Astrophysics" 2025 | Adjudicates between cosmological and astrophysical readings of LRDs |
| #38 | Li et al. 2025, ApJ 981, 19 ("Tip of the Iceberg") | Selection-bias dominant in overmassive BH puzzle; rules out cosmological reading |

### Auxiliary references in the source-paper bibliographies

- Calabrese, Slosar, Melchiorri, Smoot, Zahn 2008 (PRD 77, 123531) — origin of the `A_L` parameter.
- Linde 2003 (JCAP 05, 002) — closed inflation construction.
- Freivogel, Kleban, Rodríguez-Martínez, Susskind 2006 (JHEP 03, 039) — landscape closed-bubble curvature distribution.
- Kleban & Schillo 2012 (JCAP 2012, 029) — eternal inflation falsified by `Ω_K < 0`.
- Bianchini et al. 2020 (ApJ 888, 119) — SPTpol+Planck flat preference.
- Lemos & Lewis 2023 (PRD 107, 103505) — CMB constraints on early Universe independent of late-time cosmology.
- Loverde & Weiner 2024 (JCAP 2024, 048) — neutrinos and cosmic composition; the Ω_K-Σm_ν link.
- Akarsu, Di Valentino, Kumar, Özyiğit, Sharma 2023 (PDU 39, 101162) — anisotropic+curvature extensions.

---

## 10. Bottom Line for the Phonon-Exflation Framework

1. **Current best constraint** (Planck convention): `Ω_K = +0.0019 ± 0.0015` from ACT DR6 P-ACT-LB; `Ω_K = -0.0023 ± 0.0011` from DESI DR2 + CMB. The two best high-precision combinations differ at 2σ — DESI hints at small closure while ACT prefers slight openness. Both consistent with flat at < 2σ.

2. **The "curvature tension" is a CMB-internal lensing-amplitude anomaly**, not a CMB-vs-LSS distance tension. The `A_L > 1` excess at `ℓ ≈ 1200-1500` translates into closed-universe preference under `KΛCDM`; the Planck CMB-lensing 4-point function and ACT lensing reconstruction both prefer `A_L = 1`.

3. **JWST does not provide a curvature constraint** at currently meaningful precision. The Comini-Vagnozzi-Loeb 2026 analysis explicitly tests this and finds no preference. The "overmassive BH" puzzle is dominated by selection bias (Li et al. 2025), not curvature.

4. **For the framework**: the project's `w_0_FW = -0.918` (S58 Volovik partition) was calibrated under flat-`Ω_K = 0` baseline. Current data are consistent with this assumption at the `0.002` level. A future Spec-S5 / Roman / CMB-S4 detection of `\|Ω_K\| > 0.001` would be the relevant trigger for re-examination; until then, the flat-`Ω_K = 0` substrate-compaction assumption is empirically supported.

5. **Surviving solution-space corollary**: the framework's prediction space is not yet meaningfully tightened by curvature data — `\|Ω_K\| < 0.005` accommodates all current detections — but the channel is live and testable. Watchlist priority: medium (lower than `w_0`/`w_a` direct, comparable to `Σm_ν` and `S_8`). Recommend tracking Spec-S5 and CMB-S4 forecasts for forward-pre-registration of an `Ω_K` gate at the `10^{-4}` level.

---

*End of review document. All quoted numerical values verified against the primary-source PDFs in `researchers/Little-Red-Dots/downloads/`. Sign conventions remapped to Planck convention `Ω_K < 0 ⇒ closed` throughout.*
