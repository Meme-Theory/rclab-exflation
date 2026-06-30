# Capstone Equation Review — feynman

> Reviewer: **feynman-theorist** (path-integral / QFT / renormalization axis).
> Source under review: `sessions/framework/phonic-exflation-equation.md` ("The Phonon-Exflation Equation"), S95-era capstone.
> Independent solo synthesis. No coordination with other reviewers.
> Cross-checks performed live this review: Sage MCP (Wronskian + E3 curvature closed forms), knowledge MCP (`a_2_FW_zeta`, `a_4_FW_zeta`, `M_KK`, `t* = mellin_f_star_f0`, SDW-convergence gate `S94-K-CSUB-R-ABSOLUTE-CONVERGENCE`).
> Disclosure: a prior Round-2 fresh-eyes review by this agent is logged in the source (line 552) and in `Collabs/equation-build/feynman-review.md`. This is the *independent capstone-level* review the S95 skill mandates; it re-derives rather than re-cites.

---

## I. Verdict at a glance

The capstone is, by the standard I hold a theory to — *can I compute the number, and does the computation survive its own regulator?* — the most honest large-claim document I have audited in this project. It does the one thing the Feynman Test demands and that container-based unifications systematically dodge: it writes the action down explicitly (`§1`, boxed), identifies the propagator structure (block-diagonal `D_K(τ)`, gap never closes, `§2.3`), reads the vertices off the inner fluctuation (`§1.1`), power-counts the divergence structure via the dimension spectrum `S_d = {0,2,4,6,8}` (`§3.3`), and then — crucially — *states which numbers survive regularization and which do not* (FI/RD partition, `§3.2`; the `a_n^SD` vs `a_n^ζ` firewall, `§8.2`).

The single most important thing this document gets right, from my vantage, is that **it does not pretend the cutoff functional `f` collapses into `D_K`.** The master object is written `S[D_K, f, Λ]` with all three arguments visible (`§3.3` "Consequence"), and the cosmological-constant problem is correctly diagnosed as the *proof* that they cannot be collapsed (same `D_K`, different `f`, vacuum energy lands in a different moment). That is the QFT-correct statement. A lesser document would have buried `f` and claimed zero parameters.

What I verified holds:
- The **Spectral-Moment Decoupling Theorem** (`§4.2`) — the load-bearing algebraic-independence claim — is exactly correct. Sage confirms `W[1, R_K, R_K²] = 2·R_K′(τ)³`, `R_K′ = e⁻⁴ᵗ(e³ᵗ−1)²`, hence `W ∝ e⁻¹²ᵗ(e³ᵗ−1)⁶`, vanishing to sixth order only at `τ=0`. This licenses "vacuum / gravity / matter are distinct physics everywhere the universe lives." SOLID.
- The **E3 curvature** closed form and all three verification-ledger curvature entries (`R_K(0)=2`, `R_K′(0)=0`, `R_K(0.19)=2.01814`) reproduce to machine precision. SOLID.
- The **one-loop face** `Γ[τ] = S[D_K(τ)] + ½Tr ln(D_K²/Λ²) = S − ½ζ′_D(0,τ)` (`§1.3a`) is the QFT-canonical effective action and matches the corpus form (S16/S54/S62). The identification of the boxed `S` as the *bare* action and the loop term as a *threshold correction* is correct and is the right call — it keeps the master object from silently absorbing a loop it has not computed.

What is genuinely PRELIMINARY or carries an unstated tension (developed in §III):
- The three S95 W2 gates the document leans on for its strongest new structural claims (**W2-1** t*-corridor FAIL, **W2-2** Hochschild exhaustion, **W2-3** one-loop robustness of no-interior-saddle) are **not yet in the knowledge index** — they post-date the last `/weave --update`. I cannot independently confirm their verdicts from the canonical graph; I cite them as the document records them and flag them PRELIMINARY-pending-index.
- The "**26% one-loop**" magnitude that kills the t*-corridor (`§1.4`) is the one place where a regulator-sensitivity I would want pinned is asserted as a single number. The whole `Γ_1loop ≈ 26%` of tree+loop rests on a `½Tr ln(D_K²/Λ²)` evaluated under *one* regularization at *one* `Λ`; the document's own ZETA-NOT-PHYSICAL theorem (`§3.2`) says absolute spectral-moment magnitudes are scheme artifacts. The *qualitative* conclusion (t* is not the loop coefficient) is robust to a factor of a few; the *quantitative* `R = 1.977` is not, and the document slightly over-reads it as if it were a clean 2× miss. Minor, but it is a regulator-discipline gap in a document that is otherwise scrupulous about exactly this.

Net: the QFT spine is coherent — no sign error, no factor error, no dimensional error that I can find, and the dimensional-closure argument in `§8.1` correctly defuses the spurious `L⁻¹²` double-counting tower. The honest gaps (`a(t)`, SDW convergence, family number, `f`-selection) are real, are flagged, and are exactly the ones a substrate theory is *entitled* to leave open. The over-claim risk is low and is mostly self-policed.

---

## II. Where the equation touches my domain — what is solid

### II.1 The action is written down, and it is the right action (`§1`)

`S[D_K(τ), f, Λ] = Tr f(D_K²/Λ²) + ⟨Jψ̃ | D_K(τ) | ψ̃⟩`. This is the Chamseddine–Connes spectral action plus the canonical fermionic bilinear. The `§1.1` exhaustion argument — that a trace (operator functional) and an inner product (bilinear form) are the *only* two natural scalars of `(A_K, H_K, D_K, J)` — is the correct statement of why the action is complete, and it is the path-integral-correct reason there is "no room for a third term." The document upgrades this from a counting argument to an algebraic-rigidity claim via `dim HH¹(A_K) = dim HH²(A_K) = 0` (W2-2). I cannot confirm W2-2 from the index (not yet rebuilt), but the *mathematics* is standard: `A_K = ℂ⊕ℍ⊕M₃(ℂ)` is finite-dimensional semisimple, Whitehead's first lemma gives `HH¹ = 0` (all derivations inner), and the second-lemma analog gives `HH² = 0` (all first-order deformations trivial). The claim is **structurally sound on textbook grounds** even before the gate lands. PRELIMINARY only on the specific Sage rank-count, not on the conclusion.

GEOMETRIC/PARTICLE classification: the action and its axioms (`§1.2`) are GEOMETRIC (they concern `D_K` itself); the excitations the action describes are PHONONIC.

### II.2 The triple identity and the partition function (`§1.3a`) — QFT-coherent

`Z = Σ_{D_K(τ)} e⁻ˢ`, `S ≡ I_E`, sum over the substrate's own internal geometries, *not* over a background metric. This is the Gibbons–Hawking Euclidean-action-equals-partition-function-weight statement, correctly substrate-ized. Two things I checked and endorse:

1. **The conformal-factor instability is correctly dismissed as a container artifact.** The standard Euclidean-gravity path integral is unbounded below because the conformal mode has the wrong-sign kinetic term (Gibbons–Hawking–Perry). The document notes this is *absent here* because the Jensen deformation is volume-preserving TT (`tr h_J = 0`, G6) — the conformal/breathing mode is removed by construction at `§2.1`. This is exactly right: there is no conformal factor to destabilize because the single modulus lives on the TT eigendirection. SOLID, and a genuinely nice point.

2. **The "no interior saddle ⇒ boundary-dominated" reading is the correct path-integral statement.** An action monotone in `τ` (`dS/dτ > 0`, E7) has `e⁻ˢ` dominated by the `τ=0` boundary; the transit is the relaxation of that boundary configuration down the ramp. This is the spectral-action analog of a Gibbons–Hawking–York boundary-dominated integral. The document's claim that this makes "transit, not slow-roll" *structurally inevitable rather than observed* is, I agree, the stronger and correct framing. The slow-roll relations `r=16ε`, `n_s=1−6ε+2η` are theorems of the single-clock adiabatic Bunch–Davies vacuum; the fold violates all three premises (diabatic, `c_s≠1` BdG, multi-mode squeezed GGE), so their *derivation assumptions are absent*. This is the right way to say "INAPPLICABLE" — not a wrong number, a missing derivation. SOLID.

### II.3 The dimension spectrum is the power-counting (`§3.3`) — exactly the Feynman-Test step 4

`ζ_{D_K}(s) = Σ m_k λ_k^{−2s}`, moments are residues at `s=(d−n)/2`, dimension spectrum `S_d = {0,2,4,6,8}` for `d=8`. This *is* the renormalizability/power-counting analysis: it tells you precisely which heat-kernel coefficients exist as honest residues (`a₀, a₂, a₄, a₆, a₈`; odd ones vanish by BDI parity) and where the cone closes. The substrate handing you a **finite closed pole ladder** instead of a Wheeler-superspace sum-over-topologies is the correct diagnosis of why the framework does not inherit the `10¹²⁰` catastrophe at the structural level. This is the cleanest statement in the document of the substrate-first resolution of the CC location problem, and it is QFT-correct.

The defensive note that `S_d` is `τ`-independent (no flowing spectral dimension, `d_s ∼ 8` at the gap scale) is consistent with the canonical `d_s_fold_window_sigma = 1.4005` reading being a *diffusion-window artifact* (S92), not a CDT-like UV reduction. I confirmed S92 is in the index and the document's framing matches it. SOLID; the silence on dimension-flow is explicit and honest.

### II.4 The FI/RD partition is the regulator discipline I most respect (`§3.2`, `§8.2`)

The document partitions observables into **Functional-Invariant** (ratios of two spectrum-sums under *one* regulator: `c_s`, `R₁`, rank-drift exponent) and **regulator-dressed** (`ε_H` sign, `n_s`, `m_H`, absolute vacuum energy). This is the correct and complete statement of which numbers a spectral action is *allowed* to predict before `f` is selected. The `ε_H` sign-flip table (`§3.2`: `+0.0216` cutoff vs `−0.0449` zeta) is the honest demonstration that the CMB tilt sign is a *scheme* property, not a spectrum property. And the over-fitting defense — that the anomaly family is excluded *structurally* by S67 pre-registration, decided before the tilt comparison — is the correct epistemic move. You do not get to keep only the functionals that agree; the document knows this and protects against it.

The `a_n^SD` (Gilkey, regulator-free, for layer *identity*) vs `a_n^ζ` (zeta-regulated, for *numerics*) firewall in `§8.2` is exactly the "two `a_n` objects, never conflated" discipline that `regulator-pin-discipline.md` exists to enforce. I verified the canonical pins: `a_2_FW_zeta = 2776.165389` (S88), `a_4_FW_zeta = 1350.7216` (S75). Both match the document's table. SOLID.

### II.5 The Ordered Veil as analog-information-paradox resolution (`§5.3`) — I endorse the unitarity argument

The transit is a Bogoliubov transformation, unitary by construction; `|α_k|²−|β_k|²=1` mode-by-mode. A thermalizing relic (`S_ent > 0`) would scramble the unitary into a mixed state and create an analog information paradox (the squeeze phase hidden the way thermal Hawking flux hides infalling information). The GGE relic stays pure (`S_ent = 0`), the phase data retained in the conserved charges, so there is no Page curve to reproduce. This is the correct optical-theorem-adjacent statement: unitarity is preserved because nothing thermalizes. The document's care in separating the *substrate-BdG* `u_k` equation (relic content) from the *Mukhanov–Sasaki* `v_k` equation (emergent `A_s`) — "`A_s` is NOT computed from the BdG `u_k`" (`§5.3`) — is the right factorization and prevents a genuine category error I have seen elsewhere in analog-cosmology. SOLID. PHONONIC.

One precision I endorse: the `N_pair = 59.8` figure is correctly demoted to a *projected charge* `⟨Q⟩_GGE`, not a literal pair count (it inherits a ~60% PBCS gap overestimate and a ~225× Richardson–Gaudin condensation-energy overestimate). The regime-robust claim is `P_exc = 1`. This is the honest reporting; the number that survives is the diabaticity, not the count.

### II.6 Dimensional closure is correct, including the trap (`§8.1`)

`[S] = mass⁰`; each layer term `f_{d−2k}Λ^{d−2k}a_{2k}` is individually mass-dim 0 because Gilkey scaling `[a_{2k}] = mass^{2k−d}` cancels `[Λ^{d−2k}] = mass^{d−2k}`. The document explicitly names the double-counting error (assigning both `Λ` and `a_{2k}` an inverse-length, producing a spurious `L⁻¹²` tower) and refutes it. This is the correct dimensional analysis and it is the kind of trap I check for first. SOLID.

---

## III. Where I see tension, gap, or over-read — flagged, not silently resolved

### III.1 [TENSION — minor, regulator-discipline] The "26% one-loop" is a single-scheme number used as if scheme-invariant (`§1.4`)

The document closes the corridor "t* is the one-loop threshold coefficient" via W2-1 FAIL with `R = |t*_pred − t*|/t* = 1.977`, on the grounds that `Γ_1loop ≈ 26%` of the tree+loop spectral action is `~3×` too large to *be* the admixture weight `t* = 0.08832`.

The qualitative conclusion is almost certainly right and I do not contest it: a parameter-free `½Tr ln(D_K²/Λ²)` that lands at tens-of-percent of the action cannot be the `O(0.09)` regulator admixture. The matrix-model rigidity is correctly bounded — field content forced by the algebra, regulator weight *not* forced.

But the **`26%` magnitude is a regulator-sensitive absolute**, and the document's own ZETA-NOT-PHYSICAL theorem (`§3.2`) says absolute spectral-moment magnitudes are scheme artifacts; only ratios under a fixed regulator are physical. `½Tr ln(D_K²/Λ²) = −½ζ′_D(0,τ)` depends on the choice of `Λ` (it sets the scale inside the log) and on how the trace is regulated. A different but equally-defensible scheme could move `26%` by a factor of a few — which would move `R = 1.977` substantially. The conclusion (corridor closed) survives because even a factor-3 swing keeps `Γ_1loop ≫ t*`; but the document prints `R = 1.977` as if it were a clean "loop is 2× too big," and that specific number is not scheme-stable. This is the *one* place the document relaxes its own otherwise-exemplary regulator discipline.

Recommendation: report the corridor closure as "`Γ_1loop = O(10%)`–`O(30%)` across admissible schemes, `≫ t* = 0.088` in all of them ⇒ CLOSED structurally," not as a single `R = 1.977`. See §V item **F-1**.

### III.2 [GAP — confirmed real, correctly flagged] SDW convergence is the open gate under the CC absolute magnitude (`§8.5`, `§9` #6)

The document flags (`§8.5`) that the Seeley–DeWitt expansion is *not* certified to converge — "the `a₀`-dominated 114-OOM question, JACOBSON-NONLOCAL-64, OPEN" — and that absolute-energy observables (CC, `A_s`) remain conditional on this. I confirmed this is a live FAIL: `S94-K-CSUB-R-ABSOLUTE-CONVERGENCE` returns `converges=False`, `dK/dL` *increasing* with `L_max` (`max dK/dL = 2.1e30` against a `1e-3` ceiling), with the Mellin `a₂` intercept growing `2.08e15` (L50) → `2.11e31` (L100). **The absolute `a₂`/`a₀` moments do not converge with truncation.** The document is *correct* and honest: it explicitly restricts strong claims to the ratio-observables (`n_s`, `g₁/g₂`, `R₁`, `a₂/a₀`), which are truncation-robust (the multiplicative-normalization-cancellation invariant, `§8.2`), and holds the absolute magnitudes pending convergence.

This is not an over-claim — it is a correctly-scoped conditional. But it is the deepest open item in *my* domain, because "the absolute vacuum-energy magnitude is conditional on a divergent series being resummed" is precisely the renormalization question. The CC *ratio* `1.032` (DILUTION-CC-66) is a dimensionless tracking statement and survives; the CC *absolute* does not yet exist as a convergent number. The document says exactly this. Flagging it here so the §V harvest carries it forward as the priority renormalization computation (**F-2**).

### III.3 [PRELIMINARY — not yet indexed] The three S95 W2 gates cannot be independently confirmed from the canonical graph

W2-1 (t*-corridor FAIL), W2-2 (Hochschild exhaustion PASS), W2-3 (one-loop robustness of no-interior-saddle PASS) are cited as load-bearing for the document's strongest *new* structural claims (`§1.3a`, `§1.4`). None surfaced in `search_knowledge` — they post-date the last `/weave --update`. Per the rules, recorded verdicts are authoritative and I do not re-adjudicate; but I cannot *cross-check* them either. I flag them PRELIMINARY-pending-index. The *mathematics* of W2-2 is textbook-sound (§II.1); W2-3's claim (full `Γ[τ]` retains fixed sign with zero interior sign-changes on a 200-point grid, three routes) is plausible and consistent with the bare-action E7 monotonicity, but a one-loop term can in principle introduce an interior feature, so this is a genuine computation whose verdict I am taking on report. Recommendation: rebuild the index (`/weave --update`) so these gates enter the graph; until then any downstream citation of "one-loop-robust no-interior-saddle" should carry the pending tag. See §V item **F-3** (independent re-derivation of W2-3).

### III.4 [UNSTATED ASSUMPTION — worth surfacing] The one-loop term is treated as a threshold correction, but its *back-reaction on the saddle* is never computed

`§1.3a` correctly separates the bare `S` (the master object) from `Γ_1loop` (threshold correction). But there is a subtlety the document does not address: if `Γ_1loop` is `O(26%)` of the action (its own §1.4 figure), then it is *not* a small perturbation, and the saddle-point structure of `Z = Σ e⁻ˢ` should in principle be re-evaluated with the *full* `Γ`, not the tree `S`. The document asserts (via W2-3) that the no-interior-saddle survives at one loop — good — but it does not address whether the *location* of the boundary-domination or the *transit rate* shifts at one loop. For the qualitative "transit not slow-roll" story this does not matter (no interior saddle is no interior saddle). For any *quantitative* transit observable (`Mach`, `δt_transit`, the relic `N_pair`), a 26%-of-action loop correction is not obviously negligible and is not bounded in the document. This is not a contradiction — it is an uncomputed correction that the document's own magnitude estimate makes non-trivial. See §V item **F-4**.

### III.5 [CONFLICT-CHECK — resolved in document's favor, noted for completeness] My memory's `n_s` and the document's `n_s`

My agent memory records `n_s = 0.501 FAIL (14× overshoot)`. The document reports `n_s ∈ {0.9561, 0.9590, 0.9595}` (scheme-dependent, `1.29σ–2.10σ` from Planck). These are **not in conflict** — they are different observables that my memory compressed under one label. My `0.501` is the *bare substrate-distance / BZ-scale* tilt before transport; the document's `0.956`-band is the *Goldstone / CMB-pivot* image after the transport map, which is the correct comparison channel (the same 54-decade scale-and-channel distinction the document makes for `α_s` in its α_s box). The document's value is the right one to quote against Planck; my memory entry is stale-by-compression and I am flagging it (not resolving the document against it — the document is correct). I will update my own memory separately. No action for the document.

### III.6 [OVER-READ — very mild] "Categorically stronger than container-based unification" (`§0`, `§9`)

The claim that deriving-the-stage is *categorically* stronger than populating-a-given-one is correct and I endorse it. The mild over-read is rhetorical: the document occasionally lets this slide toward "therefore the open inputs are not defects" (`§1.4`: "what such a theory is *entitled* to leave to a future completion — not defects"). A principle theory is entitled to leave `f` open; it is *not* entitled to leave `f` open *and* claim the red tilt, because the red tilt depends on `f = √x` (`§3.2`). The document mostly polices this (the BMA band `n_s = 0.969 ± 0.022` is the honest UQ object, `§7.1`), but the "not defects" framing is one notch too generous: an open `f` that controls a sign you are claiming *is* a defect with respect to that specific claim, even if it is a legitimate openness with respect to the theory's overall status. Minor; the document's own FI/RD partition already contains the correction. No §V item; flagged for framing precision only.

---

## IV. Cross-checks performed (provenance)

| Claim in source | Check | Result |
|:--|:--|:--|
| `R_K(0)=2`, `R_K′(0)=0`, `R_K(0.19)≈2.018` (`§2.3`, ledger) | Sage `sage_eval` on E3 polynomial | `2`, `0`, `2.01814` — exact ✓ |
| `R_K′(τ)=e⁻⁴ᵗ(e³ᵗ−1)²` (`§4.2`) | Sage symbolic `diff` − claim, `simplify_full` | residual `0` ✓ |
| `W[1,R_K,R_K²] ∝ R_K′³`, `∝ e⁻¹²ᵗ(e³ᵗ−1)⁶` (`§4.2`) | Sage `det` of 3×3 derivative matrix | `W = 2·R_K′³`; `R_K′³ − e⁻¹²ᵗ(e³ᵗ−1)⁶ = 0` ✓ (decoupling theorem SOLID) |
| `a_2_FW_zeta = 2776.165389` (`§8.2`) | knowledge MCP `get_constant` | confirmed, S88, not superseded ✓ |
| `a_4_FW_zeta = 1350.7216` (`§8.2`, ledger) | knowledge MCP `get_constant` | confirmed, S75 ✓ |
| `M_KK = 7.4287×10¹⁶ GeV` (`§3.1`) | knowledge MCP `get_constant` | `7.428660036284456e16`, CONST-FREEZE-42 ✓ |
| `t* = 0.08832`, `f* = 0.9117√x+0.0883e⁻ˣ` (`§3.2`) | knowledge MCP (`mellin_f_star_f0`, S78; SPECTRAL-FUNCTIONAL-FIT-72 PASS `1.3e-14`) | confirmed ✓ |
| `Γ_1loop = ½Tr ln(D_K²/Λ²) = −½ζ′_D(0,τ)` (`§1.3a`) | knowledge MCP (S16/S54/S62 corpus forms) | canonical form confirmed ✓ |
| SDW convergence OPEN (`§8.5`, `§9` #6) | knowledge MCP `S94-K-CSUB-R-ABSOLUTE-CONVERGENCE` | FAIL, `converges=False`, `dK/dL` increasing — open gate is REAL ✓ |
| `d_s`-flow silence (`§3.3` defensive note) | knowledge MCP (S92 `d_s_fold_window_sigma=1.4005`) | windowed reading is diffusion-window artifact, matches ✓ |
| W2-1 / W2-2 / W2-3 (S95) | knowledge MCP `search_knowledge` | NOT in index (post-`/weave`); cited on report, PRELIMINARY ✓ |

Every load-bearing closed form in my domain that *is* indexed checks out exactly. The one gate that would falsify a strong claim (CC absolute) is correctly flagged open by the document.

---

## V. Carry-Forward Computations (the open-question harvest)

Each item is a runnable computation with all four fields. These are the "ripe harvest" — every open question in my domain converted to a calculation. Default Python: `phonon-exflation-sim/.venv312/Scripts/python.exe`; import `from canonical_constants import *`; GPU AMD RX 9070 XT via `torch.linalg` for any dense op ≥ 100×100.

### F-1 — Regulator-band the one-loop fraction `Γ_1loop / Γ` (sharpen the t*-corridor closure)

- **What**: Recompute `Γ_1loop = ½Tr ln(D_K²/Λ²) = −½ζ′_{D_K}(0)` and the ratio `Γ_1loop / (S_tree + Γ_1loop)` under ≥3 admissible regularization schemes (zeta `ζ′_D(0)`; Pauli–Villars subtraction at `Λ = M_KK`; sharp-cutoff direct sum on the `L_max=10` eigenvalue cache) and across `Λ ∈ {M_KK, 10 M_KK, M_Pl}`. Report the *band* of the fraction, not a single number. Goal: replace the document's scheme-fragile `R = 1.977` with a regulator-robust statement.
- **Inputs**: `L_max=10` eigenvalue cache (78,080 unique `λ_k`, multiplicities `m_k`); `S_tree = S_SA(τ_fold)` from canonical (`§5.1`, `S_fold = 2.50e5`); `t* = 0.08832` (`mellin_f_star_f0`); `M_KK`, `M_Pl_eff` from canonical_constants.
- **Gate**: PASS if `min_scheme(Γ_1loop/Γ) > 3·t* = 0.265` (i.e. the loop is `≥3×` the admixture weight in *every* admissible scheme ⇒ corridor closed regulator-robustly). INFO if the band straddles `t*` (corridor closure scheme-dependent). FAIL if any scheme gives `Γ_1loop/Γ ≈ t*` (corridor reopens). Pre-register the scheme list and `Λ` grid before running.
- **Effort**: Low–medium. The eigenvalue cache exists; `ζ′_D(0)` from existing spectra is a few-hundred-line script. This is my standing open item ("zeta-regularized one-loop Γ[τ] from existing eigenvalue data") finally cashed against a concrete gate.

### F-2 — Borel/zeta resummation of the divergent SDW series for the absolute `a₀`/`a₂` moments (the renormalization computation under the CC magnitude)

- **What**: The Mellin `a₂` absolute does not converge (`S94-K-CSUB-R-ABSOLUTE-CONVERGENCE` FAIL, `dK/dL` increasing). Test whether the *divergent* SDW partial sums are **Borel-summable** (or zeta-function-resummable) to a finite absolute moment. Construct the partial-sum sequence `a₂(L_max)` for `L_max = 5…12`, fit the large-`L` growth (the gate reports `~e^{growth·L}` behavior), and apply Borel transform + Padé–Borel resummation; cross-check against the zeta-regulated `a_2_FW_zeta = 2776.17` (which IS finite — the question is whether the divergent *raw* series resums *to* the zeta value).
- **Inputs**: raw mode-count partial sums `a_n^raw(L_max)` for the available `L_max` (the document's `§8.2` table gives `a₂^raw = 64308.24` at `L_max=10`); `a_2_FW_zeta = 2776.165389`, `a_0_FW_zeta = 6440`, `a_4_FW_zeta = 1350.7216`; `S94-K-CSUB-R-ABSOLUTE-CONVERGENCE` npz for the growth-rate fit.
- **Gate**: PASS if the Padé–Borel resummation of the divergent raw series converges to within 10% of the zeta-regulated value (⇒ the zeta moment IS the resummed physical absolute; CC-absolute conditional partially discharged). INFO if Borel-summable but to a *different* finite value (⇒ scheme ambiguity quantified). FAIL if not Borel-summable (⇒ the absolute moment is genuinely scheme-dependent and the CC-absolute stays conditional — confirms JACOBSON-NONLOCAL-64 as a hard wall).
- **Effort**: Medium. Borel–Padé on ~8 partial sums is standard; the physics payoff is high — it directly addresses the deepest open renormalization question (`§9` #6).

### F-3 — Independent re-derivation of the one-loop no-interior-saddle (verify W2-3 from first principles)

- **What**: Independently reconstruct `Γ[τ] = S_SA(τ) + ½Tr ln(D_K²(τ)/Λ²)` on a dense `τ`-grid over `[0, τ_now]` and test for interior sign-changes of `dΓ/dτ`. Use the block-diagonal structure (`§2.3`): `Tr ln(D_K²) = Σ_{(p,q)} Tr ln(D_{(p,q)}²)`, so the loop term factorizes per Peter–Weyl sector and is cheap. Compare `dΓ/dτ` against the tree `dS/dτ = +58,673` at the fold (`§5.1`) and confirm zero interior zeros. This re-derives W2-3 (which is not yet in the index) rather than citing it.
- **Inputs**: `D_{(p,q)}(τ)` blocks from the Dirac-spectrum builder at ≥200 `τ` points on `[0, 0.30]`; `S_SA(τ) = a₀ − a₂(τ) + a₄(τ)` from canonical layer values; `Λ = M_KK`.
- **Gate**: PASS if `sign(dΓ/dτ)` is constant with zero interior sign-changes on the 200-point grid (⇒ W2-3 independently confirmed; no-interior-saddle is one-loop-robust). FAIL if any interior sign-change appears (⇒ the loop introduces an interior feature absent at tree level; the "transit not slow-roll" inevitability weakens from structural to tree-level-only). Pre-register the grid before running.
- **Effort**: Medium. Per-sector `Tr ln` over 200 `τ`-points is GPU-friendly (each block ≤ `O(10⁴)`); the irrep construction at high `(p,q)` is the cost, mitigated by the Friedrich–Bär saturation bound (`math-scripts.md`) — bottom-sector log-traces dominate, so `L_max=8` likely suffices.

### F-4 — Bound the one-loop back-reaction on the transit observables (`Mach`, `δt_transit`, `N_pair`)

- **What**: If `Γ_1loop = O(26%)` of the action (the document's own §1.4 figure), the loop is not a small perturbation. Compute the *fractional shift* the one-loop term induces in the three quantitative transit observables: the fold Mach number (`13.75`), the transit duration (`δt_transit = 1.130e-3 M_KK⁻¹`), and the relic charge (`⟨Q⟩_GGE = 59.8`). Method: re-evaluate the local transit rate `τ̇` at the fold using `Γ′(τ)` instead of `S′(τ)` in the saddle-rate relation, and propagate to `Mach` and `δt`. Report `Δ(observable)/observable` per scheme from F-1.
- **Inputs**: `Γ_1loop(τ)` and `dΓ_1loop/dτ` near `τ_fold` from F-3; canonical `Mach = 13.75`, `δt_transit = 1.130e-3 M_KK⁻¹`, `c_fabric = 209.97 M_KK`, `N_pair`/`⟨Q⟩_GGE = 59.8`.
- **Gate**: PASS (loop negligible) if `|Δ(Mach)/Mach| < 0.05` AND `|Δ(δt)/δt| < 0.05` (⇒ transit observables are tree-robust; the loop is a threshold correction in fact, not just in name). INFO if `0.05 ≤ shift < 0.30` (⇒ loop correction quantified, transit numbers carry a one-loop systematic band). FAIL if `shift ≥ 0.30` (⇒ the transit observables require the full `Γ`, not the tree `S`; the §5.2 numbers need a one-loop revision).
- **Effort**: Medium. Depends on F-3 output; the rate relation is closed-form once `Γ′(τ_fold)` is in hand.

### F-5 — Optical-theorem / unitarity check on the GGE Bogoliubov transformation across the fold

- **What**: The Ordered Veil argument (`§5.3`) asserts the transit is a unitary Bogoliubov transformation with `S_ent = 0`. Verify unitarity *directly* as a sum rule: for the diabatic sudden-quench Bogoliubov coefficients `(α_k, β_k)` of the substrate-BdG `u_k`-equation, confirm `|α_k|² − |β_k|² = 1` mode-by-mode (bosonic normalization) AND the total optical-theorem-style sum rule `Σ_k (|α_k|² − |β_k|²) = N_modes` to machine precision, across the full `L_max=10` mode set. This is the unitarity leg of the Feynman Test (step 6) applied to the cosmogenesis transit, not just to the post-transit EFT (where it already PASSed at `1.1e-15`, S55).
- **Inputs**: substrate-BdG `ω_k(τ) = E_k = √((λ_k²−μ²)² + Δ_k²)` (`§5.3`); the sudden-quench matching across `τ_fold`; `λ_k`, `Δ_k`, `μ` from canonical; `P_exc = 1.000` as the diabatic-limit check.
- **Gate**: PASS if `max_k | |α_k|²−|β_k|²−1 | < 1e-12` AND `S_ent = 0` to machine precision (⇒ unitarity + purity of the Ordered Veil confirmed at the genesis transit; the analog-information-paradox resolution is computationally certified). FAIL otherwise (⇒ the Bogoliubov transform is not unitary as constructed, which would break the §5.3 purity claim). 
- **Effort**: Low–medium. Sudden-quench Bogoliubov coefficients from existing BdG spectra are a closed-form per-mode computation; this is the cleanest unitarity gate in the document's domain and it is currently asserted (`§5.3` "bosonic normalization holds mode-by-mode") rather than gate-certified at the *genesis* layer.

### F-6 — Wronskian non-degeneracy as a global truncation-robustness statement

- **What**: The Decoupling Theorem (`§4.2`) is proven on the *exact analytic* `R_K(τ)` (curvature polynomial). Confirm the algebraic independence survives the `L_max` truncation that the actual numerics use: compute the Wronskian `W[a₀, a₂, a₄](τ)` from the *truncated zeta-moment* functions `a_n^ζ(τ; L_max)` for `L_max = 5…10` and verify it remains non-vanishing at `τ_fold` and degenerate (to numerical tolerance) only as `τ → 0`. This closes the gap between the analytic theorem and the truncated objects the document actually pins.
- **Inputs**: `a_n^ζ(τ; L_max)` evaluated on a `τ`-grid for each `L_max ∈ {5,…,10}`; the analytic `W = 2·R_K′³` as the continuum target.
- **Gate**: PASS if `W^ζ(τ_fold; L_max) > 0` for all `L_max` AND `W^ζ(τ; L_max) → 0` as `τ → 0` for all `L_max` (⇒ algebraic independence is truncation-robust, not an artifact of the analytic idealization). INFO if `W^ζ` non-vanishing at the fold but the `τ→0` degeneracy is L_max-sensitive. FAIL if `W^ζ` vanishes at the fold for some `L_max` (⇒ the layers degenerate under truncation; the Decoupling Theorem's physical relevance is conditional).
- **Effort**: Low. The zeta moments at each `L_max` are already computed for the convergence study; this is a determinant evaluation on existing data.

---

## VI. Summary statement

The Phonon-Exflation Equation is, in the parts that touch my domain, a **QFT-coherent capstone with no sign, factor, or dimensional error that I can find**, and with a regulator discipline (FI/RD partition, `a_n^SD` vs `a_n^ζ` firewall, "all three arguments of `S[D_K,f,Λ]` visible") that is exactly the discipline a spectral action *must* observe to make honest predictions. The load-bearing Spectral-Moment Decoupling Theorem verifies exactly via Sage; the canonical constants verify exactly via the knowledge MCP; the one-loop face is the canonical effective action correctly demoted to a threshold correction.

The document's strongest virtue is that it *self-polices the over-claim*: it writes the free-parameter ledger as `{τ, Λ, f₀, f₂, f₄} + t*`, not zero; it flags the `a(t)` gap as "the most important caveat" without softening; it restricts strong claims to truncation-robust ratio-observables and holds the absolute magnitudes (CC, `A_s`) pending an SDW-convergence gate that I independently confirmed is a live FAIL. That is how a claim this large stays honest.

The genuine open frontier in my domain is singular and sharp: **the absolute spectral moments rest on a divergent series whose resummation is uncomputed** (`§8.5`/`§9` #6, confirmed by `S94-K-CSUB-R-ABSOLUTE-CONVERGENCE`). Everything the document claims as strong lives on the ratio/topological side that survives the continuum dissolution; everything it flags as conditional lives on the absolute/geometric side that does not. The §V harvest is built around that fault line — F-2 (Borel resummation) is the priority renormalization computation, F-1/F-3/F-4 close the one-loop discipline gap, and F-5/F-6 certify the unitarity and truncation-robustness that the document currently asserts rather than gates.

If I cannot compute it, I do not understand it. This document, almost uniquely, tells you precisely which numbers it has computed, which it has located but not computed, and which await a regulator it has not yet selected. That is the right answer to "can you put the universe in an equation": *yes — here is the equation, here is what it computes, and here is the honest list of what it does not.*
