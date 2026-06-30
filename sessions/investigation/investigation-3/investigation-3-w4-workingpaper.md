# Investigation 3 Wave 4 — M_KK derivability adjudication (Results Working Paper)

**Investigation**: 3 | **Wave**: 4 | **Plan**: investigation-3-plan-w4.md | **Theme**: M_KK-DERIVATION adjudication (live corridor vs proven-impossible wall)

This wave carries exactly ONE gate, INV3-W4-1, of `gate_type: workshop`. A workshop gate closes by **artifact-existence-with-content** — it emits NO verdict line (`gate-verdicts.md §"Investigation-Track Canonical Path"`: review/workshop gates close by artifact existence; the same closure semantic as a METHODOLOGY-class wave per `wave-classification.md §M1`). The section below therefore carries a pending block POINTING AT the workshop deliverable md + an artifact-existence checklist, NOT a verdict-line block.

## Gate Sections

### §W4-1. INV3-W4-1 (workshop — spectral-geometer ↔ paasch-mass-quantization-analyst)

**Status**: COMPLETED (landed — artifact-existence closure; NO verdict line per the workshop semantic)
**Gate ID**: `INV3-W4-1`
**Gate type**: `workshop` (EXACTLY-2-agent adversarial adjudication; closes by artifact-existence, NO verdict line)
**Trigger**: `[VERIFY]` (structural-verdict adjudication; the planner makes no numerical sign/threshold claim)
**Classification**: **GEOMETRIC** (the object is the substrate's spectral triple `(A_K, H_K, D_K)` and whether it fixes its own dimensional scale `M_KK` — the fabric itself, not its excitations)
**Adjudication question (one-line paraphrase)**: Is `M_KK` **derivable** from the SU(3) integer structure (Reading-P: Paasch `N(j)=7n` + proton-cubic → absolute `m_p`), or is it **structurally irreducible** — a scale-free spectral triple cannot fix its own scale, `M_KK` irreducibly external (Reading-S: NNU rank-1, §VII.BS)?

**Landed**: workshop deliverable `sessions/investigation/investigation-3/workshops/m-kk-derivability.md` (2 agents spectral-geometer ↔ paasch-mass-quantization-analyst, 2 rounds, strictly sequential). **Converged STRUCTURAL VERDICT: SCOPED-INTERMEDIATE — "RATIO-derivable, NORMALIZATION irreducibly external."** Closes by artifact-existence (NO verdict line).

**Workshop structure** (from plan `workshop:` block): R1 = each advocate states their reading from first principles into the shared document (Reading-S scale-free / NNU rank-1 §VII.BS; Reading-P `N(j)=7n` + proton-cubic candidate derivation); R2 = each rebuts the opponent's R1 and the pair converges on a STRUCTURAL VERDICT on `M_KK-DERIVATION`'s status + the decisive forward gate. Three sub-questions are each answered on their own merits (verdict on each may cut either way): (a) does NNU rank-1 (§VII.BS; S103 bundle-exhaustiveness `ac1dbb28`) PROVE in-principle underivability, or only characterize the rank of the EXISTING import structure? (b) does Paasch's `N(j)=7n` + proton-cubic fix `m_p` (hence `M_KK`) WITHOUT a hidden external scale once the dead Dirac-`G~1/t` LNH scaffolding is severed? (c) what SINGLE compute would DECIDE it (candidate: INV3-W3-4, the Casimir-graded `N(j)=7n` test)?

**Structural-verdict target**: a pinned position on `M_KK-DERIVATION`'s status — **LIVE-CORRIDOR** (a substrate-internal derivation of the scale's value is not foreclosed; name the open route) vs **PROVEN-IMPOSSIBLE-WALL** (the scale-free structure forecloses self-derivation; `M_KK` irreducibly external) vs a precisely-scoped **SCOPED-INTERMEDIATE** (e.g. "value-derivable, normalization-not"; "rank-1 confirms the IMPORT structure but is silent on an INTEGER-VALUE derivation") — plus the named decisive forward gate. The verdict resolves the competing claims into a NEW pinned position; it does NOT queue a computation in place of a verdict.

**Artifact-Existence Closure Checklist** (workshop closure == `wave-classification.md §M1`; NO verdict line, NO dual-SHA — closure is artifact-existence-with-content of `workshop.output_path` per the plan's `output_artifacts.workshop_md` block):

*(pending — confirm the deliverable md exists (`ls sessions/investigation/investigation-3/workshops/m-kk-derivability.md`) AND paste `grep -E '<pattern>' <path>` output for every must_contain pattern below. An absent file OR any must_contain regex returning empty means the workshop did not properly close — orchestrator MUST then SendMessage continuation to the workshop dispatch per `feedback_dispatch-discipline.md`. Closure is purely by content presence (regex match), NEVER by line/byte counts per `feedback_max-effort-full-fidelity.md`. This is a `landed`/`not-landed` outcome, NOT a substrate-physics PASS/FAIL: a missing-section `not-landed` remediates by re-dispatching the workshop, not a numerical re-run.)*

- [x] `sessions/investigation/investigation-3/workshops/m-kk-derivability.md` exists (verified on disk)
- [x] must_contain: `## Wrap-Up` (L377) — carries the pinned STRUCTURAL VERDICT **SCOPED-INTERMEDIATE** on `M_KK-DERIVATION`'s status
- [x] must_contain: `## Effected In-Session` (L397) — three `[→investigate]` session-promotion routes; 0 unchecked `- [ ]` (correct — no orchestrator-effectable non-math at the investigation-track layer)
- [x] must_contain: `## Carry-Forward Computations` (L407) — the decisive forward gate `INV3-W4-1-FWD` (non-spectral-scale existence scan) as a 4-field spec; `## Structural Verdict` (L361) also present

**Substrate framing** (GEOMETRIC, `phononic-framing.md`; preserved neutral to the outcome): the object under adjudication is the FABRIC itself — the spectral triple `(A_K, H_K, D_K)` on Jensen-deformed SU(3) and whether its own structure fixes its single dimensional scale `M_KK`. Direction of explanation: `D_K eigenvalues → spectral moments → dimensionless dynamical shapes (the protected Ô kernel) → measurement`. The workshop adjudicates precisely whether the chain ALSO fixes the dimensional weight `w = M_KK` (so that `O = w·Ô` has `w` substrate-derived), or whether `w` is irreducibly imported. FORBIDDEN inversion (neither advocate may invoke): "`M_KK` is set by GR/`G_N` as a pre-existing container the substrate lives in" — the §VII.BS framing is that `M_KK` is the one externally-calibrated CUTOFF of the substrate's own emergent metric (`N₃=0` ⇒ topologically unprotected normalization), NOT a container; the substrate-first arrow is unchanged under either reading.

## Wave 4 Synthesis (team-lead)

Wave 4 carried the single adversarial gate of investigation-3 and resolved it. The 2-agent, 2-round sequential workshop (spectral-geometer Reading-S ↔ paasch Reading-P) **converged on SCOPED-INTERMEDIATE — "RATIO-derivable, NORMALIZATION irreducibly external"**: the substrate fixes every dimensionless shape and even over-determines some couplings (n3=dim(3,0)=10 → α sub-ppm, W3-3(i)), but **no spectrum-or-representation functional can return its one dimensional weight M_KK**; the only unforeclosed route is a hypothetical non-spectral, intrinsically-dimensionful datum, which no run has populated.

The convergence was genuinely adversarial (not parallel-agreement): the paasch advocate **conceded all three of spectral-geometer's R2 rebuttal heads, each Sage-verified**:
- **(a)** NNU rank-1 (§VII.BS; ac1dbb28) proves underivability of M_KK by ANY spectrum-only functional Φ({λ_k}) AND closes the second-scale escape — leaving open only a non-spectral route. The representation-integer channel does NOT escape: **C₂(p,q) = 6(|λ_trivial|²−1/4) is Sage-exact**, so the SU(3) integers are recovered units-free from the spectrum (the τ-/regulator-invariance that makes them robust is the very fact that disqualifies them as a scale source). → WALL on the value question, reaching the integer channel.
- **(b)** Stripped of the dead Dirac-G~1/t LNH scaffolding, Paasch's N(j)=7n + proton-cubic give m_p/m_e = 150^{3/2} = 1837.117 — a dimensionless RATIO (rel-dev 5.25e-4 vs PDG), NOT absolute m_p; an anchor μ₀=m_e re-enters and m_e itself factors through M_KK (m_p = M_KK·Ô_p). Paasch ENRICHES the Ô bundle (strengthening bundle-exhaustiveness), it does not derive the scale. The proton integer 150=6·25 is not even a clean SU(3) dim (INV3-W3-4: 2-of-5).
- **(c)** The decisive forward gate is a **non-spectral-scale existence scan** (see Carry-Forward below), distinct from falsifier-(i)'s Φ({λ_k}) and from the M_Pl·Φ(integers) relocation — the latter WITHDRAWN in R2 (circular under substrate-first M_Pl; non-evidential by look-elsewhere, 2 of 6561 integer-pairs within 2% of M_KK/M_Pl by chance).

This verdict is the convergent landing of the whole investigation's dimensionful-axis sweep: **three independent routes to a substrate-internal M_KK came back negative** (W2-1 d_s-flow, W2-4 geodesic-stationarity, W3-4 N(j)=7n), while one dimensionless SU(3) identity DID land (W3-3(i) α). The substrate fixes shape, not size — and now that boundary is pinned, with the single remaining door (a non-spectral dimensionful invariant) named as the decisive test.

### What Changed
**(a) Numerical revisions**: m_p/m_e = 150^{3/2} = 750√6 = 1837.117 (rel-dev 5.25e-4); M_KK/M_Pl = 6.085e-3 (look-elsewhere 2/6561 integer-pairs within 2%); C₂(p,q) = 6(|λ_trivial|²−1/4) Sage-exact (five Casimirs bit-exact).
**(b) Structural changes**: M_KK-DERIVATION pinned OPEN-ADVERSARIAL → SCOPED-INTERMEDIATE (ratio-derivable, normalization-external); the channel-(II) representation-arithmetic "escape" RETRACTED (integers recovered from spectrum); the M_Pl·Φ(integers) route WITHDRAWN; the one unforeclosed door isolated to a non-spectral intrinsically-dimensionful datum.

### Routing to /rclab-investigate (Wave 4 → investigation close)
Per the plan's decision point, SCOPED-INTERMEDIATE routes: the decisive forward gate (INV3-W4-1-FWD) lifts as a carry-forward; the verdict + three register annotations (§VII.BS SCOPED-INTERMEDIATE note, EVOI §6 standing-gap status, the M_Pl·Φ withdrawal) route as **session-promotion candidates** to `/rclab-investigate --investigation 3` close (session-track curated-register prose, designated-writer per `feedback_framework-hygiene.md`). The verdict is an investigation finding; permanent registration requires a session-track re-compute (track-local boundary).

### Effected In-Session (non-math)
None orchestrator-effectable in-investigation. The workshop's three non-math items are `[→investigate]` session-track register annotations (an investigation cannot mutate §VII.BS / EVOI §6 / canonical registers). Consolidated into `investigation-3-housekeeping.md` for `/rclab-investigate`.

## Carry-Forward Computations

### INV3-W4-1-FWD — Non-spectral-scale existence scan (the decisive M_KK-DERIVATION gate)
| Field | Spec |
|:------|:-----|
| **What** | Test whether any intrinsically-dimensionful NON-spectral substrate invariant (cocycle-norm / holonomy carrying intrinsic units) can write M_KK with NO imported GeV/seconds anchor — distinct from falsifier-(i)'s Φ({λ_k}) (spectrum-only, FAIL-confirmed S102 `63698aa8`) and from the M_Pl·Φ(integers) relocation (withdrawn in R2). |
| **Inputs** | §VII.BS falsifier-(i) form; the substrate cocycle-norm / holonomy registry (§VII.BR f_WZ family; 3He-B cocycle norms); a single gravitational anchor (1/G_induced matching scale, NOT a pre-existing container); the W3-2 look-elsewhere corpus (MANDATORY penalty — the sin/cos & integer-ratio families are dense near targets). |
| **Gate** | ∃ non-spectral intrinsically-dimensionful invariant I with M_KK = Φ(I), NO imported scale, surviving the look-elsewhere penalty → **LIVE-CORRIDOR** (§VII.BS falsified rank-0); else → **PROVEN-WALL on normalization**. |
| **Effort** | ~1.5–2 wave-equiv (registry sweep of dimensionful non-spectral invariants + look-elsewhere-controlled existence test). |

(Mirror of the workshop's own `## Carry-Forward Computations` block in `workshops/m-kk-derivability.md`; `/rclab-investigate` lifts it.)

## Constraint-Map Updates

| Date | Mechanism / gate | Prior state | New state | Reason |
|:-----|:-----------------|:------------|:---------|:-------|
| 2026-06-15 | M_KK-DERIVATION (EVOI §6 #1 standing gap) | OPEN-ADVERSARIAL (Reading-S WALL vs Reading-P derivable) | SCOPED-INTERMEDIATE — ratio-derivable, normalization irreducibly external | INV3-W4-1 converged verdict; no spectrum-or-representation functional fixes M_KK's value |
| 2026-06-15 | Channel-(II) representation-arithmetic escape route | candidate orthogonal scale-route (Reading-P R1) | RETRACTED — collapses into channel (I) | C₂(p,q)=6(\|λ_trivial\|²−1/4) Sage-exact: integers recovered units-free from spectrum |
| 2026-06-15 | M_KK = M_Pl·Φ(integers) route | candidate (Reading-P R1) | WITHDRAWN — relocates/circular, non-evidential | substrate-first M_Pl cancels to Ψ·Φ=1; look-elsewhere 2/6561 within 2% |

## Files Produced

| Artifact | Role | Status |
|:---------|:-----|:-------|
| `sessions/investigation/investigation-3/workshops/m-kk-derivability.md` | the workshop deliverable (sole artifact-existence closure target; 4 turn + 4 closing sections) | ✓ on disk |
| `sessions/investigation/investigation-3/investigation-3-w4-workingpaper.md` | this working paper | ✓ on disk |

(Workshop gate — NO verdict line, NO script/npz/png; closes by artifact-existence per `wave-classification.md §M1`.)
