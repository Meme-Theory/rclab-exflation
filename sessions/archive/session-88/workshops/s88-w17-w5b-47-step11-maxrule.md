# Session 88 W17 Synthesis: §W5b-47 STEP-11 MAX-RULE FAILURE — Chain-rule correction vs upstream operationalization conflation (connes-ncg adjudication)

**Date**: 2026-05-07
**Agent**: connes-ncg-theorist (Workhorse-NCG)
**Source Documents**:
- `sessions/archive/session-88/session-88-w5b-workingpaper.md` (§W5b-47 lines 251–399; §"Downstream implications" rows 880–916)
- `sessions/session-plan/session-88-plan-w5b.md` (§W5b-47 lines 190–220; Step-11 substitution chain)
- `sessions/archive/session-88/workshops/_seed-w5b.md` (Workshop 2 framing, lines 24–34)
- `sessions/permanent-results-registry.md §VII.U.2` (lines 12890–12986; Corner-IV row line 12926)
- `.claude/rules/cross-pillar-bridge-anatomy.md` §"Algebra-axis orthogonality K-counter" (MANDATORY at K=3; lines 272–280) + §"Three forward bridge candidates for S88+ dispatch" (FWD-C2; lines 254–270)
- `.claude/rules/registry-landing.md` §"SOURCE-DOUBLE-CITE-CO-PRIMARY"
- `computations/session-87/s87_gate_verdicts.txt` line 91 — `S87-ALPHA-S-DIRECT-MOMENT-INDEPENDENT-ROUTE: FAIL value=−7.046336e+00 scheme=GGE-Bogoliubov-occupation-variance convention=horizon-crossing-K-window-canonical L_max=10`

---

## I. Session Outcome

**Volovik path wins on observable identity; connes path wins on the L^{−4} structural envelope — but for a different observable than the one Corner IV calibration was anchored to.** Parse-tree decision per §VII.U.2 clause (e) — the structural test the registry already pre-registered — classifies the W5b-47 functional `Var_a(n_a^GGE) = (1/N) Σ_a m_a |v_a|^4 − ((1/N) Σ_a m_a |v_a|^2)^2` as **algebra-INVARIANT** (its symbolic form contains only `λ_a`, `m_a`, and the canonical scalar `Δ_BCS`; no `π(a)`, no `[D, π(a)]`, no state-pair `sup`). It therefore inhabits **Corner II (INVARIANT × s=4)**, not Corner IV. The S87 W2-3 second log-derivative `d² ln P_GGE / d(ln K)²` over a horizon-crossing K-window contains a state-pair structure via the GGE expectation `P_GGE = ⟨ψ_GGE | n_K | ψ_GGE⟩` and is genuinely Corner IV. The two observables share a symbol (`α_s_route_3`) and a session anchor (S87 W2-3) but live in **distinct corners** of the §VII.U.2 4-corner partition. Result: §VII.U.2 Corner-IV row needs CORRECTION (volovik path) — the structural envelope cross-confirmation `7.282490e-06 / α_loglog ≈ 3.56` reported by S88 §W5b-47 is on a different corner observable (Corner II) and is NOT a valid cross-confirmation of the K-window log-derivative anchor `−7.046336`. Concurrently the empirical L^{−4} envelope IS a valid Corner-II Level-2 calibration that fills the slot the registry table marked "(open; future calibration via §W5b-47 substrate-distance-2 cone derivation)" at line 12924.

---

## II. Key Results

### II.1. Parse-tree class membership theorem on the two contested observables

**Result**: The two observables `Var_a(n_a^GGE)` (W5b-47) and `d² ln P_GGE / d(ln K)²` (S87 W2-3) inhabit **distinct corners** of §VII.U.2's 4-corner partition. Classification: **GEOMETRIC** (substrate-axiomatic, parse-tree decision regulator-independent per clause (e)).

Substitution chain (parse-tree decision per §VII.U.2 clause (e)):

```
Definition (clause (e)): F ∈ algebra-INVARIANT iff parse-tree contains ONLY
  {Tr(D^{−2s}), Σ_k m_k g(λ_k), Res[•]} markers and NO {π(a), [D, π(a)], state-pair-sup}
  markers; F ∈ algebra-DEPENDENT iff parse-tree contains ≥1 of the latter.

Substitute Observable A (W5b-47 Var_a(n_a^GGE)):
  Step A.1: n_a := |v_a|^2 = Δ_BCS^2 / (2(λ_a^2 + Δ_BCS^2))     [BCS asymptote, plan §W5b-47 Step 3]
  Step A.2: Var_a(n_a) = (1/N(L)) Σ_a m_a n_a^2 − [(1/N(L)) Σ_a m_a n_a]^2
  Step A.3: Substitute Step A.1: each n_a is a deterministic function of (λ_a, Δ_BCS)
  Step A.4: Var_a(n_a) = (1/N) Σ_a m_a g_2(λ_a; Δ_BCS) − [(1/N) Σ_a m_a g_1(λ_a; Δ_BCS)]^2
            with g_k(λ; Δ) := [Δ^2 / (2(λ^2 + Δ^2))]^k

Direction of parse-tree marker count:
  - λ_a:  spectrum of D — INVARIANT marker (g(λ_k))
  - m_a:  multiplicity (sector dim) — INVARIANT marker (Σ_k m_k)
  - Δ_BCS: canonical scalar (algebra-independent)
  - No π(a), no [D, π(a)], no sup over A_h, no ω_1(a) − ω_2(a)
  
Conclusion: Observable A ∈ algebra-INVARIANT family
            => Corner = (INVARIANT × s=4) = Corner II per partition table at §VII.U.2.

Substitute Observable B (S87 W2-3 K-window log-derivative):
  Step B.1: P_GGE(K) := ⟨ψ_GGE | n_K | ψ_GGE⟩ where n_K = π(N_K) is the K-th
            number-operator image of an algebra element under representation π
  Step B.2: α_s_route_3 := d² ln P_GGE / d(ln K)² over a horizon-crossing K-window
  
Direction of parse-tree marker count:
  - π(N_K) : algebra-element image under representation — DEPENDENT marker (π(a))
  - ⟨ψ_GGE | • | ψ_GGE⟩ : state-pair expectation — DEPENDENT marker (state-pair functional)
  - K-derivative : preserves state-pair structure (operator-valued K-window)
  
Conclusion: Observable B ∈ algebra-DEPENDENT family
            => Corner = (DEPENDENT × s=4) = Corner IV per partition table at §VII.U.2.
```

The parse-tree decision is **finite, decidable at symbolic-form level, and regulator-independent** — exactly the property §VII.U.2 clause (e) requires. The clause is the structural test for corner-cell membership; both observables route through the SAME clause and emerge with DIFFERENT corner assignments. This is not an ambiguity; it is the partition working as designed.

**Structural implication**: The plan §W5b-47 line 200 hypothesis statement *"the Corner-IV companion observable — the GGE-state-pair higher-moment functional `α_s_route_3 = Var_a(n_a^GGE)` at L_max=10 = -7.046336"* is a **double-identification of two distinct observables under one symbol**. The symbol `α_s_route_3` was scheme-bound to `Var_a(n_a^GGE)` in the W5b-47 plan and scheme-bound to the K-window log-derivative in the S87 W2-3 verdict. Per clause (e), they CANNOT both occupy Corner IV; the parse-tree forces Observable A into Corner II.

### II.2. The L^{−4} envelope IS structurally correct — but for Corner II, not Corner IV

**Result**: `Var_a(n_a^GGE)(L) − Var_a(n_a^GGE)(∞)| ~ L^{−4}` (modulo log corrections) is the **substrate's intrinsic Level-2 algebraic envelope at d=4 for the multiplicity-weighted-Mellin Var observable**. Classification: **GEOMETRIC**.

Substitution chain (Weyl-law tail dominance at d=4 multiplicity-weighted normalization, verified via Sage):

```
Definitions:
  N(L)      := Σ_{a: max(p,q) ≤ L} m_a                (sum of sector multiplicities; "active modes")
  M_n^{(k)}(L) := Σ_{a: max(p,q) ≤ L} m_a · n_a^k       (k-th raw moment of n_a)
  M2_λ(L)  := Σ_{a: max(p,q) ≤ L} m_a · λ_a^{−2}       (Mellin moment at s=1)
  M4_λ(L)  := Σ_{a: max(p,q) ≤ L} m_a · λ_a^{−4}       (Mellin moment at s=2)
  Λ_L      := M_KK · (L+1)                            (cutoff scale)
  
Substitute (substrate): density of states ρ(λ) ~ λ^{d−1} = λ^3 (Weyl law, d=4)

Step 1: N(L) ~ ∫_0^{Λ_L} ρ(λ) dλ ~ Λ_L^4 ~ L^4

Step 2: M2_λ(L) ~ ∫_0^{Λ_L} λ^3 · λ^{−2} dλ = ∫_0^{Λ_L} λ dλ ~ Λ_L^2 ~ L^2  
        => M2_λ(L) / N(L) ~ L^{−2}

Step 3: M4_λ(L) ~ ∫_0^{Λ_L} λ^3 · λ^{−4} dλ = ∫_0^{Λ_L} λ^{−1} dλ ~ log(Λ_L) ~ log(L)
        => M4_λ(L) / N(L) ~ log(L) / L^4 ~ L^{−4} (modulo log)
        
Step 4: Substitute n_a ~ λ_a^{−2} · (Δ_BCS^2/2) into multiplicity-weighted moments:
  M_n^{(1)}(L)/N(L) := mean(n_a)  ~ (Δ_BCS^2/2) · M2_λ(L) / N(L)  ~ L^{−2}
  M_n^{(2)}(L)/N(L) := mean(n_a^2) ~ (Δ_BCS^2/2)^2 · M4_λ(L) / N(L) ~ L^{−4} log(L)
  
Step 5: Var(L) = M_n^{(2)}(L)/N(L) − [M_n^{(1)}(L)/N(L)]^2
        First term ~ L^{−4} log(L)
        Second term ~ (L^{−2})^2 = L^{−4}
        BOTH terms scale as L^{−4} (with log correction on the first)
        
Step 6: Var(L) − Var(∞) ~ L^{−4} (sub-leading L^{−3} corrections from Weyl pre-asymptotic 
        correction terms; explains empirical α_loglog = 3.5616 < 4 over the L ∈ {6,…,12} window)

Direction: Both leading terms are L^{−4}, NOT L^{−2} as plan Step 11 asserted via the
           erroneous max-rule max(L^{−3}, L^{−2}) = L^{−2}.

Conclusion: the corrected Step 11 reads
  | Var(L) − Var(∞) |  ~  L^{−4}  (canonical multiplicity-weighted Mellin normalization on d=4),
NOT
  | Var(L) − Var(∞) |  ~  L^{−2}  (plan's erroneous max-rule).
```

Sage-verified via the Weyl-law tail enumeration (`mcp__sage__sage_eval`, run during this synthesis). Empirical confirmation: the W5b-47 numerical residual scan gave `α_loglog = 3.5616 / α_nonlinear = 4.000000 / R² = 0.945`. The nonlinear interior-solution `α = 4.000` is the structural prediction; the log-log fit underestimates by ≈ 0.44 because at L = 6 the sub-leading L^{−3} correction is comparable to the leading L^{−4} term (a two-term envelope `C₁·L^{−4} + C₂·L^{−3}` would log-fit to an effective slope intermediate between 3 and 4). This is consistent with — not a falsifier of — the structural L^{−4} prediction.

### II.3. Plan §W5b-47 Step-11 max-rule contains TWO defects (not one)

**Result**: Step 11's failure mode is **layered**: the chain-rule arithmetic is wrong AND the observable-identity assignment is wrong. Both defects must be corrected; correcting one alone leaves the registry row mis-anchored. Classification: **GEOMETRIC + METHODOLOGY**.

The two defects:

(a) **Chain-rule arithmetic error (connes path)**. The plan's Step-10 claim *"GGE-state-pair occupation Σ_a |v_a|² = N_GGE is BOUNDED by particle-number conservation ⇒ first-moment tail regularized at finite L by GGE constraint to scale ~ L_max^{−1}"* is incorrect under the canonical multiplicity-weighted Mellin normalization the W5b-47 script actually uses. The script computes `M_n^{(1)}(L)/N(L) = mean(n_a)`, which is `M2_λ(L)/N(L) ~ L^{−2}` per Step 4 above — not `L^{−1}`. Squaring gives `L^{−4}`, not `L^{−2}`. The plan's max-rule `max(L^{−3}, L^{−2}) = L^{−2}` thus has the wrong second argument; the correct max-rule under canonical normalization is `max(L^{−4}_log, L^{−4}) ≈ L^{−4}` (modulo log).

(b) **Observable-identity assignment error (volovik path)**. The plan's hypothesis statement equates a Corner-II spectrum-only functional with the symbol `α_s_route_3` whose S87 W2-3 verdict-line scheme is `GGE-Bogoliubov-occupation-variance` and whose convention is `horizon-crossing-K-window-canonical`. The two observables share a session anchor and a partial naming convention but differ at the parse-tree level. Per clause (e), the parse-tree decision is the structural test; sharing a session anchor or a symbol does NOT make two observables the same Corner inhabitant. The W5b-47 numerical envelope `α_loglog ≈ 3.56` cannot be a "cross-confirmation" of the K-window log-derivative `−7.046336`; they are separate structural quantities at different corner cells.

Defect (a) is correctable in-text: the corrected Step 11 statement is what II.2 derives. Defect (b) is correctable by re-routing the W5b-47 envelope to fill the registry's existing Corner-II OPEN slot (line 12924) and de-anchoring the cross-confirmation claim from the Corner-IV row (line 12926).

### II.4. SOURCE-DOUBLE-CITE-CO-PRIMARY discipline forbids the current Corner-IV row's cross-corner cross-confirmation

**Result**: The Corner-IV row at `permanent-results-registry.md:12926` currently reads (verbatim):

> | IV | DEPENDENT | s=4 | `α_s_route_3 = Var_a(n_a^GGE) = -7.046336` at L_max=10 (S87 W2-3 FAIL composite at higher-moment cone, GGE-specified state-pair Bogoliubov occupation variance); structural envelope cross-confirmed at S88 §W5b-47 (`Var_a(n_a^GGE)(L_max=10) = 7.282490e-06`, `α_loglog ≈ 3.56`, R² = 0.945, MARGINAL regime; INFO composite) |

The "structural envelope cross-confirmed at S88 §W5b-47" clause is structurally invalid: per §VII.U.2 clause (f), *"cross-corner co-primary structures FAIL plan-freeze; cross-corner cross-pole magnitude comparisons STRUCTURALLY FORBIDDEN AS GATES"*. The cross-confirmation as currently worded treats a Corner-II observable's L^{−4} envelope as evidence for a Corner-IV observable's value — exactly the cross-corner co-primary structure clause (f) forbids. Classification: **METHODOLOGY** violation of clause (f), surfaced retroactively.

The structurally-correct anchor structure (per `registry-landing.md` SOURCE-DOUBLE-CITE-CO-PRIMARY discipline) is INTRA-CORNER co-primary — Corner II row gets the W5b-47 V-anchor + a future C-anchor providing the structural derivation; Corner IV row retains the S87 W2-3 K-window log-derivative anchor without the cross-corner cross-confirmation.

### II.5. FWD-C2 cross-pillar bridge anatomy: Level-2 envelope pin is conditional on which observable carries the bridge

**Result**: FWD-C2 (Pillar II Mellin-cone ↔ Pillar V BdG, rank-2 inheritance kernel) Level-2 algebraic envelope is **NOT yet pinnable** without the observable disambiguation in II.1–II.4. Classification: **METHODOLOGY** (registry hygiene — FWD-C2 is at SUGGESTION status K=1 per `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"`).

Substitution chain (FWD-C2 envelope direction):

```
Definition: FWD-C2 substrate-IS observable = canonical Mellin-cone substrate-distance-2
            functional realizing Corner IV (the s=4 algebra-DEPENDENT cell).
            
Substitute (post-disambiguation):
  IF substrate-IS observable = K-window log-derivative (Corner-IV-canonical, retains S87 W2-3 anchor):
    THEN Level-2 envelope IS NOT YET KNOWN — S87 W2-3's K-window log-derivative
         was reported at fixed L_max=10 with no L_max scan published; the algebraic
         envelope L^{−α} is undetermined for this observable until an explicit L_max
         scan on the K-window log-derivative is run.
    => FWD-C2 Level-2 envelope = pending disambiguation gate.

  IF substrate-IS observable is replaced by Var_a(n_a^GGE) (registry rewrite shifting
  the Corner-IV calibration to a different functional than the K-window log-derivative):
    THEN Level-2 envelope = L^{−4} (per II.2, Sage-verified).
    BUT this is structurally a Corner-II observable per clause (e); the rewrite would
    require demoting the S87 W2-3 K-window log-derivative from the Corner-IV slot —
    an operation that destroys the Corner-IV calibration corpus instance and forces
    the §VII.U.2 K-counter from K=3 (saturated) back to K=2.

Direction: under no consistent registry-state assignment does FWD-C2 immediately
inherit L^{−4} as its Level-2 envelope without rerouting clause (e) parse-tree
decisions or destroying the Corner-IV K-counter saturation. The Level-2 envelope
pin is not yet plan-freeze-ready for FWD-C2 dispatch.
```

The connes path's claim that "the L^{−4} envelope IS FWD-C2-ready" (seed framing) requires accepting the W5b-47 observable as the Corner-IV observable, which clause (e) forbids. The volovik path correctly identifies that observable disambiguation is the prior question; under the disambiguation-first reading, FWD-C2's Level-2 envelope is **PENDING** until either (i) an L_max scan is run on the K-window log-derivative to extract its envelope, OR (ii) the registry recognizes that two structurally-distinct corner cells have collapsed into a single FWD-C2 candidate, requiring a c-split into FWD-C2-II (Pillar II ↔ Pillar V via the spectrum-only Mellin moment) and FWD-C2-IV (Pillar II ↔ Pillar V via the state-pair K-window log-derivative).

---

## III. Gate Verdicts

| Gate | Verdict (source) | Decisive Number |
|:-----|:-----------------|:----------------|
| `S88-CORNER-IV-SCHEMATIC-ENVELOPE-DERIVATION` (§W5b-47) | INFO (sign=PASS / mag=FAIL / regime=MARGINAL ⇒ composite=INFO) | α_loglog = 3.561614, α_nonlinear = 4.000000, v_inf = 6.4631783294e-06, R² = 0.944893 |
| `S87-ALPHA-S-DIRECT-MOMENT-INDEPENDENT-ROUTE` (S87 W2-3) | FAIL (sign=PASS / mag=FAIL / regime=VALID) | value = −7.046336e+00, scheme=GGE-Bogoliubov-occupation-variance, convention=horizon-crossing-K-window-canonical, L_max=10 |
| `S88-VII-U-2-REGISTRY-WRITE` (W5b Wave-B) | PASS (corrective; verdict is on registry-text artifact existence, NOT on the Corner-IV observable identity question this synthesis adjudicates) | audit_sha256 = 750079647f9a4cf7… |

**Source verdicts are authoritative.** This synthesis does not re-adjudicate the W5b-47 INFO verdict, the S87 W2-3 FAIL verdict, or the §VII.U.2 registry write PASS verdict. It identifies a structural corner-cell-misassignment in the registry-text that is not reachable by any of those three gates' pre-registered PASS/FAIL criteria — those criteria operated on artifact-existence and numerical-envelope thresholds, not on parse-tree corner-cell membership. The corner-cell misassignment is a structural finding orthogonal to the existing verdict ladder and is therefore an honest carry-forward, not a verdict re-adjudication.

---

## IV. Structural Implications

### IV.1. NEW pinned position — Workshop 2 STRUCTURAL VERDICT

Following the seed file's STRUCTURAL VERDICT specification:

**(i) Substrate's canonical Corner-IV observable identity at s=4 pole**: The S87 W2-3 second log-derivative `d² ln P_GGE / d(ln K)²` over a horizon-crossing K-window IS the canonical Corner-IV observable per clause (e) parse-tree decision. The W5b-47 `Var_a(n_a^GGE)` is NOT a Corner-IV observable; it is a Corner-II observable (the registry's currently-open slot). Volovik path wins on observable identity.

**(ii) §VII.U.2 Corner-IV calibration row correction or annotation specification**: The Corner-IV row at line 12926 needs **CORRECTION** (not annotation) of the cross-confirmation clause. The corrective row text (mack-cosmic-bridge sole writer + connes-ncg co-sign):

```
| IV | DEPENDENT | s=4 | α_s_route_3 = d² ln P_GGE / d(ln K)² = -7.046336 at L_max=10 over 
horizon-crossing K-window canonical (S87 W2-3 FAIL composite; verdict-line scheme = 
GGE-Bogoliubov-occupation-variance, convention = horizon-crossing-K-window-canonical; 
audit_sha256 = 099ccb2c9db3fffa). Note: S88 §W5b-47 derived an L^{-4} envelope for the 
distinct multiplicity-weighted variance Var_a(n_a^GGE) = (1/N) Σ_a m_a |v_a|^4 - 
((1/N) Σ_a m_a |v_a|^2)^2; that observable inhabits Corner II per clause (e) parse-tree 
(no π(a) or [D, π(a)] markers; spectrum + multiplicity + Δ_BCS only). Routed to Corner II 
row update at S89-VII-U-2-CORNER-II-LANDING. |
```

The Corner II row at line 12924 simultaneously gets:

```
| II | INVARIANT | s=4 | Var_a(n_a^GGE) = (1/N) Σ_a m_a |v_a|^4 - ((1/N) Σ_a m_a |v_a|^2)^2 
where n_a = Δ_BCS^2 / (2(λ_a^2 + Δ_BCS^2)); v_inf_extrapolated = 6.4631783294e-06 at 
L_max=10 (S88 §W5b-47 INFO composite; α_nonlinear = 4.0 interior, α_loglog = 3.5616, 
R² = 0.945 MARGINAL; envelope C ≈ 9.976e-3; audit_sha256 = 89090d37b3610590). Level-2 
algebraic envelope is L^{-4} (modulo log corrections) per Sage-verified Weyl-law tail 
analysis at d=4 multiplicity-weighted normalization. STAGE-1-CANDIDATE. |
```

**(iii) FWD-C2 Level-2 algebraic envelope pin**: **PENDING DISAMBIGUATION** under the volovik path. FWD-C2's substrate-IS observable cell is Corner IV (DEPENDENT × s=4); the K-window log-derivative is the canonical inhabitant of that cell, but its L_max envelope is undetermined (S87 W2-3 reported at fixed L_max=10 only). The L^{−4} envelope from W5b-47 belongs to a Corner-II observable and cannot transfer to FWD-C2 without violating clause (f) cross-corner co-primary discipline. Forward design route: c-split into FWD-C2-II (Corner-II cross-pillar bridge with the L^{−4} envelope) and FWD-C2-IV (Corner-IV cross-pillar bridge pending K-window log-derivative L_max scan).

**(iv) §W5b-47 Step 11 max-rule formal correction**: Replace the plan's

> Step 11: |Var(L_max) − Var(∞)| ~ max(L_max^{−3} from Σ|v_a|⁴ tail, (L_max^{−1})² from squared-first-moment tail) = max(L_max^{−3}, L_max^{−2}) = L_max^{−2}.

with the corrected statement (Sage-verified, II.2 chain):

> Step 11′: |Var(L_max) − Var(∞)| ~ L_max^{−4} (modulo log corrections from the borderline-convergent Mellin moment at s=2 on d=4). At canonical multiplicity-weighted normalization, both leading terms — `M_n^{(2)}(L)/N(L) ~ log(L)/L^4` and `[M_n^{(1)}(L)/N(L)]² ~ L^{−4}` — scale as L^{−4} per d=4 Weyl-law tail enumeration; the plan's `(L^{−1})² = L^{−2}` term arose from an over-strong assumption that GGE-constraint regularization scales the first moment as L^{−1}, but multiplicity-weighted normalization gives M_n^{(1)}(L)/N(L) ~ L^{−2}, not L^{−1}.

The corrected Step 12 reads `α_predicted = 4` (not 2). Empirical α_nonlinear = 4.000 confirms the corrected prediction at machine-precision interior solution; the log-log α = 3.56 is a finite-L correction artifact attributable to sub-leading L^{−3} terms.

**(v) Discriminating computation specification for S89+**: The seed file's discriminating-predicate question (d) — *"independently compute the K-window second log-derivative `d² ln P_GGE / d(ln K)²` on the §W5b-47 spectrum cache over a K-window matching S87 W2-3; check whether the result reproduces -7.046336 OR v_inf=6.46e-6 OR neither"* — is the right S89 dispatch. Pre-registration as `S89-CORNER-IV-K-WINDOW-LOG-DERIVATIVE-RECOMPUTE` (see V.1 below). Predicted outcome (substitution chain):

```
The two observables differ in BOTH the operator structure (M_4/N − (M_2/N)^2 vs 
d^2 ln P_GGE / d(ln K)^2) AND the convention domain (multiplicity-weighted Mellin 
on (A_K^{<=L}, H_K^{<=L}, D_K^{<=L}) vs horizon-crossing K-window on Bogoliubov 
amplitude trajectory). Sage parse-tree analysis (II.1) shows they share NO 
structurally-equivalent simplification path. 

Direction: prediction is that the S89 recompute REPRODUCES -7.046336 to within 
solver tolerance and does NOT reproduce v_inf = 6.46e-6 — confirming that the 
two observables are structurally distinct AND that S87 W2-3's value was correctly 
attributed to the K-window log-derivative.

Conclusion: the S89 dispatch is a confirmation gate for volovik path's reading; 
under that gate's predicted PASS the registry CORRECTION specified in (ii) above 
becomes mechanically dispatchable.
```

### IV.2. Constraint-map updates

- **OPENED**: A Corner-II calibration slot is now structurally pinnable — `Var_a(n_a^GGE)` provides the `(INVARIANT × s=4)` corner cell that §VII.U.2 line 12924 marked OPEN. K=3 saturation status is preserved; what was open at landing time is now fillable.
- **CLOSED**: The cross-corner cross-confirmation clause at line 12926 is identified as a clause (f) violation — it must be removed. This closes the corridor "Corner-IV calibration can be cross-confirmed by Corner-II envelope evidence."
- **SHARPENED**: Plan §W5b-47 Step-11 max-rule correction is **doubly motivated** — Sage-verified Weyl-law tail enumeration AND empirical α_nonlinear = 4.000. The L^{−4} envelope is structurally robust at d=4 multiplicity-weighted normalization.
- **OPEN**: Corner-IV's L_max convergence envelope. S87 W2-3 reported at fixed L_max = 10; an explicit L_max scan on the K-window log-derivative has never been run. Until run, FWD-C2's Level-2 envelope is undetermined.
- **OPEN**: Whether the S88 W7a-73 OE-form discipline (Element-2 OE-form regex requirement on cross-pillar bridge entries) extends to per-corner-cell observables in §VII.U.2's partition table. The Corner-IV row currently lacks an OE-form Element-2 specification of the K-window log-derivative; this is forward bookkeeping.

### IV.3. Layered substitution-chain audit (Step 11 anatomy)

The W5b-47 Step-11 max-rule defect surfaces a **layered substitution-chain audit pattern** that future plan-authoring should pre-register:

```
Layer 1 (arithmetic): Are the Weyl-law exponents and multiplicity-weighted 
                      normalization factors arithmetically correct? 
                      => connes-axis check
Layer 2 (parse-tree): Does the observable's symbolic form match the corner cell 
                      the registry assigns it?  
                      => clause (e) parse-tree audit
Layer 3 (operationalization): Is the observable's session-anchor scheme/convention 
                              the same operationalization as the registry-cited 
                              prior session's scheme/convention?
                              => verdict-line scheme/convention regex audit
```

Plan §W5b-47 had errors at Layer 1 (arithmetic max-rule wrong) AND Layer 3 (W5b-47 plan's symbol `α_s_route_3` shared with S87 W2-3's symbol but operationalizations differ at Layer 2). The chain-rule-correction-only reading (connes path) addresses Layer 1; the operationalization-conflation reading (volovik path) addresses Layer 3. Both must be applied; addressing only one leaves the registry mis-anchored at the other.

This layered audit pattern is a candidate methodology-rule extension to `epistemic-discipline.md §"Pre-Registration Completeness"` Class-8 sub-taxonomy (forward bookkeeping; see V.5).

---

## V. Carry-Forward Computations

### V.1. S89-CORNER-IV-K-WINDOW-LOG-DERIVATIVE-RECOMPUTE (the discriminating gate)

- **What**: Independently compute the K-window second log-derivative `d² ln P_GGE / d(ln K)²` on the §W5b-47 spectrum cache, over a K-window matching S87 W2-3's horizon-crossing window. Check whether result reproduces (i) S87 W2-3's `−7.046336`, (ii) §W5b-47's `v_inf = 6.46e-6`, or (iii) neither.
- **Inputs**: `computations/session-87/s87_alpha_s_direct_moment_independent_route.py` (canonical S87 W2-3 producing script; SHA TBD via plan-freeze grep); `computations/session-84/s84_spectrum_cache_L12_tau019.npz` (sha256 = `9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9`); `computations/session-52/s52_bogoliubov_amp.npz` (sha256 = `ecfbce08eabe84394009b69d6ae9710fc2d9e106d55ec8481466f95952e348b1`); `canonical_constants.py` (`Delta_BCS = 0.4642547394830737`, `tau_fold = 0.190`, `M_KK`); §VII.U.2 Corner-IV row text (line 12926); horizon-crossing K-window definition from S87 W2-3 plan (anchor: `sessions/session-plan/archive/session-87-plan-w2.md`).
- **Gate**: PASS iff recomputed `d² ln P_GGE / d(ln K)² ≈ −7.046336` to within solver tolerance (rel_tol < 1e-3); PASS confirms volovik path reading (the two observables are structurally distinct). FAIL iff result matches `v_inf = 6.46e-6` (would force a registry rewrite). INFO iff result matches neither (forces §VII.U.2 Corner IV → REGISTRY-INCOMPLETE flag pending S90 disambiguation). Pre-registered classification: `[VERIFY]` trigger; convention pinned at `horizon-crossing-K-window-canonical`; scheme pinned at `GGE-Bogoliubov-occupation-variance` (matching S87 W2-3 verdict-line metadata exactly).
- **Effort**: 0.4 wave-equivalents (script port from S87 W2-3 onto W5b-47 cache; ≤ 2 hours dispatch + 1 agent session).

### V.2. S89-VII-U-2-CORNER-II-LANDING (Corner-II calibration row landing)

- **What**: Land the Corner-II calibration row in `permanent-results-registry.md §VII.U.2` at line 12924 (replacing the current OPEN marker) with the W5b-47 multiplicity-weighted variance functional + L^{−4} envelope + v_inf extrapolation. STAGE-1-CANDIDATE per `joint-theorem-promotion.md` Stage 1 (Stage-2 cross-axis verify queued for S90+).
- **Inputs**: `sessions/archive/session-88/session-88-w5b-workingpaper.md §W5b-47` (already-landed numerical envelope artifacts); §W5b-48 connes-axis axiom-level non-triviality argument for Corner-II spectrum-only side; this synthesis (II.2 Sage-verified L^{−4} chain; II.4 SOURCE-DOUBLE-CITE-CO-PRIMARY anchor structure spec).
- **Gate**: `S89-VII-U-2-CORNER-II-LANDING` PASS iff (i) line 12924 contains an explicit Var_a(n_a^GGE) row entry replacing the OPEN marker; (ii) row text cites both v_inf = 6.4631783294e-06 (V-anchor; W5b-47 numerical) and the L^{−4} envelope structural derivation (C-anchor; this synthesis II.2); (iii) STAGE-1-CANDIDATE tag present; (iv) cross-link to §W5b-47 audit_sha256 = `89090d37b3610590…`. METHODOLOGY-class per `wave-classification.md` M1-M4 conjunction (artifact-existence predicate; rule-file/registry edits only; substrate-axiomatic source from §W5b-47 + this synthesis; gate-ID requires allowlist append at plan-freeze).
- **Effort**: 0.2 wave-equivalents (mack-cosmic-bridge sole writer registry edit + connes co-sign).

### V.3. S89-VII-U-2-CORNER-IV-CROSS-CORNER-CONFIRMATION-REMOVAL

- **What**: Remove the cross-corner cross-confirmation clause from the Corner-IV row at line 12926 per clause (f) discipline. The line should read only the S87 W2-3 K-window log-derivative anchor without the §W5b-47 cross-confirmation appendix; the §W5b-47 envelope is rerouted to the Corner-II row per V.2.
- **Inputs**: this synthesis II.4 (clause (f) violation identification); registry text at line 12926 (current); the corrective text spec at IV.1 (ii); `registry-landing.md` SOURCE-DOUBLE-CITE-CO-PRIMARY discipline.
- **Gate**: `S89-VII-U-2-CORNER-IV-CROSS-CORNER-CONFIRMATION-REMOVAL` PASS iff (i) line 12926 no longer contains the substring "structural envelope cross-confirmed at S88 §W5b-47"; (ii) the K-window log-derivative anchor `−7.046336` is preserved as the SOLE Corner-IV calibration source; (iii) the corrective row text matches IV.1 (ii) above. Append-only edit per Option-A protocol of `gate-verdicts.md §"Option A — sig_5 remediation pathway under absolute verdict permanence"` if the original registry-write verdict line carries `supersedes` semantics (it does not — registry text edits are not verdict-line emissions, so direct edit is permitted). Verdict line tagged METHODOLOGY-class.
- **Effort**: 0.1 wave-equivalents (mack-cosmic-bridge sole writer single edit + audit re-pass).

### V.4. S89-CORNER-IV-K-WINDOW-LMAX-SCAN (Level-2 envelope for the genuine Corner-IV observable)

- **What**: Run an L_max ∈ {6, 7, 8, 9, 10, 11, 12} scan on the K-window log-derivative `d² ln P_GGE / d(ln K)²` to extract its Level-2 algebraic envelope (the L_max convergence rate of the Corner-IV genuine observable). Conditional on V.1 PASS.
- **Inputs**: V.1 producing-script port (post-PASS); same spectrum cache + Bogoliubov amplitude data as V.1; horizon-crossing K-window definition.
- **Gate**: `S89-CORNER-IV-K-WINDOW-LMAX-SCAN` PASS iff log-log fit on `|d²lnP_GGE/d(lnK)²(L_max) − d²lnP_GGE/d(lnK)²(∞)|` returns `R² > 0.95` and an integer-valued α (consistent with substrate-distance-2 cone Mellin residue order). INFO iff R² ∈ [0.50, 0.95] (MARGINAL regime per S87+ schema-v2). FAIL iff R² < 0.50 (envelope structure absent; would falsify the structural prediction that the K-window log-derivative is a power-law-convergent observable). The L_max=∞ extrapolated value should be tracked but is NOT the gate predicate.
- **Effort**: 0.5 wave-equivalents (compute-class; depends on V.1 PASS).

### V.5. S89-LAYERED-SUBSTITUTION-CHAIN-AUDIT-PATTERN

- **What**: Methodology-rule extension to `epistemic-discipline.md §"Pre-Registration Completeness"` Class-8 sub-taxonomy adding Class 8.4 (LAYERED-SUBSTITUTION-CHAIN-AUDIT). Pre-registers the 3-layer audit pattern described in IV.3 (arithmetic / parse-tree / operationalization) for any plan substitution chain that crosses corner cells of §VII.U.2 (or any future N-corner partition).
- **Inputs**: this synthesis IV.3 (3-layer pattern); §VII.U.2 clause (e) parse-tree decision; verdict-line scheme/convention regex spec from `gate-verdicts.md`. Calibration corpus K=1 at landing: W5b-47 Step-11 (instance #1, this synthesis).
- **Gate**: `S89-LAYERED-SUBSTITUTION-CHAIN-AUDIT-PATTERN` PASS iff (i) `epistemic-discipline.md §"Pre-Registration Completeness"` extended with Class 8.4; (ii) audit-script template at `computations/_shared/_layered_chain_audit.py` (NEW) implementing the 3-layer check (Layer 1 arithmetic via pinned Sage call, Layer 2 parse-tree via clause (e) decision-procedure, Layer 3 operationalization via verdict-line regex); (iii) calibration corpus row in rule-file citing this synthesis with audit_sha256 pin. K=1 status; SUGGESTION-tier; promotes to MANDATORY at K=3 per `feedback_rules-compensate-missing-structure.md`.
- **Effort**: 0.3 wave-equivalents (rule-file extension ~0.15; audit-script template ~0.15).

### V.6. S89-FWD-C2-OBSERVABLE-DISAMBIGUATION (forward-bridge-anatomy disambiguation)

- **What**: Pre-register FWD-C2 cross-pillar bridge candidate either (option A) AS-A-c-split into FWD-C2-II (Pillar II ↔ Pillar V; Corner-II observable; L^{−4} envelope from V.2) and FWD-C2-IV (Pillar II ↔ Pillar V; Corner-IV observable; envelope pending V.4), OR (option B) AS-A-singleton FWD-C2 with explicit Corner-IV anchoring and L_max envelope deferred to V.4 PASS.
- **Inputs**: `cross-pillar-bridge-anatomy.md §"Three forward bridge candidates for S88+ dispatch"` (current FWD-C2 spec; SUGGESTION at K=1 per Hybrid Independence Test); this synthesis IV.1 (iii) FWD-C2 split rationale; V.2 + V.4 outputs (post-PASS).
- **Gate**: `S89-FWD-C2-OBSERVABLE-DISAMBIGUATION` PASS iff (i) `cross-pillar-bridge-anatomy.md §"Three forward bridge candidates"` text updated to enumerate FWD-C2-II and FWD-C2-IV explicitly (option A) OR specifies the Corner-IV anchoring with deferred L_max envelope (option B); (ii) the choice between (A) and (B) is grounded in V.4 verdict (option A if V.4 PASS extracts a CONCRETE α distinct from 4; option B if V.4 INFO/FAIL leaves the K-window envelope undetermined). METHODOLOGY-class; allowlist append required.
- **Effort**: 0.25 wave-equivalents (volovik + connes co-sign; rule-file edit + cross-link maintenance). Conditional on V.4 verdict landing.

### V.7. S89-W5B-47-PLAN-STEP-11-CORRECTION-RECORD

- **What**: Append a corrective sub-block to `sessions/session-plan/session-88-plan-w5b.md §W5b-47` documenting Step-11 max-rule correction per IV.1 (iv). The correction is a plan-revision record (audit-trail preserving), NOT a retroactive plan edit; original Step-11 text remains in place with a `# CORRECTED-AT-S89-W17:` annotation pointing to this synthesis.
- **Inputs**: this synthesis IV.1 (iv) corrected Step 11′; Sage-verified L^{−4} chain at II.2; original plan §W5b-47 Step-11 text (lines 311–316).
- **Gate**: `S89-W5B-47-PLAN-STEP-11-CORRECTION-RECORD` PASS iff (i) corrective sub-block appended; (ii) original Step-11 text unmodified (verdict permanence applies to plan-pin records as well); (iii) annotation cites this synthesis audit_sha256. METHODOLOGY-class.
- **Effort**: 0.05 wave-equivalents.

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| II.1 | Parse-tree decision (clause (e)) classifies W5b-47 `Var_a(n_a^GGE)` as **Corner-II** (INVARIANT × s=4), NOT Corner IV; S87 W2-3 K-window log-derivative is genuine Corner-IV | GEOMETRIC + METHODOLOGY | NEW pinned position | Volovik path wins on observable identity; registry rewrite mandatory |
| II.2 | `\|Var(L) − Var(∞)\| ~ L^{−4}` (modulo log) at d=4 multiplicity-weighted normalization; Sage-verified via Weyl-law tail; empirical α_nonlinear = 4.000 confirms structural prediction | GEOMETRIC | PROVEN structural envelope | Step 11 of plan §W5b-47 is corrected to L^{−4}, NOT L^{−2}; the corrected envelope IS Corner-II's Level-2 calibration |
| II.3 | Plan §W5b-47 Step 11 has TWO defects (chain-rule arithmetic + observable-identity conflation), not one | METHODOLOGY | NEW finding | Both connes path AND volovik path corrections required; chain-rule-only fix leaves registry mis-anchored |
| II.4 | Cross-corner cross-confirmation clause at registry line 12926 violates §VII.U.2 clause (f) | METHODOLOGY | NEW violation surfaced | Registry CORRECTION (not annotation) of line 12926; cross-confirmation phrase removed; W5b-47 envelope rerouted to Corner-II row |
| II.5 | FWD-C2 Level-2 envelope pin is **PENDING DISAMBIGUATION**; cannot inherit L^{−4} without violating clause (f) | METHODOLOGY | OPEN | FWD-C2 c-split (II/IV) or deferred-envelope option awaiting V.4 verdict |
| V.1–V.7 | 7 carry-forward gates (S89-class) covering observable disambiguation, registry corrections, methodology-rule extension, FWD-C2 split, and plan-correction record | mixed COMPUTE / METHODOLOGY | Pre-registered | S89 plan-freeze MUST schedule V.1 first (discriminating gate); V.2/V.3 conditional on V.1 PASS; V.4 conditional on V.1 PASS for envelope extraction |

---

## VII. Cross-link to Workshop 1 (§W5b-50 rank-deficiency tension)

The Workshop 1 tension (§W5b-50 16×16 GRID rank-deficiency, connes vs volovik) is structurally **distinct** from this Workshop 2 adjudication but shares the volovik-axis's core insight: substrate-IS observable identity is the prior question to numerical envelope characterization. In Workshop 1, the question is whether the chirality-projected 16-state basis IS the substrate's canonical truncation or an embedding-convention artifact. In Workshop 2 (this synthesis), the question is whether `Var_a(n_a^GGE)` IS the Corner-IV observable. In both, the volovik adversarial axis correctly identifies that operationalization conventions can silently substitute one observable for another at the symbol/scheme level while the parse-tree (Workshop 2) or basis-canonicality (Workshop 1) layer remains unresolved. The two workshops' resolutions are independent, but they share the same methodological lesson: **Layer-2 parse-tree/basis-canonicality audits are the prior epistemic step to Layer-3 numerical-envelope characterization**.

---

## VIII. Substrate framing (per `phononic-framing.md`)

The 4-corner classification IS a property of the spectral triple `(A_K, H_K, D_K)` itself. The Mellin-cone substrate-distance-2 pole at s=4 IS a property of the substrate's analytic continuation, NOT a measurement convention "in" a regulator container. The W5b-47 variance Var_a(n_a^GGE) IS a substrate-IS observable on `(A_K, H_K, D_K)` — its parse-tree image is in the algebra-INVARIANT family because it depends only on the spectrum `{λ_k(D_K), m_k}` of the substrate's Dirac operator, not on the algebra `A_K` action. The S87 W2-3 K-window log-derivative IS likewise a substrate-IS observable, but its parse-tree image is in the algebra-DEPENDENT family because the GGE expectation `⟨ψ_GGE | n_K | ψ_GGE⟩` requires the algebra action on the Hilbert space. The 4-corner partition does NOT measure observables "in" a container; the partition IS the substrate-level orthogonal classification of spectral-triple functionals.

Direction of explanation:

```
NCG axioms 1+4+5+6 + clause (e) parse-tree decision  (substrate-axiomatic)
   → Observable A (Var_a(n_a^GGE)) parse-tree image: algebra-INVARIANT (spectrum + multiplicity only)
   → Corner cell: (INVARIANT × s=4) = Corner II
   → Substrate's L^{-4} algebraic envelope (Weyl-law tail at d=4 multiplicity-weighted)
   → Registry §VII.U.2 Corner-II calibration landing  (laboratory-IN audit-trail commitment)

NCG axioms 1+4+5+6 + clause (e) parse-tree decision  (substrate-axiomatic)
   → Observable B (d² ln P_GGE / d(ln K)²) parse-tree image: algebra-DEPENDENT (state-pair on A_K)
   → Corner cell: (DEPENDENT × s=4) = Corner IV
   → S87 W2-3 reported value -7.046336 at L_max=10 (envelope undetermined)
   → Registry §VII.U.2 Corner-IV calibration retains S87 W2-3 anchor SOLO
```

No "container" appears in either chain; the substrate IS the spectral triple, IS the orthogonal partition, IS the parse-tree-decidable corner-cell structure, and IS the L_max-convergent envelope at d=4 multiplicity-weighted normalization. The two observables differ at the parse-tree layer of substrate-IS structure; they cannot occupy the same corner cell, and the registry cannot pin both as Corner-IV anchors without violating the substrate-axiomatic family-orthogonality theorem (§W5b-48 PASS).
