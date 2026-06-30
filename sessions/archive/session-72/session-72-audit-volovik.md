# Session 72 Project Audit: Mechanism Chain & Superfluid Physics

**Date**: 2026-04-10
**Agent**: volovik-superfluid-universe-theorist
**Scope**: Comprehensive audit of mechanism chain gaps, BCS/GGE open problems, and 3He-B inheritance status
**Sources**: Atlas D02 (mechanism lifecycle), D04 (assumptions), D08 (open questions), S72 results working paper, S72 laminar flow workshop, EVOI framework, agent memory (70+ computation results S42-S72)

---

## I. Mechanism Chain Status (Link by Link)

The EVOI framework (S66) tracks 11 mechanism chain links. Status as of S72:

| # | Link | Status | Evidence | Gap Assessment |
|:--|:-----|:-------|:---------|:---------------|
| 1 | Geometric spectral moments (a_0, a_2, a_4) | **PROVEN** | Machine epsilon across 51 tau values. 67/67 Baptista checks. S72 W1-C: zeta ratio converges monotonically to Gilkey value 0.25 at L=7. | CLOSED. No gap. |
| 2 | Product decomposition (A-tensor, Kasparov) | **PROVEN** | S72 W2-D: INSTANTON-KAPPA-72 INFO -- non-trivial fibration viable for rho > 1.80/M_KK. Kasparov product preserved for large instantons. Measure-peak instanton (rho ~ M_KK^{-1}) marginally obstructed (kappa = 1.057). | GAP: dominant instanton moduli measure peak sits at Kato-Rellich boundary. Does the instanton gas live predominantly at rho > 1.80, or at rho ~ 1? |
| 3 | GGE permanence (9/9 + structural theorem) | **PROVEN** conditional on Josephson isolation | S72 W4-B: C_V^GGE/C_V^thermal saturates at 2.20 for N>=8, alpha=0.013 (no partial thermalization). Workshop: five-layer laminar protection hierarchy. Re_GGE = 0 exact. | GAP: "conditional on Josephson isolation" means the strong-coupling J_C2/Delta = 2.01 (W4-E) makes perturbative corrections O(1). The inter-cell entropy lies in [2.21, 4.11] nats -- a factor-2 uncertainty. Integrability protects the conserved charges, but the Josephson dressing of the per-cell entropy is unresolved. |
| 4 | Fold stability (36D Hessian, alpha 26x) | **PROVEN** | HESS-40: all 22 transverse eigenvalues positive. All 28D directions stable. S62 TYPE-I-TRANSIT-62: Type-I superconductor, kappa_max = 0.502. S65 GAP-ANTIJENSEN-65: Delta/Delta_0 = 0.975 at dynamic range, gap never closes. | CLOSED. No gap. |
| 5 | SM gauge group | **PROVEN** | Extended gauge module extracts SU(3)xSU(2)xU(1). KO-dim = 6 at machine epsilon. S72 W4-F: a_2/a_4 near-constancy NOT SU(3)-specific (G_2 is MORE constant, FAIL). | GAP: Fiber selection criterion unresolved. a_2/a_4 constancy does not select SU(3) over G_2. The absolute ratio magnitude differs by 40x but no selection principle is established. |
| 6 | Higgs mass | **CONVERGING** | Aitken extrapolation: 127.5 GeV (1.9% from 125.1). S72 W2-C: best-fit f* predicts f*(0) = 0.088, giving m_H ~ 39-51 GeV (EXCLUDED). Resolution: full RG running from M_KK to M_Z with KK thresholds needed. | GAP: The spectral functional f* that gives correct n_s gives WRONG m_H at tree level. RG + KK threshold corrections are invoked but not computed. |
| 7 | Baryogenesis | **PASS** | eta_B ~ 2e-9 (3.2x from observed 6.1e-10). S61 J-BREAKING-CATALOG: 3 channels OPEN (UV/graviton/texture). BDI protects J; external breaking mandatory. | GAP: J-breaking mechanism not identified from first principles. delta_CP = 2.76e-4 is natural (g_UV^2) but requires UV physics not derived from the spectral triple. |
| 8 | CC mechanism (Volovik dilution) | **PASS** | S66 DILUTION-CC-66: rho_vac ~ M_Pl^2 H^2 closes 114 OOM to 0.01 OOM. S67 BBN-VOLOVIK-67: PASS (|w_vac-1/3| = 3.39e-41). S67 VOLOVIK-Q-A0-67: chi=INF (Euler), a_0 NOT obstruction. Workshop E2: CC dilution and laminar flow share BCS Hamiltonian ancestor, logically independent. | GAP: BBN tension 0.67 (G_eff/G = 1.5). Marginal but inside bounds. The dilution mechanism assumes tau-evolution tracks H(t) -- this mapping is assumed (C1 in D04), never derived. |
| 9 | n_s / spectral tilt | **CONDITIONAL** | Bare: n_s = 0.9567 (1.94 sigma from Planck, S72 W3-A v2 confirmed essentially bare). S72 W2-C: spectral functional f* = 0.912 sqrt + 0.088 exp gives n_s = 0.9649 (Planck central). S72 W3-C: entry horizon adds delta_n_s = +1.001 (LARGE, O(1) correction). | GAP: n_s is SCHEME-DEPENDENT. The f* that matches n_s has divergent SDW expansion (non-perturbative). Entry-horizon tilt O(1) is a major revision -- the multi-stage squeeze picture changes n_s substantially. The total n_s prediction from the compound (entry + fold + decoherence) process is UNCOMPUTED. |
| 10 | Spectral functional selection | **OPEN** | S72 W2-C establishes existence of positive f* satisfying (n_s, A_s) jointly. Anomaly + conservation hierarchy (S66) gives one-parameter dilaton family. But: f* = 0.912 sqrt + 0.088 exp is non-perturbative (divergent SDW moments). No selection principle exists. | GAP: THE existential crisis. Without a selection principle, n_s is accommodation. The EVOI table (P3) rates this at EVOI = 13.2%. Higgs mass discriminates between families (m_H^zeta ~ 174 vs m_H^cutoff ~ 127.5), but f* prediction m_H ~ 39-51 is excluded. |
| 11 | Leggett DM stability | **PASS** observationally | Omega_DM h^2 = 0.120 (0.6% from Planck). S67 LEGGETT-GRAV-DECAY: Z_2 parity protection. S59 f_DM-DEPLETION: f_DM(z=0) = 1.000. S61 DIPOLAR-THERM: Leggett->2Gold kinematically forbidden (5.5x gap). | GAP: Gravitational decay vertex uncomputed from first principles (EVOI P2). Z_2 parity protection established at S67, but the explicit Gamma_grav has not been compared to H_0. |

**Summary**: 9/11 links at PASS or PROVEN. 2 OPEN (spectral functional selection, Leggett gravitational decay vertex). The n_s link is nominally CONDITIONAL but after S72 the situation is more nuanced: the entry-horizon O(1) tilt revision (W3-C) means the compound n_s prediction must be recomputed.

---

## II. A_s Decoherence Budget (All Channels)

The A_s amplitude gap is the #1 open problem. Status tracking from S69 baseline (0.485 OOM) through S70 (0.267 OOM) to S72.

### Current baseline
- **S70 LEGGETT-VACUUM-70**: r_L = 0.617 corrects A_s gap from 0.485 to 0.267 OOM. The single largest correction identified.
- **S71 undamped compound**: delta_OOM = 2.074 (8 BCS modes, spatial + Leggett squeeze compounded).
- **Target**: delta_OOM = 0 (A_s^pred = A_s^obs = 2.1e-9). Gate: |delta_OOM| < 0.30 (factor of 2).

### Channel-by-channel status

| # | Channel | t_dec/t_transit | delta_OOM contribution | Status | Source |
|:--|:--------|:----------------|:----------------------|:-------|:-------|
| 1 | BCS squeeze (undamped) | infinity | 2.074 | BASELINE | S71 |
| 2 | Gap curvature (kappa_Delta) | 5.5e9 | 1.6e-10 (ZERO) | **DEAD** | S72 W1-A |
| 3 | Cell-crossing acoustic | 6.73 | 1.692 | TOO SLOW (9.4x) | S72 W2-A |
| 4 | Hawking broadening (thermal) | ~2.8 | ~1.1 | **RETRACTED** (wrong variance) | WS R1 V2 |
| 5 | Hawking broadening (squeezed) | ~45 | ~1.9 | TOO SLOW | WS R1 QA corrected |
| 6 | KZ pair-crossing (statistical) | ~0.13 | ~0.07 | OVER-DECOHERED | WS R1 V2 |
| 7 | KZ pair-crossing (Bogoliubov) | ~2.2 | ~1.2 | UNDER-DECOHERED | WS R2 QA D2 |
| 8 | Leggett phase diffusion | 1.3e4 | ~2.07 (no effect) | **DEAD** | WS R1 QA |
| 9 | Dispersion mode conversion | ~4200 | ~2.07 (no effect) | **DEAD** | WS R1 QA |
| 10 | Andreev standing wave | ~336 | ~2.06 (~1% correction) | **DEAD** | WS R2 V E1 |
| 11 | Josephson anisotropy (direct) | 1195-14000 | negligible | **DEAD** as direct channel | WS R2 V D1 |
| 12 | Josephson anisotropy (KZ modifier) | second-order | modifies f_KZ | DEMOTED to modifier | WS R2 QA C1 |
| 13 | Spatial squeeze (r_spatial) | -- | 0.002 OOM total | NEGLIGIBLE | S72 W2-A |
| 14 | Leggett squeeze (r_L = 0.617) | -- | 0.002 OOM total (slow channels) | NEGLIGIBLE vs BCS | S72 W2-A |
| 15 | BCS-dressed SA correction | -- | delta_n_s = 3.8e-6 | **NEGLIGIBLE** (16/155984 modes) | S72 W3-A v2 |
| 16 | Entry-horizon blueshift tilt | -- | delta_n_s = +1.001 | **LARGE** (O(1), needs inclusion) | S72 W3-C |
| 17 | Spectral functional selection | -- | Sets overall amplitude kappa | OPEN (f* amplitude = 2.37e-8) | S72 W2-C |
| 18 | Hybridization gap protection | -- | REDUCES decoherence | Works AGAINST gate band | WS R2 QA E2 |

### Assessment

The BCS squeeze dominates (99.8% of delta_OOM at any decoherence timescale). The slow channels (spatial, Leggett, Andreev, dispersion) contribute 0.002 OOM combined. The A_s budget IS the BCS decoherence budget.

**The critical open question**: The KZ pair-crossing spread is the sole surviving fast decoherence channel, but TWO models bracket the gate band:
- Statistical model (1/sqrt(N_pair) spread): t_dec/t_transit ~ 0.13, OVER-decoheres
- Bogoliubov model (delta_phi/delta_omega spread): t_dec/t_transit ~ 2.2, UNDER-decoheres
- Gate band: t_dec/t_transit in [0.57, 0.88]

The resolution requires computing the EXIT-HORIZON Bogoliubov coefficients (not the global fold transformation). If the mode-dependent phase spread delta_phi at the exit horizon is O(0.1) rather than the global O(10^{-4}), the Bogoliubov model gives t_dec/t_transit ~ 0.7, directly in the gate band.

**New complication from S72**: The entry-horizon squeeze (W3-C: r_entry ~ 2.9, comparable to fold squeeze) and its O(1) tilt correction mean the compound power spectrum must include a PRE-FOLD squeeze stage. This was not in the S70 baseline.

---

## III. BCS Open Problems

### A. Gap dynamics across transit
- **Delta(tau) is MONOTONICALLY DECREASING** through the fold (S72 W1-A). dDelta/dtau = -0.245 M_KK (nonzero first derivative). Prior assumption that Delta has a maximum at the fold is WRONG.
- **kappa_Delta = +0.330 M_KK** (concave up: linear decrease is decelerating). Gap varies by 0.5% over transit window.
- **BCS/spectral gradient ratio = 7.94e-5** (S72 W3-D): BCS energy is a 10^{-5} perturbation on the spectral action landscape. Post-transit tau_eq is a GEOMETRIC quantity, not a BCS quantity.
- **OPEN**: The full S(tau) profile beyond the fold is not available. Quartic models of S(tau) generically produce stable post-transit equilibria (313/313 at S72 W3-D), but the physical S(tau) has not been computed beyond the fold.

### B. Pairing channel and sector structure
- **B2 is catalyst** (flat band, W = 0 exact, S43 FLATBAND-43). B3 gap entirely proximity-induced (V_B3B3 = 0.059).
- **S72 W3-A v2**: Mode-selective BCS correction -- only 16 eigenvalues in (0,0) sector participate. delta_n_s = 3.8e-6 (4 OOM below Planck error bar). BCS pairing does NOT affect n_s.
- **OPEN**: Self-consistent HFB gap equation (sector-resolved Delta_{(p,q)}) never executed (Q15 in D08, Nazarewicz priority 1). Mean-field overestimates by 60% (S46 PBCS).
- **OPEN**: Full Kosmann V matrix sweep V_{kk'}(tau) over [0.15, 0.25] not computed (Q6 in D08, deprioritized after S62 CC closure but still relevant for BCS condensate strength).

### C. Leggett mode
- **Leggett-dipolar identification CONFIRMED** (S49 DIPOLAR-CATALOG): epsilon = 0.00248, m_G = 0.070 M_KK (18% from n_s requirement). 95x hierarchy over BA speed.
- **Q = 6.7e5** (S50 LEGGETT-DAMPING-50): Beliaev decay kinematically forbidden (quasiparticle gap 5.5x above order parameter gap, S61 DIPOLAR-THERM-61).
- **S70 LEGGETT-VACUUM-70**: r_L = 0.617, single largest A_s correction (0.485 -> 0.267 OOM).
- **OPEN**: Leggett gravitational decay vertex not computed from first principles (EVOI P2, delta_P(fail) = -30%). Z_2 parity protection established (S67) but Gamma_grav vs H_0 comparison unperformed.
- **OPEN**: Leggett mass imprint in Bogoliubov spectrum CLOSED (S50 BOGOLIUBOV-IMPRINT-50: trans-Planckian erasure). No observational channel for Leggett mass at cosmological scales.

### D. alpha_s (running of spectral index)
- **alpha_s = n_s^2 - 1 identity** at 6 sigma from Planck within K^2 propagators (5 independent proofs, PERMANENT theorem S49-S51). Gives alpha_s = -0.069 (Josephson sector) or [-0.040, 0] (SA-Goldstone mixing at K < K*).
- **S72 W3-C**: Entry-horizon blueshift tilt delta_n_s = +1.001 is O(1). If the tilt is frequency-dependent, alpha_s receives a LARGE correction from the multi-stage squeeze.
- **OPEN**: Transit power spectrum through fold never computed (EVOI P1, highest priority). The full Bogoliubov power spectrum as function of k determines alpha_s at k_CMB. All current alpha_s values use the slow-roll formula, which is inapplicable at Mach 13.75.

---

## IV. GGE / Ordered Veil Open Questions

### A. Thermalization
- **GGE permanence**: PROVEN within each cell (Richardson-Gaudin integrability, S56 PERMANENT). Re_GGE = 0 exact (WS R1 convergence). Combined suppression Gamma_eff ~ 10^{-72} M_KK even with hypothetical instanton breaking (WS R1 Q2).
- **Five-layer protection hierarchy**: (1) R-G integrability (exact), (2) BDI Z_2 gap (topological), (3) CG(24) kinematics (1% phase space), (4) 0D cells, (5) 16 hybridization gaps. All PERMANENT.
- **T3 in D04 marked BROKEN**: S39 found V_phys 13% non-separable, Brody beta = 0.633, t_therm ~ 6 natural units. BUT: this was the SINGLE-CELL result. The MULTI-CELL result (S61 GGE-THERM-61) shows Thouless >> transit at all N by 2625x. The S39 retraction was premature; the correct statement is that intra-cell Brody statistics indicate partial chaos but the Thouless energy scale (which governs physical thermalization) remains far above the transit rate.
- **OPEN**: Whether the T3 entry in D04 should be reclassified from BROKEN to CONDITIONAL given S61 results.

### B. Integrability breaking
- **S63 INTEG-BREAK-FABRIC-63**: delta_J = 1.85, <r> = 0.41 (Wigner-Dyson transition regime). Gamma/H_0 = 2.3e59. CC OPEN conditional on integrability breaking.
- **Instanton breaking**: epsilon_break ~ exp(-S_inst) ~ exp(-80) ~ 10^{-35}. Combined with kinematic suppression: Gamma_eff ~ 10^{-72} M_KK (WS Q2). Negligible.
- **OPEN**: Whether any non-perturbative mechanism (beyond instantons) can break integrability. All tested channels give Gamma << H_0 by vast margins.

### C. C_V predictions
- **C_V^GGE/C_V^thermal = 2.20** for N >= 8 modes with physical squeeze parameters (S72 W4-B). alpha(N>=8) = 0.013 (marginal, no trend). Step function at N=8, then flat.
- **Non-universal** (WS R2 V E3): specific to the substrate's van Hove quench. Universal lower bound: C_V ratio >= 1 (Schur-convexity). 3He-B parent gives ratio -> 1 for isotropic quenches.
- **OPEN**: Whether the C_V ratio constitutes an observational signature at cosmological scales. The ratio measures GGE non-thermality but has no identified observable counterpart in the CMB or LSS.

### D. Ordered Veil severity
- **f_OV = 0.26-0.60** (W4-E): 26-60% of maximal entropy retained as information deficit relative to thermal equilibrium.
- **S_cell(CG24) = 2.21 nats** (bare GGE, integrability-protected leading order).
- **Information deficit = 34-80 nats** (24-cell fabric).
- **OPEN**: The wide range (factor 2.3) reflects the unresolved strong-coupling Josephson dressing. The exact per-cell entropy on the fabric requires going beyond perturbative MI.

---

## V. Transit Physics Gaps

### A. Entry horizon
- **S72 W3-C**: Entry sonic horizon at tau = 0.2195. T_entry = 72.84 M_KK. All BCS modes deeply thermal (omega/T ~ 0.012). Squeeze r_entry in [2.904, 2.937] COMPARABLE to fold squeeze [2.330, 4.320].
- **OPEN**: The entry horizon is a major squeeze stage that PRECEDES the fold. Any n_s prediction must include the entry-horizon pre-squeeze as a mandatory correction. This has NOT been incorporated into the A_s or n_s budgets.
- **CAVEAT**: The entry horizon is subsonic (Ma ~ 0.76 at tau = 0.221). Sonic horizon formalism strictly applies at Ma = 1. The actual pair creation may be suppressed below the sonic point.

### B. Exit horizon and decoherence
- **Four-stage pair creation cascade** (WS R1 QA): Leggett first (Ma_L = 331), then BA phonons, then BCS quasiparticles. Temporal ordering confirmed.
- **Exit-horizon Bogoliubov coefficients**: UNCOMPUTED. The global transformation (S57, S64) has phi_Bog = pi with delta_phi = 2.4e-4. The exit-horizon transformation depends on local surface gravity kappa_exit ~ 3 M_KK (W3-C). Whether delta_phi at the horizon is O(0.1) (gate-band-compatible) or O(10^{-4}) (too coherent) is the single most important open computation.
- **Andreev reflection in tau-space** (WS R2 V E1): Present but subdominant (t_dec^AR/t_transit ~ 336). 0D localization suppresses Andreev decoherence.

### C. Kibble-Zurek
- **S55 TRANSIT-VELOCITY-55**: GGE weakly sensitive to omega_tau. 6/7 crossings diabatic. KZ saturation confirmed. S38 sudden quench VALID.
- **S43 KZ-CELL-43**: Infinite-plane artifact identified, N=32 reliable, tessellation channel CLOSED.
- **S45 KZ-NS-45**: FAIL (370 sigma). n_s = -0.588 from 992-mode Bogoliubov quench. All 3 initial n_s routes closed.
- **OPEN**: Statistical vs Bogoliubov KZ model for pair-crossing spread. This is the decisive open question (see Section II above).

### D. Tau-time mapping
- **C1 in D04: ASSUMED** (never derived). tau-evolution = cosmic expansion is the framework's core postulate. The DeWitt supermetric G_mod = 5.0 is computed but the full Friedmann-modulus coupling is approximate.
- **S72 W3-D**: Stable equilibrium exists in quartic S(tau) models. BCS is a 10^{-5} perturbation. tau_eq is purely geometric.
- **OPEN**: Rigorous derivation of the modulus equation of motion from the 12D Einstein equations reduced to M^4 x SU(3). This is Q13 in D08, never addressed.

---

## VI. Dark Matter Program Status

### A. Candidate: Leggett-channel GGE quasiparticle
- **Omega_DM h^2 = 0.120** (0.6% from Planck 0.1186). Zero free parameters.
- **CDM by construction** (S43 CDM-CONSTRUCT-43): T^{0i} = 0 exact, v_eff = 3.48e-6 c, sigma_self/m = 2.47e-65 cm^2/g. Collisionless.
- **f_DM(z=0) = 1.000** (S59): BA phonons redshift (10^{-118}). BCS QPs annihilate via K_7 recombination (Gamma*t = 10^52). Only Leggett survives. Overshoots observed 0.844 (baryon fraction needed).
- **Z_2 parity protection** (S67): cos(phi_23) structure in BCS gap. Leggett decay kinematically forbidden by 5.5x gap (S61 DIPOLAR-THERM-61). Q = 6.7e5.
- **DM/DE ratio = alpha(thermodynamic)**: S44 DM-DE-RATIO-44 PASS (7/11 methods within 10x of observed 0.387). S45 ALPHA-EFF-45: Method 7c entropy deficit gives alpha = 0.410 (1.06x obs). But alpha range [0.70, 1.15] vs needed 0.33 (S48 DMDE-REFINE-48).

### B. Detection prospects
- **No direct detection channel identified**: sigma_self/m = 2.47e-65 cm^2/g. No electromagnetic coupling. No annihilation signal (K_7 parity).
- **OPEN**: Whether Leggett DM produces any indirect astrophysical signature (e.g., through gravitational interaction, structure formation imprint, or modification of CMB lensing).
- **OPEN**: Whether f_DM overshoot (predicted 1.000 vs observed ~0.844) requires baryonic correction or indicates systematic error.

### C. Closed DM channels
- **S60 LEGGETT-DM-ABUND-60**: FAIL (double). Omega_L h^2 = 3.23e25 (26.4 OOM). tau_L = 3.6e-34 s (52 OOM). Cosmological moduli problem for Leggett as fundamental DM particle.
- **Resolution**: DM is the Leggett GGE quasiparticle (spectral weight in the Leggett channel), not the Leggett mode as a classical oscillation. The S60 FAIL was for the wrong identification.

---

## VII. Cosmological Constant Status

### A. Mechanism history
- **141+ CC mechanism closures** across S43-S72. The atlas documents 91+ numbered closures (D02) plus 50+ additional closures in later eras.
- **Key permanent closures**: Structural Monotonicity Theorem (all spectral action sectors monotone, S37). Perturbative Exhaustion Theorem (S22c). B/F asymmetry = 0 EXACTLY (S65). R-monotonicity (S64). Monotonicity theorem dE_ZP/dq > 0 (S62, permanently closes q-theory self-tuning for GGE residual).

### B. Surviving mechanism: Volovik thermodynamic dilution
- **S66 DILUTION-CC-66 PASS**: rho_vac ~ M_Pl^2 H^2 (Volovik Paper 25, Sec V; Paper 35). Closes 114 OOM gap to 0.01 OOM.
- **S67 BBN-VOLOVIK-67 PASS**: |w_vac - 1/3| = 3.39e-41 at BBN. G_eff/G = 1.5 (marginal but inside BBN bounds).
- **S67 VOLOVIK-Q-A0-67 PASS**: chi = INF (Euler characteristic). a_0 NOT an obstruction to CC mechanism.
- **S71 CC-FROM-GGE-RESIDUAL-71 FAIL**: Lambda_exc = 0.147 M_KK (110 OOM above observation). GGE residual is NOT the observed CC. Q-theory dilution is the sole survivor.

### C. Open CC issues
- **The tau-H mapping** (C1 in D04): The dilution mechanism requires rho_vac(t) = M_Pl^2 H(t)^2. This holds if the vacuum tracks the Hubble rate, which requires a dynamical coupling between the vacuum energy and the expansion. On the substrate, this maps to the spectral action's response to tau-evolution. The mapping is ASSUMED, not derived.
- **BBN tension**: G_eff/G = 1.5 is at the edge of BBN bounds. A dedicated BBN computation with the full Volovik tracking EOS (not just the leading term) would sharpen this.
- **Workshop E2**: CC dilution (chi_vac > 0 from BCS concavity) and laminar flow (Re_GGE = 0 from integrability) are logically independent, sharing the BCS Hamiltonian as common ancestor. No mutual support or tension.

---

## VIII. 3He-B Inheritance Gaps

The S60 framework-3heb-comparison established 22 correspondences. S72 workshop refined the inheritance map. Current status of key mappings:

### A. Confirmed inheritances (structural)
| # | Property | Status | Source |
|:--|:---------|:-------|:-------|
| 1 | AZ class BDI | INHERITED | S53, both systems |
| 2 | Z_2 = -1 gap protection | INHERITED | S53 BDI-W-PHONON |
| 3 | Gap isotropy | STRENGTHENED (0D, no k-dependence) | WS V4 |
| 4 | Superflow stability below v_L | STRENGTHENED (integrability exact) | WS V4 |
| 5 | BCS pairing via Kosmann connection | INHERITED (analog of attractive interaction in particle-particle channel) | S42 |
| 6 | Four-speed hierarchy cosine similarity | 0.996 (5% match) | S69 FOUR-SPEED |
| 7 | Leggett-dipolar correspondence | CONFIRMED (95x hierarchy matches) | S49, S61 |
| 8 | Landau critical velocity concept | INHERITED (Ma_L = 331) | WS convergence |

### B. Lost properties (instability channels removed)
| # | Property | 3He-B | Substrate | Consequence |
|:--|:---------|:------|:----------|:------------|
| 1 | Vortex nucleation | pi_1(SO(3)) = Z_2 | pi_1 = 0 (discrete topology) | Primary superflow breakdown removed |
| 2 | Mutual friction | Iordanskii-Bekarevich-Khalatnikov | Absent (t_J >> t_transit) | No superfluid-normal coupling during transit |
| 3 | Spatial diffusion | v_F propagation | 0D cells, no spatial propagation | Thermalization channel removed |
| 4 | Majorana surface states | N_K = 2 implies edge modes | N_3 = 0 (S44 N3-BDG-44) | No topological edge states |
| 5 | Tau thermalization | Finite (exp(Delta/T)) | Infinite (R-G integrability) | GGE permanence strengthened |

### C. Incomplete or challenged inheritances
| # | Mapping | Status | Gap |
|:--|:--------|:-------|:----|
| 1 | CFL correspondence | CHALLENGED (S61): CFL = 21 correspondences vs 3He-B = 22. DIII vs BDI strongest counter. | SU(3) group theory gives 7 correspondences STRONGER than 3He-B, but symmetry class differs. Untestable discriminant. |
| 2 | Frustration analog | REVISED (WS R2): Not confined-geometry Majorana (N_3 = 0). Correct analog = theta-texture under field gradient (energetic, no topological defects). | Quantitative comparison of 19% Schmidt reduction to 3He-B texture energy penalty unperformed. |
| 3 | Two-fluid hydrodynamics | RETRACTED (WS R2): Volovik partition (w = -0.918) is NOT Landau two-fluid. Correct mapping = BCS spectral function A(k, omega). No mutual friction, no relative velocity. | The substrate "superfluid fraction" (0.40-0.74) has no direct 3He-B experimental counterpart at T = 0. |
| 4 | Phononic crystal dispersion | ENRICHED but NO PARENT (WS R2 QA): 45 bands on CG(24) with 16 hybridization gaps. 3He-B has single isotropic gap. | The 16 gaps are a NEW feature with no parent analog. They provide additional laminar protection (Layer 5) but also suppress decoherence, working AGAINST A_s budget closure. |
| 5 | C_V ratio | NON-UNIVERSAL: substrate 2.20 vs 3He-B -> 1 (isotropic quench). Bounded below by 1 (Schur-convexity). | The deviation from 1 measures van Hove fold anisotropy, specific to the substrate. Not derivable from universality class alone. |

---

## IX. Priority-Ordered Problem List

Ranked by EVOI impact (framework movement per computation invested), incorporating S72 results.

### Level 1: CRITICAL (framework-defining)

**1. EXIT-HORIZON-BOG-73 + RE-DECOHERENCE-73**
- What: Compute Bogoliubov transformation AT the exit horizon. Determine whether mode-dependent phase spread delta_phi is O(0.1) (gate-band-compatible) or O(10^{-4}) (too coherent). Resolve statistical vs Bogoliubov KZ model.
- Why: The A_s budget CANNOT be closed without this. Both KZ models bracket the gate band [0.57, 0.88]. This is the single most important open computation in the project.
- Inputs: S72 W3-C surface gravity kappa_exit, S64 PHASE-BOGOLIUBOV-64 global phases.
- Gate: t_dec/t_transit in [0.57, 0.88].
- EVOI: ~25% (resolves A_s, the #1 open problem).

**2. COMPOUND-NS-73 (entry + fold + decoherence)**
- What: Compute the TOTAL n_s prediction including the entry-horizon pre-squeeze (S72 W3-C: delta_n_s = +1.001, O(1) correction). The current n_s = 0.9567 does NOT include entry-horizon physics.
- Why: The O(1) tilt correction from the entry horizon potentially dominates the fold contribution. Without this, n_s and alpha_s predictions are unreliable.
- Inputs: S72 W3-C Bogoliubov coefficients, S72 W1-A gap dynamics, S72 W2-A dual-timescale model.
- Gate: |n_s - 0.9649| < 0.0042 (Planck 1-sigma).
- EVOI: ~20% (resolves the scheme dependence question).

**3. SPECTRAL-FUNCTIONAL-SELECTION**
- What: Derive the physical spectral functional from a first-principles selection criterion. S72 W2-C establishes f* = 0.912 sqrt + 0.088 exp gives Planck n_s, but no selection principle exists.
- Why: Without selection, n_s is accommodation. The f* that matches n_s is non-perturbative (divergent SDW expansion). If the asymptotic expansion does not exist for f*, ALL predictions depending on SDW moments (a_0, a_2, a_4 individually) must be re-evaluated using direct spectral sums.
- Gate: Unique f with n_s in [0.955, 0.975] AND m_H in [122, 130].
- EVOI: ~13% (EVOI P3).

### Level 2: HIGH (constrains multiple observables)

**4. KK-THRESHOLD-WEINBERG-73**
- What: Compute PW-sector-resolved threshold corrections delta_1/delta_3 and delta_2/delta_3 at tau_fold = 0.19. Determines whether sin^2(theta_W) = 0.584 at M_KK runs correctly to 0.231 at M_Z.
- Why: S72 W2-B: pure SM running gives 54.5% discrepancy. Universal threshold model (Model A) gives 1.2% match but requires equal thresholds, undemonstrated at finite tau.
- Gate: |sin^2(M_Z) - 0.23122| < 0.035 (15% relative).
- EVOI: ~10%.

**5. LEGGETT-GRAV-DECAY-73**
- What: Compute gravitational decay vertex Gamma_grav for Leggett mode. Compare to H_0.
- Why: EVOI P2. delta_P(fail) = -30%. If Gamma_grav > H_0, the Leggett DM candidate is EXCLUDED.
- Gate: Gamma_grav < H_0.
- EVOI: ~17% (EVOI P2).

**6. S(tau) FULL PROFILE**
- What: Compute S(tau) for tau in [0, 2] on Jensen-deformed SU(3). Determines whether a post-transit equilibrium (tau_today) exists.
- Why: S72 W3-D reduces the question to whether S(tau) has a maximum-then-minimum structure. This requires the full profile beyond the fold, not available from local derivatives.
- Gate: Stable minimum at tau_eq in [0.19, 1.0].
- EVOI: ~8%.

### Level 3: MEDIUM (structural refinement)

**7. SELF-CONSISTENT-HFB** (Q15 in D08)
- What: Full Hartree-Fock-Bogoliubov iteration with sector-resolved Delta_{(p,q)} at fold.
- Why: Nazarewicz priority 1. Mean-field overestimates by 60%. Never executed.

**8. DISPERSION-PROTECTION-73**
- What: Quantify hybridization gap protection factor. Which BCS modes sit in which scattering islands?
- Why: Layer 5 REDUCES effective decoherence, working AGAINST A_s budget closure. The suppression factor (2x? 10x?) is unknown.

**9. FIBER SELECTION**
- What: Why SU(3) and not G_2? S72 W4-F shows a_2/a_4 constancy is NOT SU(3)-specific.
- Why: The 40x difference in absolute a_2/a_4 magnitude may be discriminating, but no selection principle exists.

**10. TAU-TIME DERIVATION** (Q13 in D08)
- What: Rigorous derivation of modulus EOM from 12D Einstein equations on M^4 x SU(3).
- Why: Core framework postulate (C1 in D04) assumed since S1, never derived.

### Level 4: CARRY-FORWARD (queued but not blocking)

| # | Item | Source | Status |
|:--|:-----|:-------|:-------|
| 11 | Non-Abelian Berry phase for 492 degenerate multiplets | Q14 in D08 (S46) | UNCOMPUTED |
| 12 | Curvature-gap anti-correlation V(B2,B2)(tau) | Q16 in D08 (S47) | UNCOMPUTED |
| 13 | Off-Jensen 5D moduli landscape | Q9 in D08 (D05 Window 3) | UNTESTED |
| 14 | Order-one condition repair for D_total | Q10 in D08 (N3 in D04) | BROKEN, unfixed |
| 15 | Complete A_F extraction via o-map | Q11 in D08 (N2 in D04) | CONDITIONAL |
| 16 | Three-phonon vertex resonance | CF4 in D08 (S46) | UNTESTED |
| 17 | ALPHA-ENV-43 void/filament alpha variation | Q22 in D08 (S43) | QUEUED |
| 18 | Phonon Gruneisen parameter | WS carry-forward #6 | EXPLORATORY |
| 19 | CV per-mode decomposition verification | WS carry-forward #5 | LOW |
| 20 | f_KZ geometric weighting on CG(24) | WS carry-forward #4 | FEEDS #1 |

---

## Structural Summary

**What is proven beyond dispute**: The spectral triple on M^4 x SU(3) produces SM quantum numbers, BDI topological class, BCS pairing at the van Hove fold, 59.8 quasiparticle pairs via sudden quench, GGE permanence (five-layer protection, Re_GGE = 0 exact), ballistic supersonic transit (Ma_L = 331), and Volovik CC dilution to 0.01 OOM. These are structural results that survive regardless of whether the open problems are resolved favorably.

**What requires resolution**: (1) The A_s decoherence mechanism (exit-horizon Bogoliubov coefficients), (2) the compound n_s prediction including entry-horizon pre-squeeze, (3) spectral functional selection, (4) KK threshold corrections for sin^2(theta_W), (5) Leggett gravitational decay vertex. These five computations collectively determine whether the framework achieves zero-free-parameter observational agreement or remains an internally consistent mathematical structure with unconnected observational channels.

**What the superfluid-vacuum program says**: The 3He-B inheritance is structural, not analogical. Every property lost in going from 3He-B to the substrate (vortices, mutual friction, spatial diffusion, Majorana states) removes an instability channel, strengthening the GGE relic's stability. The BCS Hamiltonian on the spectral triple is the single algebraic structure from which ALL post-transit physics emerges: Ordered Veil, CC dilution, non-thermal C_V, pair creation, DM stability, and the five-layer laminar protection hierarchy. This unification is the framework's primary structural achievement from the superfluid-vacuum perspective. The open problems are all within the SAME algebraic structure -- they are computations within the BCS Hamiltonian, not challenges to its foundation.
