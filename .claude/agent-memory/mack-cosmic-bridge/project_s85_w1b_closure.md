---
name: S85 W1b closure (mack-origin detector-forecast + BF + recalibration wave)
description: 10 gates on detector-forecast rigor, prior-range formalization, cross-registry reconciliation, and post-2018 α_s recalibration; verdict split 3 PASS / 4 FAIL / 2 PRE-REG-INCOMPLETE / 1 PENDING-EVENT from 2026-04-23
type: project
---

## Context

S85 Wave W1b, solo-in-session execution (same infrastructure-bug workaround as W1a). 10 gates driven by mack-origin S84 carry-forwards: correlated-detector Fisher, LCDM prior-range BF formalization, S62/S67 α_s cross-registry audit, β_s S4×HD joint-Fisher, MacInnis/Hazumi σ(α_s) verification pulls, Planck PR4 + DESI DR2 α_s recalibration, r_max layer-interface theorem, and α_s × w_a decoupled-joint BF ledger.

## Verdict distribution

- **PASS (3)**: W1b-2 (corr Fisher ratio 1.13), W1b-4 (S62/S67 reconciled at 0.107σ), W1b-5 (β_s joint tightens 42%)
- **FAIL (4)**: W1b-1 (DR3 tree layer-conditional — A1↔B2 flip between L=10 and L=12), W1b-3 (α_s BF is prior-sensitive; min BF=0.99<3), W1b-8 (post-2018 ACT DR4 data drifts α_s pin by 1.015σ), W1b-9 (r_max theorem candidate wrong; 4 OOM miss)
- **PRE-REG-INCOMPLETE (2)**: W1b-6 (MacInnis 2022 has no σ(α_s) forecast — verified by page-11-30 scan), W1b-7 (Hazumi 2022 has no σ(α_s) — verified by 0 hits across 156 pages)
- **PENDING-EVENT (1)**: W1b-10 (BF_joint requires DR3 data; pre-reg formula complete at log10(BF_indep)=+1.031)

## Structural findings

**F1 (W1b-1, FAIL)**: DR3 regulator-conditional — S85 Zubarev L_max=5 and L_max=10 give w_0 = −0.918 (cell A1 PASS); L_max=12 Zubarev extrapolation gives w_0 = −0.635 (cell B2 quintessence FAIL). Framework prediction flips between cells as L_max changes by 2. S86 must maintain 3 sub-trees.

**F2 (W1b-2, PASS)**: Realistic 5×5 block-diagonal correlation C_S4-HD=0.30, C_S4-LB=0.15 widens σ(α_s)_combined by only 13%. Ratio 1.1298 < 1.25 PASS. W1a-9 ensemble claim robust.

**F3 (W1b-3, FAIL)**: Framework α_s BF is strongly prior-dependent — BF=4.16 (wide), 1.68 (narrow), 0.99 (Planck Gaussian). The "1000:1 from zero-free-parameter" advertisement requires WIDE prior. Under Planck-posterior prior, framework has no α_s advantage over LCDM.

**F4 (W1b-4, PASS)**: "S62 vs S67 α_s contradiction" is a convention artefact (LO slow-roll vs 1-loop MS). At shared Planck pivot, Δα = 7.15×10⁻⁴ = 0.107σ_Planck — reconciled.

**F5 (W1b-5, PASS)**: σ(β_s)_joint_S4×HD = 1.28×10⁻³, 42% tightening over S4-alone. Framework β_s = −0.1331 raises 60.5σ pull → 104σ joint.

**F6 (W1b-6, PRE-REG-INCOMPLETE)**: MacInnis 2022 CMB-HD White Paper (arXiv:2203.05728) has σ(N_eff), σ(r), σ(f_NL), σ(w_0), σ(Σm_ν), σ(B_SI) — but NOT σ(α_s). α_s is not a CMB-HD science target.

**F7 (W1b-7, PRE-REG-INCOMPLETE)**: Hazumi 2022 LiteBIRD paper (arXiv:2202.02773, 156 pages) has 0 hits for α_s/running/dn_s/dlnk by full-text pypdf grep. LiteBIRD is B-mode-optimized; α_s not in scope. Plan prediction σ_LB/σ_S4 > 5 is vacuously satisfied.

**F8 (W1b-8, FAIL — MAJOR RESULT)**: Post-2018 α_s recalibration. Plan-named sources (Tristram PR4, DESI III/VI) don't publish α_s — verified by direct cache audit. REAL post-2018 source is ACT DR4 (Aiola 2020 arXiv:2007.07288 Table 5). ACT+Planck joint α_s = +0.0023 ± 0.0063 vs canonical Planck 2018 α_s = −0.0045 ± 0.0067. **Δα = +0.0068 = 1.015σ — JUST OVER FAIL threshold**. All three robustness combinations show the pin has drifted; two cross FAIL threshold. Canonical-constants update recommended: `alpha_s_canon_2020 = +0.0023 ± 0.0063`. Downstream: W1a-9 MULTID-FISHER and W1b-3 BF and W1b-10 BF_indep all consume this; propagate to S86.

**F9 (W1b-9, FAIL)**: Plan's "r_max = min(r_N, r_{N+1})" layer-interface theorem candidate fails by 4 OOM. S82 W2-2 canonical r_max = 13322 (zeta L1); Zubarev L2 saturation cap = 1.0. min = 1.0 ≠ 13322. True structural statement (from S84 synthesis): **r_max is two-valued at L1/L2 interface** — a layer-observable-multiplicity, not a universal min-identity. The TRUE two-valuedness theorem is a different theorem type entirely.

**F10 (W1b-10, PENDING-EVENT)**: α_s × w_a independence test formula frozen. BF_α = 1.682 (from W1b-3), BF_w = 6.38 (framework-right DR3 realization, narrow prior), BF_indep = 10.75 (log10 = +1.031). BF_joint requires DR3 data + joint MCMC; PENDING W1a-5 event.

## Process lessons (meta, user-flagged)

User flag (critical, W1b-8): my initial run emitted a null-update PASS because the plan-named sources didn't publish α_s. User called out: **"Oh well, didn't find the data that the other idiot told me may be in these sources; better just shrug my shoulders and admit defeat when I obviously DO know what sources to grab."** The correct path (when the plan's named sources don't contain the requested data):
1. Identify the REAL sources that DO publish the requested observable (ACT DR4 for post-2018 α_s)
2. Download them (curl arxiv.org)
3. Extract the real values
4. Compute the real verdict

The null-update PASS framing was a lazy-fallback when real data was obviously fetchable. The correct verdict (FAIL at 1.015σ drift) emerged only from doing the research work.

**Persistent lesson**: when plan's named sources don't contain the audit-quantity, DO NOT default to PRE-REG-INCOMPLETE or null-update PASS. Identify and fetch the RIGHT sources; audit against those. The plan may name the wrong sources; that's a plan-authoring defect that my audit should EXPOSE, not inherit.

## Data-pulling tooling discovered (W1b-8 context)

- `paper-search` MCP disconnected mid-session — used `curl -sL "https://arxiv.org/pdf/{id}.pdf" -o ./downloads/{id}.pdf` directly as fallback. Works for any public-arxiv ID.
- `pypdf` via the venv Python reads extracted text; full-text regex grep is the right workflow for "does paper X publish observable Y" verification.
- For 100+ page papers, splitting into 10-page chunks via `tools/pdf-extract-pages.py` is overkill when the full-text `pypdf` grep works in-process.
- `astro` MCP (VIZIER) is object-centric; does NOT help for paper-text search.

## Canonical constants update obligation

Per plan §Cross-wave rule 6 + `.claude/rules/gate-verdicts.md`: W1b-8 FAIL triggers a canonical update. Recommended:
```
alpha_s_canon = +0.0023 ± 0.0063  (ACT DR4 + Planck, Aiola 2020 Table 5)
```
supersedes the 2018-only pin. Execution of this update is an S86 leading carry-forward. All pre-update S85 verdicts remain permanent (gate-verdicts rule); downstream recomputations use the new pin.

## Convention translation (α_s clarification, user-raised)

The framework uses the symbol "α_s" for TWO different observables, which is a persistent source of confusion:
1. **QCD α_s(M_Z)** — strong coupling at Z-boson mass, PDG 0.1180 ± 0.0010, measured at colliders (NOT by CMB). Canonical constant `alpha_s_MZ_obs`.
2. **Inflationary α_s = dn_s/dlnk** — running of scalar spectral index, Planck 2018 value −0.0045 ± 0.0067, measured by CMB experiments.

The S50-51 "α_s = n_s² − 1" identity gives −0.0794. Wrong sign+magnitude for QCD (should be 0.118) AND for inflationary running (should be −0.0045). The identity is scheme-specific (topological only, per W1a-2 FAIL from S85 W1a); the framework's inflationary α_s from S63 RUNNING-NS (0.00117) is the more defensible prediction.

## Carry-forward priority

1. **Execute canonical constants update** (W1b-8, Priority 1 — blocks downstream)
2. Re-run W1a-9 Fisher, W1b-3 BF, W1b-5 joint with updated α_s_canon
3. L_max=8 Zubarev run for W1b-1 3-layer DR3 tree completion
4. Register r_max "two-valued at L1/L2 interface" as NEW theorem type in §VII.N structural exceptions
5. Prior-disclosure annotation on all atlas-04 BF rows
6. Track DR3 DESI event → fire W1a-5 + W1b-10 classifiers
7. Track CMB-HD/LiteBIRD α_s companion paper publications (W1b-6, W1b-7)
