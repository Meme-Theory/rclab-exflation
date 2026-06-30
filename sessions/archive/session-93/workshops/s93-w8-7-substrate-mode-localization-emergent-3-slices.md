# Workshop 6 — Substrate Mode Localization on Emergent 3-Slices

**Gate**: `S93-W8-7-NARROW-PATH-WORKSHOP-6-DISPATCH` (GATED ON W8-3)
**Format**: 2-agent adversarial workshop — `phonon-first-cosmologist` (coordinator) + `connes-ncg-theorist` perspectives — N=3 rounds (R1 steelman / R2 respond / R3 converge)
**Target object**: the Reading-(b) Hochschild cocycle representative `[S_exit-horizon]^♯` at the acoustic-white-hole **exit-horizon** 2-surface (τ~0.16), and the bridge coefficient `α_bridge` it would deliver
**Date**: 2026-05-24
**Workshop document for**: §IX.7 narrow-path Step-4 projection operator `Π̂_S : H_K → H_S`

---

## Numbers first (upstream verdicts on disk)

Both upstream verdicts are read from `computations/session-93/s93_gate_verdicts.txt`.

### W8-3 (joint Cauchy-Schwarz / area-volume pre-flight) — **INFO**

3-tuple: `sign=PASS, magnitude=FAIL, regime=MARGINAL`; composite **INFO**; `value='band-edge-convention-ambiguous-DEFERRED-PENDING'`. Pinned numbers from the verdict line:

| Quantity | Value | Meaning |
|:---------|:------|:--------|
| `s_CS` (Cauchy-Schwarz floor slack) | **0.0186** | `F_0·F_2 − F_1² ≥ 0` holds (sign≥0, always) — moment floor PASSES |
| `α_req` (required `α_bridge`) | **4.810e-3** | `= γ_BH/49.34 = 0.2375/49.34` (canonical `ALPHA_BRIDGE_REQUIRED_FW`) |
| `α_win_lo` (substrate-admissible α floor) | **6.381e-3** | substrate window lower edge from moment-ratio + N_e bulk-to-surface reduction |
| `oom_below` | **0.12** | `log10(6.381e-3 / 4.810e-3)` — α_req is **0.12 OOM BELOW** the substrate floor |
| `γ_BH` (SU(2)-convention Immirzi) | **0.2375** | `GAMMA_BH_SU2_CONVENTION_LQG` (Paper 03 §VII) |
| DL/Meissner SU(2) band | **[0.2722, 0.2741]** | `inDL = False` — **EXCLUDES** γ_BH |
| full prescription-spread | **[0.1274, 0.2741]** | `inSpread = True` — **CONTAINS** γ_BH |

Two independent legs are inside this single INFO:
- **Substrate magnitude leg** (`α_req` vs `α_win_lo`): FAIL by 0.12 OOM, and this is **prescription-INDEPENDENT** — the substrate window `α_win_lo = 6.381e-3` is fixed by the substrate's own moment ratio `F_2/F_1` and the `N_e = 2.92` bulk-to-surface reduction; no LQG state-counting prescription enters it.
- **LQG band-containment leg** (γ_BH vs band): **prescription-AMBIGUOUS** — γ_BH=0.2375 is excluded by the DL/Meissner SU(2) band but contained by the full prescription-spread. The band-edge depends on which state-counting prescription (DL/Meissner SU(2) vs Ghosh-Mitra vs U(1)-ABCK) is declared.

### W8-6 (pre/post Bogoliubov ratio) — **PASS**

Final canonical line (supersedes the prior FAIL emission):

| Quantity | Value | Meaning |
|:---------|:------|:--------|
| `R_BG = α_bridge^pre/α_bridge^post` | **6.838562903e-4** (`6.84e-4`) | `= 1/cosh(2r)`, the reciprocal SU(1,1) squeeze weight |
| `W_BG = cosh(2r)` | **1462.30** | post-fold bridge coefficient is ~1462× LARGER than pre-fold |
| covariance residual | **exactly 0** | substrate Bogoliubov `U_B` descends to a covariant projection-conjugation at the kinematical `H_K` layer |
| sign | **derived unconditionally** | `W_BG > 1` is alignment-independent (NOT sign-deferred) |

`R_BG < 1` pins the pre/post **relative** constraint for any future `[S_exit-horizon]^♯` construction: the pre-fold bridge coefficient is suppressed relative to post-fold by the squeeze weight `cosh(2r) = 1462.30`.

### Constants ledger (knowledge-MCP confirmed)

- `ALPHA_BRIDGE_REQUIRED_FW = 0.00481` (S92; `= γ_BH/49.34`)
- `SCALE_BRIDGE_PREFACTOR_FW = 49.34` (`= (M_Pl_red/M_KK)²/(4√3π)`; pure arithmetic, no new substrate physics)
- `GAMMA_BH_SU2_CONVENTION_LQG = 0.2375` (SU(2)-convention). **Critical**: the U(1) Chern-Simons convention value is `γ_0 ≈ 0.127` (factor ~1.87 difference); the canonical_constants provenance flags that "mixing conventions across cross-framework comparisons is a Class-(c) PIN-DRIFT-FROM-STALE-SOURCE risk." Note the full prescription-spread FLOOR (0.1274) is essentially the U(1)-ABCK value 0.127.

---

## W8-3-keyed dispatch decision (substitution chain, plan §W8-7 Step 1–5)

```
Claim: "Because W8-3 is INFO (band ambiguous), Workshop 6 MUST NOT dispatch the
        full Step-4 cocycle construction against an ambiguous target; it instead
        adjudicates the well-posed sub-questions and converges on INFO."

Step 1 [Definition]: W8-3 verdict = INFO (band-edge-convention-ambiguous).
        [canonical: computations/session-93/s93_gate_verdicts.txt:170]
Step 2 [W8-3 PASS]:  N/A — W8-3 is not PASS, so the canonical-LQG-matching
        target is NOT selected.
Step 3 [W8-3 FAIL]:  N/A — W8-3 is not a clean FAIL either; the substrate
        magnitude leg FAILs but the band-containment leg is undecided, so the
        composite is INFO, not FAIL.
Step 4 [W8-3 INFO]:  band ambiguous ⇒ determine the area-volume band edges
        FIRST (declare a single state-counting prescription), THEN re-key the
        workshop target. Do NOT dispatch the full construction against an
        ambiguous target. [Wave 8 Decision Point table, plan line 1349:
        "INFO (j-band ambiguous) | determine area-volume band edges first,
        THEN re-key W8-7 | Regime III → INFO (deferred-pending) | refined
        area-volume band computation (S94 carry-forward) before W8-7 dispatches"]
Step 5 [W8-3 unmet]: N/A — W8-3 IS met (it has an INFO line on disk).

Conclusion: the workshop converges on INFO. The full [S_exit-horizon]^♯
        construction + α_bridge OOM estimate is DEFERRED to S94, keyed to a
        refined area-volume band determination under a SINGLE declared
        state-counting prescription. R_BG from W8-6 pins the pre/post relative
        constraint for that future construction.
```

This is the correct, honest structural outcome — NOT a shortfall. Per `math-scripts.md §"All Results Are Good Results"`, INFO is a structured pre-registered outcome (the plan's Wave-8 Decision Point pre-anticipated the INFO branch and routed it to band-determination-first). It is not framed apologetically and is not iterated toward PASS.

---

## R1 — Steelman (each agent states the strongest form of its own constraint)

### R1-A (phonon-first-cosmologist): the substrate constraints on `[S_exit-horizon]^♯`

**Substrate framing (IS-not-IN).** The exit horizon at τ~0.16 IS the substrate's distinguished 2-surface — the supersonic-transit causally-disconnecting boundary of the Six-Layer Causal Structure (S70). It is not a slice we draw IN a pre-existing spacetime; it is where the fabric's a_4 BCS-condensation kinematics becomes the causal boundary. The substrate's `√(C_2(p,q))` mode spectrum projected onto this 2-surface is PRIMARY; the LQG area operator `A_p = 8πγℓ_P²√(j_p(j_p+1))` is the candidate emergent shadow. Explanation flows substrate → emergent.

Two hard substrate constraints bound the Reading-(b) cocycle:

**(C-i) Cauchy-Schwarz moment floor (from W8-3 PART A).** The spectral SUM moments satisfy `F_0·F_2 ≥ F_1²` with slack `s_CS = 0.0186 ≥ 0`. This is a substrate-IS structural identity — it holds at every L_max, regulator-invariantly (it is the discrete Cauchy-Schwarz inequality on the Peter-Weyl-weighted spectrum, KO-dimension-independent — my registered permanent result `Cauchy-Schwarz F_0·F_2 ≥ F_1²` on any spectral triple). The cocycle `[S_exit-horizon]^♯`, whatever its representative, must respect this floor: its pairing against the mode classes cannot manufacture a bridge coefficient that violates the moment inequality. The floor is satisfied (sign PASS), so it does NOT pre-forbid the construction — but it constrains the achievable `α_bridge` from below through the moment ratio.

**(C-ii) Substrate-admissible α window (the magnitude leg).** Here is the steelman of the Regime-II case. The substrate window floor `α_win_lo = 6.381e-3` is set by the substrate's OWN moment ratio + the `N_e = 2.92` bulk-to-surface reduction. The required `α_req = 4.810e-3` sits **0.12 OOM BELOW** that floor. This magnitude FAIL is **prescription-INDEPENDENT**: it does not care which LQG state-counting prescription is chosen, because `α_win_lo` is a substrate quantity. The `N_e = 2.92` anchor is the only landed instance of a substrate-side bulk-to-surface reduction at landing magnitude, and it produces O(1) outputs, not 10⁻³-suppressed ones. My substrate-side prior (registered in the bridge-class doc): P(Regime II) ≥ 0.6. The magnitude leg is fully consistent with that prior.

**(C-iii) Bogoliubov covariance (from W8-6).** `R_BG = 1/cosh(2r) = 6.84e-4`, covariance residual exactly 0. The substrate Bogoliubov `U_B` (S38 PROVEN, P_exc=1.000, 59.8 GGE pairs) descends to a covariant projection-conjugation at the kinematical `H_K` layer. This means a pre-fold `Π̂_S^pre` and a post-fold `Π̂_S^post` are NOT independent — they are `U_B`-conjugate, and the bridge coefficients they yield are locked at ratio `R_BG`. So even though the absolute `α_bridge` awaits the explicit projection operator, the pre/post RELATIVE structure is already pinned: post-fold is ~1462× the pre-fold coefficient.

**R1-A position**: The substrate magnitude leg (C-ii) already settles the Regime question prescription-independently in the Regime-II direction. The cocycle existence and Bogoliubov covariance are satisfiable; the obstruction is the magnitude, and the magnitude is a substrate fact.

### R1-B (connes-ncg-theorist perspective): the HKR-Cheeger-Simons bridge-map-class admissibility

**The bridge map is class-identified, not yet anchored.** Per the S92 closure, the Reading-(b) Step-4 map is the **HKR (Hochschild-Kostant-Rosenberg) image with `-Cheeger-Simons` scheme suffix** (foliation-aware), per `cross-pillar-bridge-anatomy.md §"Bridge-map-scheme suffix discipline"`. The cocycle `[S_exit-horizon]^♯ ∈ HH^•(A_K)` lives at the **cohomology-class layer** — Level-1 of the Three-Level ladder — which is **regulator-invariant by construction**. The L_max truncation appears only at Level-2 (the `L^{-α}` envelope) and Level-3 (the numerical anchor), NEVER at Level-1.

**Why the cocycle class is well-defined independent of the LQG prescription.** This is the connes-side steelman. The Hochschild cohomology class `[S_exit-horizon]^♯` is an intrinsic object of the spectral triple `(A_K, H_K, D_K)`. Its existence and its cohomology class do not reference any LQG state-counting convention — they are fixed by the substrate algebra `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` and the a_4-kinematics-carrying representative at the exit horizon. The HKR theorem gives the isomorphism `HH^•(A_K) ≅ Ω^•(A_K)` (orientability axiom + Chern character); the `-Cheeger-Simons` suffix records that the foliation by Σ-slicings of the emergent post-fold 4-manifold is load-bearing (Cheeger-Simons 1985 differential character at full-leaf-foliation). The class is structurally honest as the Step-4 reading.

**Where the prescription DOES enter.** The prescription enters at the LAB-IN side (Element 2 of the 5-anatomy), not the substrate-IS side. The laboratory-IN observable is the LQG area-operator eigenvalue contribution `A_p` on the Ashtekar-Lewandowski kinematical Hilbert space — and the Immirzi γ in `A_p` is what carries the state-counting-prescription dependence (SU(2) Domanski-Lewandowski/Meissner vs Ghosh-Mitra vs U(1)-ABCK). The bridge map composes the substrate cocycle THROUGH this prescription-dependent pre-substrate pin (γ), so per `cross-pillar-bridge-anatomy.md §"Element 3 fiducial-anchor binding discipline"` the entry must declare which incarnation of γ binds: (i) substrate-self-consistent, (ii) external-observation, or (iii) joint-hypersurface. Currently the binding is UNDECLARED because the prescription is unfixed — that is exactly the W8-3 INFO.

**R1-B position**: The cocycle class is well-defined and regulator-invariant independent of the LQG prescription. But the Level-3 numerical anchor — the actual `α_bridge` the bridge map delivers when composed against `A_p` — cannot be pinned until a single state-counting prescription is declared, because the prescription sets the band-edge against which the matching is tested. Building the explicit representative against an ambiguous band is premature.

---

## R2 — Respond (each agent addresses the other's best case)

### R2-A (phonon-first responds to connes' bridge-class admissibility)

Connes is right that the cocycle class is regulator-invariant and prescription-independent at Level-1 — I accept that fully; it is consistent with my own registered result that the moment floor `F_0·F_2 ≥ F_1²` is KO-dimension-independent and holds on any spectral triple. The Level-1 existence is NOT the obstruction.

But here is my sharper claim, addressing connes' "premature to build against an ambiguous band": **the prescription-independent substrate magnitude FAIL already settles Regime II regardless of the band ambiguity.** Walk the logic:

- The band-containment leg asks: "does γ_BH=0.2375 fall inside the LQG area-volume band?" That is a question about whether the EMERGENT target is self-consistent.
- The magnitude leg asks: "can the substrate DELIVER `α_bridge ≥ α_win_lo = 6.381e-3`?" That is a question about the SUBSTRATE's reach.
- `α_req = 4.81e-3 < α_win_lo = 6.381e-3` by 0.12 OOM. The substrate's reachable `α_bridge` floor is ABOVE the required value. So even if some prescription were chosen that makes the band contain γ_BH (the full-spread reading), the substrate still cannot produce a small enough `α_bridge` to land at γ_emergent = γ_BH. The substrate window forbids it from below.

So the substrate magnitude leg is the more decisive of the two legs, and it points to Regime II prescription-independently. The band ambiguity affects WHICH target the emergent side would want; the substrate magnitude affects WHETHER the substrate can reach any sub-floor target at all — and it cannot.

**However** — and this is why I do NOT push to FAIL — the 0.12 OOM is small. It is a 1.33× factor (`6.381/4.810 = 1.327`), not the ~200× Regime-II structural-failure gap. A 0.12 OOM substrate-window edge is within the kind of refinement that a more careful exit-horizon localization (the actual `[S_exit-horizon]^♯` representative, vs the moment-ratio proxy used in W8-3) could move. The W8-3 window floor is computed from a moment-ratio + N_e proxy, NOT from the explicit cocycle. So I will not over-claim: the magnitude leg FAVORS Regime II, but a 0.12-OOM edge is not the same epistemic object as the ~200× γ_emergent~50 structural failure. The honest verdict is INFO with the magnitude leg recorded as Regime-II-favoring and prescription-independent.

### R2-B (connes responds to phonon-first's "magnitude leg settles it")

I accept that the magnitude leg is prescription-independent and Regime-II-favoring. But I push back on letting it close the gate to FAIL, for two structural reasons:

**(1) The two legs test different anatomy elements and must not be collapsed.** The magnitude leg is a constraint on the substrate-IS side (Element 1: can the substrate deliver the value). The band leg is a constraint on the lab-IN side (Element 2: is the emergent target self-consistent under a declared prescription). Per the algebra-axis orthogonality discipline, conflating a substrate-IS constraint with a lab-IN constraint into a single PASS/FAIL is exactly the cross-corner co-primary that the bridge-anatomy rules forbid. The composite must remain INFO until BOTH legs are individually decided under a fixed convention — and the band leg is NOT decided.

**(2) The 0.12-OOM proxy floor is not the bit-exact substrate canonical.** Phonon-first concedes this: the `α_win_lo = 6.381e-3` window edge is a moment-ratio + N_e PROXY, not the explicit `[S_exit-horizon]^♯` cocycle evaluation. Per `substrate-first-canonical-sourcing.md §(iv-bis)` (surrogate-vs-canonical at the cohomology-class layer), a surrogate FAIL is uninformative on the canonical's PASS/FAIL prediction unless the surrogate's sign/magnitude is mechanically locked to the canonical. Here the proxy and the cocycle could differ by an O(1) factor — and 0.12 OOM IS an O(1) factor (1.33×). So a clean FAIL would be a surrogate-FAIL → canonical-FAIL inference that the rules explicitly forbid at this layer. The correct move is to DEFER the canonical `α_bridge` to the explicit construction.

**On the prescription recommendation.** Since the band leg is the undecided one, the decisive next step is to declare a single state-counting prescription. My recommendation: **DL/Meissner SU(2)** — for three reasons. (a) `γ_BH = 0.2375` was itself pinned in the SU(2) convention (Paper 03 §VII), so testing it against the SU(2) area-volume band is the convention-consistent comparison; testing the SU(2)-convention γ against the U(1)-spread band is the Class-(c) PIN-DRIFT-FROM-STALE-SOURCE risk that the canonical_constants provenance explicitly warns about. (b) The DL/Meissner SU(2) band [0.2722, 0.2741] is the narrow, prescription-internally-consistent band; the full spread [0.1274, 0.2741] is a UNION across mutually-incompatible prescriptions and is not itself a physical band any single LQG quantization realizes. (c) The full-spread FLOOR (0.1274) is essentially the U(1)-ABCK value (0.127) — mixing it with the SU(2)-pinned γ is precisely the convention-mixing the framework's own pin discipline flags. Under DL/Meissner SU(2), `inDL = False` ⇒ γ_BH is EXCLUDED ⇒ the band leg would point to FAIL too — which would CORROBORATE the substrate magnitude leg from the lab-IN side. But the recommendation itself, and the band-edge recomputation under it, is the S94 deliverable; we declare the recommendation here, we do not execute the recomputation against it here.

---

## R3 — Converge (Workshop Verdict: INFO)

Both agents converge on **INFO**. The convergence has three load-bearing components, exactly as pre-registered in the spawn directive and the plan's Wave-8 Decision Point.

### (i) The substrate magnitude leg is prescription-INDEPENDENT and Regime-II-favoring

`α_req = 4.810e-3` sits **0.12 OOM (a 1.33× factor) BELOW** the substrate-admissible floor `α_win_lo = 6.381e-3`. This window floor is set by the substrate's own moment ratio + the `N_e = 2.92` bulk-to-surface reduction — NO LQG state-counting prescription enters it. The magnitude leg therefore decides in the Regime-II direction **independent of the band ambiguity**, consistent with the substrate-side prior P(Regime II) ≥ 0.6. The Cauchy-Schwarz moment floor (`s_CS = 0.0186 ≥ 0`) is satisfied — it does not pre-forbid the construction. Both agents agree this leg is decided and prescription-independent.

**Caveat held jointly**: the 0.12-OOM edge is a moment-ratio + N_e PROXY, not the explicit `[S_exit-horizon]^♯` cocycle evaluation. 0.12 OOM is an O(1) factor, NOT the ~200× γ_emergent~50 structural-failure gap. Per `substrate-first-canonical-sourcing.md §(iv-bis)`, a proxy FAIL at this margin is not promotable to a canonical FAIL. The magnitude leg FAVORS Regime II; it does not yet PROVE it at the cocycle layer.

### (ii) The LQG band-containment leg requires a SINGLE declared state-counting prescription — RECOMMENDED: DL/Meissner SU(2)

The band-containment of `γ_BH = 0.2375` is prescription-DEPENDENT: EXCLUDED by the DL/Meissner SU(2) band [0.2722, 0.2741] (`inDL = False`); CONTAINED by the full prescription-spread [0.1274, 0.2741] (`inSpread = True`). The band leg cannot decide PASS/FAIL until a single prescription is declared.

**Joint recommendation: DL/Meissner SU(2).** Rationale (convergent across both agents):
1. **Convention-consistency**: `γ_BH = 0.2375` was pinned in the SU(2) convention (Paper 03 §VII). Testing an SU(2)-convention γ against the SU(2) area-volume band is the convention-internally-consistent comparison. Testing it against the full spread (whose floor 0.1274 ≈ the U(1)-ABCK 0.127) is the Class-(c) PIN-DRIFT-FROM-STALE-SOURCE convention-mixing risk the canonical_constants provenance explicitly warns against.
2. **Physical band vs union**: the DL/Meissner SU(2) band [0.2722, 0.2741] is a narrow band internal to ONE quantization; the full spread [0.1274, 0.2741] is a UNION across mutually-incompatible prescriptions and is not a band any single LQG quantization realizes.
3. **Corroboration direction**: under DL/Meissner SU(2), `inDL = False` ⇒ γ_BH excluded ⇒ the band leg would CORROBORATE the substrate magnitude leg's Regime-II direction from the independent lab-IN side. (This corroboration is anticipated, not asserted as a verdict — the band-edge recomputation under the declared prescription is the S94 deliverable.)

### (iii) The explicit `[S_exit-horizon]^♯` construction + `α_bridge` OOM estimate is DEFERRED to S94

The full Reading-(b) cocycle representative and its delivered `α_bridge` order-of-magnitude estimate are DEFERRED to S94, keyed to the refined area-volume band determination under the single declared (DL/Meissner SU(2)) prescription. The bridge-class doc (`lqg-narrow-path-bridge-class.md`) remains at `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION`; this workshop does NOT promote it to STAGE-1-CANDIDATE, because the Level-3 anchor (the actual `α_bridge`) is not extracted here. `R_BG = 6.84e-4 = 1/cosh(2r)` from W8-6 pins the pre/post RELATIVE constraint for that future construction (post-fold coefficient ~1462× the pre-fold), so the deferred construction inherits a substrate-derived relative anchor even before the absolute magnitude lands.

### Why dispatching the full construction now would be wrong

Per the plan substitution chain Step 4 [W8-3 INFO] and the Wave-8 Decision Point (line 1349), forcing the Step-4 cocycle construction against an ambiguous band would be building a Level-3 anchor against an undefined target — a PRU-class plan-authorship defect (the prescription is a gate-relevant machinery parameter left unpinned). The honest structural move is to fix the band edges first (declare the prescription), then re-key the construction. This is the correct, pre-anticipated INFO branch, not a shortfall.

---

## Workshop Verdict

**INFO** — Workshop 6 dispatched and adjudicated the well-posed sub-questions; converged on a deferred-pending structural verdict (NOT honest-mechanical-closure-unmet — W8-3 IS met with an INFO line; this is the W8-3-INFO-keyed convergence per plan Step 4).

- **Substrate magnitude leg**: prescription-INDEPENDENT, Regime-II-favoring (`α_req = 4.81e-3` is 0.12 OOM / 1.33× below `α_win_lo = 6.381e-3`); moment floor `s_CS = 0.0186 ≥ 0` satisfied.
- **LQG band leg**: prescription-AMBIGUOUS (γ_BH=0.2375 excluded by DL/Meissner SU(2), contained by full spread); RECOMMEND declaring DL/Meissner SU(2) (convention-consistency + physical-band + corroboration).
- **Explicit `[S_exit-horizon]^♯` + `α_bridge` OOM**: DEFERRED to S94 with a 4-field carry-forward, keyed to the refined area-volume band under the declared prescription. `R_BG = 6.84e-4` pins the pre/post relative constraint.
- **Reading (d)** (Connes-distance localization on state space) remains the filed substrate-pure alternative if the Reading-(b) construction encounters an obstruction at the S94 dispatch.

**4-tuple**: `scheme=narrow-path-workshop-6-substrate-mode-localization-emergent-3-slices-reading-b-cocycle`, `convention=NARROW-PATH-workshop-6-exit-horizon-tau-0p16-Hochschild-cocycle-HKR-Cheeger-Simons-W8-3-keyed-target`, `L_max=12`.

---

## Carry-forward (4-field spec) — to S94

### CF-S94-NARROW-PATH-WORKSHOP-6-COCYCLE-CONSTRUCTION — explicit `[S_exit-horizon]^♯` + `α_bridge` OOM under declared prescription

| Field | Content |
|:------|:--------|
| **What** | (a) Recompute the LQG area-volume band edges under the SINGLE declared **DL/Meissner SU(2)** state-counting prescription (resolving the W8-3 band ambiguity); (b) build the explicit Reading-(b) Hochschild cocycle representative `[S_exit-horizon]^♯ ∈ HH^•(A_K)` at the τ~0.16 exit horizon carrying the a_4 BCS-condensation kinematics; (c) extract the delivered `α_bridge` OOM estimate and the resulting `γ_emergent = α_bridge · 49.34`; (d) re-key the Regime verdict against the band recomputed in (a). |
| **Inputs** | W8-3 verdict (`s_CS=0.0186`, `α_req=4.810e-3`, `α_win_lo=6.381e-3`, band data); W8-6 `R_BG = 6.84e-4` pre/post relative constraint; `s84_spectrum_cache_L12_tau019.npz` (substrate spectrum, L_max=12); W8-2 Casimir table + Friedrich-Bär scaling `min|λ| = 0.4754·√(C_2+1) − 0.0036`; `ALPHA_BRIDGE_REQUIRED_FW=0.00481`, `SCALE_BRIDGE_PREFACTOR_FW=49.34`, `GAMMA_BH_SU2_CONVENTION_LQG=0.2375`; `lqg-narrow-path-bridge-class.md` 5-anatomy block; LQG Paper 04 (Bojowald 2001) area-volume uncertainty + Paper 03 §VII (DL/Meissner SU(2) state counting). |
| **Gate** | `α_bridge` OOM extraction is CONVERGED (a value pinned). Regime selection: Regime I (PASS) if `\|α_bridge − 4.81e-3\|` within ~1 OOM AND γ_emergent within rel_tol of γ_BH=0.2375 under the declared SU(2) band; Regime II (FAIL, structural) if `α_bridge ≳ 0.1` (~200× / γ_emergent~50, no γ-cutoff-running recovery per Paper 03 §VII); Regime III (INFO) if (p,q)-dependent / intermediate. The 0.12-OOM proxy edge must be resolved by the explicit cocycle, NOT the moment-ratio proxy. |
| **Effort** | ~1–2 wave-equivalents (band-edge recomputation <0.1 we; explicit cocycle representative construction is the substantive new-construction cost; `α_bridge` extraction on the existing L_max=12 cache, GPU-venv python). |

**Depends on**: W8-3 INFO band data (UPSTREAM, this session); W8-6 `R_BG` PASS (UPSTREAM, this session); `s84_spectrum_cache_L12_tau019.npz` (LANDED S84); W8-2 Casimir/Friedrich-Bär scaling (LANDED this session); `lqg-narrow-path-bridge-class.md` registry entry (LANDED S92).

---

## Cross-links

- Plan gate block: `sessions/session-plan/session-93-plan-w8.md §W8-7`
- Upstream verdicts: `computations/session-93/s93_gate_verdicts.txt` (W8-3 line 170; W8-6 final PASS line 181)
- Bridge-class registry (pending): `sessions/framework/correspondence/lqg-narrow-path-bridge-class.md`
- Phonon-first memory: `.claude/agent-memory/phonon-first-cosmologist/reference_s92-lqg-narrow-path.md`
- Bridge-map anatomy rules: `.claude/rules/cross-pillar-bridge-anatomy.md` (5-anatomy + 3-level ladder; Element 3 fiducial-anchor binding; Bridge-map-scheme suffix discipline; Deferred-pending intermediate verdict-class)
- Substrate framing: `.claude/rules/phononic-framing.md §"IS Space, Not IN Space"`
- INFO-is-a-result discipline: `.claude/rules/math-scripts.md §"All Results Are Good Results"`
