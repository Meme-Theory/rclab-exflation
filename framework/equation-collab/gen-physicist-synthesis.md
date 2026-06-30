# Capstone Equation Review — gen-physicist

> **Reviewer**: Workhorse-Gen-Physicist (cross-domain rigor / assembly-consistency axis).
> **Source under review**: `sessions/framework/phonic-exflation-equation.md` — "The Phonon-Exflation Equation" (S95-era capstone).
> **Vantage**: I authored the build-draft `Collabs/equation-build/gen-physicist-assembly-consistency.md` that is the capstone's §8 source. This review is therefore *not* fresh-eyes on §8; it is an owner's re-audit of how §8 landed in the capstone, plus a cross-domain pass on the dimensional/algebraic spine of §1, §4, §8, and the open-gate inventory of §9.
> **Disclosure of non-independence**: because I own the §8 draft, my §8 verdicts are self-citations. I have re-verified the two load-bearing pieces (Wronskian factorization, f₂ dictionary closure) by *independent* Sage compute at review time (logged in §II) so the §8 verdicts rest on a re-run, not on my prior word.
> **Verdicts cited from the source are authoritative** (task rule); I cross-checked numbers via knowledge MCP + `canonical_constants.py` + Sage, and flag conflicts without overturning recorded verdicts.

---

## §I — Executive Assessment

The capstone is a **disciplined, honest, dimensionally-closed** synthesis. Its central claim — *the universe is the spectral action `S[D_K(τ), f, Λ]` of one Dirac operator on Jensen-deformed `SU(3)`, and the 60 Atlas equations are spectral read-offs of it* — is, from the assembly-consistency vantage, **legitimate at exactly the strength the document claims and no more**. The substrate→emergent arrow (`D_K eigenvalues → a_n moments → emergent physics → measurement`) is held without a single inversion I could find across 563 lines; §0, §6.3, and the §7.1 CC box are model statements of the framing law under maximal container-relapse pressure.

What is **solid** (and I independently re-verified the arithmetic of the two that are mine to verify):
- **Dimensional closure** (§8.1): `[S] = mass⁰`, every layer term `f_{d−2k}Λ^{d−2k}a_{2k}` individually mass-dim 0, the `L⁻¹²` "spurious tower" correctly identified as a double-counting error. This is correct and is the firewall against the most common reader error.
- **The Spectral-Moment Decoupling Theorem** (§4.2): `W[a₀,a₂,a₄] = 2·R_K′(τ)³ = 2·e⁻¹²ᵗ(e³ᵗ−1)⁶`, vanishing to 6th order at and only at `τ=0`. I re-derived this from the E3 curvature at review time: residual exactly 0, proportionality constant exactly 2 (correctly absorbed into the capstone's "∝"). This theorem is the **single most load-bearing structural result in the document** — it is what licenses multiplying the `a₀×a₂×a₄`-layer probabilities in §7.3 and what defeats the "one knob dressed three ways" objection. It is Sage-certified and it holds.
- **The `a_n` convention firewall** (§8.2): the Gilkey-zeta triple `(6440, 2776.165389, 1350.7216)` vs the raw mode-count triple `(155984, 64308, 29086)` are different functionals, not rival measurements. The capstone displays the right one (`a_n^ζ`) and quarantines the raw triple to the `A_s`/fiber-variance discussion. This was the conflation I flagged as "the single most likely numerical error a reader will make"; the capstone implemented the firewall.
- **The f₂ dictionary closure** (§8.3): `f₂ ≈ 92`, **not** the old "67.9× inconsistency." This is an einstein-review patch that *replaced* my draft's "self-consistency-by-construction / 67.9×" framing — and it is a strict improvement. I re-verified: the reduced (`24π²`) and unreduced (`3π`) forms both give f₂ = 91.67–91.70; the 67.892× is correctly re-identified as the artifact of *absorbing* `f₂ = 1/16π`. The patch is arithmetically sound and sharpens honesty (it states a positive number, not a "residual").

What is **PRELIMINARY / conditional** and correctly labeled as such:
- **Absolute-energy observables** (CC magnitude, `A_s`) are conditional on an SDW-convergence statement (`JACOBSON-NONLOCAL-64`, OPEN — confirmed open in MCP). **Ratio-observables** (`n_s`, `g₁/g₂`, `61/20`, `R₁`, `a₂/a₀`) are truncation-robust. The capstone's §8.5 / §9-frontier-#6 statement of this split is exactly my draft's "Consideration" and is the correct boundary.
- **The `a(t)` / FRW gap** (§6.3) — no derived scale factor. The capstone states this "without softening" and correctly fuses it with frontier #8 (emergent EP). This is the honest center of gravity of the whole document.

What I judge **mildly over-claimed or under-pinned** (none fatal; all flagged in §III):
1. `t* = 0.08832` is called "the framework's single empirical coupling" but has **no canonical pin** (`t_star` ABSENT from `canonical_constants.py`). A load-bearing free parameter that is not in the constants ledger is a hygiene gap.
2. The §9-frontier-#8 promotion language is **genericity-qualified correctly**, but the qualification is dense; a reader may still over-read `κ_EP = 1` as a substrate *prediction* rather than a generic-identity consequence of the single-operator postulate.
3. The §8.3 dictionary itself carries an *internal* PRELIMINARY (the `24π²` vs S83 `π²·Z_fold⁻¹` form differ by the `Z_fold` normalization, "should be pinned before either is cited as *the* dictionary"). The capstone displays `f₂≈92` from the `24π²` form while flagging the `Z_fold` form is unpinned — a live, named, unresolved fork inside the headline derived-scale relation.

No claim in the document contradicts my own memory or the registry in a way I could not reconcile. The one numerical micro-conflict I found (R₁ exact-rational vs canonical-float, 7th digit) is sub-ppm hygiene, flagged in §III.

---

## §II — Independent Verification Log (review-time Sage compute)

Two pieces are mine to verify and I re-ran them rather than self-cite. Backend: Sage MCP (`sagecell`), exact-rational where the threshold is tight.

**(1) Wronskian / Spectral-Moment Decoupling (§4.2, §4.4, capstone verification ledger).**
From the E3 curvature `R_K(τ) = −¼e⁻⁴ᵗ + 2e⁻ᵗ − ¼ + ½e²ᵗ`:

| Check | Capstone claim | Sage result | Verdict |
|:--|:--|:--|:--|
| `R_K(0)` | 2 | `2` | ✓ |
| `R_K′(0)` | 0 | `0` | ✓ |
| `R_K(0.19)` | 2.018 | `2.01814` | ✓ |
| `R_K′(τ)` factored | `e⁻⁴ᵗ(e³ᵗ−1)²` | residual `= 0` | ✓ |
| `W[1, R_K, R_K²] / (R_K′)³` | constant (∝) | `= 2` (exact) | ✓ |

The proportionality constant is exactly **2**, correctly hidden inside the capstone's `W ∝ R_K′³`. The 6th-order zero at `τ=0` is `(e³ᵗ−1)⁶`. **CONFIRMED** — the algebraic-independence theorem stands on its own Sage-certified proof, independent of any agent's say-so.

**(2) f₂ dictionary closure (§8.3, einstein-review patch).**

| Form | Formula | Sage result | Verdict |
|:--|:--|:--|:--|
| reduced | `f₂ = M_Pl,red²·24π²/(M_KK²·a₂)` | `91.6732` | ✓ ≈92 |
| unreduced | `f₂ = M_Pl,unred²·3π/(M_KK²·a₂)` | `91.6991` | ✓ ≈92 |
| S75 "inconsistency" | `M_Pl,unred / [√(a₂/48π²)·M_KK]` | `67.892×` | ✓ = the 67.9× artifact (f₂=1/16π absorbed) |

`M_Pl_eff (f₂ absorbed) = 1.79830×10¹⁷ GeV`, reproducing the S75 number. The capstone's `f₂ ≈ 92` headline is **arithmetically correct**; the "67.9×" is correctly demoted to "the value at `f₂ = 1/16π`," i.e. a scheme artifact, not an inconsistency. **CONFIRMED.**

**(3) Canonical-constant provenance cross-check (MCP `get_constant` + `canonical_constants.py`):**
- `a_0_FW_zeta = 6440.0` (S88), `a_2_FW_zeta = 2776.165389` (S88), `a_4_FW_zeta = 1350.7216` (S75 source, now pinned) — all match capstone §8.2 table.
- `M_KK_gravity = 7.428660036284456×10¹⁶` (S42, CONST-FREEZE-42) — matches.
- `Lizzi_signature = 1.1286545967627695` (S74, canonical) — matches `R₁` headline.
- `f_2_default = 2.34` (Gaussian-cutoff pin) — the capstone correctly states this is NOT the f₂≈92 that closes the dictionary.
- **`t_star` = ABSENT; `Mach_transit` = ABSENT** from `canonical_constants.py` (`c_fabric = 209.97` IS pinned, matching §5.2). Flagged in §III.

**(4) Open-gate confirmation (MCP):** `JACOBSON-NONLOCAL-64` SDW-convergence is OPEN (confirmed); `DILUTION-CC-66` is PROVEN at the *ratio* `ρ_vac/ρ_obs = 1.032` — consistent with the capstone's "ratio closed, absolute open" split.

---

## §III — Conflicts, Gaps, and Unstated Assumptions

### III.1 — `t*` is a load-bearing free parameter with no canonical pin (HYGIENE → §V CF-1)
The capstone's free-parameter ledger is `{τ, Λ, f₀, f₂, f₄} + t*` (§1.4, §8.4). The `+ t*` is *the* thing that distinguishes the framework from a zero-empirical-input theory; §1.4 even closes the "t* is the one-loop threshold coefficient" corridor (S95 W2-1 FAIL, `R = 1.977`). Yet `t_star` is **not in `canonical_constants.py`**. A free parameter the document leans on this hard should be pinned with provenance (its value `0.08832`, the FAIL that de-empiricized-it-is-impossible, the `f*(x) = 0.9117√x + 0.0883e⁻ˣ` source). This is the math-scripts.md canonical-write-order applied to a parameter, not a prediction. Not a physics error; a ledger gap.

### III.2 — The dictionary's own internal fork is unresolved (`Z_fold`) (CONFLICT → §V CF-2)
§8.3 displays `M_Pl,red² = f₂ M_KK² a₂/(24π²)` and reports `f₂ ≈ 92`, but the same paragraph flags: *"the canonical S83 form is `M_Pl_eff² = M_KK² a₂ f₂^R/π² · Z_fold⁻¹`; this `24π²` form and the S83 `π²·Z_fold⁻¹` form differ by the `Z_fold` normalization, which should be pinned before either is cited as the dictionary."* So the headline derived-scale relation has **two coexisting forms differing by an unpinned `Z_fold` factor**, and the document cites one while admitting the other is canonical-at-S83. This is a genuine internal tension the capstone surfaces but does not close. The f₂≈92 number is robust *within* the `24π²` form (I verified it), but "which form is THE dictionary" is open. Flag, do not resolve (task rule).

### III.3 — R₁ exact-rational vs canonical-float: 7th-digit micro-conflict (HYGIENE → §V CF-3)
The Lizzi registry gives `R₁ = 42022400000000000/37232339454500103`, which Sage evaluates to `1.1286532`. The canonical pin `Lizzi_signature = 1.1286545967627695`. These agree to 6 sig figs but **differ in the 7th** (`...532` vs `...546`, ~1.2 ppm). The capstone prints `1.12865` (5 sig figs), so the headline is unaffected — but the two "exact" sources disagree below display precision. Either the registry rational or the canonical float is stale. Sub-ppm; pure provenance hygiene. (Per Class-8.3 publication-precision: if R₁ is ever cited downstream at >6 sig figs, this fork bites.)

### III.4 — "One generation" vs the product-KO mismatch: stated honestly, but the reader's load is high
§1.3 item 4 is the most intellectually demanding passage in the document. It (correctly) states the product triple `M⁴×SU(3)×F_SM` carries a **permanent KO mismatch** (product KO=4 vs finite KO=6), that the bosonic action is unaffected, and that the fermionic sector requires the Pfaffian/`H_K⁺` restriction — then frames the mismatch as doing *constructive* work (the level-matching analogy). I judge this **solid physics, honestly stated**, but it is the place a hostile referee will push hardest, because "the single-operator statement on `K` is exact (6/7 order-one axioms hold on the lift)" is a *bounded caveat* dressed as a strength. The capstone does not hide it — it is in the "what it does NOT claim" list — but the §V harvest below includes a concrete computation to *quantify* the 7th-axiom defect rather than leave it prose-bounded.

### III.5 — The `a(t)` gap: category-statement framing is right, but "borrows H(t)" is the actual liability
§6.3 is excellent and I have no correction to its honesty. One sharpening for the record: the dagger-rows in §7.1 (`w₀`, `wₐ`, `σ₈`, CC) are evaluated *using the container-observer's FRW `H(t)` as external input* (C10). So the document's strongest data-facing predictions (the DESI-DR3 `wₐ=0` wager, the CC closure `1.032`) are **doubly conditional**: on the spectral *value* from `D_K` (solid) AND on an `H(t)` the framework does not derive (the same undelivered effective-Friedmann map). The capstone says this in the §7.1 CC caveat box and the §7.1 dagger note — but it is worth stating in the executive frame that *the cliff-edge falsifier (DESI DR3) tests a prediction that is itself riding on a borrowed `H(t)`*. This does not weaken the falsifiability (a `wₐ` measurement still kills or spares the four-fold lock); it means a FAIL could be attributed to the borrowed `H(t)` rather than to `D_K`. The §V harvest converts the back-reaction-closure into runnable form.

### III.6 — No contradiction found between §5.3 (Ordered Veil) and the S39 retraction
I checked the one place my memory flagged a possible tension (the `project_phononic-equation-next-actions` note about "§5.3 vs the PROVEN-line, adjudicate"). The capstone **resolves it cleanly and correctly**: the surviving claim is "diabatic transit-freeze, NOT integrability permanence" (`R_therm = 5251.82 ≫ 1`, `S_ent = 0`, both S95 W5), with the S39 13% non-separable channel explicitly demoted to "irrelevant on the transit timescale." The triple-leg (diabatic + pure-product + extremal-horizon `T_H=0`) over-determination is honest. No flag — this is a model of how to retire a retracted sub-claim without losing the result.

---

## §IV — Substrate-Framing Audit (phononic-framing.md compliance)

I read the document specifically for container-relapse, since §6 is flagged as "the top container-relapse risk." Findings:

- **Direction of explanation**: held throughout. The single arrow is stated once (§0) and never inverted. Gravity is the `a₂` moment (not a law imposed); the CC is the `a₀` moment; space is "what the `a₂` moment looks like." ✓
- **Exflation vs inflation**: the capstone uses substrate vocabulary correctly — "spectral complexity grows inside each point," "supersonic transit through the van Hove fold," "GGE relic" for reheating, "effacement residual + tracking vacuum" for dark energy. No "space expands" leakage. ✓
- **The IS-not-IN levels**: §2.4 (genesis) and the moduli-deformation language are Level-1/Level-2 clean. The `τ`-flow is "the substrate's intrinsic deformation parameter," not "the substrate moving through a τ-container." ✓
- **The one place the framing law is *load-bearing for a result*, not just narrative**: §8.1's `[a_{2k}] = mass^{2k−d}` is the substrate-Gilkey reading; the capstone correctly notes that a reader who *also* writes `Λ^{d−2k}` while keeping dimension on `a_{2k}` produces the spurious `L⁻¹²` tower. This is the framing law (substrate IS the spectral data; the `Λ`-power is the regulator's, not the substrate's) doing arithmetic work. The capstone gets it right.
- **Verdict**: framing-compliant. The substrate→emergent direction is the document's spine, not a coat of paint.

---

## §V — Carry-Forward Computations (the open-question harvest)

Per the user's "ripe harvest" instruction, every open question I can convert is below with all four fields. These feed the next compute session.

### CF-1 — Pin `t*` to the canonical constants ledger (HYGIENE, fast)
- **What**: Add `t_star = 0.08832` to `canonical_constants.py` with a PROVENANCE entry, and register it in the knowledge MCP via `update_constant`. Provenance must record: the value, the `f*(x) = 0.9117√x + 0.0883e⁻ˣ` working-functional source, and the S95 W2-1 FAIL (`R = 1.977`) that closes the "t* is the one-loop threshold coefficient" corridor (so the ledger documents *why* t* is irreducibly empirical, not derivable).
- **Inputs**: `phonic-exflation-equation.md` §1.4 + §3.2; S95 W2-1 verdict line; `canonical_constants.py` SECTION for couplings.
- **Gate**: PASS iff `from canonical_constants import t_star` returns `0.08832` AND `mcp__knowledge__.get_constant("t_star")` returns the value with the W2-1-FAIL provenance note. (Artifact-existence gate, no numerical threshold — this is a hygiene write, not a physics gate.)
- **Effort**: ~15 min, single `update_constant` call + import test. Fix-in-session class.

### CF-2 — Resolve the `Z_fold` dictionary fork (`24π²` vs S83 `π²·Z_fold⁻¹`)
- **What**: Compute `Z_fold` from first principles (the fold-normalization factor relating the two displayed forms of the Planck dictionary), then verify algebraically that `M_Pl,red² = f₂ M_KK² a₂/(24π²)` and `M_Pl_eff² = M_KK² a₂ f₂^R/π² · Z_fold⁻¹` are the SAME equation once `Z_fold` is substituted. Determine which is the canonical display form and pin `Z_fold`.
- **Inputs**: `phonic-exflation-equation.md` §8.3; S83 dictionary source (`M_Pl_eff² = M_KK² a₂ f₂^R/π² · Z_fold⁻¹`); `a_2_FW_zeta`, `M_KK`, `M_Pl_reduced` canonicals; Sage `sage_eval` for the algebraic-equivalence check.
- **Gate**: PASS iff `|f₂(24π² form) − f₂(Z_fold form after Z_fold substitution)| / f₂ < 1e-6` (the two forms reconcile to publication precision) AND `Z_fold` is pinned to `canonical_constants.py`. FAIL iff the two forms differ by more than a pure `Z_fold` rescaling (would indicate a genuine factor error in one form).
- **Effort**: ~1 session-wave. Symbolic + one canonical pin. Depends on locating the S83 `Z_fold` definition.

### CF-3 — Reconcile R₁ exact-rational vs canonical-float (sub-ppm hygiene)
- **What**: Recompute `R₁ = a₀a₄/a₂²` from the canonical zeta triple at full float64 AND as a Sage exact rational; determine whether the registry rational `42022400000000000/37232339454500103` (→ 1.1286532) or the canonical `Lizzi_signature = 1.1286545967627695` is correct, and re-pin the stale one.
- **Inputs**: `a_0_FW_zeta = 6440`, `a_2_FW_zeta = 2776.165389`, `a_4_FW_zeta = 1350.7216`; `lizzi-signature-observable.md` registry rational; `canonical_constants.py:Lizzi_signature`; Sage QQ.
- **Gate**: PASS iff the two sources agree to `< 1e-7` after recompute, OR the stale source is identified and re-pinned so they agree to float64. (Class-8.3 publication-precision: R₁ is a headline FI ratio; its 7th digit should not depend on which "exact" source you read.)
- **Effort**: ~20 min. Pure recompute + one re-pin.

### CF-4 — Pin `Mach_transit = 13.75` and the conflation-guard companion `421.3`
- **What**: Add the canonical transit Mach `13.75` (velocity ratio `v_transit/c_fabric`) to `canonical_constants.py`, alongside the distinct fold-local acoustic-radius ratio `421.3` and the B2-channel fold Mach `293.79` (§6.2), each tagged with its KIND so the "never averaged" conflation-guard (§5.2) is enforced at the constants layer, not just in prose.
- **Inputs**: `phonic-exflation-equation.md` §5.2 + §6.2; `c_fabric = 209.97` (already pinned); the three Mach readings.
- **Gate**: PASS iff all three are pinned with distinct KIND tags AND a docstring cross-reference forbidding their arithmetic combination. (Artifact-existence + provenance gate.)
- **Effort**: ~20 min. Hygiene write closing a known conflation hazard.

### CF-5 — Quantify the 7th-order-one-axiom defect under the product-KO mismatch
- **What**: The capstone (§1.3 item 4) states "6/7 order-one axioms hold on the lift" and bounds the product-KO mismatch as a caveat on the 4D *interpretation*. Compute the explicit numerical magnitude of the single failing order-one axiom's defect on `M⁴×SU(3)×F_SM` — i.e., the residual of the order-one condition `[[D, a], JbJ⁻¹] = 0` (or the specific axiom that fails) on the product lift, as a function of `τ`, so the "bounded caveat" becomes a *number* rather than prose. Confirm it is `τ`-independent (a structural defect, not a dynamical one) and that it leaves the Pfaffian/`H_K⁺` fermionic measure well-defined (the gates T3-S30A/T3-S35 claim).
- **Inputs**: the product triple data (`A_K = ℂ⊕ℍ⊕M₃(ℂ)`, `H_K = L²(S_gτ)⊗ℂ¹⁶`, `D_K(τ)`); the 7 order-one axioms; `dirac_spectrum` block decomposition; the Pfaffian construction. GPU torch.linalg for the order-one commutator on the truncated spectrum.
- **Gate**: PASS iff the failing axiom's defect norm is (i) nonzero (confirming the mismatch is real, not an artifact), (ii) `τ`-independent to `< 1e-10` across `τ ∈ [0, τ_now]` (confirming it is structural), AND (iii) the Pfaffian `Pf(A_D)` remains real with `Z₂ = +1` (confirming the fermionic measure survives). This converts "a known, bounded caveat" into a pinned structural number.
- **Effort**: ~1–2 session-waves. The order-one commutator on the product lift is the new compute; the Pfaffian reality is a re-confirmation of existing gates.

### CF-6 — The back-reaction closure `H² = f(ρ_relic, S_SA)` (frontier #1 = #8, the load-bearing gap)
- **What**: This is the single most important open item (§6.3, §9-frontier-#1). Attempt the *minimal* version: derive an effective Friedmann-like relation by promoting the produced GGE relic energy density `ρ_relic` (from the §5.3 Bogoliubov spectrum, `N_pair`, `E_exc`) into a source for an emergent expansion rate `H`, using the `a₂`-channel emergent metric `g_M` and an emergent Bianchi identity `∇_μ G_eff^{μν} = 0`. Test whether the S95 W3-1 conservation-closed `G_eff^{μν}` (`noether_ratio = ½`, on-shell `∇_μ G_eff = 0`) can be *lifted from the internal `K` geometry to the emergent `g_M`* — the capstone says EIH holds on `K` and is "owed" on `g_M`.
- **Inputs**: S95 W3-1 (`G_eff^{μν}` conservation, internal `K`); S95 W3-5 (`κ_EP = 1`); the §5.3 relic spectrum (`ρ_relic`); `S_SA(τ) = a₀ − a₂ + a₄`; the `a₂` emergent-metric dictionary (§8.3, pending CF-2's `Z_fold`); the T6-FAIL diagnostic (the 155,984-mode vs 8-mode BCS overwhelm, 133,200×).
- **Gate**: This is a *structural-existence* gate, not a number-match. PASS iff a generally-covariant 4D effective action `S_eff[g_M]` is constructed whose variation yields `G_eff^{μν} = 8πG_eff T_relic^{μν}` with `∇_μ T_relic^{μν} = 0` emergent (not postulated), AND the resulting `H²` is non-trivial (does not collapse to the near-flat `a_eff(τ)` proxy that gives diverging `q_Ω`). INFO if a partial closure is achieved on the Connes-distance proxy `a(τ)` only (the §6.3 SCALE-FACTOR-54 route with `q: −0.97 → +0.81`). FAIL if the 133,200× overwhelm structurally forbids any closure (would harden the T6-FAIL into a no-go).
- **Effort**: Multi-session frontier. This is the document's flagship open problem; it will not close in one wave. Recommend decomposing into: (6a) lift the Bianchi identity `K → g_M`; (6b) construct `S_eff[g_M]` from `S_SA(τ)`; (6c) the `M_KK⁻¹ →` seconds normalization. The capstone explicitly notes (6a)+(6b)+(6c) "are one bridge" and closing it closes frontiers #1 AND #8 jointly.

### CF-7 — The NNLO Casimir EP discriminator (frontier #8, the genuine substrate prediction)
- **What**: The capstone (§9-frontier-#8) states `κ_EP = 1` at LO+NLO is a *generic identity* (the Lichnerowicz `R/4` coefficient of ANY spin Dirac operator), value-generic, NOT a substrate prediction. A genuine substrate EP *prediction* first appears at **NNLO**, where the band-specific `ν_b(C₂)` Casimir content re-enters the `κ_EP` ratio. Compute `κ_EP` at NNLO for two distinct Peter-Weyl bands (B1 acoustic vs B3 optical) and extract the predicted deviation `κ_EP^NNLO − 1`, which IS substrate-specific (it carries `C₂(b)` of the two eigenspaces).
- **Inputs**: the band-resolved D_K spectrum (B1/B3 sectors, Casimir `C₂(p,q)`); the NNLO Seeley-DeWitt structure (the `a₆` curvature polynomial where `ν_b` re-enters); `dirac_spectrum.get_irrep`; GPU for the band traces. (Note the math-scripts.md Casimir-bound feasibility pre-check for any `L_max ≥ 10` scan.)
- **Gate**: pre-register the gate-ID `CF-S96-EP-NNLO-CASIMIR-DISCRIMINATOR` (the capstone already names it). PASS iff `κ_EP^NNLO − 1` is computed as a nonzero substrate-specific number that *differs between B1 and B3* (confirming it is value-content, not a generic identity), with the sign and magnitude pinned. This is the first place the framework makes a *prediction* about the equivalence principle that a generic emergent-gravity model would not share.
- **Effort**: ~2 session-waves. The NNLO band traces are the new compute; the generic-identity baseline (LO+NLO `κ_EP=1`) is already certified (S95 W3-5).

### CF-8 — `n_s` functional selection (frontier #2): close or bound the BMA band from first principles
- **What**: The red tilt is correct *if* `f = √x`, but which spectral functional generates the physical tilt is unsolved (Window-7 / FUNCTIONAL-SELECT-67, E31 CONDITIONAL). The three rival points are `n_s ∈ {0.9561, 0.9590, 0.9595}` at `2.10σ/1.40σ/1.29σ`; the BMA band `n_s = 0.969 ± 0.022` marginalizes over `f`. Attempt a first-principles *selection* criterion for `f` from the substrate (e.g., does the acoustic-envelope `f(ω²) ∼ |ω|` of §3.2 follow from the BdG dispersion of the post-fold spectrum, fixing `√x` non-arbitrarily?), OR tighten the BMA band by computing the functional-prior from the dimension-spectrum convergence-cone constraint (§3.3, `S_d = {0,2,4,6,8}` restricts admissible `f`).
- **Inputs**: §3.2 + §3.3; the FI/RD partition; the S67 BMA computation; the post-fold BdG dispersion (§5.3 substrate-BdG `u_k`); the convergence-cone pole ladder.
- **Gate**: INFO/PASS — PASS iff a substrate criterion *uniquely* selects `f = √x` (the acoustic envelope is forced by the BdG dispersion, not chosen), collapsing the three-point spread to one prediction. INFO iff the convergence-cone constraint tightens the BMA band below `±0.022` without uniquely selecting `f`. FAIL-as-boundary iff the functional remains genuinely free (confirms `n_s` is irreducibly RD-class, which is itself a clean constraint-map result).
- **Effort**: ~1–2 session-waves. The acoustic-envelope-from-BdG-dispersion derivation is the high-value new compute.

### CF-9 — Pin the Pauli-Villars and Mellin scheme companions of the `a_n^ζ` triple (regulator-pin completion)
- **What**: My §8 draft R3 flagged that only the *zeta-scheme* `a_n^ζ` triple is pinned. The Pauli-Villars and Mellin scheme companions (`a_n^{Pauli-Villars}`, `a_n^{Mellin}`) are the S88 carry-forward and not yet pinned. Compute all three coefficients under PV and Mellin regularization and pin them, so the regulator-pin discipline (`regulator-pin-discipline.md`) is satisfiable for any future gate that cites `a_n` under a non-zeta scheme. This also lets the FI/RD partition be tested *across* regulators (the capstone's "ratios under a *fixed* regulator are physical" — but cross-regulator ratio stability is the stronger FI statement).
- **Inputs**: the D_K spectrum cache (`L_max=10/12`); the PV subtraction with mass-scale running at `Λ_UV = M_KK`; the Mellin-cone evaluator (`analytic_zeta`); `regulator-pin-discipline.md` tag format `a_n^{Pauli-Villars}`, `a_n^{Mellin}`.
- **Gate**: PASS iff all three coefficients are computed under PV and Mellin and pinned to `canonical_constants.py` with regulator tags, AND the *ratio* `a₂/a₀` agrees across {ζ, PV, Mellin} to within the FI-class drift bound (≤5% per the Lizzi FI criterion). FAIL-as-boundary iff `a₂/a₀` drifts >5% across regulators (would demote `a₂/a₀` from FI to RD — a significant constraint-map update).
- **Effort**: ~2 session-waves. PV subtraction + Mellin evaluation are the new compute; the cross-regulator FI test is the high-value output.

### CF-10 — SDW convergence (`JACOBSON-NONLOCAL-64`): bound the absolute `a₀`-moment vs `L_max`
- **What**: The deepest open gate underneath the CC-absolute and `A_s`-absolute (§8.5, §9-frontier-#6). The raw spectral sums *diverge* with `L_max`; only ratios are demonstrably stable. Compute the Gilkey-normalized `a₀^SDW`, `a₂^SDW` at increasing `L_max` (the Casimir-bound / Friedrich-Bär feasibility pre-check governs how high) and test whether the *normalized* SDW coefficients (not the raw sums) converge to a finite curvature integral, or whether the `a₀`-dominated expansion is genuinely non-convergent (which would make the CC-absolute and `A_s`-absolute permanently conditional, not just currently-open).
- **Inputs**: D_K spectrum at `L_max ∈ {8,10,12}` (the cache ceiling); the Gilkey-normalization `a₀^SDW = (4π)⁻⁴ Vol(K)`, `a₂^SDW = (4π)⁻⁴·⅙∫R_K√g`; the Friedrich-Bär saturation theorem (`math-scripts.md` D_K block-diagonality pre-check); `cc-path-a.md §IV.1`.
- **Gate**: PASS iff `a₂^SDW(L_max)` converges (`|a₂^SDW(12) − a₂^SDW(10)| / a₂^SDW(10) < ε_conv` for a pre-registered `ε_conv`, e.g. 1%), licensing promotion of the absolute `a₂`-moment. INFO iff the *ratio* `a₂/a₀` converges but the absolutes do not (the current understood state — confirms ratio-robust / absolute-conditional). FAIL-as-boundary iff the normalized SDW coefficients themselves diverge (hardens JACOBSON-NONLOCAL-64 into a structural no-go for absolute-energy observables). This is the gate that decides whether "the framework located the CC term" can ever become "the framework computed the CC magnitude."
- **Effort**: Multi-session frontier; the `L_max=12` Gilkey-normalized recompute is feasible (largest block ~9792-dim, 1.53 GB, fits VRAM per `math-scripts.md`), but the convergence-statement itself is the hard analytic question. Recommend the empirical `L_max`-scan first (feasible now), then the analytic Friedrich-Bär saturation argument.

---

## §VI — Closing Constraint-Map Position

The capstone occupies the **sole surviving region** of its own constraint surface honestly: every strong claim lives on the topological/representation-theoretic side that survives the continuum-dissolution (`T3-S43-SPECTRAL-DISSOLUTION`), and every honest gap lives on the geometric-magnitude side that does not. The §9 "geometry vs topology" organizing spine is the deepest available defense and it is correctly drawn.

From the assembly vantage, the document is **dimensionally closed, algebraically self-consistent in its ratio-observables, and explicitly conditional in its absolute-energy observables** — which is exactly what §8 certifies and exactly what an honest "one equation for the universe" claim is entitled to assert. The two centerpiece pieces I re-verified at review time (the `W = 2R_K′³` decoupling Wronskian and the `f₂ ≈ 92` dictionary closure) hold under independent Sage compute.

The harvest is real and large. The ten carry-forwards above are not "further work needed" prose; each is runnable. The load-bearing three are **CF-6** (the back-reaction closure = frontiers #1+#8, the document's flagship gap), **CF-10** (SDW convergence, the gate underneath every absolute-energy observable), and **CF-7** (the NNLO Casimir EP discriminator, the first place the framework makes an EP *prediction* a generic emergent-gravity model would not share). The four hygiene items (CF-1 `t*` pin, CF-2 `Z_fold` fork, CF-3 R₁ micro-conflict, CF-4 Mach pins) are fix-in-session class and should clear before the capstone is cited downstream as canonical.

**What is solid**: the dimensional skeleton, the decoupling theorem, the convention firewall, the f₂ closure, the framing-law compliance. **What is PRELIMINARY**: every absolute-energy magnitude (CC, `A_s`), the `Z_fold` dictionary form, the `n_s` functional. **What is over-claimed**: nothing fatally — but `t*`-as-"single empirical coupling" needs a pin, and the §9-#8 EP promotion needs its genericity qualifier read carefully (which the capstone, to its credit, supplies). **What conflicts**: the `Z_fold` dictionary fork (internal, surfaced-not-closed) and the R₁ 7th-digit (sub-ppm hygiene) — flagged, not resolved.

The equation IS the universe in the precise sense the document calibrates: all field content, couplings, and dynamics are spectral functionals of one operator. It is NOT a closed self-selecting theory — and the document says so without softening. That honesty is the reason the claim survives review.

---

*Artifacts verified on disk at review time*: this synthesis at `sessions/framework/equation-collab/gen-physicist-synthesis.md`. Cross-check Sage logs and MCP constant-provenance queries are in-conversation (not written to separate files per the no-report-file discipline). Source read in full (563 lines); §8 build-draft (`Collabs/equation-build/gen-physicist-assembly-consistency.md`, 273 lines) re-read as my own prior authorship.
