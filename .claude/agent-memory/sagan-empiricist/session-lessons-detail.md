---
name: Detailed session lessons (S32-S42)
description: Reusable lessons from sessions 32-42 -- moved from MEMORY.md for space. Covers bugs, corrections, methodology, and framework-specific insights.
type: project
---

## Session 32-34 Lessons (reusable)
- Formula correction mid-session (Tr D_K -> sum|lambda_k|): procedurally appropriate, large effect
- "Wrong triple" thesis (bulk/bare/uniform -> boundary/quantum/inhomogeneous): 3/3 legs computed
- Dump point: 2-3 independent convergences, not 7 (5 trace to single B2 min at tau=0.190)
- Null hypothesis needed: spectral action curvature on SU(2)xSU(2) for specificity test
- K-1e retraction lesson: scope errors in generator summation can reverse closures.
  Epistemic cost: 0.6x BF discount applied. Check ALL prior closures for scope completeness.
- RGE-33a: wrong-sign hierarchy (e^{-2tau}<1 but PDG needs g1/g2>1) is STRUCTURAL, unfixable.
- SECT-33a UNIVERSAL: B2 fold is global spectral feature, not singlet accident. d2 up to 13x.
- **S34 V-matrix lesson**: Frame-space (A_antisym, 8x8) != spinor-space (K_a_matrix, 16x16).
  Error persisted 33 sessions. Caught by D_phys requiring explicit eigenspinor projections.
  TRAP-33b retracted. Epistemic cost: prior probability estimate unreliable in upward direction.
- **S34 agent summary discrepancy**: Tesla summary claimed 3.8x VH enhancement; script gave 1.25-1.33x.
  Always verify agent summaries against their scripts.
- **S34 self-correction pattern**: 3 bugs found, each correction strengthened chain.
  Favorable sign (wrong frameworks accumulate contradictions) but not independently evidential.
- **S34 mu=0 forced**: Both canonical (PH symmetry) and grand canonical (Helmholtz convexity)
  close chemical potential channels. Only D_phys inner fluctuations can break PH.

## Session 35 Lessons
- **N_eff resolution**: Three independent methods (Thouless, ED, RG) converging on same conclusion
  is stronger than any single method. Correlation discount (~0.5) applies because all share DOS input.
- **BMF overturned by ED**: Mean-field Gorkov-Melik-Barkhudarov suppression was too pessimistic
  for discrete-mode system. ED is ground truth for N_eff=4 (paired GS confirmed).
- **Regulator independence**: V(B1,B1)=0 (Trap 1) means gap-edge divergence never enters M_max.
- **ENTROPY-35 FAIL**: SD monotonicity theorem applies to ALL smooth spectral action cutoffs.
- **Smooth-wall DOS is single point of failure**: All Wave 1 results depend on rho=14.02.
- **32% is boundary territory**: Framework at boundary between "structural math" and "physical theory."

## Session 36 Lessons
- **Self-consistency is load-bearing**: GCM computation showed M_max(MF) > 1 does NOT guarantee M_max(SC) > 1.
- **Tau stabilization is the decisive open question**: S_full(tau) minimum at fold UNCOMPUTED.
- **PMNS structural closure**: Schur's lemma + U(2) invariance forces eigenspace alignment = identity.
- **B1 catalyst confirmed**: ED shows B2-only gives E_cond=0. B1 required via V(B2,B1)=0.080.
- **Mixed sessions informative**: 6 PASS + 4 FAIL = net BF~1.2. Partially-correct framework signature.
- **Post-W4 revision to 12%**: TAU-STAB+TAU-DYN quantify structural mismatch (376,000x static, 38,600x dynamic).
- **Lava deficit**: 80% pass rate on consistency gates, ~0% on physical prediction gates.
- **Cascade hypothesis**: Reframes FAILs as "wrong computation." Hope, not progress.

## Session 40 Lessons
- **Abandoning probability is not a methodology**: Working paper declared probability "no longer useful." REJECTED.
- **Two acoustic prescriptions, one match**: Reporting only the match is selection bias. BF~2 combined.
- **Prerequisite-vs-confirmation**: GSL, CC-TRANSIT, B2-INTEG, QRPA confirm consistency. BF~1.5-2.5 each.
- **M_COLL-40 is clean falsification**: Naz-Hawking predicted 50-170x, got 0.34x. Good science.
- **Gauge coupling match is highest-priority**: e^{-2*0.190}=0.684 vs SM g1/g2 could fix M_KK.
- **PI directive (Framework-First-Physics)**: Stop repeating known physics. Faint Young Sun Lesson applies.

## Session 42 Lessons
- **CDM-from-geometry IS distinctive**: 5 DM-sector parameters eliminated. Ideal gas law analogy.
- **w=-1 is a prediction, not a tautology**: Three independent routes. BF vs LCDM alone ~1.0.
- **Effacement ratio is structural bottleneck**: |E_BCS|/S_fold ~ 10^{-6}. All 5 energy channels defeated.
- **Z(tau) irrelevant for homogeneous dynamics**: nabla tau = 0 for uniform evolution. Theorem.
- **Prerequisite gates dominate consistency scores**: Z-FABRIC, C-FABRIC pass as prerequisites. BF~1.5-2.0.
- **4 PASS + 3 FAIL + 1 GEOMETRIC = net BF~3.0**: Consistency gates pass, prediction gates fail.
- **Venus standard is not met**: No Venera moment. Gauge coupling match remains the path.
- **Epoch-mixing error in W-Z-42 v1**: KK-scale vs Hubble-scale at different epochs. 30 OOM error. Always check.
- **eta = 3.4e-9 is a FIT**: 1 hidden param (pair-breaking count). 0 DOF. NOT a prediction.
- **Giant Voronoi barely significant**: P=0.083 passes 0.05, structures 5x too large. BF~1.2-1.5.

## Session 43 Lessons
- **Retractions are the strongest negative evidence**: S42 CDM + eta both retracted. Prior positive BFs must be reversed.
- **c_s = c/sqrt(3) is conformal invariance, not prediction**: Both workshop agents converge. The second-sound = BAO claim adds no physics beyond w=1/3.
- **First-sound ring is genuinely distinctive**: 325 Mpc, zero free parameters, no LCDM analog. The session's most important contribution.
- **Root cause diagnosis (M_KK/M_Pl ~ 10^{-2.2})**: CC, DM, n_s, eta all trace to insufficient scale hierarchy. These are ~1.5 independent failures, not 4.
- **Fixed-temperature artifacts**: S42 eta used T_acoustic throughout cascade. Correct: microcanonical cooling gives T_eff ~ 3.5 M_KK for baryon emissions. ALWAYS use dynamic temperature in cascade calculations.
- **n_s circularity**: epsilon_H = 0.0176 was INPUT from Planck, not derived. The consistency relation n_s = 1 - 2*epsilon_H is content-free when epsilon_H is tuned.
- **Spectral action = wrong gravitating functional**: Workshop consensus. S_fold is entropy/free energy, not gravitating mass. This is the CC problem's root cause within the framework.
- **"Translation not solution"**: Carlip L = 1.74 mm produces Lambda_obs but replaces "why Lambda small?" with "why L = 1.74 mm?". No dynamical selection mechanism exists.
- **Gate that PASSES while destroying prior positive = net negative**: HF-CASCADE-43 passes its stated gate but invalidates S42 eta. The BF should reflect the combined effect.
- **alpha_s = -6.16e-4 is the only genuine CMB prediction**: 0.58 sigma from Planck. But it is a single-parameter derived quantity from the consistency relation.
- **Flat-band B2 = CDM candidate is speculative**: Bandwidth = 0 by Schur's lemma (proven), but lambda_fs = 0 requires that 4D group velocity = 0, which is UNCOMPUTED. Do not count it as a result.
- **Lava deficit STRENGTHENED**: 43 sessions, consistency gates pass at ~80%, prediction gates at ~0%. Pattern is now statistically significant.
- **BF arithmetic for correlated gates**: Use weighted geometric mean with correlation weights 0-1. Same root cause = low weight per gate.

## Session 43 Redux Lessons (2026-03-14 self-correction)
- **Scorekeeper bias is RECURRENT**: Same error as S22-S24 Redux. Treating closures as failures, penalizing self-correction, inflating negative evidence. Must actively guard against this in every assessment.
- **Closures are constraints (BF~1.0) unless they close the LAST path**: T11 closes internal baryogenesis but SM mechanisms exist. BF should be 1.0, not 0.85.
- **Self-correction handled by prior correction, not penalty**: Retracted S42 results (CDM, eta) reduce the PRIOR from 18% to 11%. The corrections themselves get BF~1.0. No double-counting.
- **Root cause diagnosis is positive evidence (BF>1)**: Workshop convergence on "wrong gravitating functional" narrows the CC search from infinite to 3 specific routes. This is science progressing, not failing.
- **Gate that PASSES while correcting prior = MIXED, not net negative**: Revised from original lesson. HF-CASCADE-43 PASSES its gate. The eta correction is prior adjustment, not gate failure. Combined BF 0.75 (not 0.55).
- **Original S43 assessment was 0.27 BF. Corrected: 1.14 BF.** Difference of 4.2x entirely from methodological corrections, not new evidence. Demonstrates how large the scorekeeper bias can be.
- **P(QFIELD FAIL | framework correct AND wrong functional) is HIGH**: If spectral action is genuinely the wrong gravitating functional, then q-theory self-tuning using spectral action SHOULD fail. BF for QFIELD moderated from 0.35 to 0.55.
- **Pre-registerable prediction is mildly positive (BF 1.2-1.5) even before testing**: The existence of a zero-parameter LCDM-discriminating prediction is itself evidence that the framework makes contact with observational cosmology. Most frameworks at 43 sessions have no such prediction.

## Session 44 Lessons (2026-03-15)
- **Formula provenance is the systematic blind spot**: Three errors in S44 (Sakharov normalization, Stieltjes ordering, Vol(SU(3))). All have correct arithmetic, wrong formula connecting spectral sums to observables. Cross-check agents endorsed wrong formulas. Pipeline reliability discount: 0.85x.
- **Nazarewicz formula audit protocol**: (1) state formula with units, (2) check dimensional consistency, (3) verify one limiting case, (4) cite original derivation. Would have caught all three S44 errors.
- **epsilon_H ratio invariance is a class-killer**: Closes the ENTIRE amplitude-projection approach to n_s (EIH singlet, trace-log, Jacobson, any combination). Structural theorem, permanent. Only velocity-type mechanisms survive.
- **G_N triple convergence is genuine**: Sakharov (2.3x), bosonic Gilkey (61/20 = 3.05x), polynomial SA (by construction). First time three independent routes agree. But: Lambda choice in Sakharov is not fully independent, and SA match is by construction. Adversarial BF = 1.5 (not 3.0).
- **CDM algebraic result is distinctive but input-dependent**: T^{0i}=0 follows from homogeneous Schwinger creation at k_4D=0. The homogeneity is an INPUT assumption. Reduces BF from 4.0 to 3.0 (adversarial: 2.0).
- **Vol(SU(3)) = 1349.7 resolves M_KK tension PROVISIONALLY**: 0.83 decades -> 0.013 decades. M_KK_Kerner scales as Vol^{-1}. But needs analytic verification of where Vol enters Kerner formula. BF = 1.5 (provisional).
- **First-sound ring is untestable**: SNR = 0.16 (DESI DR2). Venus standard still unmet. A prediction that cannot be tested with any planned instrument is not falsifiable in practice.
- **Lava deficit strengthened**: 44 sessions, consistency gates ~80% pass, prediction gates ~0% pass. Additional 0.8x discount applied.
- **KZ-NS-45 is decisive**: If n_s = 0.965 from Bogoliubov quench spectrum: BF 10-20, P -> 60%+. If FAIL: BF 0.3, P -> 8%. No other gate has this diagnostic power.
- **Fine-tuning epistemology from user**: Naturalness is a preference, not physics. The 121-digit spike function is mathematically legal. The CC gap is "unsolved" not "evidence against." Applied: CC gates get BF = 1.0 (neutral) not BF < 1.
- **Adversarial BF methodology**: Always compute P(result | null hypothesis) before assigning BF. Sakharov match within factor 3 has P(match | null, M_KK from SA) ~ 0.3-0.5, so BF ~ 1.5 not 3.0. CDM from homogeneous KK has P(CDM | null KK) ~ 0.5, so BF ~ 2.0 not 4.0.
- **Net session BF = 2.18**: Prior 12% -> Posterior 23% (13-37%). Net positive, driven by G_N and CDM. Offset by n_s crisis (BF 0.56) and pipeline errors (0.85x).
