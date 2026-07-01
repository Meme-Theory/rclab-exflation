# Reference — Phonon-Exflation Framework Orientation (first-contact snapshot)

**Captured**: 2026-05-22 (S92, first invocation)
**Verified against**: knowledge-MCP canonical constants + `sessions/framework/Phononic-*.md` + `Atlas/atlas-*.md`
**Use this when**: spawned into a context where phonon-exflation substrate language is assumed and I need to ground LQG-side claims against it

## What phonon-exflation IS (in one paragraph)

Phonon-exflation is the project's substrate-IS framework: every fiber at every point of M⁴ IS a finite spectral triple `(A_K, H_K, D_K)` on Jensen-deformed SU(3) with `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` (the CCM-2007 Standard Model algebra) and KO-dimension 6. Eigenvalues of `D_K` (155,984 at L_max=10) ARE the vibrational mode content. Spectral moments of `D_K` (Seeley-DeWitt `a_0`, `a_2`, `a_4`) ARE the emergent forces: `a_0` cosmological-constant, `a_2` Einstein-Hilbert (gravity), `a_4` Yang-Mills + Higgs. Cosmogenesis is the Jensen-deformation transit through `τ_fold = 0.190` — a first-order phase transition with Mach 13.75 supersonic transit at a van Hove singularity, NOT a bounce, NOT inflation. The post-fold state is a Generalized Gibbs Ensemble (GGE) of 59.8 quasiparticle pairs frozen by integrability (the "Ordered Veil"). The framework is over-constrained by zero free parameters at the algebraic-skeleton level + one empirical pin (`τ_fold`).

## Key canonical constants (from knowledge MCP, S92)

| Constant | Value | Provenance |
|:---|:---|:---|
| `tau_fold` | 0.19 | S12/S42; CONST-FREEZE-42; superseded=False |
| `M_KK` | 7.428660036284456e+16 GeV | (no PROVENANCE entry; ≈ 0.03 M_Pl_reduced) |
| `c_sub_baseline` | 2.238 | (substrate-physics baseline; no PROVENANCE) |
| `n_s_canonical` | 0.9561 | S91 W9; canonical pin (Planck cross-check `planck_ns = 0.9649 ± 0.0042`) |
| `w0_FW` | -0.918 | S58 Volovik partition + effacement `Γ_eff = 0.99970` |
| `α_s` | -0.069 | S84 §W8-86 PASS-THEOREM; `α_s = n_s² - 1` Ornstein-Zernike identity |
| `Ω_DM h²` | 0.120 | S75 W3-K LEGGETT-MOMENT-70 PASS at 0.00% match Planck |
| `c_Gold` (Goldstone) | 0.915 M_KK | Layer-2 envelope; speed of light analog |
| `c_fabric` (substrate) | 209.97 M_KK | Layer-1; 229× hierarchy gives 2.72 acoustic e-folds |
| `Mach_max` (transit) | 13.75 | S63 transit-cascade |
| `n_pairs` (GGE relic) | 59.8 | S38 Parker; `P_exc = 1.000` sudden-quench saturation |
| `T_acoustic` (GGE temp) | 0.112 M_KK = 8.32×10¹⁵ GeV | S53 W2-3; GUT scale at zero free parameters |
| `N_DK_eigenvalues` | 155,984 | At L_max=10 |
| `Peter-Weyl block-diagonality` | 8.4×10⁻¹⁵ | S22b; ANY left-invariant metric on ANY compact Lie group |

## Proven results at machine epsilon (atlas-04, atlas-07)

- KO-dimension = 6 (G4 PROVEN)
- D_K block-diagonal in Peter-Weyl (G10 PROVEN)
- Volume-preserving TT-deformation det(g_τ)/det(g_0) = 1 (S12)
- [J, D_K(τ)] = 0 identically — CPT structural (S17a)
- Spectral Action Monotonicity ⟨λ²⟩(τ) increasing in all 10 sectors (S17a–S37; W4)
- CUTOFF-SA-37 Structural Monotonicity Theorem (S37; closes all cutoff-function stabilization mechanisms)
- 67/67 Baptista checks; Riemann 147/147 validation
- Trace theorem S[UDU†] = S[D] (S48; SA blind to U(1)_7 phase)

## Broken / open at S92 (atlas-04, atlas-08)

- T6 BROKEN: Friedmann-BCS coupling can dynamically lock τ — shortfall 133,200×, gradient ratio 6,596× at fold (S39)
- FRIEDMANN-BCS-38 OPEN: coupled dynamics shortfall
- FUNCTIONAL-SELECT-67 OPEN: which spectral functional generates n_s?
- eps_H sign reversal: n_s prediction's regulator-class uniqueness not established (atlas-09 retraction item 36)
- τ_fold axiomatic derivation deferred to S85 5.8 (currently empirical)
- Cube-3 exponent "12" in `sin²(μ_BC) = 3/(3 + e^{12τ})` has no first-principles derivation
- CC factor 3 residual: chi_2 × HP4 route gives `0.337 ρ_obs`

## Substrate-vs-laboratory distinction (LQG-relevant)

The framework distinguishes TWO causal layers (`Phononic-C-Causality.md`):
- **Layer 1 (substrate throughput)**: stiffness/inertia ratio on `(A_K, H_K, D_K)`; bounded by `c_Gold = 0.915 M_KK`; this is what the Dirac operator's eigenvalue structure permits.
- **Layer 2 (emergent Lorentzian)**: null cone of `g_M` from `a_2` Seeley-DeWitt; this is what GR-style observers measure on the post-transit emergent metric.

They coincide EXACTLY on the Killing-protected Goldstone direction; split O(τ) on the seven gapped directions. Many things ARE NOT c-bounded — fold transit (dS/dτ functional derivative, not a velocity), instantons (topological-sector transitions), Jensen evolution (substrate-internal modulus flow), Bogoliubov pair creation (mode equation in τ, not in time). The **Spectral-Moment Decoupling Theorem** (S74; anchored in Gilkey 1975 local index theorem) is the rigorous version: a_0 derivatives are SUBSTRATE DYNAMICS (no c-bound); a_2 group velocities are PROPAGATION (c-bounded). They live in different polynomial degrees and cannot be rate-compared.

## What the framework looks like under LQG translation

- The 155,984 `D_K` eigenvalues are the framework's analog of the LQG kinematical Hilbert space basis. Where LQG has spin networks indexed by `(Γ, j_ℓ, i_n)`, the framework has Peter-Weyl eigenstates indexed by SU(3) irrep `(p,q)` + multiplicity.
- The Spectral Action Monotonicity Theorem is the framework's analog of LQG's area-gap-as-theorem result.
- The framework's `τ_fold` is its analog of LQG's Immirzi γ — but they play structurally different roles (kinematical UV anchor vs dynamical fold-location). See `project_cross-framework-comparison-s92.md` for details.

## Five framework "anchors" (Phononic-Substrate-Geometry §4)

1. `M_KK = 7.43×10¹⁶ GeV` — overall spectral scale; Debye cutoff of internal lattice
2. `Δ_BCS = 0.4643 M_KK` — BCS pairing gap at fold
3. `τ_fold = 0.190` — van Hove location; last empirical anchor
4. `E_cond = -0.137 M_KK` — condensation energy
5. 4-speed hierarchy `c_mod = 1.000 > c_BLV = 0.485 > c_BA = 0.399 > c_L ∈ [0.019, 0.032]` — four distinct sound speeds

## Pre-registered observational gates (framework side)

- `α_s = -0.069` — decisive at SO DR1 ~2029 (27σ vs slow-roll); CMB-S4 ~2030 (34σ)
- `r = 0.024` (tensor-to-scalar) — LiteBIRD ~2030 at 24σ detection
- `w_0 = -0.918, w_a = 0` — DESI DR3 (~2027); pre-registered `w_0 = -0.509 ± 0.079, w_a = -0.009 ± 0.02` (S49 post-multi-T correction)
- 7-feature GW comb at substrate frequencies — LISA / SKA ~2035 at 10⁻¹⁰ sensitivity; binary discriminator
- Proton decay `τ_p = 6.26 × 10³⁹ yr` — Hyper-Kamiokande ~2045 at ~1σ in 20-yr exposure

## When my LQG perspective is most useful in this project

- When a framework claim asserts a quantum-gravity-discreteness parallel — I can adjudicate whether the parallel is STRUCTURAL (mathematical content isomorphic) or ANALOGICAL (surface-similar with distinct dynamics).
- When a substrate-IS claim invokes "spin networks" or "discrete area" — I provide the rigorous LQG version (LOST-Fleischhack uniqueness; area operator with discrete spectrum; area gap as theorem).
- When a cross-framework workshop adjudicates between LQG and the framework at the dynamics layer — I steelman the LQG side honestly, including LQG's open problems.
- When the project considers GFT condensate cosmology, EPRL/FK, LQC perturbation predictions, or Immirzi γ pinning — I bring the corpus.

## When my LQG perspective is NOT helpful

- Pure framework-internal computations (D_K eigenvalue scans, Peter-Weyl decompositions, Seeley-DeWitt moment calculations) — those belong to connes-ncg-theorist, spectral-geometer, or the substrate-physics specialists.
- Pure observational fits (DESI, Planck, LIGO) — those belong to mack-cosmic-bridge or sagan-empiricist.
- Pure mathematical infrastructure (gate-verdict files, registry landings) — those belong to the orchestrator.
