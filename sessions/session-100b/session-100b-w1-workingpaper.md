# Session 100b Wave 1 — C10 / Dark-Energy Observational (Results Working Paper)

**Session**: 100b | **Wave**: 1 | **Plan**: session-100b-plan-w1.md | **Theme**: C10/dark-energy observational arm of the S99 litreview campaign — BBN two-route constraint adjudication (prerequisite to the ρ_vac epoch-profile read-out), wa_FW = 0 scored against the Planck-low-ℓ-independent systematics-robust combination, and w_0 branch resolution + branch-iv L_max stability under CAC.

## Gate Sections

### §W1-1. S100b-X-C10-BBN-CONSTRAINT-RECONCILE (einstein-theorist)

**Status**: COMPLETED (2026-06-07)
**Gate ID**: `S100b-X-C10-BBN-CONSTRAINT-RECONCILE`
**Trigger**: `[VERIFY]`
**Classification**: **PHONONIC**
**Agent**: `einstein-theorist`
**Hypothesis**: The S66 G_eff(BBN) 2% bound and the S98/S99 ΔN_eff lever — pointing OPPOSITE in n_eff under their published conventions — resolve under one Sage-exact unified convention via their normalization anchors (fold-anchored vs z=0-anchored), classifying the pair as one-operative-one-rescoped, distinct-observables, or genuine canonical contradiction.
**Plan reference**: `sessions/session-plan/session-100b-plan-w1.md` §W1-1 (machinery pin, 4-class outcome rubric, normalization-anchor discriminator axis, substitution chain Parts A+B, registration block, dual prior).

**Verdict**: **PASS** — outcome class **OPERATIVE-LEVER+G_EFF-RESCOPED**. 4-tuple: (value=OPERATIVE-LEVER+G_EFF-RESCOPED, scheme=FW, convention=ABSOLUTE unified-convention with normalization-anchor axis {fold-anchored, z0-anchored} as the pre-registered discriminator, L_max=N/A). Canonical line + dual-SHA companion + 3 companion rows (regulator pin, constraint scope, anchor evidence) emitted via the race-safe `emit_verdict` tool: audit_sha256 `26553084db8a42cd1ca887e14c59dd8a7e795cea7b3c378d868afcafcc00e87e`, content_sha256 `34aee687cd5137dbea0f5839b070f28b56ffa64ade0cf59dbf209fe2ab938541`, schema_version S84+. `[VERIFY]` trigger with `schema_v2_3tuple_required: false` per plan — no 3-tuple row (the directional content in the substitution chains is the discriminator derivation, not the gate's outcome variable; the outcome is 4-class set membership).

**MCP Pre-Compute Audit** (per plan `mcp_pre_compute_audit`, executed before any computation):

| Query | Salient return |
|:------|:---------------|
| `search_knowledge("S66 G_eff BBN n_eff direction")` | S66 3-row table indexed as equation entity (n_eff=2.3 → α~0.01 PASS; n_eff≤2 EXCLUDED); no prior reconcile gate exists |
| `search_knowledge("BBN relief lever from-below")` | S99-W2-BBN-RELIEF FAIL (audit `8fe0ef45…`, mech_a_n_req=1.959839) + S98-MK3-2 FAIL standing; Q29 corridor CLOSED-STRUCTURAL |
| `get_constant("delta_N_eff_vacuum_BBN_below")` | 2.0873 (S98, gate S98-MK3-2-BBN-VACUUM-FRACTION) — NOT re-adjudicated here |
| `get_constant("rho_vac_over_rho_rad_BBN_below")` | 0.474049 (S98, same gate) — NOT re-adjudicated here |
| `get_constant("N_eff_SM")` | 3.044 |
| `get_constant("T_BBN_GeV")` | 0.001 |
| `get_constant("T_RH")` | not-found (confirms plan-freeze state; run-time verification + registration executed below) |

Standing canonical verdicts confirmed: `S99-W2-BBN-RELIEF = FAIL` and `S98-MK3-2-BBN-VACUUM-FRACTION = FAIL` (both re-read from their verdict files; this gate adjudicates SCOPE, not those magnitudes). No prior gate performed this reconcile — confirmed (only the S100b plan itself indexes the hypothesis).

**Output Artifacts**:

| Artifact | Path | Check |
|:---------|:-----|:------|
| script | `computations/session-100b/s100b_x_c10_bbn_constraint_reconcile.py` | contains `from canonical_constants import` + `print_verdict_payload`; cpu-cap-OMP8; mpmath dps=50 |
| data | `computations/session-100b/s100b_x_c10_bbn_constraint_reconcile.npz` | both routes' f/ΔN_eff vs n_eff curves, crossings, residual table, table reproductions, identity checks, 50-dps decimal strings |
| plot | `computations/session-100b/s100b_x_c10_bbn_constraint_reconcile.png` | both routes on ONE axis; crossings 1.959839/1.904348/1.900014 + reference points {1.978111, 2.0, 2.3} marked; 2.02e7× discrepancy arrow |
| verdict line | `computations/session-100b/s100b_gate_verdicts.txt` | canonical PASS line + dual-SHA companion + 3 extra rows (emit_verdict, lock-serialized, sig_5 unique) |
| WP section | this §W1-1 | — |

Input pins: all 6 static SHA-256 pins verified EXACT against the plan block (2 S98 npz, 2 S66 workshop md, 2 paper PDFs); runtime SHAs captured for `canonical_constants.py` (`440f6ba11ce90575…`) and `s99_gate_verdicts.txt` (`9f8fc1240c86eed1…`, read-only anchor recovery). Gate-identity keys + n_eff reference set + budget set + anchor-axis declaration enter the audit closure per the plan's `audit_discriminators`.

**Results**:

**(1) Numbers first — the unified chain (50-dps recompute from canonical primitive pins vs S98 full-float64 npz; pre-registered tolerance ≤ 1e-12 per step).** MAX chain residual = **3.939e-16** (4 OOM inside tolerance). Per-step residuals: bound 6.3e-17, rho_vac_0 8.1e-18, rho_rad_BBN 2.9e-18, H_BBN 1.3e-16, H_ratio 1.8e-16, X 3.7e-17, relief_factor 9.8e-18, frac_base 3.5e-16, frac_below 3.8e-16, dNeff_below 3.9e-16, dNeff_base 3.0e-16; internal identities: relief pow-vs-exp form 0.0, frac_base ≡ ρ_vac,0/(3M_Pl²H_0²) 2.3e-51 (the z0 anchor made algebraically manifest), disc×cc_ratio ≡ 1.032 at 2.2e-16. Publication-image reproductions (each at its pin's own precision, Class-8.3): frac_below → 0.474049 OK; ΔN_eff → 2.0873 OK; relief_factor → 0.414115 OK; bound → 0.227107 OK; X → 40.2756 OK; frac_base → 1.144730 OK. Crossing solves (6-decimal publication; full-float64 inputs; downstream rel_tol ≥ 1e-6):

| Budget | f-bound | n_eff crossing | Prior images |
|:-------|:--------|:---------------|:-------------|
| canonical ΔN_eff ≤ 1 | 0.22710732 (exact in-script) | **1.959839** | plan-chain 1.959838 (rounded-display inputs), S99 verdict 1.959839 — both within rel 1e-6 |
| external GH-2026 ΔN_eff ≤ 0.107 | 0.02430048 | **1.904348** | plan-chain 1.904349 — within rel 1e-6 |
| external Cyburt-2016 G_eff-2% (α < 0.02 ⟺ f < 1/49 exact) | 0.02040816 | **1.900014** | new this gate; ΔN_eff-equivalent 0.089861 — the TIGHTEST of the three budgets |

Lever evaluations at the reference set (z0-anchored): n_eff = 1.978111 → f = 0.474059, ΔN_eff = 2.0874 (0.32 OOM over canonical bound); n_eff = 2.0 → f = 1.144730, ΔN_eff = 5.0405 (0.70 OOM over); n_eff = 2.3 → f = 2.0237e5, ΔN_eff = 8.911e5 (**5.95 OOM over** — the plan's "~6 OOM"). Implied-fraction discrepancy between routes at n_eff = 2.3: lever 2.0237e5 vs S66 published "~0.01" = **2.0237e7×** (plan's "~2e7×"). The a-exponent baseline: fraction ∝ a^{2(2−n_eff)} = a^{+0.043779} at the canonical pin (feeds W1-2's class separators).

**(2) Unified convention and substitution chains.** Single declared convention: ρ_vac(H) = α_V·M_Pl,red²·H^{n_eff}; f := (ρ_vac/ρ_rad)_BBN; α := ρ_vac/ρ_total = f/(1+f); ΔN_eff = f/[(7/8)(4/11)^{4/3}] with the bound factor computed exactly in-script (never hardcoded); n_eff = exponent on H; normalization-anchor axis {z0-anchored, fold-anchored} as the pre-registered discriminator.

*Chain A (lever route, z0-anchored; full-float64 npz inputs substituted):*
```
Step 1: f(BBN) = frac_base * exp((n_eff - 2)*X)        [S98-MK3-2 npz: frac_base = 1.1447295727818823,
                                                        X = ln(H_BBN/H_0) = 40.27560958603052]
Step 2: dN_eff = f / [(7/8)(4/11)^(4/3)]               [canonical S66 formula, qa L767;
                                                        bound exact = 0.22710731766023896...]
Step 3: n_eff = 1.978110506244663                      [HARD from-below; S98-MK3-1 PASS,
                                                        divergence_type=A, a3_q0_analytic = -881.5351]
Step 4: (n_eff - 2) = -0.02188949
        relief = exp(-0.02188949 * 40.27560959) = 0.41411453
        f = 1.14472957 * 0.41411453 = 0.47404915       [canonical pin 0.474049 reproduced]
        dN_eff = 0.47404915 / 0.22710732 = 2.08733542  [canonical pin 2.0873 reproduced]
Step 5: d ln f / d n_eff = X = +40.2756 > 0  =>  SMALLER n_eff (from-BELOW) relieves.
```
The z0 anchor is the DILUTION-CC normalization made algebraically manifest: frac_base ≡ ρ_vac(H_0)/(3M_Pl²H_0²) with ρ_vac(H_0) = 1.032·ρ_obs (identity verified at 2.3e-51) — the S98 script (`s98_mk3_2_bbn_vacuum_fraction.py` Section 5) fixes α_V at the present epoch and transports UP to BBN.

*Chain B (G_eff route under the unified convention — the same-observable theorem):*
```
Step 1: alpha := rho_vac/rho_total ; f := rho_vac/rho_rad   =>  alpha = f/(1+f)   [definitions]
Step 2: G_eff/G = 1/(1 - alpha) = 1/(1 - f/(1+f)) = 1 + f                          [substitute]
Step 3: => the "G-renormalization" (S66 T.4-T.5) and the "additive radiation" enhancement are the
        SAME H^2 shift: H^2/H^2_std = 1/(1-alpha) = 1+f EXACTLY. Sage symbolic: simplify_full
        (1/(1-f/(1+f)) - (1+f)) = 0. NOT distinct observables; dN_eff is the conventional UNIT.
Step 4: f(BBN) = f_anchor * (H_BBN/H_anchor)^(n_eff-2)  =>  d ln f/d n_eff = ln(H_BBN/H_anchor)
        z0 anchor (H_0 << H_BBN):      slope = +X = +40.2756 > 0  -> relief from BELOW
        upstream anchor (H_a >> H_BBN): slope = ln(H_BBN/H_a) < 0  -> relief from ABOVE
Step 5: The S66 table direction (n=2.3 relieves; n<2 worsens) REQUIRES an upstream anchor, while its
        0.67 baseline is z0-derived (qa L817: "uses the PRESENT-DAY ratio from the seesaw rho_vac ~
        M_Pl^2 H_0^2 and extrapolates using w_vac = 1/3"); E4 L723 transports the n!=2 rows upstream
        ("the vacuum energy dilutes FASTER"). The table MIXES anchors across rows (the n=2 row is
        anchor-degenerate since f ~ H^0 there).
```

*Chain C (the CC cost of the S66 escape — the decisive structural number):*
```
Step 1: f(BBN) is LINEAR in alpha_V at fixed n_eff (the law is a one-parameter power law).
Step 2: alpha_V^(S66)/alpha_V^(z0) = f_S66(2.3)/f_lever(2.3) = 0.01/2.0237e5 = 4.9414e-8
Step 3: rho_vac(z=0)|_S66 = 1.032 * rho_obs * 4.9414e-8 = 5.0996e-8 * rho_obs
Step 4: => the n_eff = 2.3 escape UNDERSHOOTS the observed CC by 7.292 OOM.
        Exact identity (anchor transport commutes with the power law):
        disc(BBN) * cc_ratio(z=0) = rho_vac_over_rho_obs = 1.032 EXACT (Sage QQ: 1.0320000000000000000).
        The inter-route BBN discrepancy IS the z=0 CC-miss factor — one number measured at two ends.
Step 5: Monotone in anchor height: the implied S66 anchor is only ln(H_a/H_BBN) = ln(67)/0.3 = 14.016
        (6.09 OOM above H_BBN, a T ~ 1 GeV epoch) — NOT the actual fold (tens of OOM above). A TRUE
        fold-anchored transport gives far smaller f(BBN) and a correspondingly LARGER CC miss. 7.29 OOM
        is the FLOOR of the CC cost, evaluated at S66's own published "~0.01".
```

**(3) S66 published-table reproduction under the unified convention.** Row n=2 ("α(BBN) = 0.67, EXCLUDED, G_eff = 3G"): the α-reading 1/(1−0.67) = 3.0303 reproduces "3G"; the f-reading 1+0.67 = 1.6700 does not — S66 plugged the f-valued 0.67 (W1-A: ρ_vac/ρ_rad) into the α-slot of T.4; BOTH readings ≫ 1.02, so EXCLUDED is convention-robust (the slip moves no verdict). The qa-conversion images of the same row: 0.67/bound = 2.9501 (qa L769 "2.95" REPRODUCED exactly); qa L869 "1.34" = 2×0.67 is an early-turn conversion slip superseded in-session; qa L31 "(8/7)(11/4)^{4/3} ≈ 5.68" — the formula is exactly 1/bound = 4.4032, "5.68" is an arithmetic slip (the canonical L767 form /0.227 is correct and is what S98+ adopted). Canonical z0 normalization updates the row magnitude: f(n=2) = 1.144730 (ΔN_eff = 5.0405) vs the W1-A-era seesaw image 0.67 (ΔN_eff 2.95), factor 1.7086 — EXCLUDED either way. Row n<2 (">0.67 EXCLUDED"): reproduced under the implied upstream anchor — f(1.78) = 14.63 > 0.67, f(1.978111) = 0.911 > 0.67. Row n=2.3 ("~0.01, G_eff ~ 1.03G, PASS"): reproduced ONLY under the upstream anchor; under the z0 anchor the same n_eff gives f = 2.0237e5 (8.9e5 in ΔN_eff units, 5.95 OOM over the canonical bound — the plan's "excluded by ~6 OOM in lever form").

**(4) Adjudication (pre-registered 4-class rubric).** (i) DISTINCT-OBSERVABLES — excluded: the G_eff form and the additive form are the same observable by exact identity (Chain B Step 3; Sage symbolic 0). (ii) GENUINE-CONTRADICTION — excluded: under ANY single anchor both forms give the same n_eff direction; the published opposite directions live at OPPOSITE anchors and the unified chain reproduces both tables from their respective anchors (resolvable, not contradictory). (iii) Operative route: the **z0-anchored lever**, on three grounds — (a) DILUTION-CC-66 fixes α_V at z=0 (ρ_vac/ρ_obs = 1.032 is the mechanism's defining empirical content; the sole surviving CC route); (b) the tracking law is an ATTRACTOR (Volovik Gibbs-Duhem response; β-relaxation Γ_fabric/H ~ 1e43, S66 qa L40-42) — α_V is the equilibrium-response coefficient, not an initial condition propagated from the fold, so fold-anchoring contradicts the attractor character that justifies the tracking law in the first place; (c) quantitatively, the fold-anchored escape costs ≥ 7.29 OOM of present-day CC (Chain C) — it solves BBN by un-solving the CC, re-opening the 114-OOM gap the mechanism exists to close. The S66 G_eff route is **RESCOPED, not retired**: its FORM is retained as the exact unit-conversion of the same observable, and its 2% bound maps to the TIGHTEST ΔN_eff budget (0.0899 < 0.107 GH-2026 < 1 canonical); its three-row n_eff TABLE is rescoped as a fold-anchored boundary-value question, anchor-mixed as published, and not an escape available to the DILUTION-CC mechanism. **Outcome = OPERATIVE-LEVER+G_EFF-RESCOPED; verdict = PASS** per the plan's PASS_meaning (one constraint operative, the other rescoped to a different normalization-anchor question, no conflict; both S66 and S98/S99 verdicts retained at their proper scopes).

**(5) Constraint-scope statement (cited by W1-2 and any S101 corridor gate).** The operative BBN falsifier for the z0-anchored (DILUTION-CC) tracking vacuum is the lever f = frac_base·exp((n_eff−2)·X) with the canonical conversion ΔN_eff = f/0.22710732 (exact). Budgets: ΔN_eff ≤ {1 (canonical), 0.107 (GH-2026 EXTERNAL), 0.0899 (Cyburt-2016 G_eff-2% EXTERNAL)} ⟺ n_eff ≤ {1.959839, 1.904348, 1.900014}. The substrate pin n_eff = 1.978111 (HARD from-below, S98-MK3-1) exceeds ALL three crossings ⇒ the standing S98/S99 FAILs are CONFIRMED at their proper scope (ΔN_eff = 2.0873: 2.09× the canonical budget, 19.51× the external 0.107). Relief inside the tracking family requires n_eff below the crossings (a 1.84× shift in the departure exponent for even the loosest budget, not substrate-justified per S99-W2-BBN-RELIEF); the remaining relief route is a NON-TRACKING epoch profile — exactly the W1-2 question. The S66 from-above escape (n_eff = 2.3) is NOT available: it is a fold-anchored boundary-value solution costing ≥ 7.29 OOM of present-day CC.

**(6) Cross-checks.** (a) *Sage MCP* (true CAS, QQ-exact rationals on the full-float64 npz inputs): bound = 0.227107317660238963…; n1 = 1.95983919169; n2 = 1.90434837559; n3 = 1.90001420791; f23 = 202369.659994; disc = 2.02369659994e7; cc_ratio = 5.09957866229e-8; cc_miss = 7.29246570473 OOM; disc×cc_ratio = 1.0320000000000000000 EXACT; identity 1/(1−α)−(1+f) simplify_full = **0 symbolic**; f_2pct = 1/49 exact — every value agrees with the in-script 50-dps engine at all printed digits. (b) *Goldstein-Hill PDF* (SHA-pinned input): "∆Neff < 0.107 (95% C.L.)" and "Neff = 2.990 ± 0.070 (68% C.L.)" extracted VERBATIM from paper 11 (arXiv:2603.13226) — the plan's external-budget pin is verbatim-correct, and the paper uses the identical ρ_rad = [1+(7/8)(4/11)^{4/3}N_eff]ρ_γ convention (no mismatch). (c) *T_RH run-time verification* (plan T_RH_pin): s76_moduli_decay_gw_spectrum.npz carries T_RH_GeV = 1.700000e15 with Γ_total = 4.05e12 GeV in the same npz; the standard reheating formula T_RH = (90/(π²g_*))^{1/4}√(Γ·M_Pl,red) with g_* = 106.75 gives 1.6977e15 (ratio 0.9987 — the pin is its 3-sig-fig image), and τ_decay = ħ/Γ = 1.6252e-37 s matches the S76 header 1.63e-37 s. Source RECOVERED and internally consistent. (d) *Bound-factor rounding images* (plan footnote, Class-8.3): exact = 0.22710731766; images in circulation: 0.227107 (verdict-line, correct 6dp), 0.227113 (canonical-constants provenance comment, its own rounding path), and 0.227111 (back-division 0.474049/2.0873 of the rounded pins, computed this gate) — all within |Δ| ≤ 5.5e-6 of exact, i.e., inside the publication precision of the 2.0873 pin that generates the back-derivations; none is consumed by this gate (the bound is computed exact in-script). (e) *Crossing-image note*: full-float64 gives n1 = 1.959839 (= the S99 verdict image; the plan-chain 1.959838 is the rounded-display-input image) and n2 = 1.904348 (plan-chain 1.904349) — each pair differs by ~1 ulp at the 6th decimal, within the pre-registered downstream rel_tol ≥ 1e-6; the npz stores 50-dps decimal strings for audit.

**(7) Registration (canonical write-order, non-FAIL outcome).** Step 1: verdict line emitted via `emit_verdict` (above). Step 2: `update_constant("delta_N_eff_budget_GoldsteinHill_2026", 0.107, …)` — landed in canonical_constants.py SECTION E with the plan-verbatim EXTERNAL-NON-CANONICAL comment + PDF verification note; `update_constant("T_RH_GeV", 1.70e15, …)` — landed with the run-time-verification provenance (S76 W2-H pin; reheating-formula + τ_decay consistency; closes the volovik-R3 hygiene flag). Step 3: falsifier-master-inventory Row #76 (BBN-VOLOVIK-67 / Window-8) constraint-scope annotation — ROUTED to `mack-cosmic-bridge` (sole writer per `feedback_mack-bridge-role.md`); NOT written by this gate's agent.

**(8) Dual-prior resolution.** Pre-registered: track_A (resolution-without-contradiction, normalization-anchor reading) prior 0.75; track_B (genuine contradiction) prior 0.25. Outcome PASS ⇒ posterior ~0.95 track_A per the pre-registered discriminator; scope tags land in the registry (Step 3 routed to mack); neither canonical session's BBN reading enters the retraction pipeline — S66's table is RESCOPED (anchor-mixed, answers a fold-side boundary-value question), S98/S99's lever is OPERATIVE.

**Substrate framing** (PHONONIC): the a_0 Seeley-DeWitt zeroth spectral moment of D_K (a_0^{ζ} = 6440.0, zeta-regulated — a DIFFERENT moment than gravity's a_2) IS the early vacuum; the Volovik tracking response ρ_vac = α_V M_Pl²H^{n_eff} is its H-response. Flow: D_K eigenvalues → a_0 zeroth moment → tracking exponent n_eff → modified-Friedmann image → BBN observables. The G_eff(BBN) 2% bound and the ΔN_eff lever are TWO laboratory-IN shadows of that ONE substrate-IS object — this gate proved they are the SAME shadow in different variables (1+f ≡ 1/(1−α) exact), and that the real two-ness lives on the normalization-anchor axis: which end of the substrate's own history pins α_V. The substrate adjudication: the tracking law is the substrate's equilibrium RESPONSE (attractor; β-relaxation effaces fold-side initial data), so its one constant is fixed where the substrate's late-time vacuum is measured (z=0, DILUTION-CC) — not propagated from the fold as an initial condition. Neither S66 nor S98/S99 was treated as authority; the unified exact chain was.

**Carry-forward**: none new from this gate (W1-2 is already planned and inherits the constraint-scope statement; Row #76 annotation is mack's Step-3 action, not a compute).

---

### §W1-2. S100b-X-C10-RHOVAC-EPOCH-PROFILE (volovik-superfluid-universe-theorist)

**Status**: COMPLETED (2026-06-07) — DPP route **(R2) CONDITIONAL-SKIP-as-INFO** (pre-registered closure; the gate did NOT fire; mode-A/mode-B compute is (R3)-only and was not run)
**Gate ID**: `S100b-X-C10-RHOVAC-EPOCH-PROFILE`
**Trigger**: `[SIGN]` (schema-v2 3-tuple emitted on this closure with `sign_verdict=N/A` per the plan's R1/R2 prescription)
**Classification**: **PHONONIC**
**Agent**: `volovik-superfluid-universe-theorist`
**Hypothesis**: The radiation-era gravitating ρ_vac(a) implied by the S100a QEQ-DRIVE output departs from the tracking baseline (fraction ∝ a^{+0.0438}) in the relief direction — eps_BBN > +0.5 — and the epoch-resolved ΔN_eff clears ≤ 1 at both BBN and recombination, against the register's tracking-class FAIL prediction.
**Plan reference**: `sessions/session-plan/session-100b-plan-w1.md` §W1-2 (DPP routing R1/R2/R3, mode-A/mode-B machinery, ODE + k_curv npz pins, class separators, forward-pinned overlay M1′–M4′, substitution chain).

**Verdict**: **INFO** — pre-registered (R2) closure shape CONDITIONAL-SKIP-as-INFO (one of the three INFO shapes distinguished in the plan's `INFO_meaning`; the value string identifies it). 4-tuple: (value=`CONDITIONAL-SKIP_qeq_drive_FAIL_tracking_law_stays_imposed_radiation-like_reading_stands`, scheme=FW, convention=ABSOLUTE, L_max=N/A). Canonical line + dual-SHA companion + schema-v2 `[SIGN]` 3-tuple row (`sign_verdict=N/A`, `magnitude_verdict=INFO`, `regime_verdict=VALID`; composite collapse: regime VALID ∧ sign ≠ FAIL ∧ magnitude INFO ⇒ **INFO**) emitted via the race-safe `emit_verdict` tool: audit_sha256 `3b53c496d4f91876309a160eeea7d9c6d2b641b3825b420d460b3287352db686`, content_sha256 `cb744ae23169c7f484da2e4eb9ef264f4f8ff043af839bf5a470e1e9f61d44f7`, schema_version S84+. npz/png **WAIVED** per the plan `output_artifacts` (`optional: true`, "WAIVED under R1 PRE-REG-INC and R2 CONDITIONAL-SKIP closures").

**MCP Pre-Compute Audit** (per plan `mcp_pre_compute_audit`, executed before the closure script was written):

| Query | Salient return |
|:------|:---------------|
| `search_knowledge("rhovac epoch profile radiation era")` | No prior epoch-profile gate exists; hits are the S99 litreview source (`session-99-litrev-x-c10-vacuum-profile-mack.md`, structural-baseline pin + the "Magnitude — epoch-dependent α_V" channel CLOSED) and the S97 ω_DM/ρ_vac pins (CC-66 observable, different gate) |
| `search_knowledge("QEQ-DRIVE q_eq substrate")` | Open channel "Upstream — substrate q_eq(H) drive" = "OPEN (the live successor)" (S99) — exactly the channel `S100a-W1-2-QEQ-DRIVE` closed as FAIL; no follow-up epoch profile computed |
| `get_constant("rho_vac_over_rho_rad_BBN_below")` | 0.474049 (S98, gate S98-MK3-2-BBN-VACUUM-FRACTION; standing FAIL-side falsifier value) — NOT re-adjudicated here |
| `get_constant("delta_N_eff_vacuum_BBN_below")` | 2.0873 (S98, same gate; companion pin) — NOT re-adjudicated here |
| `get_constant("T_BBN_GeV")` / `get_constant("z_BBN")` / `get_constant("N_eff_SM")` | 1e-3 GeV / 4e8 / 3.044 (epoch + SM pins; under R2 carried in the audit pin map only) |

No S100a follow-up computed the epoch profile — confirmed. W1-1's canonical verdict line exists and its outcome class is recorded for the interpretation clause below: **PASS**, outcome **OPERATIVE-LEVER+G_EFF-RESCOPED** (audit `26553084db8a42cd…`), with the `# constraint_scope(W1-2):` companion row present in `computations/session-100b/s100b_gate_verdicts.txt`.

**Output Artifacts**:

| Artifact | Path | Check |
|:---------|:-----|:------|
| script | `computations/session-100b/s100b_x_c10_rhovac_epoch_profile.py` | contains `from canonical_constants import` + `print_verdict_payload`; (R2) closure script — trigger-predicate verification, standing-record recompute from canonical pins, dual-SHA closure, WP §W1-2 update in the same run; cpu-cap-OMP8 |
| data (npz) | — | **WAIVED** under (R2) per plan `output_artifacts.data.optional: true` |
| plot (png) | — | **WAIVED** under (R2) per plan `output_artifacts.plot.optional: true` |
| verdict line | `computations/session-100b/s100b_gate_verdicts.txt` | canonical INFO line + dual-SHA companion + schema-v2 3-tuple row + companion rows (dpp_route / standing_record / regulator_pin / reopen_condition) via `emit_verdict` (lock-serialized, sig_5-unique) |
| WP section | this §W1-2 | updated IN THE SAME RUN as the closure (mechanical-closure-discipline item 5) |

Input pins: plan-static SHA-256 pins verified EXACT for `s99_w2_relaxation_closure.npz` (`6d8d488a…`), `s99_w1_q_nonratio_observable.npz` (`1fdfe2eb…`), `s98_mk3_2_bbn_vacuum_fraction.npz` (`c153d8d6…`) — all three are (R3)-machinery inputs, pinned-but-unexercised under (R2). Runtime SHAs captured for `canonical_constants.py` (`35797b56c236a192…`), `s100a_gate_verdicts.txt` (`446cef5501daa6bf…`, the trigger source), and `s100a_w1_qeq_drive.npz` (`e31651ac9f8b3392…`, the trigger-side artifact; its trajectory is NOT consumed under R2). Gate-identity keys + route tag + budget set + epoch pins + class separators enter the audit closure per the plan's `audit_discriminators`.

**Results**:

**(1) Numbers first — the trigger predicate (the (R2) routing record).** Pre-registered predicate: the gate FIRES iff `S100a-W1-2-QEQ-DRIVE` ∈ {PASS, INFO-with-non-tracking-trajectory}. The canonical line on disk (`computations/session-100a/s100a_gate_verdicts.txt`, latest non-superseded line for the gate-ID per the Option-A reading discipline):

> `S100a-W1-2-QEQ-DRIVE: FAIL` — value carries `slope_GDtilt_H2=2.055551`, `exp_locked_EVEN_in_H_kappa_inv=True`, `slope_imposed_cH=1.008273`, `domfrac=1.0000`, `kcurv=+3586.53`, `no_slope1_capable_substrate_drive`, `C10-ObjectC-STRUCTURALLY-CONDITIONAL` (audit `e31d45cf5309b32c…`; 3-tuple sign=PASS / magnitude=FAIL / regime=VALID; domain_used_frac=1.0000).

Verdict token = **FAIL** ⇒ trigger predicate FALSE ⇒ route **(R2) CONDITIONAL-SKIP-as-INFO** fires exactly as pre-registered at plan-freeze (no npz trajectory inspection required: the INFO-with-non-tracking-trajectory branch is reachable only from an INFO verdict). The S100a physics behind the routing: the substrate's own Gibbs-Duhem drive is exponent-LOCKED at q_eq = κ₂H² (slope d ln q/d ln H = 2.0556 on the bare backbone; κ₂-invariance 7.6e-8 — log-derivative slopes are coefficient-blind), the |H|-EVEN parity theorem forbids any equilibrium-sector potential term linear in H, and the slope-1 tracking leg reproduces q_eq = c·H only when IMPOSED (slope_imposed_cH = 1.008273). The tracking law therefore stays an IMPOSED closure — there is no substrate-derived ρ_vac(a) epoch profile for this gate to read off.

**(2) Verdict emission.** Pre-registered value string, VERBATIM: `CONDITIONAL-SKIP_qeq_drive_FAIL_tracking_law_stays_imposed_radiation-like_reading_stands`. Emitted INFO with the schema-v2 3-tuple (`sign_verdict=N/A` — the sign leg eps_BBN ≷ +0.5 was NOT evaluated because the gate did not fire; `magnitude_verdict=INFO` — the pre-registered closure shape; `regime_verdict=VALID` — the routing predicate evaluated unambiguously on an on-disk canonical line). Mode tag: none (MODE-A/MODE-B are (R3)-only).

**(3) The standing 2.0873 / 19.51× exceedance record — what it means under the radiation-like reading.** Recomputed in-script from the canonical pins (arithmetic only; NOTHING re-adjudicated — the record is S98-canonical and W1-1-scoped): fraction (ρ_vac/ρ_rad)_BBN = 0.474049; bound factor (7/8)(4/11)^{4/3} = 0.22710732 (exact in-script); ΔN_eff(BBN) = 2.0873 (consistency 0.474049/bound = 2.08733, within the pin's Class-8.3 publication precision). Exceedances: **2.0873×** the canonical ΔN_eff ≤ 1 budget; **19.51×** the external Goldstein-Hill 2026 budget 0.107 (EXTERNAL, non-canonical); 23.23× the W1-1-derived tightest budget ΔN_eff ≤ 0.089861 (G_eff-2% ⟺ f < 1/49 exact). Under (R2) this record is **UNCHANGED** — no new ΔN_eff was computed because no derived profile exists to compute it from. Its meaning is now jointly sharpened by the two upstream verdicts: (a) **W1-1 (PASS, OPERATIVE-LEVER+G_EFF-RESCOPED)** fixed the operative falsifier as the **z0-anchored lever** f = frac_base·exp((n_eff−2)·X) — the S66 from-above escape (n_eff = 2.3) is unavailable at ≥ 7.29 OOM present-day-CC cost, so the exceedance cannot be re-scoped away on the normalization-anchor axis; (b) **S100a QEQ-DRIVE (FAIL)** showed the linear tracking law q_eq = c·H is an IMPOSED closure, not a substrate derivation — the equilibrium sector is |H|-EVEN and cannot supply it. Jointly: the **radiation-like reading** (fraction ∝ a^{2(2−n_eff)} = a^{+0.043778} at the pinned n_eff = 1.978111, i.e. |eps_BBN| ≪ 0.5 by construction, near-flat across the radiation era) is the register's standing prediction, and ON THAT READING the C10/BBN arm is robustly falsified against the operative falsifier — at BBN the gravitating tracking vacuum overshoots every budget in the W1-1 scope statement (n_eff = 1.978111 exceeds all three crossings 1.959839 / 1.904348 / 1.900014). What (R2) does NOT do: it neither realizes nor excludes the time-profile relief corridor (eps_BBN > +0.5, EDE-class). That corridor was not measured — the substrate drive that would have produced a derived profile does not exist in the equilibrium sector. C10 Object-C therefore stays **STRUCTURALLY-CONDITIONAL** (the S100a tag): discharge of the BBN arm is strictly conditional on replacing the imposed tracking closure with a derived non-tracking profile, not on re-reading the standing record.

**(4) Dual-prior resolution (pre-registered).** `CONDITIONAL-SKIP (R2) → track_A ~0.85 by the trigger's own failure (tracking law stays imposed)` — the radiation-like register reading persists, with the elevated posterior reflecting that the one candidate substrate drive evaluated so far (Gibbs-Duhem equilibrium response) came back exponent-locked at H², i.e., the DRIVE route to a non-tracking profile is closed durably (H-parity theorem), leaving only the back-reaction route below.

**(5) Forward condition for re-opening (pre-registered re-fire routing).** This gate re-fires under **(R3)** — with the mode-B machinery pins UNCHANGED (friction ODE q″ + 3Hq′ + k_curv(q − q_eq(H)) = 0; k_curv = +3586.5 npz-loaded from `s99_w2_relaxation_closure.npz`; RK45 rtol 1e-8 / atol 1e-10; backbone `arr_H_bare_t` + emergent-FRW continuation; epochs z_BBN = 4e8 and z_rec = 1100; class separators ±0.5; regression check reproducing the independent S98-MK3-2 anchor 0.474049 within 1% under an imposed tracking closure) — iff a FUTURE substrate q_eq derivation lands a non-tracking q_eq(H) or self-consistent ρ_vac(H): a successor QEQ-class gate returning PASS, or INFO with a non-tracking trajectory in its npz. The structurally open route is NOT another equilibrium-potential drive (the |H|-EVEN parity theorem closes that class: T and s are |H|-odd ⇒ ∫s dT is |H|-even ⇒ no equilibrium thermodynamic potential carries a term linear in H): it is the Volovik-corpus-faithful **KV self-consistent back-reaction** (Papers 25 §V / 35 — q-oscillation energy dominating the Friedmann closure, amplitude ∝ a^{−3/2} ∝ H on the self-consistent background), which requires re-deriving H from the q-oscillation energy (the §6.3 closure) instead of pinning the H backbone. That compute is the CF candidate already logged in the S100a WP §W1-2 — no duplicate carry-forward is opened here.

**Substrate framing** (PHONONIC): the gravitating early vacuum IS the deviation of the a_0-channel q-variable from Gibbs-Duhem equilibrium (ρ_V = ε − q dε/dq; the equilibrium theorem is the wall, the deviation is the gravitating part; regulator pin a_0^{ζ} = 6440.0, cited via the standing record only — no fresh regulated moment is computed under R2). What this closure establishes substrate-first: the substrate's OWN equilibrium thermodynamics is |H|-even, so it cannot drive the linear-in-H tracking that the radiation-like reading presumes — that reading is a laboratory-IN transport-frame closure IMPOSED on the substrate, not derived from it; and on that imposed reading the BBN-epoch shadow (ΔN_eff = 2.0873) exceeds every budget in the W1-1 operative scope. The flow D_K eigenfrequencies (992-mode well, k_curv = +3586.5) → q-relaxation → gravitating ρ_vac(a) → laboratory-IN ΔN_eff shadows is intact, but its drive leg is open at the SELF-CONSISTENCY (back-reaction) node, not at the potential node. The fold transit (τ_fold = 0.190, Mach 13.75) completes ~18 OOM above T_BBN; whether the substrate holds the gravitating vacuum at the tracking worst-case at nucleosynthesis is now strictly a back-reaction question — substrate dynamics here are NOT c-limited (the q-relaxation is substrate-internal; c bounds only the emergent-metric propagation the BBN observables ride on).

**Carry-forward**: none new from this gate (the re-open compute — KV self-consistent back-reaction with H re-derived from q-oscillation energy — is the CF candidate already logged in the S100a WP §W1-2; this closure adds only the pre-registered (R3) re-fire routing, which is already plan text).
---

### §W1-3. S100b-WA-ROBUST (mack-cosmic-bridge)

**Status**: COMPLETED (2026-06-07)
**Gate ID**: `S100b-WA-ROBUST`
**Trigger**: `[VERIFY]`
**Classification**: **PHONONIC**
**Agent**: `mack-cosmic-bridge`
**Hypothesis**: The four-fold structural lock wa_FW = 0 survives the strongest systematics-robust test — the Planck-low-ℓ-independent combination ACT/SPT + WMAP + DESI DR2 BAO + Pantheon+ recovers w_a within 2σ of zero, strictly closer than the 2.92σ (DR2-marginalized) and 3.74σ (DESY5-joint) baselines.
**Plan reference**: `sessions/session-plan/session-100b-plan-w1.md` §W1-3 (route-A compressed-datavector reconstruction + route-B published anchor, grid pins, σ_gov toward-zero convention, sagan null-survival caveat, S85-W1b-8 substitution lesson).

**Output Artifacts**:
- `computations/session-100b/s100b_wa_robust.py` — producing script (contains `from canonical_constants import` and `print_verdict_payload` payload-block emission). The verdict-line content_sha256 `077dc843babcc59c9870ace19c241103f4df6208aeadfe98c625e20fc4c158c1` pins the AS-EMITTED script state, frozen at `s100b_wa_robust.frozen-15c54621f59184cc.py` per `mechanical-closure-discipline.md` §"Carry-forward script-bytes immutability"; the live file carries one post-emission, stdout-identical artifact-contract refactor (the inline payload prints wrapped into a `print_verdict_payload` function per the plan's `must_contain` and `script-template.py` convention — disclosed in the function docstring)
- `computations/session-100b/s100b_wa_robust.npz` — extracted datavector + covariances + EXTRACTION_RECORD (PDF table/eq provenance), full (w_0, w_a) posterior grids for SN variants V0–V3, marginalized w_a / w_0 / (Ω_m, H_0) posteriors, d_sigma + variants, convergence deltas, ε-sensitivity, route-B consistency record, baseline comparison table, fiducial pulls incl. D_M-free calibration invariant
- `computations/session-100b/s100b_wa_robust.png` — (w_0, w_a) 68/95% credible contours with w_a = 0 lock line + framework branch markers (−0.918 canonical, −0.842454 branch-iv) + route-B/SPT published anchors + ΛCDM point; right panel: marginal P(w_a) with variant overlays and d_σ annotation
- Verdict line in `computations/session-100b/s100b_gate_verdicts.txt` (race-safe `emit_verdict`; canonical line + dual-SHA companion + 3 extra rows: datavector PDF-SHA provenance, route-B anchors, sagan caveat): `S100b-WA-ROBUST: INFO -- ... audit_sha256=15c54621f59184ccd349f6498e89ce68fff5fae1a047922e771e6b55f07c4eab content_sha256=077dc843babcc59c...`
- Step-3 registry landing (mack sole writer, `feedback_mack-bridge-role.md`): `sessions/framework/registry/falsifier-master-inventory.md` Row #1 sub-row `1.wa-robust-s100b` ('w_a (Planck-low-ell-independent)') + `sessions/framework/registry/falsifier-watchlist.md` §"S100b W1-3 w_a robustness audit-pin" + change-log row, via `computations/session-100b/s100b_wa_robust_inventory_subrow.py` (npz-fed, idempotency-guarded). canonical_constants Step 2 SKIPPED — no NEW framework prediction constant (d_σ is an observational scoring; wa_FW = 0 already canonical).

**MCP Pre-Compute Audit**:
- `get_constant("wa_FW")` → 0.0 (provenance edge: "Framework w_a = 0 (four-fold locked, S58)") — Definition-1 anchor confirmed.
- `get_constant("wa_LCDM")` → 0.0 — the shared-null structure (sagan caveat) confirmed at the constants layer.
- `search_knowledge("w_a four-fold lock DR2 marginalized 2.92")` → pre-registered-observations.md row "w_a | 0 (exactly, four-fold locked) | −0.73 ± 0.25 | 2.92σ" — canonical baseline confirmed verbatim; S68 DR3 forecast σ(w_a) = 0.1768 surfaced (binding-instrument context).
- `search_knowledge("falsifier watchlist w_a robust")` → watchlist registry meta-entry only; **no prior gate scored the Planck-low-ℓ-independent combination** — gate not pre-closed; proceed confirmed.

**Verdict**: **INFO** — `d_sigma = 2.946`, inside the pre-registered intermediate band 2.0 ≤ d_σ ≤ 3.0 (PASS boundary 2.0, INFO/FAIL boundary 3.0). 4-tuple: (value=2.946, scheme=FW, convention=ABSOLUTE-sigma-gov-toward-zero-ROUTE-A-primary, L_max=N/A). Route tag: **ROUTE-A primary** (compressed datavector fully extractable from paper-05 incl. covariance — no fallback needed). Route-A-vs-route-B consistency tolerance **VIOLATED** (|Δw_a| = 0.327 > 1σ^B = 0.20; disclosed in the verdict value string and analyzed in (4) below — a route-operationalization finding, not a verdict input; the plan's verdict criterion is d_σ alone).

**Results**:

**(1) NUMBERS.** Route-A joint posterior (compressed Planck+ACT geometric CMB + DESI DR2 BAO 13-distance + Pantheon+ shape-matched; Ω_m, H_0 flat-marginalized on the pinned grid; ω_b analytically marginalized, |quadratic residual| ≤ 4.05e-5):

| Quantity | Value |
|:---------|:------|
| w_a (robust, V0 primary) | **−0.7970 +0.2705/−0.2808** (68% equal-tail) |
| σ_gov (toward-zero = upper bar) | 0.2705 |
| **d_σ** | **2.946** → INFO |
| w_0 (route-A, marginal) | −0.7738 [−0.8498, −0.7027] |
| Ω_m / H_0 means | 0.3164 / 66.96 (edge mass 3.9e-22 — interior posterior) |
| SN-mapping variants d_σ | V1 (direct-Ω_m prior) 4.029; V2 (z ≤ 0.7 shape) 2.781; V3 (1/(1+z)-weighted shape) 2.918 |
| Grid convergence | Δd_σ = 0.0267 (w0/wa halved), 0.0001 (Ω_m/H_0 halved) — both < 0.05 pinned ✓ |
| r_* calibration sensitivity | ε = ∓0.001 → d_σ = 2.866/3.026 (±0.080 per 0.1% of r_*) |
| Route-B published anchors (Giare Tab. II) | ACT+WMAP+DESI+PP: w_a = −0.47 +0.22/−0.20 → d_σ = **2.136** (INFO); SPT variant: −0.29 +0.25/−0.22 → d_σ = **1.160** (PASS) |

Baseline comparison (comparison rows, NOT verdict inputs; convention checks reproduced in-script: |0−(−0.73)|/0.25 = 2.920 ✓, |0−(−0.86)|/0.23 = 3.739 → 3.74 ✓, |0−(−0.62)|/0.22 = 2.818 → 2.82 ✓):

| Combination | w_a | d_σ (toward-zero bar) | Band |
|:------------|:----|:----------------------|:-----|
| DESI DR2-marginalized (canonical baseline) | −0.73 ± 0.25 | 2.920 | INFO |
| DESI+CMB+DESY5 joint (canonical baseline) | −0.86 +0.23/−0.20 | 3.739 | FAIL-side |
| DESI+CMB+Pantheon+ joint (paper-06) | −0.62 +0.22/−0.19 | 2.818 | INFO |
| **This gate, route-A (Planck-low-ℓ-independent reconstruction)** | **−0.7970 +0.2705/−0.2808** | **2.946** | **INFO** |
| Route-B published: ACT+WMAP+DESI+PP (full Planck-swap) | −0.47 +0.22/−0.20 | 2.136 | INFO |
| Route-B published: SPT+WMAP+DESI+PP | −0.29 +0.25/−0.22 | 1.160 | PASS-side |

**(2) Datavector extraction record (PDF-sourced only; never training knowledge; archived in npz `extraction_record`).** Paper-05 (Bansal-Huterer, SHA `5494d929…`): Eq. (5) compressed Planck PR3 plik + ACT DR6 datavector (R, ℓ_a, ω_b) = (1.7504, 301.77, 0.022371); Eq. (6) covariance 1e-8 × [[1559.83, −1325.41, −36.45], [−1325.41, 714691.80, 269.77], [−36.45, 269.77, 2.10]]; Eq. (4) definitions; z_* FIXED at 1090 (App. A); Eqs. (C1)–(C6) WMAP-7 ν-formalism (N_eff = 3.044, one massive ν 0.06 eV, f(y) with A = 0.3173, p = 1.83); App-B fiducial (H_0 = 68.24 fixed, ω_b = 0.02240, ω_cdm = 0.1198). Paper-06 (DESI DR2, SHA `1e82f26e…`): Table IV 13 distances — BGS D_V/r_d = 7.942 ± 0.075 (z = 0.295); (D_M/r_d, D_H/r_d, r_MH) at z = 0.510/0.706/0.934/1.321/1.484/2.330 (LRG3+ELG1 supersedes LRG3, ELG1; per-bin correlations −0.459/−0.404/−0.416/−0.434/−0.500/−0.431); Eq. (2) r_d = 147.05 Mpc (ω_b/0.02236)^−0.13 (ω_bc/0.1432)^−0.23 (N_eff/3.04)^−0.1; Eq. (1) z_d ≈ 1060. Paper-02 (Efstathiou, SHA `cab7f002…` runtime-recorded per plan): §2(i) "Pantheon+: The ΛCDM best fit gives Ωm = 0.333±0.018" (1417 SNe, 0.02 ≤ z ≤ 1.2) — the published Pantheon+ fit used, mapped as LCDM-distance-SHAPE constraint (free offset = free M; variants V1–V3 sensitivity columns). Paper-03 (Giare, SHA `4a259aeb…`): Table II + §IIIA route-B anchors (verified verbatim in dump: "WMAP+ACT+DESI+PP −0.859±0.055 … −0.47+0.22−0.20 … −5.81"). All values were re-grepped against the PDF text dumps before execution — every entry matched.

**(3) Substitution chain (plan §W1-3 item 7, numbers substituted).**
```
Def 1: wa_FW = 0.0                      [S58 four-fold lock; canonical_constants wa_FW;
                                         substrate constraint — CPL (w_0, w_a) is the lab's container]
Def 2: robust combination R (route-A) = compressed Planck+ACT (R, ℓ_a, ω_b) + DESI DR2 BAO (13)
                                         + Pantheon+ (paper-02 fit, shape-matched)
       (w_a_rec, σ⁺, σ⁻) = (−0.7970, 0.2705, 0.2808)
Def 3: w_a_rec = −0.7970 < 0  ⇒  0 lies ABOVE the central value  ⇒  σ_gov = σ⁺ = 0.2705
Substitute:  d_σ = |0 − (−0.7970)| / 0.2705 = 2.9463
Convention checks: |0−(−0.73)|/0.25 = 2.920 ✓ canonical;  |0−(−0.86)|/0.23 = 3.739 → 3.74 ✓ canonical
Direction:   smaller d_σ = lock survives; PASS direction is d_σ < 2
Conclusion:  2.0 ≤ 2.946 ≤ 3.0  ⇒  INFO at the pre-registered boundaries
```

**(4) Cross-checks and the route-inconsistency finding.** (a) *Pipeline validation*: SN shape functional self-check Ω_m = 0.333 → Ω_m_eff = 0.3331 ✓; r_d integral vs DESI Eq. (2) at pivot: 146.905 vs 147.031 Mpc → κ = 1.000853 (< 1% assert ✓; κ applied multiplicatively to r_*); quadrature doubling |ΔD|/D = 5.8e-8, |Δr_*|/r_* = 2.1e-7; interpolation operator max rel. error 1.07e-5 (< 3e-5 ✓, 14×14 bicubic nodes); BAO fiducial pulls all ≤ 1.77σ; **D_M-free calibration invariant** R/ℓ_a = (100√ω_m/c)(r_*/π): pred 5.802652e-3 vs obs 5.800444e-3 → **+0.17σ** (the calibration gate; see Methodology note). (b) *Grid convergence* (pinned tolerance < 0.05): 0.0267 / 0.0001 ✓ — d_σ = 2.946 is grid-converged; note the halved-w0/wa scan gives 2.920, so the published 3-sig-fig value carries ±0.03 grid resolution. (c) *Route-A vs route-B* (pinned tolerance |w_a^A − w_a^B| ≤ 1σ^B = 0.20): **VIOLATED** — |−0.7970 − (−0.47)| = 0.327 = 1.6σ^B. Structural reading: the two routes operationalize "Planck-low-ℓ-independent" differently. Route-A KEEPS Planck high-ℓ geometric information (the paper-05 compression distills Planck PR3 + ACT DR6 into (R, ℓ_a, ω_b) — removing the low-ℓ anomaly channel but retaining the Planck-calibrated acoustic geometry); route-B REPLACES Planck wholesale with ACT+WMAP full likelihoods. Additionally route-A's SN input is the COMPRESSED paper-02 shape fit (Ω_m = 0.333 ± 0.018) rather than the full Pantheon+ likelihood — the V0–V3 variant spread (2.78–4.03) shows the SN-compression choice is the dominant route-A systematic, ~±0.15σ around V0 for the shape-class variants (V2, V3) and +1.1σ for the crude direct-prior V1. Both routes nevertheless land in the SAME verdict band (INFO; SPT-variant PASS) — the band is route-robust even though the central w_a is not. (d) *ε-sensitivity*: d_σ crosses 3.0 at +0.1% r_* miscalibration (3.026 at ε = +0.001) — the INFO/FAIL boundary is within reach of a 1e-3 calibration systematic, while the INFO/PASS boundary (2.0) is ~12 ε-units away; the INFO verdict is robust downward, marginal upward.

**(5) What the data shows / suggests / does not address.** SHOWS: under the strictest reconstruction that strips Planck low-ℓ (route-A), the recovered w_a = −0.797 +0.271/−0.281 sits 2.946σ (toward-zero bar) from the four-fold lock w_a = 0 — essentially UNCHANGED from the canonical DR2-marginalized 2.920σ baseline (Δ = 0.026, inside the 0.027 grid-resolution); under the published full-Planck-swap (route-B) the pull relaxes to 2.136σ (ACT) / 1.160σ (SPT). The pre-registered hypothesis (within 2σ, strictly closer than both baselines) is NOT confirmed at route-A. SUGGESTS: the DR2-era DDE pull on the w_a axis is NOT primarily carried by the Planck low-ℓ anomaly channel once the geometric CMB content is retained — the pull lives in the BAO+SN+geometric-CMB interaction itself, with the Planck-vs-ACT/WMAP ω_m calibration difference accounting for the route-A/route-B gap; papers 03/05's identification of the three systematics localizations applies most strongly to the FULL-likelihood DDE significances (Δχ² class), not to the compressed-geometric w_a pull. DOES NOT ADDRESS: which of w_0 ∈ {−0.918, −0.842454} the data prefers at fixed w_a = 0 (that is §W1-4 + DR3); the DESY5-vs-Pantheon+ SN-calibration fork (route inputs pinned to Pantheon+ per plan); any w(z) shape beyond CPL.

**(6) SAGAN CAVEAT (pre-registered, verbatim-equivalent).** w_a = 0 is a NULL that ΛCDM shares — survival earns FALSIFICATION-SURVIVAL, NOT Bayesian credit over ΛCDM. The lock dodged a ~3.7σ refutation when the DDE ramp localized to systematics; this gate's INFO records that the robust combination weakens (route-B) but does not dissolve (route-A) the DDE pull. The discriminating quantity is w_0 at fixed w_a = 0 (W1-4 + DESI DR3); the R_842 rectangle (S84-DR3-RESPONSE-PROTOCOL, window open 2026-04-23, data ~2027) remains the binding instrument. Per the plan's INFO_meaning: the watchlist sub-row lands with the intermediate tag; DR3 remains decisive.

**(7) Methodology (operational deviations, honestly disclosed per `math-scripts.md` plan-authorship item 4).** Two in-session structural corrections to SCRIPT-INTERNAL validation machinery (neither is a plan-pinned criterion; the plan's pinned tolerances — 2.0/3.0 boundaries, < 0.05 convergence, ≤ 1σ^B route check, 3-sig-fig publication — were all applied exactly as pre-registered): (i) the inherited script's fiducial-validation assert tested ABSOLUTE (R, ℓ_a) pulls at the paper-05 App-B fiducial and tripped at −11.5σ on ℓ_a; diagnosis showed both pulls share a common −0.3% fractional offset (R: −0.286%, ℓ_a: −0.323%) — the App-B fiducial (H_0 FIXED at 68.24, a DESI+CMB+DESY5 fit) is not the Planck+ACT chain-mean parameter point, and ℓ_a's 0.028% precision converts that parameter-point mismatch into ~10 nominal σ. The assert was replaced by the D_M-free calibration invariant R/ℓ_a (cancels D_M exactly; tests √ω_m·r_* calibration), which passes at +0.17σ; absolute pulls retained as printed diagnostics. (ii) Interpolation nodes raised 10×10 → 14×14 after the pre-registered spot-check (< 3e-5) returned 5.23e-5 (bicubic h⁴ scaling predicted ~1.2e-5 at 14; measured 1.07e-5 ✓). Also recorded: T_CMB = 2.725 K used per paper-05 Eq. (C2) source-formalism fidelity (vs canonical 2.7255), with the κ calibration absorbing the absolute-scale residual; ε-sensitivity bounds the residual calibration systematic at ±0.08σ per 0.1%.

**Substrate framing** (PHONONIC): the late-time equation of state IS the emergent signature of the effacement residual — the 0.03% impedance-mismatch leakage (Γ_effacement = 0.99970) of the substrate's a_0 spectral-action zeroth moment. wa_FW = 0 is a STRUCTURAL consequence of the four-fold partition (S58), not a fitted null: the substrate IS the expansion history; CPL (w_0, w_a) is the laboratory's fitting container. Flow: D_K eigenvalues → a_0 zeroth moment → effacement leakage → emergent w(z) → BAO/SN/CMB distances. The three DDE-signal localizations (SN photometric offset, Planck low-ℓ, single z~0.7 bump) are container-side artifacts; this gate asked whether, once the lab's own systematics-suspect channels are removed, the lab still sees an evolution term the substrate forbids. The INFO answer: the cleanest geometric container still carries a 2.9σ-level evolution pull (route-A), relaxing to 1.2–2.1σ when the Planck calibration is swapped out entirely (route-B) — the lab's fitting container has not yet resolved whether the evolution term is its own artifact or a real signal; the substrate's null survives, unresolved rather than vindicated. Explicitly NOT evidence FOR the substrate over ΛCDM, which shares the null.

**Carry-forward**: none new from this gate. The route-A/route-B operationalization gap (0.327 in w_a, 1.6σ^B) is documented in the inventory sub-row `1.wa-robust-s100b` and is subsumed by the already-planned binding instrument (DESI DR3 R_842, §W1-4 + S84-DR3-RESPONSE-PROTOCOL) — a separate full-likelihood reconciliation compute would not change the binding decision structure and is not queued (no-padding rule).

---

### §W1-4. S100b-W0-BRANCH-RESOLUTION (sagan-empiricist)

**Status**: COMPLETED (2026-06-07)
**Gate ID**: `S100b-W0-BRANCH-RESOLUTION`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC**
**Agent**: `sagan-empiricist` (mack self-blacklisted — own carry-forward source)
**Hypothesis**: PRIMARY = A = −0.918 re-confirms under mechanical re-execution of the pre-registered decision rule on independent geometric grounds (data-proximity excluded by pre-registration), AND branch-iv w_0_B = −0.842454 is a stable prediction under the CAC L_max scan — spread over L ∈ {8, 10, 12} ≤ 0.025 = σ_DR3 fiducial.
**Plan reference**: `sessions/session-plan/session-100b-plan-w1.md` §W1-4 (CAC-branch-iv lockdown pins, leg-1 §3-rule components, Class-(c) R_JE→post-S86-formulation re-pin remediation, route-α/route-β/not-recoverable ladder, substitution chain).

**Output Artifacts**:
- `computations/session-100b/s100b_w0_branch_resolution.py` — producing script (contains `from canonical_constants import` and `print_verdict_payload`; content_sha256 `ebe9bbd0072226babd457fa55d9b5452f79be284e796c9272da86de6a1804c08`)
- `computations/session-100b/s100b_w0_branch_resolution.npz` — leg-1 record + route-adjudication record + R_JK trajectory + diagnostic candidate table + cache-layer rows + SV archaeology (canonical rho_B/offset_B/CAC/spread slots = NaN with `evaluator_recoverable=False`, per the INFO-(ii) closure)
- `computations/session-100b/s100b_w0_branch_resolution.png` — panel 1: diagnostic candidate CAC series vs L with ±0.025/±0.050 bands around −0.842454; panel 2: R_842 rectangle inset with candidates A and B + §5 reversal band
- Verdict line in `computations/session-100b/s100b_gate_verdicts.txt` (emitted via race-safe `emit_verdict`; canonical line + dual-SHA companion row + regulator-pin row + route-adjudication row): `S100b-W0-BRANCH-RESOLUTION: INFO -- ... audit_sha256=c8ab70a1833f56029452a3ae00587f96e41bbb64bd9b067092f491c14f36ed1b content_sha256=ebe9bbd0...`

**MCP Pre-Compute Audit**:
- `get_constant("w0_FW")` → −0.918 (S58, Volovik partition + effacement; NOT superseded) — Criterion-4 currency input.
- `get_constant("w0_FW_R842")` → not found — expected at dispatch; no parallel writer promoted it (re-verified at runtime: identifier absent from the `canonical_constants` namespace).
- `search_knowledge("S86-W0-PRIMARY-VALUE-RESOLVE")` → gate PASS, `value='PRIMARY=A=-0.918'`, scheme=4-criterion-adjudication — the registered leg-1 designation.
- `search_knowledge("branch-iv R_JE retirement R_JK")` → S86-BRANCH-IV-FORMULATION-COMMIT (knowledge index carries the FIRST line, FAIL; the verdict FILE shows the Option-A supersession chain FAIL→PASS, latest-line PASS audit `acc751101c8ca6ce...` = plan pin — file is authoritative per `gate-verdicts.md` §"Option A" retroactive canonicalization); Item-38 retirement record; 2B path-(c) equations ("K-coupled R_JK is canonical for branch (iv)"; R_JK vs R_JE "carry different scaling").
- `query_entity("gates", "S84-W0-REGULATOR-RESOLUTION-SV1")` → PASS, value=−0.842454, scheme=zeta, convention=branch-iv, L_max=5 — the branch-iv anchor provenance.
- NOT PRE-CLOSED: no prior gate performed the leg-2 post-S86 stability evaluation (plan-freeze statement re-verified by S86–S99 sweep: the only post-S86 hits on {−0.842454, R_JK} are the S88 W7-4 parent-CAC retrofit (A-branch Zubarev offset −0.340827, not branch-iv) and the S90 readiness audit (text-presence checks only)).

**Verdict**: **INFO** — pre-registered shape (ii): `branch-iv-w0-L-evaluator-not-recoverable`. Leg-1 CLEAN (PRIMARY = A = −0.918 re-confirmed mechanically; §5 reversal protocol armed unmodified). Leg-2: route-α and route-β both unrecoverable; branch-iv L_max stability **UNVERIFIED** — an honest formulation-gap record, NOT a drift verdict. NO `w0_FW_R842` promotion (Step-2 write-order fires ON PASS only).

Canonical line (audit_sha256 `c8ab70a1833f56029452a3ae00587f96e41bbb64bd9b067092f491c14f36ed1b`):
```
S100b-W0-BRANCH-RESOLUTION: INFO -- value='branch-iv-w0-L-evaluator-not-recoverable;leg1=clean_PRIMARY=A=-0.918_reversal-armed;route-alpha=post-S86-formulation-defines-no-w0-evaluator_R_JE-slot-vacant;route-beta=no-w0-unit-mapping-in-S85-W10-anchor-script;R_JK_traj=(0.01129619,0.00803461,0.00598992);diag-spread-span=(0.000830,0.036327)_crosses-0.025_decision-relevant' scheme=zeta convention=CAC-branch-iv-anchored-L10 L_max=mixed
```

**Results**:

*Leg-1 — mechanical re-execution of `w0-primary-decision-rule.md` §3 (NUMBERS first):*

| §3 component | Input (current registry state) | Result |
|:---|:---|:---|
| Criterion 4 registry-history | `w0_FW` = −0.918 canonical (S58, NOT superseded); `w0_FW_R842` ABSENT (B canonical-pin history = 0) | history-priority → **A** |
| Criterion 2 R_842 membership (center −0.842, hw 0.100) | offset_A = \|−0.918 − (−0.842)\| = 0.076000 (76.0% of hw); offset_B = \|−0.842454 − (−0.842)\| = 0.000454 (0.45% of hw) | **both inside** (non-discriminating, as registered) |
| Structural promotion of B | none registered (registry survey 2026-06-07) | no override |
| §5 reversal protocol | decision-rule file SHA = `da2ba36cc861ddf3...` = plan-freeze pin (bit-identical) ∧ band [−0.86, −0.83] present ∧ σ_DR3 = 0.025 present ∧ "Locked machinery" present | **ARMED UNMODIFIED** |
| Recomputed designation | pure function of (history-priority, rectangle-membership) ONLY | **PRIMARY = A = −0.918** |
| Registered designation (S86 verdict file) | `S86-W0-PRIMARY-VALUE-RESOLVE: PASS -- value='PRIMARY=A=-0.918'` | **MATCH** → leg-1 CLEAN |

Data-proximity EXCLUSION honored: the selection function's signature carries exactly the two §3 booleans; Criterion 3 (falsifiability) and ALL data-proximity numbers are structurally absent from it. The post-Dovekie σ-distances appear ONLY in this comparison table (register-side anchor currency, atlas-08 Q37 — NOT selection inputs): w_0^{post-Dovekie} = −0.803 (non-binding) → n_σ(B) = 0.731, n_σ(A) = 2.130.

*Leg-2 — route adjudication (pre-registered ladder; Class-(c) re-pin per the plan block header):*

Substitution chain with substituted numbers (plan §W1-4 item 7):

```
Definition 1: w_0_B = -0.842454      [SV1 PASS sha 6c0063d22c520da9...; S85-W10 reaudit PASS;
                                      recomputed THIS RUN from the archived closed form:
                                      -0.8424542759870739, reproduces npz to <1e-12 and the
                                      registered value to <1e-5]
Definition 2: CAC  w_0^{B,CAC}(L) := rho_B(L) + offset_B, offset_B := w_0_B - rho_B(10)
Definition 3: spread = max_{L in {8,12}} |rho_B(L) - rho_B(10)|   [offset cancels exactly]
Definition 4: sigma_DR3 = 0.025 ; thresholds PASS <= 0.025 < INFO <= 0.050 < FAIL
Substitute:   rho_B(L) requires the branch-iv evaluator at truncation L. EXACT REDUCTION
              (recovered from the archived SV1 form, verified to 1e-12):
                 w_0^{(iv)} = f(R),  f(R) = (-c_J*R + P_GGE_zeta)/(c_J*R + rho_GGE_zeta),
                 c_J = |F_Josephson_zeta|/N_cells = 336.641/32 = 10.52003125,
                 P_GGE_zeta = -0.688, rho_GGE_zeta = +1.709,  R = xi_J/xi_E_GGE(L)
              i.e. the evaluator's SOLE L-dependent input is the dressing-ratio slot R —
              the single-tag R_JE that S86 RETIRED (2B path-(c)).
Read-off:     under the post-S86 formulation the R-slot has NO defined L-dependent occupant
              -> rho_B(L) UNDEFINED -> spread UNCOMPUTABLE -> pre-registered INFO shape (ii).
```

Route-ladder evidence (all booleans from the producing script; pinned inputs):

| Test | Evidence | Result |
|:---|:---|:---|
| RA-1 archived-evaluator recovery | SV1 closed form re-run from `s84_w1a_w0_sv1.npz` anchors → −0.8424542759870739; f-reduction exact to 1e-12; f(R_SV1 = 0.453578) = same | RECOVERED + RUNNABLE; sole L-dependent input = retired R_JE slot |
| RA-2 post-S86 formulation | S86 commit chain FAIL→PASS (latest audit = plan pin `acc751101c8ca6ce...`); `branch-iv-canonical.md` (SHA = plan pin) contains the retirement + both successors and **0 occurrences of w_0** | formulation defines NO w_0 evaluator |
| RA-3 successor properties | ξ_E_GGE_inv = n_pairs·Δ_BCS/K_base = 13.642473425596 = canonical (1e-12) → L-INDEPENDENT by construction. R_JK(L) = {0.01129619, 0.00803461, 0.00598992} at L ∈ {8,10,12} (loaded npz = independent Casimir-schematic recomputation to <1e-6; R_JK(10) = canonical `R_JK` to 1e-12; a_2^{ζ}/a_4^{ζ} regulator tags). Drop-in test: f(R_JK(10)) = −0.430730 vs −0.842454 → anchor gap 0.411724 w_0-units = **16.5 σ_DR3** | R_JK is NOT a drop-in slot occupant (structurally distinct functional, "different scaling" per 2B path-(c); surrogate-vs-canonical without the §(iv-bis) algebraic-distance theorem) |
| RA-4 recombination map | no (R_JK, ξ_E_GGE_inv) → w_0 map in the registry or the S86 commit; LOCKOUT-E forbids post-2026-04-23 redefinition | none exists |
| **ROUTE-α** | RA-1 ∧ RA-2 ∧ RA-3 ∧ RA-4 | **NOT RECOVERABLE** (formulation gap — scripts all run; the formulation leaves the L-slot vacant and the legacy occupant is excluded by this gate's own pre-registration: "no legacy single-tag R_JE evaluation") |
| RB-1 anchor-script mapping | `s85_w10_r842_physical_anchor_reaudit.py`: −0.842454 enters as pinned constant `BRANCH_IV_W0_PRED`; zero references to R_JK | no w_0-unit mapping |
| RB-2 W10-2 definitional model | `w_0 = −1 + 2·ξ_eff·mellin/denom` consumes LEGACY SV2 quantities (log-linearly extrapolated at L ≥ 10); does not accept R_JK; min over all 12 branch values of \|w_0 − (−0.842454)\| = 0.019252 (branch d, unstable: stability_delta = 0.843 FAIL) | not a branch-(iv) w_0-unit mapping |
| **ROUTE-β** | RB-1 ∧ RB-2 | **NOT RECOVERABLE** |

Canonical leg-2 outputs (plan-required slots): rho_B(L) = (NaN, NaN, NaN); offset_B = NaN; CAC series = NaN; **spread = UNCOMPUTABLE**; `evaluator_recoverable = False`; route tag = NOT-RECOVERABLE. The in-script bit-exact CAC-anchor assert was scoped to the canonical-evaluator path, which did not fire; each DIAGNOSTIC candidate's CAC series satisfies w_0^{B,CAC}(10) = −0.842454 by the offset construction.

*Diagnostic sensitivity table (the quantitative core of the formulation-gap finding — NOT a verdict input):* four candidate unpinned recombinations of the successors into the R-slot, pushed through the CAC (6 sig figs):

| Candidate (unpinned rule) | rho_B(8, 10, 12) | spread | band at {0.025, 0.050} |
|:---|:---|:---|:---|
| C1: f(R_JK(L)) raw | −0.441416, −0.430730, −0.423819 | 0.010686 | PASS-band |
| C2: f(R_SV1·R_JK(L)/R_JK(10)) relative-trajectory | −0.878708, −0.842454, −0.806127 | 0.036327 | INFO-band |
| C3: f(R_SV1 + ΔR_JK(L)) additive | −0.843284, −0.842454, −0.841930 | 0.000830 | PASS-band |
| C4: −1 + 2·R_JK(L) (W10-2 model shoehorn) | −0.977408, −0.983931, −0.988020 | 0.006523 | PASS-band |

Span [0.000830, 0.036327] **crosses the 0.025 PASS/INFO boundary** → the unpinned recombination freedom is DECISION-RELEVANT at the pre-registered thresholds. Executing any one choice would set the verdict by an execution-time convention selection (PRU Class-8-adjacent freedom; v3 Class-1 adjacency) — this is precisely why the pre-registered INFO-(ii) closure, and not a forced number, is the honest outcome.

Archaeology context row C0 (FORBIDDEN legacy form — computed from the ARCHIVED W10-2 extrapolation record `R_JE^{extrap} = {5.148, 25.658, 127.880}`, no fresh evaluation of the retired tag): rho^{legacy}(8,10,12) = −0.981724, −0.996241, −0.999242. The legacy evaluator's own L=10 value sits **6.2 σ_DR3 from the registered anchor** — the registered −0.842454 is L=5-anchored and is NOT the large-L limit of its own (retired) evaluator. Class-(c) stale-pin remediation record: the carry-forward's "R_JE stability by L_max=12" pinned the RETIRED tag; re-pinned per the plan block to the post-retirement branch-iv w_0 evaluation; SV1 (PASS, value=−0.842454, L=5) / SV2 (FAIL, value=10.077109, L=8) lines verified verbatim in `s84_gate_verdicts.txt` as INPUT evidence, not the test.

*Cache-moment-layer diagnostic (§(ii.A) atlas-row vs cache-moment split; real D_K spectrum, s84 L12 cache, a_n^{ζ} tags):* a_2^{ζ,cache}/a_4^{ζ,cache} → R_JK^{cache}(8,10,12) = {0.016091, 0.011222, 0.008380} — same monotone-decreasing direction as the Casimir-schematic atlas-row trajectory, ~40% level offsets per L (the two layers are distinct F-images of the same substrate-IS quantity; a future evaluator derivation must declare its consumption layer).

4-tuple: `(value='branch-iv-w0-L-evaluator-not-recoverable;...', scheme=zeta, convention=CAC-branch-iv-anchored-L10, L_max=mixed)`. Dual-SHA: audit `c8ab70a1833f56029452a3ae00587f96e41bbb64bd9b067092f491c14f36ed1b`, content `ebe9bbd0072226babd457fa55d9b5452f79be284e796c9272da86de6a1804c08`.

**Methodology — route-selection disclosure (plan requirement)**: route tag NOT-RECOVERABLE is carried in the verdict value string. No deviation from the plan-pinned machinery: scheme=zeta (SV1-anchored, no scheme switch), L set {8,10,12}, L_anchor=10, CAC convention as pinned, deterministic, cpu-cap-OMP8. The only plan slot left unexecuted is the spread computation itself, which the pre-registered route ladder routes to INFO-(ii) when both routes fail — the scenario the plan author explicitly anticipated and pinned.

**Empirical assessment (sagan)**:
1. *What leg-1 establishes*: the PRIMARY = A designation is reproducible from the pre-registered rule on current registry state with zero data-proximity input — the branch designation remains a geometric/citation-discipline result, not a fit to DESI. The §5 reversal machinery is bit-identical to its S86 freeze.
2. *What the INFO does and does not say*: this is NOT evidence that branch-iv is unstable. It is evidence that the framework currently possesses NO defined object whose L_max stability could answer the question — the S86 retirement removed the w_0 evaluation's only L-dependent leg without re-deriving the evaluation through the successors. Stability is UNVERIFIED, and the registered −0.842454 remains an L=5-anchored value whose own legacy evaluator (now retired) ran to −0.996 at L=10.
3. *Consequence for DR3 readiness*: the §5 reversal protocol now operates on a SECONDARY whose regulator stability is unestablished — the structural caveat the plan's FAIL_meaning anticipated applies in its INFO form: a DR3 hit inside [−0.86, −0.83] would re-pin to a value whose truncation convergence is an open derivation item. Caveat routed to mack (Row #1 footnote annotation; sole writer — this gate's agent does NOT write the inventory). The 0.731σ post-Dovekie proximity remains citable only WITH the branch-shopping caveat (a PASS would have removed it; it stays).
4. *CAC-offset caveat for the future evaluator*: the parent lockdown's offset is a PHYSICAL effacement translation (−0.340827). For branch-iv, no candidate offset has a derived physical interpretation, and C0 shows the additive freedom can silently absorb a 6.2σ anchor mismatch. The future evaluator must derive its offset's physical content, not merely apply the template.

**Carry-Forward Computations (this gate; 4-field; mirrors to the WP-level block)**:
- **CF-S101-W0-BRANCH-IV-EVALUATOR** — *What*: derive the branch-iv w_0(L_max) evaluator under the post-S86 formulation: a pre-registered recombination map (R_JK distance-2, ξ_E_GGE_inv distance-1) → R-slot occupant, with the §(iv-bis) surrogate-vs-canonical algebraic-distance theorem and a declared consumption layer (atlas-row vs cache-moment); then re-run this gate's leg-2 CAC spread test on the derived evaluator. *Inputs*: `s84_w1a_w0_sv1.npz` (closed-form anchors + exact f-reduction), `s85_w12_elim1_D_K_Lmax_moments.npz` (R_JK trajectory), `s84_spectrum_cache_L12_tau019.npz` (cache-layer moments), `branch-iv-canonical.md`, this gate's npz (sensitivity table pinning the decision-relevant freedom). *Gate*: the derived map must reproduce w_0_B = −0.842454 at L_anchor=10 within 1e-5 (SV1 reproduction tolerance) with ZERO free normalization tuned to do so (else the map is itself a fit, and the stability test is void); then spread ≤ 0.025 PASS / (0.025, 0.050] INFO / > 0.050 FAIL, thresholds unchanged. *Effort*: 1 derivation workshop or solo-theorist gate + 1 compute gate (≤ 1 session).

**Housekeeping (§A flag, per the plan's input_files note)**: `branch-iv-canonical.md` §"Anchor cache" cites `computations/artifacts/s85_w12_elim1_D_K_Lmax_moments.npz`; the on-disk canonical is `computations/session-85/` (artifacts copy verified ABSENT 2026-06-07). One-line registry path fix → mack/orchestrator.

**Substrate framing (GEOMETRIC)**: w_0_FW IS the substrate's late-time spectral-action gradient projected onto observational coordinates; A and B are TWO METHODOLOGICALLY-DISTINCT projections of the SAME substrate observable (Volovik-partition averaging vs substrate-compaction direct evaluation) — the branch question is a property of the spectral triple's projection structure. Flow: D_K eigenvalues → a_0^{ζ}/a_2^{ζ}/a_4^{ζ} spectral moments → branch-iv fiber-tau compaction projection → w_0(z=0). The L_max axis is a property of the truncated triple (A^{≤L}, H^{≤L}, D^{≤L}); what this gate found is that the substrate-IS projection's truncation behavior is currently UNDEFINED at the formulation level — the laboratory (DESI DR3) reads w_0 IN its (w_0, w_a) container at σ = 0.025 precision, and the substrate side does not yet supply a truncation-converged object at that interface. PRIMARY designation remains observational-citation discipline, not a physics ranking.

---

## Wave 1 Synthesis (team-lead)

**Written**: 2026-06-07, session close. All 4 gates landed; verdicts verified on disk against each gate's `output_artifacts` must_contain set.

| Gate | Verdict | Headline value |
|:-----|:--------|:---------------|
| §W1-1 S100b-X-C10-BBN-CONSTRAINT-RECONCILE | **PASS** | outcome=OPERATIVE-LEVER+G_EFF-RESCOPED; chain residual 3.9e-16/14 steps; crossings {1.959839, 1.904348, 1.900014} all < pin 1.978111 (audit `26553084db8a42cd…`) |
| §W1-2 S100b-X-C10-RHOVAC-EPOCH-PROFILE | **INFO** (R2) | CONDITIONAL-SKIP_qeq_drive_FAIL — pre-registered route; npz/png waived (audit `3b53c496d4f91876…`) |
| §W1-3 S100b-WA-ROBUST | **INFO** | d_σ = 2.946 (route-A robust reconstruction), intermediate band [2, 3] (audit `15c54621f59184cc…`) |
| §W1-4 S100b-W0-BRANCH-RESOLUTION | **INFO** (shape ii) | branch-iv w_0(L) evaluator NOT RECOVERABLE post-S86; PRIMARY=A=−0.918 leg-1 clean (audit `c8ab70a1833f5602…`) |

**Wave reading.** The C10/BBN arm closes structurally this wave. W1-1's same-observable theorem (Sage symbolic 0: `G_eff/G = 1/(1−α) ≡ 1+f`) dissolves the S66-vs-S98/S99 direction conflict as inter-anchor mixing, not contradiction — and the surviving S66 escape route is priced at a 7.29 OOM present-day-CC undershoot (it solves BBN by un-solving the CC). With S100a-W1-2-QEQ-DRIVE FAIL (Gibbs-Duhem |H|-EVEN ⇒ q_eq = κ₂H², tracking law an IMPOSED closure), BOTH escape hatches on the standing ΔN_eff = 2.0873 / 19.51× exceedance record are now closed by independent gates; W1-2's pre-registered (R2) route records this jointly-sharpened state while honestly leaving the relief corridor (eps_BBN > +0.5) UNMEASURED-not-excluded (no substrate-derived profile exists; re-fire condition = a non-tracking substrate q_eq(H) via the KV self-consistent back-reaction route, §W1-2(5)). On the DE-observational side, W1-3's systematics-robust w_a reconstruction lands INTERMEDIATE (2.946σ from w_a = 0, statistically indistinguishable from the 2.920 DR2-marginalized baseline; route-B anchors 2.136/1.160σ) with the sagan caveat applied — survival credit only, the discriminator stays w_0 at fixed w_a = 0. W1-4 establishes that the framework currently has NO defined branch-iv w_0(L) stability object: both candidate evaluator routes are non-recoverable post-S86-retirement and the four candidate reconstructions disagree ACROSS the 0.025 PASS/INFO boundary — an honest UNCOMPUTABLE, not a convention-selected number. PRIMARY = A = −0.918 is re-verified clean on purely geometric/citation grounds; the §5 DR3-reversal SECONDARY now carries the stability-UNVERIFIED caveat ahead of any DR3 trigger.

**Decision-point evaluation** (plan §"Wave 1 → Wave 2 Decision Point"): W1-1=PASS → W1-2 scored single-falsifier (executed). W1-2=CONDITIONAL-SKIP-INFO → standing record unchanged; the Ω_b h² → D/H side-channel action item's trigger (W1-2 = PASS-or-INFO-with-EDE-like-profile) did NOT fire — no S101 gate opened. W1-1≠FAIL → the retraction-candidate adjudication item did NOT fire. W1-4=INFO → no `w0_FW_R842` promotion (PASS-only); the stability caveat landed on Row #1 SECONDARY (mack, in-session).

**Carry-Forward Computations (MATH ONLY — propagate to S101)**

### CF-S101-W0-BRANCH-IV-EVALUATOR — derive the post-S86 branch-iv w_0(L) evaluator, then re-run the stability test

Mirrored verbatim from §W1-4 "Carry-Forward Computations (this gate)" (4-field spec at that section): **What** — derive the branch-iv w_0(L_max) evaluator under the post-S86 formulation (pre-registered recombination map (R_JK distance-2, ξ_E_GGE_inv distance-1) → R-slot occupant, with the §(iv-bis) algebraic-distance theorem + declared consumption layer), then re-run leg-2's CAC spread test. **Inputs** — `s84_w1a_w0_sv1.npz`, `s85_w12_elim1_D_K_Lmax_moments.npz`, `s84_spectrum_cache_L12_tau019.npz`, `branch-iv-canonical.md`, `s100b_w0_branch_resolution.npz`. **Gate** — derived map reproduces w_0_B = −0.842454 at L_anchor=10 within 1e-5 with ZERO free normalization; then spread ≤ 0.025 PASS / (0.025, 0.050] INFO / > 0.050 FAIL. **Effort** — 1 derivation workshop or solo-theorist gate + 1 compute gate (≤ 1 session).

*(Not opened: D/H side-channel — trigger condition not met. Not duplicated: KV back-reaction CF — already logged in S100a WP §W1-2 per §W1-2(5).)*

**Effected In-Session (NON-MATH — completed before STOP)**

- [x] Row #76 constraint-scope annotation (W1-1 registration Step 3) — mack-cosmic-bridge sole-writer landing — `sessions/framework/registry/falsifier-master-inventory.md:1801` (block 1800–1809) — audit `26553084db8a42cd`
- [x] Row #1 SECONDARY stability-UNVERIFIED caveat + sub-row `1.w0-branch-resolution-s100b` (W1-4 routing) — mack-cosmic-bridge; PRIMARY cell byte-identical (uniqueness ×1 verified pre/post) — `falsifier-master-inventory.md:20,23` — audit `c8ab70a1833f5602`
- [x] Sub-row `1.wa-robust-s100b` + watchlist audit-pin/change-log rows (W1-3 Step 3) — mack-cosmic-bridge via `s100b_wa_robust_inventory_subrow.py` — `falsifier-master-inventory.md:22` + `falsifier-watchlist.md` — audit `15c54621f59184cc`
- [x] `branch-iv-canonical.md` stale `computations/artifacts/` path → `computations/session-85/` at both occurrences (W1-4 §A flag) — mack-cosmic-bridge via `s100b_w1_mack_registry_batch2.py` — `sessions/framework/registry/branch-iv-canonical.md:108,226` — provenance notes in-file
- [x] Constants `delta_N_eff_budget_GoldsteinHill_2026 = 0.107` + `T_RH_GeV = 1.70e15` landed with PROVENANCE (W1-1 canonical write-order Step 2) — einstein-theorist in-gate — `computations/_shared/canonical_constants.py:687-688,1883,1886` — gate `S100b-X-C10-BBN-CONSTRAINT-RECONCILE`

**Process observations (closed in-session; do NOT propagate)**: W1-3 attempt-1 was stopped after 2 h in a write-only edit-loop (zero executions); re-dispatch with an execution-bias mandate closed the gate in ~1 h of compute + mechanical wrap-up (one SendMessage resume nudge needed — the run finished after the agent's turn ended; payload was printed, emission completed on continuation). Orchestrator-direct presentation patches: none.

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-07 | C10 BBN arm (S66 G_eff route vs S98/S99 ΔN_eff lever) | direction conflict OPEN (S99 litrev C10 cross-cut) | RECONCILED — same observable, inter-anchor mixing; operative falsifier = z0 lever; S66 escape costs 7.29 OOM CC undershoot | W1-1 PASS (Sage-0 same-observable theorem + anchor-axis resolution) |
| 2026-06-07 | C10 ρ_vac epoch-profile relief corridor | untested | UNMEASURED-NOT-EXCLUDED; both escape hatches (normalization-anchor, equilibrium-drive) closed; re-fire = KV back-reaction route | W1-2 (R2) INFO + S100a QEQ-DRIVE FAIL |
| 2026-06-07 | w_a = 0 four-fold lock vs systematics-robust combination | untested at robust combination | INTERMEDIATE 2.946σ (survival-only; no Bayes credit; pull not primarily Planck-low-ℓ) | W1-3 INFO |
| 2026-06-07 | branch-iv w_0(L) stability | assumed testable (S99 CF pinned retired R_JE tag) | evaluator NOT RECOVERABLE post-S86; stability UNVERIFIED (honest UNCOMPUTABLE); PRIMARY=A unaffected | W1-4 INFO shape (ii) |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Other | Size |
|:-----|:-------|:------------|:------------|:------|:-----|
| W1-1 | s100b_x_c10_bbn_constraint_reconcile.py | ✓ | ✓ | 2 constants promoted | 42.8 KB / 45.7 KB / 153 KB |
| W1-2 | s100b_x_c10_rhovac_epoch_profile.py | waived (R2) | waived (R2) | — | 35.5 KB |
| W1-3 | s100b_wa_robust.py (+ frozen-15c54621f59184cc snapshot) | ✓ | ✓ | inventory_subrow.py + registry_batch2.py helpers | 60.9 KB / 1.29 MB / 227 KB |
| W1-4 | s100b_w0_branch_resolution.py | ✓ | ✓ | — | 51.6 KB / 20.0 KB / 142 KB |
