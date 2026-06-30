# WP-A v2 — Black-Hole Cosmology ↔ Phonon-Exflation: a Semiclassical-Gravity & Causal-Structure Reading

**Lead**: Hawking-Theorist (Lead A), CORRECTED re-run (v1 discarded — orchestrator-pre-steered).
**Lens**: semiclassical gravity, causal structure, BH thermodynamics, information.
**Mandate**: falsification-first. The deliverable is TENSION, not agreement. Confirmation is cheap (a wrong theory is internally consistent too); tension is informative.
**Framing law** (`phononic-framing.md`): explanations flow substrate → emergent; the substrate is logically prior. This governs the DIRECTION OF EXPLANATION ONLY — it is **not** a licence to conclude "everything is a shadow of the substrate." This document reports framework-contradicting, no-analog, and framework-exceeding findings while writing substrate-first.
**Corpus read**: `downloads/bh-cosmo/black-hole-cosmology/` (19 papers) + `downloads/bh-cosmo/eco-phenomenology/` (15). Coverage: my own reads of #13, #14, #04(Poplawski), #15, #16 + the S42 incursion; recursive subs A1 (causal structure, schwarzschild-penrose-geometer), A2 (bounce/particle-production, transit-dynamics-theorist), A3 (torsion/Dirac, dirac-antimatter-theorist), A4 (corpus digests, general-purpose). Sub artifacts in `sessions/bh-cosmo-incursion/subs/`.

---

## 0. The single most serious tension, stated first

**The framework imports the phrase "we are inside a horizon, causally disconnected pre/post" from exactly the GR literature in this corpus — and that GR literature makes the global causal cut RIGOROUSLY (a two-sided event horizon: Israel junction in Gaztañaga, Einstein-Rosen bridge in Poplawski), while the framework's own follow-up computation FAILED to reproduce a sealed interior.** The S85 acoustic-white-hole theorem (PROVEN) drew a clean bracketed pair of sonic horizons; but `S95-W4-1-WHITE-HOLE-KINEMATIC-CONSISTENCY` returned **FAIL** with `N_zeros=1; C1_structure=ASYMMETRIC_open_exit; monotone_supersonic_exit=True` (canonical, `computations/session-95/s95_gate_verdicts.txt`). There is ONE sonic crossing and the exit is open and asymmetric. So the framework's causal disconnection survives only in the weak, one-directional Unruh sense, while the corpus models seal their interiors with genuine global structure. **This is the place where the GR program is strictly more rigorous than the framework about the very claim the framework borrows from it.** [via schwarzschild-penrose-geometer, F1]

That is the headline. The body below builds the structure that locates it and four other tensions of comparable weight.

---

## 1. My classification scheme — the corpus splits on ONE axis the framework collapses

Reading the 34 papers, the organizing axis is **what kind of object the boundary/horizon IS, and what crosses it**. I classify every paper by its answer to: *is the cosmologically-relevant horizon (i) a future event horizon (ingoing, black), (ii) a past horizon (outgoing-blocked, white), (iii) a static causal boundary (de Sitter / GHY), or (iv) a material condensate surface (no true horizon)?* The framework collapses (i)–(iv) into one acoustic phase-boundary; the corpus keeps them distinct, and the distinctions are load-bearing.

| Class | Corpus members | Boundary IS | What crosses | Framework's object |
|:------|:---------------|:------------|:-------------|:-------------------|
| **C-FUTURE (black)** | Poplawski #03–07,09–11,18; Gaztañaga #12–14; Easson-Brandenberger #01 | future event horizon, formed by collapse | matter falls IN, nothing out; arrow of time set by inward flux | — (framework's genesis is NOT a collapse) |
| **C-PAST (white)** | — (none on the GR side place US inside a white hole) | past horizon | matter blocked from coming IN | **the framework's S85 acoustic WHITE hole at τ_fold** |
| **C-STATIC (dS/GHY)** | Gaztañaga #13 (Λ = GHY boundary term, r_S = r_Λ) | static causal boundary = trapped surface at r_Λ | outgoing null geodesics freeze | the framework's CC is a₀ BULK moment, NOT a boundary |
| **C-SURFACE (no horizon)** | ECO cluster #01–15 (gravastars, ClePhOs) | material condensate surface at r_g(1+ε) | partial reflection → echoes; no absorption | framework's "horizons-as-acoustic-phase-boundaries" reading |

**Throughline T1 — Orientation inversion (the deepest structural finding).** Every GR universe-in-BH model places the observable region inside a **future, black, ingoing** horizon. Gaztañaga: "the FLRW metric is inside a trapped surface … nothing can come out of a BH … the expansion comes to a halt." Poplawski: matter flux through the horizon is **unidirectional inward** and *defines* the arrow of time. The framework's S85 cosmogenesis is the **time-reverse**: an acoustic **white** hole (past-type, outgoing-blocked, anti-trapped), formed by a *phase transition* not a collapse; τ=0 is the framework's own "dynamically repulsive white hole." **These are not the same causal object — they are time-reverses.** [via schwarzschild-penrose-geometer]
- *Consequence:* the framework should NOT borrow "we are inside a black hole" rhetoric from this corpus. The corpus's black-hole interior and the framework's white-hole genesis share the word "horizon" and nothing of orientation. Strength of the correspondence the framework might want here: **WEAK / inverted** (≈2/10).

**Throughline T2 — Three problems, three non-inflationary solutions, three different mechanisms.** All of Poplawski, Gaztañaga, and Easson-Brandenberger solve horizon+flatness+structure WITHOUT inflation — and the framework also claims no inflation (exflation = internal spectral complexification). But the *mechanisms are mutually distinct*:
- Poplawski: torsion-driven brief super-fast expansion (`v_antipodal ~ 10³² c`!) makes Ω→1 via the â⁴ scaling, with `Ω_S ≈ −10⁻⁶⁹`.
- Gaztañaga: super-horizon perturbation re-entry from the *collapse* phase, with a **finite-size cutoff** at λ>2R.
- Framework: a *spatial* acoustic white hole disconnects pre/post; n_s=0.9561 from gauge-invariant spectral geometry (no temporal re-expansion).

The shared *conclusion* ("no inflation needed") is real and is a genuine cross-program convergence at the level of **what the data demands**. But "no inflation" is a negative claim shared by a dozen bounce programs — it is NOT evidence of structural correspondence between any two of them. Strength as a correspondence: **MODERATE as convergence, WEAK as identity** (≈3/10).

---

## 2. The cosmological-constant collision — bulk moment vs boundary term

This is the sharpest *conceptual* contradiction in the corpus, and it is clean.

**Gaztañaga (#13, Symmetry 2022):** Λ IS a Gibbons-Hawking-York **boundary** term. The on-shell action for a perfect fluid inside a BH reduces to a boundary term `S_on-sh = ⟨Λ/(4πG) − (ρ+3p)⟩V₄`; requiring it to vanish forces `Λ = 4πG⟨ρ+3p⟩` — "Λ is just given by the matter content inside the boundary." Equivalently, evolution inside a BH event horizon *induces* a Λ term in the EFE "even when there is no Λ to start with," via the GHY term with `r_Λ = r_S`. **Λ is codimension-1 (a surface term), parameter-free, and solves the coincidence problem for free** (Λ ~ ρ_matter by construction).

**Framework:** CC is the **a₀ zeroth Seeley-DeWitt BULK moment** = `6440 M_KK^{d-4}` (canonical, `a_0_FW_zeta`, S88); `w0_FW = −0.918` from the Volovik vacuum partition + effacement (S58). This is codimension-0 (a bulk spectral integral over D_K eigenvalues), and it is a *different spectral moment* than gravity (a₂).

**T3 — Λ-as-boundary vs Λ-as-bulk-moment is a genuine differential-geometric contradiction about what kind of object the cosmological constant is.** [via schwarzschild-penrose-geometer, sharpened here]
- Gaztañaga's construction is, on the narrow question of *the numerical value of Λ*, **more predictive** than the framework's: he derives `Λ = 3/r_S²` parameter-free and gets the coincidence problem gratis. The framework's a₀ = 6440 is a bulk number that overshoots the observed Λ by the canonical ~10¹²⁰ hierarchy and requires the *separate* DILUTION-CC / Volovik-tracking machinery (closed S66) to land `w0_FW = −0.918`.
- **BUT** — and this is decisive — **the framework's own S42 incursion already adjudicated this and found the boundary route does NOT survive.** The incursion (`sessions/framework/Collabs/blackhole-cosmology-incursion.md`, §I.3, Volovik) tested whether the GHY boundary term could serve as the q-theory external pressure `P_ext` and concluded: *"No — wrong scaling, fine-tunes M_BH"* (HIGH confidence). P_GHY ~ 1/M_BH gives 10⁻⁹⁴ Pa for a universe-mass BH vs the needed 10⁻¹⁰ Pa — off by 84 orders. So the framework has *already* rejected exactly Gaztañaga's mechanism on dimensional grounds, and replaced it with a bulk self-tuning whose fixed point is Λ*=0 (§I.5).
- **Net adjudication:** this is NOT "Gaztañaga is right and the framework is wrong." It is two incompatible theories of what Λ is, where (a) Gaztañaga is more predictive on the value but rests on a global-topology assumption (k=Λ=0 chosen, not derived — he concedes "any choice other than Λ=k=0 would require some justification outside GR"); (b) the framework is less predictive on the value but the boundary route was tested internally and *failed its own scaling check*. **The two cannot both be right about Λ's geometric nature.** Strength of any "Λ-correspondence" between corpus and framework: **CONTRADICTION, ≈1/10** — they disagree at the level of codimension.

**T3-corollary — the S42 incursion is partially superseded by this corpus, and should be flagged.** The incursion's §I.5 "symmetric fixed point Λ*=0" was already corrected in §I.10 (the "faucet" accretion source breaks the symmetry; J/Λ_obs ~ 10⁻¹⁹, negligible for self-similar recursion). The incursion did NOT have Gaztañaga's #13 GHY-boundary derivation in front of it as a competing *first-principles* Λ-origin (it cited the earlier MNRAS 2021 "zero action boundary" paper but not the cleaner Symmetry 2022 statement). The incursion's conclusion ("BH cosmology adds initial conditions, not a CC mechanism") **survives** — but its dismissal of the boundary route as "fine-tuning in disguise" is *strengthened*, not weakened, by Gaztañaga's own admission that he assumes the global topology. No retraction needed; the incursion's verdict holds and is reinforced.

---

## 3. The bounce — three distinct mechanisms, and the adiabaticity discriminator that kills the "shared Parker" story

**T4 — The three "nonsingular bounces" are genuinely distinct on every axis, and the framework's transit is the only one with a computed Bogoliubov spectrum.** [via transit-dynamics-theorist]

| | Poplawski torsion bounce | Gaztañaga degeneracy bounce | Framework transit |
|:--|:--|:--|:--|
| Driver | spin-fluid `ε_S = −κs²/4 ∝ a⁻⁶` (negative, repulsive only above nuclear ρ) | Pauli/neutron-degeneracy at GeV (SN-like rebound) | van Hove spectral fold (DOS), dS/dτ=+58,673 |
| Character | quasi-adiabatic approach to finite â_m | adiabatic cosh | **supersonic / impulsive** (Mach 13.75) |
| a(t) at bounce | closed-form, has turning point | closed-form, has turning point | **monotone** (dS/dτ>0 throughout; NO turning point) |
| Horizon-problem fix | temporal (re-expansion) | temporal (re-entry) | **spatial** (acoustic white hole) |
| Adiabaticity A=(bg rate)/(mode freq) | A ~ 2.7 (marginal cusp) | A ≪ 1 (deep adiabatic) | **A ~ 8×10⁴ (deep sudden)** |

The adiabaticity parameters span ~5 orders of magnitude. **"Torsion bounce ≈ transit" does not survive writing the mode equation.** [via transit-dynamics-theorist, computed]

**T5 — The "shared Parker pair-production mechanism" is a citation-level coincidence, not a shared computation.** This DEMOTES a correspondence the campaign frame would naturally reach for. [via transit-dynamics-theorist]
- Poplawski's "Parker production" (1007.0587, 2008.02136) is a *phenomenological bulk source* `~ βH⁴/c⁴` with a free coefficient β whose job is isotropization + a *tuned* inflation epoch — **no β_k, no mode-by-mode spectrum.** He cites Parker 1969 / Zel'dovich 1970 but does not compute a Bogoliubov coefficient.
- Gaztañaga uses **no** Bogoliubov physics and never cites Parker; his relics are classical collapse survivors.
- The framework is the *only* one of the three that writes the mode equation and computes a Bogoliubov spectrum (GGE: 59.8 pairs, P_exc=1.000, closed-form). Crucially the kinematic regimes differ (impulsive vs adiabatic), so even if Poplawski computed a spectrum it would be a *different* spectrum.
- Strength of "shared Parker mechanism": **WEAK, ≈2/10.** Both invoke gravitational/background pair creation; only the framework does the calculation. (Stale-lore guard, verified: the GGE *relic formation* is PROVEN — T2/T7 — but "GGE never thermalizes" is BROKEN, atlas-04 T3, t_therm≈6 M_KK⁻¹; the relic still forms, the permanence claim was retracted. The correspondence above is to relic *formation*, which stands.)

**T6 — Kibble-Zurek is a framework-exceeding-but-null result.** The framework *computed* KZ (S38: 0D regime, L/ξ=0.031, π₀(G/H)=0, no domain walls); none of the bounce papers compute a defect spectrum at all. But the framework's conclusion is "no observable defects," so it yields no defect-population *discriminator*. The framework is more rigorous here (it did the computation), but the result is a null — neither a tension nor a usable correspondence. [via transit-dynamics-theorist]

---

## 4. Torsion — the structural NO-ANALOG, and the arrow-of-time tension

**T7 — Einstein-Cartan spin-sourced torsion has NO substrate pre-image. This is the cleanest no-analog in the corpus.** [via dirac-antimatter-theorist]
- Poplawski's entire program rests on the **Cartan equation**: torsion `S^k_{ij} ∝ s^k_{ij}` is a *dynamical response to fermion spin density*. The quartic contact term `−κ²s²` gives the negative `ε_S ∝ a⁻⁶` that does ALL the work (bounce, flatness, horizon, UV cutoff).
- The framework's D_K on Jensen-deformed SU(3) has spin (it acts on spinors) but its connection's antisymmetric part is a **fixed geometric datum** set by the su(3) structure constants `f_{abc}(τ)` — there is **no equation in the framework where fermion occupation sources the connection.** The substrate runs geometry→matter; ECKS requires the forbidden matter-spin→torsion→geometry arrow.
- The disanalogy is theorem-backed, not naive: the framework *studied* torsion (Gate T-1, S26) and found it torsion-free by construction; the physical work torsion does in ECKS is done by an *independently-verified, different* mechanism (the spectral fold).
- Severity: **HIGH as a no-analog; LOW as a defect** (it is a deliberate design choice). The single DOF that powers the entire UIBH torsion program is structurally absent from the framework. Anyone claiming "Poplawski's universe-in-BH supports the framework" is wrong: the framework cannot host Poplawski's mechanism. [via dirac-antimatter-theorist]

**T8 — `[J,D_K]=0` (CPT, PROVEN) is cosmologically SILENT on the arrow of time, and both programs' arrows are boundary-condition arrows on reversible dynamics.** [via dirac-antimatter-theorist, F3]
- Poplawski's ECKS is T-symmetric; his cosmic arrow is carried *entirely* by the one-way matter flux through the parent horizon — a boundary condition.
- The framework advertises CPT-exactness as load-bearing, but its cosmic arrow is carried *entirely* by the Ordered-Veil diabatic transit-freeze — and `S_ent=0` reveals that to be **a boundary-condition arrow on UNITARY (reversible) dynamics**, structurally the *same kind* of arrow Poplawski gets. `[J,D_K]=0` constrains the spectrum, not the boundary data; CPT-exactness is *compatible* with the transit arrow but does not *explain* it.
- Tension: the framework's two arrows (CPT-hardwired vs transit-boundary) should be **scoped separately**; "CPT hardwired" is carrying cosmological weight it does not bear. This is a hygiene tension internal to the framework's self-description, surfaced by comparison to ECKS. Strength: real, **MODERATE** — it does not contradict a computed result but it corrects an overclaim.

---

## 5. Cosmological coupling — the boldest empirical claim, squeezed from BOTH sides

The Croker→Farrah→Rodriguez thread (#08, #15, #16) is where this corpus is most observationally live, and it is **falsification in action**.

**The claim (Farrah #15, 2023):** BH gravitating mass grows as `M ∝ a^k` with measured `k = 3.1 ± 0.76` (zero coupling excluded at 99.98%), consistent with `k=3` = vacuum-energy-interior BHs. The continuity equation then makes such BHs contribute *as vacuum energy*; BH production from cosmic SFH gives Ω_Λ. **Stellar-remnant BHs ARE dark energy.**

**The two-sided squeeze:**
- **Observational (Rodriguez #16, 2023):** the two confirmed BHs in globular cluster NGC 3201 (ages 11.5 Gyr, z_form≈2.8, masses 4.5 + 7.7 M_⊙) **exclude k=3.** A k=3 growth of (1+z)³≈55 would require either both BHs born below the maximum neutron-star mass (2.2 M_⊙, where BH formation is excluded) or both binaries face-on (P<10⁻⁴, and <10⁻⁶/<10⁻⁹ including the third candidate). k≥2.5 excluded at 4×10⁻⁵.
- **Theoretical (Poplawski #17, CQG 2025, gr-qc — peer-reviewed):** the McVittie self-consistency analysis shows a BH embedded in expanding FRW pins to the Hubble flow and does **NOT** grow with expansion. The *theory side of the same UIBH program* falsifies the k~3 dark-energy hypothesis. [via general-purpose, A4]

**T9 — The framework's DILUTION-CC is the substrate-side cousin of cosmological coupling, but Rodriguez's falsification does NOT touch it — and this asymmetry is itself the finding.**
- The framework's dark energy is Volovik vacuum tracking (DILUTION-CC, closed S66, ρ_vac/ρ_obs = 1.032), NOT astrophysical-BH mass growth. The framework does **not** predict `M_BH ∝ a³` for stellar-remnant BHs.
- Therefore the NGC 3201 + Cygnus-X-1 constraints that kill Farrah's k=3 leave the framework's DE mechanism untouched. **This is a place where the framework is SAFER than the boldest GR-side DE claim — but only because it makes a weaker, less directly-testable prediction.** The framework's DE is tied to the *vacuum* (a₀/Volovik partition), not to a population of objects you can weigh in a globular cluster. That is an honest asymmetry: less falsifiable, hence less exposed. Strength of "cosmological-coupling ↔ DILUTION-CC" correspondence: **WEAK structural cousinhood, ≈3/10** (both tie DE to BH/vacuum physics; mechanisms and falsifiability differ sharply).
- *Falsification searched-for-and-NOT-found:* I checked whether any framework prediction requires BH masses to grow with `a` (which Rodriguez would then kill). It does not. The framework is *not* in tension with Rodriguez. Auditable null.

---

## 6. Smolin CNS and the falsifiability gap

**T10 — Smolin's Cosmological Natural Selection contains the single sharpest falsifiable number in the entire corpus, and the framework has no analog of its predictive logic.** [via general-purpose, A4]
- CNS (#02): BH bounces produce offspring universes with slightly varied constants; selection drives the constants to a local **maximum of BH production**. The kill condition: the strange-quark mass can be tuned to set the neutron-star upper mass limit *without* disturbing massive-star formation, so CNS predicts NS are kaon-condensate stars capped at **M_uml ≈ 1.6 M_⊙**. **A single well-measured neutron star above ~1.6 M_⊙ falsifies CNS.** (Status: PSR J0740+6620 is 2.08±0.07 M_⊙ — already in tension; this is exactly the kind of clean single-observation kill CNS was designed to expose itself to.)
- The framework has *recursive-cosmology lore* (project_cosmic-reproduction: measurement = vacuum decay = baby universe) but **no analog of CNS's selection-prediction structure** — it does not predict that any constant sits at a BH-production extremum, and it has no equivalent single-number kill condition tied to the recursive structure.
- **This is a place where a GR-side program (CNS) is more falsifiable than the framework's analogous lore.** The framework's strength is elsewhere (zero-free-parameter geometric outputs like m_H, n_s); but on the *recursive-universe / baby-universe* axis specifically, Smolin exposes a sharp prediction and the framework exposes none. Strength: this is a **framework-exceeding finding on the GR side** — flag it as a gap, not a tension with a computed result.

---

## 7. ECO phenomenology — the GR-side horizon-vs-surface toolkit (and why it is NOT a live framework gate)

The ECO cluster (#01–15) is the observational laboratory for "true horizon vs condensate surface." It is structurally adjacent to the framework's "horizons-as-acoustic-phase-boundaries" reading, but **the framework's own GW-channel falsifiers are RETIRED** (walls=0 EXACT, S96; falsifier migrated GW→LSS, inventory Rows #71/#72). So this cluster informs GR-side discrimination and the structural-analogy map, NOT a live framework gate. Recorded for completeness and for any *future* substrate-side compact-object falsifier design. [via general-purpose, A4]

- **#04 Chirenti-Rezzolla (KEY negative result):** GW150914's ringdown CANNOT be a rotating gravastar — the ℓ=2=m axial QNM eigenfrequencies of rotating gravastars never overlap the Kerr `a=0.68` ringdown, for all compactness/thickness. A specific condensate-surface remnant is *already excluded* by data.
- **#08 Cardoso-Pani (the central tool):** the echo-delay relation `τ_echo ~ (2r_g/c)|log ε|`. The LOGARITHMIC dependence means even Planckian surface corrections (ε~10⁻⁴⁰) give an *observable* echo delay; LISA sees ≥1 event/yr for 20% echo energy. BH Love numbers are exactly zero (null test); horizons absorb (tidal heating null test). **"BHs exist" is unfalsifiable, but alternatives can be killed by one observation.**
- **#15 Destounis et al.:** the fundamental QNM of *ultra-compact* ECOs is environment-ROBUST; overtones are spectrally FRAGILE ("spectrally fragile yet modally robust"). **Design lesson for any future substrate compact-object falsifier: target the fundamental ringdown mode, not overtone hierarchies.** This parallels the framework's own pseudospectrum cautions (Kitaev integrability, ⟨r⟩=0.367).

**T11 — The ECO toolkit is a framework-exceeding observational program with NO current substrate analog, AND the framework has voluntarily exited the arena.** The framework retired its GW falsifiers; this corpus is a mature, LISA-ready discrimination program. If the framework ever wants a *live* compact-object falsifier, this cluster is the template (and #15 says: use the fundamental mode). Until then, the correspondence is **dormant by the framework's own choice**, ≈ N/A as a live gate.

---

## 8. FALSIFICATION SECTION (consolidated)

### 8.1 Tensions / contradictions / no-analogs / framework-exceeding (ranked by severity)

| # | Finding | Type | Severity | Anchor |
|:--|:--------|:-----|:---------|:-------|
| **F1** | Framework's "sealed causal disconnection" claim is NOT stable under its own follow-up: `S95-W4-1` FAIL (`N_zeros=1, ASYMMETRIC_open_exit`). GR models (Israel junction, ER bridge) make the global cut rigorously; framework gets only one-directional Unruh disconnection. **GR strictly more rigorous on the borrowed claim.** | framework-exceeded-by-GR + internal overclaim | **HIGHEST** | S95 verdict file (FAIL); S85 theorem (PROVEN); [A1] |
| **F2** | Λ-as-GHY-boundary (Gaztañaga, codim-1, parameter-free, coincidence-problem-free) vs Λ-as-a₀-bulk-moment (framework, codim-0, 6440 M_KK^{d-4}). **Genuine geometric contradiction** about what Λ IS. Gaztañaga more predictive on the value; framework's boundary route already failed its own scaling check (S42 §I.3). | contradiction (mutually exclusive) | **HIGH** | Gaztañaga #13; S42 incursion §I.3; a_0_FW_zeta; [A1] |
| **F3** | Einstein-Cartan spin-torsion (the DOF doing ALL Poplawski's work) has NO substrate pre-image — framework is torsion-free by construction (no Cartan equation; geometry→matter only). | no-analog (structural) | **HIGH** | Poplawski #04,#06,#18; Gate T-1 (S26); [A3] |
| **F4** | Gaztañaga #14's falsifiable large-scale CMB power cutoff at λ>2R (k<π/R; claimed observed as the low-ℓ deficit) is a **NO-ANALOG the framework cannot match** — n_s from spectral geometry has no super-horizon re-entry, no IR causal-horizon cutoff. GR bounce more predictive on a named observable. | framework-exceeded-by-GR | **HIGH** | Gaztañaga #14; [A2] |
| **F5** | Smolin CNS predicts NS mass ceiling ≈1.6 M_⊙ (single-observation kill); framework's baby-universe lore has NO analogous falsifiable prediction. GR program more falsifiable on the recursive-universe axis. | framework-exceeded-by-GR (falsifiability gap) | **MODERATE-HIGH** | Smolin #02; [A4] |
| **F6** | Framework's a(t)/effective-Friedmann leg is BROKEN/ASSUMED (T6 Friedmann-BCS lock, 133,200× shortfall; S98-W2-2 FAIL, AOFT conformally-stationary 0/0) — exactly the *background* layer where every GR bounce writes closed-form a(t). The honest counter-tension: on cosmological *dynamics*, the GR side is developed and the framework's is broken. | framework-exceeded-by-GR | **MODERATE-HIGH** | atlas-04 T6 BROKEN; S98 verdict file; [A2] |
| **F7** | "CPT (`[J,D_K]=0`) hardwires the arrow of time" — but the cosmic arrow is a boundary-condition arrow on *unitary* (S_ent=0) dynamics, same kind ECKS uses. CPT is silent on it. Internal overclaim surfaced by comparison. | internal overclaim | **MODERATE** | [A3]; J-D_K=0 PROVEN |
| **F8** | "Shared Parker pair-production" (Poplawski ↔ framework GGE) is citation-level only: Poplawski has a free-β bulk source, no β_k; framework is the only one that computes a Bogoliubov spectrum. Adiabaticity differs by ~5 OOM (A~2.7 vs ~8×10⁴). | weak/demoted correspondence | **MODERATE** | [A2], computed |
| **F9** | Cosmological-coupling k=3 (Farrah, the boldest GR DE claim) is killed BOTH observationally (Rodriguez NGC 3201, P<10⁻⁴) AND theoretically (Poplawski #17 McVittie, no growth). The framework's DILUTION-CC survives only because it makes a weaker, less-testable (vacuum-tied) prediction. | asymmetry (framework safer-but-less-falsifiable) | **MODERATE** | Farrah #15; Rodriguez #16; Poplawski #17; DILUTION-CC S66 |
| **F10** | Internal GR-side inconsistency: Gaztañaga #19 (relics) keeps a *standard scale-invariant baseline*, contradicting #14's large-scale-deficit headline. Even the GR program isn't settled — weakens F4's "GR more predictive" to "GR makes a sharper but internally-contested claim." | corpus-internal contradiction | **NOTE** | Gaztañaga #14 vs #19; [A4] |

### 8.2 Tensions I searched for and did NOT find (auditable absences)

1. **Does any framework prediction require BH mass growth `M ∝ a^k`?** — NO. Checked DILUTION-CC, Leggett-channel DM, the falsifier inventory. The framework's DE is vacuum-tracking, not object-mass-growth. ⇒ Rodriguez #16 does NOT falsify the framework. (Auditable null; this is *why* F9 is an asymmetry, not a direct hit.)
2. **Does the framework's CC-as-a₀ contradict the S42 incursion's "BH cosmology adds initial conditions only"?** — NO. The incursion's verdict (boundary route fails on scaling; fixed point Λ*=0; faucet correction J/Λ_obs~10⁻¹⁹ negligible) is *reinforced*, not strained, by Gaztañaga #13's own concession that he assumes global topology. No retraction of the incursion needed. (Checked specifically because I was told to challenge closed results; this one holds.)
3. **Is the S85 acoustic-white-hole theorem itself falsified by the corpus?** — NO. The theorem (causal disconnect formalized) stands as proven; what FAILED is the *stronger* S95 kinematic-consistency follow-up (sealed two-sided interior). The corpus does not touch the S85 theorem's actual content (one-directional disconnect); it exposes that the *capstone language* overstated it. So F1 is a language/scope tension, not a refutation of S85.
4. **Does Poplawski's torsion UV-cutoff correspond to the framework's M_KK cutoff?** — Searched (A3). NO meaningful correspondence: "both theories have a UV scale" is cheap. Poplawski's cutoff is a *consequence of the spin-spin contact term*; the framework's M_KK is a *compactification scale*. Different origin, coincidental co-existence. Auditable null. [A3]
5. **Is there a substrate analog of Smolin's BH-production-maximization selection?** — NO. Searched the recursive-cosmology lore; the framework has "baby universe = vacuum decay" but no variational selection principle on constants. Genuine gap (F5), not a hidden correspondence.

### 8.3 The genuinely-strong correspondences (reported because the mandate requires honesty in both directions)

These survived the falsification hunt as *real* — I rate them and say why:
- **Weyl-curvature-hypothesis compliance (≈6/10 — the strongest real match).** Poplawski's FLRW interior has Weyl C=0 exactly; the framework's genesis τ=0 is the WCH minimum (|C|²=5/14, conformally-flat slice) with S96 proving |C|² grows monotonically. Both are Penrose-WCH-compliant: low Weyl at the start, growing with clumping. [A1] Caveat: framework is "minimal-nonzero," Poplawski "exactly zero" (Type O impossible by SU(3) structure constants) — so it is a *qualitative* match (low-and-growing Weyl), not a numerical identity.
- **Boundary-condition arrow of time (≈5/10).** Both Poplawski's one-way-horizon arrow and the framework's transit-freeze arrow are boundary-condition arrows on reversible dynamics (T-symmetric ECKS / unitary transit). This is a real *structural* parallel — and it is the basis of F7 (it shows the framework's "CPT hardwires the arrow" is the overclaim). [A3]
- **"No inflation needed" convergence (≈3/10 as identity, higher as convergence).** Genuine cross-program agreement on what the data demands, but a negative claim shared by many bounce models — convergence, not correspondence.

---

## 9. What this means for the constraint map (substrate-first)

Writing strictly substrate-first (the substrate is logically prior; these GR models are GEOMETRIC-class laboratory-IN analogs):

- The substrate's genesis (first-order van Hove transit, supersonic, diabatic, monotone-S) is **mechanistically distinct from every bounce in this corpus** and is logically prior to all of them. The corpus does NOT supply a substrate mechanism; it supplies emergent-GR pictures that the substrate would have to *reproduce downstream* via the a₂ Seeley-DeWitt coefficient — and that reproduction (the a(t)/Friedmann map) is exactly the framework's BROKEN leg (F6).
- The corpus's value to the framework is **not confirmation** — it is a set of precise GR constructions that expose (i) where the framework's *causal* language outruns its computation (F1), (ii) where the framework's *Λ* is a different geometric object than the most predictive GR alternative (F2), (iii) a DOF the framework structurally lacks (F3, torsion), and (iv) named observables (large-scale CMB cutoff F4, NS mass ceiling F5, echoes/Love numbers §7) where GR-side programs are more predictive or more falsifiable than the framework on the same physics.
- The one durable structural correspondence is the Weyl-curvature hypothesis (low-and-growing Weyl from genesis), which is substrate-first-compatible: the framework's |C|² growth is DERIVED from D_K spectral structure (S96), and Poplawski's C=0 interior is the emergent-GR shadow of the same "smooth start, clumpy later" content.

---

## 10. Recommendations (NOT carry-forward computations — this is an investigation WP)

These are *findings routed for adjudication*, per the falsification mandate. They are not pre-registered gates.

1. **Capstone/`phononic-framing.md` language down-tag (F1).** "Sealed causal disconnection / pre-post causally disconnected" should be scoped to "one-directional Unruh-type acoustic disconnection" to match the S95 FAIL (`ASYMMETRIC_open_exit`). The capstone-hygiene 5-question gate (Q3: PROVEN/CONDITIONAL/BROKEN status change) is triggered by this WP touching the §7 falsifier surface and the S85/S95 status. Route to `mack-cosmic-bridge` (§7 sole writer) + capstone designated writer. **This is the single highest-value action from the incursion.**
2. **Scope `[J,D_K]=0` away from the arrow of time (F7).** In capstone prose, separate "CPT-exact spectrum (`[J,D_K]=0`, PROVEN)" from "cosmic arrow (transit-boundary condition on unitary dynamics)." The former does not explain the latter.
3. **Record the cosmological-coupling asymmetry (F9) in the falsifier inventory as a NULL-by-mechanism row:** the framework is NOT falsified by NGC 3201 / Cygnus-X-1 because it does not predict `M_BH ∝ a³` — and note that this safety comes from a *weaker* (vacuum-tied, less-testable) DE prediction than Farrah's.
4. **If a live substrate compact-object falsifier is ever wanted (the framework retired GW):** the ECO toolkit (§7) is the template, and #15's lesson is binding — target the *fundamental* ringdown mode (environment-robust), not overtones (spectrally fragile).
5. **The S42 incursion needs no retraction** but should gain a one-line cross-reference to Gaztañaga #13 (GHY-boundary Λ) noting that the boundary route's failure is *reinforced* by Gaztañaga's own global-topology concession.

---

## Appendix — sub-investigation artifacts (verified on disk)

- `subs/sub-A1-causal-structure.md` (388 lines) — schwarzschild-penrose-geometer: orientation inversion, Weyl-hypothesis match, F1 (S95 FAIL), Λ codimension contradiction.
- `subs/sub-A2-bounce-particle-production.md` (255 lines) — transit-dynamics-theorist: three distinct bounces, adiabaticity discriminator (computed), Parker demotion, Gaztañaga CMB-cutoff no-analog, KZ null, a(t) BROKEN counter-tension.
- `subs/sub-A3-torsion-dirac.md` (390 lines) — dirac-antimatter-theorist: torsion no-analog (no Cartan equation), CPT-silent-on-arrow (F3/F7), torsion-UV-cutoff null.
- `subs/sub-A4-corpus-digests.md` (252 lines) — general-purpose: Easson-Brandenberger #01, Smolin CNS #02 (NS mass ceiling), Poplawski #17 McVittie (no BH growth — theory-side k=3 falsifier), Gaztañaga #19 relics (contradicts #14 baseline), ECO cluster #04/#08/#15.

**Corpus papers read in full and cited:** Gaztañaga #13 (2202.00641), #14 (2204.11608); Poplawski #04 (1007.0587); Farrah #15 (2302.07878); Rodriguez #16 (2302.12386); + via subs: Poplawski #03/#06/#07/#17/#18, Easson-Brandenberger #01, Smolin #02, Gaztañaga #12/#19, ECO #04/#08/#15. Framework anchors: S42 incursion, S85 W6-1/W6-4, S95-W4-1 (FAIL), S96 Weyl, atlas-04 T6 (BROKEN), S98-W2-2 (FAIL), DILUTION-CC (S66), a_0_FW_zeta, w0_FW, tau_fold — all queried via knowledge MCP.
