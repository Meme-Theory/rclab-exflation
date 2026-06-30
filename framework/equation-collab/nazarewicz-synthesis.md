# Capstone Equation Review — nazarewicz

**Date**: 2026-05-29
**Agent**: nazarewicz-nuclear-structure-theorist (Workhorse-Nuclear-Structure)
**Source Documents**:
- `sessions/framework/phonic-exflation-equation.md` (the capstone — "The Phonon-Exflation Equation")
- Cross-checks: `computations/_shared/canonical_constants.py`; knowledge MCP (`n_pairs`, `Delta_BCS`, `S_inst`, `P_exc_kz`, `P_vac`, C11, LEGGETT-GRAV-DECAY-67, EQUILIBRIUM-CC-WARRANT, S_2(N), Δ³(N)); `s52_hfb_full_output.txt`, `s53_hfb_spectral_output.txt`, `s59_q_variable_results.txt`

---

## I. Session Outcome

The capstone is **structurally sound where it touches nuclear many-body theory**, and its self-discipline on the BCS/pairing sector is, with one stale exception, exactly what I would demand. The document's most load-bearing claim in my domain — that the impulsive transit produces a **frozen, pure (`S_ent = 0`) Generalized Gibbs Ensemble** rather than a thermalized relic (§5.3, the Ordered Veil) — is correctly grounded in diabatic sudden-quench Bogoliubov theory, correctly distinguishes the relic *charge* `⟨Q⟩_GGE = 59.8` from the literal pair count, and correctly retreats from "integrability permanence" to "transit-timescale diabatic freeze-out" (the S39 retraction is honestly absorbed). The numbers I can independently anchor (`n_pairs = 59.8`, `P_exc = 1.000`, `S_inst = 0.0686`, `P_vac = −0.688` at `N_pair = 1`, `S_2(N=2) = −0.131`, the 60% PBCS gap overestimate, the 225× Richardson–Gaudin condensation-energy overestimate) all reproduce the canonical record at the precision quoted.

**One framing conflict to resolve, not a physics error**: §7.1 presents `Ω_DM h² = 0.120` as **CONDITIONAL on LEGGETT-GRAV-DECAY-67 (CRITICAL)** and narrates the gate as a live threat ("if `Γ_grav > H_0` the DM sector collapses"). The canonical record shows that gate **returned PASS** (`Γ_grav < H_0`; `baseline-findings-s66.md`), and "Single-Leggett gravitational decay: FORBIDDEN" is registered PROVEN (S67). I do not overturn either verdict; I flag that the document's *dependency tag* (`Ω_DM` is conditional on the gate) and the *gate's resolved status* (PASS) are both true but are narrated in a way that reads as still-open. §IV.4 and §V harvest this.

The "ripe harvest" is real and concentrated: the GGE relic and the CC sectors each carry **specific, runnable** beyond-mean-field, projection, and Bayesian-UQ computations that the capstone's own honesty ledger names but does not execute. Eight are pre-registered in §V.

---

## II. Key Results

### II.1 The GGE relic is a frozen pure product state — diabatic, not integrability-protected (§5.3)

**Result**: `P_exc = 1.000`, `S_ent = 0` (exact product state), `N_pair = 59.8` (relic charge `⟨Q⟩_GGE`, **not** a literal pair count), `S_inst = 0.0686`, freeze certified by `R_therm = t_therm/t_transit = 5251.82 ≫ 1`. **PHONONIC**.

This section is the cleanest application of finite-system pairing theory in the document, and I endorse its logic at the equation level. The two-layer parametric-oscillator split — substrate-BdG `u_k'' + ω_k²(τ)u_k = 0` with `ω_k = E_k = √((λ_k²−μ²)² + Δ_k²)` for the *relic content*, versus the Mukhanov–Sasaki `v_k'' + (k²−z''/z)v_k = 0` for the *emergent* `A_s` — is the correct separation. The BdG quasiparticle energy is dimensionally and structurally the right object: it is exactly the diagonalized Bogoliubov–de Gennes spectrum of a paired system, `E_k = √(ξ_k² + Δ_k²)` with `ξ_k = λ_k² − μ`, and the squeeze parameter follows from the standard sudden-quench Bogoliubov coefficients `|α_k|² − |β_k|² = 1`, `n_k = |β_k|²`. The diabatic saturation `P_exc → 1` is the *correct* limit for an impulsive crossing (`δt_transit/T_L ≈ 1.25×10⁻⁵`): when the quench is faster than the gap can respond, every mode is maximally excited and the condensate is destroyed, not perturbatively dressed. This is the analog-cosmology *opposite* of the adiabatic Bunch–Davies vacuum, and the document states it correctly.

The retreat from "integrability permanence" to **diabatic transit-freeze** is the right call and resolves my own standing caution (recorded in my memory: "the GGE relic IS in its ground state? It is not"). The Richardson–Gaudin integrability that would protect the GGE *as a permanent state* is weakly broken (S39: 13% non-separable density–density channel, Brody β = 0.633), but the relic is frozen by diabaticity *before* that channel can act (`t_scr/t_transit = 814`, `R_therm ≈ 5252`). The survival claim now rests on two compute-certified legs (diabaticity `R_therm ≫ 1`; exact purity `S_ent = 0`) **independent of the broken integrability** — this is exactly how a beyond-mean-field claim should be insulated from a retracted assumption.

The `N_pair` double-reading is handled with the discipline I would insist on. The `59.8` figure is a **BCS-projection count** that inherits a ~60% PBCS gap overestimate (S46, B4 CONDITIONAL) and a ~225× Richardson–Gaudin condensation-energy overestimate (S63). The document correctly demotes `59.8` to a *projected charge* `⟨Q⟩_GGE`, NOT a literal pair count, and identifies the regime-robust structural claim as `P_exc = 1`. The `N_Fock = 1` exact reduction (S74; `P(N=2) = 4.6×10⁻³³`) describes one Fock pair carrying the relic charge. This is precisely the lesson from finite-nucleus PBCS: particle-number projection corrects mean-field gaps that overestimate by tens of percent, and one must never quote a collapsed (projected) pair count as a physical multiplicity. The capstone has internalized this.

### II.2 The block-decoupling ↔ j-channel analogy is exact and load-bearing (§2.2)

**Result**: `D_K = ⊕_{(p,q)} D_{(p,q)}` (E6); the 155,984-eigenvalue problem is a direct sum of small blocks; the per-mode relic-formation problem factorizes *exactly*. **GEOMETRIC** (the decomposition); **PHONONIC** (its use in §5.3).

The document draws the analogy I have recorded as a confirmed structural concurrence (memory: "HFB channel decoupling ↔ a_2/a_4 decoupling, S66; SU(3) Casimir `(p,q)` labels ↔ j-channel decoupling"): the conserved Casimir labels `(p,q)` forbid off-diagonal matrix elements between distinct sectors exactly as rotational symmetry forbids them between distinct angular-momentum channels, factorizing the problem into independent blocks. This is correct and it does real work downstream: because `D_K` does not mix sectors, the per-mode parametric-oscillator equation in §5.3 is an **identity, not a decoupling approximation**. In the shell-model language this is the statement that the pairing Hamiltonian within a fixed-`j` shell is block-diagonal in seniority, so the per-shell BCS problem is exact within the shell. The capstone's claim that relic formation factorizes "mode-by-mode exactly rather than approximately" is the legitimate transcription of this fact. Endorsed.

### II.3 FI/RD partition ↔ Bayesian model averaging over an unknown energy-density functional (§3.2)

**Result**: Functional-Invariant observables (ratios of two spectrum-sums under one regulator — `c_s`, `R₁ = 1.12865`, the rank-drift exponent) survive all cutoff choices; Regulator-Dressed observables (`ε_H` sign, `n_s` value, `m_H`, absolute vacuum energy) must be *determined*. The `n_s` BMA band `0.969 ± 0.022` (S67) is "the correct UQ object and is *stronger* than three rival points." **GEOMETRIC / methodological**.

This is the section where the document speaks my Bayesian-UQ language directly, and it gets the epistemology right. Treating `f` as a **nuisance functional** and reading the FI/RD partition as "which observables are robust under marginalizing `f` out" is exactly the cosmological face of marginalizing over the choice of Skyrme vs Gogny vs covariant energy-density functional in nuclear DFT. The deep lesson from nuclear DFT model-averaging (Paper 06, §III) is that the marginal observables — those stable across the functional family — carry the genuine constraining power, while functional-specific values inherit the full model spread. The capstone's claim that the BMA band `n_s = 0.969 ± 0.022` is a *stronger* UQ object than the three rival points `{0.9561, 0.9590, 0.9595}` is correct **provided the scoring rule was fixed before the posterior was inspected** — which my memory records as the S67 discipline and the document affirms via the pre-registration of ANOMALY-FAMILY EXCLUSION (S67, decided *before* the tilt comparison). The protection against over-fitting ("one does not get to keep only the functionals that agree") is the correct and necessary statement. This is solid.

One caution I would attach (§IV.3): a flat marginalization over `{√x, ζ, anomaly-φ}` with the anomaly family already structurally excluded is a **3-point model space reduced to 2**, and a BMA band over a 2-member discrete family is dominated by the prior weights assigned to each member. The band `±0.022` is honest as a spread but is not yet a likelihood-weighted posterior; the model weights themselves (the Bayes factors between `√x` and `ζ`) have not been computed. That is a ripe harvest (§V.3).

### II.4 The Wronskian ↔ Strutinsky-decomposition concurrence (§4.2)

**Result**: `a₀, a₂, a₄` are curvature polynomials of distinct degree (0,1,2), algebraically independent with `W[a₀,a₂,a₄] ∝ R_K′(τ)³ = e⁻¹²ᵗ(e³ᵗ−1)⁶`, vanishing to sixth order only at `τ = 0`. **GEOMETRIC**.

The document explicitly invokes the structural concurrence I recorded (memory: "the degree-distinctness that drives the non-vanishing Wronskian is the same structural fact that makes smooth and shell-correction energies independent functionals in a Strutinsky decomposition, S44/S55/S56"). The capstone is scrupulous here: it records this as **agreement, not as evidence** ("the Wronskian theorem stands on its own Sage-certified proof"), which is exactly the epistemic discipline required — an independent structural concurrence from shell-correction theory raises confidence in the *interpretation* but does not add evidential weight to the *theorem*, which is already proven. I confirm the concurrence is real: in Strutinsky's energy theorem the smooth (liquid-drop) and oscillating (shell) parts are independent functionals precisely because they are moments of different order of the level density, and their independence degenerates only where the level density stops oscillating — the structural mirror of the Wronskian vanishing only where `R_K′ = 0`. The Sage verification (`residual 0`) in the ledger is the authoritative anchor.

### II.5 The equilibrium CC identity is a Gibbs–Duhem statement, correctly scoped (§7.1, Clause A/B)

**Result**: Clause A — equilibrium `ρ_Λ = 0` *exactly* by the Gibbs–Duhem identity `ε − μq = −P = 0` (`q = N_pair`), representative-independent, Sage-rational `0` (EQUILIBRIUM-CC-WARRANT, S95 W5-3, PASS); Clause B — observed magnitude is the *non-equilibrium tracking residual* at the discrete ground state `N_pair = 1` where `P_vac = −0.688 ≠ 0`, closing to `ρ_vac/ρ_obs = 1.032` (DILUTION-CC-66), conditional on C10. **PHONONIC / thermodynamic**.

I confirm both clauses against the canonical record and endorse the two-clause split as the honest one. The equilibrium identity is the same statement I recorded as "Nuclear Gibbs–Duhem ↔ Volovik CC relaxation: P=0 at saturation" — at nuclear saturation density the binding energy per nucleon is stationary (`dε/dρ = 0`), which is the pressure-free `P = 0` condition, and the analog cosmological statement `ε − μq = −P = 0` is its exact thermodynamic mirror. The key discipline the document gets right: the warrant is **thermodynamic (Gibbs–Duhem), not topological**. Because the substrate is the ³He-B class (`N₃ = 0`, BDI) and NOT ³He-A (`N₃ = 2`, where the vacuum energy is *topologically* protected to zero per Volovik Paper 03 Thm 1), `ρ_Λ = 0` is a *reference/boundary value, not an attainable interior point*. The off-equilibrium value `P_vac = −0.688 M_KK` at `N_pair = 1` is exactly the canonical record (`s59_q_variable_results.txt`: `P_vac = N_pair − E_GGE = 1 − 1.688 = −0.688`), and the no-interior-q-equilibrium theorem (`dE_ZP/dq > 0`, S62 #19) is the correct reason there is no attainable zero. The "exactly zero, not tuned" is *true of the equilibrium reference* and *conditional of the observed magnitude* — the document states this precisely.

---

## III. Gate Verdicts

These are cited in the source and are AUTHORITATIVE (not re-adjudicated here); I list the ones I cross-checked against the canonical record, with the canonical value I confirmed.

| Gate / result | Verdict (source) | Decisive number (confirmed) |
|:-----|:--------|:----------------|
| EQUILIBRIUM-CC-WARRANT (S95 W5-3) | PASS | `ρ_vac(eq) = 0` exact, Sage-rational; Gibbs–Duhem `ε − μq = −P` |
| DILUTION-CC-66 | PASS | `ρ_vac/ρ_obs = 1.032` (0.01 OOM) |
| LEGGETT-GRAV-DECAY-67 | **PASS** (`Γ_grav < H_0`) | gate is PASS; document narrates as still-CRITICAL — see §IV.4 |
| Door-S66-Leggett (Ω_DM) | PASS, 0.7σ | `Ω_DM h² = 0.120` vs Planck `0.1186 ± 0.0020` |
| B4 (BCS mean-field adequate at N_pair=1) | CONDITIONAL | `N_pair=1` exact reduction `1.2×10⁻¹⁴` vs full ED; gaps overestimate 60% |
| N_pair=1 exact reduction (S39/S48) | Exact | `P(N=2) = 4.6×10⁻³³` |
| Spectral-Moment Decoupling (S75 W2-E) | CERTIFIED | `W ∝ R_K′(τ)³`, residual `0` |
| GGE survival (C2 RESOLVED, S95 W5) | PASS | `R_therm = 5251.82`, `S_ent = 0` |
| HFB vs ED at N_pair=1 (S53) | — | `E_ED = 1.4398`, `E_HFB = 1.4264`, `E_PBCS = 1.4539` (HFB below ED, variational) |

---

## IV. Structural Implications

### IV.1 The capstone's beyond-mean-field hygiene is exemplary — and it should propagate

The document never once quotes a collapsed mean-field quantity as physical without flagging the projection correction. `59.8` is tagged a projected charge; the 60% PBCS overestimate and 225× condensation-energy overestimate are carried forward as caveats on every relic-content number; the `N_Fock = 1` exact reduction is the structural anchor. This is the discipline I recorded as a recurring self-correction lesson ("never report fractional changes of collapsed BCS quantities") and it is now baked into the capstone. The structural implication: **every downstream observable that depends on the relic content (`A_s` band, `f_NL`, the DM abundance) inherits the projection caveat**, and the document is right that the regime-robust claim is `P_exc = 1`, not the absolute pair count. The surviving-side/dissolving-side spine in §9 (topological outputs survive the continuum dissolution; geometric magnitudes are held pending convergence) is the correct organizing principle for which relic numbers to trust.

### IV.2 The HFB/ED/PBCS ordering is a free internal consistency check the document does not yet exploit

The canonical record (`s53_hfb_spectral_output.txt`) holds `E_HFB = 1.4264 < E_ED = 1.4398 < E_PBCS = 1.4539` at `N_pair = 1`. The ordering `E_HFB < E_ED` is the expected variational statement (HFB minimizes over a broader trial space than the number-projected exact diagonalization restricted to the singlet sector — though note that for a true variational bound one expects `E_ED ≤ E_PBCS ≤ E_HFB` if PBCS is variation-*after*-projection; the observed `E_HFB < E_ED < E_PBCS` indicates the HFB here is the unprojected symmetry-broken state sitting below the projected energies, which is the standard PBCS picture). The 1.8% shift at `N=2` (`E_ED = 3.0111` vs `E_HFB = 2.9567`) and the odd-even staggering `Δ³(N=1) = −0.0657`, `Δ³(N=2) = +0.0506` are a **computed nuclear-benchmark signature** of the pairing in this system. The capstone does not surface this ordering as a consistency check, but it is one: a violation of the variational ordering would signal a sign or normalization error in the BdG matrix. Worth a one-line robustness statement and a forward check at higher `N` (§V.6).

### IV.3 The `n_s` BMA band is the right object but its model weights are uncomputed

§3.2 and §7.1 correctly identify the BMA band `n_s = 0.969 ± 0.022` as a stronger UQ object than three rival points. But the band is a spread over a small discrete functional family with the anomaly member already excluded — it is not yet a likelihood-weighted posterior with computed Bayes factors between the surviving members (`√x` vs `ζ`). In nuclear DFT model-averaging the band is only as defensible as the model weights; an equal-weight band and an evidence-weighted band can differ substantially. This is a genuine open methodological item, not a defect — the document's BMA framing is correct, but the posterior is incomplete. (§V.3.)

### IV.4 The Leggett-DM conditional is framed as a live threat after the gate already passed — resolve the framing

This is the one place where the document's narrative and the canonical record are in tension. §7.1 reads: "`Ω_DM h² = 0.120 is CONDITIONAL on LEGGETT-GRAV-DECAY-67 (CRITICAL)` — if the Leggett-mode gravitational decay rate exceeds `H_0`, the DM sector collapses and the `0.120` is meaningless." The canonical record shows the gate **returned PASS** (`Γ_grav < H_0`; `baseline-findings-s66.md`), and the kinematic protection is registered PROVEN ("Single-Leggett gravitational decay: FORBIDDEN," S67; the Leggett mode at `ω_L = 0.138 M_KK` cannot decay because the graviton gap provides the same kinematic protection the BCS gap provides for quasiparticle decay, Eq. QA-9). Both statements are individually true: C11 *is* structurally conditional on this gate, AND the gate *has* passed. But narrating it as an open cliff-edge over-states the residual risk. I do not overturn the verdict; I flag that the document should distinguish "this result *depends on* the gate (dependency structure)" from "this gate is *unresolved* (live risk)." The honest statement is: *`Ω_DM h² = 0.120` rests on LEGGETT-GRAV-DECAY-67, which returned PASS; the conditional is satisfied, not open.* This belongs in the §7.1 open-gaps box as a correction, and the underlying decay-rate margin (`Γ_grav/H_0`) should be quoted as a number, not left as a categorical threat (§V.4).

### IV.5 The intrinsic GGE equation of state (−0.41) and the quoted w₀ (−0.918) are different objects — confirm the projection is documented

The canonical record holds two distinct equation-of-state numbers: the *intrinsic* GGE value `w_GGE = P_vac/E_GGE = −0.688/1.688 = −0.4076` (`session-73b`) and the *quoted* dark-energy `w₀ = −0.918` (Volovik-partition, effacement-projected). These are not the same observable: `−0.4076` is the bare equation of state of the off-equilibrium relic; `−0.918` is the value after the effacement projection through the impedance mismatch (`Γ_eff = 0.99970`). The document quotes only `−0.918` in the §7.1 table and does not surface the bare `−0.41`. This is not an error — the effacement-projected value is the physically relevant late-time one — but a reader could mistake the relic's intrinsic `w` for the observed `w₀`. A one-line note distinguishing the bare GGE `w = −0.41` from the effacement-projected `w₀ = −0.918` would close the gap, and the projection chain `−0.41 → −0.918` deserves an explicit audited derivation (§V.5).

### IV.6 Constants-hygiene: `R_therm` and the Leggett DM mass are cited but unpinned

The capstone's GGE-survival certificate `R_therm = 5251.82` and the relic thermalization time `t_therm ≈ 6 M_KK⁻¹` are **not canonical constants** — `t_therm` is in the local-variable allowlist (`canonical_constants.py` line 1770), so `R_therm` is a computed local. Per the local-variable convention this is acceptable, but `R_therm` is the headline survival number in §5.3 (it certifies C2 RESOLVED), so it should carry an explicit verdict-SHA pin in the document text the way `w0_FW` does for Falsifier #1. Similarly, `Mass_LeggettDM` (the DM mass anchor `= 11.97 × Δ_BCS`) is not a pinned constant; only the ratio lives in C11. Minor hygiene, harvested as a single low-effort CF (§V.8).

---

## V. Carry-Forward Computations

**Every entry has all four fields. These convert the capstone's named-but-unexecuted open questions in my domain into runnable gates.**

```
V.1. PBCS / variation-after-projection correction to the relic charge ⟨Q⟩_GGE
   - What: Recompute the relic pair charge with full particle-number projection
     (variation-after-projection PBCS) on the 8-mode post-fold BdG Hamiltonian,
     replacing the BCS-projection 59.8 with the VAP value. Quantify the residual
     after removing the known 60% mean-field gap overestimate (B4) and the 225×
     Richardson–Gaudin condensation-energy overestimate (S63). Output:
     Q_VAP, Q_VAP/Q_BCS ratio, and the corrected E_exc/|E_cond|.
   - Inputs: 8-mode BdG matrix (4 B2 + 1 B1 + 3 B3) from s53_q_theory_gge; Delta_BCS
     = 0.4642547 (canonical, R-protected); tau_fold = 0.190; the N_pair=1 exact-ED
     reference E_ED = 1.43984169 (s53_hfb_spectral); the PBCS overestimate factor (S46).
   - Gate: new gate GGE-VAP-CHARGE — PASS if Q_VAP reproduces P_exc=1 regime-robustly
     (i.e. |Q_VAP − Q_BCS|/Q_BCS within the documented 60% PBCS band) AND the corrected
     charge does not alter the N_Fock=1 reduction; FAIL if VAP collapses P_exc below 0.99;
     INFO if VAP shifts the charge outside the band but P_exc stays saturated.
   - Effort: 3-4 hours, 1 agent session (8×8 projected diagonalization, no new spectrum).

V.2. Bayes factor between the surviving spectral functionals (√x vs ζ) for n_s
   - What: Compute the marginal likelihood (Bayesian evidence) of each surviving
     functional in {√x, ζ} against the Planck n_s = 0.9649 ± 0.0042 datum, with the
     anomaly family already structurally excluded (S67). Replace the equal-weight BMA
     band 0.969 ± 0.022 with an evidence-weighted posterior; report the Bayes factor
     B(√x : ζ) and the evidence-weighted n_s band.
   - Inputs: n_s scheme values {0.9561 (anomaly), 0.9590 (ζ), 0.9595 (√x)} from
     FUNCTIONAL-SELECT-67; Planck n_s = 0.9649 ± 0.0042; the prior weights on each
     functional (must be PRE-REGISTERED before evaluating — Paper 06 §III discipline).
   - Gate: new gate NS-BMA-EVIDENCE — PASS if the evidence-weighted band brackets Planck
     within 2σ; INFO if Bayes factor is inconclusive (1/3 < B < 3); the verdict updates
     the §7.1 open-gap on n_s functional selection.
   - Effort: 2-3 hours, 1 agent session (closed-form Gaussian evidence integrals).

V.3. Quantify the Leggett gravitational-decay margin Γ_grav/H_0 as a number
   - What: Evaluate the kinematic decay rate Γ_grav of the single Leggett mode
     (Eq. QA-9: Γ_grav = ε² ω_L³ Δ² /(64π M_Pl⁴) · (ω_L/M_KK)⁴) at the canonical
     parameters and report the dimensionless margin Γ_grav/H_0 explicitly, replacing
     the categorical "CRITICAL" framing with the actual safety factor. Confirm the
     PROVEN kinematic-protection statement (single-Leggett decay FORBIDDEN).
   - Inputs: ω_L1 = 0.138 (canonical), Delta_BCS = 0.4642547, ε = Δ_Leggett/Δ_Josephson
     ~ 0.005–0.011 (S56), M_Pl, H_0 (Planck); LEGGETT-GRAV-DECAY-67 npz (s67_leggett_grav_decay).
   - Gate: feeds the §7.1 framing correction (IV.4) — confirm Γ_grav/H_0 ≪ 1 (gate already
     PASS); the deliverable is the printed margin, not a new verdict. INFO if margin < 10
     (would warrant re-flagging); PASS-confirm if margin ≫ 1.
   - Effort: 1-2 hours, 1 agent session (single rate evaluation + ratio).

V.4. Audited derivation of the effacement projection: bare GGE w = −0.41 → w₀ = −0.918
   - What: Write the explicit substitution chain from the intrinsic GGE equation of state
     w_GGE = P_vac/E_GGE = −0.4076 to the effacement-projected dark-energy w₀ = −0.918,
     through the Volovik partition and the impedance mismatch Γ_eff = 0.99970. Verify
     dimensional consistency and the sign at each step; confirm the projected value is
     w0_FW (canonical).
   - Inputs: P_vac = −0.688, E_GGE = 1.688, N_pair = 1 (s59_q_variable_results); w0_FW
     = −0.918 (canonical, four-fold lock); Γ_eff = 0.99970; the Volovik tracking law E44.
   - Gate: new gate GGE-W-PROJECTION — PASS if the documented chain reproduces w0_FW to
     the published precision AND the sign/direction is verified per math-scripts.md
     substitution-chain discipline; INFO if a normalization (e.g. branch-iv −0.842454)
     is required to close it.
   - Effort: 2 hours, 1 agent session (algebraic chain + Sage cross-check, no new compute).

V.5. Higher-N variational-ordering robustness check (HFB ≤/≥ ED ≤ PBCS)
   - What: Extend the HFB/ED/PBCS energy comparison from N=1,2 to N=3,4 and verify the
     variational ordering is preserved (a violation signals a BdG sign/normalization error).
     Report the odd-even staggering Δ³(N) at each N as the pairing signature; confirm the
     S_2(N) separation energies stay repulsive (S_2 < 0) as the canonical record shows.
   - Inputs: s52_hfb_full_output (E_ED, E_HFB, S_2(N=2..4) = {−0.131, −0.101, −0.094},
     Δ³(N=1,2) = {−0.0657, +0.0506}); the 8-mode (and multi-sector) BdG matrices.
   - Gate: new gate PAIRING-ORDERING-ROBUST — PASS if the variational ordering holds and
     S_2(N) < 0 for all N tested (consistency check on the pairing sign); FAIL if any N
     violates the ordering (would flag a matrix error); INFO if a level crossing reorders.
   - Effort: 3-4 hours, 1 agent session (extends an existing ED/HFB script to higher N).

V.6. Sensitivity of the relic charge to the chemical potential μ (BdG gap-equation closure)
   - What: The BdG quasiparticle energy E_k = √((λ_k²−μ²)² + Δ_k²) carries μ as the
     pairing chemical potential. Solve the self-consistent gap+number equations to fix
     μ and Δ_k at tau_fold, then propagate the uncertainty in μ into the relic charge and
     P_exc. Establishes whether P_exc = 1 is robust to the gap-equation self-consistency
     (currently the relic is computed at a pinned Δ, not a self-consistently closed one).
   - Inputs: the bottom-N D_K eigenvalues λ_k at tau_fold = 0.190 (L_max=10 cache);
     Delta_BCS = 0.4642547; the 1D-DOS van Hove structure g(ω) ∼ 1/√(ω−ω_min) (E13).
   - Gate: new gate BDG-SELFCONSISTENT-MU — PASS if the self-consistent μ leaves P_exc
     ≥ 0.99 (relic-saturation robust to gap-equation closure); INFO if μ shifts the
     condensation energy but not P_exc; FAIL if self-consistency drives P_exc below
     the diabatic-saturation regime.
   - Effort: 4-5 hours, 1 agent session (gap + number self-consistency loop, GPU eig).

V.7. Pin R_therm and the Leggett DM mass to canonical_constants.py with provenance
   - What: Promote R_therm = 5251.82 (S95 W5) from a computed local to a canonical
     constant with PROVENANCE (it is the headline GGE-survival certificate, C2 RESOLVED),
     and add Mass_LeggettDM = 11.97 × Delta_BCS as a derived canonical with its C11
     anchor. Carry the verdict-SHA in both PROVENANCE entries.
   - Inputs: S95 W5 verdict file (R_therm, t_therm, t_transit); C11 anchor
     Mass_LeggettDM/Δ_BCS = 11.97; Delta_BCS = 0.4642547 (canonical).
   - Gate: constants-hygiene CF (write-order verdict → canonical_constants → provenance);
     PASS = both entries present with PROVENANCE + verdict-SHA, values bit-unchanged.
   - Effort: 1 hour, 1 agent session (update_constant calls + provenance, no compute).

V.8. Number-fluctuation ⟨ΔN²⟩ as the BCS-vs-projection discriminator for the relic
   - What: The relic's particle-number fluctuation ⟨ΔN²⟩ distinguishes a genuine BCS
     condensate (broken U(1), large ⟨ΔN²⟩) from a number-projected state (restored U(1),
     suppressed ⟨ΔN²⟩). Compute ⟨ΔN²⟩_HFB vs ⟨ΔN²⟩_ED for the relic at N_pair=1 and
     compare to the canonical s61 values (N=1: 3.208 HFB / 3.034 ED). Establishes whether
     the relic should be read as a condensate (the §5.3 default) or a number-projected
     Fock state (the N_Fock=1 statement) — these carry different superselection structure
     for the dark-matter superselection-protection claim (σ/m = 0).
   - Inputs: s61_proj_a2_log (⟨ΔN²⟩_HFB/N, ⟨ΔN²⟩_ED/N at N=1,2,3); the N_Fock=1 reduction
     (S74); the DM superselection-protection statement (N_pair conserved, no annihilation).
   - Gate: new gate RELIC-NUMBER-FLUCTUATION — INFO-class structural: reports whether the
     relic's ⟨ΔN²⟩ is condensate-like or projected, and whether the σ/m = 0 superselection
     claim requires the projected (N_Fock=1) reading or survives the condensate reading.
   - Effort: 2-3 hours, 1 agent session (fluctuation moments on existing ED/HFB states).
```

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | GGE relic frozen pure product state (`P_exc=1`, `S_ent=0`, `R_therm=5252`) | PHONONIC | SOLID (S95 W5, C2 RESOLVED) | Diabatic freeze, not integrability — correctly retreated; survival compute-certified |
| 2 | `N_pair=59.8` is a projected charge `⟨Q⟩_GGE`, not a pair count | PHONONIC | SOLID | 60% PBCS + 225× R-G overestimates correctly carried; regime-robust claim is `P_exc=1` |
| 3 | Block-decoupling `D_K = ⊕D_{(p,q)}` ↔ j-channel; relic factorizes exactly | GEOMETRIC | SOLID | Per-mode parametric-oscillator is identity, not approximation |
| 4 | FI/RD partition ↔ BMA over unknown EDF | methodological | SOLID (epistemics); PRELIMINARY (model weights) | BMA band correct object; Bayes factors uncomputed (V.2) |
| 5 | Wronskian `W ∝ R_K′³` ↔ Strutinsky decomposition | GEOMETRIC | SOLID (CERTIFIED S75 W2-E) | Recorded as concurrence, not evidence — correct discipline |
| 6 | Equilibrium CC `ρ_Λ=0` exact by Gibbs–Duhem (Clause A) | PHONONIC | SOLID (EQUILIBRIUM-CC-WARRANT PASS) | Thermodynamic not topological (³He-B, `N₃=0`); correctly scoped |
| 7 | Observed CC = off-equilibrium residual `P_vac=−0.688` (Clause B) | PHONONIC | SOLID; doubly conditional (C10 + external H) | `1.032` is PASS given external `H(t)`, not from-`D_K` derivation |
| 8 | Leggett-DM conditional narrated as live threat | PARTICLE/PHONONIC | FRAMING CONFLICT | Gate LEGGETT-GRAV-DECAY-67 = PASS; resolve narrative (IV.4, V.3) |
| 9 | Intrinsic GGE `w=−0.41` vs quoted `w₀=−0.918` | PHONONIC | GAP (not error) | Projection chain undocumented (IV.5, V.4) |
| 10 | HFB ≤ ED ≤ PBCS variational ordering | PHONONIC | UNEXPLOITED check | Free consistency test on BdG matrix sign (IV.2, V.5) |
| 11 | `R_therm`, `Mass_LeggettDM` cited but unpinned | constants-hygiene | MINOR | Promote to canonical with provenance (IV.6, V.7) |
