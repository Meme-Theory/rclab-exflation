# Investigation-1 — Cross-Cutting Synthesis

**Author:** orchestrator (Claude Opus 4.8). **Date:** 2026-06-14.
**Scope:** a wholesale, open-ended survey of the phonon-exflation framework at the S108/S109 plateau, by 31 research agents, each given the *identical* neutral charge (see `README.md`) and writing to its own file. No per-agent angle was injected (`feedback_review-dispatch-no-orchestrator-angle.md`).

**What this document is — and is not.** This synthesis is *derivative*: it summarizes and cross-indexes the 31 agent files. Every claim below is attributed to the agent file(s) that made it; those files carry the citations (registry slots, gates, constants, papers). Where a claim is a status-tag assertion (e.g. "EVOI says CLOSED, atlas-04 says CONDITIONAL"), it is the AGENT's reading and the relevant register cell should be checked before acting. The orchestrator has NOT independently re-verified each claim — this is a map of what 31 independent domain lenses surfaced, not a re-adjudication.

**On the epistemic weight of convergence.** Per `epistemic-discipline.md`, "agreement among agents" is *not* independent confirmation when agents share context. These 31 agents shared the SAME source (the framework) but applied DIFFERENT domain lenses and did NOT see each other's work. So convergence here means: *a structural feature visible from many independent vantages* — i.e., robust and not an artifact of one specialty. That is the signal. It is a triage prior for where to spend the next compute cycle, not a proof of anything.

---

## 0. The one-sentence verdict of the survey

The framework is **solid where it is intensive and structural, and soft where it is dimensionful and dynamical**: its proven core is a set of regulator-invariant, dimensionless, machine-ε structural identities (KO-dim=6, [J,D_K]=0, BDI, rank-1 normalization theorems, 10 blind STAGE-3 cross-axis promotions), while every one of its largest live gaps is a *single imported dimensional scale or an un-built dynamical sector* — and, strikingly, **the agents independently converge that most of those gaps are facets of only ~4 underlying holes**, each of which has a concrete, named, off-the-shelf piece of known physics that could fill it.

---

## 1. Cross-agent CONVERGENCE (ranked by number of independent vantages)

### CV-1 · The A_s amplitude is computed with the WRONG functional — and the "wall" disagrees with itself  *(8 agents)*
`gen-physicist`, `kaluza-klein`, `spectral-geometer`, `landau`, `transit-dynamics`, `quantum-acoustics`, `hawking`, `feynman`.
The scalar-amplitude A_s is the framework's single largest observational gap, and the agents independently diagnose the *same root cause*: an **equilibrium free-energy functional applied to a sudden (impulsive) quench**. The fix they all point to is the same — a **Bogoliubov |β_k|² / Parker-Bogoliubov power spectrum with adiabatic regularization**, not slow-roll `1/ε_H`. Damningly, the "permanent wall" is internally incoherent: the A_s miss is quoted at **3.02 / 3.15 / 4.56 / 9.5 OOM across the corpus, and even sign-flips** (S66 under-production vs S74/S77 over-production) — `landau`, `quantum-acoustics`. No A_s gate has a meaningful threshold until one canonical number is defined. The gate that would settle it — **TRANSIT-PS-67, which the constraint-matrix itself calls CRITICAL — has never actually been run** (only MIGRATED placeholder entries: `quantum-acoustics`, `tesla`, `feynman`).

### CV-2 · M_KK is the keystone: one imported scale masquerading as several "walls"  *(≈6 agents)*
`gen-physicist`, `kaluza-klein`, `nazarewicz`, `kaku`, `spectral-geometer`, (`dirac` on η_B normalization).
M_KK is **frozen-since-S42, matched to gravity, never derived**; the §VII.BS rank-1 normalization theorem *proves* it is the framework's sole imported dimensional scale. Consequence the agents converge on: the framework's honest claim is **"zero *continuous* parameters given SU(3)/Jensen + one imported M_KK,"** not "zero free parameters" (`gen-physicist`). `kaku` sharpens this to the cleanest form: the four "input dials" (K_pivot, A_s, τ_fold, M_KK) are **not four gaps but ONE unbuilt structural sector** — moduli stabilization / dimensional transmutation. `nazarewicz` supplies the missing mechanism by name: **M_KK/M_Pl = exp(−c/λ_eff) from the van Hove fold's DOS singularity = BCS/Coleman-Weinberg physics nobody has written.**

### CV-3 · a(t) / the τ↔t map / the effective Friedmann equation is IMPORTED, not derived  *(≈7 agents)*
`phonon-first-cosmologist`, `hawking`, `schwarzschild-penrose`, `van-den-dungen`, `loop-quantum-gravity`, `gen-physicist`, `nazarewicz`.
The framework's own #1 frontier. The rank-1 NNU theorem fixes the *conformal class* and the dimensionless tracking shape, but **a conformal class is not a cosmology — the Hubble backbone H(τ) is still imported** (`phonon-first`). The **τ↔t map (atlas-04 C1) is the master load-bearing assumption** (`schwarzschild-penrose`). `hawking` supplies the deepest structural insight of the whole survey: **the volume-preserving constraint (G6) that delivers the clean τ-independent G_N is the *same* constraint that empties the a₂ conformal clock (a_eff stationary ⇒ q=0/0)** — which explains why a(t) has resisted derivation for ~40 sessions, and the register has never named those two entries together. `loop-quantum-gravity`: §6.3 itself names the missing object as loop-quantum-cosmology's effective-Friedmann template.

### CV-4 · The cosmological constant is TRADED, not solved — and ρ_vac~H² is overloaded  *(≈5 agents)*
`volovik`, `quantum-foam`, `mack`, `einstein`, `connes`.
DILUTION-CC's present-epoch closure and the BBN failure are **the same ρ_vac~H² equation evaluated at two redshifts** (`volovik`: S99-W2-BBN-RELIEF FAIL = 2.087× at BBN). `mack` sharpens it to a mutual-exclusivity: **the tracking-vacuum H²-freedom the CC closure needs structurally forbids a fixed-magnitude H₀** (67.4 degenerates to H_obs) — one degree of freedom driving 3 of 5 cosmology gaps. `quantum-foam`: CC is translated to a scale degeneracy (= Carlip Λ_eff⊥Λ_bare), split across two registers, should be stated once. `connes`: the spectral action gives the wrong CC by 120 OOM while a *separate* Volovik functional gives the right one ⇒ the spectral action provably is NOT the substrate's free energy.

### CV-5 · The GGE relic is the richest UNDER-EXPLOITED asset in the framework  *(≈6 agents, as a bridge)*
`hawking`, `gen-physicist`, `string-theory`, `kaku`, `transit-dynamics`, `berry`, `einstein`.
Independently, six agents point at the computed D_K/GGE spectrum as the framework's most powerful unused object: **(a)** its entanglement spectrum IS a Page-curve object supplying the microstate count S=A/4G needs (`hawking`); **(b)** it should imprint a unique, non-slow-roll-degenerate folded **cosmological-collider bispectrum f_NL** with features at eigenvalue ratios — a sharp DESI/Euclid observable (`gen-physicist`, `kaku`); **(c)** Type III₁ modular-flow dephasing on the K₇=0 visible subalgebra is the route to emergent QM (`kitaev`, `einstein`); **(d)** the relic {β_k} locked by one ODE + a Floquet band-structure calc resolves the diabatic-freeze-vs-resonance tension (`transit`). The GGE is computed but never *queried* for these.

### CV-6 · The spectral-dimension flow d_s(σ) is a CDT/asymptotic-safety bridge misfiled as "resolved"  *(4 agents)*
`spectral-geometer`, `tesla`, `gen-physicist`, `quantum-foam`.
The substrate's own UV spectral-dimension flow (d_s → ~1.7) **IS the CDT / asymptotic-safety dimensional-reduction signature**, but is filed "RESOLVED / not-relevant." `tesla`: the SU(3)-fiber d_s was proven to have no CDT reduction, but the **M⁴-summand d_s flow — where the d_s≈3.91 that n_s needs lives — has never been computed.** `spectral-geometer` proposes running d_s(σ) as the UV→IR *transport* map (the K→K* scale map), which could close the largest observational gap with existing machinery.

### CV-7 · The dark sector is unreconciled and the DM mass is unbuilt  *(4 agents)*
`volovik`, `landau`, `quantum-acoustics`, `mack`.
Two unreconciled DM accounts run in parallel — the Leggett-channel cold relic vs Volovik's own 2024 stiff-matter w=1 from the same vacuum (`volovik`); the Leggett channel fills only ~21–25% of cold DM (`mack`). `landau` proposes an NSR/pseudogap two-scale decomposition for the missing ~14× mass factor; `quantum-acoustics` notes the flat-band B2 IS a degenerate roton (Umklapp-forbidden) = an eternal second DM candidate; `mack` proposes PBH from the fold transit to fill both the abundance gap and the empty compact-object sector.

### CV-8 · Yukawa hierarchy lives only in the unexplored moduli space — and modular flavor symmetry is the mechanism  *(3 agents, two converging on the SAME tool)*
`baptista`, `string-theory`, `kaku`.
`baptista`: every "off-Jensen" result is a 5D U(2)-invariant projection; the framework's own Schur theorem says the **Yukawa hierarchy can ONLY live in the unexplored 23D complement** (the rank-1 "wall" tests for a hierarchy in the one region the theorem forbids it). Then **`string-theory` and `kaku` *independently* arrive at the same specific fix: modular flavor symmetry (Dedekind-η), already latent in the framework's threshold corrections** — closing the rank-1 Yukawa wall AND supplying a principled τ↔K e-fold map from one structure. Two domains, same mechanism, no cross-talk: the strongest single convergence in the survey.

### CV-9 · There is NO compact-object sector — and that is where the first anchor-free prediction lives  *(≈5 agents)*
`schwarzschild-penrose`, `sagan`, `mack`, `hawking`, `little-red-dots`, `dirac`.
"CORPUS-EXCEEDS" (S106): no mass-radius, no QNM spectrum, no formation channel. Multiple agents note this is the framework's best escape from the M_KK problem: **a compact-object R/M ratio is dimensionless and anchor-free** (`sagan`), testable by NICER / QNM-echoes / asteroid-mass PBHs, and Gregory-Laflamme stability of the dynamical M⁴×SU(3) would be the framework's first compact-object-like structure (`schwarzschild-penrose`).

### CV-10 · META: register status optimism outruns derivation state  *(≈6 agents)*
`dirac`, `little-red-dots`, `loop-quantum-gravity`, `einstein`, `neutrino`, `kitaev`.
A cross-domain pattern surfaced independently by agents who could not see each other: **EVOI / atlas-04 / falsifier-inventory status tags run ahead of the actual derivation state.** Instances: baryogenesis tagged CLOSED-SOURCED-UNIQUE (EVOI) vs CONDITIONAL (atlas-04 C6), 1.1 OOM short (`dirac`); JWST-LRD BH-seed spectrum tagged LIVE-"predictions" with no derived mechanism (`little-red-dots`); Z₃-triality "three generations" PROVEN (MCP) vs capstone frontier #7 "open" (`loop-quantum-gravity`). This is exactly the drift the `capstone-hygiene-gate.md` Q3 discipline exists to catch — see §4.

---

## 2. Highest-leverage UNTRAVELED BRIDGES (the user's "most important" ask)

Ranked by (gaps closed) × (existing-infrastructure proximity). Each: the known-physics result → how the substrate fills the cement → which gaps/contradictions it bridges → who proposed it.

| # | Bridge | Known-physics anchor | Closes / bridges | Proposers | Cost |
|:--|:-------|:---------------------|:-----------------|:----------|:-----|
| **B-1** | **Run TRANSIT-PS-67 as a Parker-Bogoliubov \|β_k\|² power spectrum with adiabatic regularization** | Parker particle production; adiabatic regularization | A_s + K_pivot + α_s + n_s(k) **simultaneously** (CV-1); it's the gate the framework itself calls CRITICAL but never ran | feynman, quantum-acoustics, tesla, transit, landau, gen-physicist | **1 compute gate, existing infra** — the single highest-EVOI item in the survey |
| **B-2** | **Derive M_KK by dimensional transmutation** `M_KK/M_Pl = exp(−c/λ_eff)` from the van Hove fold DOS singularity | BCS gap / Coleman-Weinberg | The keystone scale (CV-2); collapses the four "dials" to one derived number | nazarewicz, kaku | 1 structural workshop |
| **B-3** | **Modular flavor symmetry** — D_K(τ) near the fold as a Dedekind-η modular form | Feruglio 1706.08749; modular-form flavor models | rank-1 Yukawa wall (CV-8) **AND** τ↔K e-fold map (CV-3) from one structure; η already in the threshold corrections | string-theory + kaku (independent) | 1 structural workshop |
| **B-4** | **Effective Friedmann H²(ρ) + Raychaudhuri focusing** for the reduced (a,τ) congruence | LQC `H²=(8πG/3)ρ(1−ρ/ρ_c)`; Raychaudhuri | a(t) / τ↔t map / white-hole zero-count (CV-3); §6.3 names LQC as the template | loop-quantum-gravity, schwarzschild-penrose, phonon-first | 1 compute gate |
| **B-5** | **Query the GGE entanglement spectrum** (Page curve, microstate count, cosmological-collider bispectrum) | Page curve / island formula; cosmological collider | S=A/4G microstate count + info ledger (CV-5); a falsifiable DESI/Euclid f_NL shape | hawking, gen-physicist, kaku, string-theory | 1–2 compute gates on existing 8-branch spectrum |
| **B-6** | **GGE inter-branch strong-rescattering phase** inserted into the η_B amplitude | **LHCb 2025 (2504.15008): % baryon CP from strong final-state phases** | η_B under-production (could supply the missing ×13.5) + lepton/baryon CP orthogonality (dirac C-1/C-3) | dirac | 1 compute gate on Row #67 infra |
| **B-7** | **Coupled two-fluid DE↔stiff-DM decay ODE** (effacement leak = the energy-exchange term) | Volovik 2024 two-fluid q-theory | BBN FAIL + dark-sector contradiction + stranded w=1 epoch (CV-4, CV-7) in one ODE | volovik | 1 compute gate |
| **B-8** | **Build the compact-object sector** (R/M, QNM-echoes, asteroid-mass PBH) | NICER mass-radius; ringdown echoes; PBH | first **dimensionless, anchor-free** gravity prediction → escapes the M_KK limitation (CV-2, CV-9) | sagan, schwarzschild-penrose, mack | new sector (larger) |
| **B-9** | **Cosmic birefringence β prediction** | Minami-Komatsu β≈0.34° (3.6σ) | a near-term LiteBIRD falsifier orthogonal to the n_s/α_s degeneracy; parity machinery ([J,D_K]=0, parity-twin pair) already present | mack | 1 compute gate |
| **B-10** | **Void Size Function + persistent-homology Betti curves** of the 325 Mpc ring; KBC-void timescape | Void statistics; KBC 6σ void; topological data analysis | the *only* observable distinguishing the framework from ΛCDM when 2-pt stats match; native Hubble-tension mechanism (CV-3) | cosmic-web | new sub-sector |
| **B-11** | **Emergent QM from Type III₁ modular-flow GGE dephasing** on the K₇=0 visible subalgebra | Tomita-Takesaki modular theory; eigenstate thermalization | the FOUNDING gap (CV-5e): why an integrable substrate gives QM — replaces dead scrambling/Fermi-point routes; compatible with λ_L=0, N₃=0 | kitaev, einstein, kaku | 1 structural workshop |
| **B-12** | **Aim §VII.BZ modular machinery at a Jacobson entanglement-equilibrium CC magnitude** | Jacobson 1995 / 2016 entanglement equilibrium | CC *magnitude* (CV-4) — machinery built, never pointed at the target | einstein | 1 compute gate |
| **B-13** | **a₄ conformal-anomaly / Weyl² term** | conformal anomaly | the one un-closed spectral-action CC channel (non-monotone, escapes the W4 wall) + the two-effective-action tension | connes | 1 compute gate |
| **B-14** | **NCG J-breaking deformation classification** (Boyle-Farnsworth / Bochniak-Sitarz) | algebraic SM; fermion-doubling-avoidance | turns the posited δA baryogenesis source into a *derived* object (dirac LBA-1) — a different δA could fix the 1.1 OOM | dirac, connes | 1 structural workshop |

Secondary domain bridges worth a row each (see the named files): Casimir energy of the 992-mode tower in the volume direction → derives volume-preservation + a 3rd M_KK (`kaluza-klein`); Kibble-Zurek **Z₃ defect** network → w_a + BBN (`phonon-first`); δ_CP∈{0,π} + spectrum-forced sterile-null + ΔN_eff(ν)≈0 as zero-parameter neutrino predictions for DUNE/Hyper-K (`neutrino`); Sen-tachyon K-theory descent → unitary information dynamics (`string-theory`); Vinen-vs-Kolmogorov quantum-turbulence cascade exponent → the missing TRANSIT-PS-67 input (`tesla`); Richardson-Gaudin / von-Delft ultrasmall-grain pairing → fixes the factor-~2 gap uncertainty feeding M_KK (`nazarewicz`); positronium-BEC as a lab analog of the CPT-neutral GGE relic (`dirac`); Krein-space / Lorentzian submersion NCG → the rigorous Lorentzian transit replacing naive Wick rotation (`van-den-dungen`).

---

## 3. Critical CONTRADICTIONS to adjudicate (math/physics, not bookkeeping)

These are genuine ledger-dissonances where two results cannot both be right as stated — candidate `/rclab-investigate` workshops (Q1 math/physics adjudications per `Investigating-Workshops.md`):

1. **Order-one axiom BROKEN (norm 4.0) vs D_K≡D_F Higgs-as-inner-fluctuation** — `connes`. If order-one fails, the linear/quadratic gauge+Higgs split is unprotected (CCS-2013); the §VII.W-3 Wedderburn "rescue" repairs only the χ-killed BdG corner, not D_total.
2. **Spectral action ≠ substrate free energy** — `connes` (wrong CC by 120 OOM while a separate Volovik functional is right). A deep, under-stated consequence of S37.
3. **Ordered-Veil diabatic-freeze ("never thermalizes") vs the LIVE in-band parametric resonance §VII.BP** (ω_q=2.0128 M_KK inside the pair band) — `transit`. Registered COINCIDENCE-BOUNDED, never resolved by a Floquet calc.
4. **BELL-GGE-70 (Bell-violating, S>2, 8/8 modes) vs the S58 "GGE-as-hidden-variable / superdeterminism" reading** — `einstein`. A Bell-violating relic cannot be a local-hidden-variable account.
5. **α_LIV=0 "exact" vs the 229× two-speed substrate** (c_fabric vs c_Gold) — `quantum-foam`, `loop-quantum-gravity`: the linearity of ω(k) across the crossover is asserted, never computed; over-states Hossenfelder's no-go and is inconsistent with §9's "higher-order isotropy is INFO." The cheapest high-value gate.
6. **CC closure vs H₀ prediction mutually exclusive** on the tracking-vacuum freedom — `mack` (one DOF drives 3 of 5 gaps).
7. **Acoustic white hole vs φ=0 (no superflow) held PERMANENT** — `tesla`: the horizon is a moduli-time turning point, not a spatial BLV horizon; the four-speed ³He-B match (0.996) rests on spectrum shape, not the two-fluid structure S72 retracted.

---

## 4. Curated-doc / status-tag HYGIENE DRIFTS (the fix-in-session class)

The `capstone-hygiene-gate.md` exists exactly for these. Each is a prose/status cell narrating a claim above its register status; all are flagged by an agent (attribution given), and each should be checked against the live register and down-tagged by the designated writer (`feedback_fix-in-session-never-defer.md`). **These are NOT workshops** (Q2 per `Investigating-Workshops.md`) — they route to a housekeeping ledger / designated-writer patch.

1. `framework-chaotic-instantons.md §4` narrates falsified scrambling ("lossy compression → QM," λ_L~0.16) as "marginally viable," though 4 chaos functionals falsified it to λ_L=0 — un-retracted in atlas-09 (`kitaev`).
2. Capstone narrates EMERGENT-EIH-LIFT / emergent-EP as fully open, though **both PASSED at S95** (`einstein`).
3. Canonical Penrose document draws the white hole as a **sealed bracketed pair (S85 PASS)** while S95-W4-1 FAILed to single-asymmetric-open; the S106 down-tag CFs (CF-A1-1/-2) were never lifted — the diagram contradicts its own computation (`schwarzschild-penrose`).
4. **Z₃-triality "three generations" tagged PROVEN** in the MCP vs capstone frontier #7 "open" (`loop-quantum-gravity`).
5. `atlas-neutrino-collab.md` still narrates **R=27.2** against the register's **R=9.86 FAIL** (`neutrino`).
6. **Baryogenesis: EVOI "CLOSED-SOURCED-UNIQUE" vs atlas-04 C6 "CONDITIONAL"** — η_B 1.1 OOM (≈13.5×) under-produced from a posited δA; EVOI retired the row "to §5" prematurely (`dirac`). Recommend down-tag EVOI → CONDITIONAL + mint the η_B falsifier row.
7. **Falsifier-inventory inversion**: the cleanest zero-parameter neutrino prediction, **δ_CP∈{0,π}** (vs NuFIT-6.0 ~230°, already 1.5–2σ), has *no inventory row* while the conditional mass predictions do (`neutrino`); and `proven_1450` JWST-LRD seed tagged LIVE with no derived mechanism (`little-red-dots`); baryogenesis CLOSED-SOURCED-UNIQUE vs atlas-04 CONDITIONAL again (the meta-pattern CV-10).

---

## 5. Per-agent index (file → one-line headline)

| File | Headline finding |
|:-----|:-----------------|
| `connes-ncg-theorist.md` | Order-one axiom BROKEN (norm 4.0); spectral action ≠ free energy (CC 120 OOM); a₄ conformal-anomaly is the un-closed CC channel |
| `lizzi-spectral-functional-theorist.md` | the choice of spectral functional is itself an unpinned physical d.o.f.; CC as a spectral-moment weighting problem |
| `spectral-geometer.md` | worst gaps live on the dimensionful/EXTENSIVE axis; run d_s(σ) as the UV→IR transport map; R_protected has two inequivalent values (2.33×) |
| `van-den-dungen-bridge-theorist.md` | `S_cross` defined-but-never-computed; §VII.CB a₂ un-anchorable on any finite truncation; Krein/Lorentzian submersion is the rigorous transit |
| `baptista-spacetime-analyst.md` | the full 28D Milnor moduli space never entered; Yukawa hierarchy can only live in the unexplored 23D complement; off-U(2) orbit-volume measure |
| `kaluza-klein-theorist.md` | M_KK an unpinned 0.83-decade bracket; "gauge from geometry" resolved-by-demotion; Casimir tower → volume-preservation + 3rd M_KK |
| `berry-geometric-phase-theorist.md` | RAMP / number-variance never computed (integrability rests on ⟨r⟩ alone); atlas-05 W5 over-broad vs §VII.BR WZ holonomy; c₂ Yang-monopole |
| `gen-physicist.md` | M_KK hole "refracted into three walls"; n_s (not w_0) is the live falsifier; GGE cosmological-collider bispectrum |
| `volovik-superfluid-universe-theorist.md` | two unreconciled dark sectors; present-CC vs BBN = same ρ_vac~H² eqn; coupled two-fluid DE↔stiff-DM ODE |
| `landau-condensed-matter-theorist.md` | A_s + DM-mass both Landau problems with the wrong (equilibrium) functional; A_s gap quoted at 5 OOM values; NSR pseudogap two-scale |
| `transit-dynamics-theorist.md` | A_s OPEN-by-overproduction (×7.7 via a fitted greybody knob); diabatic-freeze vs LIVE §VII.BP resonance; lock relic {β_k} then Floquet |
| `quantum-acoustics-theorist.md` | TRANSIT-PS-67 (CRITICAL) never run; A_s 12-OOM spread + sign-flip; flat-band B2 = degenerate roton = 2nd DM candidate |
| `kitaev-quantum-chaos-theorist.md` | FOUNDING gap: no surviving QM-from-substrate derivation (λ_L=0, N₃=0); Type III₁ modular GGE dephasing; chaotic-instantons doc drift |
| `tesla-resonance.md` | M⁴-summand d_s flow never computed (CDT-2 lives there); white-hole vs φ=0 contradiction; Vinen-Kolmogorov cascade → TRANSIT-PS-67 |
| `paasch-mass-quantization-analyst.md` | framework re-derived Paasch's exp(−k·C₂) mass scheme uncited; S₀=φ_paasch^{fN} coincidence; W3-1 zero-compute orphan since S33 |
| `nazarewicz-nuclear-structure-theorist.md` | M_KK keystone via dimensional transmutation exp(−c/λ) from van-Hove DOS; pairing gap known only to ×2; τ_fold = collective-inertia selection |
| `schwarzschild-penrose-geometer.md` | Penrose diagram contradicts its own S95 computation; τ↔t map is the master assumption; Raychaudhuri focusing bridge; no compact-object sector |
| `loop-quantum-gravity-theorist.md` | LQC H²(ρ) is exactly the missing effective-Friedmann; Z₃ "3 generations" PROVEN vs frontier-#7-open; α_LIV=0 over-states the no-go |
| `string-theory-theorist.md` | string contact isolated to the a₂/area-law; modular flavor symmetry → Yukawa wall; Sen-tachyon K-theory → unitary info dynamics |
| `quantum-foam-theorist.md` | 229× two-speed vs α_LIV=0 (crossover never computed); d_s→1.7 misfiled = CDT signature; CC traded for a scale degeneracy (=Carlip) |
| `mack-cosmic-bridge.md` | PBH-from-fold-transit → DM abundance + compact-object sector; CC↔H₀ mutual exclusivity; cosmic birefringence β as LiteBIRD falsifier |
| `cosmic-web-theorist.md` | 325 Mpc ring rests on an unverified amplitude identity; NO void sector; Void Size Function + Betti curves are the only ΛCDM-distinguishing LSS obs |
| `little-red-dots-jwst-analyst.md` | LRD BH-seed spectrum tagged LIVE with no derived mechanism; meta: register status outruns derivation (shared with dirac) |
| `neutrino-detection-specialist.md` | headline ν falsifiers oscillation-anchored not zero-param; δ_CP∈{0,π} (cleanest zero-param) has NO inventory row; sterile-null + ΔN_eff free |
| `dirac-antimatter-theorist.md` | η_B CLOSED(EVOI) vs CONDITIONAL(atlas-04), ×13.5 short from posited δA; LHCb-2025 strong-phase CP → GGE rescattering; J-breaking classification |
| `hawking-theorist.md` | S=A/4G posited not counted (microstate gate failed as tautology); volume-preserving constraint EMPTIES the a₂ clock (explains the a(t) gap) |
| `einstein-theorist.md` | EMERGENT-EIH-LIFT/EP PASSED S95 (capstone says open); BELL-GGE-70 contradicts S58 hidden-variable; Jacobson → CC magnitude |
| `phonon-first-cosmologist.md` | a(t) sharper than register reads (H(τ) imported); Kibble-Zurek Z₃ walls → w_a + BBN; ideal-band quantum-geometry → H(τ) |
| `kaku-speculative-theorist.md` | four "dials" = ONE unbuilt moduli sector; modular flavor symmetry (independent of string-theory); RH/Berry-Tabor⟺Hilbert-Pólya ⟺ GGE integrability |
| `sagan-empiricist.md` | n_s is the strongest empirical LIABILITY (drifting 2.7–5σ wrong way); no compact-object sector = first anchor-free prediction; net P ≈ S69's 22% |

(`README.md` carries the charge + roster; `_dispatch-tracker.md` carries the dispatch audit trail.)

---

## 6. Honest framing and recommended next moves

**What got stronger, what got weaker** (`sagan`'s recomposition, corroborated across the survey): the *structural* core strengthened (10 blind cross-axis STAGE-3 promotions are genuine independent confirmation per `joint-theorem-promotion.md`); the *observational* case weakened (n_s and w_a both moving away from the committed values). The framework's center of gravity has shifted toward publishable mathematics + lab/JUNO/DUNE falsifiers and away from CMB-cosmology fit.

**The single most efficient next compute** is unambiguous across the survey: **B-1, run TRANSIT-PS-67 as a Parker-Bogoliubov |β_k|² power spectrum** — it is the gate the framework's own constraint-matrix calls CRITICAL, it has never actually been run, and 5+ agents independently judge it the lever that closes A_s + K_pivot + α_s + n_s(k) at once with existing infrastructure.

**The deepest structural realization** is `hawking`'s: a(t) has resisted derivation for ~40 sessions because **the volume-preserving constraint that buys the clean G_N is the same one that empties the a₂ conformal clock.** Until that is named and broken (B-4: import the LQC effective-Friedmann template / Raychaudhuri), the a(t) gap is structural, not incidental.

**The most beautiful "mirror darkly" springboard** is the independent CV-8 convergence: two unrelated domains (string theory, cross-paradigm) reaching **modular flavor symmetry (Dedekind-η)** as the one object that closes both the Yukawa hierarchy and the τ↔K e-fold map — and it is *already latent* in the framework's threshold corrections.

**Routing of these outputs** (not done here; the user decides):
- §3 contradictions → `/rclab-investigate` workshop seeds (Q1 adjudications).
- §2 bridges → `/rclab-plan` carry-forward computations (4-field specs), EVOI-ordered (B-1 first).
- §4 hygiene drifts → designated-writer patches / housekeeping ledger (fix-in-session; not workshops).
- This investigation track is exploratory (`gate-verdicts.md §"Investigation-Track"`): results enter the permanent index only when promoted into a `session-{N}` gate.
