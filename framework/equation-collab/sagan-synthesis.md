# Capstone Equation Review — sagan

**Date**: 2026-05-29
**Agent**: sagan-empiricist (Sagan)
**Source Documents**:
- `sessions/framework/phonic-exflation-equation.md` ("The Phonon-Exflation Equation", S95-era capstone)
- `.claude/rules/phononic-framing.md` (framing law — binding)
- Cross-checks: `computations/_shared/canonical_constants.py`, knowledge MCP (`a_4_FW_zeta`, `w0_FW`, `tau_fold`, FUNCTIONAL-SELECT-67, LEGGETT-GRAV-DECAY-67, S93-W7-1, S95-W2-1, S95-W5-3)

---

## I. Session Outcome

The capstone is the most honest large-claim document I have audited in 95 sessions, and I say that as the agent whose standing job is to disbelieve large claims. It does the two things that almost never co-occur: it states a categorical claim ("the universe is the spectral action of one Dirac operator") **and** it prints, without softening, the four places the claim is not yet earned (the `a(t)`/Friedmann gap, the `n_s` functional selection, the `m_H` route, the CC observed-magnitude conditionality). The empirical conscience's verdict is therefore split cleanly: the **structural / representation-theoretic spine is strong and largely zero-parameter** (KO-dim=6, SM quantum numbers, CPT, block-diagonality, the Wronskian layer-independence theorem, the BDI/`N₃=0` class), while the **dimensionful-observable spine is a set of viable-but-conditional brackets** (`w₀`, `n_s`, `m_H`, `σ₈`, `Ω_DM`, CC magnitude), every one of which leans on at least one undelivered object — most often the borrowed FRW `H(t)` (caveat C10) that the document itself flags as its load-bearing gap.

My one structural complaint is the same one I have raised before and the document has now largely pre-empted: the §7.3 "scorecard" correctly refuses an aggregate PASS/FAIL ratio and correctly forbids multiplying same-layer observables (`Ω_DM` and `σ₈` are both `a₂`). That discipline is exactly right. But the joint-evidence argument grounded on the Decoupling Theorem (§4.2) is doing more rhetorical work than the math licenses, because the cross-layer "independent improbabilities" being multiplied are mostly brackets on **already-measured** observables evaluated through a **borrowed** expansion history, not blind zero-parameter predictions of unmeasured quantities. The genuine zero-parameter, falsifiable, not-yet-measured predictions — the ones that would actually move a Bayesian — are the LISA CGWB acoustic class, the S43 first-sound BAO ring, the `wₐ=0` four-fold lock against DESI DR3, and the CF-35 ³He-B cocycle ratio. Those, not the brackets, are the harvest.

---

## II. Key Results

### II.1 The free-parameter ledger is the single most important honest statement in the document

**Result**: Inputs are `{τ, Λ=M_KK, f₀, f₂, f₄} + t*` — one geometric modulus, UV-completion data (cutoff moments), and exactly one empirical functional coupling. **GEOMETRIC** (the ledger) / **PHONONIC** (`t*` as the spectral-functional analog of `Λ_QCD`).

This is the line on which the entire "extraordinary claims require extraordinary evidence" calculus turns, and §1.4 gets it right. The framework is **not** zero-parameter, and the document says so in bold. What I verified independently: the corridor "`t*` is the one-loop threshold coefficient" is **CLOSED — FAIL** (S95 W2-1, `R = |t*_pred − t*|/t* = 1.977`; confirmed in the MCP). This is a genuine elimination and it matters in *both* directions. It closes the de-empiricization route (you cannot remove `t*` from the ledger by deriving it from the loop term — the loop term is ~3× too large), and it correctly keeps the ledger honest at `{τ, Λ, f₀, f₂, f₄} + t*`. A framework that *had* claimed `t*` was forced and then quietly dropped the claim would have earned a pipeline-reliability penalty; instead the document records the FAIL and keeps the empirical coupling visible. That is the behavior of a falsifiable program.

The deeper point for evidence-weighting: the strength of every downstream "zero adjustable cosmological parameters" claim (§7.3) is *conditioned on this ledger*. A cosmological observable computed at `τ_fold` with `f = √x` carries no cosmological free parameter — true — but it carries `t*` (the admixture that selects `√x` over the excluded schemes is the same `O(1)` datum no first principle has been shown to select), and it carries the borrowed `H(t)`. The honest framing is: *zero free parameters in the cosmological sector, conditional on the spectral-functional choice and the external expansion history.* The document mostly says this; §7.3 should not be read without §1.4 and the C10 caveat in hand.

### II.2 The Wronskian layer-independence theorem is a genuine, certified, falsifiable structural result

**Result**: `W[a₀,a₂,a₄](τ) ∝ R_K′(τ)³ = e^{−12τ}(e^{3τ}−1)⁶`, vanishing to sixth order at and only at `τ=0`, nonzero at `τ_fold`. **GEOMETRIC**.

This is the strongest single argument in §4 and I want to credit it precisely because it is the kind of claim I usually have to deflate. The objection "is `a₄` just a dressed function of `a₀, a₂`, so it's one knob in three costumes?" is a real over-fitting concern, and it is answered not by assertion but by a Sage-certified non-vanishing Wronskian (S75 W2-E CERTIFIED; the document re-verifies the factor in its own ledger, residual `0`). The three spectral moments are algebraically independent functions of the modulus everywhere the universe lives, degenerating only at the maximally-symmetric genesis instant. That is what licenses calling `a₀/a₂/a₄` *distinct physics* (vacuum/gravity/matter) rather than one rescaled quantity.

Where I hold the line: the Wronskian establishes **algebraic independence of the three curvature-polynomial moments as functions of `τ`**. It does **not** by itself establish that the three *observables built on them* are statistically independent measurements in the Bayesian sense the §7.3 joint argument wants. Independence-as-functions-of-`τ` and independence-as-likelihood-factors are different claims. The document is careful enough to forbid multiplying *within* a layer (`Ω_DM × σ₈`), which is the right instinct, but the cross-layer product still treats the three layers' observational comparisons as cleanly factorizable when they share `Λ=M_KK`, share `t*` (for the regulator-dressed observables), and share the borrowed `H(t)`. The Wronskian is real and impressive; the inference from it to a large joint likelihood ratio across the *cosmological* observables is PRELIMINARY and over-reaches.

### II.3 The CC story is correctly bisected into a warranted half and a conditional half

**Result**: Equilibrium `ρ_vac = 0` **exactly** by Gibbs–Duhem (S95 W5-3 PASS, Sage-rational `0`); observed magnitude `ρ_vac/ρ_obs = 1.032` is the non-equilibrium tracking residual, **doubly conditional** on C10 (`ρ_vac ∼ M_Pl²H²`, ASSUMED-PARTIALLY-PROVEN) AND on the external `H`. **PHONONIC** (effacement residual + Volovik tracking vacuum).

I verified the Gibbs–Duhem `ρ_vac=0` identity is genuine and representative-independent in the MCP (multiple sessions: Volovik Paper 05, S43 QFIELD, S62 #19, S95 W5-3). The §7.1 "CC caveat box" is a model of the distinction I spend most of my time demanding: Clause A (non-inheritance of the 114-OOM term — warranted exactly, by an identity, not a tuned cancellation) vs Clause B (observed magnitude — conditional, off-equilibrium, leaning on C10 and borrowed `H`). The closing sentence — *"The framework has correctly located the cosmological-constant term, not solved the cosmological-constant problem"* (§9 frontier #6) — is the single most calibrated sentence in the document. I would not change a word.

The empirical caveat I add: "DILUTION-CC-66 PASS, `1.032`" is a PASS *of a dimensionless ratio given an external expansion history*. It is **not** a from-`D_K` derivation of the dark-energy density, and the document says so. A reader who lifts "CC closure: PASS (1%)" out of the §7.1 table without the caveat box will mis-state the result by a category. This is the one row most likely to be over-cited downstream, and the firewall is the caveat box, which must travel with the number.

### II.4 The α_s "12σ tension" is resolved as a channel artifact — and this supersedes my own stale memory

**Result**: Two scale-separated `α_s` observables — substrate-distance running `−0.08587279` (s=3 Mellin pole, FI-class, frozen) vs Goldstone-pivot running `≈0`. Transport degree `deg(T_{BZ→pivot}) = +2` (non-scalar) decides which a detector sees. On the matched channel the pivot image sits at **+0.67σ — consistent** (S93 W7-1 PASS). **GEOMETRIC** (transport-degree) / **PHONONIC** (Goldstone-pivot protection).

I flag this explicitly per my instructions: my own agent memory (S65/S69) records `α_s` as a "5.8σ contradiction" between Bogoliubov `α_s≈0` and `dn_s/dlnk=−0.039`. That memory is **stale**. The MCP confirms S93 W7-1 resolved the apparent `−12σ` tension structurally as a scale-and-channel conflation, with `deg(T_{BZ→pivot})=+2` *computed, not chosen* — and crucially, the resolution was achieved by the same pre-registration discipline that excludes the anomaly family (decided by the transport-degree computation, not by which answer matched). I accept the recorded verdict and update my own ledger: this is no longer a contradiction; it is a resolved channel artifact with a `+0.67σ` pivot consistency *and* a `~34σ-reach` CMB-S4/CMB-HD falsifier of the substrate-distance value (`−0.0859`). That is the right shape: a present consistency plus a future decisive test. The honest residual is that the substrate value `−0.0859` is **frozen and cannot drift to meet CMB-S4** — so if CMB-S4 measures the substrate-distance running near zero, this is a clean falsification. Good.

### II.5 The two-scalar exhaustion is a verified algebraic rigidity, not a counting argument

**Result**: `dim HH¹(A_K,A_K) = dim HH²(A_K,A_K) = 0` (S95 W2-2 PASS, exact rational rank count + Whitehead). Every derivation of `A_K` is inner; every first-order deformation reduces to an inner fluctuation. **GEOMETRIC**.

This is the load-bearing support for the §1.1 claim "there is no room for a third term — which is why the equation is complete." I credit it: the "trace + inner product exhaust the natural scalars" argument would be hand-waving if it rested on intuition, but the vanishing Hochschild cohomology makes the interaction structure *forced by the algebra*. This is a genuine structural advantage over a string field theory that must *select* its vertex from inequivalent options, and the document's comparison to the matrix-model/IKKT genre is fair. The claim is GEOMETRIC and PROVEN; I have no deflation to offer.

### II.6 The honest gap (§6.3) is correctly identified as a *category statement about the fundamental object*, not a discarded obligation — but it is the gap that conditions half the data table

**Result**: No substrate-derived FRW `a(t)`; C1 (modulus→scale-factor) POSTULATED; C2 (`K_pivot`) BROKEN-WITH-LIVE-PATHWAY; T6 (Friedmann-BCS locking) BROKEN (133,200× overwhelm); S74 W1-E Friedmann a *structural* FAIL. **NON-PHONONIC gap** (the missing object is a derived emergent-`g_M` 4D action).

§6.3 is the central honesty of the document and it is handled exactly as the Jacobson (1995) reading demands: a substrate theory is *expected* not to contain a fundamental Friedmann equation (the Einstein/Friedmann equations are equations of state of the emergent metric). But — and the document says this in bold, which I commend — "Friedmann is the wrong question" is right about the *fundamental* level and **wrong** about the *effective* level. The framework still owes a *derived effective* Friedmann map, and it already *borrows* the container-observer's `H(t)` for every late-time observable carrying a `†` in the §7.1 table (`w₀`, `wₐ`, `σ₈`, the CC tracking). 

This is the empirical crux I want to surface loudly: **every dagger-marked row in §7.1 is conditional on the same undelivered object.** `w₀ = −0.918`, `wₐ = 0`, `σ₈ = 0.799`, and `CC closure = 1.032` are spectral *values* from `D_K`, but their *cosmological evaluation* runs through a borrowed `H(t)`. That does not make them wrong — but it does mean the "zero adjustable cosmological parameters" headline is precise only if one reads "given an external expansion history" alongside it. The framework has not yet earned the right to say its cosmology is parameter-free *and* self-contained; it is parameter-free *conditional on* a piece it borrows. The document is honest about this; a careless downstream citation would not be.

### II.7 The Ordered Veil survival is now certified by compute, independent of the retracted integrability

**Result**: GGE relic survives by **diabatic transit-freeze**, not integrability permanence: `R_therm = t_therm/t_transit = 5251.82 ≫ 1` (S95 W5) AND `S_ent = 0` exact (S95 W5), both independent of the S39-retracted Richardson–Gaudin integrability (Brody β=0.633, 13% non-separable channel). Third leg: `τ_fold` is a double-root extremal Killing horizon (`κ=0, T_H=0`). **PHONONIC**.

I credit the document for the cleanest handling of a retraction I have seen in the corpus. The S39 integrability claim was *weakened* (13% non-separable channel), and a lesser document would have either buried the retraction or let the GGE permanence claim quietly inherit the broken support. Instead §5.3 explicitly re-grounds the survival on *diabaticity* (a transit-timescale statement, `R_therm ≫ 1`) plus *purity* (`S_ent=0`), both compute-certified and both independent of the broken Claim B, plus a *geometric* third leg (zero Hawking temperature). This is over-determination done right. The information-theoretic framing (no Page curve because nothing thermalizes; Bogoliubov phase retained in conserved charges) is a legitimate and attractive consequence, classified correctly as a consequence, not a separate result.

The one number I want quarantined exactly as the document quarantines it: `N_pair = 59.8` is a **projected charge `⟨Q⟩_GGE`, NOT a literal pair count** — it inherits a ~60% PBCS gap overestimate (S46) and a ~225× Richardson–Gaudin condensation-energy overestimate (S63). The regime-robust claim is `P_exc = 1`. The footnote in §5.3 says this; the §7.1 `σ/m` row and §9 both correctly carry `⟨Q⟩_GGE=59.8` with the `N_Fock=1` reduction. Good hygiene. A `59.8` cited as a pair count would be a 60%-to-225× error.

---

## III. Gate Verdicts

These are AUTHORITATIVE (cited from the source / MCP); I do not re-adjudicate. Listed for the record with the decisive number.

| Gate / Result | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| KO-dimension 6 mod 8 (E9) | PROVEN | `<10⁻¹⁵`, 10 checks; AZ class BDI |
| CPT commutant `[J,D_K]=0` (E8) | PROVEN | 79,968 pairs, machine-ε; `η=0` |
| Block-diagonality (E6) | PROVEN | `8.4×10⁻¹⁵`, 3 proofs |
| Structural Monotonicity (E7) | PROVEN | `dS/dτ\|_fold = +58,672.8`; 9,600/9,600 |
| Spectral-Moment Decoupling (S75 W2-E) | CERTIFIED | `W ∝ R_K′(τ)³`, residual `0` |
| Two-scalar exhaustion (S95 W2-2) | PASS | `HH¹=HH²=0`, exact rational |
| One-loop no-interior-saddle (S95 W2-3) | PASS | `dΓ/dτ` zero interior sign-changes, 3 routes |
| `t*` = one-loop coefficient corridor (S95 W2-1) | **FAIL (CLOSED)** | `R=1.977`; `t*` stays empirical |
| Equilibrium CC warrant (S95 W5-3) | PASS | `ρ_vac=0` exact, Gibbs–Duhem |
| α_s channel-artifact (S93 W7-1) | PASS | `deg(T)=+2`; pivot +0.67σ; substrate `−0.08587279` |
| DILUTION-CC-66 | PASS | `ρ_vac/ρ_obs = 1.032` (conditional, C10) |
| Ω_DM h² Leggett-only | PASS (0.7σ) | `0.120` (CONDITIONAL on LEGGETT-GRAV-DECAY-67) |
| r (BICEP/Keck) | PASS (within 2σ) | `0.033` (Path-H 0.00745 / Path-C 0.0117) |
| f_NL | PASS (0.47σ) | `−1.505`, Bogoliubov-Gaussian |
| σ/m (Bullet) | PASS (structural) | `0` exact, `N_Fock=1` |
| 12D cosmic censorship (S95 W4-5) | PASS | anisotropic `τ→∞` singularity censored |
| **n_s functional selection (FUNCTIONAL-SELECT-67)** | **OPEN (CONDITIONAL)** | `n_s∈{0.9561,0.9590,0.9595}`; ~22 sessions deferred |
| **C2 / K_pivot** | **BROKEN-WITH-LIVE-PATHWAY** | load-bearing gap |
| **T6 Friedmann–BCS locking** | **BROKEN** | 133,200× overwhelm |
| **wₐ four-fold lock** | **LIVE (3.43σ)** | `0` vs `−0.72±0.21` |

---

## IV. Structural Implications

**The framework now partitions cleanly along the continuum-dissolution axis, and §9's "organizing spine" is the deepest defense available.** The finite spectral triple is GEOMETRY and dissolves in the continuum limit (T3-S43-SPECTRAL-DISSOLUTION, `ε_c ∼ N^{−0.457}`). The topological/representation-theoretic outputs *survive* dissolution (GGE purity, BDI/`N₃=0` class, CF-35 cocycle, CPT, layer independence, FI ratios); the absolute geometric magnitudes are *conditional* (CC magnitude, `a_n` absolutes, `a(t)`). This is the right answer to "if the triple dissolves, why trust its outputs?" — and it has a sharp empirical reading: **the falsifiable, durable predictions live on the surviving (topological) side; the conditional brackets live on the dissolving (geometric-magnitude) side.** Every strong claim is on the surviving side; every honest gap on the dissolving side. This is structurally consistent, and I see no internal contradiction in it.

**The constraint map has tightened, not loosened, over 95 sessions.** From my domain: closures STRENGTHEN survivors. The `t*` corridor closing (FAIL), the 27 equilibrium-closure attempts failing (S17–S40, HESS-40 all-positive Hessian), the anomaly-family exclusion (S67), ZETA-NOT-PHYSICAL (S75), the off-Jensen Schur permanence — these are eliminated mechanisms that narrow the surviving solution space to a structurally specific region (a monotone-ramp transit physics with a diabatic GGE relic on a BDI substrate). The document does not cite a "constraint count" as an argument — correctly — and reports each closure as a boundary. This is exactly the epistemic discipline I would enforce.

**Two conflicts/tensions I flag explicitly (not silently resolving):**

1. **Joint-evidence over-reach (§7.3 vs §4.2).** The Wronskian licenses cross-layer *algebraic* independence of `a₀/a₂/a₄`; it does not license multiplying the *cosmological-observable comparisons* as independent likelihood factors, because those comparisons share `Λ`, share `t*` (regulator-dressed observables), and share the borrowed `H(t)`. The document's within-layer prohibition (`Ω_DM × σ₈`) is right; the cross-layer product is PRELIMINARY. **Flagged, not resolved** — this is an evidence-weighting judgment, not a recorded verdict, and it falls in my domain as sole probability estimator.

2. **My stale memory vs the document (α_s).** My S65/S69 memory records a 5.8σ spectral-running contradiction; the document and MCP record S93 W7-1 resolving it as a channel artifact. **I defer to the recorded verdict** and have noted my memory is stale (II.4). This is a memory-update obligation on me, not a conflict in the document.

**Probability assessment (my domain contribution, not a re-adjudication of any gate).** Per my methodology, structural zero-parameter geometric predictions carry full BF (no postdiction discount): the ~10 exact SM-matching structural results (KO-dim=6, SM quantum numbers, CPT, BDI, block-diagonality, etc.) plus the Wronskian and exhaustion theorems are a strong joint structural prior — these are not in dispute and the document cites them correctly. The *dimensionful-observable* sector is where the brackets on known observables (wide brackets, borrowed `H(t)`) attract my 0.6× accommodation discount, and where the open gates (FUNCTIONAL-SELECT-67, C2, T6) cap the prerequisite-gate BF at 1.5–2.0. Net: the capstone does not move my framework probability from its S69 neutral band by itself — it is a *synthesis* of existing verdicts, not a new pre-registered gate — but it sharpens the *shape* of the surviving region considerably and it correctly identifies the four near-term gates (DESI DR3, LISA, CMB-S4, LiteBIRD) that *will* move it. **No probability movement without a pre-registered gate; the capstone is commentary on the constraint map, and excellent commentary, but it is not itself a gate.**

---

## V. Carry-Forward Computations

**The user's "ripe harvest" instruction lands here.** Each open question in the document is converted to a runnable computation with all four fields. These are the calculations that would actually move a Bayesian — every one targets a falsifiable, mostly zero-parameter prediction or closes a conditional.

### V.1 — Close FUNCTIONAL-SELECT-67: does any spectral functional family uniquely select the physical n_s?
- **What**: Resolve the `n_s` scheme-dependence. Scan a *physically-motivated* functional family (acoustic `√x`-class, with the `t*` admixture as the one free parameter) and test whether the FI/RD partition + a substrate-first selection principle uniquely fixes `f`, collapsing `n_s ∈ {0.9561, 0.9590, 0.9595}` to a single value. Output: `n_s_selected ± band`, the selecting functional, and whether the BMA band `0.969±0.022` collapses.
- **Inputs**: `s66_cutoff_ns.npz`, `s67_functional_select.npz`, `s72_spectral_functional_fit.npz`; `canonical_constants.py` (`t*=0.08832`, `tau_fold=0.19`, `n_s` candidate pins); the S67 ANOMALY-FAMILY-EXCLUSION and S75 ZETA-NOT-PHYSICAL theorems as boundary constraints.
- **Gate**: FUNCTIONAL-SELECT-67 (Window-7). PASS: a unique `f` with `n_s ∈ [0.9550, 0.9700]` AND `m_H ∈ [122,130] GeV`; FAIL: no family yields the bracket / scheme-dependence persists; INFO: a family selects but only at `>2σ` from Planck.
- **Effort**: 4–6 hours, 1 agent session (deferred ~22 sessions; the decisive E31 gate is CONDITIONAL — this is the highest-leverage open compute in the document).

### V.2 — Derive the effective Friedmann map: close C1/C2/T6 jointly (frontier #1 = #8)
- **What**: Construct the derived, generally-covariant emergent 4D action for `g_M` from the `a₂` Seeley–DeWitt moment, i.e. the back-reaction closure `H² = f(ρ_relic, S_SA)` that promotes the produced relic energy density into a source for the global expansion rate. Output: an effective Friedmann equation `H²(τ)` derived from `S_SA(τ)`, the `M_KK⁻¹ →` seconds normalization, and a resolution of the `K_pivot` paradox.
- **Inputs**: `S_SA(τ) = a₀−a₂+a₄` profile (S58/S75 spectral-action data); the S44 internal-`K` Bianchi identity (EIH on `K`); the 12D metric lift (S95 W4-5); the Connes-distance proxy `a(τ)` (SCALE-FACTOR-54) and conformal embedding `Ω(τ)` (S95 W4-4 INFO); `a₂^ζ=2776.165`, `M_KK=7.4287×10¹⁶ GeV`.
- **Gate**: NEW — `EFFECTIVE-FRIEDMANN-CLOSURE` (closes C1+C2+T6+frontier-#8 jointly). PASS: a substrate-derived `H²(τ)` reproducing the SCALE-FACTOR-54 deceleration band (`q: −0.97 → +0.81`) with the `a₂` channel as source AND the lift of internal EIH to emergent `g_M`; FAIL: the 133,200× spectral-vs-BCS overwhelm persists with no closure; INFO: a closure exists only for the Connes-distance proxy, not `a_eff`.
- **Effort**: 2–3 agent sessions (the single most important open item; explicitly the load-bearing gap, §6.3 + §9 frontier #1).

### V.3 — LISA CGWB acoustic-class forecast: pin the SNR and the detection band against LISA-PLS
- **What**: Compute the cosmological gravitational-wave background `Ω_GW(f)` from the first-order van Hove transit (domain-wall / acoustic class) across the LISA band, and the explicit SNR against the LISA Power-Law Sensitivity curve. Output: `Ω_GW(f_LISA)` central value + band, peak frequency, and SNR vs the Companion-null `8.299×10⁻⁵⁸`.
- **Inputs**: `tau_fold=0.19`, `Mach=13.75`, `c_fabric=209.97 M_KK`, `δt_transit=1.130×10⁻³ M_KK⁻¹`, `N_pair`/`P_exc=1` relic spectrum; the S95 W6-2 substrate forecast (INFO-by-unavailability — the substrate side exists; only the comparison value was unavailable). Fetch the current LISA-PLS curve.
- **Gate**: Falsifier #7 (FLAGSHIP). PASS: `Ω_GW` acoustic class ≥ LISA-PLS at SNR threshold (document claims 11 OOM above PLS, SNR ~10¹³); FAIL: `Ω_GW` below LISA reach; INFO: detectable but degenerate with an astrophysical foreground.
- **Effort**: 3–4 hours, 1 agent session (the cleanest yes/no in the document; LCDM has no counterpart).

### V.4 — S43 first-sound BAO ring: amplitude-detection forecast against a named survey
- **What**: Complete the S95 W6-2 INFO-by-unavailability gate — forecast the detectability of the first-sound ring (`A_FS/A_BAO = 0.204 = c_2²/c_1²`, `r_1 ≈ 325 Mpc`, `k_1 ≈ 0.0193 Mpc⁻¹`) against a specific survey's acoustic-scale sensitivity (DESI DR3 / Euclid / SKA). Output: detection significance forecast (σ) for the ring amplitude vs the named survey's `δP/P` floor.
- **Inputs**: `A_FS/A_BAO=0.204`, `r_1≈325 Mpc`, `k_1≈0.0193 Mpc⁻¹`; the per-branch effacement suppression `δP/P≈1.4×10⁻³`; fetch DESI DR3 / Euclid power-spectrum sensitivity.
- **Gate**: NEW — `FIRST-SOUND-RING-FORECAST`. PASS: ring amplitude > survey floor at ≥3σ; FAIL: ring below floor (effacement-suppressed below detectability); INFO: marginal (1–3σ). A zero-parameter prediction with no ΛCDM counterpart.
- **Effort**: 3–4 hours, 1 agent session (resolves the only INFO-by-unavailability falsifier).

### V.5 — Close LEGGETT-GRAV-DECAY-67: is Ω_DM h²=0.120 stable or does the DM sector collapse?
- **What**: Compute the Leggett-mode gravitational decay rate `Γ_grav` and compare to `H_0`. This is CRITICAL: if `Γ_grav > H_0`, the entire `Ω_DM=0.120` PASS is meaningless. Output: `Γ_grav` (with the `m_φ³/M_Pl²` estimate sharpened beyond the S75 `Γ_grav=9.42×10¹⁰ GeV` back-of-envelope) and the `Γ_grav/H_0` ratio.
- **Inputs**: Leggett-channel mass `m_φ = 0.111 M_KK = 8.25×10¹⁵ GeV` (S75); `M_Pl`, `H_0`; the gravitational decay vertex `⟨g,g|H_grav|L⟩`; `Ω_DM h²=0.120`, `Δ_BCS`, `Mass_LeggettDM/Δ_BCS=11.97` (C11/LEGGETT-MOMENT-70).
- **Gate**: LEGGETT-GRAV-DECAY-67 (CRITICAL, 1/5). PASS: `Γ_grav < H_0`; FAIL: `Γ_grav > H_0` (DM sector collapses, `0.120` meaningless). The S75 estimate gives `Γ_grav=9.42×10¹⁰ GeV ≫ H_0` naively — this MUST be resolved (the naive number is alarming and the gate is unclosed).
- **Effort**: 4–6 hours, 1 agent session (a CRITICAL conditional underneath a headline PASS — highest-priority risk audit).

### V.6 — Pin the G_N dictionary normalization: resolve the f₂≈92 vs Z_fold form
- **What**: Resolve the §8.3 PRELIMINARY/constants-hygiene item: the `24π²` dictionary form (`M_Pl,red² = f₂ M_KK² a₂/(24π²)`, closing at `f₂≈92`) vs the canonical S83 form (`M_Pl_eff² = M_KK² a₂ f₂^R/π² · Z_fold⁻¹`) differ by the `Z_fold` normalization. Pin `Z_fold` and certify a single dictionary. Output: the canonical `f₂`, `Z_fold`, and a Sage-verified single dictionary equation.
- **Inputs**: `M_KK=7.4287×10¹⁶ GeV`, `a₂^ζ=2776.165389` (`a_2_FW_zeta`), `M_Pl,red`; the S42 Sakharov/zeta `M_KK` route; the S75 §7 self-consistency residual; `f_2_default=2.34` (Gaussian-cutoff, the DIFFERENT scheme — confirm it is not cross-substituted).
- **Gate**: NEW — `GN-DICTIONARY-NORMALIZATION-PIN`. PASS: a single `(f₂, Z_fold)` closes both forms to machine-ε with `f₂ ∈ O(10²)`; FAIL: the two forms are irreconcilable (a physical inconsistency, not a scheme gap); INFO: reconcilable only under a stated `Z_fold` convention that must itself be derived.
- **Effort**: 2–3 hours, 1 agent session (constants-hygiene; the document flags this explicitly as needing a pin before citation).

### V.7 — Pin R₁ = a₀a₄/a₂² to canonical_constants.py (the one scheme-invariant number on the cover)
- **What**: The Lizzi signature `R₁ = a₀a₄/a₂² ≈ 1.12865` (Sage-verified `1.128655` in the document's ledger) is presented as *the* FI scheme-invariant number, but it is **not in the knowledge MCP** (verified: `get_constant('R1_lizzi')` returns not-found). Promote it with full provenance and certify its truncation-robustness (FI-class). Output: `R1_lizzi` canonical entry + L_max-stability check.
- **Inputs**: `a_0_FW_zeta=6440`, `a_2_FW_zeta=2776.165389`, `a_4_FW_zeta=1350.7216`; the multiplicative-normalization-cancellation invariant; L_max scan of the ratio.
- **Gate**: NEW — `R1-LIZZI-CANONICAL-PIN`. PASS: `R₁=1.128655` reproduced from the three canonical `a_n^ζ` AND L_max-stable to the FI-class tolerance; FAIL: ratio drifts with L_max beyond FI tolerance; INFO: stable but the three `a_n^ζ` need their own re-pin first.
- **Effort**: 1–2 hours, 1 agent session (hygiene; the document's headline scheme-invariant number should be queryable, not only self-reported).

### V.8 — Pre-register the DESI DR3 wₐ=0 four-fold-lock test (the near-term cliff-edge)
- **What**: Pre-register the binding 2D `(w₀, wₐ)` posterior test against DESI DR3 (2026) BEFORE the data lands, so the result counts as a genuine pre-registered prediction (Venus Rule). Output: the `R_842` rectangle in `(w₀, wₐ)` space, the pre-registered PASS/FAIL boundary, and the current 3.43σ marginal tension on `wₐ`.
- **Inputs**: `w0_FW=−0.918` (branch-iv `−0.842454`); `wₐ=0` (four-fold structural lock); the Popovic et al. (DES) joint posterior arXiv:2511.07517v3 (`ρ(w₀,wₐ)≈−0.85`); the `R_842` 2D rectangle definition (Falsifier #1).
- **Gate**: Falsifier #1 (DESI DR3, the cliff-edge). PASS: DESI DR3 `(w₀,wₐ)` 2D posterior overlaps `R_842`; FAIL: the `wₐ=0` lock is excluded at >3σ in the 2D posterior. This MUST be pre-registered now — the binding event is 2026 and `w0_FW` provenance is already pinned (S95 W6-4).
- **Effort**: 2–3 hours, 1 agent session (pre-registration discipline; the document calls this "the most exposed prediction" and "the cliff-edge").

### V.9 — Pin the F1 falsifier: scan for the a₂-carrier scalar-channel squeeze near 72.8 M_KK
- **What**: Resolve the §6.2 "observable-visibility HELD pending" caveat on the `a₂` kinematic-carrier temperature (`72.8 M_KK`). Compute whether a scalar-channel observable squeeze branch exists near `72.8 M_KK` (an OOM above the `a₄` condensate-squeeze support `ω∈[0.82,1.06]`). Both readers predict NULL — confirm it. Output: the scalar-channel spectral density near `72.8 M_KK` and a NULL/non-NULL verdict.
- **Inputs**: the analog-temperature ledger (`a₂`: 72.8 M_KK, κ=457.66; `a₄`: 7.578 M_KK, κ=47.61); the κ-ratio 9.6117; the `a₄` condensate-squeeze support band; the [T3] scalar-tensor decoupling (`β_T=0`).
- **Gate**: NEW — `F1-A2-CARRIER-VISIBILITY`. PASS (= expected NULL): no observable scalar-channel quantum at `72.8 M_KK` (confirms the `a₂` carrier is observationally invisible, licenses the COMPOSITE two-stage emission form); FAIL: a non-NULL branch exists (the categorical "a₂ carries no observed quantum" is then false).
- **Effort**: 3–4 hours, 1 agent session (closes the one HELD-pending caveat in the white-hole causal structure).

### V.10 — CMB-S4 / CMB-HD α_s substrate-distance falsifier pre-registration
- **What**: Pre-register the `~34σ-reach` falsifier of the s=3 Mellin-residue identity `α_s = −0.08587279` at the matched substrate-distance channel against CMB-S4 (2030) → CMB-HD (2035). The substrate value is FROZEN and cannot drift — so this is a clean future falsification. Output: the matched-channel observable, the CMB-S4 sensitivity, and the σ-reach.
- **Inputs**: `α_s_substrate = −0.08587279` (s=3 Mellin pole, FI-class, frozen); `α_s_pivot ≈ 0` (Goldstone); `deg(T_{BZ→pivot})=+2`; fetch CMB-S4 / CMB-HD `α_s` sensitivity forecasts; the S93 W7-1 transport-degree factorization.
- **Gate**: Falsifier #3 (CMB-S4 → CMB-HD). PASS: CMB-S4 measures the substrate-distance running consistent with `−0.0859` at the matched channel; FAIL: CMB-S4 measures near-zero substrate-distance running (falsifies the s=3 Mellin identity). Pre-register now; the value is frozen.
- **Effort**: 2–3 hours, 1 agent session (the α_s resolution leaves a decisive future test that should be pre-registered).

### V.11 — SDW convergence (JACOBSON-NONLOCAL-64): the gate underneath the CC absolute magnitude
- **What**: Test whether the Seeley–DeWitt expansion converges for the `a₀`-dominated vacuum-energy magnitude — the open gate underneath frontier #5/#6. The CC *ratio* (`1.032`) is truncation-robust; promoting any *absolute* `a₀`-moment vacuum-energy magnitude to physical status awaits this. Output: a convergence verdict for the SDW series at the `a₀` moment (does the `L_max` truncation of the absolute magnitude converge?).
- **Inputs**: the `a_n^ζ` ladder (`a₀`=6440, `a₂`=2776.165, `a₄`=1350.72, plus `a₆, a₈` from the closed pole ladder `S_d={0,2,4,6,8}`); the L_max-dependence of the raw mode-count sums (155984 at L_max=10, divergent); the multiplicative-normalization-cancellation invariant.
- **Gate**: JACOBSON-NONLOCAL-64 (OPEN). PASS: the absolute `a₀`-moment magnitude converges with L_max (licenses promoting an absolute CC magnitude); FAIL: it diverges (CC absolute magnitude permanently held pending; only the ratio is physical); INFO: converges only after a specified resummation.
- **Effort**: 4–6 hours, 1 agent session (distinguishes "located the CC term" — done — from "solved the CC magnitude" — open).

### V.12 — NNLO emergent-EP Casimir discriminator: the first genuine substrate EP *prediction*
- **What**: Per the S95 W3 genericity finding, `κ_EP=1` (LO+NLO) is generic-identity-cored (the Lichnerowicz–Weitzenböck `R/4` coefficient of ANY spin Dirac operator) — NOT a substrate-specific prediction. The genuine substrate prediction first appears at NNLO where the band-specific Casimir `ν_b(C₂)` re-enters the ratio. Compute the NNLO `κ_EP` deviation from unity for distinct bands (B1, B3). Output: `κ_EP^NNLO − 1` per band-pair, with the substrate-specific `C₂(b)` content.
- **Inputs**: `D_K² = ∇*∇ + ¼R_K` (E5); the band Casimirs `C₂(b)` for B1/B3; the single-spectral-triple postulate (one emergent `g_M=a₂` forcing band-independence at LO/NLO); `φ(τ)=f₂Λ²a₂(τ)/(48π²)`.
- **Gate**: NEW — `CF-S96-EP-NNLO-CASIMIR-DISCRIMINATOR`. PASS: a nonzero `κ_EP^NNLO−1` distinguishing the single-operator postulate from a generic Brans–Dicke / bimetric model (a genuine substrate prediction); FAIL: NNLO also generic (EP carries no substrate value-content at any order); INFO: nonzero but below any conceivable EP-test precision.
- **Effort**: 4–6 hours, 1 agent session (converts the EP "STRUCTURALLY INEVITABLE but value-generic" status into a testable prediction at NNLO; addresses the §9 frontier #8 genericity caveat directly).

### V.13 — m_H route selection: pin a single canonical Higgs-mass route within the ~2% budget
- **What**: Resolve the §7.1 / §9 frontier #3 route-dependence: the KK-threshold band is 127.5–131.8 GeV (defensible at ~2% theory budget), the zeta route (138.5 GeV) is excluded, the μ_BC fit (188 GeV) is an ACCOMMODATION. Determine whether a substrate-first principle selects a single route. Output: `m_H_canonical ± theory-budget`, the selected route, and the residual to PDG `125.25±0.17`.
- **Inputs**: the KK-threshold correction (`m_H=127.5–131.8 GeV`); the `ε_H`/scheme table (§3.2); the FUNCTIONAL-SELECT-67 outcome (V.1 — `m_H` and `n_s` are co-determined via the same `f`); `t*=0.08832`.
- **Gate**: NEW — `MH-ROUTE-SELECT` (coupled to V.1). PASS: a single route within ~2% of PDG selected by the same `f` that fixes `n_s`; FAIL: route-dependence persists / no single route lands in `[122,130] GeV`; INFO: a route selects but only the band, not a point.
- **Effort**: 3–4 hours, 1 agent session (couple to V.1; the `n_s∩m_H` intersection is the FUNCTIONAL-SELECT-67 PASS condition).

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Free-parameter ledger `{τ,Λ,f₀,f₂,f₄}+t*` | GEOMETRIC | HONEST (S95 W2-1 closes the de-empiricization route) | The conditioning premise for every "zero-parameter" headline; `t*` is genuinely empirical |
| 2 | Wronskian layer-independence `W ∝ R_K′(τ)³` | GEOMETRIC | CERTIFIED (S75 W2-E) | Licenses distinct vacuum/gravity/matter physics; does NOT license multiplying cosmological observables |
| 3 | CC: equilibrium `ρ_vac=0` exact vs observed-magnitude conditional | PHONONIC | Clause A warranted; Clause B C10-conditional | "Located the CC term, not solved the CC problem" — the most calibrated sentence in the document |
| 4 | α_s two-channel resolution (pivot +0.67σ) | GEOMETRIC | PASS (S93 W7-1) — supersedes my stale memory | No longer a contradiction; leaves a frozen `−0.0859` as a clean CMB-S4 falsifier |
| 5 | Two-scalar exhaustion `HH¹=HH²=0` | GEOMETRIC | PASS (S95 W2-2) | Interaction structure forced by the algebra; genuine advantage over string-field-theory vertex selection |
| 6 | The `a(t)`/Friedmann gap (C1/C2/T6) | NON-PHONONIC gap | C1 POSTULATED, C2/T6 BROKEN | Conditions every dagger row in §7.1 via borrowed `H(t)`; the load-bearing open frontier |
| 7 | Ordered Veil survival (diabatic freeze, `S_ent=0`) | PHONONIC | PASS (S95 W5), independent of S39 retraction | Over-determination done right; `N_pair=59.8` is `⟨Q⟩_GGE`, not a pair count |
| 8 | Joint-evidence over-reach (§7.3 vs §4.2) | — | FLAGGED (my domain, not a verdict) | Cross-layer product treats borrowed-`H(t)` brackets as independent likelihood factors — PRELIMINARY |
| 9 | n_s scheme-dependence (FUNCTIONAL-SELECT-67) | GEOMETRIC | OPEN (~22 sessions) | The decisive E31 gate is CONDITIONAL; highest-leverage open compute (V.1) |
| 10 | Ω_DM=0.120 CONDITIONAL on Γ_grav<H_0 | PHONONIC | OPEN CRITICAL (LEGGETT-GRAV-DECAY-67) | A CRITICAL conditional under a headline PASS; the S75 naive `Γ_grav≫H_0` must be resolved (V.5) |
| 11 | LISA CGWB / S43 BAO ring / DESI wₐ=0 / CF-35 | PHONONIC | LIVE FALSIFIERS | The genuine zero-parameter harvest — falsifiable, no ΛCDM counterpart (V.3, V.4, V.8) |

---

*Reviewer's closing note (empirical conscience).* This document passes the test I apply to any framework claiming to "be the universe": it states what would refute it, in specific, quantitative, near-term terms — DESI DR3 in 2026 on `wₐ=0`, LISA in ~2034 on the acoustic CGWB class, CMB-S4 in 2030 on the frozen `α_s = −0.0859`, LiteBIRD in 2030 on `r/n_T`, Aalto/Lancaster in 2028–9 on the `7.324992` cocycle ratio. A theory that hands you five dated cliff-edges and a printed list of its own unearned obligations is doing science. The brackets on already-measured observables are weaker evidence than the document's joint-probability rhetoric implies (flagged, §IV), and the borrowed `H(t)` is a real and load-bearing dependency that the capstone is admirably honest about — but the *structural* spine is strong, the closures have *narrowed* the surviving region rather than scattering it, and the open questions are exactly the ripe, runnable mathematics §V enumerates. Extraordinary claims require extraordinary evidence; this one has assembled a genuine partial case and, more importantly, has correctly identified the four detectors that will finish adjudicating it.
