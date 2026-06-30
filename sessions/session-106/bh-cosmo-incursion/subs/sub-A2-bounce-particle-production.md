# Sub-A2 — Bounce Dynamics & Particle Production: an adversarial transit-dynamics audit

**Agent**: `transit-dynamics-theorist` (Workhorse-Transit-Dynamics)
**Campaign**: BH-Cosmology ↔ Exflation incursion (Lead A / `hawking-theorist`)
**Date**: 2026-06-13
**Mandate**: FALSIFICATION-first. Compare the GR-side **nonsingular bounce** family (Poplawski torsion bounce; Gaztañaga degeneracy-pressure / quantum-exclusion bounce) against the framework's **first-order supersonic transit** at τ_fold = 0.190. Hunt for tension, no-analogs, and places where the GR literature is more predictive than the framework. Throughlines **T2** (torsion bounce vs transit) and **T10** (bounce relics vs GGE relic) are mine; I also touch the Kibble–Zurek discriminator.

**Framing law respected** (`phononic-framing.md`): the substrate is logically prior; each GR bounce is a GEOMETRIC-class laboratory-IN model whose dynamics I read against the substrate-IS transit. **But the mandate is falsification, not confirmation** — I report below several places where the substrate has NO analog of a GR-side falsifiable prediction, and one place where the GR program is internally inconsistent in a way the framework is not.

---

## 0. Sources actually read (no training-knowledge citations)

| Source | What I extracted |
|:--|:--|
| Poplawski 1007.0587 (*Cosmology with Torsion*, PLB 694, 2010) | full text via `read_arxiv_paper`; spin-fluid `ε_S = −κs²/4 ∝ a⁻⁶`, `â_m = √(−Ω_S/Ω_R)`, `Ω_S ≈ −8.6×10⁻⁷⁰`, `v_a = 1.1×10³²c`, Parker-citation passage |
| Poplawski 1111.4595 (*Nonsingular Big-Bounce from Spinor-Torsion*, PRD 85, 2012) | full text; **cusp** bounce (ȧ jumps −v→+v), `T_cr ≈ 0.78 m_P`, `t_0 = β_cr²√(3/κh_⋆)`, density-parameter `Ω(T)−1 ∝ T⁻²` |
| Poplawski 2008.02136 (*Collapse of Fluid with Torsion*, JETP 132, 2021) | full HTML; **phenomenological** production rate `(1/c√−g)d(√−g n_f)/dt = βH⁴/c⁴` (Eq. 33), tuned-β finite inflation, `n_f ∼ a⁻⁽³⁺δ⁾` |
| Gaztañaga 2204.11608 (*How the Big Bang Ends up Inside a Black Hole*, Universe 8, 2022) | keyword-extracted body; neutron-degeneracy / nuclear-saturation (GeV) supernova-rebound bounce; **super-horizon re-entry**; **λ>2R cutoff → lack of large-scale CMB power**; `Q_H = 669` measured-cutoff claim |
| Gaztañaga 2602.17702 (*Cosmological Bounce Relics: BH/GW/DM*, 2026, physics.gen-ph) | full extraction (via subagent, verbatim quotes): **quantum-exclusion** stiff EoS `P=−ρ²/ρ_G` (gen. Chaplygin α=2), cosh-law `a∝cosh(τ/R_B)`, λ>90 m survival floor, "Bounce Dark Matter" relic BHs 10–10⁸ M_⊙ |
| Framework: `transit-flow-genesis-to-now.md` §5.2–§5.3 | mode equation, sudden-quench ratio, GGE relic, KZ freeze-out paragraph |
| Framework: `atlas-04-assumptions.md` T1/T2/T3/T7, `Phononic-framework-hypothesis.md` | T1 "Transit is sudden quench" PROVEN; "WKB structurally inapplicable, sudden approximation mandatory" PROVEN; T3 "GGE never thermalizes" **BROKEN** |
| Knowledge MCP | `T3-S38-KZ-DEFECTS` (0D regime L/ξ_GL=0.031, **no domain walls**); π₀(G/H)=0; ξ_BCS=0.8083; c_fabric=209.97; `tau_fold`=0.19; `Mach_max`=13.75; n_pairs=59.8, P_exc=1.000 |

**Corpus gap flagged**: 2602.17702 and 2204.11608 were NOT archived under `researchers/`; they live only in `downloads/bh-cosmo/`. Not my write to fix, but noted for the curator.

---

## 1. The substrate transit — what it actually IS (anchor, then compare)

The substrate IS the spectral triple `(A_K, H_K, D_K(τ))` on Jensen-deformed SU(3). As τ climbs the monotone Jensen gradient `dS/dτ = +58,673`, the Dirac density of states develops a **van Hove singularity** `g(ω) ∼ 1/√(ω−ω_min)` (an A₂ catastrophe fold) at τ_fold = 0.190. The BCS 1D theorem forces any attractive coupling to strong coupling (zero critical coupling), so the transition is **first-order**. The crossing is **supersonic** (Mach 13.75 = v_transit/c_fabric, c_fabric = 209.97 M_KK) and **impulsive**, with transit duration δt_transit = 1.130×10⁻³ M_KK⁻¹.

The cosmogenesis event is not metric expansion; it is **spectral reorganization inside each fiber** — the eigenvalue spectrum of D_K complexifies through the fold. There is no singularity (the fold is a finite van Hove cusp), no inflaton, no slow roll. The reheating analog is **Parker / Bogoliubov pair production** of fiber excitations into a **Generalized Gibbs Ensemble (GGE) relic**: 59.8 quasiparticle pairs, P_exc = 1.000.

**The governing mode equation** (substrate, `transit-flow-genesis-to-now.md` §5.3, E12):
```
u_k'' + ω_k(τ)² u_k = 0 ,     ω_k(τ) = √( ε_k(τ)² + Δ(τ)² )          (1)
```
with (α_k, β_k) the in/out Bogoliubov coefficients, |α_k|² − |β_k|² = 1, occupation n_k = |β_k|². The crossing is **diabatic**: δt_transit/T_L = 1.25×10⁻⁵, so the adiabatic condition ω'/ω² ≪ 1 is **maximally violated**, and the sudden-limit occupation saturates:
```
P_exc = |β_k|²/(1+|β_k|²)|_sudden → 1.000 .                          (2)
```

This is the structure I will hold every GR bounce against.

---

## 2. T2 — Torsion / degeneracy bounce vs van Hove transit. Are they the same bounce dressed differently?

### 2.1 Mechanism inventory (read off the equations, not the abstracts)

| | **Poplawski torsion** (1007.0587, 1111.4595, 2008.02136) | **Gaztañaga** (2204.11608 / 2602.17702) | **Framework transit** |
|:--|:--|:--|:--|
| Driver | Spin-spin contact term from Dirac torsion: `ε_S = −κs²/4 ∝ a⁻⁶`, `s² = (1/8)(ħcn)²` (1007.0587 Eq.13,15). Stiff w=+1 but **negative** energy density | Quantum **Pauli-exclusion degeneracy pressure**. 2204: neutron degeneracy at nuclear saturation (GeV), supernova rebound. 2602: stiff EoS `P=−ρ²/ρ_G` (gen. Chaplygin α=2), NEC-saturated ground state ρ_G | **van Hove spectral fold** (A₂ catastrophe) of D_K eigenvalue DOS; first-order BCS instability (zero critical coupling) |
| What stops the collapse | a⁻⁶ repulsion overtakes a⁻⁴ radiation at `â_m = √(−Ω_S/Ω_R) = 3.1×10⁻³³` (Eq.24); turning point `H=0` | density saturates at ρ_G where ẋρ=0, ω=−1, T_μν k^μ k^ν → 0 (NEC saturated). Closed k=+1 slices evade Penrose theorem | the modulus does not "stop" — it **transits** through the fold and continues up the monotone ramp; there is no turning point in τ |
| Energy/density scale | `ρ ≈ 1.1×10¹¹⁶ J/m³` at â_m — **above** Planck density by orders (1007.0587 §VII) | 2204: GeV (nuclear). 2602: ρ_G > ρ_SD, R_B < 90 m. **Far below Planck** (explicitly: "many orders away from Inflation or Planck", 10¹⁹ GeV) | M_KK = 7.43×10¹⁶ GeV (single KK hierarchy); the fold is a substrate-internal scale, not a matter density |
| Kinematic character | **CUSP**: ȧ jumps discontinuously −v→+v (1111.4595); θ=3ȧ/a jumps −3v/a_cr→+3v/a_cr. a(t) continuous, ȧ discontinuous | **ADIABATIC / quasi-de Sitter**: `a∝cosh(τ/R_B)` smooth (2602 Eq.22). Both ȧ AND a continuous and smooth | **SUDDEN / diabatic**: δt/T_L = 1.25×10⁻⁵; sudden-quench limit of the mode equation |
| Free parameters | "no free parameters (G,c set to 1)" claimed — but Ω_S, T_cr, a_r T_r are matter inputs | ρ_G, R_B, β-production rate (phenomenological) | tau_fold=0.190 pinned by van Hove non-stationarity theorem (S85); Mach 13.75 derived from c_fabric |

### 2.2 Are any of these the SAME bounce?

**No — and the differences are structural, not cosmetic.** The three "bounces" do not even share a topology of the dynamical event:

1. **Poplawski and Gaztañaga are turning-point bounces** (`H=0`, ȧ reverses sign): the scale factor reaches a finite minimum and re-expands. They are TIME-SYMMETRIC about the bounce point (up to the entropy/particle-production asymmetry Poplawski must add by hand). **The framework transit is NOT a turning point**: τ is monotone (`dS/dτ = +58,673 > 0` throughout), it never reverses. The "bounce" structural analog in the framework is the **acoustic white hole** (subsonic→supersonic→subsonic causal flow), which is a *spatial* causal boundary in the fabric, not a *temporal* turn-around of a scale factor. Calling the transit a "bounce" is already a category slip.

2. **Poplawski's driver is a⁻⁶-scaling negative-energy spin term; Gaztañaga's is a degeneracy-pressure stiff fluid; the framework's is a van Hove DOS singularity.** These are three distinct physical objects. The a⁻⁶ scaling (Poplawski) is the SAME power law as anisotropic shear σ²∼a⁻⁶ — indeed 2008.02136 spends its central argument showing torsion must beat shear, which forces him to *add particle production by hand* (§2.4 below). The framework's fold has no a⁻⁶ structure; it is a spectral-geometry feature of D_K, scale-free in this sense.

3. **Poplawski and Gaztañaga are GR (a metric scale factor a(t) in FLRW); the framework is pre-metric** — the 4D metric g_M *emerges* from the a₂ Seeley–DeWitt coefficient of the same D_K that is folding. In the substrate picture there is no a(t) at the fold to "bounce"; a(t) is a downstream emergent quantity (and the framework's own a(t)/effective-Friedmann mapping is BROKEN/ASSUMED, atlas-04 C1 — see §5 falsification).

**Internal tension WITHIN Gaztañaga's own program (a falsification finding):** the 2204.11608 bounce is a **neutron-degeneracy nuclear-saturation supernova rebound at GeV**, while the 2602.17702 bounce explicitly says the collapse stays *below* nuclear saturation (Eq.12: `ρ(τ=1s) ≪ ρ_NS`) and is driven by a quantum-exclusion stiff EoS `P=−ρ²/ρ_G` ground state. These are two **different bounce densities and two different EoS** under the same "BHU" banner. The framework's tau_fold is a single pinned value (van Hove non-stationarity theorem, S85). On the *consistency-of-the-bounce-scale* axis, the framework is tighter than the Gaztañaga program.

### 2.3 Which is more quantitative?

**Poplawski's torsion bounce is the most quantitative of the three GR models** at the *background* level: he writes a closed Friedmann system `|H| = H₀(Ω_R â⁻⁴ + Ω_S â⁻⁶)^{1/2}` (1007.0587 Eq.21), an exact parametric solution `a(η)` (1111.4595 Eqs.20–22), and pins `Ω_S ≈ −8.6×10⁻⁷⁰` from the relic-neutrino number density. That is a genuine, derived, parameter-light background. **Gaztañaga is the least quantitative on dynamics** (no closed perturbation spectrum; cosh-law with an unfixed R_B; β-production tuned).

**But the framework is the only one of the three that computes an actual particle-production spectrum** (§3). On *background dynamics* the framework's a(t) is its weakest leg (BROKEN, atlas-04 C1); on *quantum production* it is overwhelmingly the strongest. The three programs are quantitative on **different layers**, and this is the cleanest way to state the comparison honestly.

**T2 verdict**: GENUINELY DISTINCT bounces. No two of the three share mechanism, kinematic character, or even bounce topology. The "torsion bounce ≈ transit" pairing in the campaign plan is a **surface analogy that does not survive the mode equation**.

---

## 3. T-particle-production — the highest-value falsification target. Is "shared Parker mechanism" real?

This is where my spawn prompt pointed me, and the answer is sharp.

### 3.1 What each program actually does with "Parker"

**Poplawski (1007.0587, 1111.4595, 2008.02136)** invokes Parker production at **three escalating levels of (non-)rigor**:
- 1007.0587 (§VII): *qualitative* — "intense pair production in the presence of extremely large tidal forces … increases the energy density … isotropization", citing Parker 1969 [32], Zel'dovich 1970 [33], Kerlick 1975 [34]. **No equation.** The role is to isotropize and to seed Ω_S.
- 2008.02136 (Eq.33): *phenomenological rate equation* — `(1/c√−g) d(√−g n_f)/dt = βH⁴/c⁴`, where **β is "a nondimensional production rate"**, a free knob. This changes `n_f ∼ a⁻⁽³⁺δ⁾` (Eq.35) so torsion can beat shear; tuning `(βH³)/(3c³h_nf T³)` "slightly less than 1" gives a finite inflation epoch.
- **There is NO mode equation, NO Bogoliubov α_k/β_k, NO occupation spectrum n_k, NO power spectrum anywhere in the Poplawski corpus I read.** "Parker" is a *citation* and a *bulk H⁴ source term with a free coefficient*, never a computed Bogoliubov transformation.

**Gaztañaga (2602.17702)**: Parker is **not even cited**. Zel'dovich appears only for the retarded-cores PBH hypothesis, not for particle production. The relics are **classical gravitational-collapse survivors** ("nonlinear structure formation during collapse … rather than primordial quantum fluctuations"). There is **NO Bogoliubov content at all.**

**Framework**: computes the genuine object. Mode equation (1), Bogoliubov (α_k, β_k) with unitarity, occupation n_k = |β_k|², sudden-limit saturation P_exc = 1.000 (2), N_pair = 59.8 quasiparticle pairs (S38, S39 PROVEN), and a **closed-form GGE relic** `λ_k^GGE = −ln|ψ_pair[k]|²` with three Lagrange multipliers reflecting the SU(3) branch structure.

### 3.2 The adiabaticity discriminator (my computation)

**Governing structure**: for a mode obeying (1), production is controlled by the adiabaticity parameter `A_k = |ω_k'/ω_k²| ∼ (background rate)/(mode frequency)`. `A ≪ 1` ⇒ adiabatic, β→0 exponentially (no production); `A ≫ 1` ⇒ sudden, β→O(1) (broadband production). I computed A for all three (framework venv python + Sage; every step shown in the working below).

**Framework transit (sudden):**
```
T_L (BdG mode timescale)        = 90.413 M_KK⁻¹    (= dt_transit/diab_ratio)
dt_transit/T_L (diabaticity)    = 1.25×10⁻⁵        (atlas-04 T1, PROVEN)
A_framework = T_L/dt_transit    = 8.0×10⁴           ⇒ DEEP SUDDEN
```
Broadband: ALL modes with ω ≲ A/δt are produced; n_k = |β_k|² saturates → P_exc = 1.000. Sudden-limit form (Sage-exact): `|β|²(r) = (1−r)²/(4r)`, `P_exc(r) = (1−r)²/(4r+(1−r)²)`, with r = ω_out/ω_in; `lim_{r→0} P_exc = 1` (the gap collapses at the van Hove fold ⇒ saturation), `lim_{r→1}|β|² = 0` (no production absent a frequency change). The substrate sits at the r→0 (saturated) corner.

**Poplawski cusp bounce (Planck-T):** in reduced-Planck units (m_P=ħ=c=κ=1), with T_cr ≈ 0.78 m_P (1111.4595 Eq.28), g_⋆ = 28+(7/8)·90 = 106.75, h_⋆ = (π²/30)g_⋆:
```
t_0 (torsion-era timescale)     ≈ 0.48 m_P⁻¹  (~ a few Planck times)
bounce rate 1/t_0               ≈ 2.08 m_P
A_pop ≈ (1/t_0)/T_cr            ≈ 2.7         ⇒ MARGINAL (order unity)
```
**Subtlety I will not paper over** (intellectual honesty): Poplawski's bounce is a **velocity-discontinuity cusp** — ȧ jumps sign. A *true* discontinuity in a quantum-field mode frequency ω_k would give broadband sudden production (like the framework). But the cusp is in ȧ (the expansion *rate*), not in ω_k itself: the mode frequency ω_phys = √(k²/a² + m²) stays **continuous** across the bounce (only its time-derivative kinks). So Poplawski's bounce is "milder than a jump": A ~ O(1) for the bulk thermal modes (ω ~ T_cr), meaning O(1) production only for the lowest modes (ω ≲ 1/t_0 ~ m_P), and the bulk thermal bath sits right at the adiabatic boundary. It is **neither the framework's deep-sudden A~10⁴ NOR a deep-adiabatic A≪1** — and Poplawski never computes which modes get produced, so the spectrum is simply absent.

**Gaztañaga cosh bounce (quasi-de Sitter):** `a∝cosh(τ/R_B)`, H_max ~ 1/R_B, R_B < 90 m (c=1). For a sub-bounce-horizon field mode (λ ≪ R_B): `A = H_max/ω = λ/R_B ≪ 1` ⇒ **DEEP ADIABATIC**. Only super-bounce-horizon modes (λ > R_B ~ 90 m) freeze and survive — and those survive as **classical** relics (frozen curvature perturbations / pre-formed compact objects), not as Bogoliubov pairs.

**Discriminator summary:**

| Bounce | adiabaticity A | production character | spectrum computed? |
|:--|:--|:--|:--|
| **Framework transit** | **~ 8×10⁴** (deep sudden) | broadband n_k saturation, P_exc=1.000, 59.8 pairs | **YES** (closed-form GGE) |
| Poplawski cusp | ~ 2.7 (marginal) | O(1) only at lowest modes; ȧ-kink not ω-jump | NO (free-β H⁴ source) |
| Gaztañaga cosh | ≪ 1 (adiabatic) | none — classical collapse survivors | NO (no Bogoliubov) |

**~5 orders of magnitude separate the framework (sudden) from Gaztañaga (adiabatic), with Poplawski marginal in between.**

### 3.3 Verdict on "shared Parker mechanism"

**Correspondence: framework GGE relic ↔ Poplawski Parker production.**
**STRENGTH: WEAK (citation-level only). Rating 2/10.**
Reason: both *cite* Parker/Zel'dovich gravitational particle production, but only the framework *computes* a Bogoliubov spectrum. Poplawski's "Parker" is a phenomenological bulk source `βH⁴` with a free coefficient whose job is isotropization + a tuned inflation epoch — structurally a *different use* of the idea. They agree on the **name of the 1969 reference**, not on a shared computed object. The kinematic regimes are 4–5 OOM apart (sudden vs marginal). **This is the sharpest tension in my remit and it demotes a correspondence the campaign plan listed as a throughline.**

**Correspondence: framework GGE relic ↔ Gaztañaga bounce relics.**
**STRENGTH: VERY WEAK / NO-ANALOG on the production axis. Rating 1/10.**
Reason: Gaztañaga's relics are classical gravitational-collapse survivors with no Bogoliubov content and no Parker citation. The only thing shared is the word "relic." (They ARE comparable on the *relic-population* axis — see T10 §4.)

---

## 4. T10 — Bounce relics vs GGE relic. Relic-population discriminator.

### 4.1 What each predicts as a relic

| | **Gaztañaga 2602.17702 "Bounce Dark Matter"** | **Framework GGE relic** |
|:--|:--|:--|
| Relic content | broad-spectrum **relic black holes** (sub-solar → 10⁵–10⁸ M_⊙ SMBH seeds; 10–100 M_⊙ low end). = non-particle DM (BH/NS compact objects). GWs qualitatively (merger-rate enhancement) | **59.8 GGE quasiparticle pairs** (Parker pair production, P_exc=1.000). DM = **Leggett-channel inter-band coherence mode** (CPT-neutral, non-annihilating); Ω_DM h² (Leggett) = 0.1200 vs Planck 0.1207 (0.6% at 0 free params, atlas-04 row 9 PROVEN-AT-OBSERVATION) |
| Origin | classical nonlinear structure formation pre-bounce + survival of compact objects through bounce (λ>90 m floor) | Bogoliubov pair production of D_K fiber excitations at the van Hove fold |
| Mass function | Press–Schechter halo MF (broad, not monochromatic); abundance NOT computed | substrate-derived occupation spectrum; Ω_DM computed |
| GW spectrum | **Ω_GW / frequency / amplitude ABSENT** (qualitative only) | framework GW falsifier RETIRED (walls=0 EXACT, S96); peak GW-detector-sterile |
| Quantitative falsifiable number | none with error bars; tests qualitative (CMB small-scale excess, LIGO merger-rate, microlensing); **no LISA, no Ω_GW** | Ω_DM h² = 0.1200 (LIVE, 0.6% match); Aalto LTL 9-row 3He-B lab-falsifier suite (2031 horizon) |

### 4.2 Relic-population discriminator

The two programs predict **physically opposite relic types**: Gaztañaga's DM is **macroscopic compact objects** (relic black holes, 10–10⁸ M_⊙); the framework's DM is a **microscopic CPT-neutral quasiparticle coherence mode** (Leggett channel). These are observationally distinguishable in principle (microlensing / PBH searches / dynamical constraints for Gaztañaga; lab 3He-B spectroscopy + collisionless σ/m for the framework). But:

- Gaztañaga's relic prediction is **qualitative** — broad mass range, no abundance normalization, no GW spectrum, no σ-level. Even his own falsifiability section names tests (ACT/SO/CMB-S4 small-scale excess, LIGO merger rate) without a single quantitative threshold.
- The framework's DM relic is **quantitative and LIVE**: Ω_DM h² = 0.1200 at 0 free parameters (0.6% from Planck), plus a 9-row lab-falsifier suite with atomic predictions (e.g. SW1 = 58.9589 MHz).

**T10 verdict**: GENUINELY DISTINCT relic populations (macroscopic-BH vs microscopic-quasiparticle). On *quantitative predictiveness of the relic abundance*, the framework is **ahead** (a 0.6% Ω_DM match vs Gaztañaga's un-normalized mass range). On *one observable Gaztañaga has and the framework lacks* — a relic **black-hole/PBH** population — see the no-analog in §5.

**Correspondence: GGE relic ↔ bounce relics.**
**STRENGTH: WEAK as "same mechanism" (2/10); MODERATE as "both are reheating-substitute relic-population predictions" (5/10).** Both replace the standard reheating/PBH story with a bounce/transit relic, and both make a DM candidate. But the candidates are opposite in kind and only the framework normalizes the abundance.

---

## 5. FALSIFICATION SECTION (mandate-critical)

This is where I report tension, contradiction, no-analogs, and framework-exceeding results — **including tensions I searched for and did NOT find.**

### 5.1 NO-ANALOG #1 (hard flag) — Gaztañaga's large-scale CMB power cutoff (λ>2R)

**Gaztañaga 2204.11608 makes a sharp, falsifiable, large-scale prediction the framework cannot match.** During the collapse phase, perturbations exit the horizon and re-enter during expansion ("the collapsing phase acts like Inflation"), but with a **finite-size causal cutoff**: "the spectrum of incoming fluctuations have a cut-off for scales larger than **λ>2R (k<π/R)**, while Inflation is scale invariant in all scales. This results in an **anomalous lack of the largest structures in the CMB sky**." He ties this to a *measured* CMB homogeneity-scale cutoff `Q_H = 669` (Fosalba–Gaztañaga).

**The framework's n_s = 0.9561 comes from gauge-invariant spectral geometry (frozen Sasaki–Stewart spectrum, exact at CMB to 10⁻¹¹³, n_s=1 unbroken by BCS dispersion running).** The framework does **NOT** predict super-horizon perturbation re-entry from a collapse phase, and does **NOT** predict a large-scale (IR) power deficit at a causal-horizon scale 2R. There is no collapse phase in the monotone transit; there is no R(t) collapse-radius generating an IR cutoff.

**This is a genuine NO-ANALOG and a place where Gaztañaga is MORE predictive than the framework on a specific, named, claimed-detected observable.** It is exactly the kind of falsifiable large-scale signature the framework lacks. I flag it **hard**, as instructed. (Caveat for the synthesis: the `Q_H` "detection" is contested/cosmic-variance-limited at the largest scales — a `sagan-empiricist` adjudication would be appropriate — but the *prediction* is sharp and the framework has no counterpart.)

**Note for the synthesis**: the *relics* paper (2602.17702) does NOT carry this IR cutoff — there the relics are subdominant on large scales and leave a standard scale-invariant inflationary baseline. So the λ>2R cutoff lives specifically in 2204.11608. The two Gaztañaga papers are NOT consistent on whether the large-scale spectrum has a deficit (2204) or a standard scale-invariant baseline (2602) — another internal tension in his program.

### 5.2 NO-ANALOG #2 — relic black-hole / PBH population

Gaztañaga's "Bounce Dark Matter" predicts a **relic black-hole** population (10–10⁸ M_⊙) doubling as SMBH seeds; Poplawski's program predicts BH-interior baby universes. The framework's DM is a Leggett-channel quasiparticle, and the framework's primordial-black-hole content is, as far as I traced, **not a relic-population prediction at all** (the GW flagship is RETIRED, walls=0 EXACT). So a *relic-BH/PBH discriminator observable* (microlensing, PBH-merger GW, SMBH-seed demographics) is a GR-side prediction with **no framework analog**. This is less sharp than 5.1 (Gaztañaga's BH population is un-normalized) but it is a genuine asymmetry: the framework makes no PBH/BH-relic prediction to be falsified.

### 5.3 Kibble–Zurek discriminator — framework is MORE developed, but the result is "no defects" (a two-edged finding)

A first-order transit at finite rate *should* produce topological defects with a Kibble–Zurek density scaling `n_defect ∼ ξ_KZ⁻ᵈ`, `ξ_KZ = ξ₀(τ_Q/τ₀)^{ν/(1+zν)}`. **Neither Poplawski nor Gaztañaga computes a defect spectrum** — Kibble–Zurek, defects, domain walls, strings, monopoles are **entirely absent** from all five GR papers (monopoles appear only inside a reference *title* in 2602.17702). 

**The framework DID compute Kibble–Zurek (S38, S42) and found NO topological defects, for two independent reasons:**
1. **Connected coset**: `π₀(G/H) = 0` ⇒ no domain-wall topology (S19d Landau).
2. **0D regime**: `T3-S38-KZ-DEFECTS` returns `L/ξ_GL = 0.031` — the transit volume is smaller than one correlation length, so no defect can form. The KZ freeze-out length **saturates at the sudden-quench floor** `ξ_KZ = ξ_BCS = 0.8083 M_KK⁻¹` (the standard KZ scaling `(τ_Q/τ₀)^{...}` is *killed* by the sudden quench — there is no slow-quench scaling regime to exhibit). S57 theorem: "GGE Universality — all cells identical post-transit, E_DW=0, **no domain walls**."

**Two-edged reading (honest):** On the *methodology* axis the framework is far ahead — it has an explicit KZ computation where the GR programs have none. But the framework's *conclusion* is "no relic defect population," so there is **no defect-population discriminator observable** between the framework and the GR bounces (both predict no observable defects, for different reasons). This is a genuine framework-exceeding result (it computed something the GR side ignored) that nonetheless yields a null observable. I record it as such rather than inflating it into a falsifier.

**Subtle KZ tension I DID find:** the framework's claim that "Bogoliubov sudden-quench and Kibble–Zurek impulse-matching are the same physics read two ways" (`transit-flow-genesis-to-now.md` line 152) is correct *only* in the sense that both give P_exc=1 in the sudden limit. But KZ's *content* is a defect-density *scaling law* `n ∼ τ_Q^{ν/(1+zν)}`, and in the deep-sudden limit that scaling is degenerate (frozen at ξ₀) — so the framework is invoking KZ in a regime where KZ's signature prediction (the scaling exponent) is *vacuous*. This is not an error, but it means "KZ" in the framework is doing no work beyond the Bogoliubov sudden result; the two descriptions coincide trivially, not informatively. Worth a footnote in the capstone.

### 5.4 Framework-exceeding #1 — the only computed Bogoliubov spectrum

On the *particle-production* axis the framework is unambiguously **more rigorous and more predictive** than both GR programs: it is the only one of the three that writes the mode equation, computes Bogoliubov coefficients, and derives an occupation spectrum (n_k, 59.8 pairs, closed-form GGE, P_exc=1.000). Poplawski uses a free-β bulk source; Gaztañaga uses none. **If the question is "who actually did the non-equilibrium QFT," the framework wins decisively.**

### 5.5 Framework-exceeding #2 — bounce-scale uniqueness

The framework pins tau_fold = 0.190 by a van Hove non-stationarity theorem (S85, PROVEN). The Gaztañaga program gives *two different* bounce densities (nuclear-saturation GeV in 2204 vs sub-nuclear ρ_G in 2602) and Poplawski's bounce scale rides on matter inputs (Ω_S, T_cr). On *bounce-scale determinism* the framework is tighter.

### 5.6 Tension AGAINST the framework — the a(t) / Friedmann leg

**The GR bounces have one structural advantage the framework lacks: an explicit, derived scale factor a(t).** Poplawski's `a(η)` (1111.4595 Eqs.20–22) and Gaztañaga's `a∝cosh(τ/R_B)` are closed-form background solutions. The framework's a(t)/effective-Friedmann mapping is **ASSUMED/BROKEN** (atlas-04 C1: "the mapping from internal modulus to FRW scale factor is not derived from first principles"; the AOFT acoustic frame is conformally *stationary*, giving a 0/0 deceleration). So on the *background expansion history* — exactly the layer where the GR bounces are strongest — **the framework is weaker**, and the GR models can write down a deceleration history the framework currently cannot. This is the honest counter-tension to §5.4–5.5.

### 5.7 Tensions I searched for and did NOT find

- **No torsion analog in the substrate that competes with the van Hove fold.** I checked whether the framework's Dirac operator D_K could be read as sourcing an Einstein–Cartan-like torsion (Poplawski's mechanism is literally Dirac-spin → torsion). The substrate's D_K is block-diagonal, [J,D_K]=0 (CPT), AZ class BDI; its fold is a *spectral-DOS* feature, not a torsion contact term. I found **no hidden torsion bounce** masquerading as the transit — the mechanisms are genuinely different, not the same physics relabeled. (This is a "no-tension-found": the distinctness is clean, not a contradiction.)
- **No GGE/Parker contradiction with the BROKEN "never thermalizes" claim.** I verified the nuance: T2 "GGE forms post-transit" and T7 "transit produces GGE relic" are **PROVEN**; only T3 "GGE *never* thermalizes" is **BROKEN** (it thermalizes at t_therm ~ 6 M_KK⁻¹ = 9×10⁻⁴⁸ t_Hubble — "effectively never on any cosmological clock"). The framework's Parker production (59.8 pairs) is NOT strained by the GR comparison; the GR models simply don't reach this layer. I did not find the corpus straining a closed framework result here.
- **No scale-invariance contradiction on the small-scale / n_s side.** The framework's n_s=0.9561 is consistent with Planck; neither GR bounce predicts a competing n_s value (Gaztañaga keeps a scale-invariant inflationary baseline; Poplawski doesn't compute a spectrum). The only scale-invariance *no-analog* is the large-scale IR cutoff (§5.1), not a small-scale tilt conflict.

---

## 6. Correspondence strength ledger (all rated, with reasons)

| Correspondence | Strength (0–10) | Reason |
|:--|:--:|:--|
| Torsion bounce ↔ van Hove transit (T2, mechanism) | **2** | distinct driver, distinct kinematics (cusp vs sudden), distinct topology (turning-point vs monotone). Surface analogy only |
| Degeneracy bounce ↔ van Hove transit (T2) | **1** | adiabatic cosh vs sudden quench; turning point vs monotone; GeV/sub-nuclear vs M_KK spectral fold |
| Poplawski Parker production ↔ GGE Bogoliubov relic (T-PP) | **2** | citation-level match only; Poplawski has free-β H⁴ source, no spectrum; 4–5 OOM apart in adiabaticity |
| Gaztañaga relics ↔ GGE relic (T10, mechanism) | **1** | classical collapse survivors vs Bogoliubov pairs; no Parker, no Bogoliubov in Gaztañaga |
| Gaztañaga relics ↔ GGE relic (T10, "reheating-substitute relic prediction") | **5** | both replace reheating with a bounce/transit relic + a DM candidate; but opposite candidate kinds, only framework normalizes Ω_DM |
| "Both solve the horizon problem" | **4** | TRUE both do, but by **different physics**: GR via super-fast expansion (v_a~10³²c / cosh inflation); framework via acoustic white hole (causal disconnection by supersonic flow). Same *problem solved*, different *mechanism* |
| Kibble–Zurek shared structure | **3** | only the framework computes KZ; both predict no observable defects but for different reasons; no shared computed object |

**No correspondence in my remit rates above 5.** The bounce/transit pairing is, on every axis I can compute, a **GENUINELY-DISTINCT** relationship rather than a same-structure or GR-shadow-of-substrate relationship.

---

## 7. Carry-forwards (4-field specs; genuine future computation only)

**CF-A2-1 — IR-cutoff no-analog check.**
- **What**: Determine whether the framework's frozen Sasaki–Stewart spectrum admits ANY large-scale (low-k) modification — an IR cutoff, a super-horizon suppression, or a finite-volume effect — that could be compared to Gaztañaga's λ>2R / Q_H=669 CMB large-scale-power-deficit claim. Pre-registered gate: does P_ζ(k) deviate from the frozen-spectrum value by >1% at k < k_horizon-at-fold?
- **Inputs**: frozen-spectrum theorem (B9/C12); k_pivot=14.31 M_KK fold-normalization (S77); transit causal-horizon scale (acoustic white hole, S85).
- **Gate**: PASS if framework predicts a large-scale deficit comparable to 2R-cutoff; FAIL (NO-ANALOG confirmed) if frozen spectrum is exactly scale-invariant to lowest k. Expected: FAIL (confirming the §5.1 no-analog).
- **Effort**: 1 gate, modest (re-use S77 npz + Sasaki–Stewart machinery).

**CF-A2-2 — adiabaticity discriminator as a registered structural result.**
- **What**: Promote the adiabaticity-parameter spread (framework A~8×10⁴ sudden vs Poplawski A~2.7 marginal vs Gaztañaga A≪1 adiabatic) to a registered cross-framework discriminator. The mode-equation A_k is the single number that separates the substrate transit from every GR bounce.
- **Inputs**: dt_transit, T_L, diab_ratio (atlas-04 T1); Poplawski t_0/T_cr (1111.4595); Gaztañaga R_B (2602.17702).
- **Gate**: structural (artifact-existence) — a registry note that "sudden vs adiabatic Bogoliubov" is the falsifiable discriminator, with the computed A-values.
- **Effort**: small; this sub already did the computation.

---

## 8. Top throughlines + sharpest tension (for the lead)

**Throughline 1**: *The "shared Parker pair-production mechanism" between the framework and Poplawski is a citation-level coincidence, not a shared computation.* The framework is the only one of the three programs that writes the mode equation and computes a Bogoliubov spectrum (n_k, 59.8 pairs, P_exc=1.000, closed-form GGE). Poplawski uses a phenomenological free-β H⁴ source for isotropization; Gaztañaga uses no Bogoliubov physics at all (and never cites Parker). On the non-equilibrium-QFT axis the framework decisively exceeds both — but this also *demotes* a correspondence the campaign plan listed as a throughline.

**Throughline 2**: *The three "bounces" are genuinely distinct objects on every axis — mechanism (torsion a⁻⁶ / degeneracy stiff-EoS / van Hove DOS), kinematic character (cusp / adiabatic-cosh / deep-sudden, A spanning ~5 OOM), and topology (turning-point / turning-point / monotone-transit-with-acoustic-white-hole).* The framework's "bounce" is not a temporal turn-around at all; it is a monotone transit whose horizon-problem solution is a *spatial* acoustic causal boundary, not a *temporal* re-expansion. "Torsion bounce ≈ transit" does not survive the mode equation.

**Sharpest tension (single)**: **Gaztañaga 2204.11608's falsifiable large-scale CMB power cutoff at λ>2R (the "anomalous lack of the largest structures", tied to a claimed measured Q_H=669) is a NO-ANALOG the framework cannot match.** The framework's n_s from gauge-invariant spectral geometry has no super-horizon re-entry and no IR causal-horizon cutoff. This is the one place in my remit where a GR bounce model is *more predictive* than the framework on a specific, named, claimed-detected observable — and it is exactly the kind of falsifiable large-scale signature the substrate currently lacks. (Sharpened by the fact that Gaztañaga's *own* relics paper, 2602.17702, contradicts the 2204 large-scale-deficit picture by keeping a standard scale-invariant baseline — so even the GR side is not internally settled on it.)
