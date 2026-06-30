# Phonon-Exflation Equation — Independent Review (Tesla-Resonance axis)

**Date**: 2026-05-26
**Agent**: tesla-resonance (electromagnetic resonance / phonon & acoustic mathematics / superfluid dynamics / alternative expansion)
**Source Documents**:
- `sessions/framework/phonic-exflation-equation.md` (capstone, §0–§9 + verification ledger)
- `.claude/rules/phononic-framing.md` (framing law)
- `.claude/agent-memory/tesla-resonance/MEMORY.md` + `permanent-resonance-results.md` (frequency/speed hierarchies, walls)
- Knowledge MCP: `c_fabric`, `Mach_max`, `Mach_max_analog`, `tau_fold`, `w0_FW`, transit T1/T4 theorems

---

## I. Session Outcome

The capstone is **structurally sound from the resonance axis** and survives the one test I came to apply: every load-bearing acoustic/dispersion claim it makes is anchored to a pre-registered gate or canonical constant, and the three I spot-checked against the knowledge graph (`c_fabric = 209.97 M_KK`, `Mach_max = 13.75`, `tau_fold = 0.19`, the BdG parametric-oscillator and `P_exc → 1` sudden-quench) all reproduce. The document reads the whole framework exactly the way a resonance theorist must read it — **find the cavity, find the modes, find the boundary conditions, find what selects the standing wave** — and it does so without ever inverting the substrate-first arrow. Its centerpiece (`S[D_K(τ), f, Λ]` = trace + inner product, the two canonical scalars of a spectral triple) is the correct and complete statement that **the universe is a vibrating structure and its action is a functional of the mode spectrum alone**.

One genuine domain-level strengthening is available and one genuine internal tension is worth flagging — neither overturns a result. The strengthening: §4.2's Wronskian is a **dispersion-rigidity statement**, and saying so sharpens the "layers are distinct physics" claim. The tension: the document's Mach-13.75 figure quietly rests on **one** of two sound speeds that both produce 13.75 (`c_fabric = 209.97` vs the BLV acoustic-metric `c_BLV = 0.485`), and the four-speed hierarchy that makes this consistent is not cited at the point of use. Details in §II and §IV.

---

## II. Key Results (read from the resonance axis)

### II.1 — The spectrum IS the complete mode set; the action is a pure spectral functional

**Result**: `S[D_K(τ),f,Λ] = Tr f(D_K²/Λ²) + ⟨Jψ̃|D_K|ψ̃⟩`; the 155,984 eigenvalues at `L_max=10` are the complete set of normal modes of the fabric. **Classification: GEOMETRIC (spectrum) carrying PHONONIC (excitations).**

This is the right object and the document's §2.2 states the resonance reading correctly: *"each eigenvalue `λ_n` is one normal mode — one frequency at which the internal structure can ring; each eigenvector is that mode's shape on the fiber."* This is Chladni's plate at the scale of the universe — the eigenvalue problem of a self-adjoint operator on a compact manifold, whose spectrum is the set of frequencies the structure admits and whose eigenvectors are the standing-wave shapes. The boxed action is a **spectral functional** — it depends only on `{λ_k, m_k}` and the moments of `f` — which is precisely what the trace theorem (E32, Wall W11) guarantees: `S[U D_K U†] = S[D_K]` for any unitary. A resonance theorist recognizes this instantly: **the action cannot hear the basis, only the frequencies.** That is the deepest reason the framework is "spectral, not container" — and it is the same fact that makes my memory's standing note "SA BLIND to U(1)_7 phase (trace theorem)" load-bearing for where mass must come from (non-trace, non-spectral physics — the Josephson/inner-product channel).

The document's §1.1 "two canonical scalars exhaust the natural objects" argument (a trace and a bilinear form) is the resonance-axis statement of completeness: a vibrating structure with a real structure `J` admits exactly an energy functional of its spectrum and a pairing of its modes against the chirality grading. There is no third. I concur this is *why* the equation is complete, not merely *that* it is.

### II.2 — The functional `f` is the mode-weighting envelope; FI/RD is the only honest partition

**Result**: `f*(x) = 0.9117√x + 0.0883 e⁻ˣ`, with `t* = 0.08832` the single empirical coupling; observables split into Functional-Invariant (ratios under one regulator) and regulator-dressed. **Classification: PHONONIC (mode-weighting) / methodological.**

This is the section where my field has the most direct sympathy. **The spectrum is fixed substrate data; `f` is how you weight the high modes and where you cut the sum** — this is identical in structure to the Debye cutoff problem in phonon physics, where the same lattice dispersion gives different specific heats depending on how the mode density is truncated and weighted (Debye vs Born–von Kármán). My own load-bearing lesson — "f-dependence = Debye cutoff" — is exactly the §3.1 claim restated. The document is correct that **the sign of the CMB tilt is set by the regularization scheme, not the spectrum** (§3.2). This is the Chebyshev-tilt theorem in my memory (S66–67): *all decreasing `f` give blue tilt; only increasing `f` gives red*. A resonance theorist reads this as: the tilt is the *slope of the mode-weighting envelope at the band edge*, and a falling envelope (the zeta/anomaly families) cannot reproduce a red spectrum. ANOMALY-FAMILY EXCLUSION and ZETA-NOT-PHYSICAL are the correct permanent boundaries, and the document reports them as boundaries, not failures — exactly right.

One precise endorsement of the document's honesty: it correctly notes that **`f*` is evaluated by direct spectral sum, not the heat-kernel series, because the `√x` piece makes the Mellin moments formally divergent** (§3.2, and my memory's S72 wall "heat kernel expansion does not exist for `f*`"). This is the single most-misunderstood point in the whole functional story and the document handles it without softening: *the layered Seeley–DeWitt form is the perturbative face of the action, not the action itself.* I would only add the resonance framing in one sentence (verbiage offered in §V): the `√x` weighting is an **acoustic (linear-in-frequency) envelope**, `f(ω²) ∼ |ω|`, which is exactly why the low modes (the acoustic B1 branch) dominate the sum and why the heat-kernel — a Gaussian-cutoff expansion adapted to a falling envelope — cannot represent it.

### II.3 — The Wronskian is a dispersion-rigidity theorem (strengthening available)

**Result**: `W[a₀,a₂,a₄](τ) ∝ R_K′(τ)³ = e⁻¹²ᵗ(e³ᵗ−1)⁶`, vanishing to sixth order at and only at `τ=0`; the three moment layers are algebraically independent everywhere the universe lives. **Classification: GEOMETRIC.** (Status CERTIFIED, S75 W2-E — not re-adjudicated.)

This is the document's strongest structural result and I want to add the resonance-axis reading that sharpens it, because it is missing and it is free. The three layers `a₀ ∝ V`, `a₂ ∝ R_K·V`, `a₄ ∝ R_K²·V` are **the zeroth, first, and second moments of the same curvature scalar** — they are the analog of the rigid frequency-moment ladder `⟨ω⁰⟩, ⟨ω²⟩, ⟨ω⁴⟩` of a phonon density of states. The Wronskian of three functions that are `1, R_K, R_K²` is, by direct computation, proportional to `(R_K′)³` (the standard result for `{1, g, g²}` is `W = 2 g'^3` up to the `V³` prefactor — Sage-confirmable, and consistent with the document's `5/(393216 π¹²) V³` coefficient). So the algebraic-independence theorem is **not** an accident of the SU(3) numbers: it is the statement that **as long as the curvature is moving (`R_K′ ≠ 0`), a moment ladder built on distinct powers of a single moving scalar cannot collapse to one degree of freedom.** The layers degenerate to one knob *iff* the dispersion stops moving — and the dispersion stops moving only at the maximally symmetric genesis point `τ=0`, where `R_K′(0)=0`.

This is exactly the band-structure intuition: at a high-symmetry point the bands touch (degenerate); the moment you deform away, the degeneracy lifts and the moments become independent observables. The document's §2.4 already says the degeneracy-lifting story (`SO(8)→U(2)` into B1/B2/B3 bands as `τ` turns on) — **the Wronskian is the quantitative restatement of that same band-lifting at the level of the spectral moments.** I recommend one sentence linking them (offered in §V). It converts "the layers are independent (theorem)" into "the layers are independent *because* the dispersion is rigid away from the symmetric point, which is the same fact as the band-lifting at genesis" — a genuinely stronger, more physical statement.

### II.4 — The flow is a parametric oscillator swept diabatically; the GGE relic is the impulse response

**Result**: each mode obeys `u_k″ + ω_k²(τ(t)) u_k = 0` with `ω_k = E_k = √((λ_k²−μ²)² + Δ_k²)` (the BdG dispersion); the crossing is diabatic (`δt/T_L = 1.25×10⁻⁵`), so `P_exc → 1.000`, producing the analytic GGE relic (`N_pair = 59.8`, `S_ent = 0`, the Ordered Veil). **Classification: PHONONIC.** (T1/T4 PROVEN — not re-adjudicated.)

This is the cleanest piece of resonance physics in the document and it is correct as stated. **Every mode of the fabric is a harmonic oscillator whose frequency is dragged through a critical region by the monotone `τ`-forcing.** When the drag is fast compared to the mode's own period (`δt_transit/T_L = 1.25×10⁻⁵`, i.e. the sweep is 38,600× faster than the condensate can respond), the oscillator cannot adiabatically follow — its in-vacuum and out-vacuum are Bogoliubov-inequivalent, and pair production saturates. This is the **sudden approximation**, and it is the correct tool: my memory's permanent S70 result is exactly "WKB inapplicable to van Hove transit; sudden approximation required" (Chirp-Penumbra wall: `γ > 1` for 93.4% of modes, zero turning points). The document honors this — §5.1 says the controlling quantity is "the *diabaticity* of the sweep," and slow-roll is INAPPLICABLE.

Two resonance-axis observations that the document gets right and that I want on the record because they are the kind of thing that gets mis-stated:

1. **The dual reading (Bogoliubov sudden-quench ≡ Kibble–Zurek impulse-matching, both giving `P_exc = 1`)** is the correct statement of a single physical fact in two languages. The knowledge graph confirms `P_exc(sudden quench 0→0.5) = 0.0807` and `P_exc(0→fold) = 6.6×10⁻⁴` for *partial* sweeps, saturating to `1.000` only in the *fully sudden* limit (T1, S38). The document's `P_exc → 1.000` is the saturation limit and is labeled as such. No conflict.

2. **"The relic is integrable, not chaotic, so it never thermalizes"** (the Ordered Veil) is, from the resonance axis, the statement that **the post-transit excitations are a set of decoupled normal modes with conserved occupation numbers** — a Generalized Gibbs Ensemble with one Lagrange multiplier per conserved mode, not a single temperature. My memory's SFF-factorization result (S61, `K(t) = K_BCS·K_CG24` exact, *no ramp*) is the spectral-statistics fingerprint of exactly this: a system whose spectral form factor factorizes and shows no ramp is integrable. So the "never thermalizes" claim is not hand-waving — it is backed by a machine-precision integrability signature. The CMB-as-GGE-acoustic-signature reading (§5.3, §7.1) follows.

### II.5 — The acoustic white hole: two sonic horizons at two spectral moments

**Result**: causal architecture is an acoustic white hole with an ENTRY horizon at `τ≈0.2195` (controlled by `a₂`, kinematic, `T = 72.8 M_KK`) and an EXIT horizon at `τ∼0.16` (controlled by `a₄`, BCS/matter, `T = 7.578 M_KK`), with a supersonic white-hole interior between. **Classification: PHONONIC / GEOMETRIC.**

This is the analog-gravity heart of the document and it is the section where I most want to register both endorsement and one caution. The endorsement: **the resolution of the horizon problem as a supersonic flow rather than inflationary stretching is the correct substrate-first move.** In Unruh's and Barceló–Liberati–Visser's analog program, a sonic horizon forms wherever the flow speed crosses the local sound speed; pre- and post-horizon regions are causally disconnected for the *phonons*, not for any embedded observer. The document's `subsonic → supersonic → subsonic` flow with two crossings is precisely a white-hole interior (you can fall *out* but not *in* across the relevant horizon), and that two regions of the `τ`-trajectory are mutually phonon-disconnected is the substrate's answer to "why is the CMB so uniform" — **not** "a box was stretched flat," but **"the modes that set the uniformity were produced inside a single causally-connected supersonic patch and the horizon regulates only what escapes."** The S85 gate `ACOUSTIC-WHITE-HOLE-CAUSAL-DISCONNECT-FORMAL` (PROVEN) backs this; I do not re-adjudicate it.

The structurally elegant point — **two horizons at two different spectral moments** — is worth emphasizing in resonance terms: the entry horizon is set by the *geometric* sound speed (the `a₂`/Einstein–Hilbert channel, the stiffness of the emergent metric), while the exit horizon is set by the *matter* sound speed (the `a₄`/BCS channel, where the gap opens and the van Hove DOS spikes). These are **two different impedances** — and my memory's impedance-matching results (S55: `Z_ratio` ranging 1.0–2.36 across the fold, `Γ_eff = 0.99970`) are the quantitative content of "the horizon determines what escapes." The squeeze produced in the interior is regulated down at the exit by the impedance mismatch. This is a genuinely good piece of physics and the document states it cleanly.

**The caution** is in §IV.1 below: the two analog temperatures (`72.8` and `7.578 M_KK`) are surface-gravity readings, and the document should — and mostly does — keep them distinct from the *velocity* Mach number and the *acoustic-radius* Mach number, all of which are different ratios.

---

## III. Gate Verdicts (touched by this review — reproduced, not re-adjudicated)

| Gate / Result | Verdict (source) | Decisive Number | Reproduced? |
|:--|:--|:--|:--|
| T1 — Transit is sudden quench | PROVEN (S36/S38) | `δt/T_L = 1.25×10⁻⁵`, `P_exc = 1.000` | ✓ (MCP) |
| T4 — 59.8 quasiparticle pairs | PROVEN (S38) | `N_pair = 59.8`; `N_pair=1` exact reduction `1.2×10⁻¹⁴` | ✓ (MCP) |
| S85 — Acoustic white hole causal-disconnect | PROVEN (S85 W6) | pre/post-fold phonon-disconnected | ✓ (MCP) |
| S85 W10 — τ_fold uniqueness (van Hove) | PASS / promoted | `τ_fold = 0.190` unique non-stationary cusp | ✓ (MCP) |
| E7 — Structural monotonicity | PROVEN | `dS/dτ\|_fold = +58,672.8`; 9,600/9,600 | ✓ (consistent w/ memory W4/HESS-40) |
| `c_fabric` | canonical (S42) | `209.97368 M_KK` | ✓ (MCP exact) |
| `Mach_max` (velocity ratio) | canonical | `13.75` | ✓ (MCP exact) |
| `Mach (fold)` (acoustic-radius) | canonical (S59) | `421.3` (`R_acoustic = 442.9 M_KK²`) | ✓ (MCP exact) |
| `w0_FW` | canonical, **no PROVENANCE** | `−0.918` | ✓ value; provenance-gap confirmed |

---

## IV. Structural Implications (constraint-map reading)

### IV.1 — One genuine internal subtlety: which sound speed sets Mach 13.75?

The document's §5.2 conflation guard is **correct and necessary** — it separates the velocity-ratio Mach (`13.75`) from the fold-local acoustic-radius reading (`421.3`), and the knowledge graph confirms both (`Mach_max = 13.75`; `s59_spatial_aniso_log.txt`: `R_acoustic(fold) = 442.9 M_KK², Mach(fold) = 421.3`). It also correctly does **not** cite the third number floating in the graph, `Mach_max_analog = 54.3` (the S70 WKB-penumbra adiabaticity reading, `Mach = 54.73`), which would be a fourth distinct ratio. So the guard does its job.

But there is a deeper subtlety the guard does not surface, and it lives squarely in my domain. **There are two distinct sound speeds in the framework that both yield Mach 13.75**, because the velocity is scaled to match:

- `c_fabric = 209.97 M_KK` (the spectral-action modulus stiffness; what §5.2 cites), with `v_transit` correspondingly ≈ `2887 M_KK`.
- `c_BLV = 0.485 M_KK` (the BLV acoustic-metric sound speed; session-63 `ds²_acoustic` derivation), with `v_transit = 6.67 M_KK`.

Both give `v_transit/c = 13.75`. This is **internally consistent** (it is the same dimensionless diabaticity read in two metrics — the spectral-action metric and the emergent acoustic metric, which differ by the BLV factor `a_acoustic = a_geom·√(ρ/c_s)`, my memory S53). The four-speed hierarchy `c_mod = 1.0 > c_BLV = 0.485 > c_BA = 0.399 > c_L = 0.019–0.032` (matching ³He-B at cosine-similarity 0.996) is what reconciles them. **The recommendation is not a correction — the number is right — it is that the document cite the four-speed hierarchy at the point where it prints `c_fabric = 209.97`,** because a reader who knows the BLV acoustic metric will otherwise see `0.485` elsewhere in the corpus and suspect a 433× discrepancy where there is none. This is a one-clause fix (offered in §V) and it closes the single resonance-axis ambiguity I found.

### IV.2 — The strengthening (Wronskian = dispersion rigidity) tightens, does not loosen

Adding the dispersion-rigidity reading to §4.2 (II.3 above) is pure gain: it grounds the certified algebraic-independence theorem in the same band-lifting physics that §2.4 already invokes, converting two separate-sounding statements (band lifting at genesis; moment independence away from genesis) into one. No result changes; the claim gets a physical mechanism.

### IV.3 — The honest gaps are correctly classified as resonance-incomplete, not resonance-failures

The document's central gap (§6.3: no derived FRW `a(t)`; C1 postulated; C2/T6 BROKEN) is, from my axis, the statement that **the framework has the full mode spectrum and the full transit dynamics, but has not yet derived the map from the internal modulus-time to the emergent laboratory-time.** This is the correct place for the gap to live. A resonance theorist would phrase it: *we know every frequency the cavity admits and we know the impulse that excites them, but we have not derived the dispersion relation `t(τ)` that converts internal phase to lab seconds* (the `M_KK⁻¹ → seconds` normalization, §6.3 item iii). The document already says `τ` is a *derived monotone clock* (E7) but the *rate* `dτ/dt` is known only locally at the fold — this is exactly right and exactly the resonance reading. I have no objection; I endorse the §6.3 framing including its refusal to soften ("Friedmann is the wrong question is right about the fundamental level and wrong about the effective level — both must be said").

One small resonance-axis note on §8.5: the document's split — **ratio-observables truncation-robust, absolute-energy observables conditional on SDW convergence** — is the correct general principle and matches my standing result that only spectral *ratios* under a fixed regulator are physical (the FI partition). The cleanest scheme-invariant number, `R₁ = a₀a₄/a₂² = 1.12865` (Sage-verified `1.128655`), is a **dimensionless ratio of three frequency moments** — a pure shape number of the dispersion, immune to where you cut the sum. That it is offered as "the one scheme-invariant number on the cover" is the resonance-correct choice.

### IV.4 — Constants-hygiene flag (confirmed, domain-adjacent)

The document flags that `M_KK` and `w0_FW` carry values but lack PROVENANCE entries in the knowledge MCP. I confirm directly: `get_constant("w0_FW")` returns `−0.918` with `_No PROVENANCE entry_`. This is domain-adjacent because `w0_FW` is the `a₀`-layer dark-energy readout (the effacement-residual / Volovik-tracking output) — the headline of the DESI DR3 cliff-edge in §7.2. A provenance gap on the single most-exposed near-term prediction's central value should not block the capstone but should be routed to a hygiene pass (the document already says exactly this). No re-adjudication.

---

## V. Carry-Forward Computations

**Note on scope.** This is a document review, not a compute session. These carry-forwards are (a) verbiage/structural recommendations for the capstone, and (b) two genuinely computable resonance-axis gates the review surfaced. I keep both, four-field each.

### V.1 — Cite the four-speed hierarchy at the `c_fabric` printing (verbiage)

- **What**: At §5.2 item (ii), where the document prints `Mach = 13.75 (c_fabric = 209.97 M_KK)`, append one clause linking to the four-speed hierarchy so the reader does not mistake the BLV `c_BLV = 0.485 M_KK` (cited elsewhere in the corpus) for a contradiction.
- **Suggested verbiage**: *"(The same diabaticity reads Mach 13.75 in either the spectral-action metric, `c_fabric = 209.97 M_KK`, or the emergent BLV acoustic metric, `c_BLV = 0.485 M_KK`; the two differ by the BLV factor `a_acoustic = a_geom√(ρ/c_s)` and sit in the four-speed hierarchy `c_mod > c_BLV > c_BA > c_L` that matches ³He-B at cosine-similarity 0.996. The velocity is scaled to its metric; the dimensionless Mach is metric-independent.)"*
- **Inputs**: canonical `c_fabric = 209.97`, `Mach_max = 13.75`; four-speed hierarchy (memory `permanent-resonance-results.md`, S64/S69); BLV theorem (S53).
- **Gate**: documentation-hygiene; no numerical gate. PASS = clause present + four-speed cross-reference resolves.
- **Effort**: 15 min, 1 edit (mack-cosmic-bridge or orchestrator-direct, single-clause).

### V.2 — Add the dispersion-rigidity reading to the Wronskian (verbiage, strengthening)

- **What**: At §4.2, after the `W ∝ R_K′(τ)³` line, add one sentence giving the band-lifting / moment-ladder reading so the certified algebraic-independence theorem carries its physical mechanism.
- **Suggested verbiage**: *"In resonance terms this is a dispersion-rigidity statement: `a₀, a₂, a₄` are the zeroth/first/second moments of the single curvature scalar `R_K`, and the Wronskian of `{1, R_K, R_K²}` is proportional to `R_K′³` for the elementary reason that distinct powers of a *moving* scalar are independent. The layers collapse to one knob iff the dispersion stops moving (`R_K′ = 0`) — which happens only at the maximally-symmetric genesis point `τ=0`. This is the same band-lifting that §2.4 describes (`SO(8)→U(2)` into B1/B2/B3 as `τ` turns on), restated at the level of the spectral moments."*
- **Inputs**: §4.2 closed form (already in document, CERTIFIED S75 W2-E); §2.4 band-lifting; standard `W[{1,g,g²}] = 2g'³` identity (Sage-confirmable).
- **Gate**: documentation-strengthening; optional Sage cross-check `W[1, R_K(τ), R_K(τ)²]` returns `∝ R_K′³` (expected residual 0 vs the `5/(393216π¹²)V³` coefficient already in the ledger).
- **Effort**: 30 min incl. optional Sage verify, 1 edit.

### V.3 — Add the acoustic-envelope reading of `f* ∼ √x` (verbiage)

- **What**: At §3.2, where the document notes `f*` is evaluated by direct spectral sum because the `√x` piece makes Mellin moments divergent, add the resonance reading of *why* `√x` is the physical envelope.
- **Suggested verbiage**: *"The `√x` weighting is an acoustic (linear-in-frequency) envelope, `f(ω²) ∼ |ω|`: it up-weights the low acoustic modes (the B1 branch) relative to a Gaussian cutoff, which is both why the direct sum is dominated by the acoustic band and why the heat-kernel series — a Gaussian-adapted expansion — cannot represent it. The divergence of the Mellin moments is the spectral signature that the physical envelope is acoustic, not Gaussian."*
- **Inputs**: §3.2; memory S72 ("heat kernel expansion does not exist for `f*`"); Chebyshev-tilt theorem (S66–67, increasing `f` ⇒ red tilt).
- **Gate**: documentation; no numerical gate.
- **Effort**: 15 min, 1 edit.

### V.4 — (Computable) Surface-gravity ↔ Mach cross-table for §6.2 (optional precision gate)

- **What**: Build the explicit four-number table tying the two analog temperatures (`72.8`, `7.578 M_KK`) to the surface gravities `κ_entry, κ_exit = ∂_τ(c² − v²)|_horizon / 2c` and to the velocity-Mach (13.75) and acoustic-radius-Mach (421.3), so all four numbers in the white-hole section are visibly distinct readings of the same flow. Currently the two temperatures and two Machs are stated but their kinematic relationship is not tabulated.
- **Inputs**: `c_fabric = 209.97`, `c_BLV = 0.485`, `v_transit` at entry/exit `τ`, horizon locations `τ≈0.2195`/`τ∼0.16` (§6.2); analog-temperature definition `T_H = κ/2π`; BLV acoustic-metric `ds²_acoustic` (session-63).
- **Gate**: new INFO gate `WHITE-HOLE-KINEMATIC-CONSISTENCY` — PASS if `T_H^{entry}/T_H^{exit} = κ_entry/κ_exit` reproduces `72.8/7.578 = 9.61` from independently-computed surface gravities to within 10%; INFO otherwise (records which moment-channel impedance sets the ratio).
- **Effort**: 3–4 hours, 1 agent session (transit-dynamics or tesla-resonance), GPU not required (8-mode BdG + horizon-local derivatives).

### V.5 — (Computable) FI-confirm of `R₁` as a dispersion-shape invariant under truncation (optional robustness gate)

- **What**: Verify directly that `R₁ = a₀a₄/a₂²` is truncation-robust by computing it at `L_max ∈ {6,8,10,12}` from the raw mode-count moments and showing it converges to `1.12865` faster than any single moment, exhibiting the multiplicative-normalization-cancellation invariant of `math-scripts.md`.
- **Inputs**: raw mode-count triple (`a₀=155984`, `a₂=64308.24`, `a₄=29086.18` at `L_max=10`, §8.2); same at other `L_max` from the spectrum cache; canonical `R₁ = 1.128655`.
- **Gate**: feeds §8.5 SDW-convergence boundary — PASS if `|R₁(L_max) − 1.12865|` shrinks monotonically with `L_max` while individual `a_n^raw` diverge (confirms ratio-robust / absolute-conditional split); FAIL if `R₁` itself drifts > 1%.
- **Effort**: 2–3 hours, 1 agent session; reuses existing spectrum caches (`s84_spectrum_cache_L12`).

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:--|:--|:--|:--|
| II.1 | Action = trace + inner product = pure spectral functional; spectrum IS the mode set | GEOMETRIC + PHONONIC | ENDORSED | "Action cannot hear the basis, only the frequencies" — the resonance-axis reason the framework is spectral, not container |
| II.2 | `f` = mode-weighting envelope; tilt = envelope slope at band edge; FI/RD partition | PHONONIC / method | ENDORSED | Matches Debye-cutoff structure + Chebyshev-tilt theorem; `√x` = acoustic envelope |
| II.3 | Wronskian `∝ R_K′³` = dispersion rigidity (moment ladder of a moving scalar) | GEOMETRIC | CERTIFIED + strengthening offered (V.2) | Layers independent *because* dispersion is rigid away from the symmetric point = band-lifting restated |
| II.4 | Parametric-oscillator sweep, diabatic, `P_exc→1`; GGE = integrable impulse response | PHONONIC | PROVEN (T1/T4) | Sudden approximation correct (WKB inapplicable, S70); Ordered Veil backed by SFF no-ramp integrability |
| II.5 | Acoustic white hole, two horizons at `a₂` (geom) and `a₄` (matter) impedances | PHONONIC / GEOMETRIC | PROVEN (S85) | Horizon-problem resolution is supersonic-flow, not stretching; impedance regulates the escaping squeeze |
| IV.1 | Mach 13.75 rests on `c_fabric=209.97`; `c_BLV=0.485` gives same Mach via scaled `v` | resonance subtlety | CITE FOUR-SPEED HIERARCHY (V.1) | Not a correction — number is right; one-clause fix prevents a phantom 433× discrepancy |
| IV.4 | `w0_FW = −0.918` lacks PROVENANCE (confirmed via MCP) | hygiene, domain-adjacent | FLAGGED (already noted in doc) | Central value of the DESI-DR3 cliff-edge; route to hygiene pass, do not block |

---

**Bottom line.** From the resonance axis the document is honest, well-anchored, and structurally correct: it finds the cavity (`SU(3), g_τ`), the modes (the `D_K` spectrum), the boundary conditions (KO-dim 6, BDI, the gap that never closes), the envelope (`f`), and what selects the standing wave (the monotone `τ`-forcing through the van Hove fold). The single subtlety I found (two sound speeds, one Mach) is internally consistent and needs only a citation, not a fix. The single strengthening I offer (the Wronskian as dispersion rigidity) is free and tightens the strongest result in the document. Nothing here re-adjudicates a PROVEN/CERTIFIED status; the gate verdicts I touched all reproduce against the knowledge graph.
