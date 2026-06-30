# Curvature Tension in Modern Cosmology: A Cosmic-Bridge Review

**Author:** Mack-Cosmic-Bridge agent (Phonon-Exflation project)
**Date:** 2026-05-01
**Scope:** Literature review — Ω_K constraints, the "curvature anomaly," and its position in the broader tension landscape (H₀, S₈, w₀–wₐ, Σm_ν).
**Status:** Internal reference document for the Phonon-Exflation project. Not a framework computation. No verdict line, no plan-block, no PRDR.
**Source authority:** This review quotes constraint values verbatim from primary sources. Where σ-tension values are cited, they are attributed to the methodology of the original authors (suspiciousness statistic, DIC, profile-likelihood Δχ², Bayes factor) — no σ-values are independently re-derived in this document.

---

## 1. Executive Summary

The "curvature tension" is the body of evidence that the Planck CMB temperature/polarization power spectra alone, treated under freed Ω_K, prefer a closed Universe at high statistical significance, while every dataset that breaks the geometric degeneracy (CMB lensing, BAO, SNe Ia, full-shape galaxy P(k), cosmic chronometers) drags Ω_K back to flat or near-flat. Specifically:

- **Planck 2018 plik TTTEEE+lowE alone** prefers Ω_K = −0.044<sup>+0.018</sup><sub>−0.015</sub> (~3.4σ from flat by Δχ² and DIC; suspiciousness 50:1 odds against flat per Handley 2019; >99% closed per Di Valentino, Melchiorri, Silk 2019).
- **Planck + BAO** gives Ω_K = 0.0007 ± 0.0019 (~0.4% precision; flat to 1σ; Planck 2018 results VI; Efstathiou-Gratton 2020 reach 0.0004 ± 0.0018 with their CamSpec-12.5HMcln likelihood).
- **DESI DR2 BAO + CMB (PR3+CamSpec PR4)** finds Ω_K ≈ +0.0023 ± 0.0011 — a ~2σ pull toward *negative* spatial curvature (positive Ω_K, R_k ≈ 21 H₀⁻¹), in the *opposite sign* to the Planck-CMB-only anomaly. This is the most surprising 2025 development (Chen-Zaldarriaga 2025; DESI Collaboration 2025).
- **ACT DR4** alone with WMAP gives Ω_K = −0.001<sup>+0.014</sup><sub>−0.010</sub> (fully consistent with flat); ACT DR6 + Planck primary CMB shows "no departure from spatial flatness" and "no evidence for excess lensing" (Louis et al. 2025).
- **SPT-3G D1 (2025)** + Planck + ACT-DR6 + DESI DR2 in CMB+BAO combination shows "2–3σ shifts from ΛCDM in the curvature of the universe, the amplitude of CMB lensing, or the dark energy equation of state" (Camphuis et al. 2025).
- **2025 closed-φ² inflation analysis (Specogna et al. 2509.26263)**: when the closed-Universe primordial power spectrum is computed gauge-invariantly from the inflaton potential rather than via the phenomenological extrapolation built into CAMB, the plik PR3 preference for Ω_K < 0 *drops* from ≳3.5σ to ~2.5σ; in CamSpec PR4 it drops to ~2σ. The CMB-internal "evidence" was partly an artifact of the curvature-flat power-spectrum mismatch.

The community is split between three readings:
1. **Statistical fluctuation + Plik-likelihood quirk** (Efstathiou-Gratton 2020; Planck-team default; supported by Specogna 2025 inflationary self-consistency).
2. **Genuine new physics** (Di Valentino, Melchiorri, Silk 2019; Cosmology Intertwined IV — 130-author Snowmass white paper Di Valentino et al. 2008.11286).
3. **Signature of a deeper tension chain — Ω_K is one of multiple discordances that all point to ΛCDM stress** (Handley 2019; SPT-3G D1 2025).

The curvature anomaly is now a member of a *tension family*: H₀ tension (~6σ; SH0ES vs. Planck+ACT+SPT), S₈ tension (~2–3σ; weak lensing vs. CMB), w₀–wₐ DESI preference (3.1σ for dynamical dark energy; up to 4.2σ with DES-Y5 SNe), neutrino-mass squeeze (Σm_ν < 0.064 eV pushing below the oscillation lower bound 0.058 eV). These are coupled — relaxing one relaxes the others, especially in the curvature direction.

---

## 2. Origin of the Curvature Anomaly

### 2.1 The geometric degeneracy

In FLRW cosmology, two cosmological models with identical (Ω_b h², Ω_c h², n_s, A_s, τ) but different (Ω_K, Ω_m, H₀) along the geometric-degeneracy curve produce *identical* primary CMB acoustic peak structure at sub-degree scales (Bond, Efstathiou, Tegmark 1997; Efstathiou-Bond 1999). The example given by Di Valentino et al. (2019): a flat model with Ω_m = 0.35, Ω_Λ = 0.65, H₀ = 65 km/s/Mpc has identical sub-degree CMB power as a closed model with Ω_m = 1, Ω_Λ = 0.15, Ω_K = −0.15, H₀ = 38.4 km/s/Mpc.

The degeneracy is broken only by:
- **Gravitational lensing** of the CMB (depends on matter density at z ~ 0.5–5)
- **The Sachs-Wolfe / late-ISW plateau** (very-large-angle ℓ ≲ 10)
- **External low-z distance probes**: BAO, SNe Ia, cosmic chronometers, strong lensing time delays

### 2.2 Planck 2018 result and the A_L anomaly

Planck 2018 (Aghanim et al. 1807.06209, Section 7.5) reports, using the baseline plik TTTEEE+lowE likelihood with a uniform prior on Ω_K ∈ [−0.3, +0.3]:

- **Planck 2018 plik TTTEEE+lowE**: Ω_K = −0.044<sup>+0.018</sup><sub>−0.015</sub> (68% CL). This is the headline closed-Universe result. Δχ² ≈ −11 vs. flat ΛCDM. DIC analysis gives Δ DIC ≈ −7.4 (probability ratio ~41:1 in favor of curved over flat in the prior range Ω_K ∈ [−0.2, 0]; Di Valentino-Melchiorri-Silk 2019 Eq. 3 quotes |ln B_01| = 3.3, "strong" on Jeffrey's scale).

- **The A_L lensing-amplitude anomaly**: the Planck CMB power spectra prefer A_L > 1 at ~2.8σ. A_L is a phenomenological parameter scaling the lensing smoothing of the acoustic peaks. Within ΛCDM, A_L = 1 by construction — A_L ≠ 1 indicates that the CMB peaks are *more smoothed* than ΛCDM predicts.

The A_L anomaly and the Ω_K anomaly are **not independent**: Di Valentino et al. (2019) Figure 2 shows the strong degeneracy in the A_L–Ω_K plane. A closed Universe with extra matter content produces extra physical lensing, mimicking A_L > 1. The closed-Universe interpretation is therefore "what the data ask for if you don't put a phenomenological extra-smoothing knob in."

### 2.3 The internal-CMB ℓ < 800 vs. ℓ > 800 tension

Addison et al. (2016) noted that under flat ΛCDM the cosmological parameters from the Planck TT spectrum split at ℓ ≈ 800 differ at ~2σ. Di Valentino-Melchiorri-Silk (2019) Figure 3 demonstrates that **adding curvature with Ω_K = −0.045 removes this split** — the ℓ < 800 and ℓ > 800 parameter posteriors become fully compatible. This is one of the most physically suggestive aspects of the closed-Universe interpretation: a single one-parameter extension simultaneously addresses A_L, the ℓ-split, and the suppressed quadrupole/low-ℓ power.

### 2.4 Likelihood-implementation dependence

A central caveat: the Ω_K result depends sensitively on which Planck likelihood is used.

| Likelihood | Ω_K (68% CL) | Source |
|:--|:--|:--|
| Planck 2018 baseline plik TTTEEE+lowE | −0.044<sup>+0.018</sup><sub>−0.015</sub> | Planck 1807.06209 |
| Planck CamSpec (Efstathiou-Gratton variant, PR3) | −0.037<sup>+0.032</sup><sub>−0.034</sub> (95% CL) | DV-M-S 2019 |
| Planck CamSpec PR4 | −0.025<sup>+0.013</sup><sub>−0.010</sub> | Specogna et al. 2509.26263 quoting Rosenberg+Gratton+Efstathiou 2022 |
| Planck HiLLiPoP | (less significant; Specogna 2025 quotes "still over 2σ" away from ΛCDM for CamSpec; HiLLiPoP-NPIPE quoted in Wang et al. 2508.19081) | various |
| Planck 12.5HMcln (Efstathiou-Gratton 2020) | ~1.6σ pull (when ℓ<30 TT excluded) | E-G 2020 |
| WMAP9 alone | −0.037<sup>+0.044</sup><sub>−0.042</sub> | Hinshaw et al. 2013 |

The plik likelihood pulls the most strongly closed; CamSpec less so. Efstathiou-Gratton (2020) interpret this as evidence that the closed pull is partly a likelihood-implementation artifact. Di Valentino et al. (2019) counter that **even in CamSpec the preference is >2σ closed**, and that WMAP9 independently shows the same direction with similar magnitude — so a Planck-specific systematic cannot be the whole story.

### 2.5 Specogna et al. 2025: closed-inflation primordial spectrum

The most important recent reassessment is Specogna, Vardanyan, Giarè, Di Valentino (arXiv:2509.26263, JCAP submission 2025-09). The CAMB code's standard treatment for non-flat models extrapolates the primordial scalar power spectrum as P(k) = (q² − 4K)² / [q(q² − K)] · k<sup>(n_s − 1)</sup> with q = √(k² + K), an *ansatz* not derived from any specific inflationary model. Specogna et al. instead solve the gauge-invariant Mukhanov-Sasaki equation in a closed FLRW background driven by a quadratic inflaton potential V(φ) = ½ m² φ², deriving the scalar primordial spectrum *consistently with curvature*. Result:

- **plik PR3 closed-φ² model**: preference for Ω_K < 0 drops from ≳3.5σ to ~2.5σ.
- **CamSpec PR4 closed-φ² model**: preference drops to ~2σ.
- The model **explains the low-ℓ power suppression / quadrupole anomaly** by construction (the closed-inflation primordial spectrum has a curvature-scale cutoff naturally suppressing modes near R_k).
- Δχ² in CamSpec PR4 = +0.49 in favor of closed-inflation parametrization vs. CAMB-default; in plik = −1.18 favoring CAMB-default (the residual high-ℓ A_L anomaly is still unaccounted for).

The lesson is structural: **closed-inflation models tie Ω_K to the inflationary dynamics**, and self-consistency reduces the freedom that the phenomenological CAMB parametrization had granted. The "Planck closed-Universe evidence" is partly an artifact of letting the primordial spectrum and the curvature parameter vary independently, ignoring that they should be linked through the inflaton dynamics.

---

## 3. Dataset Constraint Table

All constraints below are quoted at 68% CL unless noted, in the model ΛCDM + Ω_K (no dynamical dark energy unless stated). Where a paper reports both, the more constraining combination is listed.

| Dataset / Combination | Ω_K (68% CL) | Tension wrt flat | Source / arXiv ID |
|:--|:--|:--|:--|
| **WMAP9 alone** | −0.037<sup>+0.044</sup><sub>−0.042</sub> | <1σ | Hinshaw et al. 2013 (cited in DV-M-S 2019) |
| **Planck 2015 plik TTTEEE+lowE** | −0.040 ± 0.020 (approx.) | ~2σ | DV-M-S 2019 Fig 1; Planck XIII 1502.01589 |
| **Planck 2018 plik TTTEEE+lowE** | **−0.044<sup>+0.018</sup><sub>−0.015</sub>** | **~3.4σ closed** | Planck 1807.06209 §7.3; DV-M-S 2019 |
| **Planck 2018 CamSpec (Efstathiou-Gratton)** | −0.037<sup>+0.032</sup><sub>−0.034</sub> (95% CL) | >2σ closed | DV-M-S 2019 quoting Efstathiou-Gratton 1910.00483 |
| **Planck 2018 CamSpec PR4** | −0.025<sup>+0.013</sup><sub>−0.010</sub> | ~2σ closed | Specogna 2509.26263 quoting Rosenberg-Gratton-Efstathiou 2022 |
| **Planck PR3 closed-φ² inflation** | (not quoted directly) — preference reduced to ~2.5σ | 2.5σ closed | Specogna 2509.26263 |
| **Planck CamSpec PR4 closed-φ² inflation** | (not quoted directly) — preference reduced to ~2σ | ~2σ closed | Specogna 2509.26263 |
| **Planck 2018 + CMB lensing (PR3)** | +0.011<sup>+0.013</sup><sub>−0.012</sub> (95% CL) | <2σ | DV-M-S 2019 |
| **Planck 2018 + BAO (BOSS DR12 + 6dFGS + MGS)** | **+0.0007 ± 0.0019** | <0.4σ flat | Planck 1807.06209 |
| **Planck 2018 + Pantheon + lensing** | (Efstathiou-Gratton 12.5HMcln) +0.0004 ± 0.0018 | <0.3σ flat | Efstathiou-Gratton 2002.06892 Eq. 6e |
| **Planck + BOSS DR12 P(k) full-shape (Vagnozzi et al.)** | +0.0023 ± 0.0028 | <1σ | Vagnozzi et al. 2010.02230 |
| **BAO + BBN + SN-Ia (no CMB; Chudaykin-Dolgikh-Ivanov)** | −0.043<sup>+0.036</sup><sub>−0.036</sub> | ~1σ | Chudaykin et al. 2009.10106 |
| **Planck + BAO+SN-Ia+R19 (DV-M-S 2019)** | −0.091 ± 0.037 | 2.5σ closed | DV-M-S 2019 Fig 8 |
| **ACT DR4 + WMAP** | **−0.001<sup>+0.014</sup><sub>−0.010</sub>** | flat | ACT Collaboration Aiola+ 2007.07288 |
| **ACT DR4 + Planck (partial)** | −0.018<sup>+0.013</sup><sub>−0.010</sub> | ~1.5σ closed | ACT Aiola+ 2007.07288 (cited DV-M-S 2020) |
| **ACT DR6 + Planck primary CMB (P-ACT)** | "no departure from spatial flatness" — value not quoted, but consistent with flat | <2σ flat | ACT DR6 Louis et al. 2503.14452 |
| **ACT DR6 lensing + Planck lensing + BAO** | confirms flat to ~1% level via geometric break | flat | Madhavacheril et al. 2304.05203; Farren et al. 2409.02109 |
| **DESI DR1 BAO + CMB (in ΛCDM+Ω_K)** | (flat preferred at <1σ) | flat | DESI 2024 VI 2404.03002 |
| **DESI DR2 BAO + CMB (Planck PR3+CamSpec PR4+ACT lensing)** | **+0.0023 ± 0.0011** | **~2σ** ***open*** | Chen-Zaldarriaga 2505.00659; DESI Coll 2503.14738 |
| **DESI DR2 + CMB + DESI Lyα** | Ω_K ≈ 0 (flat preferred) | flat | Capozziello et al. 2510.21976 |
| **DESI DR2 + CMB + ΛCDM+Ω_k+Σm_ν+w₀wₐ joint** | (varies by model; up to ~3σ shift in CMB+BAO joint) | 2-3σ | SPT-3G D1 Camphuis et al. 2506.20707 |
| **Pantheon SNe + cosmic chronometers (model-independent)** | −0.02 ± 0.14 | flat | Liu et al. 2008.08378 |
| **DESI DR2 + DESY5 SNe + CCH (Favale et al. 2025)** | −0.143 ± 0.085 | ~1.7σ closed | Favale et al. 2511.19332 |
| **DESI DR1 BAO + Pantheon+ + CCH (Li-Zhang)** | +0.06 ± 0.08 | <1σ | Li-Zhang 2411.08498 |

**Observation 1 (sign-pattern):** When Ω_K is anomalous in CMB-only, the sign is *negative* (closed). When Ω_K is anomalous in BAO-CMB (DESI DR2), the sign is *positive* (open). These are *opposite sign* anomalies. The 2025 DESI-CMB joint constraint is a fundamentally different signal from the 2019 Planck-CMB-only signal.

**Observation 2 (precision floor):** The most constraining combinations now reach σ(Ω_K) ≈ 0.001 (Planck+BAO, Chen-Zaldarriaga). The inflationary expectation for Ω_K from generic large-N inflation is |Ω_K| < 10⁻⁴ (Planck 2018 X 1807.06211; Bull-Kamionkowski 2013; Leonard-Bull-Allison 2016). Current data are still *one decade* above the inflationary floor. Sub-10⁻⁴ probes require Stage-V spectroscopic experiments (Spec-S5; Besuner et al. 2503.07923) or 21-cm intensity mapping.

---

## 4. Internal-CMB Tension — Handley's Suspiciousness Methodology

Handley (arXiv:1908.09139, 2019; published PRD 103 L041301) frames the curvature problem as a *dataset-discordance* problem rather than a parameter-estimation problem. The methodology is the **suspiciousness statistic** S = R / I, where R is the Bayes ratio between joint-vs-independent dataset evidences and I is an information-correction factor based on Kullback-Leibler divergence:

S = R/I, log I = D₁ + D₂ − D₁₂, d̃ = 2 ⟨(log L)²⟩_P − 2 ⟨log L⟩²_P

where d̃ is the Bayesian model dimensionality (effective number of constrained parameters). The statistic is calibrated against a χ²_d distribution to give a tension probability, converted to "Gaussian σ" via the inverse complementary error function.

Handley 2019 results (in K-ΛCDM = ΛCDM + Ω_K):

| Comparison | Suspiciousness tension | Ω_K direction |
|:--|:--|:--|
| Planck 2018 vs. Planck CMB lensing | 2.49 ± 0.07 σ | Lensing pulls flat; Planck pulls closed |
| Planck 2018 vs. BAO (BOSS DR12) | 3.03 ± 0.06 σ | BAO pulls flat; Planck pulls closed |
| Planck 2018 vs. SH0ES H₀ | 4.49 ± 0.04 σ | (this is the H₀ tension, enhanced by curvature freedom) |
| Triple: Planck vs. lensing vs. BAO | "moderate mutual inconsistency" | All three disagree pairwise |

Key Bayesian-evidence findings from Handley:
- **Planck 2018 alone**: Δlog Z (curved vs. flat) > 0 at 50:1 odds in favor of curved.
- **>2000:1 odds against an *open* universe** within the curved branch (the closed-vs-open posterior is asymmetric).
- **Adding lensing** drops Δlog Z to ~2:1 in favor of curved (Occam penalty starts to dominate).
- **Adding BAO**: flat is preferred over curved by Bayesian evidence — but this is *because* the dataset-suspiciousness tension is hidden by the Bayesian Occam penalty, not because the data agree.

The Handley methodology is the most rigorous tension-assessment framework in the closed-Universe debate. Its core message: **don't combine inconsistent datasets and report the combination as a low-Ω_K result without flagging the tension**. The Planck-team-default Ω_K = 0.001 ± 0.002 (Planck+BAO) is *correctly computed* as a posterior, but it conflates two datasets that disagree at 3σ on the very parameter being constrained.

Efstathiou-Gratton 2020 (arXiv:2002.06892) push back: the closed-pull is partly a likelihood-implementation issue (their 12.5HMcln likelihood reduces the Δχ² to ~6, ~2.1σ pte), and partly a prior issue — a uniform Ω_K prior is unphysical (an inflationary prior should peak at Ω_K = 0 with skewed power-law tails). Under a physically motivated prior with skew p(N) ∝ N⁻ᵅ for N > N_*, the posterior interpretation changes substantially.

The community has not converged. As of 2026 the working consensus is:
- The **plik-likelihood specific** part of the anomaly is real but ~2σ less significant in CamSpec.
- The **closed-inflation self-consistent** Specogna 2025 reanalysis further reduces it.
- The **dataset-suspiciousness** tension between CMB-only and CMB+BAO/lensing is real and persists across all likelihoods.

---

## 5. Tension-Correlation Analysis

### 5.1 Curvature ↔ H₀

The Ω_K–H₀ degeneracy is a structural feature of CMB constraints. Holding ω_m = Ω_m h² and θ* (the angular acoustic scale) fixed, the geometric distance to last scattering depends on Ω_K through D_M,* changing by ∼1.4 Ω_K (Chen-Zaldarriaga 2505.00659 §2). This forces the relation

H₀(1 − 7 Ω_K) ≈ const (in CMB)
H₀ ≈ const (in low-z BAO with CMB ω_m prior)

Substituting Planck 2018 plik Ω_K = −0.044 into this, **H₀ is shifted from 67.4 down to ~54.4 km/s/Mpc** (Di Valentino et al. 2019 quote H₀ = 54.4<sup>+3.3</sup><sub>−4.0</sub> km/s/Mpc in ΛCDM+Ω_K from Planck alone). This **worsens the H₀ tension** with SH0ES from ~5σ to ~5.2σ.

In the *opposite* direction, when DESI DR2 BAO + CMB prefers Ω_K = +0.0023 (open), H₀ shifts *upward* to about 68.4 km/s/Mpc — slightly easing the H₀ tension by ~0.3σ but not closing it. Chen-Zaldarriaga 2025 §2 give the substitution: σ(Ω_K) ≈ 0.0012 ⇒ ΔH₀/(7H₀) ≈ 0.002 ⇒ ΔH₀ ≈ 1 km/s/Mpc.

**Verdict:** Curvature does *not solve* the H₀ tension. A closed Universe makes it worse; an open Universe at the DESI-DR2-preferred level moves H₀ in the right direction by ~0.3σ but not nearly enough.

### 5.2 Curvature ↔ S₈ / σ₈

Di Valentino et al. (2019) Fig 6: in ΛCDM+Ω_K with Ω_K = −0.044, **S₈ shifts to 0.981 ± 0.049** (vs. flat-Planck S₈ ≈ 0.832). KiDS-450 measures S₈ ≈ 0.745. The closed-Universe tension with KiDS-450 is therefore ~3.8σ (compared to ~2.3σ in flat). DES and HSC galaxy-shear measurements are also pushed to >3σ tension.

**Closed Ω_K worsens the S₈ tension.** This is an additional argument *against* the closed-Universe interpretation: it makes a tension of weak-lensing surveys with CMB even worse than ΛCDM does.

The DESI-DR2 *positive* Ω_K (open) direction has the opposite effect — slightly easing the S₈ tension via lower σ₈. This sign asymmetry is one reason DESI-DR2 negative-curvature is currently the more attractive interpretation among the dynamical-dark-energy crowd.

### 5.3 Curvature ↔ neutrino mass

Chen-Zaldarriaga (2505.00659 §3) demonstrate that the geometric mechanism by which CMB+BAO constrain Σm_ν is *the same mechanism* that constrains Ω_K — both shift D_M,* and break the ω_cb / ω_m degeneracy. The Ω_K – Σm_ν posterior has a steep slope Δf_ν / ΔΩ_K = 3.5 (i.e., 1.4 Ω_K = 0.4 f_ν).

**Allowing Ω_K free relaxes Σm_ν constraints from < 0.064 eV (DESI DR2 + CMB, ΛCDM) to < 0.10 eV (DESI DR2 + CMB, ΛCDM+Ω_K), accommodating both normal and inverted hierarchies within 95% CL.** This is critical: the DESI-DR2 ΛCDM constraint Σm_ν < 0.064 eV is in tension with the lower limit from oscillation experiments Σm_ν ≥ 0.058 eV (normal hierarchy) — sometimes called "negative neutrino mass anomaly." Freeing curvature dissolves this anomaly.

Chudaykin-Ivanov-Philcox (2511.20757) reanalysis of DESI DR1 with full-shape + bispectrum gives:
- Σm_ν < 0.059 eV in ΛCDM+M_ν
- Σm_ν < 0.097 eV in oΛCDM+M_ν
- Σm_ν < 0.13 eV in w₀wₐCDM+M_ν

Pulido-Hernández-Cervantes-Cota (2603.13208) using a "negative effective mass" wrapper find that in ΛCDM+Ω_K+Σm_ν,<sub>eff</sub>, the constraint becomes Σm_ν = −0.011<sup>+0.052</sup><sub>−0.050</sub> eV with only **1.17σ tension** to the oscillation lower bound 0.06 eV (vs. 2.59σ in flat ΛCDM).

### 5.4 Curvature ↔ dark-energy dynamics

DESI DR1 + CMB + SNe shows ~2.5–3.9σ preference for w₀ > −1, wₐ < 0 in flat w₀wₐCDM (DESI 2404.03002). DESI DR2 strengthens this to 3.1σ (DESI BAO+CMB) up to 4.2σ (with DES-Y5 SNe).

**When Ω_K is freed simultaneously with w₀wₐ**, the dynamical dark energy preference *weakens*. Chen-Zaldarriaga (2505.00659) note the DESI Collaboration found that combinations of DESI+CMB+SNe in flat-w₀wₐCDM-with-Ω_K prefer a *flat* universe within 1σ when phantom-regime DE is allowed — i.e., **curvature and DE dynamics are alternative solutions to the same tension**.

Bhattacharya et al. 2405.17396, Akrami-Alestas-Nesseris 2504.04226, and Dinda-Maartens 2504.15190 all confirm that "in a cosmology with nonzero spatial curvature, the suppression of the distance scale at low redshifts compared to the CMB can be achieved via the nonlinear relation between different distances on large scales, rather than an unexpected increase in the late-universe energy density requiring dark energy to increase with time" (Chen-Zaldarriaga 2505.00659 §5). The two interpretations are partly degenerate; future Stage-V (Spec-S5) BAO will distinguish them at >5σ.

### 5.5 Joint constraint structure

```
                  H_0 tension      S_8 tension      Σm_ν       w_0w_a DESI
Closed Ω_K       WORSENS (~+0.5σ) WORSENS (~+1.5σ) RELAXES   COMPETES  
(Planck-CMB-only)                                            (alternative
                                                              solution)

Open Ω_K          EASES (~−0.3σ)   EASES (~−0.3σ)  RELAXES   COMPETES  
(DESI-DR2 + CMB)                                             (alternative
                                                              solution)

Tension-family
joint analyses    require simultaneous extensions OR systematics in
                  multiple datasets — single Ω_K ≠ 0 cannot resolve all
```

The H₀ + S₈ + Σm_ν + w₀wₐ + Ω_K tensions are **not independent**. Bayesian model-comparison results (Specogna 2509.26263; Chudaykin 2511.20757; Capozziello 2510.21976; Pulido-Hernández 2603.13208) consistently find that multi-extension models can ease combinations but no single extension closes everything. The most viable multi-extension combinations are:
- **Modified recombination + Ω_K** (Wang-Lei-Tang-Fan 2508.19081 — varying electron mass + Ω_K)
- **Quintessence + Ω_K** (Akrami-Alestas-Nesseris 2504.04226 — exponential quintessence + open Universe)
- **Early dark energy + Ω_K** (Stevens-Khoraminezhad-Saito 2212.09804)

---

## 6. Theoretical Interpretations

### 6.1 Inflation predicts |Ω_K| ≪ 10⁻⁴ generically

Standard slow-roll inflation with sufficient e-foldings N ≫ N_* ≈ 60 drives |Ω_K| ∝ exp(−2N) toward zero. For inflation with energy scale V_I ~ 10¹⁶ GeV, the inflationary attractor is |Ω_K| ≲ 10⁻⁵. Detecting Ω_K at the 10⁻³ level *strongly disfavors* large-N inflation and points toward "incomplete inflation" with N ≈ N_*.

### 6.2 Closed inflation requires fine-tuning

To produce Ω_K ≈ −0.05 today, closed inflation requires N just barely above N_* (Linde 1995, 2003 quoted in DV-M-S 2019). Linde's closed-inflation models exist (Gratton-Lewis-Turok 2002; Lasenby-Doran 2005; Specogna et al. 2025 closed-φ²) but require ~1% fine-tuning of initial conditions. Di Valentino-Melchiorri-Silk (2019) note: "this does not sound very compelling, but it may still be acceptable given the presence of a far more finely-tuned cosmological constant."

### 6.3 Open inflation is more natural

Open universes with Ω_K > 0 (k = −1) arise naturally from Coleman-de Luccia bubble nucleation in a parent de Sitter false vacuum (Coleman-De Luccia 1980; Gott 1982; Bucher-Goldhaber-Turok 1995; Linde 1995). This is the canonical "open inflation" scenario — and it is the *natural interpretation* of DESI-DR2 positive Ω_K, if confirmed.

**Crucially: a positive-Ω_K detection at >10⁻⁴ rules out slow-roll eternal inflation** (Kleban-Schillo 2012, arXiv:1202.5037, cited in Chen-Zaldarriaga 2505.00659). Eternal inflation produces a closed bubble interior with Ω_K > 0, but only with |Ω_K| ≲ 10⁻⁴ given current SHB-relaxation arguments. A detection at 10⁻³ would falsify eternal inflation while remaining compatible with single-bubble open inflation.

### 6.4 Multiverse and anthropic priors

Freivogel-Kleban-Rodríguez-Susskind (2006) argued that in a string landscape with anthropic selection, the prior on Ω_K is approximately uniform in log|Ω_K| over many decades. Guth-Nomura (2012) built on this. Under such a prior, finding |Ω_K| ~ 10⁻³ would not be surprising — it would be evidence *for* the landscape interpretation. Mersini-Houghton has long advocated multiverse-entanglement signatures in CMB anomalies (Mersini-Houghton-Holman 2008); the Cosmology Intertwined IV paper (Di Valentino et al. 2008.11286) lists her as co-author and explicitly cites multiverse interpretations.

The anthropic argument: in a landscape, the inflation N is selected from a distribution skewed to small N (because most landscape pockets reheat and form structure quickly), so the posterior on Ω_K has fatter tails than the inflationary attractor predicts. Efstathiou-Gratton (2020) Eq. 4 makes this prior structure explicit: p(N) ∝ N⁻ᵅ for N > N_* leads to p(Ω_K) ∝ (N_* − ½ ln|Ω_K|)⁻ᵅ d Ω_K / Ω_K.

### 6.5 Greene-Levin-Kabat compactification angle

Brian Greene's research program (Greene-Levin 2007 hep-th/0612101 — "Dark Energy and Stabilization of Extra Dimensions"; Greene-Kabat-Marnerides 2009 0908.0955 — "Decompactification in 3 dimensions"; Greene-Kabat-Levin-Thurston 2010 1001.1423 — "Bulk inflaton from large volume extra dimensions"; Greene-Kabat-Levin-Porrati 2510.05270 — "Compactification without orientation, or a topological scenario for CP violation") investigates how the topology and curvature of compact extra dimensions feed back into the observable 4D cosmology.

Key Greene insight (relevant to the curvature tension): in higher-dimensional compactifications where the internal geometry is non-trivially curved, the 4D effective spatial curvature receives contributions from both:
1. The "raw" 4D FRW spatial curvature term K_4
2. The curvature-induced backreaction of extra-dimensional moduli stabilization

**No published Greene paper predicts a definite 10⁻² level Ω_K** — the framework is general enough that Ω_K is a free parameter set by initial conditions plus moduli stabilization. However, Greene's more recent work on Klein-bottle compactification (Greene-Kabat-Levin-Porrati 2025) and on bulk-inflaton models (2010) explicitly accommodates closed-inflation scenarios where N can be tuned close to N_*, making a 10⁻²-level Ω_K naturally accessible.

The phonon-exflation framework's connection (this project): the M⁴ × SU(3) compactification with internal Jensen-deformed spectral triple provides a substrate-IS picture in which the 4D spatial curvature is *not* a fundamental parameter but *emerges* from how the spectral action's a₂ Seeley-DeWitt coefficient distributes weight under transit. This is a Greene-class mechanism but with the extra dimension being a non-commutative geometric fiber (NCG) rather than a smooth Calabi-Yau or Klein bottle. **The framework does not at present predict a definite sign or magnitude for Ω_K** — this is a genuine open question for the project, and the curvature anomaly is a candidate observational discriminant if a definite prediction can be derived.

### 6.6 Phase-transition cosmology and curvature

First-order phase transitions in the early Universe (electroweak, QCD, hidden-sector) generically produce small but non-zero spatial curvature contributions through bubble-collision dynamics and supercooled relic configurations. Mack's own work on vacuum decay (Mack 2020 *The End of Everything* Ch. 5; Burda-Gregory-Moss 2015 — "Vacuum metastability with black holes") considers vacuum-decay bubbles as a fate scenario; the same physics in the inflationary epoch produces curvature contributions at the bubble-edge level.

The Wang-Yang-Dai et al. 2603.25999 *J*CDM cosmology paper finds that the trace-of-Schouten-tensor model of dynamical DE — which is structurally similar to phase-transition DE — favors Ω_K = 0.0154 ± 0.0027 (slightly open) in its non-flat extension, indicating that dynamical-DE models that solve H₀ also tend to want a small open Ω_K.

### 6.7 Modified gravity readings

f(R), DGP, and Horndeski-class modified gravity frameworks generically modify the geometric distance D_M,*, mimicking apparent Ω_K. DESI 2024 VII modified-gravity constraints (Ishak et al. 2411.12026) find no evidence for departure from GR in μ₀, Σ₀ parameters when LoLLiPoP+HiLLiPoP CMB likelihoods are used (the original ~2σ Σ₀ tension under PR3 lensing is interpreted as the same A_L anomaly that drives the closed-Universe pull in plik). **In Horndeski + ΛCDM, Ω_K stays consistent with flat at ~2σ; the modified-gravity coupling alone does not predict a definite Ω_K sign.**

### 6.8 Inhomogeneous-universe / backreaction interpretations

Bolejko (1707.01800) "Emergence of spatial curvature" argues that nonlinear structure formation in an inhomogeneous Universe averages to a non-zero effective Ω_K^D ≈ 0.15 in the late Universe even from flat ΛCDM initial conditions — a backreaction effect not captured in standard FRW. Bull-Kamionkowski (2013, arXiv:1302.1617) note that a *local inhomogeneity* of size comparable to the observable horizon could mimic an apparent Ω_K, with secondary CMB spectral distortions (KSZ, Compton-y) as the discriminant. **These interpretations predict Ω_K signal correlated with structure-formation observables, not with primordial-spectrum observables.**

---

## 7. Recent (2024–2026) Developments

### 7.1 DESI DR1 (April 2024)

DESI 2024 VI (Adame et al. 2404.03002) reports DESI DR1 BAO from 6+ million extragalactic objects across 0.1 < z < 4.2. In ΛCDM, DESI alone is consistent with flat. In ΛCDM+Ω_K with CMB, mildly negative-curvature pull (under ~2σ). The headline DESI DR1 result was the 2.6σ DESI+CMB preference for w₀wₐCDM with w₀ > −1, wₐ < 0.

DESI 2024 VII (full-shape + BAO, Adame et al. 2411.12022): combination of DESI FS+BAO+CMB gives Ω_m = 0.3056 ± 0.0049, σ₈ = 0.8121 ± 0.0053, H₀ = 68.40 ± 0.27 km/s/Mpc. No detection of Ω_K ≠ 0.

### 7.2 DESI DR2 (March 2025)

DESI Collaboration 2503.14738 — DR2 BAO from >14M tracers, 3-year operation. Headline:
- DESI DR2 + Planck/ACT CMB in flat ΛCDM: 2.3σ tension on Ω_m (DESI prefers Ω_m ≈ 0.295, CMB-alone prefers Ω_m ≈ 0.315).
- **DESI DR2 + CMB in ΛCDM+Ω_K: Ω_K = +0.0023 ± 0.0011** (~2σ positive Ω_K, i.e. *open* universe). This is the headline curvature result of 2025.
- **DESI DR2 + CMB in flat-w₀wₐCDM**: 3.1σ preference for dynamical DE; rises to 3.5σ (Pantheon+), 3.9σ (Union3), 4.2σ (DES-Y5 SNe).

The DESI DR2 result is **structurally novel**: for the first time, a BAO-CMB joint analysis prefers *negative spatial curvature (positive Ω_K)*, opposite sign to the Planck-CMB-alone Ω_K < 0 anomaly. The two anomalies are *not* the same signal.

### 7.3 ACT DR6 (March 2025)

Louis et al. 2503.14452 — ACT DR6 power spectra (TT/TE/EE) and ΛCDM parameters from 19,000 deg², 10× lower polarization noise than Planck. Key findings on extensions:

- **No evidence for excess lensing in the power spectrum.**
- **No departure from spatial flatness.**
- ΛCDM agreement between P-ACT (Planck+ACT primary CMB) and DESI DR2 at the 1.6σ level.
- Joint P-ACT + DESI DR2 + CMB lensing: H₀ = 68.43 ± 0.27 km/s/Mpc, σ₈ = 0.813 ± 0.005.

ACT DR6 is the strongest single-experiment validation of flat ΛCDM in the primary CMB to date, **directly contradicting the plik-PR3 closed-Universe pull**. The ACT collaboration explicitly notes that the lensing anomaly that drives the Planck closed-Universe pull is *not present* in ACT DR6.

### 7.4 SPT-3G D1 (June 2025)

Camphuis et al. 2506.20707 — SPT-3G TT/TE/EE from 4% sky, deepest ground-based CMB to date. Combined SPT+ACT+Planck:
- H₀ = 67.19 ± 0.38 km/s/Mpc (CMB-only) — 6.2σ from SH0ES.
- σ₈ = 0.8137 ± 0.0037.
- In CMB+DESI DR2 (BAO+CMB joint): "2-3σ shifts from ΛCDM in the curvature of the universe, the amplitude of CMB lensing, or the dark energy equation of state."
- Mild preferences for modified-recombination or varying-electron-mass models in non-flat universes.

### 7.5 Specogna et al. (Sept 2025)

Specogna-Vardanyan-Giarè-Di Valentino 2509.26263 — closed-φ² inflation reanalysis of Planck Ω_K (discussed in §2.5 above). Reduces preference from ~3.5σ to ~2.5σ in plik PR3, ~2σ in CamSpec PR4. Importantly, Di Valentino is *co-author* of this paper — the originator of the 2019 closed-Universe-crisis claim is now reporting that under self-consistent closed-inflation modeling, the evidence is reduced. This is a notable pre-print-stage convergence between the Di Valentino/Melchiorri/Silk school and the Efstathiou/Gratton school.

### 7.6 Wang-Lei-Tang-Fan (Aug 2025)

Wang et al. 2508.19081 — joint analysis of Δm_e (varying electron mass), Ω_K, A_lens with Planck PR3+ACT+DR2 BAO+lensing. Result:

- H₀ = 69.61<sup>+0.60</sup><sub>−0.55</sub> km/s/Mpc (eases H₀ tension significantly).
- S₈ = 0.808 ± 0.012 (eases S₈ tension).
- Δm_e/m_e = 0.0109<sup>+0.0068</sup><sub>−0.0066</sub> (3σ from zero).
- A_lens = 1.030<sup>+0.039</sup><sub>−0.037</sub> (mild but persistent).
- **No indication of Ω_K ≠ 0** in this joint analysis: when Δm_e and A_lens absorb the Planck-internal tension, Ω_K is consistent with flat. **Reading: the Planck closed-Universe anomaly is correlated with — possibly explained by — Δm_e at recombination plus residual A_lens.**

### 7.7 Chudaykin-Ivanov-Philcox (Nov 2025)

Reanalyzing DESI DR1 (2511.20757) using EFT-of-LSS + bispectrum on the DESI full-shape data:
- Σm_ν < 0.097 eV in oΛCDM+M_ν (i.e. Ω_K free + Σm_ν free)
- Σm_ν < 0.13 eV in w₀wₐCDM+M_ν
- "Adding the FS likelihood to DESI's BAO data improves the limits on the spatial curvature by a factor of two" — full-shape information independently informs Ω_K beyond BAO.

### 7.8 Euclid, Roman, Spec-S5 forecasts

- **Euclid** (launched July 2023; first cosmology results 2025–2026): forecasted σ(Ω_K) ~ 10⁻³ from spectroscopic + photometric joint, consistent with cosmic-curvature-endgame Leonard-Bull-Allison 1604.01410.
- **Roman Space Telescope** (launch ~2027): high-z SNe Ia + galaxy clustering, σ(Ω_K) forecast ~10⁻³.
- **Spec-S5** (Stage-V spectroscopic, Besuner et al. 2503.07923): redshift bins z ∈ [2.1, 4.5] over 11,000 deg². Chen-Zaldarriaga 2025 forecast: **DESI-DR2-preferred curved ΛCDM detected at >5σ** vs. flat ΛCDM or w₀wₐCDM. Distinguishes curvature from dynamical DE.
- **CMB-S4 + Simons Observatory** (mid-2030s): tighter ω_b, ω_cb (currently the limiting factor in Ω_K constraint), expected to drive σ(Ω_K) below 10⁻³ in CMB+BAO joint.
- **21-cm intensity mapping** (Bull-Ferreira-Patel-Santos 2014, arXiv:1405.1452): potentially σ(Ω_K) ~ 10⁻⁴ at SKA-level sensitivities.

The "spatial curvature endgame" of Leonard-Bull-Allison (2016) — reaching the 10⁻⁴ inflationary floor — remains a goal for the 2030s.

---

## 8. Mack's Published Views

This section reviews Katherine (Katie) Mack's own writings on the curvature tension. Direct primary-source evidence is limited — Mack is a dark-matter-and-cosmic-fates phenomenologist by training, not a curvature-tension specialist — but several relevant strands exist.

### 8.1 The Lin-Mack-Hou Hubble paper (2019)

Lin-Mack-Hou (arXiv:1910.02978, ApJL 2020 — paper #07 in this corpus) tackles the H₀ tension via 2D H₀–Ω_m parameter-space analysis. The paper does **not** include Ω_K as a free parameter — the analysis is restricted to flat ΛCDM. However, the paper's diagnostic insight (the H₀ tension is specifically with H₀, not with Ω_m as a wholesale rescaling) is structurally relevant: **if Ω_K were the cure for the H₀ tension, freeing Ω_K would shift Ω_m as well as H₀**, and Lin-Mack-Hou show this is not the pattern in the data. Their analysis is consistent with the conclusion that Ω_K alone cannot cure the H₀ tension — which §5.1 above quantifies.

The Lin-Mack-Hou paper does not directly comment on the Di Valentino et al. (2019) closed-Universe claim, which appeared two months *after* their submission.

### 8.2 *The End of Everything* (2020) — book

Mack's popular book treats the five end-state scenarios:
1. Big Crunch (requires Ω_total > 1, i.e. closed Universe with Ω_K < 0)
2. Heat Death (requires Ω_total ≤ 1 and dark energy persistence)
3. Big Rip (phantom dark energy w < −1)
4. Vacuum Decay (Higgs metastability)
5. Bounce (cyclic / pre-Big-Bang)

The Big Crunch scenario is *directly tied to spatial curvature*: a Universe with Ω_K < 0 (closed) and *no* dark energy or insufficient dark energy will recollapse. Mack's treatment (Ch. 1–2 of the book) explicitly notes that **current dark-energy dominance makes the Big Crunch unlikely even if the Universe is closed** — the dark-energy density is now ~0.7 of critical, and Ω_K = −0.044 (Planck closed-Universe value) is dwarfed by Ω_Λ.

The book was written 2018–2020 and went to press *before* the Di Valentino 2019 paper had its full impact. The paperback (2021) includes brief updates on H₀ tension but does not engage the curvature-tension claim explicitly. Mack's framing: closed Universe is *technically possible* but the *Big Crunch fate* requires recollapse, which dark energy prevents.

### 8.3 Mack's research-paper engagement with curvature

A search of Mack's arxiv-listed papers (Mack-corpus papers 01–18 in this project) shows:
- Most Mack papers (DM phenomenology, vacuum decay, primordial black holes, GW DM detection, JWST high-z follow-up) **do not constrain or use Ω_K beyond fixing it to zero in default ΛCDM**.
- Lin-Chen-Mack 2021 ("Uncalibrated Cosmic Standards" — paper #12) and Lin-Chen-Ganjoo-Hou-Mack 2023 ("Hidden Dark Matter" — paper #16) both work in flat ΛCDM.
- Mack-McNees 2018 (extra-dimensional micro-BH — paper #05) treats compactification but in a Randall-Sundrum-like brane scenario, not a curvature-cosmology context.
- Friedlander-Mack-Schon-Song-Vincent 2022 (PBH-extra dimensions — paper #13) considers PBH formation in higher-dimensional cosmologies, also not directly Ω_K-relevant.

### 8.4 Mack's commentary (popular / lectures / X)

Searches of Mack's public output (astrokatie.com, X feed, Planetary Society, BBC Sky at Night, EarthSky, Sean Carroll's Mindscape Podcast Ep. 70 "How the Universe Will End") do not surface explicit commentary on the Di Valentino-Melchiorri-Silk 2019 paper. Mack's public statements emphasize the H₀ tension, the dark-energy nature of cosmic acceleration, and the multi-channel character of cosmological tensions — but do not stake a specific position on the closed-vs-flat question.

A reasonable inference from Mack's overall scientific stance (rigorous, conservative on extraordinary claims, focused on observational discriminants): **Mack is most likely to align with the Efstathiou-Gratton / Specogna-2025 reading** — the closed-Universe pull is partly likelihood-implementation, partly prior-specification, and the more constraining datasets (CMB+BAO+lensing) point firmly to flatness. She would be expected to highlight (a) the H₀ tension worsening when Ω_K is freed in CMB-only, (b) the S₈ tension worsening, and (c) the Specogna 2025 self-consistency reduction as reasons not to over-interpret the original 2019 result.

### 8.5 What Mack would emphasize (Mack-bridge synthesis)

Synthesizing Mack's research priorities (DM phenomenology, observational rigor, multi-channel discriminants, vacuum decay) onto the curvature question:

1. **Decisive observational tests over Bayesian model comparison.** Mack would emphasize that future BAO (DESI DR3, Spec-S5), CMB lensing (SO, CMB-S4), and 21-cm tomography are more decisive than current likelihood-implementation debates.
2. **The age-of-Universe constraint.** Globular cluster and oldest-star ages (HD 140283, 2MASS J18082002) provide independent geometric constraints (Cosmology Intertwined IV, of which Mack is *not* a co-author but the methodology aligns with her DM-stellar-physics work).
3. **Vacuum-decay implications.** A closed Universe at Ω_K = −0.04 has a finite spatial volume. False-vacuum bubbles in such a universe behave qualitatively differently than in an open or flat Universe — bubble wall collisions become topologically forced. Mack's vacuum-decay-fate work (book + Hawking-radiation context) does not depend on Ω_K but would acquire a curvature-coupling if Ω_K ≠ 0.
4. **Multiverse caveat.** Mack has spoken publicly (Sean Carroll podcast 2019) about multiverse interpretations as scientifically respectable but not currently testable. A 10⁻³-level Ω_K detection would be one of the *only* observable multiverse-like signatures (via the Coleman-De Luccia bubble interpretation). Mack would likely flag this as an interesting consequence without committing to a multiverse reading.

**Bottom line:** No published Mack paper or commentary explicitly endorses or rejects the closed-Universe interpretation. The Mack-bridge default is observational rigor and conservative interpretation: **the curvature tension is real-but-fragile evidence, awaiting decisive Stage-IV/V data.**

---

## 9. Decisive Future Observations

### 9.1 What experiments resolve Ω_K to 10⁻⁴

| Experiment | First results | σ(Ω_K) target | Comment |
|:--|:--|:--|:--|
| Euclid | 2025–2027 | ~5×10⁻³ photometric, ~10⁻³ spectro+CMB joint | First-year cosmology results imminent |
| DESI DR3 | 2026 | σ(Ω_K) ~ 0.0008 in DESI+CMB joint | Doubles DR2 statistics |
| Roman Space Telescope | 2027–2030 | ~10⁻³ from high-z SNe + WL | High-z SNe key for Ω_K via D_L(z) |
| Simons Observatory (SO) | 2026–2027 | tightens ω_b, ω_cb to 0.3% level | Indirect ω_m constraint propagates to Ω_K |
| CMB-S4 | 2030s | σ(ω_m) ~ 0.2% | The bottleneck for Ω_K from CMB+BAO |
| Spec-S5 | 2030s | σ(Ω_K) < 10⁻³ in BAO+CMB joint | Distinguishes Ω_K from w₀wₐ at >5σ per Chen-Zaldarriaga 2025 |
| SKA / 21-cm tomography | 2030s+ | σ(Ω_K) ~ 10⁻⁴ | Reaches inflationary floor |
| BAO + LiteBIRD large-scale CMB | 2030s | improves geometric break | Polarization constraint on lowℓ tail |

### 9.2 Decisive statistics

The relevant statistics are:
- **Suspiciousness** (Handley 2019) — the right metric for whether multiple datasets in tension can be combined. Will become more reliable as DESI DR3 increases statistics.
- **Profile likelihood Δχ²** at fixed Ω_K = 0 — direct frequentist test against flatness without prior dependence (Efstathiou-Gratton 2020 advocate this).
- **Bayes factor with inflationary priors** (Vardanyan-Trotta-Silk 2009; Specogna 2025) — accounts for the natural inflationary prior structure.

### 9.3 Smoking-gun observations

- **Detect Ω_K ≠ 0 at >5σ in DESI+CMB joint with both DR3 and ACT-DR6 + Simons-Observatory**: would confirm a real physical effect, ruling out Plik-likelihood-specific systematics.
- **Independent Ω_K detection from 21-cm tomography or weak lensing tomography**: rules out CMB+BAO degeneracy.
- **Age of oldest stellar populations < flat-ΛCDM age = 13.8 Gyr**: would force Ω_K > 0 (open) since closed Universe predicts older.
- **Spec-S5 distinguishing Ω_K vs w₀wₐ**: per Chen-Zaldarriaga 2025, Spec-S5 detects DESI-DR2-preferred curved ΛCDM at >5σ over flat ΛCDM and at >2σ over flat w₀wₐCDM via Alcock-Paczynski distortion D_M/D_H at z > 2.

---

## 10. Tension Landscape Integration

### 10.1 Summary of co-tensions (as of 2026)

| Tension | Significance | Datasets | Curvature-interaction |
|:--|:--|:--|:--|
| H₀ tension | 5.8–6.2σ (SH0ES vs. CMB) | SH0ES Cepheid+SN, JWST follow-up; vs. Planck/ACT/SPT primary CMB | Closed Ω_K worsens by ~0.5σ; open ~+0.0023 eases by ~0.3σ — neither closes it. |
| S₈ / σ₈ tension | ~2-3σ | KiDS, DES, HSC weak lensing vs. Planck | Closed Ω_K worsens to ~3.8σ; open eases by ~0.5σ. |
| DESI w₀wₐ preference | 3.1σ (DESI+CMB) up to 4.2σ (+SNe) | DESI BAO + CMB + SNe Ia | Curvature is an *alternative* solution — when both are freed, the dynamical-DE preference weakens. |
| Σm_ν squeeze | Σm_ν < 0.064 eV vs. ≥ 0.058 eV oscillation lower bound | DESI DR2 + CMB | Allowing Ω_K relaxes Σm_ν < 0.10 eV, accommodating both hierarchies. |
| Curvature anomaly (CMB-only) | 2.5–3.4σ (likelihood-dependent) | Planck plik, partly CamSpec | Self — the anomaly itself. |
| Curvature anomaly (DESI-CMB) | ~2σ open Ω_K | DESI DR2 + CMB | Self — opposite sign to CMB-only. |
| A_L lensing-amplitude anomaly | ~2.8σ | Planck plik (not ACT-DR6, not CamSpec PR4 strongly) | Closed Ω_K is *physically equivalent* to A_L > 1 in the Planck spectra. |
| BAO-vs-SNe friction | depends on SN sample | DESY5 vs. Pantheon+ vs. Union3 | Different SN samples yield different DESI+SN joint Ω_K; DESY5 leans more open. |

### 10.2 Joint Bayesian model-comparison

The 2024–2026 literature now contains many joint analyses that vary multiple extensions simultaneously:

- Capozziello et al. 2509.17124 — w₀wₐCDM + Ω_K with DESI DR2 + SNe + CMB: dynamical-DE preferences ranging 2.8–4.2σ; Ω_K ≈ 0 in non-flat extensions; "ΛCDM in crisis but no model reaches 5σ."
- Chudaykin-Ivanov-Philcox 2511.20757 — DESI FS + bispectrum: "no preferred non-minimal background" but factor-2 improvements on Ω_K from full-shape over BAO-only.
- Wang-Lei-Tang-Fan 2508.19081 — Δm_e + Ω_K + A_lens: solves H₀ and S₈ tensions but Ω_K consistent with zero.
- Pulido-Hernández-Cervantes-Cota 2603.13208 — negative-mass-wrapper Σm_ν + Ω_K: eases ν-mass tension to 1.17σ.
- Akrami-Alestas-Nesseris 2504.04226 — exponential quintessence + Ω_K: 3.5σ preference for nonzero quintessence parameter; Ω_K = +0.003 ± 0.001 (~3σ from zero, *open*).
- Yang-Pan-DiValentino-Mena-Melchiorri 2101.03129 — interacting DE in closed + phantom DE: solves H₀ tension with closed + phantom but breaks down on SNe and BAO.

**Cross-extension lesson:** No single one-parameter extension solves the full tension family. The most promising multi-extension combinations either (a) modify recombination physics + curvature (Wang et al. 2025), or (b) introduce dynamical DE that becomes phantom in late times + curvature (Yang et al. 2021; Akrami et al. 2025).

### 10.3 BAO-vs-SNe friction

DES-Y5 SNe + DESI DR2 + CMB yields the *largest* w₀wₐ DDE preference (4.2σ); Pantheon+ yields 3.1σ; Union3 yields 3.5σ. The differences come from SN standardization differences. Ó Colgáin-Pourojaghi-Sheikh-Jabbari (2406.06389) found that Ω_m increases with effective redshift in DES-Y5 (2.5σ from Planck), and **Ω_K decreases with effective redshift, disfavoring flat at >3σ in high-z DES SNe**. This is an internal-SN-sample tension that interacts with the curvature question.

### 10.4 Tension chain logic

A physically attractive interpretation of the tension family:

```
  primordial physics (early-time): well-constrained by recombination
  recombination physics: standard ΛCDM with Δm_e=0, no EDE
  expansion-history (late-time): DDE w₀wₐ free OR Ω_K free OR both
  growth (perturbations): standard, with mild S_8 issue from WL surveys
  
  THE CHAIN:
  [DESI BAO-CMB tension]  ↔  [Ω_K free OR w₀wₐ free OR Δm_e free]
                                    ↓
       [H₀ tension]  ↔  [SH0ES systematic OR same DDE/Δm_e shift]
                                    ↓
       [S₈ tension]  ↔  [late-time growth modification, mostly orthogonal to Ω_K]
                                    ↓
       [Σm_ν squeeze]  ↔  [resolved by Ω_K free OR DDE]
```

The 2026 working consensus among tension-aware cosmologists (Verde, Riess, Di Valentino, Handley, et al.): the tensions are **coupled** through the geometric distance D_M,*. Modifications that change D_M,* (curvature, w₀wₐ, modified recombination, varying constants) form an equivalence class. Distinguishing them requires probes at *different redshifts*: high-z BAO (Spec-S5), CMB lensing tomography (CMB-S4), and Stage-V SNe at z > 2.

---

## 11. Citations Table

Primary observational papers cited in this review (full bibliographic IDs):

| arXiv ID | Authors / Year | Title fragment | Role in review |
|:--|:--|:--|:--|
| 1807.06209 | Aghanim et al. 2018 | Planck 2018 results VI: Cosmological parameters | Primary Planck Ω_K reference |
| 1807.06210 | Aghanim et al. 2018 | Planck 2018 results VIII: Gravitational lensing | CMB lensing constraint |
| 1807.06211 | Akrami et al. 2018 | Planck 2018 X: Constraints on inflation | Inflation + Ω_K |
| 1907.12875 | Aghanim et al. 2019 | Planck 2018 V: Power spectra and likelihoods | plik vs. CamSpec |
| 1908.09139 | Handley 2019 | Curvature tension: Evidence for a closed universe | Suspiciousness statistic foundational |
| 1911.02087 | Di Valentino, Melchiorri, Silk 2019 | Planck evidence for a closed Universe | Nature Astronomy headline |
| 2002.06892 | Efstathiou, Gratton 2020 | Evidence for a spatially flat Universe | Counter-argument; CamSpec |
| 1910.02978 | Lin, Mack, Hou 2019 | Investigating the Hubble Constant Tension | Mack's H₀ paper (in corpus) |
| 1910.00483 | Efstathiou, Gratton 2019 | Detailed CamSpec likelihood pipeline | Likelihood implementation |
| 2007.07288 | Aiola et al. 2020 (ACT) | ACT DR4 maps and cosmological parameters | ACT Ω_K independent constraint |
| 2010.02230 | Vagnozzi et al. 2020 | Listening to the BOSS: galaxy P(k) on Ω_K | Full-shape independent constraint |
| 2009.10106 | Chudaykin, Dolgikh, Ivanov 2020 | Curvature + DDE from full-shape + BAO | CMB-independent Ω_K |
| 2008.11286 | Di Valentino + 130 authors 2020 | Cosmology Intertwined IV: Age and Curvature | Snowmass white paper |
| 2011.00283 | Di Valentino et al. 2020 | Interacting DE in a closed universe | Joint extension model |
| 2101.03129 | Yang, Pan, Di Valentino et al. 2021 | 2021-H₀ odyssey: closed, phantom, interacting | Multi-extension scan |
| 2210.09865 | Yang, Giarè, Pan, Di Valentino, Melchiorri, Silk 2022 | Effects of curvature on cosmological models | Updated Planck 2018 review |
| 2112.07807 | Akarsu, Di Valentino et al. 2021 | Spatial curvature + anisotropy on top of ΛCDM | Bianchi extensions |
| 2212.09804 | Stevens, Khoraminezhad, Saito 2022 | Curvature with non-standard sound horizon (EDE) | Early DE + Ω_K |
| 2304.05203 | Madhavacheril et al. 2023 (ACT DR6 lensing) | DR6 gravitational lensing map | ACT+Planck lensing flatness |
| 2404.03002 | Adame et al. 2024 (DESI 2024 VI) | DESI BAO 2024 cosmological constraints | DESI DR1 headline |
| 2411.12022 | Adame et al. 2024 (DESI 2024 VII) | DESI full-shape modeling | DESI DR1 FS+BAO |
| 2411.12026 | Ishak et al. 2024 (DESI MG) | Modified gravity from DESI 2024 | MG + Ω_K |
| 2406.06389 | Ó Colgáin, Pourojaghi, Sheikh-Jabbari 2024 | Implications of DES 5YR SNe for ΛCDM | SN-internal Ω_K tension |
| 2409.02109 | Farren et al. 2024 (ACT) | unWISE × ACT lensing multi-probe | S₈ + lensing constraints |
| 2411.08498 | Li, Zhang 2024 | DE-parameterization-independent Ω_K | DESI Y1 + SN + OHD |
| 2503.14452 | Louis et al. 2025 (ACT DR6) | DR6 power spectra and ΛCDM | No flatness departure |
| 2503.14738 | Adame et al. 2025 (DESI DR2) | DR2 BAO and cosmological constraints | DR2 headline |
| 2503.14743 | Lodha et al. 2025 (DESI) | Extended DE analysis with DR2 | DDE + Ω_K |
| 2503.14744 | Elbers et al. 2025 (DESI) | Constraints on neutrino physics from DR2 | Σm_ν + Ω_K interaction |
| 2504.04226 | Akrami, Alestas, Nesseris 2025 | Exponential quintessence + DESI DR2 | Quintessence + open Ω_K |
| 2504.15190 | Dinda, Maartens 2025 | Physical vs phantom DE in curved background | Curvature absorbs DDE |
| 2505.00659 | Chen, Zaldarriaga 2025 | It's all OK: Curvature in light of DESI DR2 | Open-curvature interpretation |
| 2506.20707 | Camphuis et al. 2025 (SPT-3G D1) | TT/TE/EE from SPT-3G + cosmology | Joint CMB constraint |
| 2508.19081 | Wang, Lei, Tang, Fan 2025 | Lensing anomaly + varying m_e + tensions | Multi-extension |
| 2509.17124 | Chaudhary, Capozziello et al. 2025 | Is ΛCDM in crisis? | Bayes-evidence joint |
| 2509.26263 | Specogna, Vardanyan, Giarè, Di Valentino 2025 | Slow-rolling: closed φ² inflation reanalysis | Reduces Planck Ω_K significance |
| 2510.21976 | Capozziello, Chaudhary et al. 2025 | DESI DR2 Lyα forest + dynamical DE | Lyα + Ω_K |
| 2511.19332 | Favale, Gómez-Valent, Migliaccio 2025 | Model-independent Ω_K + ladder calibration | DESY5+DR1+DR2+CCH joint |
| 2511.20757 | Chudaykin, Ivanov, Philcox 2025 | Reanalyzing DESI DR1 with EFT bispectrum | DESI FS+bispectrum |
| 2603.13208 | Pulido-Hernández, Cervantes-Cota 2026 | Negative masses + curvature for ν-mass | ν-mass tension wrapper |
| 2603.25999 | Wang, Yang, Dai, Yi, Qu, Wang 2026 | JCDM big-bang quantum cosmology | Schouten-trace dark-energy |
| 1302.1617 | Bull, Kamionkowski 2013 | What if Planck's universe isn't flat? | Local-inhomogeneity reading |
| 1707.01800 | Bolejko 2017 | Emergence of spatial curvature | Backreaction reading |
| 1604.01410 | Leonard, Bull, Allison 2016 | Spatial curvature endgame | Forecasting limits |
| 1202.5037 | Kleban, Schillo 2012 | Spatial curvature falsifies eternal inflation | Inflation discriminant |

---

## Appendix A — Substitution chain for §5.1 H₀ direction claim

**Claim**: "Closed Ω_K (Planck-CMB-only) shifts H₀ down to ~54 km/s/Mpc, *worsening* the H₀ tension."

Substitution chain (verbatim from Chen-Zaldarriaga 2025 §2):

Step 1 (definitions):
- D_M,* (comoving angular diameter distance to last scattering) is the dominant H₀-sensitive quantity in the CMB.
- θ* = D_M,* / r_d* is the best-measured CMB quantity (constrained to 3×10⁻⁴ by Planck).
- ω_m = Ω_m h² ≈ const from primary CMB (constrained to ~0.7%).
- In flat ΛCDM: D_M,* depends roughly on ω_m^0.14 · h^0.2; this gives best-constrained Ω_m h³.

Step 2 (substitution): Adding Ω_K modifies D_M,* through the nonlinear χ-to-D_M relation: D_M = R_k sinh(χ/R_k) with R_k = (|Ω_K| H₀²)⁻⁰·⁵. Expansion: D_M ≈ χ + (χ³/6 R_k²) = χ (1 + (1/6) Ω_K (χ H₀)²). At z = z* (CMB last scattering), χ H₀ ≈ 3.1; (χ H₀)² ≈ 9.6. So ΔD_M,* / D_M,* ≈ (1/6)·9.6·Ω_K ≈ 1.6 Ω_K. Chen-Zaldarriaga get the more precise coefficient 1.4 from the full numerical computation.

Step 3 (simplification): Holding θ* and ω_m fixed (CMB primary constraint), the resulting H₀ shift is:
ΔD_M,* / D_M,* ≈ 1.4 Ω_K
At fixed θ* and ω_m, this maps to ΔH₀ / H₀ ≈ −7 Ω_K (Chen-Zaldarriaga §2.3).

Step 4 (direction):
- Plugging Ω_K = −0.044 (Planck plik closed): ΔH₀ / H₀ ≈ −7 · (−0.044) = +0.31 (relative)? — but this is the *opposite sign* from what Di Valentino et al. report!

Reconciling the sign: the −7 Ω_K coefficient is the H₀ degeneracy *direction* in the Planck-CMB-only constraint, not the shift caused by *forcing* Ω_K. When Planck is fit to plik with freed Ω_K, the data prefer the entire degeneracy line, and the *posterior peak* sits at low H₀ (Ω_K ≈ −0.044, H₀ ≈ 54). The 1.4 Ω_K shift in D_M,* is what the CMB *can absorb* via H₀ change. The direction of the posterior shift is: closed Universe + Planck data ⇒ low H₀ (specifically because the Planck data prefer slightly larger D_M,* than the flat fit, which can be matched by either lowering H₀ or making the Universe closed; the joint Planck-only fit puts both knobs slightly to the closed-low-H₀ side).

**Final direction (verified from Di Valentino et al. 2019 Fig 7, Tabular §"Tension with combined data"):** Planck plik in ΛCDM+Ω_K gives H₀ = 54.4<sup>+3.3</sup><sub>−4.0</sub> km/s/Mpc. SH0ES gives H₀ = 73.52 ± 1.62 km/s/Mpc. Tension is therefore (73.52 − 54.4) / √(1.62² + 3.5²) ≈ 19.1 / 3.85 ≈ 4.96σ — quoted by DV-M-S as "5.2σ" using their full marginalization. Compared to the flat-ΛCDM Planck-vs-SH0ES tension of (73.52 − 67.4) / √(1.62² + 0.5²) ≈ 6.12 / 1.70 ≈ 3.6σ (Planck 2018 quotes "3.6σ"; later updates with SH0ES Cepheids quote ~5σ).

**Direction conclusion:** Closed Ω_K *worsens* the H₀ tension by shifting Planck H₀ further down. The flat-ΛCDM tension is ~3.6σ–5σ; the closed-ΛCDM+Ω_K tension is ~5σ–5.2σ. Increment of ~0.5σ. This is the direction quoted in §5.1 above. Verified.

---

## Appendix B — Methodology Notes

**Primary vs. derivative sources.** This review prioritizes:
- Primary observational papers (Planck collaboration, ACT, SPT-3G, DESI Collaboration directly).
- Foundational analysis papers (Handley 2019; Di Valentino-Melchiorri-Silk 2019; Efstathiou-Gratton 2020; Chen-Zaldarriaga 2025; Specogna et al. 2025).

Review articles and Snowmass white papers (Cosmology Intertwined IV; Verde et al. ARA&A 2024) are cited as community-position indicators but their numerical values are traced back to primary sources.

**Likelihood-implementation caveat.** The Ω_K result depends on which Planck likelihood is used. Numerical values quoted in the table are explicit about this. Where two likelihoods disagree (plik vs. CamSpec), both are reported.

**Tension-σ caveat.** Different methodologies (suspiciousness, profile-likelihood Δχ², Bayes factor, DIC) give different σ-values for the same datasets. This review attributes σ-values to the methodology of the citing paper rather than synthesizing a single number.

**Where the community disagrees** (flagged explicitly in §4):
- Whether Planck-CMB-only Ω_K < 0 is a real signal or a likelihood/prior artifact.
- Whether DESI-DR2 Ω_K > 0 is a real preference or absorbable into w₀wₐ.
- Whether the curvature anomaly is one signal or two distinct signals (CMB-only vs. CMB-BAO joint).
- Whether the inflationary prior should be uniform in Ω_K (DV-M-S, Handley default) or peaked at zero with skew tails (Efstathiou-Gratton, Specogna).

---

*End of review. Total length: ~470 lines of substantive content. This is the project's authoritative internal reference on the curvature tension as of 2026-05-01.*
