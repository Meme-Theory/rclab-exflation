# Session 44 Plan: SAKHAROV-GN, CDM-CONSTRUCT, Trace-Log CC, First-Sound Imprint, Holographic Spectral Action

**Date**: 2026-03-15
**Author**: Gen-Physicist (session plan)
**Format**: Parallel single-agent computations across 7 waves
**Source**: S43 quicklook (58 computations, 7 new theorems), S43 CC workshop (12 ranked S44 gates, 10 convergent items, 5 divergent items, 5 emerged insights), S43 UV/IR workshop (Volovik+Nazarewicz on polynomial vs logarithmic functional), S43 E-vs-F audit (16 instances catalogued, HOMOG-42 most sensitive), CDM-CONSTRUCT-43 (T^{0i}=0 proof, supersedes CDM-RETRACTION and FLAT-DM), S43 collab reviews (Tesla, QF, QA, Hawking, Einstein), Sagan assessment
**Motivation**: Session 43 proved the spectral action is the wrong gravitating functional (CC workshop convergence C1), established CDM by construction (CDM-CONSTRUCT-43, T^{0i}=0), and identified the first-sound ring at 325 Mpc as the framework's sole distinctive LSS prediction. The CC remains at 113 OOM. Session 44 attacks the CC from three independent routes (Sakharov induced gravity, trace-log functional, holographic bound), formalizes the CDM construction, tests the n_s tilt mechanism (Lifshitz eta vs spectral dimension flow), and computes the Fisher forecast for the first-sound ring.
**Results file**: `sessions/session-44/session-44-results-workingpaper.md`

---

## I. Session Objective

Session 44 asks: **Does replacing the spectral action with the Sakharov trace-log functional recover G_N and reduce the CC gap, and can the framework predict n_s from the Lifshitz anomalous dimension?**

Three existential problems remain from S43:

1. **CC (113 OOM)**. S43 CC workshop: spectral action is wrong gravitating functional. UV/IR workshop: polynomial (spectral action) vs logarithmic (Sakharov) weighting accounts for ~13 orders structurally. SAKHAROV-GN-44 tests this directly. TRACE-LOG-CC-44 computes the irreducible CC gap from the trace-log. HOLOGRAPHIC-SPEC-44 tests area-law suppression.

2. **DM classification**. CDM-CONSTRUCT-43 PASS: T^{0i}=0, GGE modes carry energy but not 4D momentum, CDM by construction. S43 lambda_fs = 89 Mpc RETRACTED (category error). CDM-CONSTRUCT-44 formalizes the five-part proof and examines downstream.

3. **n_s (mechanism unidentified)**. FRIEDMANN-BCS-43: constraint surface empty, 60,861x shortfall. Two surviving routes: Lifshitz anomalous dimension (LIFSHITZ-ETA-44) and spectral dimension flow (DIMFLOW-44). Unification gate: |n_s(LIFSHITZ) - n_s(DIMFLOW)| < 0.005.

Plus one prediction pipeline: first-sound ring at 325 Mpc (FIRST-SOUND-IMPRINT-44 mechanism, FIRST-SOUND-44 Fisher forecast).

**Pre-registered master gate**:
- **SAKHAROV-GN-44**: Does the Sakharov formula give G_N within 100x of observed?
- PASS: G_N^{Sakharov} within factor 100 of G_N^{obs}. BONUS: if Sakharov and spectral action a_2 agree, cutoff function f determined.
- FAIL: G_N^{Sakharov} > 3 OOM from G_N^{obs}. Induced gravity route closed.

---

## II. Wave Structure

### Dependency Graph

```
WAVE 1 (ROOT — 5 anchors, parallel)
  W1-1: SAKHAROV-GN-44    [CC anchor: G_N from log vs poly]
  W1-2: CDM-CONSTRUCT-44   [DM: formalize T^{0i}=0]
  W1-3: LIFSHITZ-ETA-44    [n_s: anomalous dim at Lifshitz]
  W1-4: TRACE-LOG-CC-44    [CC: rho_vac from Tr ln(D_BdG^2)]
  W1-5: FIRST-SOUND-IMPRINT-44 [prediction: mechanism for 325 Mpc]
         |              |              |
         v              v              v
WAVE 2 (depends on W1-1, W1-4)
  W2-1: HOLOGRAPHIC-SPEC-44 [CC: boundary modes of KZ domains]
  W2-2: DIMFLOW-44          [n_s: spectral dimension flow]
  W2-3: EIH-GRAV-44         [CC: ADM mass of fold]
  W2-4: SINGLET-CC-44       [CC: singlet projection of GGE energy]
         |              |              |
         v              v              v
WAVE 3 (predictions, partially depends on W1-5 and W2)
  W3-1: FIRST-SOUND-44      [prediction: Fisher forecast DESI DR2]
  W3-2: COHERENT-WALL-44    [acoustics: multi-wall Bragg transfer]
  W3-3: N3-BDG-44           [topology: N_3 for BdG at fold]
  W3-4: BCS-TENSOR-R-44     [prediction: r ~ 10^{-9} from first principles]
         |              |              |
         v              v              v
WAVE 4 (diagnostics, partially depends on W1-1)
  W4-1: STRUTINSKY-DIAG-44  [diagnostic: Strutinsky smoothing plateau]
  W4-2: INDUCED-G-44        [CC: self-consistent G_N from bosonic a_2]
  W4-3: FRIEDMANN-BCS-AUDIT-44 [n_s: epsilon_H shortfall after E→F fix]
  W4-4: F-FOAM-2            [CC: non-monotone cutoff from foam]
         |              |              |
         v              v              v
WAVE 5 (medium-priority, parallel)
  W5-1: JACOBSON-SPEC-44    [CC: Jacobson mapping for GGE]
  W5-2: VORONOI-FNL-44      [prediction: f_NL from Voronoi ICs]
  W5-3: DOS-TAU-44           [diagnostic: phonon DOS across transit]
  W5-4: FRG-PILOT-44         [CC: functional RG pilot for 3-sector]
  W5-5: CUTOFF-F-44          [CC: constrain f from Sakharov + a_2]
  W5-6: HOMOG-42-RECOMPUTE-44 [E→F: rerun HOMOG with corrected H]
         |              |              |
         v              v              v
WAVE 6 (specialist + remaining, parallel)
  W6-1: CHLADNI-GGE-44      [diagnostic: spatial GGE pattern]
  W6-2: 2ND-SOUND-ATTEN-44  [acoustics: attenuation length]
  W6-3: BAYESIAN-f-44        [CC: Mittag-Leffler f posterior]
  W6-4: DM-DE-RATIO-44       [cosmology: Omega_DM/Omega_DE]
  W6-5: MULTI-T-JACOBSON-44  [thermodynamics: 8-temperature first law]
  W6-6: SPECTRAL-DIM-BAND-44 [diagnostic: d_s from polariton bands]
  W6-7: DISSOLUTION-SCALING-44 [foam: epsilon_crossover scaling]
  W6-8: VAN-HOVE-TRACK-44    [diagnostic: singularity positions]
         |              |              |
         v              v              v
WAVE 7 (assessment — LAST)
  W7-1: Sagan Assessment     [probability update from 12% prior]
```

### Task Count by Wave

| Wave | Tasks | Agents | Priority |
|:-----|:------|:-------|:---------|
| 1 | 5 | 5 | CRITICAL |
| 2 | 4 | 4 | HIGH |
| 3 | 4 | 4 | HIGH |
| 4 | 4 | 4 | HIGH/MEDIUM |
| 5 | 6 | 5 | MEDIUM |
| 6 | 8 | 6 | MEDIUM/LOW |
| 7 | 1 | 1 | META |
| **Total** | **32** | — | — |

### Standing Sentinels (no computation, monitoring)

| ID | Trigger | Instrument |
|:---|:--------|:-----------|
| W-FOAM-8 | sigma_wa < 0.172 | DESI DR3 |
| GQUEST-NULL | Any pixellon signal | GQuEST |
| SIMONS-43 | >3 sigma CMB lensing enhancement | Simons Obs |
| BICEP-R | r > 10^{-5} | LiteBIRD/CMB-S4 |

---

## III. Wave Prompts

Each wave is in a separate file for deployment:

- **Wave 1**: `sessions/session-plan/session-44-wave1.md` (5 CRITICAL anchors)
- **Wave 2**: `sessions/session-plan/session-44-wave2.md` (4 HIGH CC + n_s routes)
- **Wave 3**: `sessions/session-plan/session-44-wave3.md` (4 HIGH predictions)
- **Wave 4**: `sessions/session-plan/session-44-wave4.md` (4 diagnostics)
- **Wave 5**: `sessions/session-plan/session-44-wave5.md` (6 medium-priority)
- **Wave 6**: `sessions/session-plan/session-44-wave6.md` (8 specialist/remaining)
- **Wave 7**: `sessions/session-plan/session-44-wave7.md` (1 Sagan assessment)

---

## IV. Key Numbers (Reference Table for All Agents)

| Quantity | Value | Source |
|:---------|:------|:------|
| S_fold | 250,361 M_KK^4 | s36 |
| S(0) | 244,839 M_KK^4 | s36 |
| Delta_S | 5,522 M_KK^4 | s36 |
| M_KK (gravity) | 7.4e16 GeV | s42 |
| M_KK (gauge) | 5.0e17 GeV | s42 |
| M_KK (Bayesian mode) | 3.1e17 GeV | s43 W5-12 |
| E_exc (GGE) | 50.9 M_KK | s42 |
| n_pairs | 59.8 | s38 |
| Z_fold | 74,731 | s42 |
| E_cond | -0.115 M_KK | s38 |
| Spectral gap | 0.819 M_KK | s36 |
| B2 bandwidth | 0 (exact, Schur) | s43 |
| u_2 (second sound) | c/sqrt(3) | s43 |
| r_1 (first-sound ring) | 325 +/- 20 Mpc | s43 |
| epsilon_H (target for n_s) | 0.0176 | s43 |
| epsilon_H (BCS-only) | 1.4e-6 | s43 |
| r (BCS tensors) | ~4e-10 | s43 |
| T_B2, T_B1, T_B3 (GGE) | 0.668, 0.435, 0.178 M_KK | s43 |
| GGE T_max/T_min | 3.755 | s43 |
| T^{0i}_4D (GGE) | 0 (CDM by construction) | s43 CDM-CONSTRUCT |
| w (GGE equation of state) | 0.000 (pressureless dust) | s43 CDM-CONSTRUCT |
| Carlip L | 1.74 mm | s43 |
| epsilon_crossover (foam) | 0.014 | s43 |
| prior probability | 12% (68% CI 8-16%) | s43 Sagan |
| P(structural content) | 80-98% | s43 Sagan survival |

---

## V. Agent-Model Assignments

All physics agents use **opus**. Only the knowledge-weaver (if spawned for index rebuild) uses sonnet.

| Agent | Waves | Tasks |
|:------|:------|:------|
| volovik-superfluid-universe-theorist | W1, W2, W3, W5, W6 | SAKHAROV-GN, CDM-CONSTRUCT, N3-BDG, CUTOFF-F, DM-DE-RATIO |
| hawking-theorist | W2, W3, W4, W5, W6 | HOLOGRAPHIC-SPEC, FIRST-SOUND, JACOBSON-SPEC, MULTI-T-JACOBSON, VORONOI-FNL |
| einstein-theorist | W2, W3, W4, W5 | EIH-GRAV, SINGLET-CC, BCS-TENSOR-R, FRIEDMANN-BCS-AUDIT, HOMOG-42-RECOMPUTE |
| quantum-acoustics-theorist | W1, W3, W5, W6 | FIRST-SOUND-IMPRINT, COHERENT-WALL, DOS-TAU, 2ND-SOUND-ATTEN |
| landau-condensed-matter-theorist | W1, W6 | LIFSHITZ-ETA |
| nazarewicz-nuclear-structure-theorist | W1, W4, W6 | TRACE-LOG-CC, STRUTINSKY-DIAG, BAYESIAN-f, FRG-PILOT |
| quantum-foam-theorist | W4, W5, W6 | F-FOAM-2, DISSOLUTION-SCALING |
| connes-ncg-theorist | W2 | DIMFLOW |
| tesla-resonance | W6 | CHLADNI-GGE, SPECTRAL-DIM-BAND |
| cosmic-web-theorist | W3 | FIRST-SOUND (Fisher) |
| baptista-spacetime-analyst | W4 | INDUCED-G |
| gen-physicist | W6 | VAN-HOVE-TRACK |
| sagan-empiricist | W7 | Assessment |

---

## VI. E-vs-F Correction Protocol

The S43 E-vs-F audit identified 9 AFFECTED, 3 PARTIALLY AFFECTED, and 4 UNAFFECTED computation instances. All S44 computations must follow:

1. **Derivatives (dS/dtau, d2S/dtau2, Z) are UNAFFECTED.** Use directly.
2. **Absolute S(tau) used as rho_grav is WRONG.** The gravitating energy is E = S - sum_k T_k (dS/dT_k). Until TRACE-LOG-CC-44 and CUTOFF-F-44 compute this correction, flag any computation using S(tau) as rho with "E-vs-F UNCORRECTED" and note the estimated impact.
3. **HOMOG-42 is the most sensitive result** (4.5x margin). HOMOG-42-RECOMPUTE-44 addresses this after CC computations provide the correction factor.
4. **BCS energetics are CORRECT.** E_cond, E_exc, Delta_0 are Hamiltonian eigenvalues (internal energy), not free energies.

---

## VII. Global Rules

1. **ALL physics agents use opus.** Sonnet only for knowledge-weaver bookkeeping.
2. **Script prefix**: `s44_`
3. **Python**: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`
4. **Output directory**: `tier0-computation/`
5. **Gate IDs**: as specified in each wave prompt
6. **Working paper**: `sessions/session-44/session-44-results-workingpaper.md`
7. **One writer per output file.** Other agents contribute via SendMessage.
8. **Pre-register gates BEFORE computation.** Define pass/fail, then compute.
9. **Negative results are boundaries, not failures.** They constrain the solution space.
10. **Path quoting**: ALL bash paths containing "Ainulindale Exflation" must be double-quoted.

---

## VIII. Bundle Coverage

The S44 investigation bundle (S43 quicklook) listed 40 unique computations. This plan covers 31 computations + 1 Sagan assessment = 32 tasks. The mapping:

### Covered (31 computations)

All 5 CRITICAL items: SAKHAROV-GN-44, TRACE-LOG-CC-44, CDM-CONSTRUCT-44, FIRST-SOUND-IMPRINT-44, HOLOGRAPHIC-SPEC-44.

11 of 12 HIGH items: LIFSHITZ-ETA-44, DIMFLOW-44, EIH-GRAV-44, SINGLET-CC-44, STRUTINSKY-DIAG-44, N3-BDG-44, FIRST-SOUND-44, INDUCED-G-44, COHERENT-WALL-44, F-FOAM-2, FRIEDMANN-BCS-AUDIT-44.

All 12 MEDIUM items: JACOBSON-SPEC-44, MULTI-T-JACOBSON-44, VORONOI-FNL-44, DOS-TAU-44, DISSOLUTION-SCALING-44, HOMOG-42-RECOMPUTE-44, DM-DE-RATIO-44, SPECTRAL-DIM-BAND-44, FRG-PILOT-44, CHLADNI-GGE-44, BCS-TENSOR-R-44, CUTOFF-F-44.

3 of 5 LOW items: 2ND-SOUND-ATTEN-44, BAYESIAN-f-44, VAN-HOVE-TRACK-44.

### Omitted (3 computations) with reasons

| ID | What | Why omitted |
|:---|:-----|:------------|
| L-SCALE-44 | What selects Carlip L = 1.74 mm? | S43 CC workshop C5: "Carlip L has no dynamical selection mechanism. Status: CLOSED for S44 planning." Both agents enumerated internal scales; none reach mm. Translation, not solution. Defer to S45 if CC gap narrows enough to make the L question relevant. |
| GREYBODY-TAU-44 | Gamma(tau) evolution through transit | LOW priority diagnostic. Greybody factor already computed at fold (GREYBODY-43 PASS, Gamma = 0.7093). Evolution adds information content only if the transit dynamics become relevant for a new mechanism. Defer to S45. |
| FIRSTLAW-TRANSIT-44 | First law at 10 tau points during transit | LOW priority extension. FIRSTLAW-43 already verified the first law at the fold to 1.26e-7. Multi-point extension is a consistency check, not a new gate. Defer to S45. |

### Subsumed

| Bundle ID | Subsumed by | Reason |
|:----------|:-----------|:-------|
| CC-GGE-GIBBS-44 | TRACE-LOG-CC-44 | The Gibbs-Duhem computation (rho_grav = rho_GGE - sum lambda_k I_k - Omega) is equivalent to computing the trace-log vacuum energy with equilibrium subtraction. TRACE-LOG-CC-44 implements exactly this. |
| CDM-RETRACTION-44 | CDM-CONSTRUCT-44 | CDM-CONSTRUCT-43 PASS (T^{0i}=0) supersedes the retraction entirely. Free-streaming length is a category error. |
| FLAT-DM-44 | CDM-CONSTRUCT-44 | Mixed B2/B1+B3 scenario dissolved: all branches have v_4D = 0. |
