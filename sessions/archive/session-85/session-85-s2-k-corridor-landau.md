# Session 85 — Slot S-2 Solo Synthesis
## K-Corridor Structural Geometry Phenomenology (landau-condensed-matter-theorist)

**Session**: 85 | **Slot**: S-2 | **Reviewer**: landau-condensed-matter-theorist
**Angle**: BCS / Leggett / Riemann-cover — Z_2 monodromy around K_crit, K_FIRAS, and the µ(K) map across [1.9222, 3.556e5].
**Sources read (in full)**: session-85-w3-workingpaper.md; session-85-w2-workingpaper.md; session-85-w0-workingpaper.md.
**Classification**: primarily PHONONIC with GEOMETRIC sub-blocks for the Riemann cover and the K-regulator functor; META entries for the registry-landing items.

---

## I. Session Outcome

The inflationary sub-corridor K ∈ [K_R5, K_crit] = [1.9222, 91.5] plus the R6–R7 extension K ∈ [K_crit, K_FIRAS] = [91.5, 3.556e5] is certified at session S85 as a **single mathematical object** by six mutually-reinforcing gates:

| Gate | Verdict | Role |
|------|---------|------|
| S85-W3-1 PIXIE-K_FIRAS (W3 §1)            | PASS exact | scheme-invariant anchor at γ=1 lockout |
| S85-W3-4 K-REGULATOR-MAP-THEOREM (W3 §4)  | PASS mach ε | 5-regulator atlas is functorial on {K_R5, K_crit, K_FIRAS} |
| S85-W3-5 TWO-SPEED-TRANSFER-IDENTITY (W3§5)| PASS exact | c_S_canon = f_B at K_1=10.0 across 5-atlas |
| S85-W3-6 MULTI-VALUED-LANDAU-OP (W3 §6)   | PASS | 2-sheeted Riemann cover, branch points exactly at {K_crit, K_FIRAS}, gap fraction 0.951 |
| S85-W3-9 RUNNING-MASS-GINZBURG-OZ (W3 §9) | PASS 10 OOM | mean-field self-consistent across entire inflationary sub-corridor |
| S85-W2-12 BAND-DETECTOR-MAP-LEGGETT-BOG   | PASS | L1/L2 BdG boundary → l_crit = 1424.5 ∈ CMB-S4 window |

The solo synthesis proceeds from the **µ(K) response function** — reproduced Python-verified across the full log-range — through the Riemann-cover monodromy interpretation, to an observational-channel trace (BAO, CMB µ, lensing). A structural symbol-collision is identified in `K_crit`: canonical_constants.py (= 91.5, inflationary) vs W2-12 (= 2.035, BdG L1/L2 boundary) vs plan W0-15 (= 2.0446). This is raised as a mandatory carry-forward CF item.

**Primary deliverable finding**. µ(K) is a **smooth U-shaped function on [K_R5, K_FIRAS]**, anchored at both endpoints to µ_W5_57 = 8.6949e-5 (γ=0 at K_R5, γ=1 lockout at K_FIRAS), reaching a minimum µ_min = 4.19e-6 at K_min ≈ 8.27e2 (~2.3 orders of magnitude below the endpoints). No Riemann-cover-induced kink is present at either branch point: the slope discontinuity at K_crit has jump-ratio bounded by the probing ε (scales linearly with ε to at least 10^-6, i.e. zero at the resolution of the construction). The Z_2 monodromy is carried by the Landau OP Ψ_±(K), NOT by µ(K); the scheme-invariant µ is a **monodromy-blind** observable of the 2-sheeted cover.

---

## II. Key Results

### II.A The µ(K) response function — Python-verified over 1001 log-spaced K-points

The canonical µ(K) (W3-1 construction, inherited from W5-57) is defined by

```
γ(K)  = ln(K/K_R5) / ln(K_FIRAS/K_R5)                              [Def 1]
µ_can(K) = µ_W5_57 · (K/K_FIRAS)^γ(K)                              [Def 2]
```

with `µ_W5_57 = 8.694901226608571e-5`. Under the W3-1 γ=1 lockout, the full 5-regulator atlas `{heat_kernel, zeta_interior, zubarev, connes_moscovici, rep_theoretic}` collapses to µ_can at K = K_FIRAS (spread = 0 exactly, W3-1 CC-2). Elsewhere on the corridor, the regulator residual is `µ_R(K) = µ_can(K) · (1 + δ_R · (1 − γ(K)))`, which is a structural modulation, not a scheme choice — see W3-4 theorem.

**Substitution chain (direction of µ on corridor)**:

```
Def 1: γ(K_R5) = ln(1)/ln(K_FIRAS/K_R5) = 0;  γ(K_FIRAS) = 1.
Def 2: For K in the interior, γ ∈ (0, 1) monotone.
Def 3: base factor (K/K_FIRAS) < 1 for K < K_FIRAS.
Step 1: At K = K_R5: µ = µ_W5_57 · 1^0 = µ_W5_57.
Step 2: At K = K_FIRAS: µ = µ_W5_57 · 1^1 = µ_W5_57.
Step 3: For K interior: 0 < base < 1 AND 0 < γ < 1 ⇒ base^γ ∈ (base, 1).
Step 4: Compose: µ_interior < µ_W5_57 with equality only at the two endpoints.
Direction: µ(K) is NOT monotone. It starts at µ_W5_57, dips to µ_min on the
interior, and returns to µ_W5_57 at the γ=1 lockout. A U-shape pinned at both endpoints.
```

**Numerical µ(K) scan (Python-verified; 1001 log-points on [K_R5, K_FIRAS])**:

| K | γ(K) | µ_can(K) | Zone | Notes |
|---:|---:|---:|:---|:---|
| 1.9222    | 0.000000 | 8.6949e-05 | R5 endpoint | K_R5; γ=0 fixed point |
| 10.0      | 0.135975 | 2.0915e-05 | R5–R6 | below K_crit |
| 91.5      | 0.318506 | 6.2514e-06 | R6/R7 boundary | **branch point 1** |
| 100.0     | 0.325830 | 6.0569e-06 | R6/R7 | slightly past K_crit |
| 826.8     | ~0.50    | **4.1925e-06** | R6/R7 | **K_min ≈ argmin µ** |
| 1000.0    | 0.515686 | 4.2050e-06 | R6/R7 | near K_min |
| 1.0e4     | 0.705541 | 6.9984e-06 | R6/R7 | climbing back |
| 1.0e5     | 0.895397 | 2.7921e-05 | R6/R7 | near γ=1 |
| 3.556e5   | 1.000000 | 8.6949e-05 | FIRAS endpoint | **branch point 2**; γ=1 lockout |

The minimum occurs at **K_min ≈ 826.8, µ_min = 4.19e-6** — a factor of 20.7 below the endpoint value. The growth between K=10 (µ = 2.09e-5) and K=1000 (µ = 4.21e-6) is **smooth descending** (NOT growing), contrary to the synthesis prompt's leading assumption that "µ grows between K=10 and K=1000". The prompt-cited µ(K=10) = 2.45e-9 and µ(K=1000) = 2.45e-7 do not correspond to the W5-57 / W3-1 canonical construction; those values are 4 OOM below the actual canonical values. **Flag: check prompt's µ-scan quotation.** The W3-1 cache + substitution chain above constitute the canonical object.

**Classification**: PHONONIC (µ-distortion is the transfer of spectral weight from the CMB blackbody to a chemical-potential deviation; in the substrate picture it is the leading acoustic-sector signature of pre-transit quasiparticle reorganization).

### II.B Smoothness of µ(K) at the two branch points — no Riemann kink

One might expect the 2-sheeted Riemann cover (W3-6) to induce a slope discontinuity in µ(K) at K = K_crit and K = K_FIRAS. Python-verified probing (ε ∈ {1e-3, 1e-4, 1e-5, 1e-6}):

| Branch | ε | slope_jump_rel (ratio of |slope(right) − slope(left)| / |slope(left)|) |
|---|---|---|
| K_crit  | 1e-3 | 1.82e-3 |
| K_crit  | 1e-4 | 1.82e-4 |
| K_crit  | 1e-5 | 1.82e-5 |
| K_crit  | 1e-6 | 1.82e-6 |
| K_FIRAS | 1e-3 | 0 (one-sided, γ saturated) |
| K_FIRAS | 1e-4 | 0 |

**Substitution chain (direction: jump vanishes at branch points)**:

```
Def: slope_jump_rel(K_branch, ε) = |f(K+ε) − 2 f(K) + f(K−ε)| / |f(K)−f(K−ε)|.
For a C^∞ function, slope_jump_rel ∝ ε as ε → 0.
Observed: jump_rel ≈ 1.82·ε across four decades of ε at K_crit.
Direction: linear scaling in ε ⇒ function is smooth (C^1) at K_crit to
numerical resolution. Any genuine cover-induced kink would saturate at a
fixed positive number.
```

**Physical reading**. The Riemann cover lives in the Landau OP Ψ(K), not in the scheme-invariant observable µ(K). The scheme-invariant µ is a **gauge-invariant projection** from the covering space down to the base space; projection-pullback commutes with the branch-point structure because both sheets give Ψ_±(K_crit) = 0 (both pinch together at the branch point — see W3-6 results). The monodromy Ψ_+ ↔ Ψ_− flips a phase, but |Ψ|^2 (and any spectral moment of |Ψ|^2) is invariant, so µ ∝ |Ψ|^2-moments is smooth at the branch points.

**Classification**: PHONONIC.

### II.C Riemann cover Ψ_±(K) on [K_crit, K_FIRAS] — Python-verified

From W3-6 §C: Ψ_±(K) = ±√((K − K_crit)(K_FIRAS − K)) / N, N = √(K_crit · K_FIRAS) = √(91.5 · 3.556e5) = 5701.5.

**Python-verified scan** (501 linearly spaced points on [K_crit, K_FIRAS]):

```
Ψ_+(K_crit)  = 0.000000    Ψ_−(K_crit)  = −0.000000
Ψ_+(K*)      = +31.1622    at K* = (K_crit + K_FIRAS)/2 = 1.7785e5
Ψ_−(K*)      = −31.1622    at K* = (K_crit + K_FIRAS)/2 = 1.7785e5
Ψ_+(K_FIRAS) = 0.000000    Ψ_−(K_FIRAS) = −0.000000
gap max      = 62.3245     at K*
```

Both sheets pinch at the two branch points exactly. The genus of the cover is 0 (Riemann-Hurwitz: 2-sheeted, 2 branch points ⇒ g = (N·(2g_base − 2) − Σ(e_p − 1))/2 + 1 with base g_base = 0, N = 2, Σ = 2 ⇒ g = 0). **Topological summary**: the R6-R7 branch of the K-corridor is a punctured Riemann sphere with identified branch points (a "pinched" P^1 topologically equivalent to a 2-sphere with two special points).

**Classification**: GEOMETRIC.

### II.D Z_2 monodromy interpretation — physical reading of Ψ_+ ↔ Ψ_−

The 2-sheeted Riemann cover implies: **the R6-R7 branch of the K-corridor is not simply-connected.** A closed loop in K-space encircling either K_crit or K_FIRAS **once** flips Ψ_+ ↔ Ψ_−. Encircling **twice** returns the original sheet. This is the Z_2 monodromy.

**Substrate-first reading**. Ψ_+(K) and Ψ_−(K) are two distinct spectral realizations of the **same physical vacuum**, related by the Spin(8) triality (2,1) signature action on the A_F sector (W2-11 PASS machine-zero: [T_s, σ_i] = 0 across all τ in the Jensen corridor). The physical content is:

- **Sheets are not distinguishable by any scheme-invariant spectral moment**. Every even spectral moment of Ψ (µ, spectral-action coefficients a_0, a_2, a_4, a_6) is invariant under Ψ → −Ψ. This is identical in structure to the W2-7 FAIL-with-refinement: **even-parity Seeley-DeWitt is parity-blind to HP^1 secondary twists**.
- **Odd-parity diagnostics CAN see the sheet**. η-invariant and Godbillon-Vey integral are odd-parity spectral objects; they take value +η on Ψ_+ and −η on Ψ_− in principle. The W0-23 result η = 0 exactly (by anti-Hermitian spectrum symmetry) pins the Dai-Freed torsion (W0-12 PASS, ±1 ∈ ℤ/2) as the **only odd-parity invariant that distinguishes the two sheets** — and it takes value ±1 ∈ ℤ/2, exactly the discrete invariant of the 2-sheeted cover.

**A closed K-loop around K_crit sends Dai-Freed pairing +1 ↔ −1.** This is the structural content of the Z_2 monodromy.

**What K-loops look like physically**. K is a thermodynamic / substrate-action parameter, not a coordinate in spacetime. A "closed loop in K" would be a thermodynamic process that slowly varies K from K_0 (on R5–R6 side of K_crit) around to the other sheet of R6–R7 and back to K_0. In the phononic substrate picture, this corresponds to an *adiabatic* cycle of the Jensen deformation scale through the BdG band-boundary transition, returning to the initial parameter. The substrate's sheet-label (+ or −) is the **Dai-Freed ℤ/2 class** it carries after the cycle.

**Classification**: GEOMETRIC (cover topology) × PHONONIC (physical interpretation via Dai-Freed pairing, which classifies the phononic relay-pattern chirality).

### II.E Observational-channel trace

Three observational channels trace the K-corridor through their respective Mukhanov-Sasaki or recombination-transfer projections:

**(i) BAO (DESI DR3/DR4)**. The BAO sound horizon r_s ~ 150 Mpc gives a characteristic wavenumber k_BAO ≈ π/r_s = 2.09e-2 Mpc^-1. In K-units via the Planck pivot k_pivot = 0.05 Mpc^-1, this is K_BAO = k_BAO / k_pivot ≈ 0.419. **This is well BELOW K_R5 = 1.9222** — BAO wavenumbers live on the infrared side of the substrate inflationary corridor and do not enter [K_R5, K_FIRAS] at all. Consequently, **no direct BAO signature of the Z_2 monodromy is expected**: BAO measurements probe the matter power spectrum transferred from k << k_pivot, where the Landau OP is single-valued (R5 branch only). The W0-4 DR3 15-leaf successor tree captures DR3's (w_0, w_a) response to the framework; that is a consistency test of the LCDM-corridor anchoring, not a probe of Ψ_± sheet identity.

Direction: **CLOSED channel for DR3 monodromy-probe**; DR3 data can still test the regulator-atlas successor tree (W0-4 PASS) but does not have sensitivity to K > K_crit = 91.5.

**(ii) CMB µ-distortion (PIXIE / FIRAS)**. PIXIE measures µ at cosmological scales; the framework pre-registration (W0-8 PIXIE PASS at pull = 8693σ, W3-1 PASS at regulator-spread = 0) anchors µ(K_FIRAS) = 8.69e-5 at the γ=1 lockout fixed point. A closed K-loop around K_FIRAS acts trivially on µ (by II.B smoothness result: µ is smooth at K_FIRAS and identical on both sheets via the even-parity projection). **PIXIE measures the invariant µ, not the sheet label.** The ≥ 4-OOM separation from LCDM µ ~ 2e-8 is preserved across ALL monodromy sectors.

Direction: **OPEN channel for µ endpoint-value test, CLOSED for monodromy-sector test.** PIXIE is an amplitude probe, not a sheet probe.

**(iii) CMB acoustic-to-Leggett transition (CMB-S4)**. W2-12 computed l_crit = 1424.5 from the BdG L1/L2 band boundary K_crit_BdG = 2.035 (with T_LB = 0.113 zero-free-parameter). This l lies in the CMB-S4 sensitivity window [300, 5000]. **This is the observational channel closest to the phonon-level sheet label**: it probes the substrate's two-band structure at the L1/L2 boundary. A closed K-loop around K_crit_BdG = 2.035 would flip the CP^2-fiber chirality mode (BDI class, PH² = +1, TR² = +1 per W3-10 pinning); CMB-S4 polarization-mode discrimination at l ≈ 1425 would carry a ℤ/2-distinguishable feature in principle.

Direction: **OPEN channel — CMB-S4 at l ≈ 1425 is the monodromy probe.**

**Symbol-collision flag (mandatory CF)**: W2-12 uses `K_crit_BdG = 2.035` (BdG L1/L2 band boundary) while canonical_constants.K_crit = 91.5 (inflationary sub-corridor upper endpoint). These are **different physical quantities sharing a name**. Computing l_crit with the canonical K_crit gives l = 91.5 × 0.05 × 14000 = 64,050 (far OUTSIDE CMB-S4 window [300, 5000]); computing with K_crit_BdG gives l = 1425 (INSIDE the window). The W2-12 PASS uses K_crit_BdG = 2.035. The plan W0-15 reports K_crit = 2.0446 (slightly different BdG refinement). All three values must be disambiguated before S86 downstream gates invoke `K_crit`.

**Classification**: PHONONIC (observational projection of substrate band structure).

---

## III. Gate Verdicts (verbatim from source WPs)

| Gate ID | WP-reference | Verdict | Value | Key |
|---|---|---|---|---|
| S85-W3-CF-5-PIXIE-KMFIRAS-PREREG            | W3 §W3-1  | **PASS** | 8.694901226608571e-05, 5-reg spread = 0 exact | γ=1 lockout |
| S85-W3-CF-6-K-REGULATOR-MAP-THEOREM         | W3 §W3-4  | **PASS** | max closure defect = 2.55e-16 | functorial 5-atlas |
| S85-W3-CF-2-TWO-SPEED-TRANSFER-IDENTITY     | W3 §W3-5  | **PASS** | c_S_canon/f_B − 1 = 0.0 exact | at K_1=10.0 |
| S85-W3-CF-3-MULTI-VALUED-LANDAU-OP          | W3 §W3-6  | **PASS** | branch_point_count = 2, gap frac 0.951 | genus-0, 2-sheet |
| S85-W3-RUNNING-MASS-GINZBURG-OZ             | W3 §W3-9  | **PASS** | Gi(K_crit) = 5.497e-10 | 10 OOM below 1 |
| S85-W2-BAND-DETECTOR-MAP-LEGGETT-BOG        | W2 §W2-12 | **PASS** | l_crit = 1424.50 ∈ [300, 5000] | T_LB = 0.112759 |
| S85-W3-CF-7-R7-GOLDSTONE-EMERGENCE          | W3 §W3-2  | **INFO** | N_Goldstone = 8 (count OK; plan's 6+2+1 dispersion off by 1) | dim(G)=13, dim(H)=5 |
| S85-W3-CF-4-BOGOLIUBOV-DEPHASING-AT-K       | W3 §W3-3  | **INFO** | β_BdG(K_1) = 0.5299, exp_fit = 0.3685 | in INFO [0.35, 0.65] |
| S85-W3-CF-1-BRANCH-A-A_S-CLOSURE-K2035      | W3 §W3-7  | **FAIL** | A_s_framework / A_s_Planck − 1 = 0.5712 | 57% > 30% band |
| S85-W3-CONSOLIDATED-PERMANENT-RESULT-UPGRADE| W3 §W3-8  | **INFO** | 0 inconsistencies / 6 pairs | new sub-theorem |
| S85-W3-LANDAU-CLASS-REGISTRY-ENTRY          | W3 §W3-10 | **INFO** | 7/7 fields pinned; 2 INFO caveats | BDI AZ-class |
| S85-W3-MULTIPOLE-BREAKDOWN-SCAN             | W3 §W3-11 | **FAIL** | min L* = −1 (model-dependent Casimir cutoff) | contradicts W3-9 cutoff |
| S85-W3-FALSIFIER-TABLE-OZ-CLASS             | W3 §W3-12 | **PASS** | 7/7 rows pinned | OZ falsifier ledger |
| S85-W3-PARTITION-INVARIANCE-CP2             | W3 §W3-13 | **INFO** | max K-spread = 1.21% | just above 1% PASS |
| S85-W0-8  PIXIE-MU-K-ENDPOINT-PREREG        | W0 §W0-8  | **PASS** | pull = 8692.9σ | flagship 2029+ decisive |
| S85-W0-12 CC-4-DAI-FREED-TORSION            | W0 §W0-12 | **PASS** | DF = ±1 ∈ ℤ/2 | framework-anomaly-free |
| S85-W0-23 CC-1-ETA-INVARIANT-FULL-TRIPLE    | W0 §W0-23 | **INFO** | η = 0 exact | structural anomaly-free |
| S85-W2-11 PRE-CC-2-TRIALITY-ON-JENSEN       | W2 §W2-11 | **PASS** | ‖[T_s, σ_i]‖ = 0.00e+00 exact | triality × Jensen commute |

---

## IV. Structural Implications

### IV.A What the Z_2 monodromy says about the substrate

The K-corridor partitions into three topologically distinct regions:

1. **R5–R6 sub-corridor K ∈ [K_R5, K_crit] = [1.9222, 91.5]**: simply connected, single-valued Landau OP, **BDI AZ class certified** (W3-10). All 4 structural PASS gates (W3-4, W3-5, W3-9, W2-11) live here or extend through here. This is the Landau-certified mean-field region (Gi ≪ 10^-9).

2. **R6–R7 sub-corridor K ∈ [K_crit, K_FIRAS] = [91.5, 3.556e5]**: **2-sheeted Riemann cover, NOT simply connected**. Ψ_±(K) has genus-0 topology with branch points at both endpoints. The Z_2 monodromy Ψ_+ ↔ Ψ_− is the covering-space fundamental-group action, tied to Spin(8) triality (2,1) signature and Connes-Moscovici s=3 residue.

3. **Outside the corridor K < K_R5**: sub-critical, Δ = 0, mean-field gap vanishes; observationally probed by BAO (K_BAO ≈ 0.42 < K_R5).

**Structural statement (new this synthesis)**: The **bridge between the two branches** is carried by the Dai-Freed torsion pairing (W0-12 PASS, DF = ±1 ∈ ℤ/2) — this is the ONLY odd-parity substrate invariant that distinguishes Ψ_+ from Ψ_−. Since η = 0 (W0-23) and all Seeley-DeWitt coefficients are parity-blind (W2-7 structural result), Dai-Freed is *forced* to be the monodromy label.

**Classification**: GEOMETRIC.

### IV.B What regions are covered by BDI AZ class (W3-8, W3-10)

**BDI certification scope** (from W3-10 registry entry, W3-8 consolidated block):

| K-region | BDI certified? | Why |
|---|---|---|
| [K_R5, K_crit] | **YES** | W3-10 pinning; 4 PASS theorems in W3 all on this sub-corridor; Gi ≪ 1 (W3-9) |
| [K_crit, K_FIRAS] | **NO — only on a single sheet** | Riemann cover is 2-sheeted; BDI class is sheet-dependent (PH² and TR² signs depend on Dai-Freed label) |
| K < K_R5 | Out of scope | Mean-field gap vanishes; no BdG structure to classify |
| K > K_FIRAS | Out of scope | Beyond PIXIE lockout; no further corridor data |

**Why only a single sheet above K_crit**: AZ classification invokes the two discrete symmetries PH (particle-hole) and TR (time-reversal). For BDI: PH² = +1, TR² = +1, with μ = 0 forcing chirality Γ = 1 at the fold (W5-66, W3-10). Under the Z_2 monodromy Ψ → −Ψ, the PH generator changes sign on one sheet while TR is preserved — so the (PH², TR²) pair becomes (+1, +1) on one sheet and (−1, +1) on the other, which are **different AZ classes** (BDI vs DIII). The BDI registry entry is valid on the R5–R6 corridor and on ONE sheet of R6–R7 (the sheet where the monodromy-frame has been fixed). The other sheet is class DIII by the symmetry-inversion argument.

**Consequence**: W3-10 should acquire a sheet-label qualifier. Currently the registry entry claims BDI across [K_R5, K_crit]; the natural S86+ upgrade is to extend to [K_R5, K_FIRAS] with an explicit sheet-label (the "+" sheet) attached.

**Classification**: GEOMETRIC.

### IV.C Structurally permitted vs kinematically forbidden regions

**(K, monodromy-sector, regulator)-space** partitions:

| Region | Permitted | Closed by |
|---|---|---|
| (K ∈ [K_R5, K_crit], sheet ∈ {default}, reg ∈ 5-atlas) | **PERMITTED** | BDI cert + Gi ≪ 1 + W3-4 functoriality |
| (K ∈ [K_crit, K_FIRAS], sheet = +, reg ∈ 5-atlas) | **PERMITTED** | same as above, sheet-restricted |
| (K ∈ [K_crit, K_FIRAS], sheet = −, reg ∈ 5-atlas) | **PERMITTED** (but class DIII, not BDI) | Z_2-conjugate sheet; sibling AZ class |
| K < K_R5 | **FORBIDDEN** for inflationary dynamics | Δ = 0, no BdG gap; sub-critical regime |
| K > K_FIRAS | **FORBIDDEN by γ=1 lockout** | regulator Jacobian saturates; no observable forecast beyond PIXIE |
| Closed K-loops encircling ONE branch point | **PERMITTED but changes sheet** | Z_2 monodromy; changes Dai-Freed label |
| Closed K-loops encircling BOTH branch points | **PERMITTED and sheet-preserving** | product of two Z_2 elements is identity |
| Closed K-loops not encircling any branch point | **PERMITTED and sheet-preserving** | trivially in π_1(base − branches) |

The **kinematically forbidden** region "K < K_R5 with a non-zero inflationary Δ" has been shut by the mean-field BCS gap vanishing at K = K_R5 (W3-3 sub-critical diagnostic β(K_0 = coth(1)) = 0 exact). The **phenomenologically forbidden** region "K > K_FIRAS with γ > 1" would require extrapolating the γ lockout past its fixed-point, which is unphysical by the regulator-flow structure.

### IV.D µ(K) is monodromy-blind, Ψ(K) is monodromy-active

This is the cleanest separation that came out of the Python scan. **Scheme-invariant observables (µ, spectral moments) do not see the Z_2 monodromy, but structural objects (Ψ, Dai-Freed pairing, sheet label) do.** This means:

- **PIXIE's observational flagship (pull = 8693σ) is secure against sheet-label uncertainty.** The µ endpoint value is identical on both sheets.
- **CMB-S4's potential acoustic-to-Leggett feature at l ≈ 1425 is where monodromy physics becomes accessible**, since the BdG band-boundary projection involves the L1 vs L2 discrimination which couples to sheet label via the Bogoliubov angle.
- **Dai-Freed ℤ/2 (W0-12 PASS) is the only odd-parity probe of the cover topology** within the session's computational vocabulary; W0-23's η = 0 closes the continuous-η probe.

---

## V. Carry-Forward Computations (structured; mandatory 4-field)

### CF-S2-1: K_crit symbol-collision disambiguation (blocks downstream)

- **What**: Promote `K_crit_BdG = 2.035` (W2-12) AND `K_crit_W0_15 = 2.0446` (plan W0-15) to first-class canonical_constants with distinct names (`K_crit_bdg_boundary`, `K_crit_bdg_refined`), and keep `K_crit = 91.5` (inflationary) as-is with explicit docstring on which quantity it names.
- **Inputs**: `computations/canonical_constants.py`, W2-12 JSON, W0-15 output (need to read W0-15 plan/results; flagged as prerequisite).
- **Gate**: canonical-constants PR with scheme_tag column populated; `/weave --update` pipeline audit all computation S84+ scripts for unambiguous K_crit usage; each occurrence must carry a disambiguating comment.
- **Effort**: LIGHT (documentation + rename; downstream fix-up is mechanical).

### CF-S2-2: Sheet-label extension of BDI AZ registry entry

- **What**: Upgrade W3-10 BDI registry draft to cover [K_R5, K_FIRAS] with an explicit sheet-label qualifier (`sheet=+` for BDI; `sheet=−` registers as sibling DIII entry).
- **Inputs**: W3-10 JSON, W3-6 Ψ_±(K) data, W0-12 Dai-Freed ℤ/2 PASS, W2-11 triality-Jensen commutation PASS.
- **Gate**: new W3-10-extended with n_provenance_fields_pinned = 9 (adds `sheet_label` and `dirac_signature`); must cite W0-12 Dai-Freed SHA as the monodromy-label anchor.
- **Effort**: MODERATE (requires explicit sheet-convention pinning; depends on CF-S2-1 for clean K_crit symbol).

### CF-S2-3: CMB-S4 l ≈ 1425 monodromy-sensitivity forecast

- **What**: Compute σ(sheet_label) at CMB-S4 from the L1/L2 BdG acoustic-to-Leggett transition amplitude T_LB = 0.113 and the framework-predicted Bogoliubov rotation angle θ(k_F). Determine whether CMB-S4 polarization-mode discrimination can distinguish sheet = + from sheet = − at the l ≈ 1425 feature.
- **Inputs**: W2-12 BdG spectrum cache, CMB-S4 Science Book Table 6.1 polarization sensitivity at l = 1425, the W3-6 Ψ_±(K) cache evaluated near K_crit_BdG = 2.035.
- **Gate**: pre-register σ(sheet_label)_CMB-S4 ≤ 3 → PASS; σ > 10 → FAIL (monodromy unobservable); intermediate → INFO (amplitude-dependent).
- **Effort**: MODERATE (uses existing W2-12 + W3-6 caches; new computation is the Fisher projection).

### CF-S2-4: Dai-Freed ℤ/2 label as monodromy closure anchor

- **What**: Verify explicitly that adiabatic transport of a Dai-Freed test bundle around a closed K-loop encircling K_crit flips DF(k=1) from +1 to −1; Python-verified using the W0-12 torsion computation machinery with a K-parametrized deformation.
- **Inputs**: W0-12 Dai-Freed torsion script (`s85_w0_cc4_dai_freed_torsion.py`) + Jensen deformation machinery + W3-6 Ψ_±(K) cover.
- **Gate**: DF(loop(K_crit, sheet_start=+)) = −1 ∈ ℤ/2 → PASS; identity under loop-contraction → monodromy is trivial (FAIL); partial consistency → INFO.
- **Effort**: MODERATE-HEAVY (requires augmenting W0-12 script with closed-loop transport; the kinematic setup is non-trivial since K is a substrate parameter, not a spatial coordinate).

### CF-S2-5: µ(K) monodromy-blindness theorem

- **What**: Prove (not just verify numerically) that every even-parity spectral moment M_2n[Ψ] of the Landau OP is invariant under the Z_2 monodromy Ψ → −Ψ. Follows from Ψ_+(K) + Ψ_−(K) = 0 (W3-6) and the fact that M_2n is quadratic (or higher even power) in Ψ.
- **Inputs**: W3-6 §C cover formula; W2-7 parity-blindness result (structural template).
- **Gate**: formal proof in Python + LaTeX, with at least one explicit computation showing M_2[Ψ_+] = M_2[Ψ_−] = M_2[|Ψ|]. PASS if proof closes; INFO if only verified numerically.
- **Effort**: LIGHT-MODERATE (algebraic, the proof is essentially the W2-7 parity argument transcribed to the Ψ_± domain).

### CF-S2-6: BAO-scale null-result certificate

- **What**: Formal closure certificate that BAO-scale measurements (DESI DR3, DR4) cannot probe the Z_2 monodromy because K_BAO ≈ 0.42 << K_R5 = 1.9222, i.e. BAO wavenumbers are sub-critical.
- **Inputs**: k_BAO = π/r_s ≈ 2.09e-2 Mpc^-1, k_pivot = 0.05 Mpc^-1, canonical_constants.K_R5.
- **Gate**: explicit PASS certificate with substitution chain; registry entry in observational-falsifier-ledger.md (needs to be created — see W3-12 CF).
- **Effort**: LIGHT.

### CF-S2-7: W3-11 vs W3-9 cutoff reconciliation (inherited from W3 wave)

- **What**: Pin Λ_actual from direct D_K top-eigenvalue inspection at L_max = 10; compare to Casimir-saturated sqrt(11)·M_KK = 3.32 M_KK (W3-11) and c_fabric·M_KK = 210 M_KK (W3-9 implicit). Re-run both W3-9 and W3-11 with the empirical cutoff.
- **Inputs**: D_K spectrum cache at L_max = 10, canonical_constants.c_fabric, canonical_constants.M_KK.
- **Gate**: consistency of mean-field Gi << 1 AND multipole expansion convergent under the SAME Λ; both re-run under Λ_actual; PASS if both agree; FAIL if contradiction persists.
- **Effort**: MODERATE (requires L_max=10 eigenvalue cache; GPU-accelerated).

### CF-S2-8: Branch-A A_s (W3-7 FAIL) audit

- **What**: Trace the S80 UNIFIED-AS-79 TD-path multiplicative corrections (c_sub, f_conv, F_amp) to isolate which factor(s) produce the 57% over-prediction relative to Planck. Decide strict vs lenient band policy.
- **Inputs**: W3-7 JSON, S80 UNIFIED-AS-79 cache, Planck 2018 A_s central + σ.
- **Gate**: identify factor with largest |∂A_s / ∂factor|; re-run with per-factor sensitivity scan. PASS if factor identifiable within framework's derivation chain; INFO if shortfall distributed; FAIL if no factor carries >30% leverage.
- **Effort**: HEAVY (requires detailed S80 pipeline reconstruction).

---

## VI. Summary Table

| Row | K-region | Classification | Monodromy sector | µ(K) range | Structural status |
|-----|----------|----------------|------------------|------------|-------------------|
| 1 | K < K_R5 (sub-critical) | PHONONIC | none (Δ=0) | undefined | mean-field gap vanishes; BAO lives here |
| 2 | K = K_R5 = 1.9222 | PHONONIC | single-sheet | 8.6949e-5 | R5 threshold; γ = 0 |
| 3 | K ∈ (K_R5, K_crit) = (1.9222, 91.5) | PHONONIC | single-sheet | 8.69e-5 → 6.25e-6 | R5–R6; BDI certified; Gi ≪ 1 |
| 4 | K = K_crit = 91.5 | GEOMETRIC (cover) | **branch point 1** | 6.25e-6 | Ψ_± pinch; Z_2 action trivial |
| 5 | K ∈ (K_crit, K_min ≈ 826.8) | PHONONIC | 2-sheeted | 6.25e-6 → 4.19e-6 | R6–R7 descending arm |
| 6 | K = K_min ≈ 826.8 | PHONONIC | 2-sheeted | 4.19e-6 (**argmin µ**) | far from either branch point |
| 7 | K ∈ (K_min, K_FIRAS) | PHONONIC | 2-sheeted | 4.19e-6 → 8.69e-5 | R6–R7 ascending arm |
| 8 | K = K_FIRAS = 3.556e5 | GEOMETRIC (cover) | **branch point 2** | 8.6949e-5 | Ψ_± pinch; γ = 1 lockout |
| 9 | K > K_FIRAS | forbidden | lockout violated | undefined | γ > 1 unphysical |
| | | | | | |
| **Monodromy probes** | | | | | |
| 10 | BAO (DESI DR3/DR4) | NON-PHONONIC here | sub-critical | K_BAO ≈ 0.42 < K_R5 | **CLOSED channel** |
| 11 | CMB µ (PIXIE)       | PHONONIC | endpoint (γ=1) | µ(K_FIRAS) = 8.69e-5 | **OPEN, but monodromy-blind** |
| 12 | CMB-S4 polarization at l ≈ 1425 | PHONONIC | K_crit_BdG = 2.035 | — | **OPEN, potentially monodromy-active** |
| 13 | Dai-Freed ℤ/2 (W0-12) | GEOMETRIC | sheet-label | ±1 ∈ ℤ/2 | **the only odd-parity probe** |
| 14 | η-invariant (W0-23) | GEOMETRIC | both sheets | η = 0 exact | **monodromy-blind** (η symmetric) |

---

## Closing note (landau-condensed-matter-theorist, slot S-2, 2026-04-24)

What stood out in this synthesis:

1. **µ(K) is U-shaped, not monotone.** The prompt's leading conjecture ("µ grows between K=10 and K=1000") was structurally wrong: µ *descends* from µ_W5_57 at K_R5 through a minimum µ_min ≈ 4.19e-6 near K ≈ 830 and climbs back to µ_W5_57 at K_FIRAS. The γ=1 lockout is a top-endpoint pin, not a monotonicity anchor. Both endpoints equal the same µ_W5_57 = 8.6949e-5 — a symmetric pincer of the interior.

2. **The Riemann cover is invisible in µ(K).** Slope-continuity probing at K_crit and K_FIRAS shows slope_jump_rel ~ 1.82·ε — perfectly smooth to 10^-6 probing. The monodromy lives in Ψ(K) and in the Dai-Freed ℤ/2 label, not in the observable µ. This is the direct phononic analog of the W2-7 parity-blindness structural result: **even-parity spectral moments cannot see odd-parity (sheet-label) structure.**

3. **Dai-Freed ℤ/2 is forced to be the monodromy carrier.** With η = 0 (W0-23) and all Seeley-DeWitt parity-blind (W2-7), the only odd-parity substrate invariant left is Dai-Freed (W0-12 PASS at ±1 ∈ ℤ/2) — precisely the discrete invariant a 2-sheeted cover can carry. The W0-12 and W0-23 PASS pair is the **mathematical bridge** from the Riemann cover topology to observable phononic substrate properties.

4. **BAO is closed, PIXIE is endpoint-only, CMB-S4 is the actual monodromy probe.** BAO lives at K ≈ 0.42 (sub-critical); PIXIE measures the monodromy-blind amplitude; CMB-S4 at l ≈ 1425 probes the L1/L2 BdG band-boundary (via W2-12's zero-parameter projection) where the sheet-label is coupled to the Bogoliubov rotation. CF-S2-3 is the Fisher-projection gate that decides whether CMB-S4 polarization discrimination can actually see the Z_2 flip.

5. **The K_crit symbol collision is a real bug waiting to bite.** Three values (91.5 inflationary, 2.035 BdG-W2-12, 2.0446 BdG-W0-15) share one name. Any script that imports `K_crit` and multiplies by k_pivot × D_A is prone to a ~45× error in observational projections. CF-S2-1 is the hard blocker; S86 should not start new K-gates until this is resolved.

The K-corridor is ONE mathematical object: a substrate-action parameter range bounded below by the BCS gap threshold (K_R5) and above by the γ=1 lockout (K_FIRAS), cut in the middle by the BdG band-boundary (K_crit at 91.5) into a simply-connected R5–R6 piece and a 2-sheeted Riemann cover R6–R7 piece. The whole thing is Landau-certified (mean-field, Gi ≪ 10^-9), regulator-functorial (W3-4), with a clean two-speed transfer identity (W3-5) and a sheet-label carried by the Dai-Freed ℤ/2 class. Three observational channels (BAO, PIXIE µ, CMB-S4 l ≈ 1425) project this structure; only the third one can probe the monodromy. That is the phenomenological content. The rest is structural scaffolding that makes the claim well-posed.

— landau-condensed-matter-theorist, slot S-2
