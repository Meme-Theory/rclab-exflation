# Fresh-Eyes Review — Emergent-Gravity Axis (GR Coherence)

> **Reviewer**: einstein-theorist (general-relativity / emergent-spacetime axis). Did NOT build any section.
> **Scope**: the single cross-cutting axis the builders could not self-check — does the emergent-gravity story hold up as general relativity?
> **Method**: substrate-first (IS-not-IN); GR is the *emergent* consequence of `a₂`, never the explanatory primary. Knowledge MCP queried first; every numeric carries its provenance. Sage-verified where load-bearing.
> **Verdict in one line**: The emergent-gravity story is **GR-coherent as stated**, with NO physics errors. Two presentational gaps in §8.3 (the M_Pl² dictionary self-consistency arithmetic) and one underclaim in §0.3/§7 (the equivalence-principle/Lorentz status is *asserted by inheritance*, not flagged as the open structural item it is) should be patched. The a(t)-gap framing (§6.3) is **honest, not a dodge** — but it is currently *one inch over the line* into a stronger category-claim than the framework's own ledger licenses, and I give the exact softening below.

---

## Summary of what I checked against canonical sources

| Claim under review | Canonical anchor (MCP) | GR verdict |
|:--|:--|:--|
| "gravity = `a₂` Seeley–DeWitt moment" | `a_2 = (1/12)∫√g R` second SDW moment; `Phi(a_2)=Σ_2` (E59); S86 | **Correct & well-stated** — but "kinematic skeleton" is the right hedge; full EH is NOT recovered (see §1 below) |
| CC dictionary `M_Pl,red²=f₂M_KK²a₂/(24π²)` (§8.3) | `M_Pl_eff² = Λ²·a₂·f₂^R/π²·Z⁻¹` (S83); `1/16πG=f₂Λ²a₂/(48π²)` (S86) | **Composes, but the §8.3 arithmetic does not close as printed** — residual is ~39×, not 67.9×; coefficient fork 24π² vs 48π² unflagged (see §1) |
| Sakharov cross-check `G_N^ind/G_N^obs=2.29` | SAKHAROV-GN-44 (`proven_1458`); C8 ASSUMED; "Ratio 2.29 (0.36 OOM) at Λ=10·M_KK" | **Correct, and correctly labelled CONDITIONAL** — but its *composition* with the dictionary residual is not shown (see §1) |
| emergent metric `g_M ↔ g^{ik}` (Volovik gap-node) | volovik §0.3 pillar 2; Paper 06 | **GR-coherent identification** — but equivalence-principle/Lorentz recovery is *asserted*, status is INFO/MIGRATED (T3-BATCH-S75-EMERGENT-LORENTZ), not PROVEN (see §2) |
| no derived FRW `a(t)`; "category statement" | C1 (not derived), C2 BROKEN-LIVE, T6 BROKEN (FRIED-39 133,200×), FRIEDMANN-FROM-A2-74 FAIL (S74) | **Honest gap, correctly sized** — framing 95% right; one over-reach to trim (see §3) |
| CC = `a₀` moment + Volovik tracking `ρ_vac~M_Pl²H²` | E45 DILUTION-CC-66 PASS `ρ_vac/ρ_obs=1.032`; C10 ASSUMED-PARTIALLY-PROVEN | **GR-coherent AND honest about the C10 dependence** — the H²-assumes-external-FRW circularity is correctly disclosed (see §3) |
| acoustic white-hole causal structure (§6.2) | acoustic-white-hole causal-disconnect PROVEN (S85); S70/S71 | **GR-coherent** (analog-gravity standard); no error (see §4) |

---

## Corrections/additions for the main doc

These are paste-ready. They are ordered by how load-bearing they are to the GR-coherence of the document.

### C-1 (§8.3, load-bearing — the dictionary arithmetic does not close as printed)

**The problem.** §8.3 writes the reduced dictionary `M_Pl,red² = f₂ M_KK² a₂/(24π²)` and then asserts the "67.9× internal inconsistency (S75 §7) is self-consistency-by-construction … absorbed by `f₂` (legitimately O(1–10²))." Two things are unshown, and a reader doing the substitution (as I did) hits a wall:

- With the canonical pins `f₂ = 2.34` (`f_2_default`, S62 Gaussian-cutoff), `M_KK = 7.4287×10¹⁶ GeV`, `a₂^ζ = 2776.165389` (`a_2_FW_zeta`, S88), the dictionary as written returns **M_Pl,red = 3.89×10¹⁷ GeV**, vs the canonical `M_Pl_reduced = 2.435×10¹⁸`. The residual is **M_Pl_red²/M_Pl_pred² = 39.2×**, NOT 67.9×. (Sage-verified this build.)
- The number that closes the dictionary is `f₂ ≈ 91.7` (= 39.2 × 2.34). That IS within the "O(1–10²)" band the doc claims — so the *structural* argument survives — but the doc prints `f₂ = 2.34` implicitly (via `f_2_default`) and the reader cannot reconstruct the closure.
- **The coefficient is a genuine fork.** The doc gives both `1/(16πG_N) = f₂Λ²a₂/(48π²)` (first sentence) and `M_Pl,red² = f₂M_KK²a₂/(24π²)` (second). These are consistent with each other *only* via `1/(16πG)=M_Pl_red²/2` — which holds, good — but the S83 canonical form in the knowledge base is `M_Pl_eff² = Λ²a₂f₂/π² · Z_fold⁻¹` (a `π²`, not `24π²`, with a `Z_fold` normalization absorbing the rest). The three forms (`π²`, `24π²`, `48π²`) give residuals of 1.6×, 39×, 78× respectively. The document silently picks `24π²` without reconciling against the S83 `π²·Z⁻¹` canonical.

**Why this is NOT a GR error.** The Chamseddine–Connes dictionary genuinely IS one equation in two unknowns `(M_KK, f₂)` once `a₂` is pinned. The framework pins `M_KK` independently (S42 Sakharov/zeta route), so the residual is legitimately absorbed by `f₂` as UV-completion data — this is standard in spectral-action phenomenology (CCM 2007 fix the analog by the `f₂` normalization at unification). The claim "self-consistency-by-construction" is *correct*. The defect is purely that the printed arithmetic does not visibly close and the residual magnitude (39× vs the stated 67.9×) and coefficient (24π² vs S83's π²·Z⁻¹) are not reconciled.

**Paste-ready replacement for the §8.3 paragraph after the dictionary:**

> The documented "self-consistency residual" (S75 §7) is *self-consistency-by-construction*, not a contradiction: the dictionary is one equation in two unknowns `(M_KK, f₂)` at fixed `a₂^ζ = 2776.17`. With `M_KK = 7.4287×10¹⁶ GeV` pinned independently by the S42 Sakharov/zeta route, the reduced dictionary `M_Pl,red² = f₂ M_KK² a₂/(24π²)` is closed by `f₂ ≈ 92` — an `O(10²)` cutoff-moment, the same legitimacy class as the `f₂` normalization Chamseddine–Connes fix at unification. (The `f_2_default = 2.34` Gaussian-cutoff pin is a *different scheme's* `f₂`; it is not the value that closes this dictionary, and the two must not be cross-substituted — the residual between them, ≈39×, is the scheme gap, not a physical inconsistency.) **PRELIMINARY / constants-hygiene**: the canonical S83 form of this dictionary is `M_Pl_eff² = M_KK² a₂ f₂^R/π² · Z_fold⁻¹`; the `24π²` form here and the `π²·Z_fold⁻¹` form there differ by the `Z_fold` normalization, which should be pinned in `canonical_constants.py` before either is cited as *the* dictionary.

**And the Sakharov composition sentence (§8.3 last sentence) — make the composition explicit:**

> The two independent `G_N` derivations agree to a factor **2.29 (0.36 OOM) at Λ = 10·M_KK** (SAKHAROV-GN-44, C8 — explicitly CONDITIONAL on the effective 4D UV cutoff, which the framework does not fix; at Λ = M_Pl the ratio is 26.8 / 1.43 OOM). This 2.29 is the cross-channel consistency of the *Sakharov mode-sum* route against the *spectral-action dictionary* route; it is a **0.36-OOM agreement on `G_N`**, a different and weaker statement than the dictionary's own `f₂`-closure (which is exact by construction). The two should not be conflated: the dictionary self-consistency is `O(1)`-by-construction; the Sakharov cross-check is an *independent* 0.36-OOM corroboration that the `a₂` channel really does carry the Newton coupling.

### C-2 (§4.1 / §4.2 / §7 — "Einstein–Hilbert is recovered" should everywhere read "the EH kinematic skeleton")

The document already hedges this correctly in the §4 table ("Einstein–Hilbert — **the gravitational kinematic skeleton**") and in the `Φ(a₂)=Σ₂` row ("kinematic skeleton"). Good. But §0.2, §1.1, and the §0 arrow say flatly "the Einstein–Hilbert term ⇒ the emergent 4D metric `g_M` and Newton's constant," which over-reads. **What `a₂` delivers is the EH *action functional* `∝∫√g R` — the kinematic term whose variation gives `G_{μν}=0` in vacuum.** It does NOT, by itself, deliver:

- the matter stress-energy `T_{μν}` on the RHS of `G_{μν}=8πG T_{μν}` (that is a separate substrate→emergent map, the open `a(t)`/Friedmann loop of §6.3),
- a *dynamical* graviton with the correct two polarizations and the correct Newtonian limit (the framework has `a₂` but no derived linearized-gravity propagator on `g_M`),
- the equivalence principle as a *theorem* (it is inherited from Volovik's universality class, not derived — see §2 of this review).

This is exactly why "kinematic skeleton" is the honest phrase. **Recommendation:** propagate the "kinematic skeleton" hedge to §0.2 and §1.1. Concretely, in §0.2 / §0 arrow change "the Einstein–Hilbert term ⇒ the emergent 4D metric and Newton's constant" to:

> `a₂(τ)` → the Einstein–Hilbert *kinematic term* `∝∫√g R` ⇒ the emergent 4D metric `g_M` and the Newton coupling `G_N`. (The full Einstein equation `G_{μν}=8πG T_{μν}` — the EH skeleton sourced by emergent matter — is the open substrate→FRW loop of §6.3, not a delivered result.)

### C-3 (§7.1 / §7.3 — add the equivalence-principle row as an open structural item, not a silent assumption)

The §7 scorecard and §9 open-frontiers list `a(t)`, `n_s`, `m_H`, `w₀`, CC/C10, SDW convergence, family number — but NOT the equivalence principle / emergent-Lorentz / diffeomorphism status. From a GR standpoint this is the most basic obligation an emergent-metric theory owes, and the framework's own status on it is **INFO / MIGRATED** (gate `T3-BATCH-S75-EMERGENT-LORENTZ: INFO`, `s75_emergent_lorentz.py`), not PROVEN. See §2 of this review for why this is an underclaim, not an overclaim. **Add to §9 open frontiers:**

> **8. Emergent Lorentz invariance / equivalence principle** — the metric `g_M` from `a₂` must reproduce low-energy Lorentz invariance, the equivalence principle, and diffeomorphism covariance. The framework *inherits* these from its Volovik universality class (BDI, gap-node `g^{ik}`), and the three-speed hierarchy (`c_fabric/c_Gold = 229.5`, `proven_1157`) shows the relevant emergent light-cone structure exists — but emergent-Lorentz is registered **INFO** (S75), not a derived theorem. The substrate-IS statement (isotropy of the emergent cone at low energy) is the open structural item underneath the `a(t)` gap.

### C-4 (§8.3 — minor: the Sakharov formula scope)

The Sakharov route in the knowledge base is `1/(16πG_N^Sak) = ½ Σ_{k=1}^{992} d_k ln(Λ²/λ_k²)` (S44, after Volovik Papers 07/30) — a **992-mode** sum, NOT the full 155,984. If §8.3 cites "the E30 Sakharov mode-sum," it should note the truncation (the 0.36-OOM agreement is at `L_max`-truncated 992 modes, Λ=10·M_KK), so the cross-check's truncation-sensitivity is visible alongside the `a₂` truncation caveat already flagged in §8.5. One clause suffices: "(the Sakharov mode-sum is the 992-mode `L_max` truncation; the 2.29 ratio inherits the same truncation caveat as the `a₂` channel, §8.5)."

---

## The a(t)-gap consideration

**This is the heart of the GR review, and I want to be precise, because the document is doing something subtle and mostly getting it right.**

### The framing is honest — it is NOT a dodge

§6.3 does three things that a dodge would not do:

1. It quotes the registry **verbatim and against interest**: C1 "not derived from first principles," C2 "BROKEN-WITH-LIVE-RESEARCH-PATHWAY … the framework's load-bearing gap," T6 BROKEN, and the S74 W1-E Friedmann result as a *structural FAIL*. I confirmed all four against the knowledge base: `FRIEDMANN-FROM-A2-74` reproduces a FAIL verdict in the S74 table; T6/FRIED-39 carries the 133,200× shortfall (155,984-mode spectral action vs 8-mode BCS); C1/C2 statuses are as quoted. A dodge hides the FAIL; this document leads with it and puts it in a box titled "the most important caveat in the document."
2. It explicitly **refuses to promote the two proxies** (`a_eff(τ) = (a₂(τ)/a₂_today)^{1/2}` and the Connes-distance `a(τ)` with `q: −0.97→+0.81`) to `a(t)`, labelling both PROXY. This is the correct call. Both proxies are *relabelings* of a spectral moment, not solutions of any derived Friedmann equation — `a_eff` is a complexity measure by fiat, and the Connes-distance `a(τ)` is a different object on the spectral triple (SCALE-FACTOR-54, not promoted). Promoting either would be the dodge; refusing to is the honesty.
3. It correctly identifies the gap as **the same gap viewed twice**: closing `a(t)` ≡ resolving the `K_pivot` paradox (C2/E31, EFOLD-MAPPING-52) ≡ the `M_KK⁻¹→seconds` normalization. That is the right diagnosis — all three are the single substrate→external-e-fold conversion.

So as a matter of GR bookkeeping: **the framework does not claim a derived Einstein equation, does not claim a derived Friedmann equation, does not claim a derived `a(t)`, and says so in the strongest possible terms.** That is the opposite of a dodge. A theory is entitled to say "I derive the EH kinematic term and I have not yet derived the full sourced Einstein equation" — *provided it does not also claim the consequences that only the full equation would license*. The document is disciplined about this.

### Is "Friedmann is the wrong question" a defensible GR position?

**Partly yes, partly an over-reach that I want trimmed.** Here is the careful version.

**The defensible core (substrate-first, correct).** In an emergent-gravity framework, `H(t)` is not fundamental — it is a *readout* of how the substrate's spectral weight reorganizes. Volovik's program establishes exactly this in the lab: there is no external clock; the "expansion" is the reorganization of the fermionic vacuum. So the statement "`H(t)` is a readout of `τ`, not an external clock" is **GR-coherent and is the correct substrate-first reading**. The framework is right that an FRW `a(t)` is a *container-observer's* construction, not a substrate primitive. This is the same move GR itself makes against Newtonian absolute time — and it is the move Einstein would endorse: the metric is not a stage, it is a dynamical field (here, an emergent one). The category statement is not a cop-out; it is the substrate-first commitment taken seriously.

**The over-reach (one inch over the line).** "Friedmann is the wrong question" is too strong as printed, and here is the GR argument for why. Even granting that the substrate is fundamental and `H(t)` is emergent, **the framework still owes an effective Friedmann map** — and the document's own §6.3(i) admits this ("Closing it requires (i) a derived `S_SA(τ) →` 4D gravitational action yielding a Friedmann equation"). You cannot simultaneously hold:

- (a) "Friedmann is the wrong question — there is no container, so no `a(t)` is owed" [the category statement], and
- (b) "closing the gap requires deriving a Friedmann equation" [§6.3(i), the live-research pathway].

If (a) were the *whole* truth, (b) would be unnecessary — there would be nothing to derive. The reconciliation is that the framework owes a **DERIVED effective Friedmann map** as the substrate→emergent bridge, even though it does *not* owe a *fundamental* `a(t)`. The honest gap is precisely the one the volovik draft (§6.4 backing) states perfectly: *"we have not yet derived the effective 4D Friedmann map that a container-picture observer would use to translate the internal τ-flow into their a(t)."* That is exactly right. The capstone §6.3 paraphrases it well but then slightly hardens it into "Friedmann is the wrong question," which reads as "no Friedmann map is owed" — and that contradicts §6.3(i).

**The empirical-physics teeth.** This is not pedantry. The framework makes `w₀`, `w_a`, `σ₈`, `n_s` predictions (§7) that are *only* interpretable against an expansion history. `w_a = 0` (the "live wager," 3.43σ) is a statement about `dw/da` — it presupposes an `a`. The CC closure `ρ_vac ~ M_Pl²H²` (E45) explicitly feeds an **external FRW H** (caveat C10). So the framework is *already using* an effective Friedmann map (the standard FRW `H` plugged into E46/BBN-tracking) to make every late-time prediction. The honest statement is therefore not "Friedmann is the wrong question" but:

> **The framework borrows the standard FRW `H(t)` as external input for its late-time observables (C10), and owes — but has not yet delivered — a substrate-derivation of that same `H(t)` from `S_SA(τ)`. The fundamental object is the τ-flow; the effective Friedmann map is the open bridge, not a discarded question.**

**Paste-ready softening for the §6.3 "category statement" paragraph** (replace "The honest gap is sharper than 'we haven't derived a(t)': it is *we have not yet derived the effective 4D Friedmann map…*" and the closing line):

> **Why this is a *category statement about the fundamental object*, not a discarded obligation.** The substrate, not `a(t)`, is fundamental: "space does not expand; spectral complexity grows inside each point," and `H(t)` is the *readout* of that reorganization, not an external clock. But the framework does NOT thereby escape owing a Friedmann map — it owes a *derived effective* one. Indeed it already *uses* the standard FRW `H(t)` as external input for every late-time observable (`w₀`, `w_a`, `σ₈`, the CC tracking `ρ_vac~M_Pl²H²` — caveat C10), so the effective Friedmann map is not optional; it is borrowed-pending-derivation. The honest gap is therefore: *the fundamental object is the τ-flow (a derived monotone clock, E7); the framework borrows the container-observer's FRW `H(t)` to read its late-time predictions (C10); and it has not yet derived that effective 4D Friedmann map from `S_SA(τ)` — the same open bridge as the `K_pivot` paradox (C2) and the `M_KK⁻¹→s` normalization.* "Friedmann is the wrong question" is right about the *fundamental* level and wrong about the *effective* level; both must be said.

This keeps the strong, correct substrate-first content while removing the one sentence a GR reader would (correctly) push back on. It also makes §6.3 consistent with its own §6.3(i).

### The CC-as-a₀ + Volovik-tracking, given the assumed external FRW H

**GR verdict: coherent, and the circularity is correctly disclosed — but I want the circularity stated one notch more explicitly.** The chain is:

1. CC = `a₀` moment (zeroth SDW, a *different* moment from gravity `a₂`) — correct, and the Wronskian-independence theorem (§4.2, `W ∝ R_K'(τ)³`, S75 W2-E CERTIFIED) genuinely licenses treating `a₀` as independent of `a₂`. I confirmed the Wronskian factor `R_K'(τ) = e⁻⁴ᵗ(e³ᵗ−1)²` ⇒ `W ∝ e⁻¹²ᵗ(e³ᵗ−1)⁶` (Sage, residual 0). This is the correct GR-side answer to "is the CC just a piece of gravity?" — **no, it is a different spectral moment**, and that is exactly why Λ does not gravitate the way the container picture fears.
2. Equilibrium `ρ_vac = 0` by thermodynamics (Volovik q-theory) — GR-coherent; this is the Weinberg-no-go-evading move (a different spectral moment, not a tuned counterterm), and it is the substrate-first dissolution of the 120-OOM catastrophe. Correct.
3. Observed `ρ_vac ~ M_Pl²H²` tracking — **this is where the external FRW H enters**, and the document (via C10) correctly flags it as ASSUMED-PARTIALLY-PROVEN. 

**The honest point to sharpen:** step 3 *assumes* the very FRW `H` that §6.3 says is not derived. So the CC closure (`ρ_vac/ρ_obs = 1.032`, E45, PASS) is **doubly conditional**: on C10 (the `M_Pl²H²` scaling ansatz) AND on the existence of the external FRW `H` it feeds (the `a(t)` gap, §6.3). The document states C10 but does not connect it back to the `a(t)` gap — yet they are the same dependency. **Paste-ready addition to the §7.1 "Substrate readings" paragraph** (after the `Γ_eff=0.99970` sentence):

> Note the CC closure is *doubly conditional*: on C10 (the `ρ_vac ~ M_Pl²H²` tracking ansatz, ASSUMED-PARTIALLY-PROVEN) **and** on the external FRW `H` that the tracking law feeds — i.e. on the same undelivered effective-Friedmann map as the `a(t)` gap (§6.3). The `1.032` residual is a genuine PASS *given* an external `H(t)`; it is not yet a from-`D_K` derivation of the dark-energy density, because `H(t)` itself is borrowed, not derived.

This is not a weakening of the result — `1.032` from zero free parameters *given* the tracking law is real Bayesian evidence (and the document is right to say so against "case unchanged"). It is a precise statement of *what* the result is conditional on, which is the GR reviewer's job.

---

## Error flags

**No GR errors.** The emergent-gravity story is GR-coherent as stated. Specifically, I checked and clear:

- **The `a₂`-as-gravity identification is correct.** Gravity as the second SDW moment is the standard Chamseddine–Connes result; the framework's `a₂ = (4π)⁻ᵈ/²·(20R/3)·Vol` (spectral-geometer §4.5) with `R_K(τ)` monotone is internally consistent, and the `a₂^bos/a₂^Dirac = 61/20` split (E36) is a real representation-theoretic identity. The "gravity is not a fundamental law, it is the second spectral moment" thesis is the correct substrate-first inversion and I endorse it without reservation. It is the single cleanest statement in the document.
- **The white-hole causal structure (§6.2) is GR-coherent.** Acoustic/analog horizons (sonic horizons where flow exceeds the emergent sound speed) are the standard Unruh/Visser analog-gravity construction; the framework's two-horizon (`a₂`-entry / `a₄`-exit) asymmetry with a supersonic interior is a legitimate analog white hole, and "subsonic→supersonic→subsonic" causally disconnecting pre/post-fold is the correct acoustic-causality reading of the horizon problem (PROVEN at S85, acoustic-white-hole causal-disconnect). The kinematic framing (horizons "painted onto a spectrally rigid background by the modulus velocity exceeding the sound speed — a sonic boom, not an equation-of-state transition," S71) is exactly the right distinction and is GR-correct. The PRELIMINARY label on the specific six-stratum enumeration is appropriately placed.
- **The equivalence principle is not violated** — it is *inherited* (from the gap-node universality class) rather than derived, which is an **underclaim risk, not an error**. The document does not falsely claim to derive it; it simply does not list it as the open item it is. (Patched by C-3 above.) Note the GR subtlety the document handles correctly: an emergent metric from a *single* gap structure (one `g^{ik}`) automatically gives all low-energy excitations the *same* light cone — which IS the (weak) equivalence principle at leading order. So the inheritance is physically warranted; it is the *isotropy/Lorentz at higher order* (and diffeomorphism covariance of the emergent action) that remains INFO (S75), not the leading-order universality of free fall.
- **The dictionary `1/(16πG)=M_Pl_red²/2` algebra is internally consistent** (the `48π²` and `24π²` forms agree via this identity). The arithmetic that does not close (C-1) is a *value/coefficient* reconciliation gap (which `f₂`, which `π²`-coefficient), not a structural GR error — the dictionary's form is correct; only its numerical closure is unshown.
- **`w_a = 0` as a structural prediction is GR-legitimate** (a cosmological-constant-like `a₀` term has `w=−1, w_a=0` identically; the framework's `w₀=−0.918` departure is the effacement residual). No error; this is the correct EoS structure for a tracking-vacuum `a₀` moment.

**One non-GR hygiene item I am obligated to surface** (already flagged by the volovik/transit drafts, repeating so the orchestrator does not lose it): `M_KK = 7.4287×10¹⁶ GeV` and `w0_FW = −0.918` carry values but **no PROVENANCE entry** in the knowledge MCP (confirmed: `get_constant("M_KK")` → "No PROVENANCE entry"). Since `M_KK` is the pin that closes the dictionary (C-1) and sets the `M_KK⁻¹→s` normalization (the `a(t)` gap, §6.3), its missing provenance is load-bearing for two of the GR-axis claims. Route to the constants-hygiene pass; do not block; do not invent a source. (The §"Verification ledger" already flags this — good; just confirming it is correctly placed.)

---

## Bottom line for the orchestrator

The emergent-gravity axis is the document's **strongest** axis: "gravity is the `a₂` moment" is correct, well-stated, and the right substrate-first inversion. The a(t)-gap is handled with genuine honesty — it leads with the FAIL, refuses to promote the proxies, and correctly diagnoses the gap as the single substrate→e-fold bridge. 

Four patches, none of which weaken a result:
1. **C-1** — fix the §8.3 dictionary arithmetic so it visibly closes (residual is 39×→`f₂≈92`, not 67.9×; flag the `24π²` vs S83 `π²·Z_fold⁻¹` coefficient fork). *Load-bearing.*
2. **C-2** — propagate the "kinematic skeleton" hedge to §0.2/§1.1 (the EH *term* is recovered, not the full sourced Einstein equation). *Load-bearing.*
3. **§6.3 softening** — trim "Friedmann is the wrong question" to "right about the fundamental level, wrong about the effective level"; the framework owes a *derived effective* Friedmann map (and already borrows the external FRW `H` for every late-time observable). *Makes §6.3 self-consistent with its own §6.3(i).*
4. **C-3 / §7.1 CC double-conditionality** — add the equivalence-principle/Lorentz row to the open frontiers (it is INFO, not PROVEN), and connect the CC's C10 dependence to the `a(t)` gap (same external-`H` dependency). *Honesty, not weakening.*

With these, the emergent-gravity story is fully GR-coherent and the honesty calibration is exact.
