---
name: Yu et al. 2025 PNAS port assessment
description: Verdict CONDITIONAL on rewriting weak-form loss for first-order GPE vortex dynamics. Port symmetry-prior + weak-form pattern only (~300 lines), not full ForceInfer.py.
type: project
---

**Paper:** Yu, Abdelaleem, Nemenman, Burton 2025 PNAS 122(31) e2505725122 — "Physics-tailored ML reveals unexpected physics in dusty plasmas." DOI 10.1073/pnas.2505725122. arXiv 2310.05273.

**Code location:** `tools/many-body-force-infer/ForceInfer.py` (722 lines, TF 2.4). Cloned 2026-04. Five experimental CSVs (9p, 10p, 13p, 18p, 0.75Pa15p), no pretrained checkpoints.

**Why:** User asked structural assessment of porting Yu et al.'s ML force-inference methodology into the phonon-exflation framework. Port verdict: CONDITIONAL.

**Why:** TF 2.4 cannot run on Python 3.12 + torch+ROCm GPU venv. The methodology has a substrate-analog use case (vortex-force inference in GPE simulator) that would cross-check Volovik-Mineev analytic Magnus/Iordanskii results. But the weak-form loss assumes Newton 2nd-order dynamics; GPE vortex kinematics are 1st-order. Naive port surfaces r̈-dominated artifacts.

**How to apply:**
- Specifically port: `Myint.call` symmetry-prior input layer (ρ²_xy + (z_i, z_j) individual), `w_to_coef`+`get_XY` weak-form Simpson-rule machinery, 3-NN decomposition template, `myr2` metric.
- Specifically DON'T port: screened-Coulomb fit (Eq. 4-5), plasma-specific preprocessors (`microprocess`, '15p' branches), hand-tuned RMSprop schedule, the `tf.config.set_visible_devices([], 'GPU')` line.
- Pre-registered Test 1 (decisive go/no-go): VORTEX-FORCE-INFER-RECIPROCITY. Stationary background: |f_12 + f_21| / |f_12| < 0.05; flowing: > 0.20. Tests Magnus/Iordanskii.
- Pre-registered Test 2 (mass-style cross-check): GPE-MAGNUS-CROSSCHECK. A_inferred / (ρ_s κ²) within 10% across two background densities.
- Most-likely failure: derivative-order mismatch. Yu's loss is `w¨·x` IBP for 2nd-order ODEs; GPE vortex dynamics 1st-order in time. Must rewrite to `w·(ẋ − v_s)`.
- Secondary failure: vortex effective mass is geometric (acoustic-mass renormalization per Volovik #26 BDI), not scalar; Yu's s_i descriptor (mean z) has no defect analog.
- Substrate-analog physics already covered analytically: Volovik #10 topological superfluids, #19 combined Lorentz, #26 3He-B BDI, Volovik-Mineev classification. ML route would cross-validate, not discover.
- SKIP is correct call if half-day port not budgetable; methodology is plasma-specific, the substrate-analog answers exist in closed form.

**The three "unexpected" Yu findings, from superfluid-analog perspective:**
1. Nonreciprocity from ion-wake = analog of Iordanskii force on vortex moving rel. to normal-component flow. Same universality class, different microscopic mechanism. NOT novel from Volovik viewpoint.
2. λ depends on grain size (~3× across pairs) = wake spatial extent scales with grain. Plasma-specific. No clean superfluid analog.
3. q ∝ m^p with p ∈ [0.30, 0.80] increasing with P = OML deviation, plasma-specific. No analog.

**Methodology contribution that IS reusable:** weak-form loss (Gurevich-Reinbold-Grigoriev 2019) + input-layer symmetry priors. Both are general inference patterns; neither is plasma-specific.
