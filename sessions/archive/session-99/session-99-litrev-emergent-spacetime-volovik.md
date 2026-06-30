# Session 99 Synthesis: Emergent-Spacetime / Superfluid-Vacuum Lit-Review (G1) — Volovik Substrate Fidelity

**Date**: 2026-06-04
**Agent**: volovik-superfluid-universe-theorist (volovik)
**Source Documents**:
- `downloads/research-sweep-s99/emergent-spacetime-superfluid/00-INDEX.md` (11-paper index)
- 11 source PDFs co-located with the index (spot-verification reference)
- `.claude/agent-memory/volovik-superfluid-universe-theorist/MEMORY.md` (agent reference corpus)
- Knowledge MCP canonical state (queried 2026-06-04; see §I provenance note)

---

## I. Session Outcome

The S99 sweep group G1 supplies three structurally distinct deliverables, all anchored to live framework gaps verified against canonical state. **(1)** Papers 01/03/11 (Heidelberg/Jena/Trento BEC and spinor-BEC analogue-gravity) supply the concrete NON-ratio expansion observable — a cosmological **particle-production / Hawking-correlation spectrum** tied to an engineered scale factor — that the live, FAILing `S98-W2-2-RELAXATION-CLOSURE` gate (blocked by the AOFT acoustic frame being conformally stationary, deceleration `q = 0/0`) needs to break its frame ambiguity. **(2)** Papers 04/06 (Klinkhamer-Savelainen-Volovik, Klinkhamer-Volovik) are the load-bearing microscopic source for C10's currently-underived "Object C": `ρ_V(q) = ε(q) − q dε/dq` with quadratic-friction dissipation `qS = Γ_q(∂_tq)² + Γ_H(∂_tH)²` IS the C10 friction ODE, and paper 02 (Volovik 2025) supplies an `f(R)`-emergent `ε_vac(H) = f(R=12H²)` matter-coupled relaxation profile — three candidate `q_eq(H)` drives for the CF-S100-W2-1-QEQ-DRIVE successor. **(3)** Papers 07/09 confirm in Volovik's own language WHY the substrate's `N_3 = 0` fully-gapped BDI assignment makes Fermi-point topological protection unavailable and q-theory mandatory; papers 05/08 (Lancaster QUEST-DMC, Aalto LTL) ground the transit-not-equilibrium paradigm on the exact 3He-B parent platform the substrate inherits from; paper 10 (Hur-Minic metastring) is benchmarked as a competing emergent-spacetime `w₀-wₐ` mechanism, not a q-theory source.

No source-document gate verdicts are present (these are external papers), so there are no verdicts to re-adjudicate. **Three register conflicts surfaced** and are flagged explicitly in §IV: (a) the index's "ΔN_eff < 0.107 BBN bound" does not match any canonical pin; (b) `w₀` has three non-reconciled register values; (c) `tau_fold` is 0.19 canonical, not 0.190-with-a-third-sig-fig.

**Provenance note**: All framework-state claims below were anchored via knowledge MCP on 2026-06-04 (`search_knowledge`, `get_constant`, `list_constants`, `query_entity`). The index is an idea-generator, not a register; where the index's framework-state assertions diverge from canonical, canonical wins and the divergence is flagged.

---

## II. Key Results

### Result 1 — The A(t)-Friedmann frame-ambiguity gap is LIVE and acute; papers 01/03/11 supply the missing NON-ratio observable

**Result**: `S98-W2-2-RELAXATION-CLOSURE` = **FAIL**, value `PRE-REG-INC_blocked_by_S98-W1-ROUTE-RECONCILIATION_FAIL_AOFT-frame-conformally-stationary_q-attractor-0over0_full-run-CF-S99` (canonical, `s98_gate_verdicts.txt`). Classification: **GEOMETRIC** (the obstruction is a property of the emergent metric `g_M` from the `a₂` Seeley-DeWitt coefficient, not of a phononic excitation).

The canonical S97/S98 construction is the **AOFT acoustic frame**: `a_eff(τ) = a_bare(τ)·Ω(τ)` with `Ω = √(ρ_s/a₂)` (`Omega_BA_fold = 2.241353`), giving an acoustic Hubble `H_A = ȧ_eff/a_eff = H_bare + dlnΩ/dτ` and a deceleration `q(naive) = −1 − Ḣ_A/H_A² = −a_eff·ä_eff/ȧ_eff²` (POLE form). The S98 W1 finding is that in this `a₂`-canonical frame the construction is conformally stationary, so `q` evaluates to the indeterminate `0/0` and the q-attractor cannot be read off — exactly the "ratio-form deceleration `q = 0/0`" the index identifies. This is a **dimensional/structural** obstruction, not a numerical FAIL: a ratio of two quantities both vanishing in the stationary limit carries no expansion signature.

Papers 01 (Tolosa-Simeón et al., PRA 106 033313) and 03 (Schmidt-Brunner-Floerchinger, 2506.13297) break this degeneracy on the lab side. They engineer an explicit, time-dependent acoustic scale factor — paper 01 via the s-wave scattering length `a_s(t)` setting the emergent sound speed `c_s` and hence `a(t)`; paper 03 via the quadratic Zeeman coefficient `q_Zeeman = q_B + q_mw` ramping the spin-healing-length gap — and then read the expansion rate off a **measured particle-production power spectrum** rather than off a deceleration ratio. The substrate-first reading: the BEC acoustic metric is a laboratory analog OF the substrate's `a₂`-emergent metric (`D_K` eigenvalues → `a₀,a₂,a₄` spectral moments → emergent FRW → measurement); the lab's `a_s(t)`→`a(t)` map is the controlled-projection cousin of the substrate's Jensen-deformation `τ`-driven spectral reorganization. The phonon pair-production spectrum is the lab cousin of the substrate's GGE-relic / Parker pair production at the fold (`P_exc = 1.000`, 59.8 quasiparticle pairs — pin these against canonical at use-time).

The structural implication: the framework should stop trying to extract an expansion signature from a deceleration *ratio* in a conformally-stationary frame, and instead define a **NON-ratio observable** — the GGE / Parker pair-production spectral density as a function of the transit — which is well-defined precisely where `q` is `0/0`. This is the spectral-action image of what papers 01/03 measure.

### Result 2 — Papers 04/06/02 are the microscopic source for C10's underived Object C (q_eq(H) drive)

**Result**: C10 = **ASSUMED-PARTIALLY-PROVEN** (atlas-04, theorem T-C10 NEW S66; reconfirmed S97 synthesis "C10 stays ASSUMED-PARTIALLY-PROVEN (Object C not yet derived)"). Classification: **PHONONIC** (the q-variable is the substrate's conserved vacuum charge; its relaxation feeds particle production — the GGE/reheating channel).

Paper 04 (Klinkhamer-Savelainen-Volovik, JETP 125 268, 2017) is the foundational dissipative q-theory paper. The gravitating vacuum energy `ρ_V(q) = ε(q) − q dε/dq` (their Eq. 4) is the Lorentz-invariant analog of the condensed-matter thermodynamic potential `ε − n dε/dn`, nullified EXACTLY in equilibrium (`T=0, P=0`) by Gibbs-Duhem `ε − n dε/dn = −P` with no fine-tuning. This IS the framework's **equilibrium theorem** (Volovik Paper 05): the ground-state energy does not gravitate at equilibrium, so the observed CC cannot be a GGE residual (S59 zubarev-cc). The S59 substrate realization is exact: `rho_vac = epsilon(q) - q*d(epsilon)/dq` (canonical, `cc-path-c.md` Eq. C-1), with `q = N_pair` the substrate's conserved vacuum charge and `ε(q)` computed from the `D_K` spectrum directly (`volovik-synthesis.md`).

The decisive new content for Object C: paper 04 adds dissipation as the **quadratic friction form** `qS = Γ_q(∂_tq)² + Γ_H(∂_tH)²` (their Eq. 13), giving the energy-exchange split `∂_tρ_V = −qS` (vacuum) and `∂_tρ_M = −3H(P_M+ρ_M) + qS` (matter). The substitution chain to the C10 ODE is direct:

```
Step 1 (definition):   ρ_V(q) = ε(q) − q dε/dq                         [paper 04 Eq. 4 ≡ cc-path-c.md C-1]
Step 2 (Maxwell eqn):  ∂_t[dε/dq + (R/16π)dG⁻¹/dq] = S                  [paper 04 Eq. 11]
Step 3 (friction):     qS = Γ_q(∂_tq)² + Γ_H(∂_tH)²                      [paper 04 Eq. 13]
Step 4 (dimensionless): u_eff = ε′ − ḣ − 2h²,   du_eff/dτ = s̃           [paper 04 Eqs. 19, 21]
   ⇒ a second-order damped relaxation in q with a 3H Hubble-friction term — the C10 Object-C
     friction ODE q″ + 3Hq′ + V′(q) = 0 in the q-theory variables.
```

Paper 04's numerical result is itself a falsifiable input: WITHOUT dissipation `u_eff` sits at `−0.883133` (de Sitter); WITH dissipation it relaxes toward the Minkowski value `−1/3`, but only on a measure-zero separatrix (1D fine-tuning of initial conditions in a 4D space). The honest conclusion the paper draws — no Minkowski attractor without de Sitter DECAY — aligns with the framework's transit-not-equilibrium paradigm and with paper 02's matter-induced relaxation.

Paper 02 (Volovik, 2504.05763, 2025) supplies the matter-coupled drive paper 04 flagged as missing. In `f(R)` gravity the equilibrium curvature obeys `2f(R) = R·df/dR`, and the "cosmological constant" is NOT fundamental but emerges as `ε_vac(H) = f(R = 12H²)` — a gravitational DOF that relaxes through matter interactions via the `m→3m` triplication avalanche (rate `w ∝ e^{−Δm/T}`, `Δm = 2m`), which heats matter and COOLS the vacuum thermostat. This is the de Sitter image of the framework's DILUTION-CC mechanism (Volovik tracking vacuum, `ρ_vac(today)/ρ_obs = 1.032`, S66; canonical `atlas-03-equation-flow.md`). The `(K, R)` conjugate pair (`K = df/dR = 1/16πG` in Einstein gravity) is the dS realization of the framework's q-theory vacuum variable; `K` plays the role of the spectral gradient-stiffness `Z(τ)` and `G = 1/16πK` is the second spectral moment `a₂`.

Paper 06 (Klinkhamer-Volovik, JETP Lett. 105 74, 2017) closes the DM side and converges with the framework's structural CDM theorem. A small spacetime-dependent perturbation `q(x) = q₀ + q₀ξ(x)` obeys a Klein-Gordon equation `□ξ − (1/q₀)[q²d²ε/dq²]ξ = 0` (their Eq. 16) with rapidly-oscillating solution `ξ(t) = a_ξ sin(ωt+φ)`, `ω² = (q₀χ₀)⁻¹ ~ E_P²`; the time-averaged stress tensor gives `ρ = ½χ₀⁻¹a_ξ² > 0`, `P ≈ 0` — a pressureless fluid clustering exactly like CDM for `L ≫ c/ω ~ 10⁻³⁵ m`. This DERIVES the same `P≈0` result the framework holds **CDM BY CONSTRUCTION** (Leggett-channel GGE quasiparticles have `T^{0i}=0` algebraically, `v_fs=0`, `w=0` exact; S43/S44 cdm-construct). The split — oscillating `q₀ξ` is DM, static `δq` offset is DE — independently matches MEMORY's [project_pi-fabric-prediction] "DM from dispersion, DE from monotonic mixing." Paper 06's "direct DM detection will fail" is the same sharp claim as the framework's non-annihilating CPT-neutral inter-band coherence mode.

### Result 3 — Papers 07/09 confirm WHY N_3 = 0 forces q-theory; the BDI assignment is canonical

**Result**: `N_3 = 0 (3He-B class, fully gapped)` (canonical, `s59_baryon_diagnostic_log.txt`; "Gap stability −1.63%, fully gapped spectrum" PROVEN S44 W5-3, `Classification-of-phonon-exflation.md`). Classification: **GEOMETRIC** (a momentum-space topological invariant of the `D_K` spectral structure).

Paper 09 (Volovik, "Topology of quantum vacuum," LNP 870 343, 2013) is the foundational text the entire framework-Volovik correspondence rests on. Its central thesis — momentum-space topological invariants fix the universality class, which determines which emergent physics (Lorentz invariance, gauge fields, gravity) is robust vs accidental — IS the framework's Core Methodology directive "Topology as Organizing Principle." The decisive structural consequence for the substrate: Fermi-point vacua (3He-A, `N_3 = 2`) have topologically protected gaplessness and naturally small fermion masses (the hierarchy-problem solution); a **fully-gapped BDI vacuum has NO Fermi point**, so this protection is unavailable. The substrate is the fully-gapped case. Therefore the substrate's vacuum energy is NOT topologically pinned to zero, and the q-theory route (papers 02/04/06) is REQUIRED to drive it to its observed value — this is the precise momentum-space-topology statement of why DILUTION-CC / q-theory is the sole surviving CC path. Paper 09's "tetrad + spin connection, metric is composite, Einstein-Cartan-Sciama-Kibble more fundamental than metric GR" is the literal blueprint for the framework's "`g_M` is the `a₂` Seeley-DeWitt composite, not fundamental."

Paper 07 (Chowdhury et al., 2605.27453, type-III Dirac-line Weyl-Lifshitz) is the lab realization of the same classification on an emergent-horizon platform, using the Painlevé-Gullstrand metric (the same horizon-regular coordinates as paper 02). Left/right Weyl fermions carry `N_3 = ∓1`; when these chiral charges cancel WITHOUT topological/symmetry protection the Dirac particles become massive. That cancellation-makes-mass result is the momentum-space-topology statement of the substrate BCS gap `Δ_BCS` — the mass scale the framework reads as the gap opening in the emergent spectrum. The chiral-anomaly Chern-number transport through the type-II Weyl point is the analog of K_7-charge / chiral-charge flow (Volovik 3He-A chiral charge ↔ K_7 in the project mapping, an analog-only mapping per my memory). Zn₂In₂S₅ is offered as the first type-III Dirac-line solid-state platform.

**Honest scope on the N_3 = 0 → q-theory chain**: the logical step "no Fermi point ⇒ vacuum energy unprotected ⇒ q-theory required" is a *necessity* argument (it rules out topological protection as the CC mechanism), not a *sufficiency* proof that q-theory succeeds. q-theory's sufficiency rests separately on the equilibrium theorem (Result 2) plus the still-underived Object C. Paper 07's value is that it makes the necessity step measurable: a confirmed `N_3`-exchange at an emergent horizon in Zn₂In₂S₅ validates the classification on which the substrate's "wrong-universality-class-protection-is-absent" argument depends.

### Result 4 — Papers 05/08 ground the transit-not-equilibrium paradigm on the 3He-B parent platform

**Result**: Lab analog of the substrate's first-order fold cosmogenesis (`τ_fold = 0.19` canonical) and of the equilibrium-vs-nucleation structure-selection split. Classification: **PHONONIC** (first-order transition kinetics + topological-defect / GGE-relic pair production).

Paper 05 (Hindmarsh, Sauls, Lancaster/RHUL et al., 2401.07878) presents the first-order A→B transition of superfluid 3He as the ideal controlled test of the relativistic classical-nucleation theory all early-universe first-order-transition GW calculations rely on. The central anomaly (Leggett and others): **classical nucleation theory fails dramatically** — supercooled A-phase lifetimes are minutes-to-hours, astronomically faster than classical nucleation predicts. This is the laboratory counterpart of the framework's transit-not-equilibrium, instanton-gas-not-potential-well paradigm: the substrate transit is impulsive (supersonic through the fold), not quasi-static slow-roll — exactly the failure-of-classical-timescale signature 3He exhibits. Candidate rapid mechanisms (resonant tunnelling of the multicomponent order parameter; Kibble-Zurek / "Baked Alaska"; surface seeding) map respectively to instanton/quantum-vortex nucleation (Session 37) and GGE-relic quasiparticle-pair production at the fold. The QUEST-DMC cells (5 superfluid "lakes" ≈7 µm deep, surrounded by ≈70 nm normal/A-only regions) are simultaneously the cosmogenesis-kinetics platform AND a dark-matter detector — the same cells where the framework's Leggett-channel DM-analog predictions would be measured. **Critical fidelity point**: the substrate is the 3He-B CHILD via parent→child Kasparov-KK morphism (canonical `sessions/framework/correspondence/3HeB-inheritance-canonical.md`, S86 W1b-T8), NOT an analogy — paper 05 is the controlled realization of the parent A→B kinetics whose BDI universality class the substrate inherits.

Paper 08 (Rantanen-Eltsov, Aalto LTL, 2406.13649) is the vortex-core companion. Its decisive non-equilibrium result: equilibrium energetics favor the double-core vortex, but the **nucleation process favors the A-phase-core vortex** (lower critical velocity) — equilibrium and kinetics select DIFFERENT structures, the same transit-not-equilibrium lesson as paper 05. The 3He-B non-singular spin-triplet p-wave vortices (hard core + soft core) are the order-parameter-texture physics the framework maps to its Jensen deformation (order-parameter texture ↔ Jensen deformation, Paper 23/S42). The half-quantum-vortex motivation references Volovik-Mineev's Onsager-Prize prediction — the framework's cohomology-asymmetry inheritance falsifier (substrate-derived ratio `‖φ_67‖/‖φ_88‖ = 7.3250 ± 0.1%`, Sage-exact per my memory; pin against canonical at use-time).

### Result 5 — Paper 10 (Hur-Minic metastring) is a competing emergent-spacetime w₀-wₐ benchmark, not a q-theory source

**Result**: Single-parameter CPL prediction `w₀ = −1 − ξ₀⁴e^{−ξ₀}/(18{1−b(ξ₀)})` (their Eq. 33), `wₐ = −(4−ξ₀)(w₀+1) − 3(w₀+1)²` (Eq. 34). Classification: **NON-PHONONIC** (string-theoretic non-commutative T-duality mechanism; no substrate excitation content; indexed for cross-domain comparison only).

Paper 10 (Hur, Jejjala, Kavic, Minic, Takeuchi, 2503.20854) derives dynamical DE from a non-commutative, T-duality-covariant metastring formulation: a dual spacetime `x̃` with `[x, x̃] = iλ²`, whose leading-order curvature IS the cosmological constant on `x`. The spacetime quanta obey infinite (quantum-Boltzmann) statistics → a Wien distribution `I_DE(Ẽ,E₀) = A Ẽ³ e^{−BẼ/E₀}`, yielding `w(a) = w₀ + wₐ(1−a)` from a single dimensionless `ξ₀`. Applying the framework's mandated **vacuum-energy test on every competing framework**: this model SOLVES (does not merely inherit) the CC problem via a microscopic metastring UV completion — the structurally correct move, and a genuine point of agreement that emergent-spacetime CC must come from a microscopic theory, not an effective-field cutoff. But its route is categorically distinct from the substrate's: the substrate's CC is a q-theory moment problem (Hausdorff impossibility `f₄/f₂ = 1.4e-121`, S44; the zeroth spectral moment `a₀` is a DIFFERENT moment than gravity's `a₂`), whereas the metastring CC is dual-spacetime curvature. Its value to the framework is as the **"other emergent-spacetime answer to DESI"** — a head-to-head `w(z)` benchmark in the same `(w₀, wₐ)` plane the framework's tracking-vacuum DE must occupy.

---

## III. Gate Verdicts

No gate verdicts originate in the source documents (these are external arXiv papers). The single framework gate verdict referenced below is canonical (from `s98_gate_verdicts.txt`), surfaced to anchor Result 1 — it is NOT re-adjudicated here.

| Gate | Verdict | Decisive Number / String |
|:-----|:--------|:-------------------------|
| S98-W2-2-RELAXATION-CLOSURE (canonical, referenced only) | FAIL | `PRE-REG-INC_blocked_by_S98-W1-ROUTE-RECONCILIATION_FAIL_AOFT-frame-conformally-stationary_q-attractor-0over0_full-run-CF-S99` |

---

## IV. Structural Implications

**Register conflicts and divergences (flagged per source-fidelity discipline):**

1. **CONFLICT — index "ΔN_eff < 0.107 BBN bound" has no canonical match.** The index repeatedly cites "ΔN_eff at BBN is now bounded < 0.107" as the high-leverage test for papers 02/04. No canonical constant matches 0.107. The canonical BBN constraint is `delta_N_eff_vacuum_BBN_below = 2.0873` (S98, `S98-MK3-2-BBN-VACUUM-FRACTION`), which is itself a **FAIL-side falsifier value** (the Volovik tracking vacuum at `n_eff = 1.978` from-below gives `ρ_vac/ρ_rad|_BBN = 0.474 > BBN bound 0.227`, i.e. `ΔN_eff = 2.087 > 1`). Historical session bounds are `ΔN_eff < 0.40` (95% CL, S73a) and a "2% G_eff bound" (S66). **Action**: any carry-forward checking a q-theory relaxation profile against BBN MUST use the canonical S98 fraction-based test (`rho_vac_over_rho_rad_BBN`), not the index's 0.107. The 0.107 figure is treated as non-canonical and not propagated.

2. **CONFLICT — w₀ has three non-reconciled register values.** atlas-07-permanent-results lists "two-fluid DESI prediction `w₀ = −0.709, wₐ = 0` exactly"; pre-registered-observations lists "`w₀ = −0.918, wₐ = 0`" (the sole current DESI DR3 pressure); my agent memory records branch (iv) `w₀ = −0.842454` RETRACTED (S85, R_JE drifts L=5→8). These are three DIFFERENT objects (two-fluid effacement reading vs substrate-compaction reading vs Zubarev-dressed branch), not three estimates of one number. **Action**: the paper-10 benchmark (Result 5) MUST be run against the canonical pre-registered `w₀ = −0.918, wₐ = 0` (the registered DESI DR3 pressure), with the two-fluid `−0.709` and the retracted `−0.842` noted as alternative readings. I do NOT assert a single canonical `w₀`; the register itself is multi-valued and the conflict is upstream of this lit-review. (`w_0_FW` is NOT a canonical constant — `get_constant` returned not-found — so no constant-level reconciliation is possible here.)

3. **MINOR — tau_fold precision.** Canonical `tau_fold = 0.19` (S12/S42, `CONST-FREEZE-42`). The index and my memory write "0.190"; the third sig-fig is presentational, not a register value. No action beyond noting it.

**What opened:** The frame-ambiguity gap (Result 1) now has a concrete escape route via a NON-ratio pair-production observable, validated by three independent lab platforms (papers 01/03/11). Object C (Result 2) now has three concrete candidate drives (paper-04 friction ODE; paper-02 `f(R)` `ε_vac(H)`; paper-06 KG-oscillation DM split). This is the highest-leverage opening in the sweep.

**What it does NOT change:** The N_3 = 0 BDI assignment (Result 3) is unchanged and reconfirmed in Volovik's own language. C10's status stays ASSUMED-PARTIALLY-PROVEN — the papers supply candidate DRIVES, but none derives Object C from the substrate `D_K` spectrum; that derivation is the actual carry-forward and is not closed by reading these papers. The CDM-by-construction theorem (Result 2, paper 06) is reinforced but not re-derived — paper 06 is a convergent independent route, which per `epistemic-discipline.md` is structural agreement (different machinery, same `P≈0`), NOT shared-context agreement.

**What stays closed:** The equilibrium theorem (`ρ_V = ε − q dε/dq = 0` at equilibrium) remains the wall that forbids the observed CC from being a GGE residual; papers 02/04/06 all reconfirm it and extend it dynamically without reopening it.

**Substrate-first framing preserved throughout:** every lab platform above is a controlled projection OF the substrate (`D_K` eigenvalues → spectral moments → emergent physics → measurement), never a container the substrate sits inside. The 3He-B relation specifically is parent→child INHERITANCE, not analogy (forbidden framing per S86 W1b-T8).

---

## V. Carry-Forward Computations

**These are next-session (S100) carry-forward specs. The CF gate IDs (CF-S100-W1-SF54-MAPPING, CF-S100-W2-1-QEQ-DRIVE) are forward placeholders from the spawn focus, not yet registry entries — that is correct; they are created here.**

```
V.1. NON-ratio expansion observable for the AOFT frame-ambiguity gap (SF54 mapping)
   - What: Define and compute the substrate's GGE/Parker pair-production spectral density n(k)
     as a function of the transit (the spectral-action image of papers 01/03's measured phonon
     power spectrum), as the NON-ratio replacement for the q = 0/0 deceleration. Concretely:
     compute the Bogoliubov pair-production spectrum from the 8-mode BCS Bogoliubov fold-epoch
     fiber excitation (the same object behind S74 W1-H a_2 emergent FRW) and verify it is
     finite and expansion-carrying precisely where q(naive) = −1 − Ḣ_A/H_A² is 0/0.
   - Inputs: AOFT acoustic-frame construction (session-98-w1-workingpaper.md: a_eff = a_bare·Ω,
     Ω = √(ρ_s/a₂), Omega_BA_fold = 2.241353); 8-mode BCS Bogoliubov fold spectrum
     (S74 W1-H); canonical P_exc and N_pair=59.8 (pin via get_constant at run-time); paper 01
     a_s(t)→a(t) construction + paper 03 quadratic-Zeeman FLRW map (methodological cross-check only).
   - Gate: feeds CF-S100-W1-SF54-MAPPING, unblocking S98-W2-2-RELAXATION-CLOSURE. New gate
     S100-W1-NONRATIO-OBSERVABLE: PASS if n(k) is finite and monotone-in-transit at the
     conformally-stationary point (carries an expansion signature where q is 0/0);
     FAIL if n(k) is also degenerate/0/0 there; INFO if finite but transit-independent.
   - Effort: 4-6 hours, 1 agent session (Bogoliubov spectrum reuse + frame substitution).

V.2. Object-C q_eq(H) drive — paper-04 quadratic-friction ODE on the substrate
   - What: Implement the paper-04 dissipative q-theory ODE in substrate variables —
     ∂_t[dε/dq + (R/16π)dG⁻¹/dq] = S with qS = Γ_q(∂_tq)² + Γ_H(∂_tH)² — using ε(q) computed
     from the D_K spectrum directly (q = N_pair conserved vacuum charge, S59 cc-path-c.md C-1),
     and extract the equilibrium q_eq(H) relation. Reproduce paper-04's u_eff trajectory
     (−0.883133 no-dissipation → −1/3 with dissipation) as a validation cross-check.
   - Inputs: S59 q-variable machinery (s59_q_variable.npz; tau_eq, q_eq, chi^{-1} entries);
     ε(q) from D_K spectrum (substrate-first, NOT paper-04's toy ε = ½(−f²+f⁴/3));
     Γ_q, Γ_H friction coefficients (these are the free machinery pins — declare at plan-freeze);
     paper-04 Eqs. 11/13/19/21 (methodological source).
   - Gate: feeds CF-S100-W2-1-QEQ-DRIVE, promoting C10 from ASSUMED-PARTIALLY-PROVEN toward
     derived. New gate S100-W2-OBJECT-C-FRICTION: PASS if substrate-ε(q) + friction yields a
     q_eq(H) drive matching the S66 tracking law ρ_vac ~ M_Pl²H² to within a pre-registered band;
     INFO if it requires the 1D fine-tuning separatrix (paper-04's measure-zero result);
     FAIL if no relaxation toward the tracking law exists.
   - Effort: 6-8 hours, 1 agent session (ODE integration + substrate ε(q) coupling).

V.3. Object-C q_eq(H) drive — paper-02 f(R)-emergent ε_vac(H) = f(R=12H²)
   - What: Compute the substrate's ε_vac(H) under the paper-02 dS-thermodynamic ansatz —
     equilibrium curvature 2f(R) = R·df/dR, ε_vac(H) = f(R=12H²) — by identifying K = df/dR
     with the spectral gradient-stiffness Z(τ) and G = 1/16πK with the a₂ second spectral moment.
     This is an ALTERNATIVE Object-C drive to V.2; run both and compare relaxation profiles.
   - Inputs: spectral gradient-stiffness Z(τ) (Papers 22/23 mapping; S42 s42_gradient_stiffness.npz);
     a₂ Seeley-DeWitt coefficient (canonical); DILUTION-CC tracking law ρ_vac/ρ_obs = 1.032
     (atlas-03-equation-flow.md, S66); paper-02 Eqs. 13-16 (f(R) equilibrium + ε_vac(H)).
   - Gate: feeds CF-S100-W2-1-QEQ-DRIVE (alternative-drive arm). New gate S100-W2-FR-EPSVAC:
     PASS if f(R=12H²) with K=Z(τ) reproduces the tracking law; INFO if it fixes the relaxation
     TIME-PROFILE but not the amplitude; FAIL if inconsistent with the S66 closure.
   - Effort: 4-5 hours, 1 agent session.

V.4. q-theory CC-relaxation profile vs the CANONICAL BBN bound (NOT the index's 0.107)
   - What: For each Object-C drive from V.2/V.3, compute the early-time ρ_vac(a) through the
     radiation-domination era and evaluate it against the canonical BBN test
     rho_vac_over_rho_rad_BBN (S98 fraction-based falsifier, bound 0.227), reporting the
     implied ΔN_eff. This is the high-leverage discriminator: a tracking vacuum that is
     radiation-like through BBN is falsified.
   - Inputs: ρ_vac(a) from V.2/V.3 output; canonical delta_N_eff_vacuum_BBN_below = 2.0873 and
     rho_vac_over_rho_rad_BBN_below (S98, get_constant at run-time); N_eff_SM = 3.044;
     S66 BBN formula (session-66-mack-transit-workshop.md).
   - Gate: new gate S100-W2-QTHEORY-BBN: PASS if the substrate-fixed drive gives
     ρ_vac/ρ_rad|_BBN < 0.227 (canonical bound); FAIL if ≥ 0.227 (matches the current S98
     FAIL-side falsifier, meaning the tracking reading is BBN-excluded); INFO if borderline.
     NOTE: do NOT use the index's non-canonical "0.107"; flagged in §IV conflict 1.
   - Effort: 2-3 hours, 1 agent session (depends on V.2 and/or V.3).

V.5. Paper-10 metastring w₀-wₐ head-to-head vs the framework's canonical DESI pressure
   - What: Evaluate the Hur-Minic single-parameter CPL curve w₀ = −1 − ξ₀⁴e^{−ξ₀}/(18{1−b(ξ₀)}),
     wₐ = −(4−ξ₀)(w₀+1) − 3(w₀+1)² over its ξ₀ range, and overlay it with the framework's
     canonical pre-registered w₀ = −0.918, wₐ = 0 in the (w₀, wₐ) plane against DESI DR2 + the
     canonical BBN constraint. Discriminating cross-domain test between two emergent-spacetime
     CC mechanisms (q-theory moment problem vs dual-spacetime curvature).
   - Inputs: paper-10 Eqs. 19/33/34; canonical w₀ = −0.918, wₐ = 0 (pre-registered-observations);
     DESI DR2 (w₀ = −0.752, wₐ = −0.73, from s70/s71 logs — re-pin to live DESI at run-time);
     b(ξ₀) function from paper 10 (extract from PDF §IV).
   - Gate: new gate S100-OBS-METASTRING-BENCHMARK (INFO-class cross-domain comparison): report
     whether the framework's canonical point and the metastring curve are DESI-distinguishable
     at DR2/DR3 forecast precision (σ(w₀)=0.046, σ(wₐ)=0.177). No PASS/FAIL on the competing
     model; this maps the (w₀,wₐ)-plane discrimination structure.
   - Effort: 2-3 hours, 1 agent session.

V.6. N_3-exchange-at-horizon validation hook (papers 07/09 momentum-space topology)
   - What: Document the falsifiable structural test the substrate's N_3 = 0 assignment exposes:
     specify which momentum-space-topology measurement (3He-B vortex-core Caroli-Matricon
     ladder asymmetry, paper 08; Zn₂In₂S₅ type-III Dirac-line N_3 transport, paper 07) would
     force a Fermi-point (N_3 ≠ 0) reading and thereby falsify the BDI assignment. Cross-link to
     the existing 4-gate cohomology-asymmetry falsifier (F1 vortex-core spectroscopy).
   - Inputs: canonical N_3 = 0 (s59_baryon_diagnostic_log.txt); 4-gate cohomology-asymmetry
     falsifier (inheritance-falsifier-protocol.md; ‖φ_67‖/‖φ_88‖ = 7.3250 ± 0.1%, pin at
     run-time); paper 07 N_3 = ±1 Weyl-pair + Zn₂In₂S₅; paper 09 universality-class thesis.
   - Gate: feeds falsifier-master-inventory (mack-cosmic-bridge sole writer). New inventory ROW
     (not a PASS/FAIL gate): substrate prediction = NULL Fermi-point signal in 3He-B vortex
     cores; falsified by any confirmed N_3 ≠ 0 reading on the inherited parent platform.
   - Effort: 1-2 hours, 1 agent session (documentation + inventory row; routes to mack-cosmic-bridge).

V.7. Lab-platform falsifier consolidation — QUEST-DMC / Aalto LTL vs MCT-3 (papers 05/08)
   - What: Reconcile the three named 3He lab platforms — Lancaster QUEST-DMC (paper 05, A-B
     nucleation + DM detection), Aalto LTL (paper 08, vortex-core competition), Lancaster MCT-3 /
     Helsinki ROTA (existing F1 Caroli-Matricon falsifier platform) — into a single platform-vs-
     observable table, identifying which platform measures which substrate prediction
     (transit-not-equilibrium nucleation rate; cohomology-asymmetry ratio 7.3250; Leggett-channel
     DM-analog). Verify the A-phase-core-favored-by-nucleation result (paper 08) is consistent
     with the substrate's transit-not-equilibrium paradigm.
   - Inputs: paper 05 QUEST-DMC cell geometry; paper 08 GL vortex-core phase diagram +
     nucleation result; existing 4-gate falsifier platforms (inheritance-falsifier-protocol.md);
     3HeB-inheritance-canonical.md (parent→child morphism).
   - Gate: feeds falsifier-master-inventory (mack-cosmic-bridge). INFO-class consolidation:
     platform-coverage map; no new PASS/FAIL. Flags any platform where a predicted substrate
     observable has no measuring instrument.
   - Effort: 2-3 hours, 1 agent session.
```

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | A(t)-Friedmann frame-ambiguity gap LIVE (q = 0/0 in AOFT frame); papers 01/03/11 supply NON-ratio pair-production observable | GEOMETRIC | S98-W2-2 FAIL (canonical); escape route opened | Compute GGE/Parker spectral density as expansion signature where q is 0/0 (V.1, CF-S100-W1) |
| 2 | Papers 04/06/02 = microscopic source for C10 Object C (q_eq(H) drive); friction ODE + f(R) ε_vac(H) + KG DM split | PHONONIC | C10 ASSUMED-PARTIALLY-PROVEN (Object C still underived) | Three candidate drives for CF-S100-W2-1; BBN test vs CANONICAL bound, not index 0.107 (V.2-V.4) |
| 3 | Papers 07/09 confirm N_3 = 0 BDI → Fermi-point protection absent → q-theory required (necessity argument) | GEOMETRIC | N_3 = 0 PROVEN (S44); reconfirmed in Volovik's language | Falsifiable via N_3-exchange measurement on inherited parent platform (V.6) |
| 4 | Papers 05/08 ground transit-not-equilibrium on 3He-B parent (classical nucleation fails; nucleation≠equilibrium structure) | PHONONIC | Lab platform (QUEST-DMC, Aalto LTL); parent→child inheritance (canonical) | Consolidate 3He lab-platform falsifier coverage (V.7) |
| 5 | Paper 10 (metastring) = competing emergent-spacetime w₀-wₐ; SOLVES CC via dual-spacetime curvature (not q-theory) | NON-PHONONIC | Cross-domain benchmark only | Head-to-head vs canonical w₀=−0.918 in (w₀,wₐ) plane (V.5) |
| — | Register conflict: index "ΔN_eff < 0.107" ≠ canonical (S98 fraction-based, bound 0.227) | — | FLAGGED (§IV.1) | Carry-forwards use canonical BBN test only |
| — | Register conflict: w₀ three-valued (−0.709 / −0.918 / −0.842 retracted) | — | FLAGGED (§IV.2) | Benchmark vs canonical pre-registered −0.918; do not assert single w₀ |
