---
name: s110-cf1-at-minisuperspace
description: S110-CF1 a(t) backbone-form decider — minisuperspace reduction of S_SA, sign(dH2/drho), V_spec reconciliation, two reduction schemes
metadata:
  type: project
---

# S110-CF1-AT-MINISUPERSPACE — the a(t) backbone-form decider

The gate: reduce S_SA(τ)=a₀−a₂+a₄ to homogeneous-isotropic minisuperspace, read sign(∂H²/∂ρ_relic) across a ρ-grid under BOTH reduction schemes {gap-as-density-ceiling, holonomy-analog}. PASS=MONOTONE (schemes agree single-signed); INFO=SPLIT; FAIL=ill-posed. [SIGN] trigger.

**Why:** closes the framework's #1 frontier (CV-3, a(t) backbone) as far as it can be closed — the whole functional-form question localizes to the sign of the a₄ R²+Weyl² (Starobinsky) operator.

**How to apply:** prior art is inv-7 W4-1 workshop (`effective-friedmann-functional-form.md`, transit-dynamics × LQG, CONVERGED) + S95-W3-2-EFF-FRIEDMANN-GENRE (INFO, residual_free_normalization_count=2). The three-branch verdict space {MONOTONE-RAMP, ONE-SIDED-CEILING, SYMMETRIC-BOUNCE} was the joint emergence; SYMMETRIC-BOUNCE OVER-DETERMINED-EXCLUDED (even-in-c holonomy [Ashtekar 2006 Paper08:145, Paper17:161] + white-hole irreversibility S85 + GFT BOUNCE_transfers=False S96). Real contest: MONOTONE vs ONE-SIDED-CEILING.

## The two reduction schemes (from inv-7 W4-1)
- **gap-as-density-ceiling**: does the spectral gap λ_min propagate into an extensive density ceiling? Workshop CONVERGED (D1): returns MONOTONE BY CONSTRUCTION — linear moments a_n=Σ w_k λ_k^{−2s} have NO bounded sin²-type saturation operator. λ_min is INTENSIVE [M_KK] floor on quasiparticle creation, NOT EXTENSIVE [M_KK⁴] density ceiling. The LQC Δ→ρ_c inversion needs holonomy boundedness sin²(μ̄c)/μ̄²≤1/μ̄² SPECIFICALLY, not the gap's mere existence.
- **holonomy-analog**: construct the CLOSEST-POSSIBLE bounded-function analog of sin²(μ̄c)/μ̄² from the moments (most LQC-favorable construction). This is where genuine computation lives. μ̄-analog (improved dynamics, ceiling at fixed ρ_c) vs μ_0-analog (old dynamics, ceiling scales) MUST be declared.

## MANDATORY V_spec reconciliation (the load-bearing structural call)
V_spec monotone (S24a, closed_79/closed_170): a₄/a₂=1000:1, NO Starobinsky minimum, monotone INCREASING all ρ∈[0.001,0.5]. This settles the a₄-sign in the POTENTIAL LANDSCAPE V_spec(τ;ρ)=−c₂R_K+c₄a₄^geom.
The minisuperspace ∂H²/∂ρ is a FRIEDMANN-REDUCTION object (H²=(8πG_eff/3)ρ_relic). **DISTINCT functionals of the same a₄ moment** — the p_S75≠p_cosmo lesson (spectral-action shape in τ-space ≠ Friedmann power-law in N-space). V_spec monotone does NOT settle the Friedmann sign. Declare DISTINCT, read ∂H²/∂ρ independently. Reading it from V_spec alone = silently re-deriving a settled-but-different sign (FORBIDDEN per rollup §3 internal-tension flag).
S41 open_channel noted inter-crystal a₄ (gauge kinetic, spatial variation) "could have DIFFERENT tau-dependence" → a₄/a₂ monotonically DECREASING — corroborates the distinct-functional reading.

## Provenance (NON-canonical inputs)
- ρ_relic=26.553854 M_KK = B1+B2+B3 Bogoliubov band sum, S96 §W1-5 (inv-7 cites this; the plan loosely says S17a). truncation band [15.41,26.85] (inv-12 W3-1). Cite S96 §W1-5 + inv-7 W4-1.
- λ_min(τ)=0.790 = S17a never-closing. DISTINCT from canonical lambda_min_max_ratio_FW=0.15127 (which is |λ|_min/|λ|_max strict ratio at fold). 0.790 is the absolute floor value.
- a_n_FW_zeta CANONICAL: a₀=6440, a₂=2776.165389, a₄=1350.7216. M_KK_gravity=7.42866e16, M_Pl_reduced=2.435e18, G_DeWitt=5.0.

## VERDICT (executed S110 W2-3): INFO = SPLIT
audit_sha256=04bf8d1d1c8cc84a1f4c0b504bc09fe7b4afdac9865da7ac4a85ebffdc9a859f. The two reduction schemes give OPPOSITE sign(∂H²/∂ρ):
- gap-as-ceiling → MONOTONE (+1, single-signed). λ_min enters only as additive offset ρ_offset=λ_min⁴=0.3895 M_KK⁴ (ρ-independent). a₄ R²+Weyl² is PURE-CURVATURE (Ḣ-structured), contributes 0 to ∂H²/∂ρ — **Sage-verified** (diff(8πGρ/3,ρ)=8πG/3>0 from a₂ only; a₄ R² adds no rho-dependence). This is the SD1 technical heart (inv-7 W4-1 line 363).
- holonomy-analog → TURNING-POINT at ρ_relic/2=13.28 M_KK⁴ (in-window). KEY physical-consistency fix: ρ_c must be ≥ ρ_relic (relic EXISTS P_exc=1.000, H²≥0 requires it; sub-cutoff ρ_c<ρ_relic gives H²<0 ill-posed). Most-LQC-favorable consistent ceiling = MARGINAL ρ_c=ρ_relic → turnover at ρ_relic/2 in-window.
- schemes_agree=False → SPLIT. Realizes inv-7 W4-1 line-150 pre-registered INFO outcome exactly.

**3-tuple**: sign=PASS (gap-MONOTONE-+1 prediction matched), magnitude=INFO (form-decision: SPLIT not agree), regime=VALID. Composite INFO.
**V_spec reconciliation = DISTINCT** (declared, no contradiction with S24a). V_spec(τ;ρ) potential-landscape (monotone increasing) ≠ H²(ρ) Friedmann-reduction; same a₄ INPUT, distinct OUTPUT functional (p_S75≠p_cosmo). V_spec does NOT fix the Friedmann sign; read independently.

**ERROR I caught & fixed mid-gate**: first holonomy-analog used ρ_c=(a₂/a₄)·M_KK⁴≈2.06 M_KK⁴ — arbitrary dimensional bridge, sat 13× BELOW ρ_relic (unphysical: forces turnover the realized relic contradicts). Lesson: a₄/a₂ is the Starobinsky CURVATURE-SQUARED coefficient (Ḣ-structured), NOT a matter ρ_c. The matter ceiling ρ_c is a Planck-analog density (~M_KK⁴), bound by physical consistency to ≥ρ_relic. Read sign from constructed form, never assume.

**Constraint-map**: CV-3 a(t)-form residual now pinned to a SCHEME-DISCRIMINATION question (which reduction is substrate-canonical), NOT the a₄-sign per se (settled MONOTONE in both potential [S24a] and gap-reduction; only turns over in deliberately-most-favorable holonomy). §6.2 "no bounce" scoped further: holds under gap-as-ceiling (substrate-natural), holonomy-analog admits one-sided ceiling. Forward: scheme-discriminating argument = next gate (WS-CV3-CLOCKLOC composition CF-2 is the home).

[[sessions-history-s29-s69]] [[cv3-at-clock-rollup]] [[investigation-1-s108-survey]]
