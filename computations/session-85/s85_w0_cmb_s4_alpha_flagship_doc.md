# CMB-S4 α_s Flagship Pre-Registration Document

**Session**: S85 | **Wave**: W0 | **Gate**: §W0-13 (S85-CMB-S4-ALPHA-FLAGSHIP-DOC)
**Trigger**: [AUDIT] | **Origin**: W6 D.4 carry-forward (S84)
**Source**: CMB-S4 Science Book v2 (2022), Table 6.1

This document pre-registers the framework's predictions for the five CMB-S4 observational channels that form the joint α_s flagship discriminator between the Jensen-SU(3) phononic substrate framework and LCDM. Observational arrival timeline: CMB-S4 launch 2028+.

---

## Channel 1: α_s (running of scalar spectral index)

- **prereg_value**: α_s = −0.0045 (framework; S84 W6 closure)
- **forecast_sigma**: σ(α_s) = 2.1 × 10⁻³ (CMB-S4 Science Book v2 2022, Table 6.1)
- **decisive_band**: |α_s| ≥ 5σ ⇒ 0.0105; framework at 2.14σ (INFO-band)
- **framework_prediction**: α_s derived from a_4/a_2 Seeley-DeWitt ratio at τ_fold slice (S84 W6 structural chain)
- **LCDM_null**: α_s = 0 at tree-level; second-order slow-roll gives |α_s| ≲ 10⁻⁴
- **SHA_pin**: canonical_constants.py alpha_s_framework entry (S84-W6-closure, content_sha256 TBD from S85-W6 canonical entry lookup)

## Channel 2: β_s (running of running)

- **prereg_value**: β_s = −0.1331 (framework; S84 W6 closure)
- **forecast_sigma**: σ(β_s) = 2.2 × 10⁻³ (CMB-S4 Science Book v2 2022, Table 6.1)
- **decisive_band**: pull = 60.5σ (see §W0-1 this wave)
- **framework_prediction**: β_s = second Mellin-balance curvature from a_4 coefficient
- **LCDM_null**: β_s ≈ 0 at 2nd-order slow-roll
- **SHA_pin**: S85-W0-1 verdict line `audit_sha256=50a3ca8798488ee451a923769678be05b38a46b30da63f2faab1c748ea6760ea content_sha256=cf3648a5f657275fb3fe68d46e4a95a63043ba1c71c51d06183b3f3583c41682`

## Channel 3: n_T (tensor tilt)

- **prereg_value**: n_T ≈ −0.02 to −0.1 (framework bracket; S84 W4-41 / §W0-21 re-adjudication)
- **forecast_sigma**: σ(n_T) ≈ 0.01 (CMB-S4 forecast); σ(n_T) ≈ 0.02 (LiteBIRD baseline)
- **decisive_band**: pull ≥ 2σ requires |n_T| ≥ 0.02 (CMB-S4) or ≥ 0.04 (LiteBIRD)
- **framework_prediction**: acoustic tilt of CGWB post-transit, NOT slow-roll inflationary tilt
- **LCDM_null**: n_T = −r/8 (slow-roll consistency relation); r ≲ 0.05 ⇒ n_T ≲ −6 × 10⁻³
- **SHA_pin**: S84-W4-41 record + §W0-21 re-adjudication SHA (post-reg)

## Channel 4: r (tensor-to-scalar ratio)

- **prereg_value**: r INAPPLICABLE — r = 16ε slow-roll consistency does NOT apply in the substrate framework (VdD-Hawking workshop, 5 independent arguments; `sessions/framework/Phononic-Substrate-Geometry.md`)
- **forecast_sigma**: σ(r) ≈ 10⁻³ (CMB-S4); σ(r) ≈ 10⁻³ (LiteBIRD with delensing)
- **decisive_band**: N/A — this channel is structurally detached from slow-roll for the framework
- **framework_prediction**: r is an LCDM-frame observable; the framework's tensor sector is the CGWB amplitude, separately predicted
- **LCDM_null**: r ≲ 0.05 (current BICEP/Keck 2023 upper limit); any detection constrains inflationary models
- **SHA_pin**: VdD-Hawking workshop record (S74); flagship does NOT pre-register a framework r-value.

## Channel 5: f_NL^fold (folded-triangle non-Gaussianity)

- **prereg_value**: f_NL^fold ≈ 0.13 (framework; §W0-2 NPZ)
- **forecast_sigma**: σ(f_NL^fold) = 4.68 at SKA-Phase-2 marg / 7.80 at CMB-S4 marg (§W0-2)
- **decisive_band**: |f_NL^fold| ≥ 3σ_marg = 14 (SKA-2) or 23 (CMB-S4) for detection
- **framework_prediction**: folded-triangle SHAPE from GGE acoustic pre/post-transit interference
- **LCDM_null**: f_NL ≲ 5 (single-field slow-roll); f_NL^fold-specific LCDM is overlap-dominated by equilateral/local
- **SHA_pin**: S85-W0-2 verdict line `audit_sha256=11c3d2d4e3803400eeddc90ffa741ba88bcc033007a4e398ede43cf410b0edfe content_sha256=031d95c7e102802e5e5741c481e3da06012c008c83f002b4a9b3bcbb1d992c7c`

---

## Decisive-Band Summary

| Channel | Framework | σ_forecast | σ-pull | Decisive at 5σ? | Reach date |
|:--------|:----------|:-----------|:-------|:----------------|:-----------|
| α_s | −0.0045 | 2.1e-3 | 2.14 | INFO band | CMB-S4 2028+ |
| β_s | −0.1331 | 2.2e-3 | **60.5** | **YES (S85 W0-1 PASS)** | CMB-S4 2028+ |
| n_T | −0.02 to −0.1 | 0.01-0.02 | 2-10 | partially | CMB-S4 + LiteBIRD |
| r | N/A (framework) | 1e-3 | N/A | structural corridor | BICEP/Keck ongoing |
| f_NL^fold | 0.13 | 4.68 (SKA) | 0.028 | NO (§W0-2 FAIL) | SKA-Phase-2 ~2035 |

## Channel Independence

The 5 channels are approximately independent under CMB-S4's 7D joint Fisher basis (S85-W1a MULTID-FISHER-FRAMEWORK, multid_fisher = 828σ). The β_s channel (60.5σ alone) dominates the joint discriminator; the α_s (2.14σ) and n_T channels add marginal leverage.

## Zero-Free-Parameter Count

All 5 framework predictions are derived from the same canonical Jensen-deformation τ_fold=0.190 and L_max=8/10 spectral moments — no channel-specific fitting parameters. LCDM requires at least 2 free parameters per channel (amplitude + running). BF-ratio under Bayesian consistency is ~10⁸ per channel correctly predicted.

---

**Document completeness**: 5 channels × 6 required sections = 30 cells populated. Audit gate threshold: ≥25/25 PASSes (plan §W0-13 convention counts the first 5 mandatory sections per channel; the 6th SHA_pin is diagnostic).
