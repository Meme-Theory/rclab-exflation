# Investigation-1 — Landau (Condensed-Matter / Many-Body) Vantage

**Agent**: landau-condensed-matter-theorist
**Vantage**: symmetry-first phase-transition physics — order parameters, the most general free-energy functional consistent with the symmetry, quasiparticle (Landau) description of strongly-interacting systems, superfluidity, BCS/Ginzburg-Landau, non-equilibrium pair production through a transition.
**What I actually read**: atlas-00, -04 (assumptions), -08 (open questions, in full incl. S52-S107 freshness), the open-channel-ledger §A-§F (S105-current frontier), my own agent memory (framework-constants, s64 A_s budget, s66 Lizzi-Landau, s84 symmetry-class). I queried the knowledge MCP before every claim below: `search_knowledge` / `trace_entity` / `get_constant` on A_s overproduction, Leggett mass anchor, BCS 3D-Ising class, Higgs quartic, σ_8, flat-band/Peotta-Törmä, pseudogap/BCS-BEC crossover, Kibble-Zurek.

**Framing discipline**: I obey `phononic-framing.md`. The substrate IS the system; the explanation runs D_K spectrum → spectral moments → emergent fields → observation. Where a result is GEOMETRIC / PARTICLE / NON-PHONONIC I say so. I do not invert into container thinking.

**One sentence up front**: The framework's internal geometry is a genuine, proven Landau problem solved correctly — but its two largest live gaps (the A_s amplitude floor and the dark-matter mass) are *also* Landau problems, and both are currently being attacked with the wrong functional. The substrate keeps reaching for an equilibrium free energy when the physics is a quench. That is the through-line of everything below.

---

## 1. BIGGEST GAPS

### G-1. The A_s amplitude normalization — the framework's largest *quantitative* failure, and it is a Landau-quench problem misdiagnosed as a budget-accounting problem.

This is open-channel-ledger **A2** ("A_s amplitude floor, 3.02× Planck, *permanent structural-position wall*") and **A3** ("TD/LI H̃-divergence, 4.56-OOM gap, the rate-limiting open question for A_s closure since S84"). Knowledge MCP confirms `TRANSIT-PS-67` is **OPEN-CRITICAL** and resolves α_s + A_s + n_s(k) simultaneously (constraint-mega-matrix UNCOMPUTED-CRITICAL #1).

The numbers are not small, and they are not stable across sessions — which is itself a tell (see Contradiction C-1). My own s64 memory records the raw transit amplitude as **3.15 OOM** over Planck; the knowledge-base equation entries record **9.5 OOM** (`P_ζ = 6.73` vs `A_s = 2.1e-9`); atlas-04 Summary and the ledger record the residual floor as **3.02× Planck** and the H̃-divergence as **4.56 OOM**. These are three different framings of one quantity.

Here is the structural diagnosis from my vantage. The transit produces a generalized-Gibbs ensemble of Bogoliubov pairs (T1-T4 PROVEN: P_exc=1.000, 59.8 pairs, sudden quench dt/T_L=1.25e-5). The scalar power is being assembled as
```
A_s = prefactor · (1/ε_H) · F_amp · (1/c_sub) · f_conv
```
with the closure attempted by *adding up* phase-decoherence channels (W2-B inter-branch variance +0.15, Mott +0.14, BKT +0.11, thimble PENDING) — my s64 result. That is a **budget** picture: total amplitude minus suppression channels. But the physically correct object for a sudden quench through a critical point is a **Kibble-Zurek** normalization: the amplitude is set by the *frozen* correlation length ξ̂ at the moment the adiabatic-impulse boundary is crossed, not by the asymptotic pair number times a stack of independent decoherence factors. The knowledge base shows ξ_KZ is already computed and **saturated at the sudden-quench floor** (ξ_KZ = 0.808 M_KK⁻¹, "shorter: sudden quench", s53/s55). A saturated ξ_KZ is the signature that the framework is in the **impulse regime where the standard KZ scaling law `ξ̂ ∝ τ_Q^{ν/(1+zν)}` breaks down** — and in that regime the amplitude normalization is *not* the naive product. The 3-9 OOM overproduction is, in Landau terms, what you get when you normalize an impulse-quench spectrum with a quasi-static (slow-roll-shaped) prefactor. The gap is real but I judge it **misclassified as "permanent structural-position wall"** — it is a normalization-scheme problem, and normalization schemes are exactly where Landau theory has the most to say (see Bridge B-1).

### G-2. The dark-matter mass (the "170× problem") — the most durable unsolved quantitative gap in my sub-domain, still open after ~60 sessions.

Knowledge MCP: the required-to-observed ratio is `m_required/m_Leggett = 170` (atlas-spectral-geometer-collab §5), and the best substrate anchor is `Mass_LeggettDM/Δ_BCS = 11.97` (C11 CONDITIONAL, pinned S96). The Leggett mode (Q=670,000 undamped, dipolar mass within 18% of the ³He analog) is the framework's dark-matter quasiparticle, and its Ω_DM h² = 0.1200 lands 0.6% from Planck (PROVEN-AT-OBSERVATION, 0-free-param). That abundance match is genuinely strong. But the **mass** that feeds it is anchored at ~12× Δ_BCS while structure formation wants ~170× — a factor ~14 shortfall that has never closed. Q3 (GOLDSTONE-MASS-FROM-DISORDER) is the live decisive question for it and remains UNCOMPUTED. This is the gap I would put second only to A_s.

### G-3. K_pivot — the scale-mapping gap (A1; "single largest *observational* load-bearing gap").

C2 is BROKEN-WITH-LIVE-RESEARCH-PATHWAY: no physical mechanism places the CMB pivot at K* ≈ 0.087 M_KK where n_s = 0.965 works; the physical e-fold mapping gives K ~ 10⁻⁵⁷ M_KK (flat, n_s = 1). This is not primarily a condensed-matter gap — it is a dimensional-transfer / RG-flow gap (the deg(T_{BZ→pivot}) transport map per phononic-framing). But it couples to G-1: the *same* transit that overproduces A_s is the one that has to land the pivot scale, and a correct impulse-quench treatment fixes both the amplitude **and** the characteristic frozen wavenumber simultaneously. They are one object viewed twice.

### G-4. τ_fold = 0.190 has no selection principle (A4).

Equilibrium τ-stabilization is a PROVEN wall (T5 BROKEN; 27 closures; HESS-40; S76 35D ridge; S95 one-loop + variational corridors FAILED). The honest fork is dynamical relaxation vs declaring τ_fold an empirical input. From my vantage this is the **order-parameter value at the transition**, and the framework has proven there is no static free-energy minimum that selects it. That is a clean, important negative — but it leaves the framework's single most-used number unexplained. I rank it a gap, not a contradiction, because the framework states it honestly.

---

## 2. CRITICAL CONTRADICTIONS

### C-1. The A_s gap magnitude is quoted at 3.15 / 3.02 / 4.56 / 9.5 OOM across the corpus, with no single canonical figure.

- My s64 memory: baseline S73B = **3.15** OOM over Planck.
- Knowledge equation entries (eq_13245, eq_13154): `P_ζ = 6.73`, gap = **9.5** OOM.
- atlas-04 Summary / open-channel-ledger A2: residual floor = **3.02×** Planck (≈ 0.48 OOM as a floor, but quoted as the wall).
- atlas-04 Summary / ledger A3: TD/LI H̃-divergence = **4.56** OOM (atlas-08 CF21 simultaneously says **2.38** OOM and flags the reconciliation explicitly).

CF21's own text admits the figure disagreement ("atlas-04 Summary reports this gap as 4.56-OOM (vs 2.38 here) — reconcile the figure"). This is not a rounding drift; 2.38 vs 4.56 vs 9.5 are structurally different claims about *how far* the transit overproduces. **A framework cannot call something a "permanent structural-position wall" while disagreeing with itself by 7 orders of magnitude about the wall's height.** This is the single most important contradiction I found, because the entire A_s research program is gated on a number nobody has pinned. It needs one canonical definition (raw P_ζ at horizon-exit vs post-decoherence residual vs the H̃-branch difference) before any closure gate is meaningful.

### C-2. The Higgs is simultaneously "PROVEN-AT-OBSERVATION, 0-free-param" and +5.36% off, while the spectator quartic was selected *by* the observation.

The ledger lists m_H = 131.8 GeV as **PROVEN-AT-OBSERVATION (0-free-param)** at +5.36% from 125.1 GeV (= 67/1251; +38.5σ vs the tight PDG band). My s66 workshop memory records that the Chamseddine-Connes vs zeta functional choice was disambiguated *because* m_H^cutoff ≈ 127.5 GeV matched observation while m_H^zeta ≈ 174 GeV did not — i.e., **the observation selected the functional**. You cannot then turn around and present the resulting 131.8 GeV as a zero-free-parameter *prediction* validated by the same observation. This is a mild circularity, not a fatal one (the quartic λ_CCM = (4/3)g₃²·(a₄/a₂) is a genuine geometric relation, and +5.36% from zero geometric inputs is real evidence), but the "+38.5σ" framing and the "PROVEN-AT-OBSERVATION" tag overstate it. In Landau language: the Higgs IS the |S|² radial (amplitude) mode of the order parameter, its mass² is the quartic curvature λv², and the framework derives λ from the heat-kernel ratio a₄/a₂ — that is the honest, strong claim. The 5.36% is a real residual that the Volovik-effacement screening (Γ_eff=0.99970) is being asked to absorb (session-102-plan-w4), and *that* screening is the unproven step.

### C-3. n_s is "COMMITTED-LIVE 0.9590" while the observations are moving away from it in the falsifying direction.

n_s = 0.9590 (sqrt-cutoff) is 1.40σ from Planck and was COMMITTED at S103 (Q28 ANSWERED, A₆-robust). But the S104 freshness bullet records ACT DR6 (0.9709-0.974) and SPT-3G (0.9679) landing **inside the pre-registered live-watch in the falsifying direction** (the σ-ladder runs 1.40σ → 2.70σ → 3.13σ → 5σ), with functional re-shopping now FORBIDDEN (PROHIBITED_ACTIONS Class 1). This is handled correctly procedurally — the fence is the right move. But the framework's headline n_s and the newest data are diverging, and the capstone still narrates 0.9590 as a success. This is a contradiction-in-tension, flagged here because the capstone-hygiene gate (Q3) keys on exactly this kind of prose-vs-register drift.

### C-4. The BCS sector is "3D Ising universality, PERMANENT" yet the cosmological transit is a sudden quench (mean-field, no critical fluctuations).

My framework-constants memory and atlas record **BCS universality class = 3D Ising (Z₂, d=3, n=1), PERMANENT** (S43). But T1 is PROVEN: the transit is a **sudden quench** with dt/T_L = 1.25e-5 and P_exc = 1.000 — the system is swept through the transition far faster than any critical mode can respond, which is the *opposite* of the quasi-static critical regime where 3D-Ising exponents govern. Both can be true (the *static* class is 3D Ising; the *dynamic* passage is impulse-quenched), but the corpus does not consistently distinguish them, and several A_s closure attempts (BKT sector-resolved, Mott) implicitly invoke equilibrium-critical scaling that the sudden quench forbids. This is the same disease as C-1/G-1 at the level of universality-class bookkeeping. (My s84 memory already flagged the related point that the framework's AZ class is BDI-hybrid, not the ³He-B textbook DIII, and that the OP coset is 8-dim not 5-dim — the inheritance is partial, not exact.)

---

## 3. UNSUPPORTED LOAD-BEARING ASSUMPTIONS

### U-1. That the spectral action Tr f(D²) is the correct effective action for the order-parameter dynamics. (atlas-04 S3, ASSUMED)

This is the deepest one in my domain. S3 is explicitly ASSUMED, and the framework's own F.5 result shows the spectral action **penalizes BCS pairing with the wrong sign** (+12.76 anti-trapping, 93×). The atlas states it plainly: "SA is a spectral moment, not a total energy. The BCS condensation energy is a Fock-space quantity. These are categorically different functionals." This is precisely the Landau warning: **the free energy that governs the order parameter is not the same functional as the one-particle spectral sum.** A_s, n_s, the modulus potential, and the CC all ride on Tr f(D²) being the right Landau-Ginzburg functional, and the framework has a proof it is *not* for the pairing channel. The two-layer architecture (S72: spectral governs n_s/gravity/H_0; BCS governs DM/pairs/A_s) is the framework's workaround — but the workaround is itself an *assumption* that the two functionals decouple cleanly, and the A_s problem (which is supposed to be BCS-sector) keeps pulling in spectral-sector quantities (H̃, ε_H). U-1 is the load-bearing crack under G-1 and G-2 both.

### U-2. That f_conv (the conversion factor from substrate amplitude to observed P_ζ) and the effacement Γ_eff = 0.99970 are physical, not fitted.

The A_s ledger formula carries an `f_conv` factor and the Higgs residual is screened by Γ_eff = 0.99970. Neither is derived from a Landau free energy; both are the places where an unexplained multiplicative number lives. When a framework with "zero free parameters" has a residual exactly absorbed by a 0.03% leakage factor, that leakage factor is a de-facto free parameter until it is derived. The Volovik partition gives Γ_eff a *story* (impedance mismatch at the acoustic white hole) but I have not seen it pinned to a substrate computation independent of the quantity it rescues.

### U-3. That the Leggett-mode mass anchor (11.97 Δ_BCS) is the *full* dark-matter mass, with no overdamping or thermal-occupation correction.

C11 is CONDITIONAL on three legs; the lab-side leg (S100b W6-3, MgB₂ Leggett overdamping) is annotated as a *consistency* leg that does **not** discharge the condition. The assumption that the relic Leggett mode survives undamped (Γ_grav < H_0) to today is doing heavy lifting for the 0.6%-Planck abundance match. In real condensed-matter systems the Leggett mode is *generically overdamped* by the pair-breaking continuum (exactly what Yuan 2412.13830 shows in MgB₂); the framework's escape is that the substrate L1 mode sits kinematically below the pair-breaking edge (x_L1 = 0.149 < 1). That is a clean argument, but it is a *single* kinematic inequality bearing the entire DM-survival claim, and it has never been stress-tested against the mass shortfall in G-2 — if the true DM mass is 170× Δ_BCS rather than 12×, the below-edge protection (which depends on ω_L1/2Δ_BCS) may not hold.

### U-4. That τ-evolution = cosmic time (C1, ASSUMED), now scoped to "the dimensional-readout leg only."

C1 is the framework's core postulate and remains ASSUMED. The S101-S102 work is honest and impressive — the rank-1 normalization-non-universality theorem (§VII.BS STAGE-3-PERMANENT) shows the substrate fixes *all dimensionless dynamical shapes* from zero continuous parameters and imports exactly one dimensional scale (M_KK). That genuinely shrinks the assumption to a single scale-setting. But the identification of the *internal modulus velocity* with the *FRW expansion rate* — that dτ is dt up to the one scale — is still a postulate, and it is the hinge on which every cosmological prediction turns. I note it not as a flaw (it is stated honestly) but as the load-bearing assumption a condensed-matter skeptic must keep in view.

---

## 4. AREAS NEEDING REFINEMENT

### R-1. Pin one canonical A_s gap number (resolves C-1). Define the three quantities separately and forever: (a) raw horizon-exit P_ζ from the impulse-quench spectrum; (b) the post-decoherence residual floor; (c) the TD-vs-LI H̃-branch difference. The corpus currently blurs all three. Until this is done, no A_s closure gate has a meaningful threshold.

### R-2. Re-derive the A_s normalization in the proper impulse-quench (sudden) limit, not the slow-roll-shaped prefactor. The framework has ξ_KZ saturated at the sudden-quench floor — it knows it is in the impulse regime — but the amplitude formula still carries a `1/ε_H` slow-roll factor. In the impulse limit the amplitude is set by the frozen-mode occupation |β_k|² at the adiabatic-impulse boundary, which is a *Bogoliubov coefficient*, not a slow-roll ratio. This is the single highest-leverage condensed-matter recomputation available.

### R-3. Distinguish static vs dynamic universality class explicitly (resolves C-4). State everywhere whether a closure invokes the *static* 3D-Ising critical exponents (legitimate only for equilibrium quantities) or the *impulse-quench* Bogoliubov spectrum (the only legitimate object during transit). The BKT and Mott A_s channels need this audit.

### R-4. The Higgs residual (+5.36%) and the effacement factor (U-2) should be decoupled. Either Γ_eff = 0.99970 is derived independently of m_H, or the m_H claim is re-tagged from "PROVEN-AT-OBSERVATION 0-free-param" to "geometric quartic + one screening factor." The current presentation conflates a genuine geometric result (λ from a₄/a₂) with a rescue factor.

### R-5. The dark-matter mass anchor needs a quasiparticle stress-test. Compute the Leggett-mode self-energy from the pair-breaking continuum at the *substrate* (not lab) parameters and ask whether the below-edge protection (U-3) survives if the mass is pushed toward the structure-formation-required 170× Δ_BCS. This couples G-2 and U-3 directly.

### R-6. The sub-leading anharmonic sign in the Volovik CC tracking ("from below," n_eff → 2 from below) is type-A converged but the BBN-epoch arm fails by ~2.087× (Q29, FAIL-STRUCTURAL). This is a refinement target in the cosmological-bridge domain more than mine, but the "from below" direction is a Landau-anharmonicity statement (the quartic-and-higher curvature of ρ_vac(q)), and a proper Landau expansion of ρ_vac(q) to sixth order might constrain whether the BBN shortfall is structural or an artifact of truncating the free energy at quartic.

---

## 5. UNTRAVELED BRIDGES (the most important section)

Each below is a known condensed-matter result the framework has **not** engaged (verified via knowledge MCP), with a concrete sketch of how the substrate fills the cement — and, where I can, how it bridges two of the gaps/contradictions above.

### B-1. ★ Beyond-slow-roll / impulse-quench power spectra (Kibble-Zurek in the fast-quench regime) — DIRECTLY bridges G-1 (A_s) and C-1 (the gap-magnitude contradiction).

**The result/mystery**: In the *fast*-quench (impulse) limit, the standard Kibble-Zurek scaling `ξ̂ ∝ τ_Q^{ν/(1+zν)}` saturates and the defect/excitation spectrum is set instead by the **non-adiabatic Bogoliubov coefficients** at the freeze-out boundary — see Zurek's own treatment of the sudden-quench crossover and the broad analog-gravity literature on particle production in rapidly-varying backgrounds (Jain/Weinfurtner-class BEC experiments; del Campo & Zurek, *Universality of phase transition dynamics*, Int. J. Mod. Phys. A 29 (2014) 1430018, arXiv:1310.1600). The framework's `ξ_KZ = 0.808 M_KK⁻¹ "saturated at sudden-quench floor"` is the *fingerprint of this regime*, but the A_s amplitude is still being assembled with a slow-roll-shaped `1/ε_H` prefactor plus an additive decoherence budget.

**How the substrate fills the cement**: The transit (T1-T4, all PROVEN) gives the exact impulse-quench data the framework needs and the slow-roll formula throws away: the pair wavefunction (93% B2, 6.3% B1, 0.7% B3), P_exc = 1.000, and the Bogoliubov |β_k|² mode-by-mode. The scalar power should be `A_s ∝ Σ_k |β_k|² /(comoving volume at freeze-out)`, normalized by the frozen ξ_KZ — *not* the asymptotic pair number times Π(decoherence factors). This is a single, well-posed recomputation. **The bridge**: doing it in the correct impulse limit (i) replaces the unstable 3.15/9.5/4.56-OOM budget figure with one canonical number derived from |β_k|² (resolves C-1), and (ii) the *same* calculation outputs the characteristic frozen wavenumber k̂ = 1/ξ̂, which IS the pivot-scale mapping K_pivot has been missing (G-3/A1). One impulse-quench spectrum, computed once, attacks A_s, the gap-magnitude contradiction, AND the K_pivot gap. This is the highest-leverage item I can offer.

### B-2. ★ The Higgs/amplitude (longitudinal) mode and its damping into the pair-breaking continuum — bridges C-2 (Higgs circularity) and U-2 (effacement factor).

**The result**: In a BCS/BEC superconductor the order-parameter amplitude ("Higgs"/"Schmid") mode sits at ω_H = 2Δ, right at the pair-breaking edge, and is *generically overdamped* by decay into the two-quasiparticle continuum — its observability and apparent mass depend critically on whether it sits below or at the edge (Pekker & Varma, *Amplitude/Higgs Modes in Condensed Matter*, Annu. Rev. Cond. Mat. Phys. 6 (2015) 269, arXiv:1406.2968; Shimano & Tsuji, terahertz Higgs-mode spectroscopy in NbN, Science 345 (2014) 1145). The framework has the amplitude mode (`c_Br5_Higgs3 = 11.465` Γ-point, `ω_H2 = 1.410`) but treats m_H as a bare quartic curvature with a 0.03% effacement rescue.

**How the substrate fills the cement**: Compute the Higgs (|S|²-radial) mode's self-energy from coupling to the substrate's own pair-breaking continuum (the B2/B3 two-quasiparticle states), exactly as Pekker-Varma do. **The bridge**: the resulting continuum shift is a *derived* renormalization of m_H — if it lands at ≈ −5.36% it would derive the residual that the effacement factor is currently fitting (kills U-2 and de-circularizes C-2 simultaneously). This is a substrate computation the framework can do with existing (0,0)-sector data; it converts a fitted screening factor into a Landau self-energy.

### B-3. ★ Pseudogap / preformed-pair (Nozières-Schmitt-Rink) regime — the missing piece of the dark-matter mass (G-2) and the BCS-3D-Ising tension (C-4).

**The result/mystery**: The framework engaged the BCS-BEC crossover only at the deep-BEC endpoint (`E_vac/E_cond = 28.8`, `g·N(E_F) = 2.18`, S61) — but the *interesting* physics is the **pseudogap regime** in the middle, where pairs preform above the condensation transition and the single-particle gap (Δ_pg) decouples from the condensate order parameter. The canonical treatment is Nozières-Schmitt-Rink (J. Low Temp. Phys. 59 (1985) 195) and its modern incarnations (Chen, Stajic, Tan, Levin, *Phys. Rep.* 412 (2005) 1, arXiv:cond-mat/0404274). In the pseudogap regime there are **two mass scales**: the pairing gap and the phase-stiffness scale, and they can differ by an order of magnitude.

**How the substrate fills the cement**: The 170× mass problem (G-2) is the symptom of forcing a *single* mass scale (Δ_BCS, via the 11.97× Leggett anchor) to do the job of what is physically *two* scales. In NSR language: the Leggett/abundance physics is set by the **phase-stiffness** scale (which gives the correct Ω_DM h² = 0.120), while structure formation probes the **single-particle (pseudo)gap** scale, which is the larger one. **The bridge**: an NSR/pseudogap decomposition of the (0,0)-sector gap into Δ_pairing vs the phase-stiffness D_s could simultaneously (i) preserve the 0.6% abundance match (phase-stiffness leg) and (ii) supply the missing ~14× factor for the structure-formation mass (pairing-gap leg) — resolving G-2 *without* breaking the one thing that works. It also resolves C-4: the static 3D-Ising class governs the phase-stiffness transition, while the preformed-pair gap is the impulse-quench object — two scales, two regimes, no contradiction. The framework already has the superfluid-weight machinery (Peotta-Törmä D_s = (2Δ/V)Tr g, deeply engaged) to compute the phase-stiffness leg.

### B-4. Goldstone-mode mass from disorder-induced finite correlation length (the Imry-Ma / random-field mechanism) — bridges G-2 and U-3.

**The result**: A Goldstone (phase) mode acquires a finite mass when the symmetry-breaking field is spatially disordered with finite correlation length — `m² ~ 1/ξ_disorder²` (Imry-Ma, *Phys. Rev. Lett.* 35 (1975) 1399; the random-field XY problem). The framework has this as Q3 (GOLDSTONE-MASS-FROM-DISORDER, decisive, UNCOMPUTED) with the relevant disorder set by the non-C² Josephson couplings J_su2 = 0.059, J_u1 = 0.034.

**How the substrate fills the cement**: The Josephson-coupling disorder on the substrate's gauge directions sets ξ_disorder, and m_Goldstone² ~ 1/ξ_disorder² could give a mass *parametrically larger* than the bare Leggett anchor — potentially the missing factor for G-2 — while remaining below the pair-breaking edge (preserving U-3's protection argument). This is a clean, pre-registered, never-run computation that directly targets the framework's #2 gap. I rank it just below B-3 because B-3 explains *why* there should be two scales and B-4 supplies *one mechanism* for the second one; they are complementary.

### B-5. Anderson-Higgs *evasion* via the Kosmann obstruction reframed as a topological-order (deconfined) phase — bridges C-2 and the N4 BROKEN wall.

**The result/mystery**: The framework PROVED the U(1)_7 Goldstone *cannot* be gauged ([iK_7, D_K] = 0; N4 BROKEN, Anderson-Higgs Impossibility wall, S51). In ordinary Landau theory an ungaugeable, gapless Goldstone is a problem. But there is a known escape the framework has not engaged: in **deconfined / topologically-ordered phases** (Senthil et al., deconfined quantum criticality, *Science* 303 (2004) 1490; and the broader fracton literature) symmetry-protected gapless modes coexist with no Higgs mechanism and no Landau order parameter, because the relevant degrees of freedom are *fractionalized*. (Note: the framework checked a *fracton-immobility* DM corridor at S104 W5-3 and FAILED it — "no position operator on a compact fiber" — so the fracton-DM door is closed, but the deconfined-criticality framing for the *Goldstone* is a distinct, untraveled question.)

**How the substrate fills the cement**: Treat the U(1)_7 sector not as a would-be-Higgsed gauge symmetry but as a **deconfined critical** sector whose gaplessness is protected by the same [iK_7, D_K] = 0 identity that forbids gauging. **The bridge**: this would convert the N4 BROKEN wall from a *defect* into a *feature* (the substrate is a beyond-Landau topologically-ordered phase, which is exactly the kind of "concrete substrate for a known mystery" the project conceit calls for), and it bears on C-2 because a deconfined sector has its own amplitude-mode spectrum distinct from the naive Higgs. Speculative — but it is the right known-physics box to open for an ungaugeable Goldstone.

### B-6. Hertz-Millis quantum-critical scaling of the modulus (τ) — bridges G-4 (τ_fold selection) and R-6 (CC anharmonicity).

**The result**: When a *bosonic* order parameter has no static minimum but is driven through a transition by coupling to a continuum of soft modes, the relevant theory is the Hertz-Millis quantum-critical action (Hertz, *Phys. Rev. B* 14 (1976) 1165; Millis, *Phys. Rev. B* 48 (1993) 7183), where Landau damping from the fermionic continuum generates the effective dynamics `ω ~ k^z` with dynamical exponent z. The framework has PROVEN there is no static τ minimum (T5/A4) but has only tried one-loop + variational *equilibrium* selection (S95 FAIL).

**How the substrate fills the cement**: τ is a bosonic modulus coupled to the 155,984-mode D_K continuum. Hertz-Millis says the modulus dynamics — including any *dynamically* selected scale — comes from **Landau damping** of τ by that continuum, not from a static potential. **The bridge**: this is the "dynamical-relaxation" fork of A4 made concrete (it tells you the friction term q'' + 3Hq' + ... that Q29/C10 needs for the CC tracking-vacuum closure, R-6), and it offers a *dynamical* (not static) origin for a preferred τ scale via the damping-induced effective action — the only route left after the equilibrium corridors closed. The dynamical exponent z would be computable from the D_K spectral density at the fold.

---

## Highest-leverage next steps (3-5 concrete items)

1. **Pin ONE canonical A_s gap number** (R-1, resolves C-1). Define raw-P_ζ / post-decoherence-residual / H̃-branch-difference as three separate named quantities in canonical_constants, each with a verdict-pinned value. This is bookkeeping but it unblocks every downstream A_s gate. *Effort: ~1 session, no new physics.*

2. **Recompute A_s in the impulse-quench (Bogoliubov-|β_k|²) limit** (B-1, R-2). Replace the slow-roll `1/ε_H` prefactor + additive decoherence budget with the frozen-mode occupation normalized by the saturated ξ_KZ. Output BOTH the amplitude and the frozen wavenumber k̂. *This single computation attacks G-1, C-1, and G-3 (K_pivot) at once — the highest-leverage item in the whole list.*

3. **NSR/pseudogap two-scale decomposition of the (0,0)-sector gap** (B-3, R-5). Separate the phase-stiffness scale (feeds the 0.6%-Planck Ω_DM via Peotta-Törmä D_s) from the single-particle pseudogap scale (feeds structure formation). *Targets the ~14× dark-matter mass shortfall (G-2) without breaking the abundance match, and dissolves C-4.*

4. **Derive the Higgs continuum self-energy (Pekker-Varma)** (B-2, R-4). Compute the |S|²-mode shift from coupling to the substrate two-quasiparticle continuum and test whether it reproduces the −5.36% residual currently absorbed by Γ_eff. *Converts a fitted screening factor (U-2) into a derived Landau self-energy and de-circularizes the Higgs claim (C-2).*

5. **Run the never-computed Goldstone-mass-from-disorder gate** (B-4, Q3). m_Goldstone² ~ 1/ξ_disorder² with ξ_disorder set by J_su2 = 0.059, J_u1 = 0.034. *Pre-registered, zero-cost-to-specify, directly targets G-2; complements B-3.*

— Landau-condensed-matter-theorist. The recurring structural finding across all five sections: the substrate keeps reaching for an equilibrium free energy where the physics is a sudden quench. The proven internal geometry is a Landau problem solved right; the two big live gaps (A_s, DM mass) are Landau problems being solved with the wrong functional. Fix the functional (impulse-quench normalization; two-scale pseudogap) and the gaps and contradictions collapse together.
