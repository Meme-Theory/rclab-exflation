# Investigation 8 — Seed Digest

**Date**: 2026-06-14 (S108–109 plateau)
**Mode**: investigation (`/rclab-plan --investigation 8`)
**Seed (`--from`)**: three investigation-1 survey outputs —
`investigation-1/mack-cosmic-bridge.md` + `investigation-1/phonon-first-cosmologist.md` + `investigation-1/einstein-theorist.md`
(3-agent survey batch). Direct-seeded (no inv-1 `_synthesis.md` exists yet).
**Invocation note**: typed `--investigation 8 --context <3 files joined by &&>`; resolved to `--from`
(the canonical agent-survey seed shape; identical precedent inv-3 / inv-4 / inv-5 / inv-7).
**Shape**: fanout (4 per-wave plan files + thin plan-index).
**Source manifest** (each agent is sole writer of its inv-1 file):

| Agent | inv-1 file | Vantage | Sections lifted |
|:------|:-----------|:--------|:----------------|
| mack-cosmic-bridge | `investigation-1/mack-cosmic-bridge.md` | observational cosmology — DM/DE phenomenology, w(z), CMB/BAO, PBH, reionization, Hubble tension | G1–G5, C1–C6, U1–U5, R1–R5, B1–B5, NS 1–5 |
| phonon-first-cosmologist | `investigation-1/phonon-first-cosmologist.md` | cross-domain pattern detector — the seams between the eight pillars (analogue gravity, flat-band quantum geometry, Goldstone counting, Kibble-Zurek, SYK/Krylov) | G-1–G-4, C-1–C-4, A-1–A-4, R-1–R-5, B-1–B-6, NS 1–5 |
| einstein-theorist | `investigation-1/einstein-theorist.md` | principle-theory — covariance, equivalence principle, the cosmological term, EPR/Bell completeness, motion-from-field-equations | G-1–G-4, C-1–C-3, A-1–A-4, R-1–R-5, B-1–B-5, NS 1–5 |

---

## Thesis (cross-agent convergence)

The framework's deepest unresolved knot is **the single dimensionful-scale / a(t)–Hubble-backbone degree of freedom**, and all three vantages name it independently:

- **mack** (G2 + meta-knot): "three of my five biggest gaps and two of my contradictions trace to this one degree of freedom" — the a(t)/H²-freedom that simultaneously closes the CC (DILUTION-CC), blocks the H₀ prediction, leaves Friedmann BROKEN, and makes the vacuum a non-equilibrium transit.
- **einstein** (G-1): the "seconds-normalization of a(t)" — the surviving §6.3 residue; the substrate fixes the conformal class + all dimensionless shapes but imports exactly one dimensional scale `w = M_KK` (§VII.BS rank-1 NNU).
- **phonon-first** (G-1, sharpened): "a conformal class is precisely NOT a cosmology" — the substrate supplies the conformal class + the dimensionless tracking shape, but **the Hubble backbone H(τ) those shapes ride on is still imported, not derived** ("we import one number AND one function").

**Two NEW constructive attacks on the knot emerge** (the investigation's spine):

1. **einstein B-1**: Jacobson (2015) entanglement-equilibrium on the §VII.BZ modular weight `A_hor = A_K ⋊_{σ^ω} ℝ` → the **CC magnitude** (δS_ent = 0 at fixed volume; the framework built the modular machinery for horizon-faithfulness and never turned it on the CC).
2. **phonon-first B-1**: the integrated **quantum-metric stiffness** `∫ Tr g d²k` of the fold band, dimensionalized by M_KK → the **Hubble backbone H(τ)** (the post-2015 ideal-flat-band literature the framework's own Peotta-Törmä machinery is one step from).

The **same H²-freedom DOF drives the live dark-sector observational front** (mack C5 / phonon-first C-1 / einstein A-2): DESI w(z) (w_a = 0 four-fold lock vs `−0.73 ± 0.21`, **3.43σ and increasing**), the BBN-Volovik vise (`ΔN_eff = 2.087 > 1` overproduction vs 7-OOM present-CC undershoot escape), and the S_8 front (w_0 = −0.918 > −1 lowers σ_8 toward KiDS — a possible *asset*). **Two mechanisms compete** to explain the w_a≠0 / BBN tension: phonon-first B-3 (Kibble-Zurek Z_3 walls, w = −2/3) and einstein B-5 (running-vacuum RG, Solà `Λ(H) = c₀ + c₁H² + …`). Plus a **quantum-foundations cluster** (einstein C-1 Bell-vs-hidden-variable; R-2 Born rule) and **cross-domain spectral / condensed-matter bridges** (CDT spectral-dimension at high L_max; Higgs near-criticality; Watanabe-Murayama branch count).

### Cross-agent convergence map

| Convergence | mack | phonon-first | einstein | Investigation route |
|:------------|:-----|:-------------|:---------|:--------------------|
| **The a(t) / dimensionful-scale knot** (#1 framework gap) | G2 + meta-knot | G-1 (conformal-class ≠ cosmology; H(τ) imported) | G-1 (seconds-normalization) | W2-1 (Jacobson→CC-mag) + W3-2 (quantum-metric→H(τ)): TWO constructive attacks |
| **Dark-sector observational front** (DESI w(z) / BBN / S_8) | C5, B3, B5, U2 | C-1 (w_a hardening), C-4 (BBN vise), B-3 | A-2, R-3, B-5 | W1-2 (S_8+τ_reio) + W3-1 (Kibble-Zurek walls) + W2-4 (running-vacuum): observe + two mechanisms |
| **DM abundance closure** (Leggett saturates only ~21–25%) | G1, R1, U3, B2 | C-2 (Leggett-only permanent) | — | W1-1 (PBH from fold) + W1-3 (f_DM reconciliation) |
| **Quantum foundations** (Bell / Born / hidden-variable) | (B4 vacuum-decay) | B-6 (SYK/Krylov integrability) | C-1, B-4, R-2, G-3 | W4-1 (Bell adjudication workshop) + W2-3 (Born rule) |
| **n_s / w0_FW hygiene** (selection under observational stress) | U5, R5 | R-5 | C-3, A-4, R-4 | Routed OUT (Q2 hygiene HY2/HY3) — session-track |
| **Finite-L analytic-continuation ceiling** | C6, R3 | R-1 (spectral-dim L_max) | — | W1-4 (no-go theorem) + W3-3 (P(σ) L_max=14-16) |
| **Vacuum metastability / Higgs near-criticality** | B4 | B-5 (Higgs quartic running) | — | W3-4 (λ(μ) running) — bridges A-3 |

---

## Candidate gate table (deduped; per-wave bucketing)

Owner = reviewer-origin (the seed author whose domain the wave covers), except W4 whose owner is a NEUTRAL planner (`gen-physicist`) because it carries the two adjudication workshops where the W1/W2 owners are participants. Suggested exec = substrate-match (the per-wave planner finalizes). Every item traces to a specific seed finding (no invented items — the seed IS the scope).

### Wave 1 — mack-cosmic-bridge: observational cosmology & the dark-sector front

| # | Gate ID | gate_type | Suggested exec | Seed anchor | One-line scope |
|:--|:--------|:----------|:---------------|:------------|:---------------|
| 1 | INV8-W1-1 | compute | mack-cosmic-bridge (hawking-adjacent) | mack B2/G1/G4, NS-1 | PBH mass spectrum from the van Hove fold transit (first-order transition + S64 Bogoliubov spectrum + 59.8 Parker pairs + Mach 13.75); does f_PBH(M) integrate to the missing ~0.27 of Ω_DM in the [10¹⁷,10²³] g asteroid window? Closes f_DM abundance (G1) + first compact-object sector (G4). |
| 2 | INV8-W1-2 | compute | mack-cosmic-bridge | mack B3/B5/C5/R2, NS-5 | S_8 = σ_8√(Ω_m/0.3) + τ_reio from ONE GGE growth history (w_0=−0.918 > −1 suppresses late growth → low σ_8); σ-distance vs CMB-S_8 (~0.83) AND lensing-S_8 (KiDS 0.766); τ_reio vs Planck 0.054±0.007. Places w_0 on the DESI-liability AND S_8/τ_reio-asset ledgers. |
| 3 | INV8-W1-3 | solo | mack-cosmic-bridge | mack R1/U3, NS-3 | f_DM partition reconciliation: resolve the ≥4 register numbers (f_DM=0.006/0.209/0.947; Ω_DM=0.2657 vs Ω_DM h²=0.120) into ONE substrate-IS partition (mass anchor vs abundance vs cold-DM fraction); state supply-or-retire logic for the un-derived dimer-Z₂ Parker channel CONDITIONAL on W1-1. (Canonical-table WRITE is session-track HY4.) |
| 4 | INV8-W1-4 | compute | spectral-geometer (mack-origin) | mack R3/C6, NS-4 | Finite-L-cannot-reach-the-analytic-continuation-pole NO-GO theorem: prove which truncation families miss which poles `s < d/2` and from which side (the §VII.CB g_M = a_2_FW_zeta residue-subtracted continuation pattern that FAILED 3×). Structural theorem; the §VII row re-class is session-track HY6. |

### Wave 2 — einstein-theorist: the dimensionful-scale knot, precision-GR & quantum foundations

| # | Gate ID | gate_type | Suggested exec | Seed anchor | One-line scope |
|:--|:--------|:----------|:---------------|:------------|:---------------|
| 1 | INV8-W2-1 | compute | einstein-theorist (connes co-option for modular machinery) | einstein B-1/G-2/R-5, NS-2 | Jacobson-2015 entanglement-equilibrium → CC **magnitude**: vary GGE entanglement entropy of a small causal diamond on the §VII.BZ modular weight `A_hor = A_K⋊_{σ^ω}ℝ`, impose δS_ent=0 at fixed volume, read off Λ. Attacks JACOBSON-NONLOCAL-64 (the gate gating CC/A_s magnitudes). |
| 2 | INV8-W2-2 | compute | einstein-theorist | einstein B-3/G-1, NS-3 | Emergent PPN (γ, β) + emergent Eötvös η of g_M from the a₂/a₄ moment structure + residual band-dependence at NNLO; test vs Cassini |γ−1|<2.3e-5 + MICROSCOPE η<1e-15. OBSERVATION-FREE falsifier — if η_emergent>1e-15 the framework is already falsified by existing data. Extends the S95 §W3-2 leading-order EP PASS. |
| 3 | INV8-W2-3 | compute | einstein-theorist (kitaev co-option for GGE structure) | einstein R-2/G-3, NS-4 | Born rule derive-or-no-go (S58 VI.1): trace over the GGE's 8 Richardson-Gaudin integrals → reduced density matrix for one phonon mode → check probabilities = |ψ|². PASS = derived from coarse-graining; INFO = no-go (Born rule is an input like the metric signature). |
| 4 | INV8-W2-4 | compute | einstein-theorist (volovik co-option for q-theory) | einstein B-5/A-2/C5 | Running-vacuum (Solà) RG `c₁` coefficient of `Λ(H)=c₀+c₁H²+…` vs the substrate q-theory n=2 tracking coefficient (k=+3586.5 M_KK, S97); agreement ⇒ C10's borrowed-external-H is RG-grounded, not borrowed; check the RG `Λ(H_BBN)` against the S99 ~2.087× ΔN_eff shortfall. |

### Wave 3 — phonon-first-cosmologist: cross-domain bridges (transit + condensed-matter + spectral-geometry)

| # | Gate ID | gate_type | Suggested exec | Seed anchor | One-line scope |
|:--|:--------|:----------|:---------------|:------------|:---------------|
| 1 | INV8-W3-1 | compute | transit-dynamics-theorist | pfc B-3, NS-1 | Kibble-Zurek defect density of the transit through the ACTUAL Z_3-structured Jensen manifold at the ACTUAL Mach 13.75 (z=2 known, dt/T_L=1.25e-5): does a frozen Z_3 wall network form (the π_0(U(1))=0 "no-walls" argument may have used U(1) instead of U(1)×Z_3)? Walls give w=−2/3 (candidate DESI w_a≠0) + a^{−1}-redshifting BBN channel. Reaches C-1 (w_a) AND C-4 (BBN) with one compute. |
| 2 | INV8-W3-2 | compute | phonon-first-cosmologist (baptista/landau co-option for the quantum metric) | pfc B-1/G-1, NS-2 | Quantum-metric stiffness: compute `∫ Tr g d²k` of the fold band (g_ab = Re⟨∂_a u|(1−P)|∂_b u⟩, substrate-IS, no imported scale but M_KK), dimensionalize by M_KK, test whether the Peotta-Törmä superfluid-weight stiffness IS the Hubble backbone H(τ) the rank-1 NNU theorem imports. If yes, the a(t) gap closes from a substrate-IS invariant. (Substrate flat band: Tr g>0, Ω=0 — the C=0 maximally-NON-ideal case.) |
| 3 | INV8-W3-3 | compute | spectral-geometer (phonon-first co-author) | pfc R-1, NS-3 | Push P(σ)=Tr e^{−σ D_K²} to L_max=14-16 (GT-builder lifts the Sym^13/14 wall, S105): compute d_s(σ→0) (Weyl/manifold dim, should → 8) AND d_s(σ_*) (windowed at the fold) past the narrow-band artifact; make the CDT/asymptotic-safety dimensional-reduction comparison the framework currently ASSERTS but never measured (energy-axis γ_E, per the diffusion-window K=2 specialization). |
| 4 | INV8-W3-4 | compute | phonon-first-cosmologist (connes co-option for the quartic RG) | pfc B-5 | Run the Higgs quartic λ(μ) from m_H=131.8 GeV up to M_KK on the substrate spectrum: does λ stay positive (absolute stability — a prediction distinguishing the substrate from the SM) or λ→0 near some scale (SM near-criticality reproduced from geometry — strong evidence f IS physical, bridges A-3)? |
| 5 | INV8-W3-5 | compute | phonon-first-cosmologist (landau co-option for Goldstone classification) | pfc B-2/R-2 | Watanabe-Murayama Goldstone counting `n_NG=(dim G−dim H)−½ rank ρ`, ρ_ab=−i⟨[Q_a,Q_b]⟩ from the D_K commutator/Kosmann-connection algebra (z=2 known ⇒ Type-B): settle the 6-vs-7 branch count as a theorem WITHOUT the deferred full SU(3) sigma-model, and classify Type-A (acoustic, feed GGE pair count → A_s) vs Type-B. |

### Wave 4 — cross-vantage adjudications (the two genuine Q1a workshops)

| # | Gate ID | gate_type | Agents (EXACTLY 2, 2 rounds) | Seed anchor | One-line scope |
|:--|:--------|:----------|:-----------------------------|:------------|:---------------|
| 1 | INV8-W4-1 | workshop | einstein-theorist ↔ kitaev-quantum-chaos-theorist | einstein C-1/B-4/G-3, NS-1 | Bell-vs-hidden-variable: S58 "GGE IS the hidden variable / superdeterminism (QM emergent from determinism)" vs S70 "GGE pairs violate CHSH 8/8 modes, S up to 2.452 (GGE is quantum)". Resolve via the framework's own M2 algebra-axis orthogonality — split the GGE into a classical thermodynamic layer (mode-effective temperatures, would-be hidden variable) ⊥ an irreducibly-quantum entanglement layer. STRUCTURAL VERDICT on what the GGE IS. |
| 2 | INV8-W4-2 | workshop | mack-cosmic-bridge ↔ connes-ncg-theorist | mack B1/C2/U5, NS-2 | Cosmic birefringence: does the effacement-residual a₀ dark-energy component carry a parity-odd Chern-Simons coupling (mack: β≠0, predict β vs Minami-Komatsu 0.342°±0.094°, LiteBIRD-decisive) or does the CPT-exact spectrum [J,D_K]=0 + γ9-tracelessness Tr(γ9 f)=0 (T7) FORBID isotropic birefringence (connes: β=0, framework predicts a null)? STRUCTURAL VERDICT on β — a parity falsifier ORTHOGONAL to the tilt observables (breaks the n_s/α_s/a₀-DE degeneracy). |

**gate_type rationale (Q1/Q2/Q3 per `Investigating-Workshops.md`)**:
- **W4-1 + W4-2 are genuine Q1a workshops** — TWO agents, opposed first-principles readings of a SPECIFIC tension, multi-round (R1 steelman / R2 rebuttal / R3 converge), output a STRUCTURAL VERDICT. W4-1: einstein holds the principle-theory completeness reading (the M2-split resolution — the GGE carries irreducible Bell-entanglement, so "QM emergent from determinism" is false-as-stated), kitaev authored the S70 Bell-PASS and holds the quantum-chaos reading; the GGE is the shared object both read oppositely. W4-2: mack holds the effacement-DE parity-coupling reading (β≠0), connes holds the γ9-traceless/CPT-exact reading (β=0) and owns the NCG parity sector; the substrate's parity machinery is the shared evidence.
- **The a(t)-knot is NOT a workshop** — the two constructive attacks (W2-1 Jacobson, W3-2 quantum-metric) are independent COMPUTES; you cannot adjudicate readings whose values do not yet exist. Their convergence (do both routes land on the same dimensionful scale?) is the job of `/rclab-investigate --investigation 8` at close, not a plan-time gate.
- **The w_a/BBN mechanisms are NOT a workshop** — Kibble-Zurek walls (W3-1) and running-vacuum (W2-4) are two independent candidate MECHANISMS, each with its own compute, not two readings of one object.

---

## Routed OUT — Q2 session-track hygiene (NOT investigation gates)

An investigation cannot mutate curated session-track registers (track-local boundary per `gate-verdicts.md §"Investigation-Track Canonical Path"`). These route to session-promotion at `/rclab-investigate --investigation 8` close, NOT to gates in this plan.

| HY | Item | Seed anchor | Session-track target |
|:---|:-----|:------------|:---------------------|
| HY1 | Promote the EMERGENT-EIH-LIFT framing in the capstone — frontier #1/#8 is structurally CLOSED (emergent EIH conservation identity §W3-1 + derived emergent EP §W3-2); residue = the single seconds-normalization `w=M_KK` of §VII.BS. Retire "frontier #1/#8 fully open." | einstein R-1, NS-5 | capstone `phonic-exflation-equation.md` (designated-writer patch; capstone-hygiene Q3) |
| HY2 | Reconcile the n_s "CLOSED + firing-in-falsifying-direction" label (the functional is committed; the value 0.9590 is 1.40σ→5σ low against Planck→P-ACT). Report n_s as a BAND [0.9557, 0.9595] with the √x selection explicitly carried, not a point + single σ. | mack U5/R5, pfc R-5, einstein C-3/A-4 | capstone §7 + atlas-04 §IX + `falsifier-master-inventory.md` (mack sole-writer) |
| HY3 | Add a gate/provenance for `w0_FW = −0.918` (currently `Gate: None` despite being a load-bearing 2.13σ→DR3-binding observational prediction). | einstein R-4 | `canonical_constants.py` PROVENANCE |
| HY4 | f_DM canonical partition TABLE write + a PROVENANCE entry for `Omega_DM = 0.2657` (currently none). The reconciliation COMPUTE is INV8-W1-3; the table-into-register WRITE is session-track. | mack R1, NS-3 | `canonical_constants.py` + `falsifier-master-inventory.md` (mack sole-writer) |
| HY5 | Register the Strutinsky = O'Neill A-tensor = spectral-action saddle-point cross-pillar identity (gradient ratio 0.71 at the fold) as a §VII slot with the 5-anatomy treatment — currently sits in agent memory, not the permanent-results registry. | pfc R-4 | `permanent-results-registry.md` §VII (5-anatomy) |
| HY6 | Re-class the §VII.CB/AU/BT/AM Level-3 rows as "structurally-unreachable-by-design, Level-1 cohomology-class identity carries the result" — CONDITIONAL on the INV8-W1-4 no-go theorem landing. | mack R3/C6, NS-4 | `permanent-results-registry.md` §VII (mack sole-writer of the observable surface) |

---

## Surveyed-but-not-elevated bridges (context cross-refs, NOT gates)

Per "the highest-leverage-next-steps block is the PRIMARY source" — these survey bridges were NOT in any agent's top-5 next-steps; they are recorded as context cross-references for the gates that DO land, and as candidate seeds for a future investigation.

- **einstein B-2** (Penrose-Diósi gravitational decoherence, derived E_G(a₂, band-difference) measurement scale replacing the S58 F_J coincidence) — adjacent to INV8-W2-3 (Born rule) + C-2; cross-ref in W2-3 context.
- **mack B4** (vacuum-decay rate Γ(τ_fold→τ′) as the τ_fold metastability selector) — adjacent to INV8-W3-4 (Higgs quartic running / metastability); cross-ref in W3-4 context.
- **phonon-first B-4** (analog-gravity QNM ringdown of the sonic horizon → compact-object sector, rescues a GW observable the Item-49 CGWB retirement gave up) — adjacent to INV8-W1-1 (PBH = the OTHER compact-object route) + Row #88; cross-ref in W1-1 context.
- **phonon-first B-6** (SYK/Krylov complexity vs the substrate's λ_L=0 integrability — which modes are bounded-Krylov/permanent vs linear-Krylov/thermalizing) — adjacent to INV8-W4-1 (Bell GGE classical/quantum split) + C-2; cross-ref in W4-1 context.

---

## Cross-investigation dedup (load-bearing — each gate block MUST carry its cross-reference so `/rclab-coordinate` does not see redundancy)

Every adjacency to the prior inv-2…inv-7 clusters is **complementary (distinct machinery / distinct observable), NOT duplicate**:

- **INV8-W1-1 (PBH from fold)** ↔ inv-4 GR batch (compact-object causal structure) + inv-6 kaluza-klein (Row #88 compact-object cell) + inv-7 W2-2 (LRD accretion-photosphere envelope) + inv-7 W3-1 (LQG modular-horizon entropy): all touch the empty compact-object sector (Row #88), but INV8-W1-1 is the FIRST FORMATION-CHANNEL route (a fold-transit PBH mass FUNCTION), distinct from the envelope/entropy/causal-structure routes.
- **INV8-W2-1 (Jacobson entanglement-equilibrium → CC MAGNITUDE)** ↔ inv-4 W1-2 (Euclidean replica → 1/4 area coefficient) + inv-4 W3-1 (de Sitter a₀ horizon first law) + inv-5 W1-5 (entropy-functional CC a₀/a₂) + inv-7 W3-1 (modular-horizon entropy S∝A/4G): all use the §VII.BZ crossed product / JACOBSON-NONLOCAL-64, but INV8-W2-1 is the entanglement-equilibrium VARIATION (δS_ent=0) reading off the CC MAGNITUDE, distinct from the area-coefficient / first-law / entropy-functional routes.
- **INV8-W2-3 (Born rule) + INV8-W4-1 (Bell)** — FRESH; no prior investigation touched the Bell/Born-rule/superdeterminism quantum-foundations cluster (inv-1 has not yet spawned a foundations investigation).
- **INV8-W3-1 (Kibble-Zurek walls) + INV8-W2-4 (running-vacuum)** — FRESH mechanism-computes for the w_a/BBN tension; inv-4 W3-1 (de Sitter a₀ ≡ Volovik tracking) and inv-5 W1-2/W1-5 (a₄-anomaly + entropy-functional CC) touch the SAME CC but neither computes a wall network or an RG-running c₁H².
- **INV8-W3-3 (P(σ) @ L_max=14-16, CDT comparison)** ↔ inv-3 W2-1 (d_s-flow as K→K* map) + inv-3 W2-2 (isospectral rigidity at L_max=3): same heat-trace d_s observable, but INV8-W3-3 is the HIGH-L_max (14-16) CDT/asymptotic-safety dimensional-reduction comparison (GT-builder unlock), distinct from the K→K* scale-transport map and the low-L_max rigidity test.
- **INV8-W3-4 (Higgs quartic λ RUNNING / near-criticality)** ↔ inv-5 W1-1 (Pati-Salam Higgs quartic m_H VALUE) + inv-5 W2-3 (Pekker-Varma Higgs self-energy) + inv-5 W3-3 (Higgs-residual synthesis): all touch the Higgs sector, but INV8-W3-4 is the RG-RUNNING/metastability question (does λ→0 near a high scale?), distinct from the m_H-VALUE +5.36% residual computes.
- **INV8-W1-4 (finite-L no-go theorem)** — the structural generalization of the §VII.CB/AU/BT/AM recurring Level-3 FAILs (mack R3/C6); no prior investigation proved the general no-go. Cross-references INV8-W3-3 (the OTHER L_max-truncation gate — they share the "what a finite truncation can/cannot reach in a spectral sum" theme).

A result that must become permanent is **promoted into a session** (lifted as a carry-forward into a session-mode `/rclab-plan` plan and re-computed under a `session-{N}` gate), not held here — `gate-verdicts.md §"Investigation-Track Canonical Path"` (track-local boundary).
