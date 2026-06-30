# Session 72 — Schwarzschild-Penrose Causal Structure Synthesis

**Date**: 2026-04-10
**Author**: Schwarzschild-Penrose Geometer
**Sources**: S72 results working paper (20 gate verdicts), S72 laminar flow workshop (Volovik x QA), Phononic-Penrose-Diagrams.md, pre-registered-observations.md, constraint-mega-matrix.md
**Prior causal results**: S70 4-panel Penrose sequence (sonic horizons at {0.160, 0.220}), S71 entry horizon featureless + frozen moments + GSL + chirp universality

---

## Section 1: Session Overview and Gate Verdict Summary

Session 72 executed 20 gate computations across 4 waves plus one 2-agent workshop (Volovik x Quantum-Acoustics: laminar flow mapping). The session addressed three structural questions from the causal perspective:

(i) Does the three-way observational consistency at tau = 0.19 survive scrutiny? (W1-E)
(ii) What is the decoherence architecture of the acoustic white hole exit? (W1-A, W2-A, W3-C, W4-A, workshop)
(iii) What is the entanglement geometry of the BCS fabric? (W4-C, W4-D)

### Gate Verdicts (20 total)

| Gate | Wave | Verdict | Key Number |
|:-----|:-----|:-------:|:-----------|
| KAPPA-DELTA-72 | W1-A | INFO | t_dec/t_transit = 5.5e9 (gap curvature dead) |
| GILKEY-REEVAL-72 | W1-B | INFO | delta = 13.3% (S71 PASS downgraded) |
| ZETA-RATIO-CONVERGENCE-72 | W1-C | PASS | a_6/a_4 = 0.223 at L=7, monotone decreasing |
| CAUCHY-SCHWARZ-W0-72 | W1-D | FAIL | w_0 formula disconnected from Volovik partition |
| TAU-FOLD-CONSISTENCY-72 | W1-E | PASS | Three-way overlap at [0.189, 0.191] |
| DUAL-DECOHERENCE-72 | W2-A | INFO | delta_OOM = 1.69 at physical t_dec; target needs 0.716 |
| WEINBERG-72 | W2-B | FAIL | 54.5% discrepancy (pure SM); 1.2% with universal thresholds |
| SPECTRAL-FUNCTIONAL-FIT-72 | W2-C | PASS | f* = 0.912 sqrt + 0.088 exp, ||residuals|| = 1.3e-14 |
| INSTANTON-KAPPA-72 | W2-D | INFO | kappa(peak) = 1.057 (marginal); large rho viable |
| BCS-DRESSED-SA-72 | W3-A | INFO | delta_n_s = 3.8e-6 (mode-selective; BCS negligible) |
| ASYMPTOTIC-TRUNCATION-72 | W3-B | INFO | SDW series asymptotic (ratio monotone increasing) |
| BLUESHIFT-TILT-72 | W3-C | PASS | delta_n_s = +1.001 (O(1) correction from entry horizon) |
| TAU-EQUILIBRIUM-72 | W3-D | INFO | BCS/spectral = 7.9e-5 (tau_eq is geometric) |
| MODULAR-CHIRP-72 | W3-E | FAIL | 8.4 OOM discrepancy (incommensurable quantities) |
| DECOHERENCE-BISPECTRUM-72 | W4-A | PASS | f_NL = -0.313 (Planck-safe by 80x) |
| CV-SCALING-72 | W4-B | INFO | alpha = 0.013 (flat; GGE saturates at 2.20 for N >= 8) |
| FRUSTRATION-SCHMIDT-72 | W4-C | PASS | K(frustrated) = 3.234 > 2.0 |
| ISLAND-GRAPH-72 | W4-D | PASS | Area law R^2 = 0.988; monogamy-min R^2 = 0.996 |
| CG24-GGE-ENTROPY-72 | W4-E | INFO | S_cell = 2.21 nats; Ordered Veil f_OV = 0.26-0.60 |
| G2-CONSTANCY-72 | W4-F | FAIL | G_2 MORE constant than SU(3) (1.93% vs 2.92%) |

**Summary**: 7 PASS, 3 FAIL, 10 INFO. The PASS results are structurally significant: the three-way tau consistency (W1-E), the entry horizon tilt (W3-C), the area law on CG(24) (W4-D), the frustrated entanglement survival (W4-C), the non-Gaussianity (W4-A), the spectral zeta convergence (W1-C), and the spectral functional existence (W2-C). The FAILs close specific conjectured connections (Cauchy-Schwarz to w_0, modular chirp to S71 chirp, G_2 specificity). The INFO verdicts refine quantitative knowledge without resolving structural questions.

---

## Section 2: Causal Structure Analysis of S72 Results

### 2.1 The Acoustic White Hole: Updated Causal Diagram

The S70 Penrose sequence established the acoustic causal structure: sonic horizons at tau_sonic = {0.160, 0.220}, supersonic region Delta_tau = 0.060, acoustic white hole at the fold (Ma = 54.73), null cone opening 2.09 degrees. S71 established that the entry horizon at tau = 0.2195 is spectrally featureless (no eigenvalue crossings, all gaps open) and that causal structure is kinematic (velocity-driven), not spectral (moment-driven).

S72 reshapes the causal picture in three ways.

**First**: W3-C (BLUESHIFT-TILT-72 PASS) establishes that the entry sonic horizon is NOT a negligible perturbation. The entry-horizon squeeze parameters r_entry in [2.904, 2.937] are COMPARABLE to the fold squeeze r_compound in [2.330, 4.320]. The entry horizon temperature T_entry = 72.84 M_KK places all BCS modes in the deeply thermal regime (omega/T = 0.012, |beta_k|^2 in [83, 89]). The tilt correction delta_n_s = +1.001 is O(1) in absolute terms. The S70 4-panel Penrose diagram (Diagram C from the Phononic-Penrose-Diagrams framework document) must be annotated: the entry horizon at tau = 0.220 is not merely a causal boundary but a SQUEEZE STAGE with thermal occupation comparable to the fold itself. The transit is a TWO-STAGE squeeze: entry horizon pre-squeeze followed by fold amplification.

In the language of Penrose diagrams: the entry horizon is an event horizon of the acoustic white hole. The squeeze at the entry horizon is the acoustic analog of pair creation at the white hole horizon. What S72 adds is that this pair creation is not the tiny Hawking effect one might expect -- it is deeply thermal, with |beta|^2 ~ 85 particles per mode. The white hole is not merely a formal construct; it is a copious particle source.

**Second**: The laminar flow workshop (Volovik x QA) establishes the converged Mach hierarchy:

    Ma_Leggett = v_tau / c_L = 8.27 / 0.025 = 331
    Ma_BA = v_tau / c_BA = 8.27 / 0.399 = 20.7
    Ma_BLV = v_tau / c_BLV = 8.27 / 0.485 = 17.1
    Ma_fold = v_tau / c_s = 54.73 (at fold, where c_s is the BCS sound speed)

The Landau critical velocity v_L = c_L = 0.025 M_KK is the Leggett speed -- the slowest collective mode sets the pair-creation threshold. The Ma_Landau = 331 means the transit is supercritical with respect to ALL four speeds. The four-stage pair creation cascade follows:

```
  tau decreasing →

  VACUUM          LEGGETT PAIRS     BA PHONON PAIRS    FULL BCS
  (no excitation)  (DM creation)     (31 modes @ |β|²=1.015)  (N_pair=59.8)
       |                |                  |                  |
    v < c_L          v = c_L            v = c_BA           v = c_BLV
       |                |                  |                  |
  Ma_L < 1          Ma_L = 1           Ma_BA = 1          Ma_BLV = 1
```

This cascade is the temporal ordering of pair creation on the acoustic Penrose diagram. Reading the diagram from past (tau large, pre-transit) to future (tau small, post-transit): first the Leggett modes go supercritical, then the Bogoliubov-Anderson modes, then the full BCS sector. The entry sonic horizon at tau = 0.220 corresponds to Ma_BA = 1 (the Anderson-Bogoliubov crossing), while the fold at tau = 0.190 is deeply supercritical for all modes.

**Third**: The workshop establishes Re_GGE = 0 EXACTLY (from Richardson-Gaudin integrability). This is the definitive statement about the post-transit causal structure: Ma >> 1 and Re = 0 simultaneously. The spectral flow is BALLISTIC SUPERSONIC -- it passes through the phononic crystal without scattering, like a photon traversing a transparent medium. The acoustic white hole produces pairs (Ma >> 1, Landau criterion satisfied), but the pairs do not thermalize (Re = 0, integrability prevents mode-mode scattering). This is the geometric content of the Ordered Veil: it is the statement that the acoustic metric has a white hole with copious Hawking radiation, but the radiation cannot re-enter the horizon (the white hole horizon is one-way) and cannot scatter with itself (integrability). The post-transit state is a coherent GGE, not a thermal bath.

### 2.2 The tau-Fold as a Caustic: W1-E Three-Way Consistency

W1-E establishes that three independent observational channels -- gauge coupling ratio g'/g, spectral tilt n_s, and dark energy equation of state omega_L -- overlap at tau in [0.189, 0.191], with tau_fold = 0.19 inside this window. The overlap width Delta_tau = 0.0013 is set by the n_s channel (the tightest constraint, sigma_tau = 0.011).

From the causal structure perspective, this three-way overlap has a geometric interpretation. The fold at tau = 0.190 is a CAUSTIC of the spectral flow -- the point where the van Hove singularity creates a density of states divergence. A caustic is where null geodesics of the acoustic metric focus. The statement that three observables converge to the same tau is the statement that the fold caustic determines all three:

- n_s = 0.9567 is set by the spectral action gradient at the caustic: eps_H = (dS/dtau)^2 / (2 S d^2S/dtau^2) evaluated at the fold. This is a GEOMETRIC property of the caustic (the curvature of the spectral action along the modulus direction).

- g'/g = exp(-2tau) is set by the Jensen deformation at the caustic. This is a TOPOLOGICAL property (the exponential map on the Lie algebra at the fold point).

- omega_L is set by the spectral functional's sensitivity to tau through g^2(tau), with d(ln omega_L)/d(tau) = 1.000. This is a SPECTRAL property (the first spectral moment's tau-dependence).

The three-way overlap at a single tau is the statement that the fold caustic is SIMULTANEOUSLY a geometric, topological, and spectral locus. In the Penrose diagram framework: the fold is a distinguished point on the modulus space conformal diagram (Diagram B) where the acoustic null cones collapse to 2.09 degrees, the BCS condensate freezes, and all three observational channels converge. It is the geometric analog of a focal point -- a point determined by the global structure of the spacetime, not by local dynamics.

The 34.6% gap between the 1-loop SM sin^2(theta_W) at M_KK (0.382) and the Baptista boundary condition (0.584) -- quantified by W2-B (WEINBERG-72 FAIL) -- is the KK threshold correction that the framework requires at this caustic. The universal threshold model (Model A: equal corrections across gauge groups) achieves 1.2% agreement, but requires SU(3) x SU(3) symmetry that is broken at tau = 0.19. This 34.6% gap is a GEOMETRIC deficit of the caustic: the fold's Jensen deformation creates an asymmetry between gauge sectors that pure SM running cannot bridge. The KK tower threshold corrections must restore this symmetry. Whether they do is computable from the Peter-Weyl spectrum but has not yet been computed -- this is the highest-priority follow-up from the causal perspective.

### 2.3 The Decoherence Architecture of the Exit Horizon

The S72 workshop produced a nine-channel decoherence hierarchy for the exit sonic horizon. From the causal structure perspective, this hierarchy has a clear geometric organization.

The exit horizon (tau approximately 0.160, Ma = 1 outbound) is where the supersonic region ends. In the acoustic Penrose diagram, this is the WHITE HOLE horizon -- the boundary past which no acoustic signal from the supersonic interior can propagate. The decoherence that controls the A_s amplitude is the process by which information about the coherent squeeze state is lost as it crosses this horizon.

The nine channels, organized by their causal origin:

**Channels originating AT the horizon** (surface gravity effects):
1. KZ pair-crossing spread: t_dec/t_transit ~ 0.13 (statistical) or ~ 2.2 (Bogoliubov). This is the spread in CROSSING TIMES across the horizon -- different pairs cross at different tau, acquiring different phases. The gate band [0.57, 0.88] sits between the two models.
2. Hawking broadening: t_dec/t_transit ~ 45 (corrected from 2.8 using squeezed-state phase variance). Thermal character of Hawking radiation at the horizon. Too slow.
3. Andreev standing wave: t_dec/t_transit ~ 336. Retroreflection at the subsonic boundary. Too slow.

**Channels originating BEYOND the horizon** (post-horizon propagation):
4. Cell-crossing acoustic: t_dec/t_transit = 6.73. Acoustic signals traversing Voronoi cells on CG(24). Too slow by 9.4x.
5. Leggett phase diffusion: t_dec/t_transit ~ 1.3e4. Inter-band phase oscillation. Dead.
6. Dispersion mode conversion: t_dec/t_transit ~ 4200. Hybridization gap crossings. Dead.

**Channels originating BEFORE the horizon** (pre-horizon dynamics):
7. Gap curvature (kappa_Delta): t_dec/t_transit = 5.5e9. Gap amplitude variation through the fold. Dead (W1-A).
8. Josephson anisotropy: Second-order modifier to KZ, not an independent channel. Demoted.

**Channels originating IN the spectrum** (spectral properties):
9. BCS dressing: delta_n_s = 3.8e-6. Mode-selective correction. Negligible.

The geometric lesson: only channels originating AT the horizon are fast enough. The horizon IS the regulator of the white hole's overproduction (S71 result confirmed: "the horizon determines what escapes, not what is produced"). The A_s amplitude is set by the exit horizon's surface gravity and the pair-crossing distribution across that horizon.

The critical open question -- statistical (1/sqrt(N_pair)) versus Bogoliubov (delta_phi/delta_omega) model of the pair-crossing spread -- maps to a question about the CAUSAL STRUCTURE at the horizon. In the statistical model, pairs are created as independent events (Poisson process at the horizon). In the Bogoliubov model, pairs are created by a single coherent transformation (all phases locked to phi = pi with spread 2.4e-4). The S64 result (PHASE-BOGOLIUBOV-64: phi_Bog = pi exactly, delta_phi = 2.4e-4 in the sudden-quench limit) favors the Bogoliubov model. But this is the GLOBAL Bogoliubov transformation -- the LOCAL transformation at the exit horizon may have larger phase spread due to the local surface gravity kappa_exit.

In Penrose diagram language: the global Bogoliubov transformation connects the in-vacuum (tau >> tau_fold, pre-transit) to the out-vacuum (tau << tau_fold, post-transit). The exit-horizon Bogoliubov transformation connects the in-vacuum to the intermediate state at the horizon. These are DIFFERENT transformations. The S64 delta_phi = 2.4e-4 is for the global transformation; the horizon transformation has untabulated coefficients determined by kappa_exit. The resolution requires computing the greybody factor of the acoustic white hole -- the frequency-dependent transmission amplitude through the exit horizon. This is the RE-DECOHERENCE-73 computation.

---

## Section 3: Area Law and Entanglement Structure

### 3.1 W4-D Island Graph: Area Law with Monogamy Crossover

The CG(24) Cayley graph of S_4 carries the substrate's tessellation structure. W4-D establishes that the entanglement entropy of a bipartition A|B follows an AREA LAW (S proportional to the number of cut edges n_cut) with R^2 = 0.988, decisively beating the volume law (R^2 = 0.970). The best model is monogamy-capped area law (R^2 = 0.996).

From the causal structure perspective, the area law on CG(24) is the ANALOG of the Bekenstein-Hawking area law on a black hole horizon, mediated through the substrate picture. The mapping:

| Black hole | Substrate fabric |
|:-----------|:----------------|
| Event horizon area A | Cut surface n_cut (number of boundary edges) |
| Bekenstein-Hawking entropy S = A/4G | S_ent = s_edge * n_cut - gamma_topo |
| Planck area l_P^2 | Josephson junction entropy s_edge = 1.291 nats |
| Topological entropy gamma_topo | gamma_topo = -5.835 nats (negative, from monogamy) |

The negative topological entropy (gamma = -5.835, unlike the positive +19.07 from S64) arises because the monogamy bound S_max = 5.545 nats per vertex (8 BCS modes, 2^8 states) caps the entanglement at small subsystems. For |A| <= 3, every boundary vertex has degree 6, so the bare entropy 6 * 1.386 = 8.315 nats EXCEEDS the monogamy bound. The system is in the monogamy-saturated regime: entanglement per vertex is maximized, and the entropy is proportional to |A| (volume law), not n_cut (area law). The crossover to genuine area law occurs at |A| ~ 7.5 vertices, where monogamy releases because vertices share neighbors within A.

This monogamy crossover is the substrate analog of the Page curve. On the fabric:

```
  S_ent                                    
  (nats)   Monogamy     Crossover    Area law
    50  ─                          ─────────── |A| = 12 (half system)
        |              /
    40  ─            /
        |          /
    30  ─        / 
        |      /
    20  ─    /
        |  / 
    10  ─/    
        |
     0  ┼─────┼─────┼─────┼─────┼─────┼─── |A|
        0     2     4     6     8    10   12
              ^                ^
          Monogamy         Crossover
          saturated       at |A| ~ 7.5
          (volume law)    (to area law)
```

The Page curve rises monotonically and saturates at |A| = 12 (the half-system size for CG(24) with 24 vertices). This is the expected behavior for a GAPPED system with area-law entanglement -- not a black hole analog (which would show a turnover and descent after the Page time). The substrate fabric is a gapped BCS condensate, not a thermal system, and its entanglement structure reflects this: entropy is carried by Josephson junctions (boundary edges) and bounded by the finite Hilbert space per cell.

The structural content: the area law on CG(24) is a consequence of the BCS gap. Gapped systems have exponentially decaying correlations, which produce area-law entanglement. The area law coefficient s_edge = 1.291 nats/edge is set by the per-junction quantum entanglement (S71: S_vN = 1.386 nats per junction). The monogamy bound is set by the per-cell Hilbert space dimension (2^8 = 256). These are both GEOMETRIC properties of the spectral triple -- the area law is not imposed but derived from the BCS structure of the fiber.

### 3.2 W4-C Frustration: Entanglement Survives Geometric Phase Winding

The frustrated 3-cell ring (C_3 topology) has K(frustrated) = 3.234, a 19% reduction from the unfrustrated K(2-cell) = 3.988. The frustration effect is PURE -- adding a third cell without ring closure gives K = 3.986 (negligible reduction), so the 19% comes entirely from the odd-cycle geometric phase winding.

From the causal perspective, the frustrated ring is a TOPOLOGICAL OBSTRUCTION to simultaneous minimization of all three Josephson junction energies. The classical ground state has 120-degree phase separation (each cell's BCS phase differs by 2pi/3 from its neighbors), with frustration energy E_frust = +1.40 M_KK per bond versus E_aligned = -2.80 M_KK. The quantum entanglement (Schmidt number K) survives this obstruction because the Josephson pair-tunneling Hamiltonian generates entanglement regardless of the classical phase configuration.

The S71 GSL result (S_gen monotone increasing through all 4 stages of frustrated ring evolution) combines with W4-C: the generalized second law holds on the frustrated ring because the entanglement entropy S_vN = 1.836 bits (frustrated) is still substantial. The area decrease of 0.002 nats at the Stage 3 to 4 transition (the analog of black hole area loss to superradiance) is overwhelmed by matter entropy growth. The GSL is structurally robust against frustration.

The causal implication: geometric frustration on the CG(24) fabric does not create naked singularities in the entanglement structure. The BCS gap (Delta = 0.464 M_KK) exceeds the frustration penalty per bond (approximately 0.47 M_KK per bond), maintaining the gap protection that underlies the area law. The fabric's entanglement structure is CENSORED -- frustration cannot expose the bare vacuum, just as cosmic censorship prevents the exposure of singularities.

---

## Section 4: Entry/Exit Horizon Geometry

### 4.1 W3-C Entry Horizon: Deep Thermal Occupation

The entry sonic horizon at tau = 0.2195 has surface gravity kappa_v = 457.66 M_KK^2 (from S71), giving Hawking temperature T_entry = kappa_v/(2pi) = 72.84 M_KK. All BCS modes are in the deeply thermal regime:

| Mode | omega_k (M_KK) | omega/T | |beta_k|^2 | r_entry |
|:-----|:---------------|:--------|:----------|:--------|
| B1 | 0.876 | 0.0120 | 82.7 | 2.904 |
| B2 | 0.839 | 0.0115 | 86.3 | 2.925 |
| B3 | 0.818 | 0.0112 | 88.5 | 2.937 |

The entry-horizon squeeze parameters r_entry in [2.904, 2.937] are comparable to the fold compound squeeze r_compound in [2.330, 4.320]. This is not a small perturbation. The entry horizon is a MAJOR squeeze stage.

Causal interpretation: The entry horizon is the outer boundary of the acoustic white hole. Modes approaching the fold from the subsonic region (tau > 0.220) encounter the sonic horizon, where the null cones of the acoustic metric begin to tilt. At the horizon, one family of null geodesics becomes trapped -- they can enter the supersonic region but cannot escape. The pair creation at this horizon (|beta|^2 ~ 85 per mode) is the acoustic Hawking effect. S71 established that this horizon is spectrally featureless (no eigenvalue crossings, all gaps open), confirming it is a KINEMATIC event (driven by the velocity field), not a spectral event (driven by eigenvalue structure).

The tilt correction delta_n_s = +1.001 from the entry horizon has a geometric origin: the mode-dependent squeeze dr_entry/d(ln omega) = -0.500 (exact analytic) creates a spectral tilt that adds to the fold's native red tilt. The entry/fold tilt ratio is 1.7%, but the absolute magnitude is O(1) because the fold slope is steep (-58.79 per unit ln omega). The sign is POSITIVE (redder): lower-frequency modes (B3, omega = 0.818) are more squeezed than higher-frequency modes (B1, omega = 0.876) by delta_r = 0.034.

**Updated multi-stage squeeze sequence**:

```
   ENTRY HORIZON          FOLD              EXIT HORIZON
   tau = 0.220           tau = 0.190        tau = 0.160
       |                    |                    |
   r ~ 2.9              r ~ 2.3-4.3          (decoherence)
   |beta|^2 ~ 85        N_pair = 59.8        regulator
   delta_n_s = +1.0     delta_n_s = -58.8    delta_OOM -> A_s
       |                    |                    |
   PRE-SQUEEZE          AMPLIFICATION        REGULATION
```

The three stages are causally ordered on the acoustic Penrose diagram: the entry horizon is in the causal PAST of the fold, which is in the causal past of the exit horizon. Information about the squeeze state propagates from entry to fold to exit along the acoustic null geodesics. The entry horizon PREPARES the state that the fold amplifies; the exit horizon REGULATES what escapes.

### 4.2 Laminar Flow Workshop: Five-Layer Protection Hierarchy

The workshop's central structural result is the five-layer laminar protection hierarchy:

| Layer | Mechanism | Suppression | Status |
|:------|:----------|:------------|:-------|
| 1 | Richardson-Gaudin integrability | Gamma = 0 exact | PERMANENT |
| 2 | BDI Z_2 gap protection | Delta > 0 always | PERMANENT |
| 3 | CG(24) energy + momentum conservation | f ~ 1% of phase space | PERMANENT |
| 4 | 0D cell geometry (no spatial propagation) | t_J/t_transit = 949 | PERMANENT |
| 5 | 16 hybridization gaps (phase space fragmentation) | ~17 disconnected islands | PERMANENT |

All five layers are PERMANENT structural results. Their combined effect: even with hypothetical integrability-breaking at epsilon_break ~ exp(-S_inst), the effective scattering rate is Gamma_eff ~ 10^{-72} M_KK. The mean free path l_mfp ~ 10^{55} meters -- 10^{29} times the observable universe. The Ordered Veil is protected to absurd precision.

The causal content: Ma >> 1 and Re = 0 simultaneously. The transit is BALLISTIC SUPERSONIC -- the spectral flow passes through the phononic crystal without scattering. In the acoustic Penrose diagram, this means the null geodesics within the supersonic region are STRAIGHT LINES (no scattering deflects them). The acoustic metric inside the white hole is conformally flat in the integrable limit, because the absence of scattering means acoustic perturbations propagate freely. The only deviation from conformal flatness comes from the spatially varying sound speed c_s(tau), which creates the acoustic curvature that bends the null cones.

The five layers map to five independent constraints on the acoustic Penrose diagram:

- Layer 1 (integrability): null geodesics do not scatter (no vertex corrections to the acoustic propagator).
- Layer 2 (gap protection): the acoustic metric is non-degenerate at all tau (the gap ensures c_s > 0 everywhere inside the BCS window).
- Layer 3 (CG(24) kinematics): only 1% of mode triples satisfy conservation laws on the Cayley graph (the Brillouin zone is too sparse for efficient scattering).
- Layer 4 (0D cells): no spatial propagation within a cell (the acoustic metric has no spatial extent within each fiber).
- Layer 5 (hybridization gaps): inter-branch scattering is gapped (the acoustic dispersion has band gaps that prevent energy transfer between branches).

### 4.3 The Surviving Decoherence Question

After S72, the decoherence architecture reduces to a single open question: the exit-horizon pair-crossing model. The statistical estimate (t_dec/t_transit ~ 0.13, over-decohered) and the Bogoliubov estimate (t_dec/t_transit ~ 2.2, under-decohered) bracket the gate band [0.57, 0.88]. The resolution requires the EXIT-HORIZON Bogoliubov coefficients beta_k(tau_exit), which differ from the global coefficients computed in S64 because they depend on the local surface gravity kappa_exit rather than the global fold geometry.

This is a well-posed geometric computation: determine the mode-dependent transmission amplitude (greybody factor) through the exit sonic horizon. In the acoustic Penrose diagram, this is the PEELING analysis of outgoing modes at the exit horizon -- computing how much of each squeezed mode's amplitude escapes the white hole and how much is reflected back. The greybody factor depends on the acoustic potential barrier at the horizon, which is set by kappa_exit and the mode frequency omega_k.

---

## Section 5: Structural Implications and Carry-Forward

### 5.1 Hard Walls Established or Confirmed

S72 establishes or confirms the following hard boundaries:

1. **Gap amplitude decoherence is dead**: W1-A proves t_dec(gap)/t_transit = 5.5e9 (eleven orders of magnitude too slow). The BCS gap varies by only 0.5% across the transit. This is a PERMANENT closure: gap amplitude dynamics cannot contribute to the A_s budget.

2. **BCS dressing of n_s is negligible**: W3-A v2 proves delta_n_s = 3.8e-6 from mode-selective BCS. Only 16/155,984 weighted modes participate in BCS pairing. The bare n_s prediction stands.

3. **SDW expansion is asymptotic**: W3-B establishes the ratio sequence |a_{2k+2}/a_{2k}| is monotonically increasing at all tested L_max. Combined with W2-C (best-fit f* has divergent SDW moments), this means all predictions depending on a_6 or higher moments must use direct spectral sums, not the SDW expansion.

4. **Five-layer laminar protection**: The workshop proves Gamma_eff ~ 10^{-72} M_KK. The Ordered Veil is structurally permanent.

5. **a_2/a_4 near-constancy is NOT SU(3)-specific**: W4-F proves G_2 is MORE constant (1.93%) than SU(3) (2.92%) under Jensen-type deformation. This removes a_2/a_4 constancy as a fiber selection criterion.

### 5.2 Soft Boundaries Refined

1. **A_s decoherence**: The exit-horizon pair-crossing model must be resolved. Statistical (0.13) and Bogoliubov (2.2) bracket the gate band. Computation: EXIT-HORIZON-BOG-73.

2. **Weinberg angle**: Pure SM running gives 54.5% discrepancy. Universal thresholds give 1.2%. The PW-sector-resolved threshold computation determines which outcome holds. Computation: THRESHOLD-RATIO-73.

3. **Post-transit equilibrium**: Quartic spectral action models have stable minima; quadratic and cubic do not. The question reduces to the global shape of S(tau) beyond the fold. Computation: SPECTRAL-ACTION-PROFILE-73.

4. **Instanton sector**: Large instantons (rho > 1.80/M_KK) are Kasparov-compatible, but the measure peak at rho ~ M_KK^{-1} has kappa = 1.057 (marginally obstructed). The non-trivial bundle sector exists but is not dominant.

### 5.3 Connection to Prior Penrose Diagram Updates

The S72 results update the framework's nine canonical Penrose diagrams (from the Phononic-Penrose-Diagrams framework document) as follows:

**Diagram C (Acoustic Penrose)**: Annotate the entry horizon at tau = 0.220 with the thermal data from W3-C: T = 72.84 M_KK, |beta|^2 ~ 85, r ~ 2.9. The entry horizon is now established as a MAJOR squeeze stage, not merely a causal boundary. Add the four-stage pair creation cascade (Leggett at Ma_L = 331, BA, BCS).

**Diagram D (Tessellation CG(24))**: Add the W4-D area law (R^2 = 0.988), the monogamy crossover at |A| ~ 7.5, and the frustrated Schmidt number K = 3.234 from W4-C. The tessellation is now characterized by its entanglement structure: area law with monogamy saturation at small subsystems.

**Diagram B (Modulus Space)**: The W1-E three-way overlap at [0.189, 0.191] confirms the fold caustic as a triply-determined geometric locus. The W3-D equilibrium result (INFO: depends on quartic S(tau)) adds the post-transit equilibrium point at tau_eq ~ 0.49 (representative quartic model) as a CANDIDATE feature that awaits the global S(tau) profile.

### 5.4 Carry-Forward Computations (Causal Priority)

Ranked by impact on causal structure understanding:

1. **EXIT-HORIZON-BOG-73** (CRITICAL): Compute the Bogoliubov transformation AT the exit horizon. Determines greybody factor and mode-dependent phase spread. Resolves the statistical vs Bogoliubov KZ model. Input to A_s budget closure.

2. **THRESHOLD-RATIO-73** (HIGH): Compute PW-sector-resolved KK threshold corrections delta_1/delta_3 and delta_2/delta_3 at tau_fold = 0.19. Determines whether the 34.6% sin^2(theta_W) gap can be closed.

3. **SPECTRAL-ACTION-PROFILE-73** (MEDIUM): Compute S(tau) for tau in [0, 2]. Determines whether a post-transit stable equilibrium exists and at what tau.

4. **DISPERSION-PROTECTION-73** (MEDIUM): Quantify hybridization gap protection factor (Layer 5). Determines how much Layer 5 reduces effective decoherence.

5. **KZ-GEOMETRIC-73** (MEDIUM): Compute f_KZ on CG(24) with physical E_J distribution. The Josephson anisotropy modulates the KZ spread as a second-order effect.

---

## Section 6: Summary Table

| # | Topic | Finding | Causal Implication | Status |
|:--|:------|:--------|:-------------------|:-------|
| 1 | Three-way tau overlap (W1-E) | tau in [0.189, 0.191] from n_s, g'/g, omega_L | Fold caustic triply determined: geometric + topological + spectral locus | PASS |
| 2 | Gap curvature dead (W1-A) | t_dec(gap)/t_transit = 5.5e9 | Gap amplitude decoherence permanently closed; exit horizon is sole regulator | INFO (PERMANENT closure) |
| 3 | Entry horizon thermal (W3-C) | T = 72.84 M_KK, |beta|^2 ~ 85, delta_n_s = +1.001 | Entry horizon is a MAJOR squeeze stage comparable to fold; two-stage squeeze picture | PASS |
| 4 | BCS dressing negligible (W3-A v2) | delta_n_s = 3.8e-6 (16/155,984 modes) | Bare n_s prediction stands; condensate does not distort the acoustic flow | INFO |
| 5 | Dual decoherence (W2-A) | delta_OOM = 1.69 at physical; target needs 0.716 | Cell-crossing 9.4x too slow; exit horizon structure is the bottleneck | INFO |
| 6 | Area law on CG(24) (W4-D) | R^2 = 0.988; monogamy-min R^2 = 0.996 | Bekenstein area law analog on fabric; monogamy crossover at |A| ~ 7.5 | PASS |
| 7 | Frustrated entanglement (W4-C) | K(frustrated) = 3.234 (19% reduction) | BCS gap censors frustration; no naked singularities in entanglement structure | PASS |
| 8 | Laminar Ma = 331, Re = 0 (workshop) | Ballistic supersonic; five-layer protection | Acoustic null geodesics unscattered; Ordered Veil is structurally permanent | CONVERGED |
| 9 | Nine decoherence channels (workshop) | Only KZ fast enough; statistical (0.13) vs Bogoliubov (2.2) bracket gate band | Exit horizon greybody factor determines A_s; highest-priority open computation | OPEN |
| 10 | Spectral functional f* (W2-C) | f* = 0.912 sqrt + 0.088 exp; non-perturbative | SDW expansion does not exist for f*; CC term formally infinite; spectral action still finite | PASS |
| 11 | Zeta ratio convergence (W1-C) | a_6/a_4 = 0.223 at L=7, monotone decreasing toward Gilkey 0.25 | Finite-spectrum contamination confirmed; high-order SDW coefficients unreliable | PASS |
| 12 | f_NL Gaussian (W4-A) | f_NL = -0.313 (Planck-safe by 80x) | Laminar flow confirmed: Gaussian velocity distribution from large N_pair | PASS |
| 13 | GGE protection robust (W4-B) | C_V ratio saturates at 2.20 for N >= 8 | Non-universal (van Hove quench specific) but bounded below by 1 (Schur-convexity) | INFO |
| 14 | Ordered Veil persists (W4-E) | f_OV = 0.26-0.60; I_deficit = 34-80 nats | Fabric retains 26-60% information deficit vs thermal; CG(24) bipartite blocks frustration | INFO |
| 15 | Instanton kappa marginal (W2-D) | kappa(peak) = 1.057; large rho pass | Non-trivial bundle viable for large instantons; alpha_s remains zero at tree level | INFO |
| 16 | SDW asymptotic (W3-B) | Ratio sequence monotone increasing; N* ~ 6-7 | Past optimal truncation at a_8; direct spectral sums required for higher moments | INFO |
| 17 | tau equilibrium geometric (W3-D) | BCS/spectral = 7.9e-5; quartic models have stable minima | Post-transit equilibrium determined by S(tau) shape, not BCS condensation | INFO |
| 18 | Weinberg angle gap (W2-B) | 54.5% (pure SM) / 1.2% (universal threshold) | KK threshold corrections at the fold caustic determine outcome | FAIL (open) |
| 19 | G_2 more constant (W4-F) | G_2 variation = 1.93% < SU(3) 2.92% | a_2/a_4 constancy is rank-2 Lie group property, not SU(3)-specific | FAIL (closes selection criterion) |
| 20 | Modular chirp incommensurable (W3-E) | 8.4 OOM gap between modular and S71 chirp | Bogoliubov rotation rate and eigenvalue curvature are distinct spectral functionals | FAIL |
