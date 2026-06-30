---
name: s100b-wa-robust-lessons
description: S100b W1-3 w_a robustness gate — INFO 2.946σ; route-A/route-B operationalization gap; compressed-CMB fiducial-validation lesson
metadata:
  type: project
---

# S100b-WA-ROBUST (W1-3) — outcome pin + reusable lessons

**Outcome (2026-06-07)**: INFO — d_σ = 2.946 (band 2–3) for w_a = 0 (S58 four-fold lock) vs the
Planck-low-ℓ-independent combination. Route-A reconstruction (compressed Planck+ACT geometric CMB
+ DESI DR2 BAO 13-distance + Pantheon+ shape): w_a = −0.7970 +0.2705/−0.2808. Canonical home:
`sessions/framework/registry/falsifier-master-inventory.md` Row #1 sub-row `1.wa-robust-s100b`
(+ watchlist audit-pin §"S100b W1-3"). Verdict audit_sha256 `15c54621f59184cc…`. Do NOT duplicate
the numbers table here (AMRI).

**Why:** three findings recur in any future w_a / dark-energy systematics gate.

**How to apply:**

1. **"Planck-low-ℓ-independent" is NOT one combination.** Geometric-compression route (paper-05
   Bansal-Huterer (R, ℓ_a, ω_b) — keeps Planck-calibrated acoustic geometry, drops only the low-ℓ
   anomaly channel) recovers w_a ≈ −0.80 (d_σ 2.95, indistinguishable from the 2.92 DR2-marg
   baseline); full-Planck-swap route (Giare ACT+WMAP full likelihoods) gives −0.47 (2.14σ), SPT
   −0.29 (1.16σ). Gap = 1.6σ^B — the DR2-era w_a pull is NOT primarily a Planck-low-ℓ artifact;
   it lives in the BAO+SN+geometric-CMB interaction with the Planck-vs-ACT/WMAP ω_m calibration
   difference setting the spread. Always declare WHICH operationalization a "robust" claim uses.

2. **Compressed-CMB fiducial-validation lesson (pipeline-internal)**: absolute (R, ℓ_a) pulls at a
   PUBLISHED fiducial are the WRONG internal calibration test when that fiducial is not the CMB
   chain-mean (paper-05 App-B fixes H₀ = 68.24 from a DESI+CMB+DESY5 fit → common −0.3% D_M(z*)
   offset → ℓ_a's 0.028% precision turns it into ~10 fake σ). The RIGHT test is the D_M-free
   invariant R/ℓ_a = (100√ω_m/c)·(r_*/π) — passed at +0.17σ. Same trap will recur for any
   compressed-datavector reconstruction.

3. **SN-compression is the dominant reconstruction systematic**: paper-02's LCDM-shape fit
   (Ω_m = 0.333 ± 0.018) mapped via shape-matching (V0) vs direct-Ω_m prior (V1) vs range/weight
   variants moves d_σ across 2.78–4.03. Shape-matching with free offset (= free M) is the faithful
   mapping of a published LCDM-shape fit onto w0waCDM; a direct-Ω_m prior is NOT (it imports the
   LCDM shape-degeneracy as a false constraint). r_*-calibration sensitivity: ±0.08σ per 0.1%.

4. **Verdict-band robustness vs central-value robustness are different claims**: both routes land
   INFO-band (SPT PASS-side) while central w_a differs by 0.33 — band-level conclusions can be
   route-robust when point estimates are not.

Related: [[s84-dr3-response-protocol]] (R_842 stays the binding instrument; this gate does NOT
trigger it), `project_s100b_w1_plan_pins.md` (W1-4 w_0-discriminator framing).
