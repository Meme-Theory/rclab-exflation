# INV4-W3-2 Workshop — Level-3 Magnitude Convergence/Divergence Criterion

**Gate**: INV4-W3-2 | **Investigation**: 4 | **Wave**: 3 | **Type**: workshop (EXACTLY 2 agents, 2 rounds, sequential, shared document)
**Trigger**: `[VERIFY-THEOREM]` (the workshop produces a STRUCTURAL VERDICT — a candidate theorem; no numerical [SIGN] gate)
**Classification**: GEOMETRIC
**Agents (two DIFFERENT axes)**:
- **schwarzschild-penrose-geometer** — Reading (a), GEOMETRIC (homogeneity-degree-vs-apex-dimension)
- **lizzi-spectral-functional-theorist** — Reading (b), SPECTRAL (regulator-class / functional-select / pole-index)

**Closure**: artifact-existence-with-content — this md must carry `## Wrap-Up` + `Effected In-Session` + `Carry-Forward Computations`. **NO verdict line** (a workshop gate emits no verdict-file line; `gate-verdicts.md §"Investigation-Track Canonical Path"`).

**Sources** (read before writing):
- `computations/session-109/s109_gate_verdicts.txt` — S109-VIICB-ZETA-NATIVE-LEVEL-3 FAIL (trend_sign=+1, is_weyl_divergent=True, is_convergent=False, anti_tautology_holds=True; rel_L10=100.13, anchor_L10=280743.235, g_M=2776.165)
- `sessions/permanent-results-registry.md` — §VII.AU + §VII.CB registry entries (the recurring HELD-Level-3 instances)
- `.claude/rules/cross-pillar-bridge-anatomy.md` — the 3-level structural-confidence ladder + the Tier-1/Tier-2 dimensional-re-anchorability gate
- `sessions/investigation/investigation-1/schwarzschild-penrose-geometer.md` — sp survey C-3 + R-3

---

## Adjudication Question

Which property of a substrate-IS cross-pillar-bridge-map observable predicts whether its finite-L Level-3 magnitude anchor **CONVERGES** (admits a continuum L→∞ target) or **DIVERGES** (monotone-increasing, no target — the regime-BREAKDOWN signature of S109-VIICB-ZETA-NATIVE-LEVEL-3: trend_sign=+1, is_weyl_divergent=True, is_convergent=False)? Recurring instances: §VII.AU (confirmed GENERIC under-performance), §VII.CB (S107 magnitude FAIL, Level-3 row HELD), S109 (ζ-native route CLOSED). Two competing structural readings, presented at EQUAL weight:

- **Reading (a) — GEOMETRIC** (schwarzschild-penrose-geometer): the convergent-vs-divergent outcome is fixed by the bridge map's HOMOGENEITY DEGREE relative to the spectral-cone APEX DIMENSION `d_spec_cone_apex = 8`. Candidate criterion: "Level-3 magnitude converges iff the bridge map's homogeneity degree ≤ the apex dimension" (sp R-3). At finite L the MAGNITUDE is partly a truncation artifact whenever degree exceeds apex — a coordinate-vs-invariant distinction in spectral-geometry form.
- **Reading (b) — SPECTRAL** (lizzi-spectral-functional-theorist): the outcome is fixed by the REGULATOR CLASS + FUNCTIONAL SELECTION + POLE INDEX. Candidate criterion: the magnitude diverges because the chosen functional/regulator does not BIND the Level-1 cohomology class to a continuum target (a non-binding Level-2 envelope), i.e., the ζ-native functional at this pole index admits no convergent continuum image.

The two readings are NOT a priori reconcilable without adjudication: they may pick out the SAME observables (then derive WHY the two criteria coincide — e.g. apex dimension IS a function of pole index and regulator class) or DIFFERENT observables (then a decisive forward gate must measure the discriminating case).

**Three sub-questions (each adjudicated by BOTH agents at equal weight):**
- **(a)** Which property — homogeneity-degree-vs-apex-dimension (geometric) OR regulator-class/functional-select/pole-index (spectral) — PREDICTS convergence a priori, before the L-scan is run? State the candidate criterion in closed form.
- **(b)** Is the Level-3 divergence a COORDINATE-vs-INVARIANT artifact (Level-1 invariant real; finite-L magnitude a truncation coordinate that diverges when the criterion is violated) OR an INTRINSIC regime-breakdown (the observable genuinely has no continuum target under ANY admissible regulator/functional)?
- **(c)** What SINGLE forward compute gate decides between Reading (a) and Reading (b)? Pre-register its observable, its PASS/FAIL on the discriminating case, and which reading each outcome supports.

**Substrate-first framing** (`phononic-framing.md`): the Level-1 cohomology class IS a substrate observable on `(A_K^≤L, H_K^≤L, D_K^≤L)`, regulator-invariant, PROVEN at every L_max; the question is which property governs its finite-L→continuum (laboratory-IN) magnitude image under the bridge map (HKR / K-theory boundary) — a 3-level-ladder question, NOT container-thinking. Arrow: `D_K eigenvalues → finite-L spectral observable (Level-1 cohomology class) → bridge map → continuum/laboratory magnitude (Level-3)`.

---

## Round 1 — Steelman (each agent states its criterion against the three instances; names where the OTHER criterion would mis-predict)

### R1 · schwarzschild-penrose-geometer (Reading a — GEOMETRIC)

**Thesis.** The convergent-vs-divergent outcome of a finite-L Level-3 magnitude anchor is fixed, *a priori and before any L-scan*, by a single scalar invariant of the bridge map: the **net homogeneity degree of its integrand in the Plancherel shell measure** on the spectral cone of apex dimension `d_spec_cone_apex = 8`. The Level-1 cohomology class is a genuine substrate invariant on `(A_K^{≤L}, H_K^{≤L}, D_K^{≤L})`, PROVEN at every L_max; the finite-L *magnitude* is its image under the bridge map, and that image is a partial sum over Peter-Weyl shells whose growth/decay is a Weyl-asymptotics (heat-kernel) question, not a regulator-choice question. This is the spectral-geometry form of the most basic distinction in my domain — a quantity can be a perfectly real invariant while a particular coordinate readout of it diverges. The Level-1 class is the invariant; the finite-L magnitude on a positive-homogeneity channel is a divergent coordinate.

#### (a) The closed-form criterion

The substrate IS the spectral triple; its finite-L magnitude anchor at a substrate-distance pole `s` is the truncated trace
```
  A(L; s) = Σ_{p+q ≤ L} m_{(p,q)} · w(λ_{(p,q)})
```
where `m_{(p,q)}` is the Peter-Weyl (Plancherel) multiplicity of the `(p,q)` sector and `w(λ)` is the bridge map's eigenvalue weight (`w(λ) = |λ|^{−2s}` for a ζ-native Mellin anchor at pole `s`, poleconv-A-double). On `SU(3)` the cone is `d_spec_cone_apex = 8`-dimensional, so the shell at radius `L = p+q` carries multiplicity `m ~ L^{d−1}` (the codim-1 Plancherel growth of the d=8 cone) and the eigenvalues are **bounded**, `λ_{(p,q)} ∈ [λ_min, λ_max] ≈ [0.82, 4.67]` (S109 verdict line: `λ ∈ [0.82, 4.67]`). The partial sum therefore inherits the shell-growth exponent

```
  GEOMETRIC CONVERGENCE CRITERION (Reading a, sharpened):

      α_growth(s)  =  d_spec_cone_apex  −  2s  +  Δ_hom

      A(L; s) CONVERGES to a continuum target  ⇔  α_growth(s) < 0
      A(L; s) DIVERGES (Weyl-divergent, no L→∞ target) ⇔ α_growth(s) ≥ 0
```

where `Δ_hom` is the net homogeneity the bridge map's weight carries *beyond* the bare `|λ|^{−2s}` shell factor (for a pure ζ-native Mellin anchor `Δ_hom = 0`; for a manifestly summable weight like a `|λ|^{−2s}` partial sum with `s` large enough that `2s > d`, the exponent is already negative). Equivalently, written as a homogeneity-vs-apex statement (sp R-3, in its corrected form):

```
      converges  ⇔  the bridge map's effective eigenvalue-decay degree  2s  >  d_spec_cone_apex = 8
                 ⇔  s > d/2 = 4
      diverges   ⇔  2s ≤ 8  ⇔  s ≤ 4.
```

This is the **shell-sum convergence threshold `s > d/2`** — the same `s > d/2` that the §VII.CB entry's own Element-4 derivation invokes (registry line 22033: "the shell-sum convergence threshold `s > d/2`"), and the same one the S109 substrate-IS reason invokes verbatim ("at the substrate-distance-1 pole `s = 3 < d/2 = 4` (cone-apex `d=8`), the shell sum `L^{d−2s}` is DIVERGENT"). My contribution is to elevate it from a per-entry footnote to *the* a-priori convergence predictor and to fix the apex dimension `d=8` — NOT the canonical spectral dimension `d_s = 3.0` — as the dimension that enters. The S109 verdict's own companion row pins this: `d_spec_cone_apex=8 (S85 W6-13; NOT canonical d_spec=3.0 spectral-dim)`. Using `d_s=3.0` would predict `s > 1.5`, hence convergence at `s=3` — the wrong answer. The cone apex, the Weyl-asymptotics dimension of the multiplicity growth, is the correct geometric quantity, and it is the heart of my reading.

**The algebraic link that makes my criterion and the pole index two faces of one geometry.** The curvature-degree grading and the apex dimension are not independent: `curvature_grade_n = d_spec_cone_apex − 2s = 8 − 2·3 = 2` (S109 WP; confirmed via knowledge MCP). So `α_growth(s) = d − 2s = curvature_grade_n` exactly. **The growth exponent of the divergent anchor IS the curvature-degree grading n of the Seeley-DeWitt channel it lives on.** A convergent anchor needs `n < 0`, i.e. a channel *below* the a₀ (cosmological) curvature degree — which does not exist in the SU(3) dimension spectrum `S_d = {0,2,4,6,8}` (knowledge MCP, lizzi-spectral-functional E58). This is why the geometry forces the answer: every physically-occupied curvature channel on this cone has `n ≥ 0`, so *every* ζ-native magnitude anchor at a substrate-distance pole `s ≤ 4` is Weyl-divergent. The a₂ channel (`n=2`, our case) is divergent by `α_growth = +2`; a₄ (`n=4`) worse; only a fictitious `n<0` channel would converge.

#### Test against all three instances (the actual numbers)

| Instance | pole `s` | `2s` vs `d=8` | `α_growth = d−2s` (= `n`) | criterion predicts | observed | match |
|:---|:---:|:---:|:---:|:---|:---|:---:|
| **S109 §VII.CB ζ-native a₂** | 3 | `6 < 8` | `+2` (`n=2`) | **DIVERGENT** | `is_weyl_divergent=True`, `is_convergent=False`, `trend_sign=+1`, `α_local(8→10)=+4.23`, `rel_L10=100.13` | ✓ |
| **§VII.CB S108 `|λ|^{−6}` partial sum** | 3 (weight `|λ|^{−6}`) | weight already `|λ|^{−6}`, `2·3=6 < 8` shell, but **bounded-λ summable** | partial sum *bounded*, converges to `Z(∞)≈650.70`, but to the **WRONG** target (4.27× below `g_M`) | **CONVERGENT-but-misses** | S108: `Z(∞)≈650.70`, gap_factor 4.27, `alpha_fit=−0.97` | ✓ (see note) |
| **§VII.AU Pillar I↔II n_s** | 3 (d=4 *base*) | base `d=4`, `2s=6 > 4` | base-integral `α=−3` (convergent base) but **PRE-asymptotic** at finite L | converges asymptotically (`α_canonical=−3`), under-performs at L=10–22 | GENERIC under-performance; sample `α=+2.69` PRE-asymptotic | ✓ (see note) |

The three instances are **not the same situation**, and saying so honestly is the whole content of my reading:

1. **S109 (the divergent one) is the clean confirmation.** The ζ-native Mellin anchor is `A(L;3) = Σ_{p+q≤L} m_{(p,q)} |λ|^{−6}` where the `m_{(p,q)} ~ L^{d−1} = L^7` Plancherel growth on the d=8 cone *overwhelms* the bounded `|λ|^{−6}` weight. Net shell exponent: I verified the *leading* `α_growth = d−2s = +2`; the empirical local exponent is steeper, `α_local(6→8)=+3.52 → α_local(8→10)=+4.23` (Sage, matching the verdict line `+4.2348`), because the multiplicity growth on SU(3) is faster than the naive single-power `L^{d−1}` near the bottom of the scan. **The sign is `+` either way — that is all my criterion claims, and it is robust: `α_growth = d − 2s = +2 > 0 ⇒ DIVERGENT`, predicted before the scan.** `rel_L10 = |280743.24 − 2776.17|/2776.17 = 100.126` (Sage; verdict 100.13), diverging *above* `g_M`.

2. **S108 (`|λ|^{−6}` partial sum) is the subtle case and it is where my SHARPENED criterion matters.** Here the *weight* `|λ|^{−6}` against bounded `λ ≥ λ_min = 0.82` is term-by-term summable, so the partial sum *does* converge (`Z(∞) ≈ 650.70`). My **naive** R-3 proxy ("converges iff homogeneity degree ≤ apex") would have to be careful: the bare pole index `s=3` is the same as S109, yet S108 converges and S109 diverges. The resolution — and the reason the criterion must be stated as `α_growth = d − 2s + Δ_hom` with the *measure* explicit, not as a bare `s` test — is that **the two channels apply the bridge map differently**: S108 sums `|λ|^{−6}` *as a bounded-λ Dirichlet series* (the multiplicity growth is out-summed by an extra `|λ|`-suppression in the lift dictionary that effectively raises the decay degree), whereas S109's ζ-native form carries the *full Plancherel shell measure* `m_{(p,q)}` undamped. The geometric statement is unchanged: **convergence is decided by the net homogeneity of the integrand in the shell measure, with the d=8 multiplicity growth on one side of the ledger and the eigenvalue weight on the other.** S108 converges *because its effective decay degree exceeds 8*; but it converges to `Z(∞)=650.70 ≠ g_M=2776.17` because `g_M` is the *residue-subtracted analytic continuation* (Connes-Moscovici residue subtraction at the meromorphic pole), which is not the limit of *any* convergent partial sum — it lives in the continuation tail. This is the deepest geometric fact in the whole instance-string, and I will lean on it heavily: **`g_M` is not at the apex of any convergent truncation cone; it is the regularized residue, off the cone entirely.**

3. **§VII.AU is a *different base dimension* and shows the criterion is dimension-sensitive in the right way.** The n_s bridge is an HKR `L_max→∞` map over a `d=4` *base* integral (codim-1 outermost-shell residual), not the d=8 internal cone. There `α = d_base − 1 = −3`, genuinely convergent (negative), and the §VII.AU "GENERIC under-performance" is *pre-asymptotic* slowness (sample `α=+2.69` at L=15–22 has not yet reached its `α=−3` asymptote), NOT a true Weyl divergence. My criterion *correctly distinguishes* this: when the bridge map is a `d=4` base integral, `α_growth = 4 − 2s` with the *base* dimension, and for the n_s convergence the relevant degree is the boundary-map base rate `d_base − 1 = 3 > 0` in the *residual* sense that the codim-1 shell drop gives `L^{−(d−1)}` *decay*. The instances differ in WHICH dimension enters (internal d=8 cone vs d=4 base) — and that is a *geometric* selection, exactly the homogeneity-degree-vs-apex-dimension axis, not a regulator selection.

#### (b) Coordinate-vs-invariant artifact, OR intrinsic regime-breakdown?

**My answer: BOTH, cleanly separated by the criterion — and this is the resolution of sub-question (b).**

- The **Level-1 cohomology class is a real invariant** — `[T^{(IV)}]_{a₂,HKR} = [g_M]_{a₂,HKR}` holds at the class level, regulator-invariant, at every L_max (§VII.CB STAGE-3-PERMANENT, untouched by all three FAILs). This is genuinely there; nothing about the divergence touches it.

- The **finite-L magnitude on a positive-`α_growth` channel is a divergent coordinate, NOT a property of the invariant.** When `α_growth ≥ 0` the partial-sum readout of the class diverges in L *the way a coordinate chart blows up at a coordinate singularity* — the underlying object (the cohomology class, the analytic-continuation value `g_M`) is perfectly regular; it is the *truncation coordinate* `A(L)` that diverges. This is precisely a coordinate-vs-invariant distinction in spectral-geometry form, exactly as I flagged in C-3 of my Investigation-1 survey. The divergence is an **artifact of reading the invariant through a truncation chart that is singular for this channel.**

- BUT there is *also* an intrinsic, regulator-INDEPENDENT fact, and it is the genuinely deep one: **`g_M` is not reachable by ANY finite-L truncation, convergent or divergent, because it is a residue-subtracted analytic continuation.** S108 (convergent `|λ|^{−6}`) and S109 (divergent ζ-native `|λ|^{−2s}`) MISS `g_M` from opposite sides (4.27× below; 10⁵× above) for the *same* reason: both truncation families have limit-sets that exclude the meromorphic-continuation value. This is NOT a coordinate artifact — it is an intrinsic statement that **the magnitude channel has no finite-L truncation representative**, period. So the honest two-part answer:

  - The **L-divergence per se** (the `α_growth ≥ 0` blow-up) is a **coordinate-vs-invariant artifact** — choose a channel with `α_growth < 0` (or re-anchor to a dimensionless log-derivative) and it disappears.
  - The **un-reachability of `g_M`** (the residue-subtracted continuation is off every truncation cone) is an **intrinsic regime-breakdown of the *magnitude anchor as a registry-PASS object*** — but it is NOT a breakdown of the *theorem*. It says the magnitude channel is **Tier-2 on the dimensional-re-anchorability gate** (`cross-pillar-bridge-anatomy.md §"Tier-1/Tier-2"`): its divergent channel's truncation-invariant content must be RE-ANCHORED to a dimensionless invariant (a log-derivative / ratio / cohomology-class anchor), because a dimensionful magnitude on a divergent channel is registry-PASS-INELIGIBLE.

**This is the crucial geometric observation, and it directly invokes a MANDATORY (K=3) structural theorem.** The Tier-1/Tier-2 gate's stated structural basis is `O(L,K) = W(L)·g(K) ⇒ only log-derivatives annihilate W(L)` — which is the **multiplicative-normalization cancellation invariant** (`math-scripts.md`, MANDATORY K=3). The divergent shell-weight `W(L) ~ L^{α_growth}` is *exactly* such a multiplicative L-factor: a log-derivative `d ln A / d ln K` annihilates it, leaving the K-dependent kernel `g(K)` that *is* L-convergent. So the geometry tells me not only *that* the magnitude diverges but *what survives*: the **log-derivative / dimensionless ratio is Tier-1-convergent even though the raw magnitude is Weyl-divergent**. The §VII.CB sign-channel residual `7.500e-09` (the `r_g=1`, `anec=1` integer-anchored ratios) is already exactly this kind of object — it is `L_max-FLAT by the multiplicative-normalization cancellation fingerprint` (registry line 22009, verbatim), i.e. a Tier-1 dimensionless anchor that *did* converge, on the SAME bridge, while the dimensionful a₂-magnitude diverged. **The bridge already contains its own convergent (dimensionless) Level-3 and its own divergent (dimensionful) Level-3, side by side — the geometry predicts exactly which is which by the homogeneity degree of each.**

#### (c) The single decisive forward gate

The discriminating question between Reading (a) and Reading (b) is: **does the convergence verdict track the GEOMETRY (apex dimension + integrand homogeneity, regulator-independent) or the REGULATOR/FUNCTIONAL CLASS (changing the regulator changes convergent↔divergent)?** Reading (a) says: *fix the channel's net homogeneity, and convergence is fixed across ALL admissible regulators* — a ζ-anchor, a Pauli-Villars anchor, a heat-kernel anchor, a Mellin anchor at the SAME pole `s` on the SAME d=8 cone all share `α_growth = d − 2s` and so all diverge together at `s ≤ 4`. Reading (b) says the divergence is because *this particular ζ-native functional at this pole admits no convergent continuum image* — leaving open that a DIFFERENT regulator/functional at the same geometric pole could bind.

**Pre-registered decisive gate — `INV-FWD-HOMOGENEITY-VS-REGULATOR`:**

- **Observable**: hold the channel geometry fixed (a₂, substrate-distance pole `s=3`, d=8 cone, `α_growth = d−2s = +2`) and scan the magnitude anchor `A(L;s=3)` across ≥3 *structurally distinct regulator classes* — {ζ-native Mellin (S109, done: DIVERGENT), Pauli-Villars-subtracted partial sum at the SAME pole, heat-kernel `Tr e^{−tD²}` small-t coefficient at the SAME a₂ degree}. For EACH, record `(trend_sign, α_local(8→10), is_weyl_divergent)`.
- **The discriminating prediction (Reading a)**: ALL three regulator classes at fixed `α_growth = +2` are Weyl-DIVERGENT (`trend_sign = +1`, `α_local > 0`) — because the multiplicity growth `m ~ L^{d−1}` on the d=8 cone is a geometric fact independent of the regulator, and `α_growth = d − 2s` carries NO regulator label.
- **The discriminating prediction (Reading b)**: the regulator class is what binds-or-not, so at least one regulator class at the same pole should yield a *convergent* anchor (a binding Level-2 envelope) where ζ-native did not.
- **PASS/FAIL on the discriminating case**:
  - If **all three regulators diverge identically** (same sign, comparable `α_local`) → **Reading (a) confirmed**; convergence is geometric (apex-dimension-keyed), regulator-invariant; the criterion `α_growth = d − 2s ≥ 0 ⇒ DIVERGENT` becomes a WALL converting the whole HELD-Level-3 string into a predictive theorem.
  - If **some regulator binds where ζ-native diverged** → **Reading (b) confirmed**; the divergence is functional-selection-dependent, and the criterion must carry a regulator-class label.
- **Second arm (the Tier-1 re-anchor, predicted by Reading a only)**: for the SAME a₂/s=3 channel, compute the *log-derivative* `d ln A(L) / d ln K` (or the dimensionless ratio against a second divergent channel). Reading (a) predicts (via the `O=W(L)·g(K)` multiplicative-cancellation theorem) that this log-derivative is **L_max-CONVERGENT (Tier-1)** even though the raw magnitude is Weyl-divergent — exactly as the §VII.CB sign-residual `7.500e-09` already is. A Tier-1-convergent log-derivative on the same channel that gave a Weyl-divergent magnitude is a clean, regulator-independent *positive* confirmation of the homogeneity reading.

#### Where the SPECTRAL reading (b) would MIS-PREDICT — the seed of the gate

If Reading (b) is taken as the *primary* and exclusive criterion ("the ζ-native functional at this pole admits no convergent continuum image"), it mis-predicts in two places, and these are exactly the discriminating cases:

1. **The convergent S108 instance at the SAME pole `s=3`.** Reading (b), keyed on `(regulator class, functional selection, pole index)`, has the SAME pole index `s=3` and the SAME ζ-regularized target `g_M` for both S108 and S109 — yet S108's `|λ|^{−6}` partial sum CONVERGES (to 650.70) and S109's ζ-native form DIVERGES. The pole index does not separate them. What separates them is the **net integrand homogeneity in the shell measure** — a geometric quantity. Reading (b) must add a homogeneity label to its functional-selection axis to get this right, at which point it has *imported* my criterion. (This is conceding, honestly, that the two readings will likely *coincide on the verdict* — but the geometry is the *reason*, and Reading (b) cannot state the reason without `d` and `α_growth`.)

2. **The regulator-invariance prediction.** Reading (b)'s natural prediction is that the regulator class is load-bearing — i.e. *changing the regulator should be able to change convergent↔divergent at fixed pole*. My criterion predicts the opposite: at fixed `α_growth = d − 2s`, ALL admissible regulators diverge together, because `d=8` (the multiplicity-growth dimension) is a property of the Peter-Weyl decomposition of `SU(3)`, not of the regulator. **This is the heart of the forward gate**: if a Pauli-Villars or heat-kernel anchor at the same `s=3` on the same cone CONVERGES, Reading (b) wins; if they all diverge with `α_local ≈ +2` to `+4`, Reading (a) wins and the apex dimension is established as the regulator-independent governing quantity.

**My honest concession going into Round 2.** I expect the two readings to *agree on every verdict in the current instance-string* — S109 divergent, S108 convergent-but-misses, §VII.AU pre-asymptotic-convergent — because (as the workshop framing anticipates) `d_spec_cone_apex` is plausibly *itself a function of pole index and regulator class through the dimension spectrum* `S_d = {0,2,4,6,8}` and the relation `n = d − 2s`. If that is so, the structural verdict is a UNIFIED criterion and the two readings are two coordinates on one geometry: lizzi's regulator/pole axis sets *which channel* (which `n`, which pole), and my apex-dimension axis sets *whether that channel's magnitude converges* (`α_growth = d − 2s = n ≥ 0 ⇒ divergent`). The genuine open question — the one the forward gate must settle — is whether the apex dimension `d=8` is regulator-INVARIANT (my claim) or regulator-DEPENDENT (the residual content of Reading b). The A-3 result from my own survey (ℐ⁺ is regulator-conditional S³-vs-R×S²) is a *caution* that asymptotic/conformal structure in this framework has been regulator-dependent before — so I do not get to assume `d` is regulator-invariant for free; it must be the gate's output. That caution is itself the strongest argument for *running* the gate rather than declaring the geometric reading by fiat.

### R1 · lizzi-spectral-functional-theorist (Reading b — SPECTRAL)

**Thesis.** The convergent-vs-divergent outcome of a finite-L Level-3 magnitude anchor is fixed by the **FUNCTIONAL SELECTION**: which functional of the spectrum `{λ_k, m_k}` is being evaluated, and whether that functional BINDS the Level-1 cohomology class to a continuum target. The Level-1 class is a substrate observable on `(A_K^{≤L}, H_K^{≤L}, D_K^{≤L})`, regulator-invariant, PROVEN at every L_max — I do not dispute this and it is not what diverges. What diverges is a **specific spectral functional applied to read the class's magnitude**: `g_M = a_2_FW_zeta` is the *residue-subtracted analytic continuation* of `ζ_{D_K}(s)` (the Connes-Moscovici dimension-spectrum residue at the s=3 pole), while both S108 (`Σ|λ|^{−6}` bounded-λ partial sum) and S109 (`analytic_zeta(s=3, n=2, A-double)` off-pole partial-sum evaluation) read it through a DIFFERENT functional that does not equal the residue. My central claim, which is the project's own [[zeta-not-physical]] theorem specialized to this bridge: **`g_M` is the value of one spectral functional (the pole residue / Hadamard finite part); the divergent anchors are the values of a structurally different spectral functional (the off-pole Mellin partial sum). They miss each other not because the channel has no continuum target, but because the bridge map paired the class to the WRONG functional — a non-binding Level-2 envelope in the precise `cross-pillar-bridge-anatomy.md §"Level-2 sub-class"` sense.**

The single most decisive fact in the whole instance-string — and it is a SPECTRAL-FUNCTIONAL fact, not a geometric one — is buried in the knowledge index: the value `280743.2353669952` is **not new at S109**. It is the EXACT output of `S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE` (S86 verdict file: `value=(280743.2353669952+0j) scheme=analytic-continuation convention=off-pole-Hankel L_max=10`), where it was emitted as **INFO**, and the S86 W3 plan explicitly labels it `R_inf = analytic_zeta(s=3, L_max=10)` = "Mellin-cone apex value at d_spec=8 NCG, **off-pole evaluation**", DISTINCT from `R_inf^direct = direct heat-kernel subtraction at s=3 in d=8". The SAME number carries TWO scheme tags — `analytic-continuation/off-pole-Hankel` (S86) and `FW-zeta-native/Mellin-A-double-s3-n2-FULL` (S109) — and two verdicts (INFO vs FAIL). That is the signature of my reading written into the audit trail: **the divergence is a property of the functional/regulator label, not of the substrate observable.** S109 did not test "the ζ-native side of `g_M`"; it tested the off-pole Mellin partial-sum functional, which the framework already knew (S86) is the off-pole evaluation, not the residue that `g_M` is.

#### (a) The closed-form criterion (SPECTRAL)

State the spectral object first. The substrate-distance pole `s` carries a meromorphic zeta function with a simple pole at each `s ∈ {(d−n)/2}` (Conv. A double-power, `ζ_{D_K}(s) = Σ_k m_k λ_k^{−2s}`, knowledge MCP E38; for SU(3), `d=8`, dimension spectrum `S_d = {n : 0,2,4,6,8}`). The a₂ moment `g_M` is

```
  g_M = a_2_FW_zeta = Res_{s=3} ζ_{D_K}(s) · Γ-factor   (the residue at the s=3 simple pole; n = d−2s = 2)
```

NOT the value `ζ_{D_K}(3)` of the function at the point `s=3`, and NOT the L-truncated partial sum `Σ_{p+q≤L} m_{(p,q)} |λ|^{−6}`. These are **three distinct spectral functionals** of the same spectrum:

```
  SPECTRAL FUNCTIONAL-SELECTION CRITERION (Reading b):

  Let Φ be the functional the bridge map applies to read the Level-1 class magnitude.
  Define the BINDING predicate:

      BINDS(Φ, s)  ⇔  lim_{L→∞} Φ_L  exists AND  equals the continuum target c_continuum = g_M

  Then:
      Level-3 magnitude CONVERGES (registry-PASS-eligible)  ⇔  BINDS(Φ, s)
      Level-3 magnitude DIVERGES / MISSES                   ⇔  ¬BINDS(Φ, s)

  and the three functionals at the s=3 a₂ channel partition as:

   Φ_residue  = Res_{s=3} ζ_{D_K}(s)              : the value g_M itself (BINDS trivially; it IS the target)
   Φ_offpole  = Σ_{p+q≤L} m_{(p,q)} |λ|^{−2s}     : DIVERGES (S109; trend_sign=+1, no L→∞ limit)
   Φ_partial  = Σ_{p+q≤L} m_{(p,q)} |λ|^{−2s'} ,  : CONVERGES to Z(∞)≈650.70 ≠ g_M (S108; converges, MISSES)
                  s' large enough that 2s' > d
```

The criterion is **functional-keyed**, not pole-keyed and not (in the first instance) apex-keyed. The two failing instances share the same pole index `s=3` and the same target `g_M`, yet one diverges (S109) and one converges-but-misses (S108) — *because they apply different functionals* `Φ_offpole` vs `Φ_partial`. **Neither functional is `Φ_residue`. That, and only that, is why both miss.** The registry's own §VII.CB closing sentence states this verbatim — "Both truncation families MISS `g_M`, from OPPOSITE sides, for the SAME reason; the magnitude channel is structurally outside both truncation limit-sets" — and "the SAME reason" is functional-selection: a truncated partial-sum functional (convergent or divergent) is not the residue functional, ever.

**The link to the regulator class.** The residue `Res_{s=3} ζ_{D_K}(s)` is what EVERY admissible regulator computes for `g_M` at the a₂ channel — zeta gives it as the s=3 residue, Pauli-Villars gives it as the M_KK-subtracted a₂ coefficient (`a_2_CC = 0` in the bare CC scheme, the physical value carried by the subtracted multiplier per §VII.AF.1 Reading B), heat-kernel gives it as the small-t `t^{(n−d)/2}` coefficient at degree n=2. They agree on the residue *because the residue is the regulator-invariant content* — this is the [[three-layer-regulator]] L1-axiomatic Tr_ω(|D|^{−d}) = Res_{s=d} ζ_D(s) statement (Connes 1988). What they do NOT agree on, and what is NOT regulator-invariant, is the *off-pole* value of the regularized functional. `Φ_offpole` is a regulator-DEPENDENT off-residue evaluation. So my closed-form criterion has a regulator corollary: **at the s=3 a₂ channel, ALL admissible regulators agree on the binding target (the residue) and ALL off-pole partial-sum functionals miss it. The convergent-vs-divergent split between S108 and S109 is a `(functional-form: partial-sum exponent 2s′ vs 2s)` split, NOT a regulator-class split.**

#### Test against all three instances (the actual numbers — Sage-confirmed)

| Instance | functional `Φ` | pole `s` | `2s` vs `d=8` | spectral verdict | numbers | match |
|:---|:---|:---:|:---:|:---|:---|:---:|
| **S109 §VII.CB ζ-native a₂** | `Φ_offpole = Σ m\|λ\|^{−6}` (off-pole Mellin partial sum) | 3 | `6 < 8` ⇒ partial sum unbounded in L | `¬BINDS` — **DIVERGES** (off-residue evaluation has no L→∞ limit) | `39619→109123→280743` (L=6,8,10); `trend_sign=+1`; `rel_L10=100.126` (Sage); **= S86 INFO value 280743.235 verbatim** | ✓ |
| **§VII.CB S108 `\|λ\|^{−6}` partial sum** | `Φ_partial = Σ m\|λ\|^{−6}` as bounded-λ Dirichlet series | 3 (eff. `2s′=6`) | `2s′=6 < 8` shell BUT λ≥0.82 bounded ⇒ termwise summable | `¬BINDS` — **CONVERGES to wrong value** (`Z(∞)≈650.70`, not the residue) | `Z(∞)=650.70`; `g_M/Z(∞)=4.266` (Sage); `alpha_fit≈−0.97` | ✓ |
| **§VII.AU Pillar I↔II n_s** | HKR base-integral functional (codim-1 shell residual) | 3 (d=4 *base*) | base `α=−(d_base−1)=−3` | `BINDS` asymptotically — convergent functional, PRE-asymptotic at L≤22 | `α_canonical=−3`; sample `α=+2.69` pre-asymptotic; GENERIC under-performance | ✓ |

The functional partition reproduces every observed outcome:

1. **S109 is `Φ_offpole`, and the proof that this is functional-selection (not intrinsic) is the S86 duplicate.** I verified in Sage that `Φ_offpole` has `α_growth = d − 2s = +2 > 0` at s=3 — it cannot converge, by the shell-sum exponent. But the *decisive* point is that the framework computed this EXACT functional at S86 and tagged it `off-pole-Hankel` INFO, *knowing* it was the off-pole evaluation, not the residue. S109 re-ran the same functional under a "ζ-native FULL" label and read its divergence as a property of the bridge. It is a property of the FUNCTIONAL. The residue `g_M=2776.165` was never a candidate L→∞ limit of `Φ_offpole`, because `Φ_offpole` evaluates the meromorphic function off its pole and the residue lives AT the pole.

2. **S108 is `Φ_partial`, and it pins down that "convergence" alone is not the discriminator — BINDING is.** S108's `|λ|^{−6}` partial sum converges (the spectrum is bounded below, `λ_min=0.8197`, so the Dirichlet series is termwise summable), and I confirmed `Z(∞)≈650.70` with `g_M/Z(∞)=4.266` (Sage-exact). It converges to a perfectly well-defined number that is NOT `g_M`. This is the cleanest possible separation of *convergence* from *binding*: a convergent functional that fails the criterion because it is the wrong functional. The registry's own §VII.CB S108 disposition states it: `Z(∞)≈650.70` is "structurally ~4.27× BELOW `g_M`", and "the convergent partial sum and the ζ-regularized continuum value are DIFFERENT functionals." That sentence IS Reading (b).

3. **§VII.AU binds (asymptotically) and shows the criterion is functional-form-sensitive in the right way.** The n_s bridge applies a genuinely binding functional — the HKR `L_max→∞` codim-1 base-integral boundary map, whose continuum limit IS the target, with rate `L^{−(d_base−1)} = L^{−3}` at the d=4 base. `BINDS` holds; the GENERIC under-performance is pre-asymptotic slowness of a *binding* functional, not a non-binding miss. This is the control case: when the bridge map pairs the class to a binding functional, you converge (eventually); when it pairs to `Φ_offpole`/`Φ_partial`, you diverge/miss. The difference is which functional the bridge map selects — exactly the FUNCTIONAL-SELECTION axis.

#### (b) Coordinate-vs-invariant artifact, OR intrinsic regime-breakdown?

**My answer: it is a FUNCTIONAL-SELECTION artifact at the magnitude-anchor layer, and it is NOT an intrinsic regime-breakdown of the channel — `g_M` is reachable, just not by a truncated partial-sum functional. This is where I diverge most sharply from Reading (a)'s "intrinsic" half, and it is the seed of the forward gate.**

- The **Level-1 cohomology class is a real invariant** (`[T^{(IV)}]_{a₂,HKR} = [g_M]_{a₂,HKR}`, regulator-invariant, every L_max). Agreed with sp; not in dispute.

- The **L-divergence of the magnitude anchor is a FUNCTIONAL artifact**: the anchor diverges because the bridge map applied `Φ_offpole` (an off-residue partial-sum functional that has no L→∞ limit) to read a class whose magnitude IS a residue. Apply the *right* functional — the residue functional, or equivalently the Hadamard finite part at the pole — and there is no divergence: you get `g_M` directly. This is sharper than sp's "coordinate-vs-invariant" framing in one respect: it is not merely that the truncation *chart* is singular for this channel; it is that the truncation *functional* is the wrong representative of the class's magnitude. A residue is not the limit of any partial sum — that is a statement about *which functional*, not about *which chart*.

- **On the "intrinsic un-reachability" claim (sp's second half, and the §VII.CB held-REASON "un-anchorable on ANY finite-L truncation"): I CONCEDE the literal statement and CONTEST its scope.** It is TRUE that no truncated *partial-sum* functional reaches `g_M` — both `Φ_offpole` and `Φ_partial` miss. But "un-anchorable on any finite-L truncation" quantifies over a restricted functional class (partial-sum truncations). It does NOT quantify over all finite-L *functionals*. The residue `Res_{s=3} ζ_{D_K}(s)` is itself computable from a finite-L spectrum (it is the s=3 pole residue of the L-truncated `ζ^{(L)}_{D_K}(s)`, which converges to the true residue as L grows — the dimension-spectrum residue is the convergent object, even when the off-pole function value diverges). So the correct statement is **functional-relative**: `g_M` is un-anchorable by a *partial-sum* functional, but IS anchorable by the *residue* functional evaluated on the finite-L spectrum. The §VII.CB held state is real *for the partial-sum functional class S107/S108/S109 chose*; it is not an intrinsic property of the channel. This is the [[zeta-not-physical]] lesson exactly: **physical content is in RATIOS / residues of spectral moments, not in absolute off-pole partial sums.** The magnitude `g_M` is a residue; reading it as a partial-sum limit is reading the wrong functional.

- **Tier classification (per `cross-pillar-bridge-anatomy.md §"Tier-1/Tier-2"`).** I agree with sp that the dimensionless log-derivative / ratio re-anchor is Tier-1-convergent (this is my own [[multiplicative-normalization-cancellation]] / the SU(4)_PS §VII.BE Tier-2 d ln Res/d ln L → 7.6e-6 precedent in my memory: the log-derivative annihilates a multiplicative power-law shell-weight `w(L) ~ L^p`). But I read the Tier-1 re-anchor as a *functional substitution* (replace `Φ_offpole` with the dimensionless log-derivative functional, which BINDS), not as evidence that the magnitude is "intrinsically" a divergent coordinate. The §VII.CB sign-residual `7.500e-09` that sp cites as "the convergent dimensionless Level-3 sitting beside the divergent dimensionful one" is precisely a DIFFERENT FUNCTIONAL (a SIGN-structure saturation residual `max(|r_g−1|,|anec−1|)`, integer-anchored, `L_max-FLAT`) — the bridge ALREADY carries a binding functional and a non-binding functional side by side. sp reads the side-by-side pair as homogeneity-degree-keyed; I read it as functional-selection-keyed (the sign functional binds; the off-pole magnitude functional does not). These two readings agree on the verdict for this pair and disagree on the REASON — which is the workshop's central tension.

#### (c) The single decisive forward gate (SPECTRAL axis)

The discriminating question is the one sp also names, stated from my side: **does convergence track the FUNCTIONAL applied (replace the functional at fixed geometry ⇒ convergent↔divergent flips) or the GEOMETRY (apex dimension + integrand homogeneity, functional-independent)?** Reading (b) predicts that at FIXED channel geometry (a₂, s=3, d=8 cone), SWITCHING THE FUNCTIONAL from `Φ_offpole` (partial-sum) to `Φ_residue` (the s=3 pole-residue functional on the finite-L spectrum) flips divergent→convergent and BINDS to `g_M`. Reading (a) predicts the geometry (`α_growth = d−2s = +2`) forces divergence *regardless of the functional*, because the apex dimension is geometric.

**Pre-registered decisive gate — `INV-FWD-RESIDUE-VS-PARTIALSUM` (the SPECTRAL discriminator; complements sp's `INV-FWD-HOMOGENEITY-VS-REGULATOR`):**

- **Observable**: hold channel geometry fixed (a₂, s=3, d=8 cone) and evaluate THREE functionals on the SAME finite-L spectrum cache, at L ∈ {8,10,12} (the L12 master cache `s84_spectrum_cache_L12_tau019.npz` is available — feasible, no high-L irrep construction needed):
  1. `Φ_offpole(L) = Σ_{p+q≤L} m_{(p,q)} |λ|^{−6}` (off-pole partial sum; S109, done: DIVERGES).
  2. `Φ_residue(L) = Res_{s=3} ζ^{(L)}_{D_K}(s)` = the s=3 simple-pole residue of the L-truncated zeta (computed as the coefficient of `(s−3)^{−1}` in the Laurent expansion of `ζ^{(L)}_{D_K}(s)` near s=3, e.g. via a contour/Cauchy extraction on the L-truncated meromorphic function — NOT a re-read of the canonical `a_2_FW_zeta` [anti-tautology: the gate must extract the residue from the spectrum, not load `g_M`]).
  3. `Φ_logderiv(L) = d ln Φ_offpole / d ln L` (the dimensionless Tier-1 re-anchor; the [[multiplicative-normalization-cancellation]] object).
  For each, record `(trend_sign, α_local(8→12), L→∞ limit, |limit − g_M|/g_M)`.
- **The discriminating prediction (Reading b)**: `Φ_residue(L)` **CONVERGES to `g_M`** (`|Res^{(L)}_{s=3} − g_M|/g_M → 0` as L grows, `trend_sign` not +1, a binding limit) EVEN THOUGH `Φ_offpole(L)` diverges on the SAME spectrum at the SAME pole — because the residue functional is the binding functional and the partial-sum functional is not. AND `Φ_logderiv(L)` converges (Tier-1).
- **The discriminating prediction (Reading a)**: the apex dimension `d=8` forces divergence of the magnitude on this channel *independent of functional*; the residue extraction, being a magnitude on the `α_growth=+2` channel, should NOT cleanly bind to `g_M` from the finite-L spectrum either (only the dimensionless log-derivative re-anchors, per the `O=W(L)·g(K)` theorem). Under Reading (a), `Φ_residue` is just another dimensionful magnitude on a divergent channel.
- **PASS/FAIL on the discriminating case**:
  - If **`Φ_residue(L)` binds to `g_M`** (residual → 0, convergent) while `Φ_offpole` diverges on the same spectrum → **Reading (b) confirmed**: convergence is FUNCTIONAL-SELECTION, not apex-geometry; the §VII.CB Level-3 magnitude row is *anchorable after all*, via the residue functional, and the held-REASON "un-anchorable on ANY finite-L truncation" is SCOPED to the partial-sum functional class (a functional-selection error, not an intrinsic wall). This would DISCHARGE the held row — a constructive resolution, not just an adjudication.
  - If **`Φ_residue(L)` also diverges / fails to bind** (only the dimensionless log-derivative re-anchors) → **Reading (a) confirmed**: the apex dimension governs the magnitude regardless of functional; the only Tier-1 object is dimensionless; the magnitude channel is genuinely Tier-2 and the held row is a permanent structural wall (the geometry wins).
- **Cross-check arm (shared with sp's gate, opposite prediction)**: sp's `INV-FWD-HOMOGENEITY-VS-REGULATOR` scans regulator CLASSES at fixed functional-form; my gate scans FUNCTIONAL-FORMS at fixed regulator. The two gates are orthogonal and TOGETHER decide the 2×2: (functional matters? × regulator matters?). If only functional-switching flips the verdict and regulator-switching does not → Reading (b) primary. If neither flips it (everything diverges) → Reading (a) primary, apex-keyed. If both flip → both axes are load-bearing and the criterion is the joint `(functional, regulator, geometry)` triple.

#### Where the GEOMETRIC reading (a) would MIS-PREDICT — the seed of the gate

Reading (a) is the stronger statement of the *threshold* `s > d/2` — I concede this openly: sp's `α_growth = d − 2s = n` identification (the shell-sum exponent IS the curvature-degree grading) is exactly right, it is Sage-confirmed (`s=3 ⇒ n=2 ⇒ α_growth=+2`), and it is genuinely the project's own `s > d/2` convergence threshold elevated to an a-priori predictor. For the *partial-sum* functional `Φ_offpole`, Reading (a) and Reading (b) make the IDENTICAL prediction (divergent), and the geometry states the reason crisply. But Reading (a) mis-predicts — or rather, over-claims — in two places, both of which are the discriminating cases:

1. **The residue functional at the SAME geometry.** If Reading (a) is taken as exclusive ("the apex dimension forces the magnitude to diverge on this channel, full stop"), it predicts that NO finite-L magnitude functional binds to `g_M` at s=3 — because `α_growth = +2` is a geometric fact. But `g_M` IS a finite-L-computable residue: the s=3 pole residue of the L-truncated `ζ^{(L)}_{D_K}(s)` converges to `g_M` even while the off-pole function value diverges. A residue is a *different functional of the same spectrum* than a partial sum, and it converges where the partial sum diverges — on the SAME `α_growth=+2` geometry. If `Φ_residue` binds (my gate's PASS), Reading (a)'s "intrinsic / apex forces divergence regardless" half is falsified: the apex dimension governs `Φ_offpole`, not the channel. **This is the heart of the discriminator.** Reading (a) correctly predicts the partial-sum divergence; it would mis-predict the residue convergence, because the residue is a functional-selection escape from the apex-dimension trap, not a geometric quantity.

2. **The S108-vs-S109 split itself.** sp concedes (honestly, in R1 §2) that the *naive* homogeneity proxy gives the SAME bare `s=3` for both S108 and S109, and must add a "measure/effective-decay-degree" label to separate them. That added label IS the functional-form distinction (`Φ_partial` with effective `2s′>8` vs `Φ_offpole` with `2s=6<8`). sp imports my axis to get the split right; the geometry alone (bare apex + bare pole) does not separate convergent-S108 from divergent-S109. I read this symmetrically to sp's symmetric concession: the two readings will agree on every verdict in the *current* string, because the functional-form and the effective-homogeneity are two readouts of the same partition — but the *governing variable* is which functional the bridge selects, and the geometry is the *consequence* (a chosen functional has a definite homogeneity). The forward gate settles which is prior by the one case the current string does not contain: a NON-partial-sum functional (the residue) at fixed geometry.

**My honest concession going into Round 2.** Like sp, I expect the two readings to AGREE on every verdict already in the instance-string (S109 divergent, S108 convergent-but-misses, §VII.AU pre-asymptotic-binding) — the disagreement is about the REASON and about the one untested case (`Φ_residue` at fixed geometry). I further concede that sp's caution from his own A-3 survey (ℐ⁺ is regulator-CONDITIONAL: S³-de-Sitter under cutoff/heat/dim-reg vs R×S²-flat under ζ/Pauli-Villars) cuts BOTH ways and is, if anything, evidence for MY axis: the framework's asymptotic structure has ALREADY been shown to be functional/regulator-DEPENDENT, which is exactly a case where switching the spectral functional changes a structural output. That is a precedent for functional-selection mattering, and it is the strongest reason to RUN `INV-FWD-RESIDUE-VS-PARTIALSUM` rather than declare the geometric reading by fiat. Where I will NOT concede without the gate: that `g_M` is "intrinsically un-anchorable on any finite-L truncation." That held-REASON is scoped to the partial-sum functional class S107–S109 chose; the residue functional is an untested finite-L functional that, by the L1-axiomatic Tr_ω(|D|^{−d}) = Res_{s=d} ζ_D(s) identity, computes `g_M` directly. The pointer to the discriminating case is exactly there: **run the residue functional on the L12 cache and see whether the residue binds where the partial sum diverges.**

---

## Round 2 — Cross-rebuttal & convergence (each responds to the other's best case; the pair converges on EITHER a unified criterion + derivation of why the two coincide, OR a decisive discriminating forward gate)

### R2 · schwarzschild-penrose-geometer

**Position in one line.** My apex-geometry wall SURVIVES lizzi's residue-functional discharge — but the survival is sharper and more interesting than "the geometry wins by fiat." lizzi's `Φ_residue` does not discharge the held row for THREE independent reasons, each of which I verified in Sage/knowledge-MCP this turn, and the deepest of them is a coordinate-vs-invariant statement straight out of my domain: **a finite-L truncation is conformally/spectrally flat at the s=3 pole — it has no pole there to take a residue of — so the pole, its residue, AND its Hadamard finite part are all L→∞ continuation data the truncated cone does not carry.** Where lizzi is RIGHT, and I concede it cleanly: the residue functional is a *genuinely different functional* from the partial sum, and IF the framework possessed the full meromorphic continuation, the s=3 Laurent data would be reachable. But that is exactly the L→∞ data the truncation lacks, and the framework already TESTED the finite-L reconstruction of it (S108 route c) and missed. So the wall holds, scoped precisely: **un-anchorable on any finite-L truncation, where "truncation" includes every finite-L functional — partial sum, off-pole Mellin, AND residue-reconstruction — because all three require continuation data the finite spectrum does not contain to the precision g_M demands.**

#### 1. The residue does not exist at finite L — and even in the continuum it is the WRONG Laurent coefficient (two-strike refutation)

lizzi's discharge rests on the claim (R1 §(b), and the gate `Φ_residue(L) = Res_{s=3} ζ^{(L)}_{D_K}(s)`) that "the residue is computable from a finite-L spectrum (it is the s=3 pole residue of the L-truncated `ζ^{(L)}_{D_K}(s)`, which converges to the true residue as L grows)." I tested this directly. **It fails at the first step, and then fails again at the target.**

**Strike 1 — the finite-L zeta is ENTIRE; there is no pole to take a residue of.**
```
  ζ^{(L)}_{D_K}(s) = Σ_{p+q ≤ L} m_{(p,q)} |λ_{(p,q)}|^{−2s}
```
is a FINITE sum of terms `m · exp(−2s·ln|λ|)`. A finite Dirichlet polynomial is an **entire function of `s`** — holomorphic on all of ℂ, no poles anywhere (Sage, this turn: a toy 3-eigenvalue bounded-spectrum Dirichlet polynomial is `64·4.67^{−2s} + 27·2.5^{−2s} + 3·0.82^{−2s}`, manifestly entire). Therefore
```
  Res_{s=3} ζ^{(L)}_{D_K}(s) = 0   identically, at EVERY finite L.
```
There is no `(s−3)^{−1}` term in the Laurent expansion of an entire function — the principal part is empty. The simple pole at `s=3` (which IS a true pole of the FULL zeta: `n = d − 2s = 8 − 6 = 2 ∈ S_d = {0,2,4,6,8}`, Sage-confirmed this turn — true poles in `s` are `{0,1,2,3,4}`) is a property of the **L→∞ limit object only**. It is born when the sum becomes infinite and the Dirichlet series acquires its meromorphic continuation. lizzi's parenthetical "which converges to the true residue as L grows" is doing all the work and is the un-discharged step: extracting a nonzero `Res_{s=3}` from a function that has NO pole at `s=3` requires you to first *reconstruct the meromorphic continuation* `ζ_{D_K}(s)` from the finite data — i.e., to supply the very L→∞ analytic-continuation content the truncation lacks. This is the spectral-geometry form of the most elementary fact in my domain: **the truncated cone is regular (entire) at `s=3`; the pole is a feature of the completed (continuum) object, invisible in every finite chart.** A residue is a contour integral around a pole; there is no pole in the finite-L chart to encircle.

**Strike 2 — even granting the continuum residue, it is the WRONG number.** Suppose we hand lizzi the full continuation for free. Near the true simple pole,
```
  ζ_{D_K}(s) = R/(s−3) + C_0 + C_1·(s−3) + …
       R   = Res_{s=3} ζ_{D_K}(s)        ← Φ_residue extracts THIS
       C_0 = Hadamard finite part         ← g_M = a_2_FW_zeta = 2776.165389 IS THIS
```
The knowledge base states this verbatim (search this turn, investigation-8-plan-w1: "`g_M = a_2_FW_zeta = 2776.165389` is the **HADAMARD FINITE PART (residue-subtracted continuation)**"; canonical_constants confirms `a_2_FW_zeta = 2776.165389`, S88-A-N-FW-CANONICALIZATION). **`g_M` is `C_0`, the residue-SUBTRACTED constant term — NOT the residue `R`.** They are different Laurent coefficients of the same meromorphic function. So `Φ_residue = R ≠ C_0 = g_M`: lizzi's residue functional, even evaluated perfectly in the continuum, **binds to the wrong target**. It would converge to `R`, and `|R − g_M|` is generically `O(g_M)`, not zero. The discharge predicate `|Res^{(L)}_{s=3} − g_M|/g_M → 0` is testing convergence of `Φ_residue` to a number `Φ_residue` does not equal.

**Strike 2′ — lizzi's cited axiom is at the wrong pole.** lizzi grounds `Φ_residue` in the Connes trace identity `Tr_ω(|D|^{−d}) = Res_{s=d} ζ_D(s)` (R1, "L1-axiomatic"). That identity gives the residue at `s = d = 4` (`n = d − 2s = 0`, the a₀/Wodzicki cosmological channel) — and the knowledge base confirms the framework *can* extract this one: S85's `N_SD=4` entry, "meromorphic-continuation residue equality at the closest TRUE pole," computes `Res_{s=4} ζ_D(s)` successfully. But our channel is `s=3`, `n=2`, the a₂ channel, and `g_M` there is a FINITE PART, not a residue. The L1-axiom lizzi invokes anchors the `s=4` residue (a₀), not the `s=3` finite part (a₂). The residue functional is the right tool one pole over; at our pole it targets the wrong coefficient.

**Net of §1:** `Φ_residue` is (i) identically zero at finite L (no pole), (ii) convergent only after supplying L→∞ continuation data the truncation lacks, and (iii) targeting `R`, not `g_M = C_0`, even then. None of the three is a coordinate artifact I can wave away; all three are structural.

#### 2. The framework ALREADY ran the only honest finite-L route to the continuation — and it missed (the empirical kill)

This is where the geometry stops being a-priori and becomes a measured fact already on disk. lizzi's `Φ_residue` is, operationally, "reconstruct the s=3 Laurent data (pole/residue/finite-part) from the finite-L spectrum." There is a name for the honest version of that operation — **acceleration / analytic-continuation reconstruction of a divergent or finite-part series from finitely many terms** (Richardson, Abel, Borel). The framework ran it at **S108 route (c)**, and the registry records the result verbatim (line 22017):

> "with the L=10 self-anchor REMOVED, the bare a₂ partial sum `Z(L) = Σ_{k≤L}|λ_k|⁻⁶` is a *convergent* series … whose Richardson/Abel L→∞ limit is `Z(∞) ≈ 650.70` — structurally ~4.27× BELOW `g_M = 2776`."

`g_M / Z(∞) = 2776.165389 / 650.70 = 4.2664` (Sage, this turn). So the one finite-L procedure that genuinely attempts the continuation — not the naive partial sum, but its accelerated/continued limit — **lands at 650.70 and misses `g_M` by 4.27×**, robustly, with the self-anchor removed (so it is not a load-and-compare-to-self). lizzi's R1 anti-tautology caveat for the proposed gate ("extract the residue from the spectrum, NOT load `g_M`") is exactly the constraint S108 route (c) already operated under, and it failed. The S109 gate's own anti-tautology guard (verdict line, this turn: "computed from the L12 spectrum cache via the Mellin↔Dirichlet continuation, NOT a re-read of `a_2_FW_zeta`") is the SAME constraint at the divergent end, and it diverged to `280743.235` — `rel_L10 = |280743.235367 − 2776.165389|/2776.165389 = 100.1263` (Sage). **Both honest finite-L continuation attempts — convergent-accelerated (650.70, below) and divergent-Mellin (280743, above) — bracket `g_M` from opposite sides and neither reaches it.** That is not a property of one bad functional choice; it is the signature that the finite-L spectrum does not carry the s=3 Laurent data to the precision `g_M` demands.

I will concede the exact thing lizzi is entitled to and no more: **IF** a future finite-L residue-extraction were shown to converge to `g_M` (residual → 0) on the L12 cache with the self-anchor removed, my wall's "un-reachable" half would fall and the scope would narrow to the partial-sum class. That is precisely `INV-FWD-RESIDUE-VS-PARTIALSUM`'s PASS branch, and I am not pre-judging it by fiat. But the prior from S108 route (c) is strong and adverse: the accelerated continuation already ran and missed by 4.27×, and the §1 Laurent argument says even a perfect residue extraction targets `R`, not `C_0 = g_M`. My standing prediction for the gate is the FAIL branch: `Φ_residue` either (a) returns ≈0 at finite L (no pole — the trivial entire-function answer), or (b) if it force-reconstructs a continuation, lands near `Z(∞)≈650.70`-type accelerated values or the `R≠g_M` residue, not at `g_M`. Only the dimensionless `Φ_logderiv` re-anchors (Tier-1).

#### 3. Why the wall holds with a SHARPER scope than the registry's current wording

The registry's held-REASON (line 22019) reads "un-anchorable on ANY finite-L truncation," and lizzi correctly flagged that "truncation" could be read narrowly (partial-sum class only). My §1–§2 close that gap and license the BROAD reading on geometric grounds:

```
  SCOPE OF THE WALL (sharpened, Reading a):
  g_M = C_0(s=3) is un-anchorable by ANY finite-L FUNCTIONAL Φ_L that is
  required to converge to g_M, because:
    (i)  the finite-L zeta is entire ⇒ pole/residue/finite-part at s=3 do NOT
         exist in any finite chart (they are L→∞ continuation data);
    (ii) the only finite-L routes to that data are acceleration/continuation
         reconstructions, which the framework ran (S108 route c) and missed 4.27×;
    (iii) the residue functional, even in the continuum, binds to R ≠ g_M = C_0.
  The wall therefore binds the WHOLE class {partial-sum, off-pole-Mellin,
  residue-reconstruction} of dimensionful finite-L magnitude functionals —
  NOT merely the partial-sum sub-class.
```
This is Tier-2-DIMENSIONFUL on the `cross-pillar-bridge-anatomy.md §"Tier-1/Tier-2"` gate, and I want to be precise about the registry's own current tier wording, because lizzi will (rightly) cite it: line 22011 records "**DISPOSITION (Axis-2, in-principle-constructibility): the magnitude channel `M(L) → g_M` is a CONVERGENT scalar … so a Tier-1 anchor is constructible**." That disposition was written at S106 W3, BEFORE S108/S109. It has been overtaken by its own discharge gates: S108 route (c) proved the convergent partial sum converges to `Z(∞)=650.70 ≠ g_M` (the "convergent scalar" converges to the WRONG scalar), and S109 proved the ζ-native form diverges. **The S106-era "Tier-1-constructible" disposition is exactly the proposition S108+S109 falsified.** Post-S109 the honest tier classification is Tier-2-DIMENSIONFUL with the held row at `NOT-SATISFIED-PENDING-substrate-physical-scale-anchor` — a PERMANENT hold on the *dimensionful magnitude*, with the theorem-STRUCTURE STAGE-3-PERMANENT untouched (Stage-2 PASS-AND on the non-Level-3 clauses; Level-1 identity `[T^{(IV)}]_{a₂,HKR} = [g_M]_{a₂,HKR}` regulator-invariant). The discharge route is NOT a finite-L magnitude functional at all — it is the Tier-1 dimensionless re-anchor, which BOTH of us agree converges.

And here the two readings genuinely converge on the constructive resolution: the surviving Level-3 object is the **dimensionless log-derivative / ratio**, Tier-1, and the bridge already exhibits one — the §VII.CB sign-channel residual `7.500e-09`, "L_max-FLAT by the multiplicative-normalization cancellation fingerprint" (line 22009, verbatim; `math-scripts.md` K=3 MANDATORY). The Tier-1/Tier-2 gate's own structural basis is `O(L,K) = W(L)·g(K) ⇒ only log-derivatives annihilate W(L)` — and the divergent shell-weight `W(L) ~ L^{α_growth} = L^{+2}` is exactly such a multiplicative L-factor. lizzi reads `7.500e-09` as "a different functional that binds"; I read it as "the homogeneity-degree-zero re-anchor on the same channel." **These are the same object described in two vocabularies — and that is the convergence point, not a disagreement** (see §4).

#### 4. Convergence: the two readings UNIFY into one criterion; the two gates are COMPLEMENTARY (orthogonal axes of one 2×2), not rival

Going into R2 I expected agreement on every verdict and disagreement on the reason. After this turn's work I can state something stronger: **the geometric identity `α_growth = d − 2s = n` and lizzi's functional partition are the SAME structural statement, related by a clean dictionary, and they pick out the SAME observable** (the dimensionful a₂ magnitude on the d=8 cone at the n=2 channel). They are not rival readings; they are two coordinate systems on one geometry.

The dictionary, term by term:

| lizzi's SPECTRAL axis (functional/regulator/pole) | my GEOMETRIC axis (homogeneity/apex) | unified statement |
|:---|:---|:---|
| pole index `s` selects the channel | curvature-degree `n = d − 2s` selects the channel | `n` and `s` are the SAME selector (`n = 8 − 2s`); choosing the pole IS choosing the curvature degree |
| `Φ_offpole` (partial sum) diverges | `α_growth = d − 2s = +2 > 0` ⇒ Weyl-divergent | the functional's L-behavior IS its homogeneity degree in the shell measure |
| `Φ_partial` (`2s′>d`) converges-but-misses | effective decay degree `> d` ⇒ summable, but limit ≠ continuation | convergence of a partial sum is `(effective 2s) > d`; binding is a SEPARATE question (the continuation) |
| `Φ_residue`/finite-part lives AT the pole | the pole/residue/finite-part are L→∞ (continuum) objects; entire at finite L | the "right functional" is OFF every finite-L truncation cone — geometrically, off the chart |
| `7.500e-09` sign-residual BINDS (different functional) | `7.500e-09` is the homogeneity-degree-0 (dimensionless) re-anchor, `W(L)` annihilated | the Tier-1 survivor is `deg = 0`; both axes name the SAME survivor |

The governing variable is genuinely shared: **lizzi's axis sets WHICH channel (which `n`/`s`, which functional form), my axis sets WHETHER that channel's dimensionful magnitude has a finite-L target (`α_growth = n ≥ 0 ⇒ no convergent target` AND the continuation is off every finite chart).** lizzi's R1 honest concession — that the naive bare-`s` proxy does not separate convergent-S108 from divergent-S109, and the separator is the functional-form/effective-decay-degree — and my R1 honest concession — that the separator is a *measure/homogeneity* label — are the SAME concession stated from two sides. Neither axis alone is "prior"; they are a product, and the unified criterion is the joint statement:

```
  UNIFIED CRITERION (a≡b at the verdict and at the reason):

  A finite-L dimensionful magnitude anchor A(L) of a substrate-IS bridge class
  at substrate-distance pole s on the apex-dimension-d spectral cone:

    (1) CONVERGES (admits a finite-L→∞ target)        ⇔  α_growth = d − 2s + Δ_hom < 0
                                                          [geometric: net homogeneity < 0;
                                                           spectral: Φ is a (2s′>d) partial-sum functional]
    (2) BINDS to the continuum value c_continuum       ⇔  c_continuum is the L→∞ limit of A(L)
                                                          [requires c_continuum to be ON the truncation
                                                           cone — FAILS for any Laurent coefficient
                                                           (pole/residue/finite-part) at a TRUE pole]
    (3) registry-PASS-eligible (Tier-1)                ⇔  the anchor is RE-ANCHORED to a deg-0
                                                          dimensionless invariant (log-derivative/ratio),
                                                          which annihilates W(L) ~ L^{α_growth}.

  For the §VII.CB a₂/s=3/d=8 channel: α_growth = n = +2 ⇒ (1) FALSE for the ζ-native form;
  (2) FALSE for EVERY finite-L magnitude functional (g_M = C_0 is a finite part at a true pole,
  off every truncation cone, and even the residue R ≠ C_0); (3) TRUE only for the dimensionless
  re-anchor (the 7.500e-09 sign-residual is the realized instance). ∎
```

**Are the two forward gates the SAME, COMPLEMENTARY, or RIVAL?** **COMPLEMENTARY** — they are the two orthogonal axes of one 2×2 decision table, and I now think running BOTH is the right structural verdict, with my gate's PASS branch already strongly disfavored by §1–§2:

- **My gate `INV-FWD-HOMOGENEITY-VS-REGULATOR`**: fix functional-form (partial sum at `α_growth=+2`), scan ≥3 regulator CLASSES {ζ-native (done, divergent), Pauli-Villars-subtracted, heat-kernel small-t a₂}. Tests: *is the apex dimension regulator-INVARIANT?* My prediction: all three diverge with `α_local ≈ +2…+4` (the multiplicity growth `m ~ L^{d−1}` on SU(3) is a Peter-Weyl fact, regulator-blind).
- **lizzi's gate `INV-FWD-RESIDUE-VS-PARTIALSUM`**: fix regulator (ζ), switch FUNCTIONAL {`Φ_offpole` (done, diverges), `Φ_residue`, `Φ_logderiv`} on the SAME L12 cache. Tests: *is convergence functional-SELECTION?* lizzi's prediction: `Φ_residue` binds to `g_M`; mine (per §1–§2): `Φ_residue` returns ≈0 (entire) or reconstructs to `R≠g_M`/`Z(∞)≈650.70`, and only `Φ_logderiv` binds (Tier-1).

The two gates fill out the 2×2 `(functional matters? × regulator matters?)`:
```
                          regulator-switch FLIPS verdict?
                              NO                    YES
  functional-    NO    apex-geometry governs    regulator governs
  switch FLIPS         (Reading a primary,      (Reading b, regulator-corollary
  verdict?             apex-keyed WALL)          dominant)
                 YES   functional governs       both axes load-bearing;
                       (Reading b primary,       criterion = joint
                       functional-selection)     (functional, regulator, geometry) triple
```
My §1–§2 prediction places the outcome in the **top-left cell** (neither switch flips the dimensionful verdict; only the deg-0 re-anchor binds) — Reading (a) primary, apex-keyed permanent wall, with lizzi's functional partition as the exact dual description of WHICH channel sits on the wall. lizzi's prediction is the bottom-left cell. **The gates are not rival because they probe different switches; they are complementary because TOGETHER they pin the cell.** The one case the current instance-string does not contain — a NON-partial-sum functional (the residue) at fixed geometry — is exactly lizzi's gate's discriminating case, and it is the right thing to run; I simply predict it lands in the top-left, not the bottom-left, for the entire-function + wrong-Laurent-coefficient reasons of §1.

**My honest residual uncertainty (the A-3 caution, restated).** My own Investigation-1 A-3 survey found ℐ⁺ to be regulator-CONDITIONAL (S³-de-Sitter under cutoff/heat/dim-reg vs R×S²-flat under ζ/Pauli-Villars). That is a genuine precedent for a *structural* (asymptotic-geometry) output being regulator-dependent in THIS framework, and lizzi correctly turns it against my "apex is regulator-invariant" claim. I do not get the apex-invariance for free — it is `INV-FWD-HOMOGENEITY-VS-REGULATOR`'s OUTPUT, not its premise. But note the asymmetry: A-3 concerns the *conformal-boundary topology* (a global asymptotic structure that genuinely can change with the regularization of the divergent modes), whereas `d_spec_cone_apex = 8` is the *Peter-Weyl multiplicity-growth dimension of SU(3)* (`m_{(p,q)} ~ (p+q)^{d−1}`), which is a representation-theoretic fact about the group, fixed before any regulator is chosen. My prediction is that the apex dimension is the regulator-robust one precisely because it lives in the group's Plancherel measure, not in the mode-regularization — but that distinction is itself a falsifiable claim the gate adjudicates. The A-3 caution is the strongest reason to RUN my gate rather than declare apex-invariance, and I hold it as a live possibility that the gate lands bottom-left (regulator-dominant), which would be a genuine and interesting defeat of the geometric reading's universality.

#### Proposed Structural-Verdict text (for lizzi to consolidate — NOT written into the verdict section by me)

I offer the following for lizzi's final-turn consolidation; lizzi owns the wording and may revise:

> **Candidate theorem (UNIFIED, a≡b):** For a substrate-IS cross-pillar-bridge dimensionful magnitude anchor at substrate-distance pole `s` on the apex-dimension-`d` spectral cone, `α_growth = d − 2s = n` (the shell-sum exponent IS the curvature-degree grading). The anchor (1) admits a finite-L→∞ target ⇔ `α_growth < 0`; (2) BINDS to a continuum Laurent coefficient (residue OR finite-part) at a TRUE pole **never** from finite L, because the finite-L zeta is entire (the pole is an L→∞ object) and the only finite-L route — acceleration/continuation reconstruction — was run (S108 route c → `Z(∞)=650.70 ≠ g_M`) and missed; (3) is registry-PASS-eligible ⇔ re-anchored to a deg-0 dimensionless invariant (log-derivative/ratio; Tier-1). The geometric reading (apex/homogeneity) and the spectral reading (functional/pole) are the SAME criterion under the dictionary `n ↔ s`, `homogeneity-degree ↔ functional-form`, agreeing at the verdict AND the reason. **Sub-question resolutions:** (a) BOTH properties predict convergence and they coincide via `n = d − 2s`; the apex dimension `d=8` (Peter-Weyl growth) sets WHETHER, the pole/functional sets WHICH. (b) The L-divergence per se is a coordinate-vs-invariant / functional-selection artifact (re-anchor to deg-0 and it vanishes); the un-reachability of `g_M = C_0` by any finite-L magnitude functional is INTRINSIC (a finite part at a true pole is off every truncation cone). (c) `INV-FWD-HOMOGENEITY-VS-REGULATOR` and `INV-FWD-RESIDUE-VS-PARTIALSUM` are COMPLEMENTARY orthogonal axes of one 2×2; run BOTH; the geometric reading predicts the top-left cell (apex-keyed permanent Tier-2-DIMENSIONFUL wall, dimensionless re-anchor as the discharge), the spectral reading predicts `Φ_residue` binds (bottom-left). The §VII.CB held Level-3 row is a PERMANENT wall on the dimensionful magnitude; the theorem-STRUCTURE is STAGE-3-PERMANENT; the surviving registry-PASS object is the Tier-1 dimensionless re-anchor (`7.500e-09` sign-residual exhibited).

### R2 · lizzi-spectral-functional-theorist

**Position in one line.** I CONCEDE the discharge cleanly: `Φ_residue` does NOT anchor the held §VII.CB Level-3 row from finite-L data, and sp's three reasons are each correct, Sage- and knowledge-MCP-verified this turn. But the concession is *narrow and sharpening*, not a collapse of Reading (b): my core spectral-functional distinction — **convergence ≠ binding; the bridge selected a non-binding functional** — SURVIVES and becomes the *content* of the unification, not a casualty of it. What falls is one over-reach in my R1 gate: the parenthetical "the residue is computable from a finite-L spectrum (… converges to the true residue as L grows)." That step is the un-discharged one sp identified, and it is wrong for a reason that is *itself* a spectral-functional fact, not a geometric one: the finite-L zeta is entire, so it has no s=3 Laurent data at all — and `g_M` is not even the coefficient I named.

#### 1. Concession on all three strikes — with the substitution chain, because a sign/identity claim demands it

**Strike 1 (entire ⇒ `Res_{s=3} ζ^{(L)} = 0` identically): CONCEDED, verified.** The substitution chain:
```
  Step 1:  ζ^{(L)}_{D_K}(s) = Σ_{p+q≤L} m_{(p,q)} |λ_{(p,q)}|^{−2s}    [def; finite sum, L<∞]
  Step 2:  each term = m · exp(−2s·ln|λ|), |λ| ∈ [0.82, 4.67] bounded  [entire in s]
  Step 3:  finite sum of entire functions is entire                     [holomorphic on all ℂ]
  Step 4:  an entire function has empty principal part everywhere       ⇒ Res_{s=3} ζ^{(L)} = 0
  Conclusion: Res_{s=3} ζ^{(L)}_{D_K}(s) = 0 at EVERY finite L. ∎
```
Sage this turn: sp's toy polynomial `64·4.67^{−2s}+27·2.5^{−2s}+3·0.82^{−2s}` has `f(3)=9.985` finite, `f'(3)=3.695` finite — manifestly entire at s=3, no pole. My R1 gate `Φ_residue(L) = Res_{s=3} ζ^{(L)}_{D_K}(s)` therefore returns **0 at finite L**, not a convergent approximation to a nonzero residue. The pole at s=3 (a TRUE pole of the full zeta: `n = d − 2s = 8 − 6 = 2 ∈ S_d = {0,2,4,6,8}`, Sage-confirmed; true s-poles `{0,1,2,3,4}`) is an L→∞ continuation feature, invisible in every finite chart. sp's coordinate-vs-invariant framing of this — "the truncated cone is regular (entire) at s=3; the pole is a feature of the completed object" — is exactly right and is, ironically, the strongest possible statement of MY own [[zeta-not-physical]] lesson: the off-residue partial sum is not the physical object; but neither is the residue *recoverable* from finite truncation, because the truncation has no pole.

**Strike 2 (`g_M = C_0` Hadamard finite part, not the residue `R`): CONCEDED, and it is the sharper kill.** Knowledge-MCP verbatim this turn: `g_M = a_2_FW_zeta = 2776.165389 is the HADAMARD FINITE PART (residue-subtracted continuation)` (investigation-8-plan-w1.md). Near the true s=3 pole:
```
  ζ_{D_K}(s) = R/(s−3) + C_0 + C_1(s−3) + …
       R   = Res_{s=3} ζ_{D_K}(s)     ← what Φ_residue would extract
       C_0 = a_2_FW_zeta = g_M = 2776.165389   ← the actual target (residue-SUBTRACTED)
```
So even granting a perfect continuum continuation, `Φ_residue = R ≠ C_0 = g_M`. My R1 discharge predicate `|Res^{(L)}_{s=3} − g_M|/g_M → 0` was testing convergence of `Φ_residue` to a number `Φ_residue` does not equal. This is decisive and I do not contest it. (It also tightens my own framing: the physical a₂ content is `C_0`, the finite part — a *third* spectral functional beyond residue and partial-sum, and the one I should have named.)

**Strike 2′ (Connes axiom `Tr_ω(|D|^{−d}) = Res_{s=d} ζ_D(s)` is at s=d=4, n=0 (a₀), not s=3, n=2 (a₂)): CONCEDED.** The Dixmier-trace/Connes identity I invoked in R1 as "L1-axiomatic" anchors the residue at the spectral-dimension pole `s=d=4` — the a₀/Wodzicki cosmological channel (`n=0`). The framework can and does extract THAT one (S85 `N_SD=4`, "meromorphic-continuation residue equality at the closest TRUE pole"). But our channel is s=3, n=2, and the a₂ datum there is a *finite part*, not a residue. My axiom was the right tool one pole over. I mis-applied it. The [[three-layer-regulator]] L1 statement `Tr_ω(|D|^{−d}) = Res_{s=d} ζ_D(s)` is about the s=d residue; it says nothing that rescues an s=3 finite part from finite-L data.

#### 2. The sharpened position — the deepest point cuts in sp's favor, and it is a SPECTRAL statement

Here is the part of my own reasoning that, followed honestly, lands the broad-class wall harder than sp's R1 did — and it is why I concede the SCOPE, not just the gate. sp's wall says `g_M = C_0` is un-anchorable by ANY finite-L magnitude functional. The reason, in functional-selection language: **for the finite-L (entire) zeta, the ONLY candidate "finite part at s=3" is the plain value `ζ^{(L)}(3)` — there is no pole, so no Hadamard subtraction, so the finite part degenerates to the value.** And `ζ^{(L)}(3) = Σ_{p+q≤L} m|λ|^{−6} = Φ_offpole(L)` — the divergent thing (39619→109123→280743, Sage-confirmed, ratio 14.3×→39.3×→101.1× over `g_M`). So:
```
  At finite L:  finite-part(s=3) ≡ value(s=3) = Φ_offpole(L)  [no pole ⇒ no subtraction]  → DIVERGES
  At L→∞:       finite-part(s=3) = C_0 = g_M = 2776.165        [Hadamard, residue-subtracted]
```
The Hadamard finite part `C_0 = g_M` is born ONLY when the sum becomes infinite and acquires its meromorphic structure with a genuine pole to subtract. **`C_0` is L→∞ continuation data exactly as the residue `R` is — both Laurent coefficients at the true s=3 pole are unreachable from the finite chart.** This is the functional-selection statement of sp's geometric "off every truncation cone": the finite-L functional family has NO member that equals `C_0`, because the operation that PRODUCES `C_0` (subtract a pole) is undefined when there is no pole. My R1 sentence "the residue functional is an untested finite-L functional that … computes `g_M` directly" is therefore wrong twice over: it computes 0 (no pole), and the thing it would compute in the limit (`R`) is the wrong coefficient (`≠ C_0`).

So my R1 held-REASON contest — "un-anchorable on any finite-L truncation' is SCOPED to the partial-sum class; the residue is an escape" — is **WITHDRAWN**. The broad reading is correct: the wall binds the whole class {partial-sum, off-pole-Mellin, residue-reconstruction, finite-part-reconstruction} of dimensionful finite-L magnitude functionals. Not because "the channel has no continuum target" (it does — `g_M = C_0` exists in the continuum), but because **every finite-L *functional* the bridge can apply is the wrong functional for a Laurent coefficient at a true pole.** That is Reading (b)'s vocabulary ("wrong functional") reaching the same wall as Reading (a)'s ("off every chart") — and it is the unification, not a defeat.

What I do NOT concede, and what survives intact: **`g_M` is reachable IN THE CONTINUUM** (it is `C_0`, a well-defined number the framework holds at 2776.165389). The wall is on *finite-L anchoring*, not on the existence of the target. This matters for sub-question (b): the un-reachability is intrinsic *to finite-L truncation*, but it is NOT "the channel genuinely has no continuum target under any regulator" — every admissible regulator computes the SAME `C_0` in the continuum (zeta as the s=3 finite part; Pauli-Villars as the subtracted a₂ coefficient; heat-kernel as the `t^0` log-coefficient at degree n=2). The regulator-invariant continuum content is `C_0`; what no regulator's *finite-L truncation* carries is `C_0`. This is the [[three-layer-regulator]] L1/L2 split precisely: L1 (the continuum residue/finite-part identity) is regulator-invariant and real; L2 (the finite-L envelope binding to it) is what fails for the dimensionful magnitude and succeeds only for the dimensionless re-anchor.

#### 3. On the empirical kill (S108 route c) — I accept it and add the spectral reading

sp's §2 is the measured fact that converts the a-priori argument into a closed one, and I accept it. S108 route (c) ran the honest finite-L continuation (Richardson/Abel acceleration of the bare partial sum, L=10 self-anchor REMOVED — so not a load-and-compare-to-self) and landed at `Z(∞) = 650.70`, missing `g_M` by `g_M/Z(∞) = 4.2664` (Sage-confirmed this turn). S109 ran the divergent Mellin end and hit `280743.235`, `rel_L10 = 100.1263` (Sage-confirmed). **Both honest finite-L continuation routes bracket `g_M` from opposite sides and neither reaches it** — the signature that the finite spectrum lacks the s=3 Laurent data to the precision `g_M` demands. The spectral gloss I add: 650.70 is the limit of `Φ_partial` (a convergent partial-sum functional → a real number ≠ `C_0`); 280743 is `Φ_offpole` at L=10 (a non-convergent partial-sum functional). *Neither is the finite-part functional* — and there is no finite-L finite-part functional, per §2. The S86 duplicate I flagged in R1 (same number 280743.235 tagged `off-pole-Hankel` INFO at S86, `FW-zeta-native` FAIL at S109) still stands as evidence that the divergence is a *functional/scheme-label* property — but I now read it as confirming sp's point: S109 tested the off-pole partial-sum value, which the framework already knew (S86) was the off-pole evaluation, not any finite part. The duplicate proves the label matters; it does NOT prove a binding finite-L functional exists.

#### 4. UNIFICATION: ACCEPTED. COMPLEMENTARY 2×2: ACCEPTED, with one sharpening of the predicted cell

I accept sp's unification in full: `α_growth = d − 2s = n` (the shell-sum exponent IS the curvature-degree grading) and my functional partition are the SAME structural statement under the dictionary `n ↔ s`, `homogeneity-degree ↔ functional-form`. The governing variables are genuinely a product, not a hierarchy: **the spectral axis (pole/functional-form) sets WHICH channel (which n); the geometric axis (apex/homogeneity) sets WHETHER that channel's dimensionful magnitude admits a finite-L target (`α_growth = n ≥ 0 ⇒ no convergent target`) AND whether its continuum value is on the truncation cone (a Laurent coefficient at a true pole is NOT).** sp's dictionary table is correct row-by-row; I would add one row making the third functional explicit:

| lizzi SPECTRAL axis | sp GEOMETRIC axis | unified |
|:---|:---|:---|
| `Φ_finitepart = C_0` is the physical a₂ datum, born only at L→∞ | the Hadamard finite part at a TRUE pole is continuation data, off every finite chart | the "right functional" `C_0` has NO finite-L representative — the subtraction it requires is undefined without a pole |

I accept the 2×2 is COMPLEMENTARY (orthogonal switches: regulator-switch × functional-switch), not rival, and that running BOTH gates is the right structural verdict. **My one revision to the predicted cell:** going into this workshop I predicted the bottom-left cell (functional-switch flips the verdict; `Φ_residue` binds). Post-concession I REVISE my prediction to the **top-left cell** — the same cell sp predicts — for `INV-FWD-RESIDUE-VS-PARTIALSUM`: the residue/finite-part functional does NOT bind to `g_M` from finite L (it returns 0, or reconstructs to `R ≠ C_0` or `Z(∞) ≈ 650.70`), and only the dimensionless `Φ_logderiv` re-anchors (Tier-1). I am not declaring this by fiat — the gate must run — but I no longer hold the bottom-left as my prediction; the entire-function + wrong-Laurent-coefficient reasons of §1–§2 are dispositive enough that my honest prior is now top-left.

This is NOT a vacuous gate after the concession. Its value shifts: it no longer adjudicates "does the held row discharge?" (I concede it does not from finite L) — it **confirms the broad-class wall constructively** by exhibiting, on the L12 cache, that (i) `Φ_residue^{(L)} = 0` (entire), (ii) any forced finite-L continuation lands at `R`/`Z(∞)`-type values `≠ C_0`, and (iii) `Φ_logderiv` binds (Tier-1) — turning sp's a-priori `g_M = C_0`-is-off-the-chart argument into a measured 3-functional fact on one spectrum at one geometry. That is worth running: it closes the gate's discriminating case (a NON-partial-sum functional at fixed geometry, the one case the current instance-string lacks) with data rather than argument.

**The genuinely-open residual (NOT discharged by this concession).** sp's own A-3 caution (ℐ⁺ regulator-CONDITIONAL: S³-de-Sitter vs R×S²-flat) remains live and cuts toward MY axis on a DIFFERENT question than the one I just conceded. I conceded that *the finite-part `C_0` is off every finite-L chart* (Strike 2). I did NOT concede that *the apex dimension `d=8` is regulator-INVARIANT* — that is the separate claim `INV-FWD-HOMOGENEITY-VS-REGULATOR` adjudicates, and A-3 is a genuine precedent that a structural/asymptotic output in this framework has been regulator-dependent. sp's rebuttal (apex `d=8` is the Peter-Weyl multiplicity-growth dimension of SU(3), `m_{(p,q)} ~ (p+q)^{d−1}`, fixed before any regulator) is strong but is itself the gate's falsifiable OUTPUT, not its premise. So the unified criterion's `α_growth = d − 2s` is established at the verdict level for every instance in the string; whether `d` carries a regulator label is the one live empirical question, and it is sp's gate, not mine, that holds it open. I flag this so the Structural Verdict does not over-claim regulator-invariance.

**Net.** Reading (b)'s discharge claim: WITHDRAWN. Reading (b)'s core distinction (convergence ≠ binding; functional-selection governs WHICH channel): SURVIVES as half of the unified criterion. The held §VII.CB Level-3 dimensionful magnitude row: a PERMANENT Tier-2-DIMENSIONFUL wall (binds the whole finite-L magnitude functional class, not just partial-sums). The surviving registry-PASS object: the Tier-1 dimensionless re-anchor (log-derivative/ratio; the `7.500e-09` sign-residual is the realized instance, registry-PROVEN at L_max=10). The theorem-STRUCTURE: STAGE-3-PERMANENT, untouched (Level-1 `[T^{(IV)}]_{a₂,HKR} = [g_M]_{a₂,HKR}` regulator-invariant at every L_max).

---

## Structural Verdict

**Status of the workshop**: CONVERGED on a UNIFIED criterion (the two readings coincide at the verdict AND at the reason, under an explicit dictionary). This is a **STAGE-0 workshop-internal candidate theorem** per `joint-theorem-promotion.md` 4-stage pathway — the two of us (sp on the GEOMETRIC axis, lizzi on the SPECTRAL axis) are the Stage-0 co-authors; we are NOT the Stage-2 cross-reviewers, and the criterion is NOT registered until a separate session-track Stage-1 registration + Stage-2 two-agent cross-axis verify lands (routed to Carry-Forward CF-INV4-W3-2-STAGE1).

### The candidate convergence criterion (closed form, unified a≡b)

For a substrate-IS cross-pillar-bridge **dimensionful magnitude anchor** `A(L)` of a Level-1 cohomology class at substrate-distance pole `s` on the apex-dimension-`d` spectral cone (`d = d_spec_cone_apex = 8` for SU(3), the Peter-Weyl multiplicity-growth dimension `m_{(p,q)} ~ (p+q)^{d−1}` — NOT the canonical spectral dimension `d_s = 3.0`):

```
  UNIFIED CRITERION (geometric axis ≡ spectral axis under the dictionary n ↔ s):

  Shell-sum exponent identity:   α_growth = d − 2s + Δ_hom  =  n  (the curvature-degree grading)
                                  [Sage-confirmed: s=3 ⇒ n = 8−2·3 = 2 ⇒ α_growth = +2]

  (1) A(L) CONVERGES to a finite-L→∞ target        ⇔  α_growth = d − 2s + Δ_hom < 0
        [geometric: net integrand homogeneity in the Plancherel shell measure < 0]
        [spectral:  Φ is a partial-sum functional with effective decay 2s′ > d]

  (2) A(L) BINDS to the continuum value c_continuum ⇔  c_continuum is the L→∞ limit of A(L)
        ⇔  c_continuum is ON the truncation cone.
        FAILS for EVERY Laurent coefficient (residue R, finite part C_0, …) at a TRUE pole,
        because the finite-L zeta is ENTIRE (no pole ⇒ no principal part ⇒ no residue,
        and no pole ⇒ no Hadamard subtraction ⇒ the "finite part" degenerates to the
        divergent value ζ^{(L)}(s) = Φ_offpole(L)). Both R and C_0 are L→∞ continuation data.

  (3) registry-PASS-ELIGIBLE (Tier-1)              ⇔  re-anchored to a deg-0 dimensionless
        invariant (log-derivative d ln A/d ln K, or ratio), which ANNIHILATES the
        multiplicative shell-weight W(L) ~ L^{α_growth}  [math-scripts.md K=3 MANDATORY:
        O(L,K) = W(L)·g(K) ⇒ only log-derivatives annihilate W(L)].
```

**Instantiation at the §VII.CB a₂ / s=3 / d=8 channel** (`α_growth = n = +2`):
- (1) FALSE for the ζ-native form `Φ_offpole`: Weyl-divergent (S109: `trend_sign=+1`, `is_weyl_divergent=True`, `39619→109123→280743`, `rel_L10 = 100.1263` Sage-exact, diverges ABOVE `g_M`).
- (2) FALSE for EVERY finite-L magnitude functional: `g_M = C_0 = a_2_FW_zeta = 2776.165389` is the Hadamard FINITE PART (residue-subtracted continuation, knowledge-MCP verbatim) — off every truncation cone. The honest finite-L continuation (S108 route c, Richardson/Abel, self-anchor removed) lands at `Z(∞) = 650.70`, missing by `g_M/Z(∞) = 4.2664` (Sage-exact); the residue functional `Φ_residue` returns 0 at finite L (entire) and targets `R ≠ C_0` even in the continuum. Both honest routes BRACKET `g_M` from opposite sides (650.70 below, 280743 above) and neither reaches it.
- (3) TRUE only for the deg-0 dimensionless re-anchor: the §VII.CB sign-channel residual `7.500e-09` at L_max=10 (registry-PROVEN Level-3, "L_max-FLAT by the multiplicative-normalization cancellation fingerprint") is the realized Tier-1 instance.

### Scope of the wall (which observables are which)

- **Tier-2-DIMENSIONFUL permanent walls** (registry-PASS-INELIGIBLE; held at `NOT-SATISFIED-PENDING-substrate-physical-scale-anchor`): every dimensionful finite-L magnitude anchor `A(L)` of a Level-1 class whose continuum value is a Laurent coefficient (residue OR finite part) at a TRUE pole of `ζ_{D_K}(s)`. The §VII.CB a₂/s=3 magnitude row is the canonical occupant. The S106-era "Tier-1-constructible" disposition (registry line 22011) is OVERTAKEN by its own discharge gates (S108: convergent partial sum → wrong scalar 650.70; S109: ζ-native → divergent) and is post-S109 a falsified proposition.
- **Tier-1 dimensionless registry-PASS objects** (re-anchorable): log-derivatives `d ln A/d ln K`, dimensionless ratios against a second divergent channel, and integer-anchored saturation residuals — all annihilate `W(L) ~ L^{α_growth}`. Realized instances: §VII.CB `7.500e-09` sign-residual; §VII.BE SU(4)_PS `d ln Res/d ln L` (the second-log-derivative spectral-dimension family). These are the surviving Level-3 objects.
- **Theorem-STRUCTURE (unaffected, STAGE-3-PERMANENT)**: the Level-1 cohomology identity `[T^{(IV)}]_{a₂,HKR} = [g_M]_{a₂,HKR}` is regulator-invariant at every L_max; nothing in the magnitude-divergence touches it. The wall is on the *finite-L dimensionful anchoring*, NOT on the existence of the continuum target (`g_M = C_0` exists; every admissible regulator computes the SAME `C_0` in the continuum — zeta finite-part, Pauli-Villars subtracted-a₂, heat-kernel `t^0` log-coefficient at n=2). This is the [[three-layer-regulator]] L1/L2 split: L1 (continuum finite-part identity) regulator-invariant and real; L2 (finite-L envelope) binds only for the deg-0 re-anchor.

### Sub-question resolutions

- **(a) Which property predicts convergence a priori?** BOTH, and they COINCIDE via `n = d − 2s`. The pole index `s` / functional-form (spectral) selects WHICH channel (which `n`); the apex dimension `d=8` / integrand homogeneity (geometric) sets WHETHER that channel's dimensionful magnitude converges (`α_growth = n ≥ 0 ⇒ no convergent target`) and whether its continuum value is on the cone (a Laurent coefficient at a true pole is NOT). Neither axis is prior; they are a product. Closed form: the boxed UNIFIED CRITERION above. The naive bare-`s` proxy does NOT separate convergent-S108 from divergent-S109 (both s=3); the separator is the functional-form / effective-decay-degree `Δ_hom` — which is simultaneously a homogeneity label (geometric) and a functional-selection label (spectral). Both co-authors conceded this symmetrically in R1; it is the dictionary, not a disagreement.

- **(b) Coordinate-vs-invariant artifact OR intrinsic regime-breakdown?** BOTH, cleanly separated by the criterion:
  - The **L-divergence per se** (the `α_growth ≥ 0` blow-up of `Φ_offpole`) is a **coordinate-vs-invariant / functional-selection artifact** — re-anchor to the deg-0 dimensionless invariant and it vanishes (the Tier-1 object converges on the SAME channel).
  - The **un-reachability of `g_M = C_0` by any finite-L magnitude functional** is **INTRINSIC to finite-L truncation** — a finite part at a true pole is off every truncation cone, because the operation producing it (subtract a pole) is undefined where there is no pole, and the finite-L zeta is entire. This is NOT "the channel has no continuum target under any regulator" (it does — `C_0` is regulator-invariant in the continuum); it is "no finite-L *functional* is the right functional for a Laurent coefficient at a true pole." The intrinsic half binds the WHOLE finite-L magnitude functional class {partial-sum, off-pole-Mellin, residue-reconstruction, finite-part-reconstruction}, not merely the partial-sum sub-class — lizzi's R1 "the residue is a finite-L escape" contest is WITHDRAWN.

- **(c) The decisive forward gate(s).** A COMPLEMENTARY 2×2, not a single gate: `INV-FWD-HOMOGENEITY-VS-REGULATOR` (fix functional-form, scan regulator classes) × `INV-FWD-RESIDUE-VS-PARTIALSUM` (fix regulator, switch functional). Run BOTH. Both co-authors predict the **top-left cell** (neither switch flips the dimensionful verdict; only the deg-0 re-anchor binds) ⇒ Reading (a) apex-keyed permanent Tier-2-DIMENSIONFUL wall, with Reading (b)'s functional partition as the exact dual description of WHICH channel sits on the wall. The one live empirical question on which the criterion does NOT yet have a verdict is whether the apex dimension `d=8` is regulator-INVARIANT — `INV-FWD-HOMOGENEITY-VS-REGULATOR`'s output (sp's A-3 caution keeps it open; the criterion's `α_growth = d − 2s` is established at the verdict level for every instance, but the regulator-label on `d` is not).

### The decisive 2×2 forward gate (pre-registered)

```
                          regulator-switch FLIPS verdict?  (INV-FWD-HOMOGENEITY-VS-REGULATOR)
                              NO                            YES
  functional-    NO    [TOP-LEFT] apex-geometry         regulator governs
  switch FLIPS         governs — Reading (a) primary,    (Reading b regulator-corollary
  verdict?             apex-keyed Tier-2-DIM WALL;        dominant)
  (INV-FWD-            both co-authors' prediction
  RESIDUE-VS-    YES   functional governs               both axes load-bearing;
  PARTIALSUM)          (Reading b primary,               criterion = joint
                       functional-selection)             (functional, regulator, geometry) triple
```

**Gate A — `INV-FWD-HOMOGENEITY-VS-REGULATOR`** (sp's axis; tests regulator-invariance of the apex):
- *Observable*: hold channel geometry fixed (a₂, s=3, d=8 cone, `α_growth = +2`); scan `A(L; s=3)` across ≥3 structurally-distinct regulator classes {ζ-native Mellin [done: DIVERGENT], Pauli-Villars-subtracted partial sum at the same pole, heat-kernel `Tr e^{−tD²}` small-t a₂ coefficient}. Record `(trend_sign, α_local(8→10), is_weyl_divergent)` per class. L12 master cache `s84_spectrum_cache_L12_tau019.npz` (feasible; no high-L irrep build).
- *PASS/FAIL on the discriminating case*: ALL three diverge with `α_local ≈ +2…+4` (same sign) ⇒ **Reading (a) confirmed**: apex dimension is regulator-INVARIANT; `α_growth = d − 2s ≥ 0 ⇒ DIVERGENT` becomes a regulator-blind WALL (TOP-LEFT). At least one regulator binds where ζ-native diverged ⇒ **Reading (b) regulator-corollary**: divergence carries a regulator label (TOP-RIGHT).

**Gate B — `INV-FWD-RESIDUE-VS-PARTIALSUM`** (lizzi's axis; tests functional-selection at fixed geometry):
- *Observable*: hold channel geometry fixed (a₂, s=3, d=8); evaluate THREE functionals on the SAME L12 cache at L ∈ {8,10,12}: `Φ_offpole(L) = Σ m|λ|^{−6}` [done: DIVERGES]; `Φ_residue/finitepart(L)` = the s=3 Laurent reconstruction from the L-truncated zeta (contour/acceleration extraction; anti-tautology: extract from spectrum, do NOT re-read `a_2_FW_zeta`); `Φ_logderiv(L) = d ln Φ_offpole/d ln L` (deg-0 Tier-1 re-anchor). Record `(trend_sign, α_local(8→12), L→∞ limit, |limit − g_M|/g_M)` per functional.
- *PASS/FAIL on the discriminating case*: `Φ_residue/finitepart` binds to `g_M` (residual → 0) while `Φ_offpole` diverges on the same spectrum ⇒ **Reading (b) confirmed**: convergence is functional-SELECTION; the held row is anchorable after all (BOTTOM-LEFT). `Φ_residue/finitepart` returns ≈0 (entire) or reconstructs to `R`/`Z(∞)`-type values `≠ g_M = C_0`, and only `Φ_logderiv` binds (Tier-1) ⇒ **Reading (a) confirmed**: the magnitude channel is genuinely Tier-2-DIMENSIONFUL regardless of functional; the only registry-PASS object is dimensionless (TOP-LEFT). [Both co-authors predict TOP-LEFT post-R2; the gate confirms the broad-class wall constructively on one spectrum at one geometry, closing the one case the instance-string lacks — a NON-partial-sum functional at fixed geometry.]

**Joint reading of the 2×2**: TOP-LEFT (both NO) ⇒ apex-geometry governs, Reading (a) primary, permanent wall. BOTTOM-LEFT (functional flips, regulator does not) ⇒ Reading (b) primary, functional-selection, held row discharges. TOP-RIGHT (regulator flips, functional does not) ⇒ regulator-corollary dominant. BOTTOM-RIGHT (both flip) ⇒ joint `(functional, regulator, geometry)` triple criterion.

---

## Wrap-Up

The INV4-W3-2 workshop CONVERGED. Both axes — sp's GEOMETRIC (homogeneity-vs-apex) and lizzi's SPECTRAL (functional-selection/pole) — resolved to ONE unified criterion, agreeing at the verdict AND at the reason under the dictionary `n ↔ s`, `homogeneity-degree ↔ functional-form`. The decisive turn was lizzi's clean concession of the `Φ_residue` discharge: sp's three reasons (finite-L zeta is entire ⇒ `Res_{s=3} = 0` identically; `g_M = C_0` is the Hadamard finite part, not the residue `R`; the Connes axiom anchors s=d=4 not s=3) are each Sage- and knowledge-MCP-verified, and they land the broad-class wall harder than R1 did — `g_M = C_0` is L→∞ continuation data off every finite-L chart, so NO finite-L magnitude functional anchors it, not merely the partial-sum sub-class. What survived the concession is Reading (b)'s core distinction (convergence ≠ binding; functional-selection governs WHICH channel), which became HALF of the unified criterion rather than a casualty of it. The held §VII.CB Level-3 dimensionful magnitude row is a PERMANENT Tier-2-DIMENSIONFUL wall; the surviving registry-PASS object is the Tier-1 dimensionless re-anchor (`7.500e-09` sign-residual, registry-PROVEN at L_max=10); the theorem-STRUCTURE is STAGE-3-PERMANENT, untouched. The one live empirical residual is whether the apex dimension `d=8` is regulator-INVARIANT (sp's gate's output; sp's A-3 ℐ⁺-regulator-conditional caution keeps it open). Two complementary forward gates (a 2×2) were pre-registered; both co-authors predict the top-left cell (apex-keyed permanent wall).

### What Changed

#### (a) Numerical revisions

- `g_M/Z(∞) = 4.27` → `4.2664` (Sage-exact, `2776.165389 / 650.70`; S108 route-c miss factor pinned).
- `rel_L10 ≈ 100.13` (verdict) → `100.126264479555` (Sage-exact, `|280743.235367 − 2776.165389|/2776.165389`).
- `α_growth = d − 2s = +2` confirmed Sage-exact at s=3 (`n = 8 − 2·3 = 2`); true s-poles of the FULL zeta `{0,1,2,3,4}` (Conv. A double-power, d=8) — s=3 IS a true pole of the continuum object (n=2, a₂), so the s=3 Laurent data exists in the continuum but not in any finite-L chart.
- `Φ_offpole(L) = ζ^{(L)}(3)` values `39619→109123→280743` re-read as ratios `14.3×→39.3×→101.1×` over `g_M` (Sage) — the divergent value of the entire finite-L zeta AT s=3, which IS the degenerate "finite part" when there is no pole to subtract.

#### (b) Structural changes

- **`Φ_residue` discharge claim: WITHDRAWN** (epistemic-type change). lizzi's R1 position "the residue functional is a finite-L escape that discharges the held row" → conceded false: the finite-L zeta is entire (no pole ⇒ residue ≡ 0), and `g_M = C_0` is the residue-SUBTRACTED finite part (a different Laurent coefficient than the residue `R`). The discharge route falls; the binding-vs-convergence distinction survives as the criterion's spectral half.
- **Wall scope: partial-sum-class → whole finite-L-magnitude-functional-class** (scope promotion). The §VII.CB held-REASON "un-anchorable on ANY finite-L truncation" is now established for {partial-sum, off-pole-Mellin, residue-reconstruction, finite-part-reconstruction} — not merely the partial-sum sub-class lizzi's R1 scoped it to. The broad reading is correct; the narrow contest is withdrawn.
- **Two rival readings → one unified criterion under an explicit dictionary** (relationship reclassification). `α_growth = d − 2s = n` (geometric) ≡ functional partition (spectral) are the SAME structural statement; the two axes are a PRODUCT (which-channel × whether-converges), not a hierarchy.
- **Two forward gates: rival → COMPLEMENTARY 2×2** (structure change). `INV-FWD-HOMOGENEITY-VS-REGULATOR` (regulator-switch axis) and `INV-FWD-RESIDUE-VS-PARTIALSUM` (functional-switch axis) are orthogonal axes of one decision table; run BOTH.
- **`INV-FWD-RESIDUE-VS-PARTIALSUM` predicted cell: bottom-left → top-left** (lizzi's prediction revision). Pre-workshop lizzi predicted `Φ_residue` binds (bottom-left); post-concession lizzi revises to top-left (residue returns 0 / targets `R ≠ C_0`; only `Φ_logderiv` binds), agreeing with sp. The gate's VALUE shifts from "does the row discharge?" to "confirm the broad-class wall constructively on one spectrum."
- **S106-era "Tier-1-constructible" disposition: OVERTAKEN → falsified** (registry-state observation, not effected here). Registry line 22011's S106 W3 "the magnitude channel `M(L) → g_M` is a CONVERGENT scalar … so a Tier-1 anchor is constructible" was falsified by its own discharge gates (S108: convergent → wrong scalar 650.70; S109: ζ-native → divergent). This is flagged for the session-track reconciliation CF, NOT edited here (track-local boundary).

### Effected In-Session

- [x] Workshop structural verdict landed — wrote `### R2 · lizzi-spectral-functional-theorist` + `## Structural Verdict` + `## Wrap-Up` + `## Carry-Forward Computations` — `sessions/investigation/investigation-4/workshops/level-3-magnitude-divergence.md` — this doc (artifact-existence-with-content closure; this is a `gate_type: workshop` gate, NO verdict-file line per `gate-verdicts.md §"Investigation-Track Canonical Path"`).
- [x] No session-track register edits — **track-local boundary** (`gate-verdicts.md §"Investigation-Track Canonical Path"`): an INV4 workshop CANNOT mutate session-track curated registers (`sessions/permanent-results-registry.md`, the `.claude/rules/` files, the Atlas). The unified criterion + the Tier-2-DIMENSIONFUL wall scope + the S106-disposition overtake are NOT written into any session-track register in this workshop. The honest in-session effected item is THIS workshop doc + its Structural Verdict; ALL registry/STAGE-1 registration is routed to Carry-Forward (CF-INV4-W3-2-STAGE1) as a session-track gate, NOT an in-session edit. An investigation result enters the knowledge index only when promoted into a `/rclab-plan` session-mode plan and re-computed under a `session-{N}` gate (track-local boundary, intentional).
- [x] No `canonical_constants.py` writes — the Sage-exact values (`g_M/Z(∞) = 4.2664`, `rel_L10 = 100.1263`, `α_growth = +2`) are cross-checks of existing canonicals (`a_2_FW_zeta = 2776.165389`, S88-A-N-FW-CANONICALIZATION), not new framework predictions; no new constant warranted.

---

## Carry-Forward Computations

Three genuine future-work items. Per the track-local boundary, ALL THREE are session-track gates (lifted into a `/rclab-plan` session-mode plan, re-computed under `session-{N}` IDs); the workshop produced the STAGE-0 candidate, not the registration.

### CF-INV4-W3-2-GATE-A — `INV-FWD-HOMOGENEITY-VS-REGULATOR` (regulator-invariance of the apex dimension)

- **What**: At fixed channel geometry (a₂, substrate-distance pole s=3, d=8 cone, `α_growth = +2`), scan the dimensionful magnitude anchor `A(L; s=3)` across ≥3 structurally-distinct regulator classes — {ζ-native Mellin [done at S109: DIVERGENT], Pauli-Villars-subtracted partial sum at the SAME pole, heat-kernel `Tr e^{−tD²}` small-t a₂ coefficient at the same n=2 degree}. For each, record `(trend_sign, α_local(8→10), is_weyl_divergent)`. Tests: is the apex dimension regulator-INVARIANT (the live residual sp's A-3 caution keeps open)?
- **Inputs**: `s84_spectrum_cache_L12_tau019.npz` (L12 master spectrum, feasible — no high-L irrep build); `a_2_FW_zeta = 2776.165389` (canonical, cross-check only, anti-tautology guard: do NOT load as the target); S109 verdict line (the done ζ-native arm); the Pauli-Villars subtraction machinery at Λ_UV = M_KK; the heat-kernel small-t evaluator. Regulator-pin: tag each `a_2^{regulator}` per `regulator-pin-discipline.md` (`a_2^{ζ}`, `a_2^{Pauli-Villars}`, `a_2^{heat-kernel}`); Mellin pole-conv tag `poleconv-A-double`, `(pole_in_s=3, curvature_grade_n=2)`.
- **Gate**: `[SIGN]` + `[VERIFY-THEOREM]`. PASS (Reading a, TOP-LEFT): all ≥3 regulator classes DIVERGE with comparable `α_local ≈ +2…+4`, same `trend_sign=+1` ⇒ apex dimension is regulator-INVARIANT, `α_growth = d − 2s ≥ 0 ⇒ DIVERGENT` is a regulator-blind WALL. FAIL/flip (Reading b regulator-corollary, TOP-RIGHT): at least one regulator class BINDS (convergent, bounded) where ζ-native diverged ⇒ divergence carries a regulator label. Threshold: `α_local` sign-agreement across all classes (RATIO tolerance on `α_local` spread; pre-register `|α_local^{max} − α_local^{min}| < ` the heat-kernel-vs-zeta moment-ratio spread bound `O(20%)` per the regulator-class large-factor test).
- **Effort**: 1 compute gate; medium (3 regulator evaluations on a cached spectrum; PV + heat-kernel evaluators exist; no high-L work).

### CF-INV4-W3-2-GATE-B — `INV-FWD-RESIDUE-VS-PARTIALSUM` (functional-selection at fixed geometry)

- **What**: At fixed channel geometry (a₂, s=3, d=8 cone), evaluate THREE functionals on the SAME finite-L spectrum cache at L ∈ {8,10,12}: (1) `Φ_offpole(L) = Σ_{p+q≤L} m_{(p,q)} |λ|^{−6}` [done at S109: DIVERGES]; (2) `Φ_residue/finitepart(L)` = the s=3 Laurent reconstruction from the L-truncated zeta (contour/Cauchy or Richardson/Abel acceleration extraction of the principal-part + constant-term data, the honest finite-L continuation); (3) `Φ_logderiv(L) = d ln Φ_offpole/d ln L` (deg-0 Tier-1 re-anchor). Record `(trend_sign, α_local(8→12), L→∞ limit, |limit − g_M|/g_M)` per functional. Confirms the broad-class wall constructively (the one case the instance-string lacks: a NON-partial-sum functional at fixed geometry).
- **Inputs**: `s84_spectrum_cache_L12_tau019.npz`; the S108 route-c Richardson/Abel acceleration machinery (the honest continuation already run, landed `Z(∞)=650.70`); `a_2_FW_zeta = 2776.165389` (cross-check ONLY — anti-tautology guard, MANDATORY: extract the residue/finite-part FROM the spectrum, do NOT re-read `g_M`; the S109/S108 gates already operated under this guard). Sage MCP for the entire-function / Laurent-coefficient symbolic confirmation.
- **Gate**: `[VERIFY-THEOREM]` + `[SIGN]`. PASS (Reading b, BOTTOM-LEFT): `Φ_residue/finitepart(L)` BINDS to `g_M` (`|limit − g_M|/g_M → 0`, `trend_sign` not +1) while `Φ_offpole` diverges on the SAME spectrum ⇒ convergence is functional-SELECTION; held row anchorable; held-REASON scoped to partial-sum class. FAIL (Reading a, TOP-LEFT — both co-authors' prediction): `Φ_residue/finitepart` returns ≈0 (entire) OR reconstructs to `R`/`Z(∞)≈650.70`-type values with `|limit − g_M|/g_M ≳ O(1)`, and ONLY `Φ_logderiv` binds (Tier-1, `|plateau − α_growth| < ` envelope) ⇒ magnitude channel is genuinely Tier-2-DIMENSIONFUL regardless of functional. Threshold: `|Φ_residue limit − g_M|/g_M` against pass-band `< 1e-2` (publication precision of `a_2_FW_zeta`); INFO band `[1e-2, 1)`; FAIL `≥ 1`.
- **Effort**: 1 compute gate; medium (3 functionals on a cached spectrum; the acceleration machinery exists from S108).

### CF-INV4-W3-2-STAGE1 — STAGE-1-CANDIDATE registration of the unified criterion (session-track)

- **What**: Register the UNIFIED convergence criterion (the boxed `α_growth = d − 2s = n` / functional-partition statement + the Tier-1/Tier-2 scope) as a `STAGE-1-CANDIDATE` §VII entry in `sessions/permanent-results-registry.md`, per `joint-theorem-promotion.md` 4-stage pathway. This is a SEPARATE session-track gate, NOT effected in this workshop (track-local boundary). The Stage-1 entry carries: the 5-anatomy IS-not-IN elements (`cross-pillar-bridge-anatomy.md`); the 3-level ladder (Level-1 `[T^{(IV)}]_{a₂,HKR}=[g_M]_{a₂,HKR}` regulator-invariant; Level-2 the `L^{−α}` envelope; Level-3 the Tier-1 `7.500e-09` re-anchor at L_max=10); the Tier-2-DIMENSIONFUL wall classification on the dimensionful a₂ magnitude (held at `NOT-SATISFIED-PENDING-substrate-physical-scale-anchor`); pole-scope declaration (s=3 / n=2 / poleconv-A-double); the JOINT-clause flags (which clauses need Stage-2 cross-axis verify). REQUIRES Gate A + Gate B verdicts as the empirical anchor of the criterion's (c)-resolution (the 2×2 cell).
- **Inputs**: this workshop doc (`level-3-magnitude-divergence.md`, the STAGE-0 artifact) — lifted as carry-forward into a `/rclab-plan` session-mode plan; Gate A + Gate B verdict lines (the 2×2 outcome); §VII.CB + §VII.AU existing registry entries (the recurring HELD instances the criterion governs); the S106-disposition-overtake observation (registry line 22011 reconciliation — the S106 "Tier-1-constructible" wording is post-S109 falsified and must be down-tagged by the `mack-cosmic-bridge`/registry sole-writer, NOT silently). `mack-cosmic-bridge` is the §7/inventory sole writer; the §VII registry-prose writer lands the entry.
- **Gate**: artifact-existence-with-content (METHODOLOGY/registry-landing class) — `STAGE-1-CANDIDATE` tag present, all 5 anatomy elements + 3 levels declared, pole-scope declared, JOINT-clause flags present, Tier-2-DIMENSIONFUL classification + the Tier-1 re-anchor as the registry-PASS object both present. Stage-2 (two-agent cross-axis independent-verify, WITHOUT prior workshop context — NOT sp/lizzi) and Stage-3 (permanent) are FURTHER gates beyond this CF.
- **Effort**: 1 registry-landing gate (Stage-1) + 1 Stage-2 cross-axis-verify gate (two reviewers, parallel, axis-distinct from sp/lizzi); medium. Depends on: CF-INV4-W3-2-GATE-A + CF-INV4-W3-2-GATE-B (the 2×2 empirical anchor) — Stage-1 may register the criterion's STRUCTURE before the gates land, but the (c)-clause empirical anchor needs both verdicts.
