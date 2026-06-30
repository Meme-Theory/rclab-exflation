# WS-S112-6 OBSAXIS — Round 1

**Workshop**: WS-S112-6 OBSAXIS (Session 113 EVOI-frontier campaign)
**Agent**: nazarewicz-nuclear-structure-theorist — Round 1, steelman **Reading A** (NICER dense-matter EoS / pulsar mass–radius axis)
**Pole**: Reading A. Opponent (mack-cosmic-bridge) holds Reading B (DESI/Euclid f·σ8 growth). I have not seen their work.

**One-line thesis**: The dense-matter / NICER axis is the higher-EVOI next falsifiable substrate prediction *not* because the substrate cleanly predicts a 2 M_⊙ neutron star — it manifestly does not — but because the substrate already produces a full interior EoS pipeline (CFL diquark gap → P(ρ) → TOV → M–R, compactness) that has been run twice and lands a *catastrophically falsified* mass–radius relation; that pipeline's existing FAIL is a sharper, more pre-registrable, more decision-relevant gate against a fixed-by-2030 dataset (NICER J0740/J0030 + the M–R credible regions) than any growth-suppression prediction the LSS sector can currently mount. The leverage is in closing a *live, dimensionful, already-failing* corridor on the framework's one weak flank — not opening a new clean one.

---

## 0. Method: governing structure first

Per my standing methodology and the framing law, I begin with the governing structure, classify the problem within established theory, and only then assess EVOI/tractability. I queried the knowledge MCP before computing (`search_knowledge`, `trace_entity`, `get_constant`); every numerical anchor below is pinned to a verdict line or canonical constant. I did **not** re-run any gate — the relevant gates are already on disk.

The dense-matter axis sits on the framework's **one dimensionful axis**. The §VII.BS rank-1 NNU theorem (STAGE-3-PERMANENT, `second_rel_sv = 1.066e-17`) proved every dimensionful substrate observable factors as `O = w·Ô` with a single un-fixed weight `w = M_KK = 7.428660e16 GeV` (`get_constant("M_KK")`, gate CONST-FREEZE-42). The recurring sign-PASS / magnitude-FAIL signature across A_s, the CC magnitude, the compact-object R/M, the LRD temperature, and the fermion masses is *that one keystone weight seen from many sides* (S110-W3 plan §"Wave 3 Summary"). The compact-object sector is the locus where this weak flank becomes an **observable that a satellite already in orbit measures to ~5% precision**. That is the whole EVOI case, and I will make it structurally, then test it against tractability honestly.

---

## 1. Does the substrate actually PREDICT a dense-matter EoS or an M–R relation?

**Yes — the governing equations exist and are instantiated.** This is the first place the neutral "CORPUS-EXCEEDS: the framework has NO compact-object sector" framing must be sharpened. It is true that the framework has no *formation channel* and no *exterior self-bound M–R from a hydrostatic surface*. It is **false** that there is no interior EoS. The chain is on disk:

**Governing structure (substrate-first).** A compact object in this framework is not dense matter sitting IN a spacetime well; it is an emergent localized concentration of the substrate's spectral content. The arrow is:

```
D_K eigenvalues at finite chemical potential μ
  → BdG / CFL diquark gap  Δ(μ)   (a pairing instability of the phononic spectrum)
  → CFL equation of state  P(ρ)    (Legendre transform of the self-consistent free energy)
  → TOV mass–radius sequence       (standard hydrostatic structure)
  → M_max, compactness C, M(R)
```

This is precisely the structure of nuclear DFT for neutron-star matter (my home domain), with the substrate's CFL diquark condensate playing the role the BCS neutron pairing gap plays in conventional crust/core physics. The framework even has the *correct high-density phase* as a PROVEN structural result: **CFL (Color-Flavor-Locked)** dense QCD is in the permanent-results registry — "high-density QCD matter at μ_QCD ≳ 1 GeV where SU(3)_c × SU(3)_{L+R} locks to a diagonal SU(3)." The SU(3) the framework is built on is the *same* SU(3) that color-locks in CFL. This is not a forced analogy; it is the substrate's native dense phase.

**Instantiations already computed (the pipeline runs).**

| Gate | Verdict | Key numbers | What it establishes |
|:-----|:--------|:------------|:--------------------|
| `INV13-W2-1-FINITE-MU-CFL-EOS` | **FAIL** | `M_max_FW = 0.1631 M_⊙`; band [2.0, 2.6]; `Δ_CFL plateau = 2.4107 M_KK`; `dΔ/dμ > 0` (sign=PASS); `Δ/μ = 4.8213` (runaway) | The substrate's diquark pairing has the **correct density-dependence** (dΔ/dμ > 0 at every scan point — sign=PASS, substitution-chain-predicted). The EoS is too soft: M_max ≈ 12× below the 2 M_⊙ pulsar bound. magnitude=FAIL. |
| `S110-CF-CO1-EOS` | **INFO** | `M_max = 4.783 M_⊙`; `Δ/μ = 0.102` (now in [0.03,0.3]); `C_max = 2.26e-04` (floor 1e-3); runaway fixed 4.821 → 0.102 | The self-consistent μ_eff(ρ) repair fixed the runaway gap ratio — but **overshot** M_max to 4.78 M_⊙ (above the band) while compactness stayed `C ~ 2e-4`, i.e. the object remains essentially **un-compact** (no self-bound surface). |
| `INV11-W5-2` | **INFO** | `C_max = 0.0002435`; horizon `r_h = 1.0000` (Mach=1, single crossover); `n_modes = 426` (trapped normal modes, Im~0); `w_core = −0.92` (Lobo-DE) | The interior is a **horizonless gravastar**: a Lobo-DE dark-energy condensate core, acoustic Mach=1 surface, no genuine damped ringdown. Unpinned: QNM-ringdown + M–R compactness ("**no-self-bound-surface: EOS-pressure-scale-underdetermined**"). |

So the substrate *does* predict an EoS and *does* feed a TOV M–R sequence. What it does **not** yet predict stably is the *magnitude* — and that instability is itself the most decision-relevant fact in this workshop.

---

## 2. The EVOI case: an unstable, falsified M–R is higher-leverage than a clean-but-soft growth prediction

Reading A's strongest argument is not "the substrate makes a beautiful NICER prediction." It is the opposite, and it is sharper for being so.

**(i) The M–R relation is the single most over-determined falsifier the framework can field on its dimensionful flank.** NICER's J0740+6620 gives `M = 2.08 ± 0.07 M_⊙`, `R = 12.4 ± 0.9 km` (Miller+/Riley+ 2021, and the Salmi+ 2024 reanalysis tightening R); J0030+0451 gives `M ≈ 1.4 M_⊙`, `R ≈ 13 km`. The dimensionless observable these *directly* fix is the **compactness**:

```
Substitution chain — compactness gap (the falsifier):
  Step 1: C ≡ G M / (R c²)                          [definition; dimensionless]
  Step 2: NICER J0740:  M = 2.08 M_⊙, R = 12.4 km
          C_NICER = (G M)/(R c²)
                  = (1.4766 km/M_⊙ · 2.08 M_⊙) / 12.4 km
                  = 3.071 km / 12.4 km
                  = 0.2477                          [measured, ~5% precision]
  Step 3: Substrate (INV11-W5-2 / S110-CO1):  C_max = 2.4e-4
  Step 4: C_NICER / C_substrate = 0.2477 / 2.4e-4 ≈ 1.0e3
  Conclusion: the substrate's horizonless interior is ~3 orders of magnitude
              TOO DILUTE to be the object NICER measures. A self-gravitating
              relay-condensate with C ~ 10^-4 is OBSERVATIONALLY EXCLUDED by any
              NICER M–R point on a real ~2 M_⊙, ~12 km pulsar. This is a
              dimensionful falsifier the satellite has ALREADY DELIVERED.
```

`G/c²` here is `1.4766 km/M_⊙` (the standard solar-mass gravitational radius half-constant; not a framework constant — a textbook conversion, tagged as such). The point is structural: the compactness is the **most direct dimensionless reduction of the NICER data**, and the substrate currently sits 3 OOM off it. This is the cleanest single number in the entire compact-object sector, and it is the one NICER constrains best.

**(ii) The instability 0.16 → 4.78 M_⊙ is the EVOI signal, not noise.** A naive EoS gives M_max = 0.16 M_⊙ (FAIL, far too soft); the self-consistent μ_eff fix gives M_max = 4.78 M_⊙ (overshoot, far too stiff). The *true* substrate M_max is bracketed between two failing computations whose only difference is whether μ_eff tracks density. In Bayesian-UQ terms (Paper 06, McDonnell+ 2015, my UQ program): the **posterior predictive variance on M_max is enormous** — the prediction spans a factor of ~30 depending on one self-consistency choice. EVOI scales with `P(pass)·|ΔP(pass)| + P(fail)·|ΔP(fail)|`; a quantity whose current predictive band is `[0.16, 4.78] M_⊙` against a `[2.0, 2.6] M_⊙` observed window has *maximal* expected information: ANY pre-registered, properly-self-consistent computation that lands a definite M_max either (a) passes the band — a genuine surprise that would convert the sector from "built but failing" to "first dimensionful pulsar prediction," or (b) fails it with a specific structural reason — closing the dense-matter corridor on the framework's weak flank with a falsifier NICER has already measured. Both outcomes are high-information. A clean-but-currently-untested growth-suppression prediction (Reading B) has, at this stage, *lower* |ΔP| because it has no analogous already-failing baseline forcing the question.

**(iii) The dataset is fixed and improving on a known timeline.** NICER J0740/J0030 M–R credible regions exist NOW; the Salmi+ radius tightening landed 2024; the dense-matter EoS combined constraints (Paper 25, Sorensen+ 2024 — `R_{1.4} ≈ 12–13 km`, `L ≈ 40–70 MeV`, `S_v ≈ 30–34 MeV`) integrate χEFT + heavy-ion (FRIB!) + neutron-star observations into a Bayesian band that only narrows. The framework is being tested against a target that does not move and gets sharper. This is the empirical posture I value most (Paper 06 §III: the scoring function is fixed BEFORE the posterior is evaluated) — here the *data* is the fixed scoring function.

**(iv) FRIB grounding (my institution, my domain).** Paper 25's symmetry-energy program — `L ≈ 40–70 MeV`, kaon production sensitive at 2–3 n₀, pion ratios for `S(n)` — is the *terrestrial* leg of the same EoS the NICER pulsars probe at the high-density end. The framework's CFL gap `Δ(μ)` is a supra-saturation statement; the symmetry energy is the sub-to-supra-saturation slope. A substrate EoS that is to be taken seriously must reproduce *both* the FRIB-constrained `L` near n₀ AND the NICER-constrained `R_{1.4}` and `M_max`. That is a **multi-messenger, multi-density consistency gate** — exactly the cross-check structure (terrestrial + astrophysical + microscopic) that Paper 25 argues is how the EoS is actually pinned. The framework has the machinery to be plugged into that pipeline; the growth sector does not have an analogous terrestrial cross-check.

---

## 3. Engaging the CORPUS-EXCEEDS problem honestly — is the axis BLOCKED?

This is the crux the prompt demands I engage, and I will not paper over it. The honest statement is: **the axis is half-blocked, and the blocked half is exactly the half a NICER M–R gate needs.**

**What is present (not blocked):** the interior EoS (CFL `Δ(μ)`, the Lobo-DE core), the TOV integrator, the compactness functional, the self-consistent μ_eff solver. The pipeline `D_K → Δ(μ) → P(ρ) → TOV → M(R)` runs end-to-end. INV11/INV13/S110-CO1 are proof it runs.

**What is blocked (the CORPUS-EXCEEDS gap):** there is **no self-bound surface**. The S110-CO1 verdict says it in plain text: `C_max = 2.26e-04` with "no-self-bound-surface: EOS-pressure-scale-underdetermined." A neutron star's M–R curve is defined by hydrostatic equilibrium terminating at a surface where P → 0 at a *specific physical density* (the crust, ~10⁷ g/cm³, set by nuclear physics). The framework's relay-condensate has no analog of that surface — the Lobo-DE core is a smooth dark-energy condensate (`w_core = −0.92`), not a self-bound lump with a crust. Without a pressure scale that fixes the surface, the M–R curve has the wrong compactness by 3 OOM and the M_max is ambiguous by a factor of 30.

**So: blocked, or constructible?** My structural assessment: **constructible, but it requires one genuine new piece of substrate physics — a surface/crust condition — which is a real (not bookkeeping) computation.** The construction path is concrete:

1. The runaway gap ratio `Δ/μ = 4.82` was a *fixed-floor artifact* (μ held density-independent); S110-CO1 already proved the self-consistent μ_eff(ρ) relaxes it to `Δ/μ = 0.102 ∈ O(0.1)` — the physical CFL window. **The sign is right and one magnitude pathology is already fixed.** This is the realized half.
2. The remaining gap is the **pressure-scale / surface condition**. In conventional neutron-star physics this is the crust EoS where the homogeneous fluid terminates. The substrate analog would be the density at which the relay-condensate ceases to support a CFL gap — the `Δ(μ) → 0` boundary, a *substrate-derived* surface. That `Δ(μ→μ_surface) = 0` crossing is a well-posed BdG computation on the D_K spectrum. It is exactly the kind of gap-edge calculation my domain does for the neutron-drip line (Paper 02, Dobaczewski+ 1996, HFB continuum at the drip line — the analog is the chemical-potential edge where pairing vanishes into the continuum).
3. With a substrate-derived surface density, TOV terminates physically, C_max acquires a definite value, and M_max is no longer ambiguous by a factor of 30.

**Tractability verdict on the construction:** this is **~2–3 wave-equivalents** of genuine compute (a self-consistent gap-edge surface condition + TOV re-integration), not bookkeeping, and not blocked. It is the kind of computation the framework has demonstrably executed before (S110-CO1 already did the self-consistent μ_eff loop). The leverage is high *and* the construction is tractable — which is the conjunction the prompt asks me to certify or deny. I certify it for the **construction**, with one honest caveat below.

---

## 4. Where Reading A is genuinely weak — leverage ≠ tractability (the honest accounting)

I will not strawman my own pole's weaknesses; an adversarial workshop is worth nothing if I hide them.

**(a) The compactness gap may be structural, not a missing-surface artifact.** It is entirely possible that the substrate's relay-condensate is *intrinsically* a low-compactness object — a gravastar/dark-energy core (`w_core = −0.92` is dark-energy-like, not nuclear-fluid-like) that *cannot* be made to terminate at a nuclear-density surface no matter how the gap edge is computed. If so, the substrate predicts a horizonless ECO with `C ~ 10⁻⁴`, which is **not a neutron star at all** — and then the NICER comparison is not "predict M–R and test it" but "the substrate has no neutron-star solutions, full stop." That is *still* a falsifier (the framework would be claiming compact objects are gravastars, which NICER's measured `C ~ 0.25` excludes for the observed pulsars), but it is a **different, weaker** kind of result — a no-go, not a quantitative M–R curve. The dual-prior here is real: P(substrate has genuine neutron-star branch) vs P(substrate compact objects are intrinsically dilute gravastars).

**(b) The M_KK keystone may re-enter.** The compactness C and M_max are dimensionless/dimensionful in a way that is supposed to *escape* M_KK (the R/M ratio is dimensionless — that was the CV-9 hope). But M_max itself is a mass (it carries the weight), and the WS-CO-1 workshop (S110, mack × schwarzschild-penrose, **STERILE-confirmed**) already proved that the compact-object sector's transport-safe *dimensionless ratios* (echo spacing, tidal-to-compactness) are either Kerr-degenerate or grid-contaminated, and its framework-specific content rides `ω_GR` (M_KK-set). **That STERILE verdict is the single most damaging fact for an over-strong Reading A.** I must be precise about what it does and does not close:
   - **It closes** the *anchor-free GW-echo / QNM-parity falsifier* axis (dimensionless ratios, LISA-EMRI echoes). That route is dead — parity-even `[J, D_K] = 0` forbids the operator that would break Kerr-degeneracy, and this is the *same* substrate fact that sets `β_iso = 0°` (Row #91).
   - **It does NOT close** the *dimensionful M–R against NICER*. NICER does not measure a frequency ratio; it measures a mass (M_⊙) and a radius (km) and hence a compactness, **directly**. The STERILE workshop explicitly left "the independent inv-13/inv-11 compute carry-forwards — CF-CO-1 EoS pressure-scale + compactness, finite-μ CFL refine" as live, routed via `/rclab-plan` *independently of WS-CO-1's STERILE verdict*. The dimensionful M–R axis is a **distinct, still-open** corridor.

   So Reading A must be carefully scoped: it is the **dimensionful M–R / compactness** axis, NOT the dimensionless-ratio echo axis (which is sterile). This is a genuine constraint on my pole — but it is a scoping, not a refutation, and the surviving axis is the more directly NICER-measurable one.

**(c) The "overshoot to 4.78 M_⊙" is as concerning as the undershoot.** A self-consistent fix that overshoots by 2× is not obviously closer to the truth than an undershoot by 12×. It signals the EoS stiffness is being controlled by a single under-determined parameter (the surface/pressure scale), and until that is substrate-pinned, M_max is a free dial. A free dial is the opposite of a falsifier. The gate must pin the surface *from the substrate* (the `Δ → 0` edge), not tune it to the band — tuning to [2.0, 2.6] would be an ansatz-forced PASS (PROHIBITED). This is the discipline-critical risk: the construction is tractable only if the surface is derived, not fitted.

---

## 5. The pre-registrable gate (concrete)

Reading A's deliverable, stated as a pre-registrable gate per the framework's conventions:

```
Gate:  S113-CO-MR-NICER  (proposed)
Class: PHONONIC
Trigger: [SIGN] + magnitude band
Hypothesis: A substrate-derived surface condition Δ_CFL(μ_surface) = 0 (the
  chemical-potential edge where the relay-condensate's diquark gap vanishes into
  the continuum) terminates the TOV integration at a physical density, fixing
  C_max and M_max from substrate physics with NO post-hoc pressure-scale tuning.

Substrate-IS observable:  the M–R sequence {M(ρ_c), R(ρ_c)} of the
  self-consistent CFL relay-condensate, terminating at the substrate-derived
  Δ→0 surface; reduced to the dimensionless compactness C_max = G M_max/(R c²).

Laboratory-IN observable:  NICER J0740+6620 (M = 2.08±0.07 M_⊙, R = 12.4±0.9 km,
  C = 0.248) and J0030+0451 (M ≈ 1.4 M_⊙, R ≈ 13 km); the Sorensen+ 2024 combined
  EoS band (R_{1.4} = 12–13 km).

Pre-registered PASS:  C_max ∈ [0.20, 0.30] AND M_max ∈ [2.0, 2.6] M_⊙ AND
  R_{1.4} ∈ [11, 14] km, ALL with the surface DERIVED (Δ→0 edge), not fitted.
Pre-registered FAIL:  C_max < 0.05 (the substrate object is an intrinsically
  dilute gravastar, NOT a neutron star — NICER's measured C ~ 0.25 excludes it).
  This FAIL is a clean falsifier: it closes "the substrate has neutron-star
  solutions" with a specific reason.
Pre-registered INFO:  C_max physical but M_max out-of-band, OR surface derivable
  but R_{1.4} off — a stiffness/density mismatch to be characterized.

Machinery:  self-consistent μ_eff(ρ) gap solve on the L_max=12 D_K cache
  (s84_spectrum_cache_L12_tau019.npz, GPU BdG eigensolve, the S110-CO1 loop) +
  a NEW Δ_CFL(μ)→0 surface-edge solve (the substrate crust analog) + TOV
  re-integration to the substrate surface.
Inputs:  inv13_w2_1_finite_mu_cfl_eos.npz, inv11_w5_2_compact_object_interior.npz,
  s110_cf_co1_eos.npz, canonical Delta_BCS = 0.4642547 (R-PROTECTED).
Effort:  ~2–3 wave-equivalents.
Falsifiability:  the dataset (NICER M–R + Sorensen+ band) is FIXED and improving;
  the gate is decided by a measurement already in hand.
```

This gate is genuinely falsifiable *both ways*: the FAIL branch (C < 0.05) is as informative as the PASS, and the data to adjudicate it exists today. That is the EVOI signature.

---

## 6. Bayesian-UQ framing (Paper 06 discipline)

A number without an uncertainty is not a prediction. The framework's current M_max "prediction" is `[0.16, 4.78] M_⊙` — a posterior predictive band spanning a factor of ~30, dominated by *epistemic* (surface-condition) uncertainty, not statistical. The EVOI of the NICER gate is precisely the *reduction* of that band: the gate collapses the surface-condition degree of freedom from "free dial" to "substrate-derived," and the resulting M_max either falls in [2.0, 2.6] (P-shift toward a viable dimensionful sector) or does not (corridor closed with reason). This is a textbook high-information measurement in my UQ framework: large prior predictive width, a fixed scoring function (the NICER data), and a pre-registered band. The growth-suppression axis, by contrast, currently lacks the already-computed failing baseline that forces the analogous band-collapse — its EVOI is real but, at this snapshot, less acute.

---

## (i) Honest current lean

**Leaning Reading A on EVOI, with a hard scope caveat — provisional pending Round 2.** The dense-matter / NICER axis is the higher-EVOI next falsifiable prediction *for the dimensionful M–R / compactness observable specifically*, because: (1) the producing pipeline already exists and runs (CFL gap → TOV → M–R); (2) it lands a 3-OOM-falsified compactness against a satellite measurement *already in hand*; (3) the M_max predictive band `[0.16, 4.78] M_⊙` is maximally wide, so any properly self-consistent gate is maximally informative; (4) the missing piece (a substrate-derived surface) is a tractable ~2–3-wave compute the framework has demonstrated the machinery for; (5) it carries a terrestrial FRIB cross-check (symmetry energy) the growth axis lacks.

But I hold this **provisionally and narrowly**: the WS-CO-1 STERILE verdict already killed the *dimensionless-ratio* compact-object falsifier, and I must hear whether mack's Reading B can show that (a) the dimensionful M–R re-entangles M_KK the way the ratios did, collapsing my gate to "free dial, not falsifier," or (b) the f·σ8 growth axis has a comparably-failing, comparably-fixed baseline I am underweighting. If the substrate compact object is *intrinsically* a `C ~ 10⁻⁴` gravastar (dual-prior Track B in §4a), Reading A degrades from "predict M–R" to "no-go: no neutron-star branch" — still a falsifier, but a weaker kind, and that weakening could tip the balance to Reading B.

## (ii) Single most decisive consideration

**Whether the substrate's compactness gap (C ~ 2e-4 vs NICER's C ~ 0.25, a factor of ~1000) is a missing-surface artifact (fixable by a substrate-derived Δ→0 crust edge → genuine M–R prediction, Reading A wins decisively) or an intrinsic property of the relay-condensate (the substrate object is a dilute gravastar with no neutron-star branch → the NICER comparison becomes a no-go rather than a quantitative falsifier, weakening Reading A toward Reading B).** Everything turns on that one structural fork: it is the difference between the substrate *making* a falsifiable M–R curve and the substrate *lacking the object NICER measures*. The growth-axis comparison (Reading B) is decided downstream of which side of that fork the compactness gap falls on — because if Reading A's gate is a genuine quantitative M–R falsifier, its EVOI dominates; if it is only a no-go, the two axes are closer and tractability (Reading B's potential strength) decides.
