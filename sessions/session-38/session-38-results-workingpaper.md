# Session 38 Results Working Paper

**Date**: 2026-03-08
**Format**: Workshop-focused (3 workshops x 2 rounds) + 7 targeted computations
**Master Gate**: CC-INST-38
**Pre-38 Probability**: 5-8% (spectral action route, structural floor)
**Paradigm**: Transit physics, not equilibrium. Instanton gas, not static BCS.

---

## Instructions for Contributing Agents

**Write your results in your designated section below.** Each section has a header with your agent name and computation ID. Include:

1. **Gate verdict** (PASS/FAIL/CONSISTENT/CLOSED) with the pre-registered criterion
2. **Key numbers** (the 3-5 most important quantitative results)
3. **Cross-checks** performed and their outcomes
4. **Data files** produced (paths relative to project root)
5. **Assessment** (2-3 sentences on what the result means)

Do NOT write outside your designated section. Do NOT modify other agents' sections.

---

## Session 38 Context

Session 37 established:
- **Structural Monotonicity Theorem**: S_f(tau) has no minimum for any monotone cutoff. PERMANENT.
- **Dense instanton gas**: S_inst=0.069, tunneling 93%, L/xi_GL=0.031 (0D limit)
- **Giant pair vibration**: omega=0.792, 85.5% strength, coherence 6.3x
- **BCS-BEC crossover**: E_vac/E_cond=28.8, fluctuations dominate 29x
- **F.5 wrong sign**: BdG shift +12.76 vs E_cond -0.137 (static condensate)
- **K7-G1 algebraic closure**: PMNS from (p,0)/(0,q) sectors impossible

Session 38 asks: what does the instanton gas DO during transit through the fold? And is the gas Chaotic or Ordered.

---

## Workshop W0: CC-Through-Instanton (Einstein x Nazarewicz)

**Output**: `sessions/session-38/session-38-einstein-naz-workshop.md`
**Gate**: CC-INST-38

### W0 Gate Verdict: CC-INST-38

**CC-INST-38: F.5 SURVIVES (CLOSED, 76x margin)**

| Measurement | Value | Status |
|:------------|:------|:-------|
| <Delta^2>/Delta_0^2 (T=0.05) | 1.431 | 130x above 0.011 threshold |
| <Delta^2>/Delta_0^2 (T=0.20) | 2.508 | 228x above threshold |
| min(<Delta^2>/Delta_0^2) | 0.831 (T=0.004) | 76x above threshold |
| <delta_S_BdG>_inst (T=0.05) | 22.45 | 2.2x LARGER than static |
| <delta_S_BdG>_inst (T=1.00) | 205.33 | 19.7x LARGER than static |
| Ratio instanton/static BdG | 2.2x to 83.8x | STRENGTHENED anti-trapping |
| F.5 sign status | **SURVIVES** | Instanton averaging makes it worse |

### W0 Key Conclusions

1. **<Delta^2>/Delta_0^2 >= 0.83** is a thermodynamic identity for double-well potentials. 76x above the 0.011 reversal threshold at all T.
2. **Instanton averaging STRENGTHENS F.5 wrong-sign.** BdG shift grows from 10.4 (static) to 22-872 (instanton-averaged). More fluctuations = larger penalty.
3. **Extensivity mismatch persists.** 8 BCS modes vs 155,984 total. Gradient shortfall 2,840x.
4. **Spectral action is the wrong functional for BCS.** It penalizes the eigenvalue shift that pairing requires. Structural sign mismatch.
5. **Remaining open path: FRIEDMANN-BCS-38** — coupled dynamics with BCS back-reaction (not spectral action). Current shortfall 38,600x.

---

## Workshop W1: "The Pair Vibrator as a Phonon" (Nazarewicz x QA)

**Output**: `sessions/session-38/session-38-naz-qa-workshop.md`
**Agents**: nazarewicz + quantum-acoustics-theorist

### W1 Summary

The GPV at omega_PV = 0.792 is NOT a phonon — it is a **collective pair vibration** (pair-transfer mode, Delta_N = +/-2) of the B2 flat optical band, analogous to the nuclear giant pair vibration. It survives the 443x quench as a resonance because integrability (C-5/C-6) prevents thermalization — anomalous from nuclear perspective where giant resonances dissolve above T ~ 3-4 MeV. Post-quench GPV retains 50-70% strength, frequency shift < 7.3%, Q > 5 (underdamped). Parametric amplification (omega_att/omega_PV = 1.81 near 2:1) is kinematically forbidden (2.6e-4 pump cycles during transit). Domain wall localization excluded (PT-RATIO-35 + 0D). Post-quench state is GGE, not thermal. GPE must use BdG equations (not scalar GPE). KK spin of pair-transfer operator on SU(3) is an OPEN QUESTION.

| Question | Answer | Status |
|:---------|:-------|:-------|
| What 4D field does the GPV become under KK reduction? | Massive pair-transfer scalar at 0.792 * M_KK, carries K_7 = +/-1/2. KK spin (scalar/vector/tensor) OPEN | PARTIAL |
| Is omega=0.792 related to a physical mass? | Yes: m_GPV ~ 0.792 * M_KK (GUT scale). Post-quench shift < 7.3% | ANSWERED |
| Connection to 1D Poschl-Teller bound states? | EXCLUDED — PT-RATIO-35 (18x short) + 0D limit (no walls). GPV is bulk, spatially uniform | CLOSED |
| 4D observer interpretation of pair vibration spectrum? | GGE with GPV pole broadened but present (Q>5). Pair-removal scalar at 0.137*M_KK is lightest mode | ANSWERED |

---

## Workshop W2: "Instanton Resonance" (Nazarewicz x Tesla)

**Output**: `sessions/session-38/session-38-naz-tesla-workshop.md`
**Agents**: nazarewicz + tesla-resonance

### W2 Summary

S_inst = 0.069 is NOT tunneling — it is a **quantum critical point** where the BCS order parameter undergoes large-amplitude pair vibration in the Z_2-restored phase. The barrier (0.0047) is 0.4% of one oscillation quantum; WKB is invalid (1/S ~ 14.5). No nuclear system has S < 1. Closest analog: backbending band crossing in ^158Er (S_eff ~ 0.1-0.3). The frequency hierarchy omega_tau >> omega_att > omega_PV >> Gamma_L is a universal **BCS four-scale architecture** (not SU(3) representation theory), mapping onto E_breathing >> omega_0 > omega_PV >> Gamma_decay in nuclear physics. Nuclear analog: deformed ^24Mg (sd-shell, shape coexistence), not ^16O. Inverted Born-Oppenheimer confirmed (Kapitza = 0.030, matches SD band decay ^152Dy). Q-factor = 2.86 (doorway state regime). Pair-removal/B3-B2 near-resonance at 2.9% detuning is fully hybridized (Feshbach doorway, V >> delta_E). omega_att = 9*(B3-B1) at 0.08% accuracy is OPEN — tau-sweep needed to determine if algebraic theorem or flat-band-stabilized coincidence.

| Question | Answer | Status |
|:---------|:-------|:-------|
| Attempt frequency in spectral units? | omega_att = 1.430, 9th harmonic of B-sector span (0.08%). Fully geometric, no free parameters | ANSWERED |
| Resonance condition with SU(3) harmonics? | omega_att = 9*(B3-B1), omega_PV = 6*(B3-B2). Structural vs coincidental requires tau-sweep | OPEN |
| Kapitza ratio Gamma_inst/omega_tau significance? | 0.030 = inverted Born-Oppenheimer. Geometry fast (33x), pairing slow. SD band decay analog | ANSWERED |
| Tunneling rate derivable from geometry alone? | YES. Full chain g_ij -> D_K -> BCS -> omega_att. No free parameters (C-3) | ANSWERED |

---

## Workshop W3: "Kibble-Zurek at the Fold" (Landau x Hawking)

**Output**: `sessions/session-38/session-38-landau-hawking-workshop.md`
**Agents**: landau + hawking

### W3 Summary

The transit through the fold is a **Parker-type cosmological particle creation event** (no horizon, NOT Hawking radiation). The sudden quench (tau_Q/tau_0 = 8.7e-4) destroys the BCS condensate and creates 59.8 quasiparticle pairs with near-maximal occupation (n_Bog = 0.999 per mode) in a **non-thermal GGE distribution** with 8 Richardson-Gaudin conserved integrals. The GGE is the unique, deterministic outcome of unitary evolution from the BCS ground state -- a prediction, not a fit.

Central structural result: the **Schwinger-instanton identity** S_Schwinger = S_inst (0.070 = 0.069) -- the Euclidean tunneling action and Lorentzian pair creation exponent are the same WKB integral through the BdG gap. The instanton gas IS the pair creation viewed in Euclidean time. Proposed as provable theorem (SCHWINGER-INST-38).

Key R2 correction: the NG mode **ceases to exist** post-transit (not "liberated"). Cooper pairs are K_7-neutral; no Higgs mechanism; no condensate = no phase fluctuation. Post-transit has fewer collective degrees of freedom. U(1)_7 restored.

Backreaction is perturbative (3.7%). Excitations are **cosmologically permanent** via three-layer protection (Richardson-Gaudin integrability + block-diagonal theorem + suppressed 4D coupling). This is the only known particle creation mechanism producing a permanent non-thermal relic. The transit is "preheating without reheating" -- energy injected but never thermalizes.

| Question | Answer | Status |
|:---------|:-------|:-------|
| What does the 4D observer see? | Spatially uniform energy injection: 59.8 massive KK quasiparticle pairs, non-thermal GGE, no defects | ANSWERED |
| Bogoliubov pair creation as particle production? | Yes -- Parker-type (no horizon). Schwinger exponent = instanton action (0.070 = 0.069) | ANSWERED |
| Post-quench state from 4D? | GGE with 8 conserved integrals. Inverted spectrum (quasi-uniform occupation). Pure state, S_ent <= 5.55 bits | ANSWERED |
| U(1)_7 restoration? | YES. NG mode ceases to exist. Fewer collective DOF post-transit | ANSWERED |
| Effective Hawking temperature? | Does not exist. Mode-dependent T_eff,k nearly degenerate (sudden limit). Non-thermal | ANSWERED |
| Cosmological stability? | Permanent. Three-layer integrability protection. GGE parameters are cosmological constants | ANSWERED |

Open gates: GGE-LAMBDA-38 (compute 8 Lagrange multipliers, HIGH), KK-MASS-38 (4D mass spectrum, HIGH), SCHWINGER-INST-38 (prove identity analytically, MEDIUM), INFO-ENT-38 (entanglement entropy, LOW).

---

## Targeted Computations

### C-1: <Delta^2> from MC Data [ZERO-COST]

**Agent**: nazarewicz
**Status**: COMPLETE
**Gate**: CC-INST-38 (input)
**Input**: `tier0-computation/s37_instanton_mc.npz`
**Data**: `tier0-computation/s38_cc_instanton.npz`

| Measurement | T=0.05 | T=0.20 | T=1.00 | T=5.00 |
|:------------|:-------|:-------|:-------|:-------|
| <Delta^2>/Delta_0^2 | 1.431 | 2.508 | 5.228 | 11.335 |
| <\|Delta\|>/Delta_0 | 1.024 | 1.343 | 1.930 | 2.836 |
| f(\|Delta\| < 0.1*Delta_0) | 4.82% | 3.86% | 2.75% | 1.89% |

Full temperature sweep (12 points, T = 0.001 to 10.0):
- Minimum <Delta^2>/Delta_0^2 = **0.831** at T = 0.004 (low-T quantum limit)
- <Delta^2>/Delta_0^2 increases monotonically above T = 0.004
- At ALL temperatures: <Delta^2>/Delta_0^2 >> 0.011 (F.5 sign reversal threshold)
- Time near Delta=0 is always < 5% -- the system spends most time near +/-Delta_0

**Assessment**: The instanton gas does NOT suppress <Delta^2>. The fluctuations ADD to the mean-square gap (because both +Delta_0 and -Delta_0 contribute positively to <Delta^2>). The minimum ratio 0.831 at T=0.004 is 76x above the 0.011 threshold needed to reverse F.5. The F.5 wrong-sign verdict SURVIVES in the instanton gas with overwhelming margin.

---

### C-2: Instanton-Averaged BdG Shift [LOW-COST]

**Agent**: nazarewicz (computed within W0)
**Status**: COMPLETE
**Gate**: CC-INST-38 (secondary)
**Input**: Dirac eigenvalues at fold + MC <Delta^2> from C-1
**Data**: `tier0-computation/s38_cc_instanton.npz`

| Quantity | T=0.05 | T=0.20 | T=1.00 | T=5.00 |
|:---------|:-------|:-------|:-------|:-------|
| <delta_S_BdG>_inst | 22.45 | 56.30 | 205.33 | 872.46 |
| Ratio to static (12.76) | 1.76x | 4.41x | 16.09x | 68.36x |
| Ratio to GL static (10.43) | 2.15x | 5.41x | 19.71x | 83.76x |

Tau sweep (at T=1.0, 9 tau values from 0 to 0.5):
- <delta_S_BdG>_inst peaks at tau = 0.20 (fold): 205.33
- Static delta_S_BdG peaks at tau = 0.20: 27.18
- Instanton averaging AMPLIFIES the BdG shift by 7.5x at the fold
- Gradient shortfall: dS_fold = 61,899 vs d_inst/dtau = 21.8 -> shortfall 2,840x

| Summary Quantity | Value |
|:---------|:------|
| <delta_S_BdG>_inst (T=0.05) | 22.45 (1.76x LARGER than static) |
| <delta_S_BdG>_inst (T=1.00) | 205.33 (16.1x LARGER than static) |
| Static delta_S_BdG | +12.76 |
| Sign of net effect | **ANTI-TRAPPING** (instanton makes F.5 worse) |
| Gradient shortfall | 2,840x (instanton correction vs spectral action gradient) |

**Assessment**: Instanton averaging STRENGTHENS the F.5 wrong-sign effect, not weakens it. The time-averaged BdG shift is 1.8x to 68x LARGER than the static value because <Delta^2> > Delta_0^2 at all temperatures. The instanton correction to the spectral action gradient is 2,840x too small to create a minimum. The entire class of "spectral action + BCS correction" approaches to tau stabilization is now closed.

---

### C-3: Attempt Frequency Extraction [ZERO-COST]

**Agent**: nazarewicz
**Status**: COMPLETE
**Input**: `tier0-computation/s37_instanton_action.npz`, `s37_pair_susceptibility.npz`, `s31Ba_instanton_kapitza.npz`, `s38_cc_instanton.npz`

#### Method

The S37 instanton action S_inst = 0.069 was computed via S_inst = integral sqrt(2 * F_BCS(Delta)) dDelta, which implicitly sets m_eff = 1 in the GL kinetic term. The attempt frequency must be extracted from the SAME energy landscape for self-consistency:

omega_att = sqrt(F_BCS''(Delta_0))    [m_eff = 1, self-consistent with S_inst]

The GL quartic approximation F ~ a*Delta^2 + b*Delta^4 gives S_inst_A = 0.287 (4.2x larger than numerical S_inst = 0.069) because the quartic overestimates the barrier width. However, the curvature at the MINIMUM agrees to 2.5% between GL and full BCS because the minimum is the expansion point. The discrepancy in S_inst comes from the barrier region (Delta near 0) where the quartic fails.

#### Primary Results

| Quantity | Value | Uncertainty |
|:---------|:------|:------------|
| omega_att (BCS, PRIMARY) | 1.430 | +/- 0.019 (1.3%) |
| omega_att (GL quartic) | 1.449 | -- |
| omega_PV (pair vibration) | 0.792 | exact (from ED) |
| omega_barrier (BCS) | 1.175 | -- |
| omega_tau (modulus at fold) | 8.269 | -- |
| Gamma_Langer | 0.250 | -- |
| Gamma_simple | 1.335 | -- |
| exp(-S_inst) | 0.934 | -- |

#### Frequency Hierarchy

| Frequency | Value | Physical meaning |
|:----------|:------|:----------------|
| omega_tau | 8.269 | Jensen metric oscillation at fold |
| 2*E_B2 | 1.691 | Pair-breaking threshold |
| omega_att | 1.430 | BCS attempt frequency (PRIMARY) |
| omega_barrier | 1.175 | Barrier-top instability rate |
| E_B2 | 0.845 | B2 flat-band eigenvalue |
| omega_PV | 0.792 | Giant pair vibration (collective) |
| Gamma_Langer | 0.250 | Langer tunneling rate |
| omega_pair_removal | 0.137 | Pair removal mode |
| B3-B2 spacing | 0.133 | Inter-sector eigenvalue gap |
| B2 bandwidth | 0.058 | Intra-B2 spread |
| B2-B1 spacing | 0.026 | Inter-sector eigenvalue gap |

Hierarchy: omega_tau >> 2*E_B2 > omega_att > omega_barrier > E_B2 > omega_PV >> Gamma_L

#### Key Ratios

| Ratio | Value | Significance |
|:------|:------|:-------------|
| omega_att / omega_PV | 1.806 | Attempt freq ~ 9/5 of pair vibration |
| omega_PV / (2*Delta_0) | 0.514 | Bound collective mode (below pair-breaking) |
| omega_PV / (2*Delta_OES) | 0.853 | Near corrected threshold |
| omega_att / omega_tau | 0.173 | Attempt << modulus oscillation |
| Gamma_Langer / omega_tau | 0.030 | Kapitza ratio (Langer) |
| Gamma_simple / omega_tau | 0.161 | Kapitza ratio (simple) |
| omega_pair_removal / (B3-B2) | 1.029 | Near-resonance (2.9% detuning) |

#### Resonance Analysis

Only THREE unique eigenvalue spacings exist in the 8-mode spectrum at the fold: B2-B1 = 0.026, B3-B2 = 0.133, B3-B1 = 0.159. None matches omega_att or omega_PV directly. The single near-resonance is omega_pair_removal = 0.137 vs B3-B2 = 0.133 (2.9% detuning). This may be physically significant: the pair removal energy nearly equals the B3-B2 inter-sector spacing, suggesting the pair removal mode transfers spectral weight between the B2 and B3 sectors.

The harmonic ratio omega_att/omega_PV = 1.806 is close to 9/5 (error 0.35%). The ratio omega_PV/(B3-B2) is close to 6/1 (error 0.76%). These near-integer relationships suggest an underlying harmonic structure in the BCS energy landscape, but are not exact resonances.

#### Instanton Parameters (m_eff = 1)

| Quantity | Value |
|:---------|:------|
| delta_inst (instanton width) | 0.851 |
| L / delta_inst | 0.035 (system << instanton) |
| xi_BCS / delta_inst | 0.950 (comparable) |
| n_inst (dilute gas) | 0.115 |
| diluteness (n * delta) | 0.098 |

The system size L = 0.030 is 28x smaller than the instanton width delta_inst = 0.851, confirming the 0D limit (no room for a single complete instanton). The BCS coherence length xi_BCS = 0.808 is 95% of the instanton width -- the two length scales are essentially the same, as expected for a single-gap BCS system.

#### Nuclear Physics Benchmark

The pair vibration at omega_PV = 0.792 sits at 51% of 2*Delta_0 (mean-field pair-breaking threshold), or 85% of 2*Delta_OES (odd-even staggering threshold). In nuclear physics, the pair vibration typically sits near 2*Delta (0.8-1.2 ratio). The ratio 0.51 from the mean-field Delta_0 is anomalously low, but using Delta_OES gives a nuclear-like ratio of 0.85. This is consistent with the BCS-BEC crossover regime (g*N = 2.18) where mean-field overestimates Delta relative to the exact gap.

The attempt frequency omega_att = 1.43 is 1.81x the pair vibration frequency. In nuclear physics, the "attempt frequency" for tunneling (alpha-decay, fission) is set by the nuclear frequency omega_0, which is typically 2-5x larger than the pairing vibration energy. The ratio 1.81 here is at the low end of the nuclear range, consistent with the system being in the strong-coupling (BCS-BEC crossover) regime rather than the weak-coupling BCS limit.

#### Geometric Origin

omega_att is FULLY DERIVABLE from SU(3) geometry:

SU(3) metric -> D_K(tau) -> {E_B2, v_F, rho} -> {M_max, Delta_0, E_cond} -> {a_GL, b_GL} -> omega_att

Every input traces to the Jensen-deformed metric on SU(3) and the Kosmann lift on the spinor bundle. There are no free parameters. The attempt frequency is as geometric as the Dirac eigenvalues themselves.

#### Assessment

The attempt frequency omega_att = 1.430 +/- 0.019 sits between the pair-breaking threshold (2*E_B2 = 1.691) and the pair vibration energy (omega_PV = 0.792). This is physically sensible: the attempt frequency measures how fast the gap oscillates around its equilibrium, which should be faster than the collective pair vibration (which involves coherent superposition of particle-hole excitations) but slower than individual pair-breaking (which requires exciting a single quasiparticle across the gap).

The Kapitza ratio Gamma_Langer / omega_tau = 0.030 is well BELOW unity, meaning the actual tunneling rate (including the Boltzmann suppression exp(-S_inst) = 0.93 and the barrier prefactor) is 33x slower than the modulus oscillation. This differs from the S31 estimate of 5.98-9.64 because S31 used a different effective coupling ratio and did not include the Langer prefactor. The Gamma_simple / omega_tau = 0.161 is also below unity but closer, at 6.2x slower.

The key finding is that omega_att, omega_PV, and omega_barrier are all O(1) in D_K eigenvalue units -- the BCS frequency scales are NOT hierarchically separated from the geometric scales of SU(3). This is fundamentally different from condensed-matter BCS where omega_Debye >> Delta >> single-electron level spacing. Here, all three scales are comparable because the B2 sector has only 4 modes and the system is in the BCS-BEC crossover regime.

#### Data Files

| File | Content |
|:-----|:--------|
| `tier0-computation/s38_attempt_freq.py` | Full computation script |
| `tier0-computation/s38_attempt_freq.npz` | All frequencies, ratios, instanton parameters |

---

### C-4: KZ Defect Density Estimate [LOW-COST]

**Agent**: gen-physicist
**Status**: COMPLETE
**Gate**: KZ-COSMO (original: n_defect x Vol(4D) > 1; reformulated: see below)
**Input**: `tier0-computation/s36_tau_dynamics.npz`, `s37_instanton_action.npz`, `s37_instanton_mc.npz`, `s36_bdi_winding.npz`, `s37_pair_susceptibility.npz`

#### Gate KZ-COSMO Verdict: ILL-POSED / REFORMULATED

The original gate criterion (n_defect x Vol(4D horizon) > 1) assumes spatially extended domain walls from Kibble-Zurek in a system with spatial dimensions. The BCS pairing is **0-dimensional** (L/xi_GL = 0.031): there is no spatial direction for domain walls to form. The gate is ill-posed as stated.

**Reformulated criterion**: P_exc (quasiparticle excitation probability) > 0.5?
**Measured**: P_exc = 1.000 (sudden quench, saturated). **PASS (reformulated)**.

The physical meaning: the sudden quench **destroys** the BCS condensate entirely. No condensate survives the transit. Excitation energy exceeds condensation energy by 443x.

#### Key Numbers

| Quantity | Value | Comment |
|:---------|:------|:--------|
| Adiabaticity tau_Q / tau_0 | **8.71 x 10^{-4}** | **SUDDEN QUENCH** (tau_Q << tau_0) |
| xi_KZ (formal KZ formula) | 0.139 | xi_0 * (tau_Q/tau_0)^{1/4}, but formula invalid |
| xi_KZ (physical, sudden-quench floor) | 0.808 | Saturated at xi_0 = xi_BCS |
| P_LZ (Landau-Zener, diabatic) | **0.999** | Exponent = 6.84 x 10^{-4} |
| P_exc (KZ excitation) | **1.000** | All 8 BCS modes excited |
| n_Bog (Schwinger-analog) | **0.999** | Per-mode pair creation probability |
| E_exc / |E_cond| | **443** | Excitation energy >> condensation energy |
| BDI winding number nu | **0** | TRIVIAL: no topologically protected defects |
| N_defect (1D, formal) | 0.037 | << 1 defect in window (0D renders this moot) |
| Gamma_inst (instanton rate) | 0.739 | Domain wall annihilation time ~ 1.35 |
| t_transit / t_annihilation | 8.35 x 10^{-4} | Transit 1200x faster than annihilation |
| t_ann / t_Hubble | 793 | Annihilation 793x slower than Hubble time |

#### Derivation Summary

**1. Transit parameters**: |v_terminal| = 26.5, BCS window [0.175, 0.205] width 0.030. Quench time tau_Q = 1.13 x 10^{-3} (natural units). BCS critical exponents (mean-field): nu = 1/2, z = 2, giving KZ exponent nu/(1+z*nu) = 1/4.

**2. Sudden-quench regime**: tau_Q/tau_0 = 8.71 x 10^{-4} << 1. The transit crosses the BCS window in 0.087% of the microscopic relaxation time. The standard KZ formula xi_KZ = xi_0 (tau_Q/tau_0)^{1/4} gives xi_KZ = 0.139, but this is below the microscopic floor. Physically, xi_KZ saturates at xi_0 = xi_BCS = 0.808.

**3. 0D resolution**: L/xi_GL = 0.031 means the pairing system has no spatial extent. KZ in 0D does not produce domain walls. Instead, it produces universal quasiparticle excitation (P_exc = 1). The Landau-Zener formula confirms: P_LZ = 0.999 (exponent = 6.84 x 10^{-4}, essentially zero). Every mode is excited.

**4. Topological content**: BDI winding number nu = 0 at mu = 0 (PH-forced). No topologically protected defects exist. Pfaffian sign = -1 at all tau (no topological phase transition). Domain walls between +Delta and -Delta regions, even if formed, are not topologically protected and annihilate on timescale 1/Gamma_inst ~ 1.35.

**5. Bogoliubov pair creation**: Per-mode P_pair ~ 0.995 for all 8 BCS modes. DOS-weighted total pair creation: 59.8 quasiparticle pairs. This is a complete disruption of the BCS vacuum.

**6. 4D mapping**: In the 0D limit, every 4D spatial point undergoes the same sudden quench of its internal-space BCS sector. The excitation is spatially uniform, not localized. There are no 4D domain walls (because the gap field is internal, 0D). The excitation energy (E_exc = 69.0) exceeds condensation energy (|E_cond| = 0.156) by a factor of 443.

#### Cross-Checks

1. **tau_Q consistency**: Delta_tau/|v_terminal| = dt_transit (from s36 trajectory integration). Ratio = 1.000. EXACT.
2. **Three tau_0 choices** (1/Delta_0, 1/omega_PV, tau_GL) all give tau_Q/tau_0 < 0.003. All in sudden-quench regime. Result is robust against choice of microscopic timescale.
3. **E_exc/E_cond = 443** is consistent with S37 result E_vac/E_cond = 28.8. The KZ estimate is larger because it counts DOS-weighted excitation energy across all 8 modes, while the S37 vacuum energy sums quantum fluctuations at equilibrium. Both confirm: excitation energy >> condensation energy.
4. **Dimensional analysis**: xi_KZ has dimensions of length (spectral units). tau_Q has dimensions of time. KZ exponent 1/4 is dimensionless. Consistent.

#### Data Files

| File | Content |
|:-----|:--------|
| `tier0-computation/s38_kz_defects.py` | Full computation script |
| `tier0-computation/s38_kz_defects.npz` | All results (transit params, KZ lengths, excitation probabilities, energies, gate verdict) |

#### Assessment

The transit through the van Hove fold is a **sudden quench** (tau_Q/tau_0 = 8.7 x 10^{-4}), not an adiabatic passage. The standard Kibble-Zurek picture (spatial domain walls from causal horizon fragmentation) does not apply because the BCS system is 0-dimensional. Instead, the sudden quench universally excites all 8 BCS modes with probability P_exc = 1.000, depositing energy 443x the condensation energy into quasiparticle excitations.

The BDI topological class is trivial (nu = 0) at mu = 0, so no topologically protected defects exist. Any domain walls that might form are unprotected and annihilate via instantons, but the annihilation time (1.35 natural units) is 793x the Hubble time, meaning they would persist cosmologically even without topological protection. However, this is moot: in 0D there are no domain walls to form.

The key physical conclusion is that the BCS condensate is **completely destroyed** by the transit. The quench is too fast for the order parameter to track. This is consistent with the S37 finding that E_vac/E_cond = 28.8 (fluctuations dominate 29x) and with the CHAOS-3 result (t_scr/t_transit = 814). The internal-space BCS pairing cannot survive the fold transit in any form. Whatever the 4D observer sees, it is not a BCS condensate.

---

### C-5: D_K Level Spacing Statistics [ZERO-COST]

**Agent**: kitaev-quantum-chaos-theorist
**Status**: COMPLETE
**Gate**: CHAOS-1
**Input**: `tier0-computation/s27_multisector_bcs.npz` (eigenvalues across 9 (p,q) sectors, 9 tau values)
**Priority**: HIGHEST

#### Data Source and Method

Eigenvalues from the s27 multisector BCS computation: 9 Peter-Weyl sectors with (p,q) in {(0,0), (1,0), (0,1), (1,1), (2,0), (0,2), (3,0), (0,3), (2,1)}, at tau in {0, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50}. The tau=0.20 grid point is the nearest to the fold at tau=0.190.

The ratio statistic r_n = min(s_n, s_{n+1})/max(s_n, s_{n+1}) was computed from consecutive spacings within each sector. This diagnostic does NOT require spectral unfolding (Oganesyan & Huse 2007). Two unfolding methods (polynomial degree-5, local average) were applied as cross-checks on P(s).

Exact degeneracies from the residual U(1)_7 symmetry were removed before analysis. Further decomposition by degeneracy multiplicity (proxy for K_7 quantum number) was performed to assess the impact of superimposed independent sequences.

#### Primary Result: (2,1) Sector (Largest, 84 Unique Levels)

| tau | N_unique | <r>_raw | err | <r>_poly | <r>_local | Classification |
|:----|:---------|:--------|:----|:---------|:----------|:---------------|
| 0.00 | 12 | 0.507 | 0.095 | 0.570 | 0.394 | N/A (too few) |
| 0.10 | 84 | 0.443 | 0.031 | 0.462 | 0.430 | INTERMEDIATE |
| 0.15 | 84 | 0.399 | 0.034 | 0.418 | 0.398 | POISSON |
| **0.20** | **84** | **0.321** | **0.028** | **0.340** | **0.305** | **SUB-POISSON** |
| 0.25 | 84 | 0.352 | 0.031 | 0.370 | 0.332 | SUB-POISSON |
| 0.30 | 84 | 0.329 | 0.027 | 0.349 | 0.344 | SUB-POISSON |
| 0.35 | 84 | 0.390 | 0.030 | 0.413 | 0.403 | POISSON |
| 0.40 | 84 | 0.364 | 0.032 | 0.378 | 0.356 | POISSON |
| 0.50 | 84 | 0.312 | 0.028 | 0.323 | 0.317 | SUB-POISSON |

Three unfolding methods agree to within 0.03, confirming robustness.

#### Cross-Sector Comparison at Fold (tau=0.20)

| Sector | N_unique | <r>_raw | err | Classification |
|:-------|:---------|:--------|:----|:---------------|
| (2,1) | 84 | 0.321 | 0.028 | SUB-POISSON |
| (3,0) | 54 | 0.510 | 0.034 | GOE? |
| (0,3) | 54 | 0.510 | 0.034 | GOE? |
| (2,0) | 38 | 0.483 | 0.045 | INTERMEDIATE |
| (0,2) | 38 | 0.483 | 0.045 | INTERMEDIATE |
| (1,1) | 36 | 0.336 | 0.039 | SUB-POISSON |
| (1,0) | 22 | 0.320 | 0.067 | SUB-POISSON |
| (0,1) | 22 | 0.320 | 0.067 | SUB-POISSON |
| (0,0) | 6 | 0.106 | 0.045 | SUB-POISSON |

Pooled across all large sectors: <r> = 0.430 +/- 0.016 (N=292 ratios). Pooled within-multiplicity classes (best K_7 resolution): <r> = 0.375 +/- 0.019 (N=262 ratios).

#### Critical Diagnosis: Sub-Poisson Artifact

The (2,1) sector shows <r> = 0.321 at the fold, **below** the Poisson value of 0.386. This is diagnostic of **superimposed independent spectral sequences** (Berry-Tabor 1977). The unresolved U(1)_7 conserved charge means eigenvalues with different K_7 quantum numbers coexist in a single sorted list. When levels from different K_7 subsectors cross, they create anomalously small spacings that cluster r-values near zero, driving <r> below Poisson.

Evidence for this mechanism:
- Minimum spacing / mean spacing = 0.0083 at fold (83x smaller than mean -- systematic near-crossings)
- Degeneracy multiplicities {1,2,3,4,5,6} correspond to different K_7 weight space contributions
- Within-multiplicity pooled <r> = 0.375 recovers Poisson to 0.6 sigma

#### The (3,0)/(0,3) Anomaly

The (3,0) and (0,3) sectors show <r> ~ 0.51 at tau=0.20, nominally GOE. However, this result is NOT stable across tau: <r> oscillates between 0.29 (tau=0.25) and 0.51 (tau=0.20) with period ~0.05 in tau. For genuine GOE statistics, <r> should be stable at ~0.53 for all tau > 0. The 2-sigma oscillation (SE ~ 0.04 for N=52 ratios) confirms this is a statistical fluctuation from finite sample size, not genuine quantum chaos.

KS tests at fold: (2,1) prefers Poisson over GOE (p_Poisson/p_GOE = 2.5e11). (3,0) marginally prefers GOE (p_GOE/p_Poisson = 1648) but this is not reproducible at adjacent tau values.

#### Gate CHAOS-1 Verdict: ORDERED

| Criterion | Threshold | Measured | Status |
|:----------|:----------|:---------|:-------|
| <r> > 0.50 at fold | 0.50 | 0.321 (2,1) | ORDERED |
| <r> > 0.50 at fold | 0.50 | 0.430 (pooled) | ORDERED |
| <r> > 0.50 at fold | 0.50 | 0.375 (within-mult) | ORDERED |
| Primary diagnostic | 0.42 boundary | 0.321 | Below Poisson |

**The D_K spectrum on Jensen-deformed SU(3) is integrable, not chaotic, at the van Hove fold.** The level spacing statistics are consistent with Poisson (within-multiplicity) or sub-Poisson (mixed K_7 subsectors) across all sectors with adequate statistics. No sector shows robust, tau-stable GOE behavior.

#### Assessment

The Dirac operator D_K(tau) at the fold is **not quantum chaotic** by the BGS criterion. The spectrum retains enough conserved structure from the U(1)_7 symmetry (proven exact by [iK_7, D_K] = 0 at all tau, Session 34) to maintain integrable-class level statistics. The Jensen deformation breaks SU(3) -> U(1)_7, but this residual symmetry is sufficient to prevent the transition to random-matrix statistics. This is consistent with the Berry-Tabor conjecture: the system has conserved quantities (K_7 eigenvalues) at all tau, so its spectrum remains Poisson.

This result constrains the "chaos-first" interpretation: while the instanton gas dynamics may be chaotic in the many-body Fock space (CHAOS-2 test), the single-particle Dirac spectrum itself is integrable. Chaos, if present, must arise from the many-body interactions, not from the geometry of the internal space.

#### Data Files

| File | Content |
|:-----|:--------|
| `tier0-computation/s38_level_spacing.py` | Analysis script (full computation) |
| `tier0-computation/s38_level_spacing.npz` | All <r> values, per-sector, per-tau |
| `tier0-computation/s38_level_spacing.png` | 8-panel diagnostic plot |

---

### C-6: OTOC of Gap Operator [MEDIUM-COST]

**Agent**: kitaev-quantum-chaos-theorist
**Status**: COMPLETE
**Gate**: CHAOS-2
**Input**: 8-mode BCS Hamiltonian in pair Fock space (dim=256), V_phys from DOS-weighted V_8x8

#### Hamiltonian Construction

The BCS Hamiltonian was built in the pair Fock space for 8 modes (B2 x4, B1, B3 x3) with DOS-weighted pairing interaction V_phys_{kk'} = V_{kk'} * sqrt(rho_k * rho_k'). The Fock space dimension is 2^8 = 256. Single-particle energies: E_B2 = 0.8453 (x4), E_B1 = 0.8191, E_B3 = 0.9782 (x3). Chemical potential mu = 0 (PH-forced). The Hamiltonian conserves total pair number N_pair = sum_k n_k, decomposing into 9 sectors (N_pair = 0, ..., 8).

| Parameter | Value |
|:----------|:------|
| dim(Fock) | 256 |
| E_min (ground state) | -0.6684 |
| E_max | 11.7178 |
| Spectrum width | 12.386 |
| <N_pair> in ground state | 1.000 |
| V_phys max | 0.880 |
| Hermiticity error | 4.4e-16 |

#### OTOC Computation

The gap operator A = (Delta + Delta^dag)/sqrt(2) where Delta = sum_k sqrt(rho_k) P_k (DOS-weighted pair annihilation) was evolved exactly: A(t) = exp(iHt) A exp(-iHt) via the eigenbasis. The OTOC F(t) = -Tr(rho [A(t), A(0)]^2) / Z was computed at 8 temperatures (T = 0.02 to 10.0) over t = 0 to 80 natural units (2000 time points).

| Quantity | Value |
|:---------|:------|
| lambda_L (Lyapunov exponent) | **No exponential regime** |
| Early-time growth | F(t) ~ t^{1.9} (BCH universal quadratic) |
| Late-time behavior | **Oscillatory**, quasi-period ~ 6.7 natural units |
| Best exponential fit R^2 | 0.80 at beta=0.5 (from power-law contamination, not genuine) |
| F_max / <A^2>^2 (normalized) | 5.2 -- 5.4 (O(1) saturation, no scrambling) |
| MSS bound violated? | **No** (no positive lambda_L to compare) |

**Detailed Lyapunov analysis**: Sliding-window exponential fits across all time intervals yield R^2 < 0.70 uniformly. The "weak exponential" fits at high T (beta = 0.1, 0.5) with R^2 ~ 0.78 are artifacts of fitting a power-law rise (t^{1.9}) over a limited window. The early-time exponent converges to 2.0 at low temperature, confirming this is the Baker-Campbell-Hausdorff universal quadratic growth F(t) = (1/2)||[H, A]||^2 t^2, not Lyapunov growth.

**Cross-check**: Single-mode OTOC (B2[0] only) at beta=1.0 shows F_max = 157, versus F_max = 19,266 for the full gap operator. The ratio (123x) is consistent with DOS weighting, not chaos amplification.

#### Many-Body Level Spacing Statistics

The BCS many-body spectrum was analyzed within each N_pair sector (pair number is exactly conserved: ||[H, N_pair]|| = 0). The branch occupation numbers N_B2, N_B1, N_B3 are NOT conserved (||[H, N_B2]|| = 4.07), confirming inter-branch pair scattering is active.

| N_pair | dim | <r> | err | KS p(Poisson) | KS p(GOE) | Verdict |
|:-------|:----|:----|:----|:--------------|:----------|:--------|
| 1 | 8 | 0.407 | 0.044 | 0.648 | 0.069 | POISSON |
| 2 | 28 | 0.487 | 0.054 | 0.033 | 0.0001 | NEITHER |
| 3 | 56 | 0.436 | 0.036 | 0.044 | 0.0002 | NEITHER |
| **4** | **70** | **0.526** | **0.031** | **0.321** | **0.0004** | **POISSON** |
| 5 | 56 | 0.439 | 0.037 | 0.200 | 0.0000 | POISSON |
| 6 | 28 | 0.343 | 0.055 | 0.161 | 0.0001 | POISSON |
| 7 | 8 | 0.514 | 0.116 | 0.674 | 0.808 | GOE (N=8, not significant) |
| Pooled (within-sector) | 240 | 0.459 | 0.017 | -- | -- | INTERMEDIATE |

**Critical finding**: The N_pair=4 sector (largest, dim=70) has <r> = 0.526, which by r-ratio alone looks borderline GOE. However, the KS test **rejects GOE** (p = 0.0004) while **accepting Poisson** (p = 0.321). The r-ratio is elevated by finite-size fluctuations; the full distribution P(s) is Poisson. GOE is rejected at >3 sigma in every sector with more than 8 states.

The N_pair=7 sector (dim=8) formally accepts both GOE and Poisson, but with only 8 levels the statistical power is negligible. This is not evidence for chaos.

#### Spectral Form Factor

| Quantity | Full spectrum (beta=1) | N_pair=4 sector |
|:---------|:----------------------|:----------------|
| K(0) | 1.0 | 1.0 |
| K_min | 6.55e-5 | 3.43e-5 |
| K_plateau | 7.68e-2 | 7.99e-2 |
| Dip-to-plateau ratio | 1172 | 2327 |

The SFF shows a dip-ramp-plateau structure, but the high dip-to-plateau ratio is driven by the small Hilbert space dimension (plateau ~ 1/dim), not by RMT correlations. A Poisson spectrum of 70 uncorrelated levels produces comparable ratios.

#### Gate CHAOS-2 Verdict: ORDERED

| Criterion | Threshold | Measured | Status |
|:----------|:----------|:---------|:-------|
| Exponential OTOC growth | R^2 > 0.90 over 1 decade | R^2 < 0.70 (all windows) | **ORDERED** |
| lambda_L > 0 | Positive, robust | No exponential regime | **ORDERED** |
| Many-body <r> > 0.50 (KS) | GOE at p > 0.05 | p(GOE) < 0.001 for dim > 8 | **ORDERED** |
| MSS bound violated | lambda_L > 2*pi*T | N/A (no lambda_L) | **SAFE** |

**The many-body BCS dynamics in the 0D instanton gas are NOT quantum chaotic.** The OTOC shows BCH quadratic early-time growth (F ~ t^{1.9}) followed by oscillatory behavior at the pair vibration frequency, with no exponential Lyapunov regime. The many-body level statistics are Poisson (KS rejects GOE at p < 0.001 in all sectors with adequate statistics). The system is a quasi-integrable pair vibrator, not a scrambler.

#### Assessment

The BCS Hamiltonian on 8 modes with DOS-weighted pairing produces a 256-dimensional Fock space that is exactly solvable. Despite active inter-branch pair scattering (||[H, N_B2]|| = 4.07), the many-body dynamics remain integrable. This is because the pairing interaction V_{kk'} is too structured: it derives from Kosmann inner products on a specific geometry (Jensen-deformed SU(3)), not from random couplings. In the SYK paradigm, chaos requires random all-to-all coupling; here the coupling matrix has rank-1 structure within the dominant B2 sector (the four B2 modes are nearly degenerate with nearly identical V elements). The system has too many approximate conserved quantities (approximate B2 pair number, approximate U(1)_7 charge in the Fock space) to reach the chaos threshold.

This result, combined with CHAOS-1 (single-particle Poisson), establishes that neither the single-particle geometry nor the many-body BCS dynamics of this framework exhibit quantum chaos. The "chaos-first" interpretation would require a mechanism beyond the BCS pairing vertex to generate scrambling.

#### Data Files

| File | Content |
|:-----|:--------|
| `tier0-computation/s38_otoc_bcs.py` | Full OTOC computation script |
| `tier0-computation/s38_otoc_bcs.npz` | All results (OTOC, spectra, level statistics, SFF) |
| `tier0-computation/s38_otoc_bcs.png` | 9-panel diagnostic plot |

---

### C-7: Scrambling Time vs Transit Time [LOW-COST]

**Agent**: kitaev-quantum-chaos-theorist
**Status**: COMPLETE
**Gate**: CHAOS-3
**Input**: OTOC from C-6 + transit time from s36_tau_dynamics.npz

#### Method

Since CHAOS-2 found no exponential growth, the scrambling time t_scr is defined operationally as the time for the OTOC to first reach 50% of its saturation value. This is the fastest timescale on which the gap operator "spreads" through the Fock space, even in the absence of genuine chaos. The transit time through the BCS window (tau = 0.175 to 0.205) comes from the S36 tau dynamics computation.

| Quantity | Value |
|:---------|:------|
| t_scr (50% saturation, fastest T) | 0.92 (at beta = 20) |
| t_transit (full spectral gradient) | 1.13e-3 |
| Ratio t_scr / t_transit | **814** |
| Scrambling during transit? | **No** |

#### Gate CHAOS-3 Verdict: ORDERED

| Criterion | Threshold | Measured | Status |
|:----------|:----------|:---------|:-------|
| t_scr < t_transit | Ratio < 1 | Ratio = 814 | **ORDERED** |
| Scrambling during transit | t_scr / t_transit < 10 (generous) | 814x | **ORDERED** |

Even defining "scrambling" generously as the time for the OTOC to reach half its saturation value (not requiring exponential growth), the saturation time is 814x longer than the transit time through the BCS window. The pair vibrator does not have time to complete a single oscillation (period ~ 6.7) during transit (duration ~ 0.001). The transit is 6,700x too fast for even one pair vibration cycle.

#### Assessment

The 0D BCS system cannot scramble information during the transit through the van Hove fold. The transit is 814x faster than the fastest OTOC saturation timescale and 6,700x faster than a single pair vibration period. This confirms the preliminary S37 estimate that the transit is too fast for many-body dynamics to develop. The instanton gas, while exhibiting large fluctuations (E_vac/E_cond = 28.8), is a quasi-periodic pair vibrator, not a scrambler. The "chaos-first" hypothesis requires either (a) a much slower transit mechanism, or (b) scrambling physics arising from degrees of freedom beyond the 8-mode BCS sector.

---

## Gate Summary Table

| Gate ID | Computation | Pre-Registered Criterion | Verdict |
|:--------|:------------|:------------------------|:--------|
| CC-INST-38 | W0 + C-1 + C-2 | <Delta^2>/Delta_0^2 < 0.011 => F.5 overturned | *PENDING* |
| CHAOS-1 | C-5 | <r> > 0.50 at fold => GOE | **ORDERED** (<r>=0.321, sub-Poisson, integrable) |
| CHAOS-2 | C-6 | lambda_L > 0 with exp growth | **ORDERED** (no exponential regime, F~t^{1.9} quadratic, KS rejects GOE at p<0.001) |
| CHAOS-3 | C-7 | t_scr < t_transit | **ORDERED** (t_scr/t_transit = 814x, pair vibration period 6700x transit) |
| KZ-COSMO | C-4 | n_defect x Vol > 1 | **ILL-POSED / REFORMULATED** (0D system, no spatial defects. Reformulated P_exc>0.5: PASS at P_exc=1.000. Condensate destroyed by sudden quench.) |

---

## Constraint Map Updates

*[To be filled as results come in]*

### New Entries

| ID | Mechanism | Gate | Verdict | Session |
|:---|:----------|:-----|:--------|:--------|
| | | | | |

### State Changes

| ID | Old State | New State | Reason |
|:---|:----------|:----------|:-------|
| | | | |

---

## Probability Assessment

**Pre-session**: 5-8% (spectral action route, structural floor per Sagan)
**Instanton route**: NOT YET ASSESSED (this session determines)

*[Post-session assessment to be filled after all workshops and computations complete]*

---

## Files Created This Session

| File | Content | Agent |
|:-----|:--------|:------|
| `sessions/session-38/session-38-results-workingpaper.md` | This file | team-lead |
| `sessions/session-38/session-38-einstein-naz-workshop.md` | W0: CC-Through-Instanton | einstein + nazarewicz |
| `tier0-computation/s38_level_spacing.py` | CHAOS-1 analysis script | kitaev-quantum-chaos-theorist |
| `tier0-computation/s38_level_spacing.npz` | CHAOS-1 data (all <r> values) | kitaev-quantum-chaos-theorist |
| `tier0-computation/s38_level_spacing.png` | CHAOS-1 diagnostic plot (8 panels) | kitaev-quantum-chaos-theorist |
| `tier0-computation/s38_otoc_bcs.py` | CHAOS-2 OTOC computation script | kitaev-quantum-chaos-theorist |
| `tier0-computation/s38_otoc_bcs.npz` | CHAOS-2 data (OTOC, spectra, SFF, level stats) | kitaev-quantum-chaos-theorist |
| `tier0-computation/s38_otoc_bcs.png` | CHAOS-2 diagnostic plot (9 panels) | kitaev-quantum-chaos-theorist |
| `tier0-computation/s38_attempt_freq.py` | C-3 attempt frequency script | nazarewicz |
| `tier0-computation/s38_attempt_freq.npz` | C-3 data (all frequencies, ratios) | nazarewicz |
| `sessions/session-38/session-38-naz-qa-workshop.md` | W1: Pair Vibrator as Phonon | *PENDING* |
| `sessions/session-38/session-38-naz-tesla-workshop.md` | W2: Instanton Resonance | *PENDING* |
| `sessions/session-38/session-38-landau-hawking-workshop.md` | W3: Kibble-Zurek at Fold | *PENDING* |

---

## Session Execution Order

Per session plan Section VII:

1. **C-1 first** — provides <Delta^2> input for W0
2. **W0** — CC-Through-Instanton (Einstein x Nazarewicz), 2 rounds
3. **C-2 after W0** — instanton-averaged BdG shift using W0 results
4. **C-5 parallel** — level spacing statistics (HIGHEST priority, independent)
5. **W1-W3 after W0** — can run in parallel
6. **C-3 with W2** — attempt frequency (input to Instanton Resonance workshop)
7. **C-4 with W3** — KZ defect density (input to Kibble-Zurek workshop)
8. **C-6, C-7 last** — depend on C-5 results and OTOC computation

---

*"The map was never still." — Spectral Post Mortem*
*"Find the frequency." — Tesla*
*"Compute it." — Einstein*
*"What does the observer actually measure?" — Sagan*
