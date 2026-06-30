# Session 85 Slot S-2 — K-Corridor Structural Geometry Phenomenology
## Solo Synthesis: 3He-B / K-STAR Inheritance Track

**Author**: volovik-superfluid-universe-theorist (solo, no coordination with landau)
**Date**: 2026-04-24
**Source inputs**: `session-85-w3-workingpaper.md`, `session-85-w2-workingpaper.md`, `session-85-w0-workingpaper.md` (+ cross-reference `session-85-w4-workingpaper.md` §W4-5 for INFO inheritance audit)
**Slot focus**: map the 3He-B/K-STAR analog inheritance across the K-corridor under the five W3 certifications; identify Leggett-mode analog of γ=1 lockout; mark BDI scope boundary.

---

## I. Session Outcome

The K-corridor `K ∈ [K_R5, K_FIRAS] = [1.9222, 3.556×10⁵]` is now certified as a **single mathematical object** by six W3 + W2 verdicts (W3-1, W3-4, W3-5, W3-6, W3-9, W2-12). Viewed through the 3He-B parent-child inheritance lens, the corridor is the substrate's laboratory-equivalent of the **Leggett-Bogoliubov response curve** parametrised by the reduced temperature variable `x = Δ/(2 T_eff)` with `K(x) = coth(x)`. The corridor's three named endpoints partition (x, K) into three physically distinct regimes:

| Endpoint | K-value | Substrate x | Inheritance regime |
|:---------|:-------:|:-----------:|:-------------------|
| `K_* = coth(1)` | 1.3130 | x* = 1 | Lab-framework anchor (S84 W5-58 PASS at 1.13%) |
| `K_R5` | 1.9222 | 0.5767 | Inflationary sub-corridor floor (R5/R6 boundary) |
| `K_crit_BdG` | 2.035 | 0.5491 | L1/L2 BdG band boundary → CMB ℓ = 1425 (W2-12) |
| `K_crit` | 91.5 | — (deep post-threshold) | Inflationary sub-corridor upper endpoint (R6/R7 branch point) |
| `K_FIRAS` | 3.556×10⁵ | γ=1 | PIXIE μ-distortion endpoint (R7 upper branch point) |

The corridor carries a 2-sheeted Riemann cover on [K_crit, K_FIRAS] (W3-6 PASS, genus-0, branch points exactly at the two endpoints). The γ=1 lockout pins `(1−γ) = 0` at `K_FIRAS`, which in the 3He-B language is the inheritance-dual of a **Leggett-mode resonance condition** where the longitudinal-NMR coupling `(chi_N/chi_B)` saturates to unity. The monodromy is `Z_2` around each branch point — inheritance carries it directly from the spin–isospin rotational structure of `H = SU(2)×U(1)×SO(2)` (W3-2).

**Key non-reclassified result**: the Landau-structural-block registered by W3-8 (BDI AZ class + 8 Goldstones + two-speed transfer + functorial regulator atlas under deep mean-field Ginzburg `Gi ~ 5.5×10⁻¹⁰`) inherits faithfully from 3He-B **on the inflationary sub-corridor only** `[K_R5, K_crit]`. The R6-R7 branch `[K_crit, K_FIRAS]` is Riemann-cover geometry the 3He-B parent does not possess (see §IV); that region is **inheritance-extension**, not inheritance-parent.

All gate verdicts are cited verbatim from source WPs (§III). I do not re-adjudicate.

---

## II. Key Results

### II.1 Lab-Cosmo Analog Table (3He-B phenomenon → cosmic-corridor observable → K-value)

**Classification**: PHONONIC (K-corridor is substrate Leggett-Bogoliubov response curve; both columns probe the same `D_K` spectrum).

**Framing note** (per `.claude/rules/phononic-framing.md`): 3He-B is the **parent**. Cosmic-corridor observables are **inheritance** of the same spectral-triple structure at ~60 OOM higher energy scale. This is not analogy; it is the same `D_K` eigenvalue problem realized on two vastly different internal-geometry scales. (See `framework-3heb-comparison.md` SHA `a0b2e378…`; `inheritance-inversion-60.md` SHA `5c77d0a6…`.)

| # | 3He-B laboratory phenomenon | Cosmic-corridor observable | K-value | Inheritance status | Gate |
|:-:|:----------------------------|:---------------------------|:--------|:-------------------|:-----|
| 1 | BCS gap opens at x = Δ/(2 T_eff) = 1 (reduced temp) | Substrate Leggett-Bogoliubov floor `K_*` | **1.3130** | PASS (1.13% lab-fw match) | S84 W5-58 |
| 2 | Inflationary sub-corridor threshold: Δ(K) = 0 at K_R5 | R5/R6 boundary (mean-field Landau threshold) | **1.9222** | PASS (β_BdG(K_R5)=0 structural) | S85 W3-3 |
| 3 | L1 (acoustic) / L2 (Leggett) BdG band boundary | BdG band boundary → CMB ℓ = 1425 in S4 window | **2.035** | PASS zero-parameter projection | S85 W2-12 |
| 4 | BdG dephasing amplitude β_BdG(K_1) | Bogoliubov mode-mixing rate at on-corridor K=10 | **10.0** | INFO (reg-spread PASS; exp 0.368 in INFO band) | S85 W3-3 |
| 5 | R6/R7 phase transition: sub-corridor upper endpoint, Δ(K_crit) = 3.17 M_KK | Inflationary sub-corridor upper endpoint (1st Riemann branch point) | **91.5** | PASS (Ginzburg Gi(K_crit)=5.5×10⁻¹⁰) | S85 W3-9 |
| 6 | Mean-field regime: Gi ≪ 1 (3He-B: Gi ≈ 10⁻⁷; substrate: 10⁻¹⁰) | Fluctuation-correction negligible across [K_R5, K_crit] | [1.9222, 91.5] | PASS (10-OOM margin) | S85 W3-9 |
| 7 | Longitudinal Leggett resonance `ω_L² = (4/5)(chi_N/chi_B) Δ²/ℏ²` saturation | PIXIE μ-distortion fixed point (regulator-swap Jacobian = 1) | **K_FIRAS = 3.556×10⁵** | PASS (μ = 8.69×10⁻⁵, 5-reg spread = 0) | S85 W3-1 |
| 8 | Z_2 monodromy around phase-transition branch (3He-B textures) | 2-sheeted Riemann cover, Ψ_+ ↔ Ψ_− on loop around K_crit or K_FIRAS | [91.5, 3.556×10⁵] | PASS (gap fraction 0.951) | S85 W3-6 |
| 9 | NMR-level lab accessibility: 3He-B Leggett spectroscopy at meV | CMB-S4 α_s access at k_pivot: d²S/dk² | — (joint) | INFO — FISHER row in W4-5 analog table | S85 W4-5 Row 0 |
| 10 | K-STAR tokamak density-cascade → turbulent zeroth spectral moment | DESI DR3 w_0 → a_0 Volovik partition | — (joint) | INFO — FIRST-PRINCIPLES-REASONING | S85 W4-5 Row 1 |

**Rows 1, 2, 3, 5, 6, 7, 8 are corridor-pinned by K-value** — each has a first-principles substitution chain identified in W3/W2 workingpapers.

**Rows 4, 9, 10 are corridor-crossed** — they track channels accessing the corridor rather than points on it. They depend on the same Landau structural block (W3-8) but are external to the K axis.

Rows 9 and 10 are **INFO per W4-5** because 2 of the 5 channels (LiteBIRD n_T ↔ 3He-B tensor-mode spectroscopy; 21-cm folded bispec ↔ K-STAR 3-pt correlations) carry `ANALOG-CANDIDATE-UNVERIFIED` status — laboratory-parameter match is not published. This is an inheritance-audit honesty signal, not a framework defect.

### II.2 Leggett-Mode Analog of the γ=1 Lockout

**The γ=1 lockout** (W3-1 structural reading): at `K_FIRAS`, the regulator-swap Jacobian `J_R,R'` collapses to unity by the identity `γ(K_FIRAS) = log(K_FIRAS/K_R5)/log(K_FIRAS/K_R5) = 1`, making μ(K_FIRAS) = 8.69×10⁻⁵ **exact across the 5-regulator atlas** (spread = 0 by construction).

**3He-B Leggett-mode analog: the `ω_L² → Ω_B²` saturation fixed point.**

Substitution chain (definition → substitution → simplification → direction):

1. **Definition** (from `framework-3HeB-comparison.md` and Volovik-Mineev NMR spectroscopy):

   `ω_L²(q) = Ω_B² + c_L² · q²`

   where `Ω_B² = (4/5)(chi_N/chi_B) Δ_B²/ℏ²` is the B-phase longitudinal NMR frequency squared (optic-like mode at q=0), chi_N is normal-state susceptibility, chi_B is B-phase susceptibility, c_L is Leggett-mode group velocity, Δ_B is B-phase gap.

2. **Substitution** — reduced temperature-ratio variable:

   Let `ξ_L = chi_N/chi_B`. Then `Ω_B²/Δ_B² = (4/5) ξ_L / ℏ²`. Define lab-dimensionless "gamma-lab":

   `γ_lab(T) ≡ log(chi_N/chi_B(T)) / log(chi_N/chi_B(0))`

   The chi_B(T) → 0 limit (T → 0, gap fully open) makes `γ_lab → 1` by construction; chi_B(T_c) = chi_N makes `γ_lab = 0`.

3. **Simplification**: the (1 − γ_lab) factor multiplies the regulator-dependent correction to `ω_L`. When γ_lab = 1 (at T → 0, bulk-limit Leggett resonance), the correction `δ_R · (1 − γ_lab)` vanishes for every convention R; the lab-measured `Ω_B²/Δ_B² = 4/5 · ξ_L(0)` is independent of the gap convention chosen (weak-coupling, strong-coupling, empirical fit).

4. **Direction** (the claim): γ_lab → 1 is the 3He-B version of the gate's `(1 − γ) = 0` at `K_FIRAS`. In both systems, the locked point is **the endpoint where the regulator-swap Jacobian saturates to unity** because the logarithmic scale variable crosses its defining denominator.

**Lab-correspondence table** (substrate-dual of W3-1 CC-3):

| Aspect | Cosmic corridor (W3-1) | 3He-B Leggett |
|:-------|:-----------------------|:--------------|
| Log variable | γ(K) = log(K/K_R5)/log(K_FIRAS/K_R5) | γ_lab(T) = log(chi_N/chi_B(T))/log(chi_N/chi_B(0)) |
| Lockout point | γ(K_FIRAS) = 1 | γ_lab(T → 0) = 1 |
| (1−γ) factor | multiplies δ_R regulator shift on μ(K) | multiplies δ_R regulator shift on ω_L² |
| Fixed-point observable | μ(K_FIRAS) = 8.694901×10⁻⁵ | Ω_B²(T=0) = (4/5) · ξ_L(0) · Δ_B(0)²/ℏ² |
| Regulator spread | 0 (exact) across 5-atlas | 0 (exact) across BCS gap conventions |

**Verified-numerics cross-check** (Sage, 2026-04-24):

```
γ(K_R5 = 1.9222)         = 0.000000    (1 − γ) = 1.000000
γ(K_* = 1.3130)          = −0.031428   (1 − γ) = 1.031428   [sub-floor; formally outside corridor]
γ(K_crit_BdG = 2.035)    = 0.004702    (1 − γ) = 0.995298
γ(K_1 = 10.0)            = 0.135975    (1 − γ) = 0.864025
γ(K_crit = 91.5)         = 0.318506    (1 − γ) = 0.681494
γ(K_FIRAS = 3.556×10⁵)   = 1.000000    (1 − γ) = 0.000000   ← lockout
```

**What this buys the framework**: PIXIE's μ(K_FIRAS) is not merely an external observation — it is the substrate's own analog of a Leggett-mode resonance at T = 0, the condensed-matter phenomenon where longitudinal NMR gives a convention-free gap readout. The 4-OOM separation from LCDM (μ_LCDM ~ 2×10⁻⁸) is the inheritance-dual of the resolvable meV-energy-scale gap between 3He-B Leggett frequency and Larmor frequency: same structural signature, detected at vastly different energy scales.

**Scope limit on the analog**: the direction Ω_B² → Ω_B² at T → 0 in 3He-B reflects *thermodynamic* gap saturation; the framework's `γ(K_FIRAS) = 1` is *spectral* (logarithmic variable saturating). Both are lockout-structured, but the 3He-B limit is a measurement limit (colder = cleaner), while the substrate limit is a pre-registered endpoint (K_FIRAS defined by W5-57). The physical content is shared (regulator Jacobian → 1); the physical cause is not interchangeable. (See framework-3heb-comparison.md Surprise Catalog, "adiabatic fabric" entry, for a prior instance of this parent vs child distinction.)

### II.3 BDI AZ-Class Scope: Which Regions Are Covered

**BDI AZ class** (W3-10 INFO, W5-66 INFO upstream): T² = +1, C² = +1, chiral S — certified at L_max = 10 on the **inflationary sub-corridor** `[K_R5, K_crit] = [1.9222, 91.5]`.

**Covered region** (inheritance from 3He-B holds quantitatively):

| Region | K-range | BDI coverage | Inheritance quality |
|:-------|:--------|:-------------|:--------------------|
| Sub-R5 tail | [K_*, K_R5) = [1.3130, 1.9222) | Covered (lab anchor) | K_* = coth(1) matches lab 1.13% (S84 W5-58) |
| Inflationary sub-corridor | [K_R5, K_crit] = [1.9222, 91.5] | **Fully covered** | W3-8 Landau structural block; Gi ≪ 1 (W3-9) |
| BdG L1/L2 boundary | K_crit_BdG = 2.035 | In-corridor point | W2-12 projects to ℓ=1425, zero-parameter |

**Outside BDI scope** (inheritance extends structurally, but the 3He-B parent lacks the relevant phenomenon):

| Region | K-range | BDI status | Parent mismatch |
|:-------|:--------|:-----------|:----------------|
| R6-R7 branch (Riemann cover) | (K_crit, K_FIRAS) = (91.5, 3.556×10⁵) | **Outside** | 2-sheeted cover with branch points is not a 3He-B feature; it is **inheritance-extension** (substrate has extra structure the parent doesn't) |
| Upper branch point | K_FIRAS = 3.556×10⁵ | **Outside** (lockout endpoint) | γ=1 lockout has lab analog (Ω_B² saturation, §II.2) but is not a 3He-B topological phenomenon |
| CP² sector (SU(3) - SU(2)×U(1)) | 4 broken generators (W3-2) | Covered by BDI | **No 3He-B analog** — CP² is framework-unique; SU(3) not SO(3)×U(1) |

**Substitution chain for coverage claim** (W3-9 direction argument):

1. Def: BDI coverage at K requires mean-field validity, i.e., `Gi(K) ≪ 1`.
2. Substitute (W3-9 algebra): `Gi(K) = 1.734×10⁻¹⁰ · (Δ(K)/M_KK)` where `Δ(K) = Δ_BCS · √((K − K_R5)/K_R5)`.
3. Simplify: `Gi(K_crit) = 1.734×10⁻¹⁰ · 3.169 = 5.497×10⁻¹⁰`.
4. Direction: Gi monotone-increasing in K on `[K_R5, K_crit]`; max at K_crit. For K > K_crit, Δ(K) grows further; but R6-R7 branch lives on the **Riemann-cover OP Ψ_±(K) = ±√((K−K_crit)(K_FIRAS−K))/N**, not the mean-field OP Δ(K). This is why W3-11 FAIL (multipole breakdown with Casimir cutoff) and W3-9 PASS (Ginzburg with c_fabric·M_KK cutoff) sit in tension — they use different cutoff ansätze. Both gates agree on the **direction**: mean-field Landau runs out of gas somewhere in the [K_crit, K_FIRAS] region, but the precise breakdown scale is model-dependent.

**Key insight from 3He-B parent**: 3He-B does not carry a Riemann-cover OP. The 3He-B order parameter `A_αi` lives on `SO(3)` × `SO(3)` / `SO(3)` (relative rotation of spin and orbital), which is a connected simply-connected manifold *after* quotienting (with discrete `π_0` giving textures). The substrate's `SU(3)` / `SU(2)×U(1)` quotient gives `CP²`, which is simply-connected; but the R6-R7 branch adds a **Spin(8) triality** (2,1) signature (W3-6 Structural reading) that the 3He-B parent does not possess — the substrate is *richer* than 3He-B in this specific respect.

**Per the inheritance-inversion-60 discussion**: this is an example where the substrate is parent to 3He-B (via idealized algebraic BCS limit) *within the inflationary sub-corridor only*. The R6-R7 branch extends into structure the real 3He-B does not have. Calling this "analogy breakdown" would be wrong — it is inheritance-extension. 3He-B is a *simplification* of the substrate in that region, missing the triality fold.

---

## III. Gate Verdicts (verbatim from source working papers)

**Rule**: gate verdicts from source WPs are authoritative. I cite them verbatim here and do not re-adjudicate. Conflicts with plan-prose are flagged.

### III.1 Inflationary-corridor certifications (the six W3/W2 PASS gates defining the K-corridor as one object)

| Gate ID | Status | Value | Scheme | Source WP line |
|:--------|:------:|:-----:|:-------|:---------------|
| `S85-W3-CF-5-PIXIE-KMFIRAS-PREREG` | **PASS** | 8.694901226608571×10⁻⁵ | canonical_heat_kernel, convention A, L_max=10 | W3 §W3-1 (line 17) |
| `S85-W3-CF-6-K-REGULATOR-MAP-THEOREM` | **PASS** | 2.550×10⁻¹⁶ (closure defect) | cross-regulator, convention A∪B, L_max=10 | W3 §W3-4 (line 151) |
| `S85-W3-CF-2-TWO-SPEED-TRANSFER-IDENTITY` | **PASS** | 0.0 exact | cross-regulator, convention A, L_max=10 | W3 §W3-5 (line 194) |
| `S85-W3-CF-3-MULTI-VALUED-LANDAU-OP` | **PASS** | 2 branch points | heat_kernel, convention A, L_max=10 | W3 §W3-6 (line 244) |
| `S85-W3-RUNNING-MASS-GINZBURG-OZ` | **PASS** | 5.497×10⁻¹⁰ (Gi at K_crit) | heat_kernel, convention A, L_max=10 | W3 §W3-9 (line 390) |
| `S85-W2-BAND-DETECTOR-MAP-LEGGETT-BOG` | **PASS** | ℓ_crit = 1424.50, T_LB = 0.112759 | BdG-to-CMB-ℓ transfer, zero-parameter | W2 §W2-12 (line 657) |

### III.2 Cross-session inheritance anchors

| Gate ID | Status | Value | Notes | Source |
|:--------|:------:|:-----:|:------|:-------|
| `S84-W5-58 K-Star-Lab-Framework-Match` | **PASS** | ratio = 0.01133 (1.13%) | K_* = coth(1) = 1.3130; lab 3He-B K = 1.3279 under Conv.A | `.claude/agent-memory/.../w5-58-k-star-lab-match-84.md` |
| `S85-W4-5-KSTAR-3HEB-LAB-INDEP` | **INFO** | 5/5 analogs named; 2/5 UNVERIFIED | 3 rows FISHER/FP, 2 rows ANALOG-CANDIDATE-UNVERIFIED | W4 §W4-5 (line 508) |

### III.3 Inheritance-edge (INFO/FAIL with structural content)

| Gate ID | Status | Value | Structural content |
|:--------|:------:|:-----:|:-------------------|
| `S85-W3-CF-4-BOGOLIUBOV-DEPHASING-AT-K` | **INFO** | β_BdG(K=10) = 0.5299; exp = 0.3685 | 3-reg spread < 1% PASS; Landau exponent INFO band [0.35, 0.65] (strong-pairing saturation); W3 §W3-3 (line 104) |
| `S85-W3-CF-7-R7-GOLDSTONE-EMERGENCE` | **INFO** | N = 8 (count PASS; plan 6+2+1=9 inconsistent) | CP² has 4 broken gens, not 6; plan arithmetic erratum; W3 §W3-2 (line 60) |
| `S85-W3-CF-1-BRANCH-A-A_S-CLOSURE-K2035` | **FAIL** | relerr = 0.571 (57%) | Framework A_s over-produces at all K on sub-corridor; strict band closed; W3 §W3-7 (line 289) |
| `S85-W3-MULTIPOLE-BREAKDOWN-SCAN` | **FAIL** | min L* = −1 | Casimir cutoff Λ=√(L_max+1)·M_KK contradicts W3-9 effective cutoff c_fabric·M_KK; model-dependent; W3 §W3-11 (line 499) |

### III.4 W0 plan-level conflicts flagged

- **W0-15 CC-vi**: `K_crit` plan value = 2.0446, `canonical_constants.K_crit` = 91.5; **INFO (plan-level flag)** per W0 §W0-15 line 1426. Gate verdict: FAIL (strict dispersion identity).
- **W2-12 `K_crit` symbol collision**: explicit carry-forward line 710 ("K_crit = 91.5 canonical vs K_crit_BdG = 2.035 plan-§W2-12"). This is a **real** collision — see §V below.
- **W0-17 K_floor + K_wall**: FAIL 0/5 — `K_floor` and `K_wall` constants missing from canonical_constants.py; W0 line 1537 uses K_R5 and K_crit as proxies.

---

## IV. Structural Implications

### IV.1 The corridor is a stratified Riemann surface with two branch points

W3-6 establishes that `Ψ(K)` on `[K_crit, K_FIRAS]` admits a 2-sheeted Riemann cover with branch points exactly at both endpoints. Genus-0, 2 sheets, Z_2 monodromy. Plus W3-1 establishes `γ(K_FIRAS) = 1` as a structural fixed point.

**Monodromy interpretation in superfluid-vacuum language**: traverse a closed loop in the complex K-plane encircling either `K_crit` or `K_FIRAS`. The order parameter flips sign: `Ψ_+ ↔ Ψ_−`. This is the substrate's implementation of a **half-quantum vortex (HQV)** sensibility: in 3He-B, half-quantum vortices exist as π-disclinations in the A-texture carrying Z_2 monodromy (Volovik-Mineev 1977 theorem; Onsager Prize 2014 result). The substrate Riemann cover is the spectral-triple dual of a HQV — the sign flip happens on the order-parameter sheet, not in spatial geometry.

**Inheritance caveat**: 3He-B proper has DIII topology (triplet pairing, C² = −1). The substrate is BDI (singlet-analog, C² = +1). HQV in 3He-B is real and observed (Volovik-Autti-Heikkinen experiments 2016). The substrate's HQV is **not** a literal half-quantum vortex — it is the spectral-analog realization, same Z_2 invariant and same monodromy group, but embedded in the spectral-triple structure rather than in 3D spatial geometry. This is the `N_3 = 0` vs `N_3 = 2` distinction (framework is 3He-B class not 3He-A class; see `n3-bdg-44-result.md`).

### IV.2 The two γ=1 lockouts as a bi-polar pair

Three algebraic facts:

- `γ(K_R5) = 0` by definition (logarithmic lower endpoint).
- `γ(K_FIRAS) = 1` by definition (logarithmic upper endpoint).
- `(1 − γ(K_R5)) = 1` (maximal regulator sensitivity at floor).
- `(1 − γ(K_FIRAS)) = 0` (zero regulator sensitivity at ceiling).

The corridor is **bi-polar**: maximal regulator-class dispersion at the lower endpoint, zero at the upper. This directly inherits the 3He-B phenomenon where BCS-gap-convention dependence is strongest near T_c (gap just opening, fit-function ambiguous) and vanishes at T → 0 (gap saturates to the universal 4/5 coefficient). W3-3 exp_fit = 0.3685 (at fit-range extending into strong-pairing regime where Δ/ξ_F rises to 2.05) is the quantitative echo: convention-sensitivity softens the exponent away from mean-field 0.5 precisely when the regulator-swap Jacobian is still active (low K end of corridor).

The lab 3He-B anchor `K_* = coth(1) = 1.3130` (S84 W5-58 PASS at 1.13%) sits structurally **below `K_R5`** — it is a sub-floor anchor from the BDI inheritance class, not a corridor point. This is consistent: the lab experiment pins the coupling `x = Δ/(2T_eff) = 1` at a reference temperature different from the cosmological-threshold K_R5 (which corresponds to x ≈ 0.577 = atanh(1/1.9222)). The anchor is the substrate's "unity-temperature" calibration; the corridor floor is the substrate's "pair-formation-threshold" calibration. Both inherit from 3He-B, but measure different aspects of the gap.

### IV.3 The BdG corridor and the inflationary corridor are two distinct K-corridors

Plan W2-12 uses `K_crit_BdG = 2.035`. Canonical_constants uses `K_crit = 91.5`. These are **different physical quantities** that share the token `K_crit`. W2 line 710 documents this collision explicitly. It is **not** a convention error — both are real physical endpoints — but it is a notational bug that will bite the next agent who imports `K_crit` and multiplies by `k_pivot × D_A` expecting 1425.

3He-B parallel: in the superfluid literature, the token `T_c` means at least two different temperatures (superfluid transition temperature ~ 2.5 mK, and Leggett-resonance saturation temperature T → 0). They are not interchangeable. The substrate has the same notational hazard in the K variable.

### IV.4 The Goldstone count 8 is inherited faithfully, but the dispersion breakdown is SU(3)-unique

W3-2 INFO: N_Goldstone = 8 via dim(G_cont)=13 − dim(H_cont)=5. Plan's 6+2+1 breakdown sums to 9 (arithmetic error; CP² has 4 broken gens, not 6). Framework-level breakdown: 4 CP² + 2 SO(3)/SO(2) + 1 U(1)_rel + 1 U(1)_T = 8.

**Inheritance split**:

- **3He-B-inherited** (2 SO(3)/SO(2) Goldstones): the 3He-B B-phase has 2 broken rotational generators (joint spin-orbital rotation), identical to our substrate's SO(3)/SO(2) coset. These 2 Goldstones are the inheritance.
- **SU(3)-unique** (4 CP² Goldstones): no 3He-B analog. The SU(3) → SU(2)×U(1) breaking generates CP² = SU(3)/(SU(2)×U(1)) with 4 real broken gens. These are NOT inherited; they are substrate-native.
- **U(1)_rel Goldstone** (1): analog of the 3He-B phase mode (Leggett-related, relative superfluid phase). Inherited.
- **U(1)_T Goldstone** (1): arises from U(1)_T (time-translation as continuous on G-side, broken to discrete on H-side). No simple 3He-B analog (in 3He-B, time-translation is unbroken in the normal state). This is substrate-native.

**BDI scope on the count**: BDI constrains the AZ symmetry (T² = +1, C² = +1, S). It does NOT constrain the coset-dimensional arithmetic. The Goldstone count 8 is consistent with BDI (AZ class is 0D symmetry; Goldstones are IR field content in d=3) but not forced by it. This is one of the scope boundaries: BDI covers the symmetry-class structure, not the dim(G/H) count.

### IV.5 Tension between W3-9 and W3-11 cutoffs is unresolved but not fatal

W3-9 uses effective cutoff Λ ≈ c_fabric·M_KK = 210·M_KK (gives Gi = 5.5×10⁻¹⁰, PASS by 10 OOM). W3-11 uses Casimir cutoff Λ = √(L_max+1)·M_KK = 3.32·M_KK (gives moment ratio 0.91, FAIL). Both are physically defensible.

**3He-B parent guidance**: in real 3He-B, the natural cutoff is the Fermi energy `E_F ≈ 1 K × k_B` (much larger than Δ ≈ 2 mK × k_B; ratio ~500). If the substrate inherits faithfully, the natural cutoff is the maximum D_K eigenvalue, which for Jensen-deformed SU(3) at L_max = 10 is ~M_KK times a "bandwidth factor". The W3-9 choice (c_fabric ≈ 210) approximates this; the W3-11 Casimir choice (√11 ≈ 3.3) is much more restrictive.

**Recommendation** (for S86 carry-forward): extract Λ_actual from the L_max=10 D_K spectrum directly. If Λ_actual / M_KK ≳ 100, W3-11 re-runs as PASS with huge margin, confirming the W3-9 picture. If Λ_actual / M_KK ~ 3, W3-11 FAIL is real and W3-9 Gi calculation over-estimates the cutoff. The 3He-B parent strongly suggests the former (Fermi-energy natural cutoff is what the spectrum itself provides), but the substrate must verify directly.

### IV.6 What I am explicitly NOT claiming

- **Not claiming** 3He-B IS the framework. It is the idealized algebraic parent; the substrate extends it via CP², Riemann covers, and Spin(8) triality.
- **Not claiming** γ=1 lockout and Ω_B² → (4/5) saturation are the **same physics**. They are inheritance-dual: same structural role (regulator-swap Jacobian → 1), different physical cause (spectral variable vs thermodynamic temperature).
- **Not claiming** the 2-sheeted Riemann cover is a half-quantum vortex in the literal 3He sense. Same Z_2 monodromy, but embedded in the spectral-triple order parameter, not in 3D spatial geometry. The substrate is BDI, not DIII.
- **Not claiming** the BDI AZ class covers the R6-R7 branch. W3-8's Landau structural block is explicit: `K ∈ [K_R5, K_crit]` only. The R6-R7 branch is outside BDI scope and is substrate-extension.

---

## V. Carry-Forward Computations (MANDATORY 4-field per `feedback_fix-in-session-never-defer.md`)

### V.1 K_crit symbol disambiguation (highest priority)

| Field | Content |
|:------|:--------|
| **What** | Promote `K_crit_BdG = 2.035` to canonical_constants.py with a distinct name (e.g. `K_L1L2_BdG` or `K_crit_bdg_boundary`); keep `K_crit = 91.5` for inflationary sub-corridor upper endpoint. Add provenance comments pointing to S85 W2-12 (BdG boundary) and S84 W5-55 (inflationary endpoint). Update W0-15 plan pin (`K_crit = 2.0446`) to use the disambiguated name or correct it to 2.035 if the plan intended the BdG quantity. |
| **Inputs** | `sessions/archive/session-85/session-85-w2-workingpaper.md` line 710 (explicit collision), `sessions/archive/session-85/session-85-w3-workingpaper.md` lines 157-159 (inflationary usage), `sessions/archive/session-85/session-85-w0-workingpaper.md` lines 1404, 1426, 1433 (plan-level conflict), `computations/canonical_constants.py` line 122. |
| **Gate** | Pre-register `CF-W2-12-K_crit-SYMBOL-DISAMBIG-S86` with PASS criterion: (i) canonical_constants.py contains both symbols with distinct names; (ii) no computation script imports `K_crit` and multiplies by `k_pivot × D_A` (i.e., no stale BdG uses hidden under the inflationary name); (iii) W0-15 plan K_crit value reconciled to one of `2.035` (BdG) or `91.5` (inflationary) or retracted. |
| **Effort** | **LIGHT** (canonical_constants.py PR + grep-audit downstream; ~2 hours). |

### V.2 γ=1 lockout ↔ Ω_B² saturation quantitative inheritance test

| Field | Content |
|:------|:--------|
| **What** | Compute the quantitative inheritance parameter `ξ_L_eff = chi_N/chi_B(0)` for the substrate analog of 3He-B's Leggett coefficient `(4/5)` via spectral-moment overlap at K_FIRAS. Test whether the substrate reproduces `ξ_L_eff = 4/5` at γ=1 lockout (inheritance PASS) or a different value (inheritance extension / BDI-specific tweak). Pre-register band: PASS if `|ξ_L_eff − 4/5| / (4/5) < 10%`; INFO if 10% to 50%; FAIL if > 50% (lockout not structurally 3He-B-equivalent). |
| **Inputs** | W3-1 PIXIE μ(K_FIRAS) = 8.694901×10⁻⁵ (the lockout observable); 3He-B `Ω_B²/Δ_B² = 4/5 × ξ_L/ℏ²` from Volovik-Mineev (`framework-3HeB-comparison.md`); D_K spectral moments at L_max=10 (existing cache from S84); substrate susceptibility ratio analog computed via `a_0` (Volovik partition moment) and `a_2` (Seeley-DeWitt). |
| **Gate** | Pre-register `CF-S2-GAMMA-LEGGETT-INHERITANCE-S86` as INFO-gate (pilot computation): (i) identify substrate analog of chi_N (a_0 or a_2 ratio?); (ii) compute at K_FIRAS under 5-regulator atlas (expect spread = 0 by lockout); (iii) compare to 4/5 reference. |
| **Effort** | **MODERATE** (ξ_L identification requires Volovik-partition cross-reference; computation is a spectral-moment ratio using existing D_K cache; ~1 day). |

### V.3 R6-R7 Riemann-cover HQV analog detection test

| Field | Content |
|:------|:--------|
| **What** | Test whether the Z_2 monodromy of the W3-6 Riemann cover corresponds to any observable half-quantum-vortex-like texture in the CP² sector of the order parameter. Pre-register direction claim: traversing a K-loop around K_crit should flip `Ψ_+ ↔ Ψ_−` (established W3-6); test whether this sign flip carries a CP²-texture signature (e.g., winding number in the 4 broken-gen subspace) that is physically distinguishable from a trivial phase. |
| **Inputs** | W3-6 artifact `computations/s85_w3_multi_valued_op_r6r7.npz` (Ψ_±(K) on 41 K-points); D_K eigenvector cache at L_max=10 restricted to CP² sector (needed); canonical `3He-B HQV` reference from Volovik-Mineev topological-defect classification (the Onsager Prize result). |
| **Gate** | Pre-register `CF-S2-R6R7-HQV-ANALOG-S86` as INFO-gate: (i) construct CP² Berry connection on the Riemann cover; (ii) integrate around K_crit and K_FIRAS; (iii) classify result as (a) trivial (no CP² content, monodromy is pure Ψ_± sign flip), (b) π-HQV-analog (half-integer winding in CP² subspace), (c) other. |
| **Effort** | **MODERATE-HEAVY** (requires CP² projector construction; GPU linalg on 155,984-eigenvalue cache; ~2 days). |

### V.4 BDI-inflationary-sub-corridor permanent-registry entry creation

| Field | Content |
|:------|:--------|
| **What** | Create `sessions/framework/permanent-results-registry.md` (currently absent; W3-8 and W3-10 both flagged this as a carry-forward) and land the Landau structural block as its first entry with the 7-field provenance from W3-10 PLUS a Volovik-track Addendum pinning the 3He-B inheritance scope boundary: [K_*, K_crit] inheritance faithful; (K_crit, K_FIRAS) inheritance-extension (substrate has Riemann-cover structure 3He-B lacks). |
| **Inputs** | W3-8 JSON `computations/s85_w3_consolidated_upgrade.json` (Landau block statement); W3-10 JSON `computations/s85_w3_landau_class_registry.json` (BDI 7-field entry); `framework-3heb-comparison.md` (22 correspondences, 16 surprises); `inheritance-inversion-60.md` (inheritance vs analogy distinction); `w5-58-k-star-lab-match-84.md` (K_* = coth(1) anchor). |
| **Gate** | Pre-register `CF-S2-REGISTRY-VOLOVIK-ADDENDUM-S86` as PASS if: (i) registry file created; (ii) Landau structural block entry contains the 7-field provenance; (iii) Volovik addendum identifies 4 inheritance-faithful Goldstones (2 SO(3)/SO(2) + 1 U(1)_rel + 1 U(1)_T or equivalent split) vs 4 substrate-native (4 CP²) and names the R6-R7 branch as inheritance-extension. |
| **Effort** | **LIGHT** (documentation; ~3 hours). |

### V.5 BDI inheritance scope audit against W4-5 UNVERIFIED rows

| Field | Content |
|:------|:--------|
| **What** | For the 2 UNVERIFIED rows of W4-5 (Row 2: LiteBIRD n_T ↔ 3He-B tensor-mode spectroscopy, LOW substrate-correlation; Row 4: 21-cm folded bispec ↔ K-STAR 3-pt correlations, MED), identify whether the lab-parameter-match obstruction is (a) experimental (the lab measurement has not been done with tensor-sector or 3-pt isolation) or (b) structural (the analog does not actually hold at the D_K eigenvalue-problem level). Classifier pre-registered: STRUCTURAL if the substrate-moment accessed by the lab differs from the substrate-moment accessed by the cosmological channel at the L_max=10 cache. |
| **Inputs** | W4-5 row table (W4 §W4-5 lines 519-523); L_max=10 D_K tensor-sector projectors (to construct); W4-5 analog script `computations/s85_w4_kstar_3heb_lab_indep.py`. |
| **Gate** | Pre-register `CF-S2-W4-5-UNVERIFIED-AUDIT-S86` as INFO or PASS: (i) tensor-mode substrate-moment identification for Row 2; (ii) 3-pt spectral moment substrate identification for Row 4; (iii) per-row classification STRUCTURAL vs EXPERIMENTAL. If STRUCTURAL, remove from the watchlist (analog does not hold); if EXPERIMENTAL, retain as UNVERIFIED with explicit lab-parameter target. |
| **Effort** | **MODERATE** (tensor-sector projector construction; ~1 day). |

### V.6 K_floor/K_wall canonical constants landing (W0-17 FAIL remediation)

| Field | Content |
|:------|:--------|
| **What** | W0-17 FAIL (0/5) records that `K_floor` and `K_wall` constants are missing from canonical_constants.py (W0 §W0-17, line 1537 uses K_R5 and K_crit as proxies). Land these as canonical constants with provenance. K_floor likely identifies with K_R5 (Volovik-inheritance "pairing floor") and K_wall likely identifies with K_crit (phase-boundary wall), but S85 did not verify the identification. |
| **Inputs** | W0-17 FAIL row; `canonical_constants.py` for K_R5 and K_crit current entries; W5 D.4 closure statement (if retrievable) or explicit definitions of K_floor and K_wall from session-85-plan-w5.md or source S84 WPs. |
| **Gate** | Pre-register `CF-S2-K-FLOOR-WALL-LAND-S86` as PASS if: (i) K_floor and K_wall land in canonical_constants.py with provenance; (ii) the identifications `K_floor = K_R5` and `K_wall = K_crit` are either verified (PASS) or refuted with distinct values (INFO flag, new investigation); (iii) W0-17 structurally re-runs as PASS with the landed constants. |
| **Effort** | **LIGHT-to-MODERATE** (depending on whether K_floor and K_wall are provably identical to K_R5 and K_crit, or require new computation). |

---

## VI. Summary Table

| Item | Status | Key result | Source |
|:-----|:------:|:-----------|:-------|
| Corridor as single object | CERTIFIED | 6 verdicts (W3-1, W3-4, W3-5, W3-6, W3-9, W2-12) pass | §III.1 |
| Lab-cosmo analog table | 10 rows | 7 corridor-pinned (3He-B/substrate), 3 channels (W4-5) | §II.1 |
| γ=1 lockout ↔ Leggett Ω_B² saturation | INHERITED (structural) | Lockout point is `χ_N/χ_B(T→0) = 1` or `K/K_FIRAS = 1`; regulator-swap Jacobian → 1 in both | §II.2 |
| γ=1 numeric verification | Sage-verified 2026-04-24 | γ(K_R5)=0, γ(K_FIRAS)=1, ratios on corridor pts | §II.2 |
| BDI AZ class scope | `[K_R5, K_crit]` only | Mean-field Ginzburg Gi ≪ 1 (10 OOM margin); R6-R7 branch outside scope | §II.3 |
| Monodromy interpretation (superfluid) | Z_2 HQV-analog | Spectral-triple dual of 3He HQV; BDI not DIII; no literal spatial vortex | §IV.1 |
| Bi-polar regulator sensitivity | Max at K_R5, zero at K_FIRAS | `(1−γ)` factor structures 3He-B-inherited gap-convention softening | §IV.2 |
| K_crit symbol collision | OPEN | 91.5 vs 2.035 vs 2.0446; 3 different referents share one name | §IV.3 + §V.1 |
| Goldstone split | 4 inherited + 4 substrate-native | 2 SO(3)/SO(2) + 1 U(1)_rel + 1 U(1)_T inherited; 4 CP² substrate-native | §IV.4 |
| W3-9 vs W3-11 cutoff tension | UNRESOLVED | c_fabric·M_KK (W3-9 PASS) vs √(L_max+1)·M_KK (W3-11 FAIL); 3He-B parent favors former | §IV.5 |
| Carry-forward items | 6 | §V.1-V.6; LIGHT to MODERATE-HEAVY effort | §V |

**Classifications (per `.claude/rules/phononic-framing.md`)**:
- §II.1 (analog table): **PHONONIC** (substrate excitations probing D_K spectrum)
- §II.2 (γ=1 lockout): **GEOMETRIC** (spectral-triple structural identity)
- §II.3 (BDI scope): **GEOMETRIC** (AZ-class topology of spectral-triple)
- §IV.1 (Riemann cover): **GEOMETRIC** (order-parameter topology)
- §IV.4 (Goldstone split): **PARTICLE** (representation-theoretic content of D_K)
- §IV.5 (cutoff tension): **NON-PHONONIC** (regularization ansatz choice)

**Author classification final**: the K-corridor synthesis is **PHONONIC + GEOMETRIC** — the corridor is the substrate's own Leggett-Bogoliubov response curve (phononic), organized by the Riemann-cover geometry of the Ψ_± order parameter (geometric). The 3He-B parent is a condensed-matter laboratory realization of the same spectral triple at ~60 OOM lower energy scale; inheritance is real, structural, and carries the specific caveats catalogued in §II.3 and §IV.6.

---

**End of Slot S-2 Volovik synthesis.**
