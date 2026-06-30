# Mottola/Mazur GVCS vs. the Spectral-Action Vacuum — a₀-vs-a₄ Verdict + Falsification

**Sub-investigation** (Lead B, Pillar B; throughlines T4/T5). **Author**: lizzi-spectral-functional-theorist. **Date**: 2026-06-13.
**Mandate**: FALSIFICATION-first. Hunt tensions and no-analogs; report a clean "different physics" as high-value.
**Sources read in full** (on-disk PDFs, `downloads/bh-cosmo/gravastar-condensate-stars/`):
- `20_2025_Mottola_GVCS-Effective-Theory-of-Gravity.pdf` (arXiv:2502.02519 — current canonical EFT statement; the authoritative source here)
- `09_2010_Mottola_Trace-Anomaly-DE-Condensate-Stars.pdf` (the 127pp lectures — the mechanism derivation, §§III–V)
- `16_2022_Mottola_Snowmass-Beyond-Einsteins-Horizon.pdf` (arXiv:2206.00139 — crisp prediction sketch)
- `03_2004_Mazur_Dark-Energy-Condensate-Stars-Casimir.pdf` (gr-qc/0405111 — the "Casimir-in-the-large" reading + 3-region model)
- `14_2018_Beltracchi-Gondolo_Formation-of-Dark-Energy-Stars.pdf` (arXiv:1810.12400 — a classical-GR dynamical formation channel)
- `19_2023_Mottola_GVCS-Review-Chapter.pdf` (consolidated map; cross-checked, not re-quoted)

**Framework anchors verified via knowledge MCP** (NOT trusted blindly):
- `w0_FW = −0.918` (S58 Volovik partition + effacement Γ_eff=0.99970). `get_constant` confirmed.
- `a0_fold = 6440.0` — canonical_constants.py:476 verbatim comment **"a_0 (volume term)"**; `rho_vac_over_rho_obs = 1.032` is canonical_constants.py:660 **"substrate-IS: a_0 Seeley-DeWitt zeroth moment tracks the Volovik H²-scaling vacuum (D_K → a_0 → rho_vac)"**.
- `a_4_FW_zeta = 1350.7216` — canonical_constants.py:468 **"Yang-Mills + Higgs quartic moment"**; `a4_fold = 1350.72` = ½·ζ_D(2).
- **PRIOR FRAMEWORK WORK (anti-rediscovery)**: S69 Lizzi collab W4-C (`sessions/archive/session-69/session-69-lizzi-collab.md`), PROVEN theorem, already establishes the exact structural point pressed here: *"In the anomaly-derived spectral action (Paper 02, arXiv:1103.0478), the anomaly IS the action, not a correction to it. The conformal anomaly Weyl² term appears at leading order, not suppressed by (4π)⁻⁴."* Equation `S_anom = −(1/2) ln det(D²/μ²)` is registered (s69_conformal_anomaly.py). This sub-investigation EXTENDS that anchor to the Mottola GVCS program; it does not re-derive it.

Framing law (`phononic-framing.md`): every GR model here is a GEOMETRIC-class laboratory-IN analog; the substrate is logically prior. But the mandate is falsification — divergences are reported as divergences, not dissolved into "substrate shadows."

---

## (i) THE MOTTOLA MECHANISM, STATED WITH EQUATIONS

### I.1 The problem and the strategy

Mottola's program addresses two problems at once: the BH information paradox and the cosmological-constant magnitude. The strategic claim (2025 §I; 2010 §I): classical GR treats T^μ_ν as a sharp classical source, but SM matter is quantum, and the renormalized ⟨T̂^μ_ν⟩ has connected correlators ⟨T̂T̂⟩ − ⟨T̂⟩⟨T̂⟩ ≠ 0 that are singular **on the light cone** (k²→0), not just at short distance (UV). Light-cone singularities extend over macroscopic distances and **do not decouple**; they are the conformal/trace anomaly. This is the EFT element missing from both the Wilsonian higher-curvature expansion and from a fixed-Λ classical GR.

### I.2 The trace anomaly (the a₄-class object)

In D=4, any QFT that is classically scale/conformally invariant acquires a non-zero renormalized trace (2025 eq. 3.1; 2010 eq. 4.53):

```
⟨T̂^μ_μ⟩ = a (E − ⅔□R) + b C²  +  Σ_i β_i L_i  ≡ A/√−g                         (M-1)
```

with the two fourth-order curvature invariants (2025 eq. 3.2):

```
E   = R_αβγλR^αβγλ − 4R_αβR^αβ + R²          (Euler–Gauss–Bonnet, topological)
C²  = C_αβγλC^αβγλ = R_αβγλR^αβγλ − 2R_αβR^αβ + ⅓R²   (Weyl² conformal)            (M-2)
```

**The coefficients are fixed by field content, NOT by a UV cutoff** (2025 eq. 3.3; 2010 eq. 4.55):

```
a = −(ℏ/(4π)²)·(1/360)·(N_S + 11 N_F + 62 N_V)        (Euler coefficient; 2025 renames b′→a)
b = +(ℏ/(4π)²)·(1/120)·(N_S +  6 N_F + 12 N_V)        (Weyl² coefficient)             (M-3)
```

with (N_S, N_F, N_V) the count of massless scalar / Dirac-fermion / vector fields. **This (4π)⁻² × field-content structure is precisely the structure of the heat-kernel a₄ Seeley–DeWitt coefficient.** The conformal anomaly literally IS the a₄ coefficient: in the Gilkey/Seeley–DeWitt expansion the integrated a₄ density carries the C² and E invariants with field-content-weighted coefficients of exactly form (M-3). This identification is not analogy; it is the standard heat-kernel definition of the 4D conformal anomaly (Birrell–Davies; Duff). It is registered framework-side too: `a_4_FW_zeta` (= ½ζ_D(2)) is the "Yang-Mills + Higgs quartic moment" — the fourth spectral moment of D_K.

### I.3 The anomaly effective action and the conformalon φ

The a and b terms of (M-1) **cannot** be removed by any local counterterm (the b″□R term can — it is a local R² and is NOT a true anomaly). Hence S_anom is intrinsically non-local (2025 eq. 3.6; 2010 eq. 4.61):

```
S_NL_A[g] = ¼ ∫d⁴x√−g (E−⅔R)_x ∫d⁴y√−g' G₄(x,y) [ (a/2)(E−⅔R) + b C² + Σβ_i L_i ]_y          (M-4)
```

where G₄ is the Green function of the unique 4th-order conformally-covariant operator Δ₄ (2025 eq. 3.5):

```
Δ₄ ≡ □² + 2R^μν∇_μ∇_ν − ⅔R□ + ⅓(∇^μR)∇_μ                                          (M-5)
```

G₄ is **singular on the light cone** — this is the source of all near-horizon significance. The non-local action is recast into a LOCAL form by introducing a single new scalar field φ, the **conformalon** (2025 eq. 3.8; 2010 eqs. 4.62–4.64):

```
S_A[g;φ] = −(a/2)∫d⁴x√−g [ (□φ)² − 2(R^μν − ⅓R g^μν)(∂_μφ)(∂_νφ) ] + ½∫d⁴x A φ          (M-6)
```

φ satisfies the linear 4th-order EOM (2025 eq. 3.10):

```
Δ₄φ = (1/2a)·(A/√−g) = ½E − ⅓R + (b/2a)C² + (1/2a)Σβ_i L_i                          (M-7)
```

φ has **zero scaling dimension** → S_A is a marginally relevant (dimension-4) Wilsonian operator that MUST be added to the Einstein-Hilbert action. It obeys the Wess–Zumino consistency condition S_A[e^{−2σ}g;φ] = S_A[g;φ+2σ] − S_A[g;2σ] (2025 eq. 3.9), which forbids any polynomial ∫√−g φ^n potential. φ is "closely related to" the conformal factor σ of g_αβ = e^{2σ}ḡ_αβ but is NOT the string dilaton (no SSB; explicit anomaly breaking). Mottola coins it the *conformalon*.

**Where collapse is halted, microscopically:** solving (M-7) on a Schwarzschild background gives φ_S(r) = c_S ln(1−r_M/r) + … (2025 eq. 3.12). The associated anomaly stress tensor T^μ_ν[A] grows as (1−r_M/r)⁻² ∼ f⁻² as r→r_M (2010 eq. 5.2; 2025 eqs. 3.18, 3.23):

```
T^α_β[A] ∼ κ_H⁴ (1 − r_H/r)⁻² · diag(−3,1,1,1) → ∞   as r → r_H                      (M-8)
```

This blow-up is **not** because curvature is large at the horizon (it is ∼κ_H² ∼ 1/M², small for large M); it is because the timelike Killing vector ∂/∂t becomes null there (K^μK_μ→0), a coordinate-invariant non-local property. So the anomaly stress can DOMINATE the classical Einstein terms in a thin near-horizon layer **for a BH of any mass**, even with vanishing local curvature. That is what produces the boundary layer.

### I.4 The dynamical vacuum energy (the topological branch → 4-form)

The second element: a constant Λ in GR is equivalent to an abelian **4-form** field strength F = dA with "Maxwell" action (2025 eqs. 4.1–4.3):

```
S_F[g,A] = −(1/2κ⁴)∫ F∧*F = +(1/2κ⁴)∫d⁴x√−g F̃²,    *F ≡ F̃ = (1/4!)ε^αβγλF_αβγλ          (M-9)
```

In D=4 a 4-form has (i) no propagating DOF — F̃ is constrained constant in the absence of sources (∂_μF̃=0, eq. 4.5); (ii) stress tensor ∝ g^μν (eq. 4.6):

```
T^μν_F = −(1/2κ⁴) g^μν F̃²    ⇒    Λ_eff = (4πG/κ⁴) F̃²  ≥ 0                          (M-10)
```

**Three consequences Mottola stresses (2025 §IV):** (1) Λ_eff ≥ 0 **strictly** — only de Sitter-like (positive) vacuum energy is possible, never AdS. (2) The absolute minimum Λ_eff = 0 is attained iff F̃₀ = 0, and this is *required* by the source-free flat-space Einstein equation (eq. 4.8) — flat space with Λ=0 is the ground state, **with no fine-tuning of κ**. (3) F̃ is a classical field strength, **not sensitive to UV/Planck physics** — the magnitude of vacuum energy is set by a boundary condition (an integration constant), not a zero-point sum.

### I.5 The Euler-class identification + torsion (the load-bearing step)

The new physics that ties §I.3 to §I.4: identify F of the 4-form with the **4-form of the Euler class** (2025 eq. 5.1):

```
F ≡ ε_abcd R^ab ∧ R^cd  = dA,    A = ε_abcd(ω^ab∧dω^cd + ⅔ ω^ab∧ω^ce∧ω^fd η_ef)      (M-11)
```

A is the **SO(3,1) Chern–Simons 3-form of the spin connection ω^a_b**, and *F = −E + *dA_T (eq. 5.7): in pure-Riemannian (torsion-free) geometry *F = −E exactly (the Euler density), but in **Einstein–Cartan geometry with torsion** the Chern-Simons 3-form has a torsion piece A_T that is metric-independent. Fermions couple to ω^a_b (not to the Christoffel connection) through ∇_μΨ = (∂_μ + ⅛ω_{ab μ}[γ^a,γ^b])Ψ (eq. 5.8). Treating A (hence the torsion part) as a dynamical variable independent of the metric and identifying it with the 4-form A of §I.4 makes the massless-fermion Euler contribution into a J·A interaction (2025 eqs. 5.11–5.12):

```
S_int[A;φ] = (1/3!)∫d⁴x√−g J^αβγ A_αβγ,    J^αβγ = −(a_F/2) ε^αβγμ ∂_μφ,
a_F = −(ℏ/(4π)²)·(11/360)·N_F        (the massless-FERMION part of the Euler coeff a)        (M-12)
```

The resulting "Maxwell" equation with source (eq. 5.13):

```
∇_λ F^αβγλ = κ⁴ J^αβγ    ⇔    ∂_μF̃ = (κ⁴ a_F/2) ∂_μφ                                  (M-13)
```

**The punchline:** since Λ_eff ∝ F̃² (M-10), and ∂_μF̃ ∝ ∂_μφ (M-13), **Λ_eff changes wherever and whenever φ changes — but only when a_F ≠ 0, i.e. only when massless fermions couple to torsion.** Near a horizon, blueshift (1.2) makes the lightest fermions effectively massless inside a layer |r−r_M| ≲ ΔrF = L_F²/4r_M (2025 eqs. 6.1–6.2; L_F the fermion Compton scale). Inside this layer φ rolls and F̃ (hence Λ_eff) drops from the de Sitter value to 0; outside it, classical Schwarzschild with Λ_eff = 0 is recovered. The 3-current J is localized on the worldtube R × S² of the r≃r_M surface. κ is the **topological vacuum susceptibility of gravity**, the analog of the QCD chiral/topological susceptibility (Veneziano U(1); the 2D Schwinger-model charge screening) — a NEW scale a priori unrelated to M_Pl, exactly as Λ_QCD and f_π are unrelated to it.

### I.6 Is p=−ρ DERIVED or POSTULATED?

**DERIVED, at two distinct levels** — and this matters for the comparison:
- **Equation-of-state level (clean derivation):** the interior p_V = −ρ_V is NOT an ansatz. It follows from (M-10): a 4-form field strength matched to D=4 has T^μν_F = −(1/2κ⁴)g^μν F̃², which is *identically* a cosmological term ⇒ p = −ρ exactly, w = −1 exactly, with NO freedom. This is the same reason a constant Λ has w=−1. (The 2010/2004 Mazur reading reaches the same w=−1 interior via the Gliner/de-Sitter "most repulsive component" of the static-spherical stress tensor, eq. 6 of Mazur 2004, which has three scaling components p=ρ/3 ∼ f⁻², p=ρ ∼ f⁻¹, p=−ρ ∼ f⁰; the p=−ρ piece is the sub-dominant constant one.)
- **Existence-of-solution level (now first-principles, but only as a variational EXISTENCE indication):** the 2025 paper does NOT yet have a closed gravastar solution. It rescales the near-horizon eqs. (2025 §VIII), defines dimensionless α,β (eqs. 8.15–8.16) and γ (∝κ), gives a variational ansatz f,h,φ,ψ (eqs. 9.6, 9.11–9.12), and minimizes the effective action S(η,λ) — finding genuine minima at, e.g., (η=2.557, λ=0.232) for γ=0.1 (Fig. on p33). So the gravastar is presented as **the minimum of a zero-temperature effective potential**, with the existence of the boundary-layer solution *indicated* (the paper's word) but a full numerical solution still listed as an open problem (2025 §X; 2022 Snowmass §8 open-problems list). The classical prototype is exact: the Schwarzschild 1916 constant-density interior in the r_star→r_M compact limit IS a thin-shell gravastar with positive surface tension (2025 §II, citing Mazur–Mottola 2015).

**Net:** w=−1 interior is structurally forced (4-form algebra); the *halting* of collapse and the *thickness* ℓ = 2√(L_Pl r_M) ≈ 2.2×10⁻¹⁴√(M/M_⊙) cm (2010 eq. 5.3) of the boundary layer are derived from the anomaly stress-tensor scale-matching; the full existence/stability is a variational indication, not yet a theorem.

---

## (ii) THE a₀-vs-a₄ SPECTRAL-MOMENT VERDICT  ⟵ the central question

**Setup.** Both programs say "dark energy is a spectral object of the vacuum." The question is *which spectral moment* carries it. The framework's Λ is a₀ (zeroth/volume moment); Mottola's dynamical Λ is sourced by the trace anomaly, which IS a₄ (fourth/curvature moment). I claim these are **genuinely different spectral-moment objects** — a real divergence, NOT the same physics in different language. The argument is in three steps; the conclusion is then refined by a crucial subtlety that makes the divergence *sharper*, not softer.

### Step 1 — The framework's Λ is unambiguously a₀ (the volume term)

Framework-side, the cosmological constant is the **zeroth** Seeley–DeWitt moment: Λ_cc = (2f₀/f₂)·a₀, with `a0_fold = 6440.0` documented in canonical_constants.py as literally **"a_0 (volume term)"**. The DILUTION-CC closure (S66; `rho_vac_over_rho_obs = 1.032`) is documented as **"substrate-IS: a_0 Seeley-DeWitt zeroth moment tracks the Volovik H²-scaling vacuum."** In the heat-kernel expansion a₀ = (1/(4π)^{d/2})∫√g · (field multiplicity) — it is the **mode count / volume term**, the coefficient of Λ^d in Tr f(D²/Λ²), the most UV-divergent piece. In the zeta scheme it is the half mode-count ½Σ_n d_n. **a₀ knows nothing about curvature** — it is pure spectral weight (volume × degeneracy). The framework's dark energy lives here.

### Step 2 — Mottola's dynamical Λ is sourced by a₄ (the conformal anomaly)

Mottola's Λ_eff is set by F̃ via the 4-form, but the *dynamics* that makes Λ_eff change — the entire mechanism — is the conformal anomaly (M-1). The anomaly coefficients (M-3) carry the (4π)⁻² × (N_S,N_F,N_V) structure that is the DEFINING signature of the **a₄** heat-kernel coefficient. There is no a₀ anywhere in Mottola's mechanism; indeed his central selling point (M-10 consequence 3) is that the magnitude is **independent of UV zero-point energies** — i.e. he explicitly REMOVES the a₀-type quartic-divergence (the Pauli "radius of the universe to the moon" estimate, Mazur 2004 §1) from the physics and replaces it with a boundary condition on F̃. The whole point of his program is: *do not let a₀ (the UV mode-count quartic divergence) set the dark energy*; let the **a₄-anomaly + a boundary condition** set it.

### Step 3 — Therefore the two programs put dark energy in DIFFERENT spectral moments

| | **Framework (this project)** | **Mottola GVCS** |
|:--|:--|:--|
| Dark-energy carrier | a₀ — zeroth/volume SDW moment | a₄-anomaly (Weyl² C² + Euler E), via 4-form F̃ |
| Spectral weight | ∝ Σ_n d_n (mode count) | ∝ (N_S,N_F,N_V)/(4π)² (anomaly central charges) |
| Curvature content | none (pure volume) | fourth-order curvature invariants |
| Magnitude set by | thermodynamic self-tuning (q→P=0, Volovik) | macroscopic boundary condition on F̃ (integration constant) |
| Sign | tracks Volovik vacuum (w₀=−0.918) | Λ_eff ≥ 0 strictly (de Sitter only) |
| UV sensitivity | a₀ IS the quartic divergence (then diluted) | a₀ explicitly discarded; UV-insensitive by construction |

**VERDICT: GENUINELY DIFFERENT SPECTRAL MOMENTS — a₀ (framework) vs a₄ (Mottola). This is a real DIVERGENCE in which spectral moment carries the dark-energy physics, not the same physics in two languages.** The two even disagree on the *role* of a₀: the framework's a₀ IS the dark-energy carrier (after Volovik dilution); Mottola's program is *built to exclude* a₀ (the UV mode count) from dark energy. This passes the spectral-functional-theorist's own test: what is functional-INDEPENDENT here is the *statement* "dark energy is a vacuum spectral object"; what is functional/moment-DEPENDENT is *which moment* — and the two programs land on different moments. SCHEME-DEPENDENT in the strongest sense: not just a different regulator, a different moment of the same operator.

### The crucial subtlety (sharpens, does not soften, the divergence)

One might object: "the conformal anomaly contains the Euler term E, which is *topological*; and the framework's a₀ is also a topological/global object — so maybe Mottola's dynamical Λ, which comes specifically from the **Euler/topological half** of a₄ (M-11, the Euler-class 4-form), is closer to a₀ than to the Weyl² half of a₄." Let me press on this, because it is the one place the verdict could wobble.

- It is TRUE that Mottola's dynamical Λ is carried by the **Euler-class branch** (E, the topological half of a₄), promoted to the 4-form F = ε R∧R, NOT by the Weyl² branch (C², the conformal half of a₄). Mottola himself flags this by renaming b′→a in 2025 "in recognition of the unique and primary role the topological Euler class plays." So the dark-energy carrier is the **topological half of a₄**, while the genuinely-propagating new scalar physics (the SGW breather, §below) comes from the full anomaly including C².
- But this does NOT pull it toward the framework's a₀. The Euler density E is a *fourth-order curvature* invariant (R∧R, the Gauss–Bonnet term, ∫E = Euler characteristic × 32π²). a₀ is a *zeroth-order* volume term (∫√g, no curvature). They are different SDW grades (grade 4 vs grade 0) and different cohomological objects (E is the Pfaffian/Euler class of the curvature 2-form; a₀ is the trivial volume cocycle). Topological-ness does not collapse the grade. **The divergence is between grade-4-topological (Mottola) and grade-0-volume (framework) — these do not meet.**
- This makes the verdict SHARPER: Mottola's dark energy is the *Euler half of a₄*; the framework's is *a₀*. Two non-adjacent moments. The framework's a₄ (= the Yang-Mills + Higgs quartic moment, `a_4_FW_zeta`) is the moment that, in the framework, gives gauge couplings and the Higgs quartic — NOT dark energy. So if one tried to map Mottola's dynamical-Λ object onto the framework, it would land on the framework's **a₄ slot, which the framework has already assigned to Yang–Mills/Higgs, not to Λ.** The two frameworks would be in direct competition over what a₄ is *for*.

### Cross-check against the framework's own prior result (no rediscovery)

This is exactly consistent with the S69 W4-C anchor (PROVEN): in the framework's *anomaly-derived* spectral action (my Paper 02 line, arXiv:1103.0478), "the anomaly IS the action" and "the conformal anomaly Weyl² term appears at leading order." That is the framework's a₄-anomaly functional — and S67 FUNCTIONAL-SELECT-67 *excluded* it as the bosonic functional because it produces a blue n_s tilt (the c₂, c₄ are positive and multiply negative da_k/dτ). In other words: **the framework has already TESTED an a₄-anomaly-driven vacuum functional (the Mottola-type object) and rejected it as the framework's bosonic action on observational grounds (n_s).** Mottola's program is, structurally, the GR-side incarnation of the very functional the framework's n_s data excluded. This is a strong, independent corroboration of the a₀-vs-a₄ verdict — and it is the single most important cross-framework finding here.

---

## (iii) FALSIFICATION / TENSION SECTION

I separate (A) where Mottola is MORE developed than the framework (the framework should learn from it / it pressures the framework to deliver), (B) direct contradictions, (C)–(D) the specific tensions the spawn flagged.

### A. What Mottola COMPUTES that the framework does not (predictive-surface pressure on the framework)

1. **A closed boundary-layer EFT with a variational action minimum (2025 §VIII–IX).** Mottola reduces the quantum backreaction problem to ODEs in r with an extremizable action S(η,λ) and exhibits explicit minima. The framework's analog — the fold transit — is dynamical (a τ-flow), not a static minimized object; the framework has NO compact-object structure theory. *On compact-object internal structure, Mottola's program is far more developed.* The framework simply does not model the interior radial profile of a collapsed object. **No framework counterpart exists; this is a genuine asymmetry, not a substrate shadow.**

2. **A concrete falsifiable laboratory prediction the framework lacks: Scalar Gravitational Waves (SGW).** Mottola's φ is a propagating spin-0 "breather" metric polarization h₀ (the conformal factor becomes dynamical), with a SECOND-order wave equation (despite Δ₄ being 4th order, the diffeo constraints reduce it) carrying positive energy (2017; 2022 Snowmass §7). Amplitude h₀ ≈ 0.5×10⁻²¹ (100 Mpc/r) from NS mergers, set by the QCD gluon condensate ⟨G²⟩ ≈ 250–500 MeV/fm³ (Snowmass eq. 7.1). This is **at current detector sensitivity** and disentanglable by triangulation with ≥3 detectors. *The framework has its own GW story — and it is RETIRED (walls=0 EXACT, S96; falsifier migrated GW→LSS). The framework predicts NO extra scalar GW polarization from a horizon-replacement.* This is a sharp DISCRIMINATOR: **a confirmed SGW breather polarization in NS mergers would support Mottola and would have no home in the framework**; the framework's GW channel is dead by its own audit. Mack must NOT resurrect the retired framework GW falsifier on the back of Mottola's SGW — they are different objects (Mottola's h₀ is a conformalon breather; the framework's was a transit-GW amplitude). Flag for the discriminator map: SGW is a GR-side / Mottola-side prediction, tagged as such.

3. **Dynamical dark energy in cosmology with a definite coupling (2022 §6; 2010 §VI).** Mottola's φ couples baryonic matter (via residual gluon condensates ⟨G²⟩≠0) and radiation (via ⟨F²⟩≠0 under inhomogeneity) to Λ_eff, predicting departures from ΛCDM (bulk viscosity, broken adiabaticity, w(z) deviations) with the SINGLE free parameter κ. The framework's w₀=−0.918 + DILUTION-CC is a different mechanism (Volovik thermodynamic self-tuning) and a different number. *Both predict w≠−1 deviations dynamically; the microphysics and the predicted form of w(z) differ.* This is a clean place for a future falsifier: the two predict different w(z) shapes (Mottola: φ-driven, gluon-condensate-sourced; framework: substrate-compaction-driven, Volovik-tracking). NOT the same physics (see C below).

### B. Direct contradictions with framework claims

4. **Λ_eff ≥ 0 STRICTLY (Mottola) vs framework w₀ = −0.918 with a Penrose-branch that can go ζ→w₀≈−0.494 (R_842).** Mottola's 4-form algebra (M-10) FORBIDS negative vacuum energy and forbids w < −1 — the interior is *exactly* w=−1, and cosmologically Λ_eff ≥ 0 always (de Sitter-like only). The framework's canonical w₀ = −0.918 (i.e. w > −1, a quintessence-like value), and the R_842 late-time rectangle has regulator-dependent branches (ζ→w₀≈−0.494, Zubarev→w₀≈−0.997). **Mottola's mechanism cannot produce w₀ = −0.918 for a *static interior* — its interior is rigidly w=−1.** This is a genuine tension *at the level of the interior EoS*: Mottola's condensate is rigidly w=−1; the framework's vacuum is not. (Cosmologically Mottola's *effective* w(z) can deviate from −1 through φ-dynamics even though the local condensate is w=−1 — so the contradiction is sharpest for the *static compact-object interior*, softer for the *cosmological time-averaged* w.) See (D) below for the resolution of how a w=−1 local condensate and a w≠−1 effective cosmology coexist in Mottola — and why the framework's w₀≠−1 is structurally a DIFFERENT statement.

5. **The Euler/a₄ assignment competes with the framework's a₄ = Yang–Mills/Higgs assignment.** If one imported Mottola's mechanism, his dynamical Λ would land on the framework's a₄ slot (the Euler half), but the framework has ALREADY assigned a₄ to Yang-Mills + Higgs quartic (`a_4_FW_zeta`, the leading term of the framework's selected zeta/cutoff functional). The framework cannot put dark energy in a₄ without either (a) double-booking the moment that gives gauge couplings, or (b) re-opening the S67/S69 functional-selection (which excluded the a₄-anomaly functional on n_s grounds). **This is a structural incompatibility, not a translation.**

### C. (spawn item c) Static de Sitter vs dynamic transit

**This is the sharpest tension.** Mottola's gravastar interior is a STATIC de Sitter condensate — an equilibrium endpoint, the minimum of a zero-temperature effective potential (2025 §IX), at zero temperature with zero entropy (2025 §I: "the de Sitter interior has no entropy"). Beltracchi–Gondolo (2018) confirm the formation is dynamic but the **endpoint is static**: once the p=−ρ core forms, S_r=0 ⇒ mass constant ⇒ density constant in t (their §IV.B "end states have S_r=0"). The core, once formed, does not evolve.

The framework's de Sitter condensate is a **DYNAMIC transit, NOT a static state**: the fold at τ_fold=0.190 is a first-order phase transition, supersonic (Mach 13.75), impulsive — the de Sitter-like phase is *passed through*, not *settled into*. The framework explicitly carries "Dynamic transit without static stabilization" as an open channel (S55, verified via knowledge MCP) — "conformal diagram shows viable cosmology without fixed point." The Ordered Veil (S38, PROVEN): "the transit IS the physics."

**Compatibility verdict: INCOMPATIBLE as stated, for the compact-object case.** Mottola's object is a *static endpoint*; the framework's de Sitter is a *dynamic transit with no fixed point*. These are different ontological categories:
- Mottola NEEDS a stable static minimum (the gravastar must persist as an astrophysical object for Gyr). The framework's transit is the OPPOSITE — there is deliberately no static stabilization (S55 open channel); the de Sitter phase is transient.
- The framework's cosmogenesis is a one-time impulsive transit (Mach 13.75); Mottola's gravastar is a standing endpoint of stellar collapse, formed quasi-statically (Beltracchi–Gondolo pileup).

There is a *partial* reconciliation only if one maps Mottola's gravastar onto the framework's *acoustic white hole* (S85 PROVEN) rather than onto a static condensate: both replace a horizon with a phase boundary, both are causally protective. But the time-character is opposite (static endpoint vs impulsive transit), so even that mapping breaks on dynamics. **This is a genuine no-go for identifying the two — report it as a contradiction, not a shadow.**

### D. (spawn item d) w₀=−0.918 (framework) vs w=−1 exact (Mottola)

**Substitution chain (per math-scripts §"Double-Check Logic"):**
- Mottola interior: T^μν_F = −(1/2κ⁴)g^μν F̃² (M-10) ⇒ p_V = −(1/2κ⁴)F̃², ρ_V = +(1/2κ⁴)F̃² ⇒ **w ≡ p_V/ρ_V = −1 EXACTLY** (the 4-form has no other stress component; this is algebraically rigid).
- Framework: w0_FW = −0.918 (S58), i.e. w = −0.918 > −1. So p_FW = −0.918 ρ_FW.
- Difference: |w_Mottola − w_FW| = |−1 − (−0.918)| = 0.082. Mottola is more negative by 0.082.

**Is this a tension? YES, but a scoped one — and the scoping is itself informative:**
- For the **static compact-object interior**, Mottola's w=−1 is rigid (4-form algebra) and the framework's w₀=−0.918 has no place — but note the framework does NOT claim a compact-object interior at all, so this is a comparison of a Mottola-interior against a framework-COSMOLOGICAL number. They are not the same observable. (Apples: Mottola's local gravastar EoS. Oranges: the framework's cosmological dark-energy w₀.)
- For **cosmological w(z)**: Mottola's *local* condensate is w=−1, but his *effective* cosmological w(z) deviates from −1 through φ-dynamics (gluon-condensate sourcing, broken adiabaticity, bulk viscosity; 2022 §6). The framework's w₀=−0.918 is a cosmological time-averaged value from Volovik partition + effacement. **Both predict cosmological w ≠ −1; the mechanisms and signs differ.** Mottola's deviation is φ-driven and can go either side depending on ⟨G²⟩ evolution; the framework's −0.918 is a fixed > −1 quintessence-like value from imperfect effacement (Γ_eff=0.99970, the 0.03% leakage).
- **Sharpest reading:** Mottola's vacuum *cannot* be a w>−1 quintessence in its *condensate* sector — the 4-form forbids it. If the framework's w₀=−0.918 (w>−1) is the *vacuum* EoS (not a dynamical-field deviation), then it is structurally INCOMPATIBLE with a 4-form/Mottola vacuum (which is rigidly w=−1). The framework's w>−1 comes from effacement leakage of a Volovik condensate — a thermodynamic imperfection, NOT a 4-form. **This is the cleanest single divergence: the framework's vacuum is a thermodynamically self-tuned superfluid condensate sitting slightly above w=−1 by imperfection; Mottola's vacuum is a topological 4-form condensate sitting exactly at w=−1 by algebra. Different microphysics, different numbers, different sign-structure (w>−1 vs w=−1 boundary).**

---

## (iv) NO-ANALOG LIST (honest, both directions)

### Mottola has, framework does NOT:
1. **The conformalon φ as a propagating scalar metric polarization (SGW breather h₀).** No framework counterpart. The framework's scalar sector is the Jensen deformation τ (a modulus driving the spectral action), which is NOT a propagating wave polarization of g_M. Mottola's h₀ is a genuine new GW degree of freedom; the framework predicts no such polarization (and its GW channel is retired).
2. **The 4-form / 3-form gauge field F = dA tied to the Euler class + Chern–Simons of the spin connection.** No framework analog. The framework has no abelian p-form vacuum-energy field; its Λ is a₀, a passive spectral weight, not a dynamical gauge field with a "Maxwell" equation and a current source.
3. **The topological vacuum susceptibility κ as the single free parameter.** The framework's vacuum has no κ-analog. (The framework's free-ish parameter is τ_fold=0.190, a transit-physics parameter, structurally different — it sets WHEN the transit happens, not the magnitude of a vacuum-energy gauge field.)
4. **A compact-object interior structure theory (radial profiles, surface tension τ_S, boundary-layer thickness ℓ=2√(L_Pl r_M), variational action minimum).** The framework has no compact-object model at all.
5. **Einstein–Cartan torsion as the activation mechanism** (massless fermions coupling to the spin connection ω generate J). The framework lives on KK geometry of Jensen-deformed SU(3) with the Levi-Civita connection; torsion is not a framework degree of freedom in the vacuum sector. (Torsion DOES appear elsewhere in the broader bh-cosmo incursion via Poplawski — but that is a DIFFERENT sub-investigation and a different use of torsion; Mottola's torsion is a vacuum-energy-activation device, not a bounce mechanism.)
6. **The "boundary condition not UV cutoff" resolution of the CC magnitude** (F̃₀=0 in flat space, no fine-tuning). The framework's CC magnitude is resolved differently — by Volovik dilution (114 OOM via tracking vacuum), a thermodynamic, not a boundary-condition, mechanism.

### Framework has, Mottola does NOT:
7. **The full Standard Model from a finite spectral triple** (KO-dim=6, SM quantum numbers, g₁/g₂=e^{−2τ}, Higgs mass m_H from KK threshold). Mottola's EFT takes the SM as input (the (N_S,N_F,N_V) counting), it does not derive it.
8. **a₀, a₂, a₄ as a unified moment hierarchy of ONE operator D_K** giving Λ (a₀), Newton's G (a₂), and Yang–Mills/Higgs (a₄). Mottola has the a₄-anomaly but no a₀/a₂ derivation from a single spectral operator — his G is the classical Einstein-Hilbert input, his Λ is a separate 4-form.
9. **The S_ent=0 pure-state Ordered Veil from a Bogoliubov/GGE transit** — a *quantum-information* resolution of the entropy problem via a pure product state. Mottola ALSO resolves the entropy problem (de Sitter interior has no entropy, T=0), but via a *static cold ground state*, NOT a transit-produced pure state. Both kill Bekenstein-Hawking entropy; the *mechanism* differs (static cold condensate vs dynamic transit-freeze). [This is a near-analog with a different mechanism, not a no-analog — noted for the discriminator map.]
10. **A cosmogenesis (the fold transit) — the origin of the universe.** Mottola's program is about compact-object endpoints + present-day dark energy; it has a cosmology-side (dynamical dark energy) but NOT a first-order cosmogenesis transit / acoustic white hole. The framework's transit IS its Big Bang replacement.
11. **The GGE relic / dark-matter sector** (Leggett-channel quasiparticles). No Mottola analog.

### Near-analogs (shared target, different mechanism — for the discriminator map, NOT to be conflated):
- Horizon → physical surface/phase boundary: BOTH (Mottola anomaly boundary layer ↔ framework acoustic phase boundary). Mechanism differs (anomaly stress blow-up vs acoustic Mach-13.75 supersonic flow).
- No information paradox: BOTH (no true horizon ⇒ no loss). Mechanism differs (static condensate vs pure-state transit).
- Vacuum = gravitational BEC/condensate: BOTH explicitly (Mazur 2004 cites Volovik ref. 10 and the BEC analogy; framework IS Volovik q-theory). **This is the deepest shared root** — both descend from Volovik's superfluid-vacuum picture. But Mazur–Mottola's condensate order parameter is the *conformal factor of the metric* (σ/φ), whereas the framework's is the *Jensen deformation of the spectral triple* (τ). Same ancestor (Volovik), different order parameter.

---

## Bottom line (the single sharpest result + the verdict)

**a₀-vs-a₄ VERDICT: GENUINELY DIFFERENT SPECTRAL MOMENTS.** The framework's dark energy is the **a₀ zeroth/volume Seeley–DeWitt moment** (mode count, UV-quartic, then Volovik-diluted; canonical_constants.py:476/660). Mottola's dynamical vacuum energy is sourced by the **trace anomaly = a₄**, and specifically by its **Euler/topological half** (E, promoted to the 4-form F=εR∧R via Chern–Simons of the spin connection + torsion), with magnitude set by a boundary condition on F̃, explicitly engineered to be **independent of the a₀-type UV mode count**. These are non-adjacent SDW grades (grade-0 volume vs grade-4 topological-curvature) and cohomologically distinct objects; topological-ness does not collapse the grade. This is a real divergence in which spectral moment carries the dark-energy physics — the two programs would be in direct competition over what a₄ is *for* (Mottola: dark energy; framework: Yang–Mills + Higgs). It is independently corroborated by the framework's OWN prior result: S67/S69 already TESTED an a₄-anomaly-driven bosonic functional (the framework's Paper-02 anomaly action — structurally the Mottola object) and EXCLUDED it on n_s blue-tilt grounds.

**Single sharpest tension:** Mottola's de Sitter condensate is a **STATIC, w=−1-exact, zero-entropy equilibrium endpoint** (the minimum of a T=0 effective potential; Beltracchi–Gondolo's core has S_r=0 ⇒ constant ρ ⇒ no time evolution). The framework's de Sitter is the OPPOSITE: a **DYNAMIC, impulsive (Mach 13.75), first-order TRANSIT with deliberately NO static stabilization** (S55 open channel "Dynamic transit without static stabilization"; Ordered Veil S38 "the transit IS the physics"). Static-endpoint vs no-fixed-point-transit is an ontological contradiction, not a language difference — the two cannot be identified, and the w₀=−0.918 (framework, w>−1 by Volovik effacement imperfection) vs w=−1-exact (Mottola, by rigid 4-form algebra) divergence is its EoS-level fingerprint: a thermodynamically self-tuned superfluid sitting *just above* w=−1, versus a topological 4-form condensate pinned *exactly at* w=−1.
