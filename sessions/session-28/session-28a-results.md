# Session 28a Results: Zero-Cost Diagnostics + Torsionful BCS

**Date**: 2026-02-27
**Computations**: 7 (6 zero-cost post-processing + 1 torsionful BCS)
**Runtime**: ~10 min total (4 parallel agent groups)
**Input data**: s19a, s23a, s25, s27 .npz files (all pre-existing)

---

## I. GATE VERDICTS

| # | Gate | Verdict | Decisive Number | Feeds Into |
|:--|:-----|:--------|:----------------|:-----------|
| 28a-1 | KC-1 Parametric Injection | **PASS** | B_k(gap) = 0.023, Γ = 29,643 at τ=0.40 | 28c (KC-2 through KC-5) |
| 28a-2 | L-1 Thermal Spectral Action | **CLOSED** | dF/dτ > 0 everywhere, all T | L-7 deprioritized |
| 28a-3 | E-1 Lichnerowicz Decomposition | **DIAGNOSTIC** | 84-95% of gap² from curvature in (1,0)/(0,1) | Context for BCS |
| 28a-4 | C-1 S_can vs S_LC | **CLOSED** | S_can monotone ↓, all smooth cutoffs | V-1 confirmed connection-independent |
| 28a-5 | C-4 Spectral Correlations | **DIAGNOSTIC** | q_can=0.28 vs q_K=0.16, weak signal | Needs higher irreps |
| 28a-6 | S-2 M_max vs C_2 Dispersion | **DIAGNOSTIC** | M_max ~ C_2^{-1.49}, μ_crit/λ_min ~ 0.95 | KC-2 phonon model |
| 28a-7 | E-4/S-1/L-4 Torsionful BCS | **MINOR PASS** | M_max(μ=0) = 0.529, 4.83× enhancement | 28b Landau diagnostics |

**Score: 1 PASS, 1 MINOR PASS, 2 CLOSES, 3 DIAGNOSTICS**

---

## II. DETAILED RESULTS

### 28a-1: KC-1 Parametric Injection Rate (Bogoliubov Coefficients) — PASS

The Jensen deformation generates real particle creation via the Parker mechanism. The adiabaticity parameter B_k measures the rate of parametric amplification per mode.

**Key numbers:**
- B_k at gap edge = 0.023 (threshold for PASS: > 0.01) — **2.3× above threshold**
- B_k max over all modes = 0.225 at τ=0.40, sector (3,3), ω=3.73
- Total multiplicity-weighted injection rate: Γ = 6,228 (τ=0.10) → 29,643 (τ=0.40)
- Adiabaticity ratio ω/|dω/dτ| minimum = 1.05–1.14 (weakly non-adiabatic regime)
- Zero modes cross the catastrophic creation threshold (ratio < 1), but 6,000–10,000 modes have ratio < 10

**Physical interpretation:** The evolving Jensen metric stretches eigenfrequencies at a rate that breaks adiabaticity for gap-edge modes. Higher-Casimir sectors (3,3), (2,3), (3,2) have the strongest injection (B_k up to 0.23), while gap-edge modes show moderate but above-threshold creation. Injection rate grows monotonically with τ. **The Constraint Chain gateway is open — KC-2 through KC-5 in Session 28c proceed.**

**Output**: `s28a_bogoliubov_coefficients.npz`, `s28a_bogoliubov_coefficients.png`

---

### 28a-2: L-1 Thermal Spectral Action — CLOSED

The finite-temperature free energy F(τ; T) = −T Σ_n ln(1 + exp(−|λ_n(τ)|/T)) is monotonically increasing at ALL temperatures tested.

**Key numbers:**
- F_ferm(τ; T): Monotonically INCREASING at all 10 temperatures (T/λ_min = 0.1 to 10.0)
- F_bos(τ; T): Monotonically INCREASING at all temperatures
- F_total(τ; T): Monotonically INCREASING at all temperatures
- Per-sector analysis (9 sectors): ALL sectors have minimum at τ=0 (boundary)
- Zero sign changes in dF/dτ across the entire (τ, T) plane

**Physical interpretation:** The Boltzmann weight exp(−|λ|/T) is a positive multiplicative factor that cannot flip the sign of dF/dτ. Thermal corrections inherit the monotonicity of the T=0 spectral action. This is structurally the same obstacle as Connes' theorem: the spectral action on a homogeneous space is a sum of individually monotone terms, and temperature weighting preserves monotonicity.

**The thermal stabilization channel is closed.** L-7 (self-consistent τ-T minimum) is deprioritized for 28b since L-1 provides no minimum to refine.

**Output**: `s28a_thermal_spectral_action.npz`, `s28a_thermal_spectral_action.png`

---

### 28a-3: E-1 Lichnerowicz Gap Decomposition — DIAGNOSTIC

Decomposes the spectral gap into algebraic (M_Lie) and curvature (Ω_LC + R/4) contributions using the Lichnerowicz formula D_K² = ∇*∇ + R/4.

**Key numbers:**

| Sector | Curvature fraction f_R = 1 − (gap_T/gap_K)² | Enhancement (gap_K/gap_T)² |
|:-------|:----------------------------------------------|:--------------------------|
| (0,0) | 1.00 (trivially — D_can = 0) | ∞ |
| (1,0)/(0,1) | 0.84 – 0.95 | 6.2 – 19.9× |
| (1,1) | 0.56 – 0.87 | 2.3 – 7.5× |

**Physical interpretation:** In the fundamental/anti-fundamental sectors, 84-95% of the D_K spectral gap² comes from the spin connection curvature. The algebraic Casimir (M_Lie) contributes only 5-16%. This explains quantitatively WHY D_can gaps are so much weaker. The maximum available enhancement of 19.9× at τ=0.50 exceeds the 7-13× needed to cross M=1, but the actual torsionful BCS (28a-7) found M_max = 0.529 — the BCS kernel depends on full matrix element structure, not just the gap.

**Tightness result:** R_contribution exceeds the scalar curvature bound R_K/4 everywhere in (1,0)/(0,1) sectors (tightness 1.17-1.35), meaning Ω_LC contributes beyond just the scalar endomorphism.

**Output**: `s28a_lichnerowicz.npz`, `s28a_lichnerowicz.png`

---

### 28a-4: C-1 Spectral Action S_can vs S_LC — CLOSED (V-1 TRANSFERS)

This was flagged as "the single most important number Session 28 can produce." The answer is definitive.

**Key numbers:**
- S_can(τ): **Monotonically DECREASING** under all smooth cutoffs (heat kernel, Lorentzian) at all Λ
- S_LC(τ): **Monotonically DECREASING** under all smooth cutoffs at all Λ
- Delta_S = S_can − S_LC: INCREASING at Λ ≥ 2 (S_can falls more slowly)
- S_can/S_LC ratio: 1.229 (τ=0) → 1.339 (τ=0.50) — monotonically increasing
- Sharp cutoff at Λ=1: Non-monotone (discretization artifact from eigenvalue crossing boundary)

**Physical interpretation:** The spectral action for BOTH the Levi-Civita and canonical-connection Dirac operators decreases monotonically with Jensen deformation. Removing the spin connection changes the scale (~23% larger for D_can) and rate of decrease (slower), but NOT the monotonic character. Connes' structural argument — "sum of monotone terms cannot have a minimum" — is connection-independent.

**V-1 (spectral action monotone, Session 24a) transfers to the torsionful sector.** The torsion channel for spectral action stabilization is CLOSED. Any τ-stabilization must come from outside the spectral action functional.

**Output**: `s28a_spectral_action_comparison.npz`, `s28a_spectral_action_comparison.png`

---

### 28a-5: C-4 Spectral Correlation R_2(s) — DIAGNOSTIC (WEAK SIGNAL)

Nearest-neighbor spacing statistics for D_can vs D_K, fit to the Brody distribution P(s) ~ s^q exp(−cs^{q+1}).

**Key numbers:**
- Mean Brody q for D_K: q_K = 0.156 ± 0.235 (near Poisson, q=0)
- Mean Brody q for D_can: q_can = 0.283 ± 0.231 (intermediate)
- D_can consistently shows slightly MORE level repulsion (Δq = +0.075)
- One crossover: sector (1,1) at τ=0.50 — D_K has q=0.000 (Poisson), D_can has q=0.734 (near-GOE)
- D_K shows non-monotonic pattern in (2,0)/(0,2): q peaks at τ~0.15 (q~0.65-0.78, near-GOE) then collapses to Poisson

**Statistical reliability warning:** Only 18-42 distinct eigenvalue levels per sector at max_pq_sum=3. Individual q values have large uncertainties. Aggregate trends are more reliable than single points. Definitive level statistics require max_pq_sum ≥ 6.

**Physical interpretation:** The spin connection (Ω_LC) in D_K introduces level clustering at large τ (toward Poisson). Removing it (D_can = M_Lie) preserves modest level repulsion. This is consistent with the physical picture: torsion has the opposite effect of the spin connection on spectral rigidity.

**Output**: `s28a_spectral_correlations.npz`, `s28a_spectral_correlations.png`

---

### 28a-6: S-2 M_max vs C_2 Dispersion Relation — DIAGNOSTIC (PHONON-LIKE)

Maps M_max across all 9 sectors as a function of the quadratic Casimir C_2(p,q).

**Key numbers:**
- At μ=0: M_max monotonically DECREASING with C_2 (phonon-like). (0,0) strongest (M=0.097), (3,0)/(0,3) weakest (M=0.047). All well below threshold.
- Power law: M_max ~ C_2^{−1.49} (steeper than 1/C_2)
- At μ=λ_min: NON-MONOTONIC. Singlet dominates (M=6.25–9.71). U-shape at intermediate C_2: dip at (2,0)/(0,2) then resurrection at (3,0)/(0,3).
- **Universal threshold: μ_crit/λ_min ~ 0.95 ± 0.05** across ALL sectors and ALL τ. BCS condensation requires μ within 5% of the spectral gap.
- At μ=1.2·λ_min: Singlet DROPS below threshold (M=0.68) while ALL other sectors become supercritical — an inversion effect.

**Physical interpretation:** The BCS instability is phonon-like in that lowest representations (longest wavelength modes on SU(3)) condense first. However, there is no acoustic branch — the dispersion is power-law decay, not linear. The universal μ_crit/λ_min ~ 0.95 threshold means the Constraint Chain question reduces to: can parametric amplification generate μ_eff ≥ 0.95·λ_min_can?

**Output**: `s28a_mmax_dispersion.npz`, `s28a_mmax_dispersion.png`

---

### 28a-7: E-4/S-1/L-4 Torsionful BCS — MINOR PASS

The single highest-priority computation of Session 28. Redoes the BCS gap equation using D_can eigenstates.

**Key numbers:**

| Quantity | D_can (torsionful) | D_K (Levi-Civita) | Enhancement |
|:---------|:-------------------|:-------------------|:------------|
| **M_max(μ=0), best** | **0.529** | 0.110 | **4.83×** |
| Best sector | (0,1) at τ=0.50 | (0,1) at τ=0.50 | — |
| M_max(μ=λ_min), best | 24.39 | 7.10 | 3.44× |
| Max enhancement at μ=λ_min | 24.39 | 1.89 | **12.88×** |

**Per-sector at μ=0:**

| Sector | M_can range [τ=0..0.50] | M_K range | Mean enhancement |
|:-------|:------------------------|:----------|:----------------|
| (1,0)/(0,1) | 0.162 – 0.529 | 0.060 – 0.110 | 3.51× |
| (1,1) | 0.086 – 0.294 | 0.049 – 0.085 | 2.47× |
| (2,0)/(0,2) | 0.078 – 0.255 | 0.048 – 0.092 | 2.12× |
| (3,0)/(0,3) | 0.052 – 0.167 | 0.039 – 0.083 | 1.64× |
| (2,1) | 0.056 – 0.181 | 0.040 – 0.070 | 1.91× |

**Enhancement grows monotonically with τ** because gap_can/gap_K decreases monotonically (from 0.40 at τ=0 to 0.224 at τ=0.50 in (0,1)).

**Cross-validation (all pass):**
- V_can ≠ V_K: V_diff = 0.012–0.121 (bases genuinely differ)
- Eigenvalue difference: 0.61–0.87 (spectra genuinely differ)
- D_K regression matches s27_multisector_bcs.npz at all overlapping τ
- λ ↔ −λ pairing symmetry at machine epsilon
- D_can anti-Hermiticity error < 10⁻¹⁴

**Physical interpretation:** Torsion provides ~5× enhancement through gap weakening (dominant) and basis rotation (secondary, ~30% effect). But 5× is not enough to bridge the 7-13× gap from K-1e. M_max(μ=0) = 0.529 is still 1.9× below threshold. The μ=0 obstruction survives the connection change.

**However:** At μ = λ_min_can, M_max = 24.39 — the D_can spectrum is strongly supercritical with even modest chemical potential. Combined with KC-1 PASS (parametric amplification generates real phonon injection), the Constraint Chain KC-2→KC-5 becomes the decisive test: can the Bogoliubov drive produce μ_eff ≥ 0.95·λ_min_can?

**Output**: `s28a_torsionful_bcs.npz`, `s28a_torsionful_bcs.png`

---

## III. SYNTHESIS

### What Session 28a Established

**The torsion story has two chapters:**
1. **Spectral action stabilization via torsion: CLOSED.** C-1 proves V-1 transfers to D_can. Both operators produce monotonically decreasing spectral actions. L-1 confirms thermal corrections cannot break this monotonicity. The connection choice is quantitative (23% scale change), not qualitative. This is the session's most important negative result.

2. **BCS condensation via torsion: ALIVE BUT CONDITIONAL.** E-4/S-1/L-4 shows D_can nearly quintuples M_max at μ=0 (0.110 → 0.529), but falls 1.9× short of threshold. The μ=0 obstruction survives. However, D_can is strongly supercritical at μ = λ_min (M=24.4), and KC-1 confirms the Jensen deformation generates real phonon injection with B_k = 0.023 at the gap edge. The question shifts entirely to: **can parametric amplification generate sufficient μ_eff?**

### The Decisive Path Forward

Session 28a has narrowed the framework's survival to a single quantitative question embedded in the Constraint Chain:

```
KC-1 (PASS) → KC-2 (T-matrix: does phonon scattering thermalize?)
            → KC-3 (μ_eff from kinetic equation: does μ_eff ≥ 0.95·λ_min?)
            → KC-4 (Luttinger K: does 1D fermionization create a Fermi surface?)
            → KC-5 (BCS with van Hove: does pairing survive?)
```

**If KC-3 delivers μ_eff ≥ 0.95·λ_min_can:** M_max > 1 in the D_can basis. BCS condensation occurs. Framework probability rises substantially from current 5% (panel) / 3% (Sagan).

**If KC-3 delivers μ_eff < 0.95·λ_min_can:** The BCS channel closes for both connections. The framework's last active mechanism dies.

### What Feeds Into Sessions 28b and 28c

| Result | Feeds Into | Status |
|:-------|:-----------|:-------|
| KC-1 PASS | 28c: KC-2 through KC-5 | **PROCEED** — Constraint Chain gateway open |
| L-1 CLOSED | 28b: L-7 self-consistent τ-T | **DEPRIORITIZED** — no minimum to refine |
| E-4/S-1/L-4 MINOR PASS | 28b: All Landau diagnostics on D_can | **PROCEED** — D_can is the relevant spectrum |
| C-1 CLOSED | 28b: C-3 order-one condition | Proceed independently (NCG axiom check) |
| S-2 phonon-like dispersion | 28c: KC-2 T-matrix | **SUPPORTS** phonon collision model |

### Updated Closed Mechanism Count

Session 28a adds 2 new closes:
- **Closure 19b**: L-1 thermal spectral action (extends V-1 to finite temperature)
- **Closure 19c**: C-1 S_can monotone (extends V-1 to canonical connection)

**Total closed mechanisms: 20** (18 prior + 2 new). Closure-to-pass ratio: 10:1.

---

## IV. OUTPUT FILES

| File | Computation | Gate |
|:-----|:-----------|:-----|
| `tier0-computation/s28a_bogoliubov_coefficients.py` | KC-1 script | PASS |
| `tier0-computation/s28a_bogoliubov_coefficients.npz` | KC-1 data | PASS |
| `tier0-computation/s28a_bogoliubov_coefficients.png` | KC-1 plot | PASS |
| `tier0-computation/s28a_thermal_spectral_action.py` | L-1 script | CLOSED |
| `tier0-computation/s28a_thermal_spectral_action.npz` | L-1 data | CLOSED |
| `tier0-computation/s28a_thermal_spectral_action.png` | L-1 plot | CLOSED |
| `tier0-computation/s28a_lichnerowicz_decomposition.py` | E-1 script | DIAGNOSTIC |
| `tier0-computation/s28a_lichnerowicz.npz` | E-1 data | DIAGNOSTIC |
| `tier0-computation/s28a_lichnerowicz.png` | E-1 plot | DIAGNOSTIC |
| `tier0-computation/s28a_spectral_action_comparison.py` | C-1 script | CLOSED |
| `tier0-computation/s28a_spectral_action_comparison.npz` | C-1 data | CLOSED |
| `tier0-computation/s28a_spectral_action_comparison.png` | C-1 plot | CLOSED |
| `tier0-computation/s28a_spectral_correlations.py` | C-4 script | DIAGNOSTIC |
| `tier0-computation/s28a_spectral_correlations.npz` | C-4 data | DIAGNOSTIC |
| `tier0-computation/s28a_spectral_correlations.png` | C-4 plot | DIAGNOSTIC |
| `tier0-computation/s28a_mmax_dispersion.py` | S-2 script | DIAGNOSTIC |
| `tier0-computation/s28a_mmax_dispersion.npz` | S-2 data | DIAGNOSTIC |
| `tier0-computation/s28a_mmax_dispersion.png` | S-2 plot | DIAGNOSTIC |
| `tier0-computation/s28a_torsionful_bcs.py` | E-4/S-1/L-4 script | MINOR PASS |
| `tier0-computation/s28a_torsionful_bcs.npz` | E-4/S-1/L-4 data | MINOR PASS |
| `tier0-computation/s28a_torsionful_bcs.png` | E-4/S-1/L-4 plot | MINOR PASS |
