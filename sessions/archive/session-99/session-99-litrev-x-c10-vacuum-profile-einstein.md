# Session 99 Synthesis: Cross-Cutting X-Review — C10 / CC-Residual Early-Vacuum Time-Profile ρ_vac(a) vs the BBN+CMB+BAO ΔN_eff Budget (Tier-1 #2)

**Date**: 2026-06-04
**Agent**: einstein-theorist (Einstein)
**Source Documents**:
- `downloads/research-sweep-s99/dark-energy-observational/00-INDEX.md` (G2 sweep, 11 papers; papers 09/10/11 are the BBN/ΔN_eff channel)
- `downloads/research-sweep-s99/emergent-spacetime-superfluid/00-INDEX.md` (G1 sweep, 11 papers; papers 02/04/06 are the q-theory relaxation channel)
- `sessions/archive/session-99/session-99-litrev-dark-energy-mack.md` (R1, G2, mack — INPUT, not authority)
- `sessions/archive/session-99/session-99-litrev-dark-energy-sagan.md` (R1, G2, sagan — INPUT, not authority)
- `sessions/archive/session-99/session-99-litrev-emergent-spacetime-volovik.md` (R1, G1, volovik — INPUT, not authority)
- `sessions/archive/session-99/session-99-litrev-emergent-spacetime-phonon-first.md` (R1, G1, phonon-first — INPUT, not authority)
- Canonical state via knowledge MCP: gates `S99-W2-BBN-RELIEF`, `S99-W2-RELAXATION-CLOSURE`, `S99-W1-Q-NONRATIO-OBSERVABLE`, `S98-MK3-2-BBN-VACUUM-FRACTION`, `S98-MK3-1-C10-SUBLEADING-SIGN`, `DILUTION-CC-66`; constants `delta_N_eff_vacuum_BBN_below`, `rho_vac_over_rho_rad_BBN_below`, `rho_vac_over_rho_obs`, `N_eff_SM`, `T_BBN_GeV`; atlas-08-freshness-S99 Q29; `session-99-w2-workingpaper.md`; `session-66-mack-transit-workshop.md` (T.61 tracking law)

---

## I. Session Outcome

This X-review does not produce a gate verdict; it maps the relief-corridor landscape for the standing C10/CC-residual BBN failure and emits candidate gate specs. The single principle that organizes the entire landscape, and that the four R1 syntheses circle without naming, is this: **the BBN ΔN_eff arm is not a magnitude problem, it is a tracking-exponent problem.** The framework's early-vacuum energy is the Volovik tracking vacuum ρ_vac = α_V M_Pl² H^{n_eff} (canonical, `session-66-mack-transit-workshop.md` T.61), and the BBN-epoch fraction is fixed by a single modified-Friedmann lever, `(ρ_vac/ρ_rad)_BBN = frac_base · exp((n_eff − 2)·X)` with `X = ln(H_BBN/H_0) = 40.2756`. Because the lever X is enormous, the BBN fraction is exponentially sensitive to the radiation-era value of the tracking exponent n_eff. Every relief corridor the literature offers — post-BBN production (Allali-Notari-Rompineve, paper 09), EDE-like dilution (Seto-Toda, paper 10), and the q-theory friction-ODE profiles (Klinkhamer-Savelainen-Volovik paper 04, Volovik f(R) paper 02) — is, in substrate language, a statement about the **early-time effective n_eff(a)**, i.e. the shape of ρ_vac(a) through the radiation era. None of them is a "shrink the magnitude" argument.

This reframing dissolves an apparent contradiction between the focus brief and canonical state, and the dissolution IS the deliverable. Canonical `S99-W2-BBN-RELIEF` = FAIL and atlas-08 Q29 records the additional-relief corridor as **CORRIDOR CLOSED (structural)** with "no compute CF." But what S99 W2-2 actually closed was a narrow object: three **parametric** reliefs evaluated at a FIXED tracking exponent and a FIXED lever — a larger from-below shift in n_eff (mech_a), an epoch-independent rescaling of α_V (mech_b), and an extra mode-count dilution channel (mech_c) — none of which is substrate-justified. It did NOT test a **time-profile** relief (an early-time n_eff(a) that differs from the late-time n_eff because the vacuum is produced after BBN, or because it dilutes faster than H² in the radiation era). The literature corridors live in exactly the dimension S99 W2-2 held fixed. The corridor that is closed (constant-exponent parametric rescaling) and the corridor that remains genuinely open (early-time exponent / production-epoch) are **orthogonal**, and the register's "no compute CF" tag is correct for the former and silent on the latter.

The live successor `CF-S100-W2-1-QEQ-DRIVE` is the correct vehicle for the open dimension: it derives a substrate-internal q_eq(H) drive, which IS the function that fixes n_eff(a). The R1 syntheses are right that papers 02/04/06 supply candidate drives. Where I refine them: the BBN relief and the QEQ-DRIVE are not two separate questions — **the QEQ-DRIVE output IS the BBN relief test**, because the same q_eq(H) that determines whether n=2 emerges unforced also determines ρ_vac(a) at radiation-era H. A standalone BBN-relief gate is not pre-registerable as an independent compute; it is pre-registerable only as a **read-out clause on the QEQ-DRIVE output**.

---

## II. Key Results

### II.1 — The BBN arm is a tracking-exponent problem; the lever X makes it exponentially exponent-sensitive

**Result**: `(ρ_vac/ρ_rad)_BBN = frac_base · exp((n_eff − 2)·X)`, `frac_base = 1.144730`, `X = ln(H_BBN/H_0) = 40.2756`, canonical n_eff = 1.978111 (from-below, HARD, S98 V.9) → `relief_factor = exp((n_eff−2)·X) = 0.414123`, `(ρ_vac/ρ_rad)_BBN = 0.474049`, `ΔN_eff = 2.0873`. **GEOMETRIC** (the tracking exponent n_eff is a property of the a₀ Seeley-DeWitt zeroth moment's H-response, not a phononic excitation amplitude; the BBN fraction is its modified-Friedmann image).

This is the structural spine of the whole review, and it is the principle-theoretic statement the R1 syntheses approach numerically but do not isolate. The canonical relation (verified to 0.000e+00 residual in `session-99-w2-workingpaper.md` §W2-2) is a one-parameter family in n_eff at fixed lever. Differentiating, `∂ ln(ρ_vac/ρ_rad)_BBN / ∂ n_eff = X = 40.2756`: a change of 0.01 in the tracking exponent moves the BBN fraction by a factor e^{0.40} ≈ 1.5. The dimensional reason is transparent — the radiation era spans ~40 e-folds of Hubble rate between BBN and today, and ρ_vac/ρ_rad scales as H^{n_eff−2}/H^{... } = H^{n_eff − 4} relative to radiation (ρ_rad ∝ H² in the radiation era via H² ∝ ρ_rad), so the BBN/today ratio carries (H_BBN/H_0)^{n_eff−2} after the radiation normalization. The exponent (n_eff − 2) is therefore the only quantity that matters at the lever's leverage.

The consequence is decisive for how to read every budget. Reaching ΔN_eff ≤ 1 (ratio ≤ 0.227113, the canonical element-abundance worst-case) at the fixed substrate lever requires **n_eff = 1.95984** (Sage-exact; this is the gate's mech_a value 1.959839). Reaching the Goldstein-Hill combined budget ΔN_eff ≤ 0.107 requires **n_eff = 1.904349** (Sage, my computation). The canonical from-below value is n_eff = 1.978111. So the framework's predicted exponent sits between the bare tracking value n = 2 and the value needed for relief — and the gap is small in exponent space (Δn ~ 0.018 to reach 0.227, Δn ~ 0.074 to reach 0.107) precisely because the lever amplifies it. **The CC-residual BBN tension is a question about the third decimal place of a tracking exponent**, which is exactly the kind of quantity a substrate-internal back-reaction (the QEQ-DRIVE) could fix or fail to fix.

### II.2 — What S99 W2-2 actually closed: parametric (constant-exponent) relief, three mechanisms

**Result**: `S99-W2-BBN-RELIEF` = **FAIL**, `any_substrate_justified = False`, `track_B_structural = True`; mech_a (n_eff = 1.959839, ×1.835 the substrate shift), mech_b (α_req = 0.479080 epoch-independent rescaling), mech_c (475.2 of 992 modes). atlas-08 Q29: **CORRIDOR CLOSED (structural)**, "no compute CF." **PHONONIC** (the BBN vacuum fraction is the a₀ tracking-vacuum at the radiation epoch). Verdict authoritative — NOT re-adjudicated here.

The precise scope of this closure is the load-bearing point, and I read the gate's own value string to fix it. All three mechanisms are evaluated **at the single substrate-justified lever X = 40.2756 and with the tracking exponent held at its canonical structure** — they ask "what constant rescaling, applied uniformly across all history, closes the gap?" and answer "none that the substrate forces." mech_a asks for a 1.835× larger from-below shift than the sub-leading-sign computation (`S98-MK3-1-C10-SUBLEADING-SIGN` = PASS, `a3_q0_analytic = −881.5351`) actually delivers — and that computation FIXES the shift, so a larger one is not derivable. mech_b asks for an epoch-independent α_V ≈ 0.479, not substrate-derived. mech_c asks for a half-of-all-modes dilution channel with no substrate warrant.

What this closure does NOT touch: a relief in which the **effective tracking exponent in the radiation era differs from its late-time value**, because the vacuum is produced after BBN (so n_eff^{early} is effectively −∞ before production: ρ_vac ≈ 0 at T > 1 MeV) or because it dilutes faster than H² early (EDE-like, ρ_vac ∝ a^{−m}, m > 4, so the effective n_eff^{early} > 2 in the radiation-era H-language). These are **time-profile** reliefs, not constant-rescaling reliefs. The gate's `track_B_structural = True` flag and the Q29 "structural" tag mark the constant-exponent corridor closed; they are silent on the time-profile corridor because S99 W2-2 never parameterized n_eff(a). The volovik R1 synthesis is therefore correct that "0.107 has no canonical match" (it is an external bound, not a gate threshold), and the mack/sagan R1 syntheses are correct that the time-profile relief is the surviving question — but neither set states that the closed corridor and the open corridor are different dimensions of the same one-parameter family. They are.

### II.3 — n=2 is NOT substrate-forced: the exponent the BBN arm depends on is itself underived

**Result**: `S99-W2-RELAXATION-CLOSURE` = **FAIL**, `slope_bare_UNFORCED = 3.415925` (dev = 2.415925 from target 1), `forced_only = True`, `C10-ObjectC-NOT-substrate-forced`, `k_curv = +3586.53` (Routh-Hurwitz restoring well). C10 stays **ASSUMED-PARTIALLY-PROVEN**; capstone §8.5 stays OPEN. **GEOMETRIC** (the friction-ODE attractor slope is a property of the q-variable dynamics / D_K eigenfrequency curvature). Verdict authoritative.

This is the result that ties the two arms together and that no R1 synthesis connects to the BBN arm explicitly. The mapping is exact (`session-99-w2-workingpaper.md` §W2-1, Sage-exact): the tracking law ρ_vac ∝ H^n gives, via (q − q*)² ∝ H^n, a friction-ODE attractor slope **slope = d ln q/d ln H = n/2**, so n = 2 ⇔ slope = 1. The bare substrate friction ODE q″ + 3Hq′ + V′(q) = 0 (with V = δρ_vac built from the 992 D_K eigenfrequencies, k_curv = +3586.53) produces an UNFORCED slope of 3.42, not 1 — slope = 1 (n = 2) arises ONLY when an external linear closure q_eq = c·H is IMPOSED. In other words, **the framework does not currently derive n = 2; it assumes it as a fluid closure.**

The implication for the BBN arm is direct and was not drawn in the R1 set. The BBN fraction `exp((n_eff − 2)·X)` is computed at n_eff ≈ 2 (the from-below departure from the assumed n = 2). But if n = 2 is not substrate-forced, then the radiation-era exponent is genuinely open — it could be the value that emerges from a substrate-internal q_eq(H) drive, which need not be 2 and need not be epoch-independent. **The same uncomputed object (the substrate q_eq(H) drive) controls both the late-time tracking slope AND the early-time ρ_vac(a) the BBN budget scores.** This is why a standalone BBN-relief compute is not the right gate: the BBN read-out is a downstream clause on the QEQ-DRIVE, not an independent calculation. The S99 W2-1 FAIL and the S99 W2-2 FAIL are two read-outs of one missing function.

### II.4 — The three literature relief corridors are three ansätze for n_eff(a); each maps to a substrate object

**Result**: Corridor A (post-BBN production, paper 09 Allali-Notari-Rompineve), Corridor B (EDE-like dilution, paper 10 Seto-Toda), Corridor C (q-theory friction profiles, papers 02/04/06). Each is a distinct early-time ρ_vac(a) shape. **PHONONIC** (all are time-profiles of the a₀ tracking vacuum). Papers are idea-generators, not authority.

The principle-theoretic reading collapses the three corridors onto one axis — the radiation-era effective exponent / production epoch — and assigns each a substrate counterpart and a falsifier:

- **Corridor A — post-BBN production.** Paper 09's loophole: element-abundance bounds are avoided if ρ_vac is produced after T ~ 1 MeV. Substrate counterpart: the GGE-relic / spectral-complexification that sources the effacement-era vacuum completes after the BBN window. This is the strongest relief (ρ_vac ≈ 0 at BBN ⇒ ΔN_eff^{BBN} ≈ 0 regardless of magnitude), but it is the most chronology-constrained: it requires the fold-transit → GGE-formation timeline to place ρ_vac buildup after BBN. The framework's reheating temperature T_RH = 1.70e15 GeV is ~18 orders ABOVE T_BBN ~ 1 MeV — the transit completes vastly before BBN, so the naive reading is that the vacuum exists at BBN. Corridor A therefore requires a SECOND, slow, post-BBN complexification distinct from the fold transit, which the framework does not currently carry. **Conditional on a chronology the framework has not derived.**

- **Corridor B — EDE-like dilution.** Paper 10's mechanism: ρ_DE ∝ a^{−m}, m = 4 or 6, peaked near matter-radiation equality, negligible at BBN. Substrate counterpart: an early-time tracking exponent steeper than n = 2 (in H-language, n_eff^{early} > 2, so ρ_vac/ρ_rad shrinks toward the past). This evades the DIRECT expansion-rate BBN channel but carries paper 10's residual: fitting the CMB then requires increased Ω_b h², which reduces D/H (raises χ²_Cooke). And the Goldstein-Hill bound (paper 11) is COMBINED BBN+CMB+BAO, so Corridor B must be negligible at BOTH BBN and the CMB-N_eff-sensitive epoch (recombination), strictly stronger than paper 10's BBN-only evasion. **Conditional on the substrate q_eq(H) producing n_eff^{early} > 2 AND on the Ω_b h² → D/H side-channel clearing.**

- **Corridor C — q-theory friction profiles.** Papers 02/04/06 supply computable ρ_vac(a). Paper 04's friction ODE IS the C10 Object-C ODE (the S99 W2-1 object); its u_eff trajectory (−0.883133 → −1/3) reaches Minkowski only on a measure-zero separatrix. Paper 02's f(R)-emergent ε_vac(H) = f(R = 12H²) fixes a relaxation time-profile from the chosen f(R) form. Paper 06's static-δq/oscillating-ξ split places DE as a static offset. Substrate counterpart: these ARE the candidate q_eq(H) drives the QEQ-DRIVE will test. Corridor C is not a separate relief — **it is the mechanism that decides whether Corridors A or B are realized**, because the q_eq(H) drive determines n_eff(a), hence the production epoch and dilution rate. **This is the load-bearing corridor; A and B are its possible outputs.**

The structural unification: Corridors A and B are the two ways an n_eff(a) profile can satisfy the BBN budget (vanish-then-appear, or dilute-steeply), and Corridor C (the QEQ-DRIVE) is the only one that can DERIVE which, if either, the substrate realizes. A and B are read-outs; C is the computation.

### II.5 — The budget reconciliation: 0.107 is external state-of-the-art, 0.227113 is the canonical gate threshold

**Result**: three distinct ΔN_eff bounds, NOT to be conflated (Sage-exact): element-abundance worst-case **0.227113** (canonical `S99-W2-BBN-RELIEF` threshold) → framework 2.0873 over by the gate metric (frac_below/bound = 2.087283); ANR CMB-era free-streaming 0.39 / fluid 0.46 (paper 09) → 5.3521× / 4.5376×; Goldstein-Hill combined BBN+CMB+BAO **0.107** (paper 11, N_eff = 2.990 ± 0.070) → **19.5075×**. **NON-PHONONIC** (these are external observational bounds; only the framework's 2.0873 is a substrate output).

**CONFLICT FLAGGED AND RESOLVED.** The volovik R1 synthesis (§IV.1) states "the index's ΔN_eff < 0.107 BBN bound does not match any canonical pin" and instructs carry-forwards to use the canonical fraction test (bound 0.227113), NOT 0.107. The mack and sagan R1 syntheses (and the focus brief) lead with the 19.5× figure against 0.107. Both are correct on their own terms, and the resolution is a layer distinction:

- **0.227113** (= 7/8·(4/11)^{4/3}, the denominator of the canonical ΔN_eff formula) is the gate's pre-registered threshold and the value `S99-W2-BBN-RELIEF` was scored against. The phonon-first R1 synthesis (§IV) states this resolution precisely: "0.107 is the EXTERNAL observational bound (Goldstein-Hill); 2.0873 is the framework's predicted value." This is the correct reading.
- **0.107** is the current tightest EXTERNAL bound (paper 11, arXiv 2603.13226), sharing the IDENTICAL ρ_rad = [1 + (7/8)(4/11)^{4/3} N_eff] ρ_γ definition the framework uses (paper 11 Eq. 1), so 2.0873 and 0.107 are directly comparable with no convention mismatch.

The honest statement: against the canonical gate threshold the framework is ~2.09× over (the gate metric); against the looser ANR CMB-era bounds ~4.5–5.4× over; against the current state-of-the-art combined bound **~19.5× over**. The 19.5× is the empirically binding number; the 2.09× is the gate-internal number. They differ because the gate was pinned to the element-abundance worst-case, not the combined budget. **This is a genuine threshold-currency gap**: the canonical gate `S99-W2-BBN-RELIEF` should carry the 0.107 combined budget as the binding external falsifier alongside its 0.227113 internal threshold (a registry hygiene item, NOT a re-adjudication — the FAIL verdict holds and tightens under either bound). I do NOT propagate 0.107 as a canonical pin; it is the external falsifier value, and any constant promotion must tag it as such.

### II.6 — The a(t)/non-ratio leg advanced in S99 W1 and is a prerequisite, not a sibling, of the QEQ-DRIVE

**Result**: `S99-W1-Q-NONRATIO-OBSERVABLE` = **INFO** (composite; sign = PASS, magnitude = INFO, regime = MARGINAL), `finite_across_crossing = True` (18 crossings), `sign_agree_frac_cross = 1.000000`, `H_bare_nonstationarity_relvar = 0.3887`, `aeff_relvar = 7.4e-07` (nonstationarity_OOM_gap = 5.719), exporting `arr_H_bare_t_backbone_for_S99-W2-RELAXATION-CLOSURE`. **GEOMETRIC** (the non-ratio observable is built on the emergent-metric H(τ) backbone). Verdict authoritative.

This is the result the focus brief did not foreground and that reorders the dependency chain. The S98-era a(t) gap (S98-W1-ROUTE-RECONCILIATION FAIL, q = 0/0 conformally-stationary) is what the G1 R1 syntheses (volovik, phonon-first) treat as still-open. But S99 W1 already executed the non-ratio observable the papers 01/03/11 motivate: it found a finite, sign-coherent observable across the fold (the `H_bare` backbone has 0.39 relative variance — genuinely non-stationary, OOM-separated from the conformally-stationary acoustic combination's 7e-07), and it EXPORTED that H(τ) backbone for the relaxation closure. So the W2-1 friction-ODE was integrated along a genuinely non-stationary H(τ), not the degenerate one. The q = 0/0 frame ambiguity is no longer the blocker for the relaxation closure — **the blocker is now that the friction ODE on the resolved H(τ) backbone gives an unforced slope of 3.42, not 1.** The R1 syntheses' V.1 carry-forwards (CF-S100-W1-SF54-MAPPING, the non-ratio observable) are partly RETROSPECTIVE: the W1 non-ratio observable landed INFO in S99, and its export is the INPUT to the QEQ-DRIVE. The dependency is W1 (done, INFO) → W2-1 (done, FAIL) → CF-S100-W2-1-QEQ-DRIVE (open). This corrects the G1 R1 framing that treats the a(t) gap and the C10 drive as two parallel open gaps; they are sequential, and the first leg has advanced.

---

## III. Gate Verdicts

All canonical (knowledge MCP / verdict files), surfaced to anchor the corridor map. NONE re-adjudicated.

| Gate | Verdict | Decisive Number / String |
|:-----|:--------|:-------------------------|
| `S99-W2-BBN-RELIEF` | **FAIL** | frac_below=0.474049, bound=0.227107, relief_factor=0.414115, extra_needed=0.479080; mech_a(n_eff=1.959839,×1.835)/mech_b(α=0.479080)/mech_c(475.2of992) all `any_substrate_justified=False`; `track_B_structural=True` |
| `S99-W2-RELAXATION-CLOSURE` | **FAIL** | slope_bare_UNFORCED=3.415925 (dev=2.416), slope_driven_IMPOSED=1.008273, `forced_only=True`, `target1_n2_domfrac=0.4100`, k_curv=+3586.53, `C10-ObjectC-NOT-substrate-forced` |
| `S99-W1-Q-NONRATIO-OBSERVABLE` | **INFO** | composite INFO; sign=PASS magnitude=INFO regime=MARGINAL; finite_across_crossing=True (18 cross); H_bare_nonstationarity_relvar=0.3887; nonstationarity_OOM_gap=5.719; exports H_bare backbone |
| `S98-MK3-2-BBN-VACUUM-FRACTION` | **FAIL** | ΔN_eff=2.0873; frac_below=0.4740; bound=0.2271; relief_factor=0.4141; X=ln(H_BBN/H_0)=40.2756; relief_direction=True |
| `S98-MK3-1-C10-SUBLEADING-SIGN` | **PASS** | divergence_type=A; sign_a3_meas=−1; a3_q0_analytic=−881.5351 (fixes the from-below n_eff shift) |
| `DILUTION-CC-66` | **PROVEN (S66)** | rho_vac_over_rho_obs=1.032; CC_OOM=115.5; **conditional on C10 + external FRW H** (present-epoch closure unaffected by BBN arm) |
| C10 (atlas-04 status) | **ASSUMED-PARTIALLY-PROVEN** | ρ_vac ~ M_Pl²H² scaling assumed; q_eq(H) drive NOT derived; n=2 not substrate-forced (S99 W2-1) |
| Q29 (atlas-08-freshness-S99) | **CORRIDOR CLOSED (structural)** | additional-relief (constant-exponent parametric) corridor closed; BBN-VOLOVIK-67/Window-8 stays LIVE (inventory Row #76, mack); no compute CF |

---

## IV. Structural Implications

### Relief-corridor map (the deliverable)

The C10/CC-residual BBN landscape, organized by the n_eff(a) principle of §II.1. Status keyed to canonical state.

| Corridor | Substrate object | What it requires | Status | Closed/open on what |
|:---------|:-----------------|:-----------------|:-------|:--------------------|
| **Constant-exponent parametric** (gate mech_a/b/c) | uniform rescale of n_eff, α_V, or mode count | substrate to force n_eff=1.95984, or α_V≈0.479, or 475/992 modes | **CLOSED (structural)** | Q29; none substrate-justified; FAIL `S99-W2-BBN-RELIEF` |
| **A — post-BBN production** (paper 09) | ρ_vac builds after T~1 MeV (effective n_eff^{early}=−∞ before production) | a slow post-BBN complexification distinct from the fold transit (T_RH=1.70e15 GeV ≫ T_BBN) | **CONDITIONAL** | on a fold→GGE chronology placing ρ_vac buildup post-BBN — NOT currently derived |
| **B — EDE-like dilution** (paper 10) | n_eff^{early}>2 (ρ_vac/ρ_rad steepens toward the past) | substrate q_eq(H) → n_eff^{early}>2 AND Ω_b h²→D/H side-channel clears AND CMB-era N_eff window cleared | **CONDITIONAL** | on the QEQ-DRIVE output AND the combined (not BBN-only) budget |
| **C — q-theory friction profile** (papers 02/04/06) | substrate-internal q_eq(H) drive fixing n_eff(a) | derive q_eq(H) from D_K back-reaction; does it give a radiation-era profile clearing 0.107? | **OPEN — load-bearing** | `CF-S100-W2-1-QEQ-DRIVE`; A and B are its possible outputs |
| **Late-time present-epoch closure** (DILUTION-CC-66) | a₀ tracks Volovik H² vacuum at z≈0 | (already closed) | **PROVEN (S66), unaffected** | independent of the BBN arm; ρ_vac/ρ_obs=1.032 |

**Reading of the map.** Two corridors are settled and three are coupled. The constant-exponent corridor is genuinely closed (the register is right). The present-epoch closure is genuinely proven and the BBN arm does NOT threaten it (the 115.5-OOM CC closure is a z≈0 statement; the BBN failure is a radiation-era statement; they are separated by the lever X and do not interact — a point the R1 syntheses correctly preserve by noting "present-epoch closure unaffected"). The three coupled corridors (A, B, C) are ONE corridor in disguise: corridor C (the q_eq(H) drive) is the computation, and corridors A and B are the two profile-shapes its output could take. **There is exactly one open compute: derive the substrate q_eq(H), read off n_eff(a), and evaluate ρ_vac(a) at radiation-era H against the 0.107 combined budget.** This is CF-S100-W2-1-QEQ-DRIVE with a BBN read-out clause appended.

### What opened

- **The BBN arm is re-cast from a closed dead-end to a downstream clause of an open gate.** atlas-08 Q29 closes the *parametric* corridor; this review shows the *time-profile* corridor is open and is identical to the QEQ-DRIVE. The "no compute CF" on Q29 is correct for the parametric question and should NOT be read as "the BBN arm has no surviving compute" — the surviving compute is the BBN read-out of CF-S100-W2-1-QEQ-DRIVE.
- **The exponent-sensitivity quantification** (∂ ln(ρ_vac/ρ_rad)_BBN/∂n_eff = X = 40.2756; n_eff = 1.904349 needed for 0.107) gives the QEQ-DRIVE a sharp, pre-registerable BBN target in exponent space.

### What is confirmed-stable (no shift)

- C10 stays ASSUMED-PARTIALLY-PROVEN; n=2 not substrate-forced (S99 W2-1). The QEQ-DRIVE is the path from ASSUMED to derived.
- DILUTION-CC-66 present-epoch closure (ρ_vac/ρ_obs = 1.032) unaffected.
- The equilibrium theorem ρ_V = ε − q dε/dq = 0 (papers 04/06 reconfirm) stays the wall forbidding the observed CC from being a GGE residual. The relaxation is a dynamical extension, not a reopening.

### Conflicts surfaced (flagged per discipline)

1. **CONFLICT — budget value 0.107 vs 0.227113 (RESOLVED as a layer distinction, §II.5).** volovik R1 calls 0.107 non-canonical and routes carry-forwards to the 0.227113 fraction test; mack/sagan R1 and the focus lead with 19.5× against 0.107. Resolution: 0.227113 is the canonical gate threshold; 0.107 is the external state-of-the-art falsifier (paper 11, same ρ_rad definition). Both correct; the gate should carry 0.107 as its binding external falsifier (hygiene CF V.3). Not a re-adjudication — FAIL holds under both.
2. **CONFLICT — focus brief vs canonical Q29 on "is a BBN-relief gate pre-registerable NOW?"** The focus asks for a standalone BBN-arm relief gate; canonical Q29 says the relief corridor is CLOSED with no compute CF. Resolution (§II.2, §IV): the CLOSED corridor (constant-exponent parametric) and the pre-registerable corridor (time-profile / n_eff(a)) are orthogonal. A standalone BBN gate is NOT independently pre-registerable; it IS pre-registerable as a read-out clause on CF-S100-W2-1-QEQ-DRIVE (V.1). The two views are consistent once the dimension is named.
3. **MINOR — R1 a(t)/non-ratio framing is partly retrospective.** volovik/phonon-first R1 V.1 carry-forwards present the non-ratio observable as a forward S100 compute; canonically `S99-W1-Q-NONRATIO-OBSERVABLE` already landed INFO in S99 and exported the H_bare backbone consumed by W2-1. The forward leg is the QEQ-DRIVE (W2), not the non-ratio observable (W1, done). Dependency is sequential, not parallel (§II.6).

### Substrate-first framing preserved

Every corridor flows D_K eigenvalues → a₀ Seeley-DeWitt zeroth moment → tracking-vacuum H-response n_eff(a) → modified-Friedmann ρ_vac(a) → BBN abundances / N_eff. The BBN budget is the laboratory-IN shadow of the substrate-IS tracking exponent; the substrate IS the early-vacuum time-profile, it is not a fluid placed in an FRW container. The q-theory papers (02/04/06) are controlled microscopic cousins of the substrate's q-variable (the volume-preserving Jensen deformation), never a container the substrate sits inside.

---

## V. Carry-Forward Computations

```
V.1. CF-S100-W2-1-QEQ-DRIVE with appended BBN read-out clause (the single load-bearing compute)
   - What: Derive a substrate-internal q_eq(H) drive (H-dependent equilibrium/source from D_K
     back-reaction — e.g. a back-reaction closure H² = f(ρ_relic, S_SA) per capstone §6.3, NOT an
     imposed CPL fluid law), re-integrate the friction ODE q″ + 3Hq′ + V′(q)=0 (V=δρ_vac from the
     992 D_K eigenfrequencies, k_curv=+3586.53) along the S99-W1 H_bare backbone WITHOUT the imposed
     linear closure, and READ OFF the radiation-era effective exponent n_eff(a). Then evaluate
     ρ_vac(a) = α_V M_Pl² H^{n_eff(a)} at the BBN epoch via (ρ_vac/ρ_rad)_BBN = frac_base·exp((n_eff−2)·X)
     and at recombination. Output: q_eq(H) map; n_eff(a) profile; (ρ_vac/ρ_rad) at BBN and at the
     CMB-N_eff-sensitive epoch; corridor classification (A post-BBN / B EDE-like / radiation-like).
   - Inputs: S99-W1-Q-NONRATIO-OBSERVABLE npz (H_bare backbone export, audit 8bcbca9c…);
     S98-MK3-1-C10-SUBLEADING-SIGN npz (sign_a3_meas=−1, a3_q0_analytic=−881.5351 — drive sign already
     derived); V′(q)=δρ_vac(τ) from D_K spectral moments; det g_τ=const Jensen volume-preservation;
     frac_base=1.144730, X=40.2756, n_eff(canonical from-below)=1.978111;
     delta_N_eff_vacuum_BBN_below=2.0873, rho_vac_over_rho_rad_BBN_below=0.474049; N_eff_SM=3.044,
     T_BBN_GeV=0.001; paper 04 ODE (Eqs. 17a-c/19/21), paper 02 f(R) ε_vac(H)=f(R=12H²) (Eqs. 13-16).
   - Gate: CF-S100-W2-1-QEQ-DRIVE [SIGN], with TWO clauses (PASS-AND):
       (slope clause) PASS iff substrate q_eq(H) yields |d ln q/d ln H − 1| ≤ 0.05 UNFORCED
         (n=2 substrate-forced; C10 Object-C → derived; §8.5 OPEN→CLOSED);
       (BBN read-out clause) PASS iff the SAME q_eq(H) gives n_eff^{early} clearing ΔN_eff ≤ 0.107 at
         BOTH BBN and recombination (combined Goldstein-Hill budget); INFO iff it clears the canonical
         0.227113 element-abundance bound (n_eff ≤ 1.95984) but not 0.107 (n_eff ≤ 1.904349);
         FAIL iff radiation-like (n_eff^{early}≈2 ⇒ ΔN_eff≈2.09, the standing failure persists).
     Composite: PASS only if BOTH clauses PASS; this is the C10 closure gate.
   - Effort: 6-8 hours, 1 agent session (volovik or transit-dynamics; ODE integration + substrate
     ε(q) coupling + BBN lever read-out; reuses S99 W1/W2 npz).

V.2. Corridor-A chronology check — does the substrate place ρ_vac buildup after BBN?
   - What: Trace the substrate vacuum-complexification timeline from the fold transit (T_RH=1.70e15 GeV)
     through BBN (T~1 MeV) and test whether ANY substrate channel builds ρ_vac AFTER BBN (distinct from
     the prompt fold-transit GGE relic, which completes ~18 OOM above T_BBN). Concretely: is there a slow
     secondary complexification (post-transit spectral reorganization) whose ρ_vac is ≈0 at T>1 MeV?
     Output: ρ_vac(T) buildup curve; verdict on whether Corridor A (post-BBN production) is substrate-realizable.
   - Inputs: T_RH=1.70e15 GeV (S76); fold-transit/GGE chronology (N_pair=59.8, P_exc=1.000); n=2 tracking
     onset epoch; paper 09 post-BBN-production loophole; T_BBN_GeV=0.001, z_BBN=4e8.
   - Gate: NEW S100-C10-CORRIDOR-A-CHRONOLOGY (conditional, fires only if V.1 BBN clause = INFO/FAIL).
     PASS iff a substrate channel gives ρ_vac(T>1 MeV)≈0 (Corridor A realized, ΔN_eff^{BBN}≈0); FAIL iff
     ρ_vac is present at full magnitude at BBN (Corridor A NOT substrate-realizable; only Corridor B survives).
   - Effort: 3-4 hours, 1 agent session (volovik/mack; chronology derivation). Depends on: V.1 (BBN clause).

V.3. C10 gate budget-currency hygiene — carry 0.107 as the binding external falsifier
   - What: Update S99-W2-BBN-RELIEF / S98-MK3-2-BBN-VACUUM-FRACTION to record the Goldstein-Hill combined
     BBN+CMB+BAO budget ΔN_eff<0.107 (paper 11, N_eff=2.990±0.070) as the binding EXTERNAL falsifier
     alongside the canonical element-abundance threshold 0.227113. Document the three-bound hierarchy
     (0.107 combined / 0.39–0.46 ANR CMB-era / 0.227113 element-abundance) so downstream consumers cite
     the right one. Tag 0.107 explicitly as external-observational, NOT a substrate pin.
   - Inputs: paper 11 (arXiv 2603.13226) N_eff=2.990±0.070, ΔN_eff<0.107; paper 09 (arXiv 2404.15220)
     0.39/0.46; delta_N_eff_vacuum_BBN_below=2.0873; the existing gate verdict lines; the shared ρ_rad
     definition (paper 11 Eq. 1 ≡ canonical S66 formula).
   - Gate: registry-hygiene; new update_constant `delta_N_eff_budget_combined_GH2026 = 0.107` with
     provenance tag "EXTERNAL observational falsifier (Goldstein-Hill 2026), NOT substrate-derived".
     INFO-class (threshold-currency, not new physics; the FAIL holds and tightens under either bound).
     Routes to mack-cosmic-bridge (falsifier-master-inventory Row #76 BBN-VOLOVIK-67 sole writer).
   - Effort: 1 hour, 1 agent session.

V.4. Exponent-sensitivity pre-registration — the BBN target in n_eff space
   - What: Pin the exponent-space BBN targets so the V.1 BBN read-out clause has hard thresholds:
     ∂ ln(ρ_vac/ρ_rad)_BBN/∂n_eff = X = 40.2756; n_eff ≤ 1.95984 clears 0.227113; n_eff ≤ 1.904349 clears
     0.107; n_eff ≥ 1.978111 (canonical from-below) is the standing-FAIL value. Express the radiation-era
     n_eff(a) the QEQ-DRIVE must deliver. Sage-QQ the three crossing exponents to publication precision.
   - Inputs: frac_base=1.144730, X=40.2756, bound_elem=0.227113, budget_GH=0.107, n_eff_canonical=1.978111;
     the lever relation (ρ_vac/ρ_rad)_BBN=frac_base·exp((n_eff−2)·X).
   - Gate: feeds V.1 BBN read-out clause as its pre-registered threshold table. INFO-class
     (pre-registration support; no new verdict). Sage-exact rationals required per regulator-pin-discipline.
   - Effort: 1 hour, 1 agent session (mostly Sage QQ + a pre-registration block).

V.5. Corridor-B side-channel — Ω_b h² → D/H residual under EDE-like (n_eff^{early}>2) relief
   - What: IF V.1 returns Corridor B (EDE-like, n_eff^{early}>2 clearing the direct BBN channel), compute
     the residual constraint via the inferred-baryon-density channel (paper 10's warning): the CMB-fit-
     required Ω_b h² shift and its propagated D/H vs Cooke+18 (2.527e-5±0.030e-5). Output: Δ(Ω_b h²),
     predicted D/H, χ²_Cooke contribution.
   - Inputs: V.1 n_eff(a) profile (Corridor B branch); Omega_b, omega_H2 (canonical — query get_constant);
     paper 10 EDE-vs-N_eff baryon-density mechanism; paper 11 compressed Ω_b h²=0.022371; Cooke+18 D/H.
   - Gate: NEW S100-C10-CORRIDOR-B-OMEGAB-DH (conditional, fires only if V.1 = Corridor B). PASS iff
     predicted D/H within 2σ of Cooke+18; FAIL iff the baryon-density channel reintroduces >2σ D/H tension
     (Corridor B relief incomplete; combined budget not cleared). Depends on: V.1 (Corridor B branch).
   - Effort: 2-3 hours, 1 agent session.
```

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | BBN arm is a tracking-exponent problem: ∂ln(ρ_vac/ρ_rad)_BBN/∂n_eff = X = 40.2756; n_eff=1.904349 clears 0.107 | GEOMETRIC | Principle isolated | Whole C10/CC-BBN landscape collapses to "what is n_eff(a) in the radiation era?" |
| 2 | S99-W2-BBN-RELIEF closed the CONSTANT-exponent corridor (mech_a/b/c, none substrate-justified) | PHONONIC | FAIL; Q29 CORRIDOR CLOSED (structural) | Closure is real but narrow; time-profile corridor untouched and orthogonal |
| 3 | n=2 NOT substrate-forced: bare friction-ODE slope=3.42, slope=1 only under imposed q_eq=c·H | GEOMETRIC | S99-W2-RELAXATION-CLOSURE FAIL | The exponent the BBN arm depends on is itself the underived object; one missing q_eq(H) drives both |
| 4 | Three literature corridors = three n_eff(a) ansätze; C (q_eq drive) is the computation, A/B are its outputs | PHONONIC | A/B CONDITIONAL, C OPEN load-bearing | Exactly one open compute: derive q_eq(H), read off ρ_vac(a) at BBN+recomb vs 0.107 |
| 5 | Budget reconciliation: 0.227113 canonical gate threshold vs 0.107 external state-of-the-art (19.5×) vs 0.39–0.46 ANR | NON-PHONONIC | CONFLICT RESOLVED (layer distinction) | Gate should carry 0.107 as binding external falsifier; FAIL holds under both (V.3) |
| 6 | S99-W1 non-ratio observable landed INFO; exported H_bare backbone consumed by W2-1 | GEOMETRIC | INFO; a(t) leg advanced | a(t) gap and C10 drive are SEQUENTIAL not parallel; forward leg is QEQ-DRIVE (W2), not W1 |
| 7 | DILUTION-CC-66 present-epoch closure (ρ_vac/ρ_obs=1.032) unaffected by BBN arm | PHONONIC | PROVEN (S66), stable | z≈0 closure and radiation-era BBN failure are lever-separated; no interaction |

---

*Anchoring note: every framework-state claim verified against canonical via knowledge MCP (search_knowledge / get_constant / query_entity / trace_entity) on 2026-06-04. The two indexes and the four R1 syntheses are treated as INPUT/idea-generators per the Focus, not authority; the four canonical gate verdicts (S99-W2-BBN-RELIEF FAIL, S99-W2-RELAXATION-CLOSURE FAIL, S99-W1-Q-NONRATIO-OBSERVABLE INFO, S98-MK3-2-BBN-VACUUM-FRACTION FAIL) and the atlas-08 Q29 closure are authoritative and NOT re-adjudicated. Three conflicts flagged and resolved: (1) budget 0.107-vs-0.227113 = external-falsifier-vs-canonical-gate-threshold layer distinction; (2) focus-vs-Q29 "BBN gate pre-registerable now" = the closed constant-exponent corridor is orthogonal to the open time-profile corridor (pre-registerable only as a QEQ-DRIVE read-out clause); (3) R1 a(t)/non-ratio carry-forwards are partly retrospective (W1 already INFO). All ratios Sage-exact: dNeff 2.0873 over budgets = 2.087×(elem 0.227113) / 5.352×(ANR-fs 0.39) / 4.538×(ANR-fl 0.46) / 19.507×(GH 0.107); n_eff crossings 1.95984 (→0.227113) / 1.904349 (→0.107) at lever X=40.2756; friction-ODE slope=n/2 (n=2 ⇔ slope=1). No probability estimates (Sagan's domain); structural characterization only.*
