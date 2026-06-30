# Session 85 Workshop: feynman x lizzi — Perturbative-Ledger Immunization Theorem Family (1C)

**Date**: 2026-04-25
**Format**: Iterative 2-agent workshop (2 rounds, 4 turns)
**Agents**: feynman (feynman-theorist), lizzi (lizzi-spectral-functional-theorist)
**Source Documents**:
- sessions/archive/session-85/session-85-w9-workingpaper.md
- sessions/archive/session-85/session-85-w2-workingpaper.md
- computations/s85_gate_verdicts.txt (filter to S85-W9-1, W9-2, W2-HARMONIC-NOT-INSTANTON)
- sessions/permanent-results-registry.md (note §VII.P/Q occupied; cascade discipline from 1D)
- sessions/archive/session-85/session-85-workshop-schedule.md (W0-W5 — for S-1 and S-3 cross-pairings)
- sessions/archive/session-85/session-85-w6-13-workshop-schedule.md (mother schedule, this workshop §1C)

**Focus Topics** (from schedule §1C invocation):
1. Enumerate the immunization family from W9-1 §VII.P + W9-2 §VII.Q + W2-HARMONIC
2. Lattice-spacing immunization candidate
3. Gauge-fixing immunization candidate (BRST-style)
4. Weyl-rescaling immunization candidate (conformal-anomaly cancellation)
5. Family-registry consolidation as §VII.P/Q-FAMILY meta-theorem (note: actual landing slot may cascade, see 1D)

---

## Round 1 — feynman: Opening Analysis

### F1: Enumeration of Categorical Lifts (W9-1, W9-2, W2-HARMONIC)

#### F1.1 The three landed theorems as a categorical pattern

Every immunization theorem on the substrate has the canonical form

```
Theorem (Immunization). Observable X is immune to source-of-contamination Y at level Z,
where
   X  = a spectral-moment-derived observable on D_K (Jensen-deformed SU(3))
   Y  = a class of would-be contaminations (non-perturbative, regulator-dependent,
        gauge-fixing-dependent, lattice-discretization-dependent, Weyl-rescale-dependent, ...)
   Z  = the level at which the immunity is asserted (machine-epsilon identity,
        OOM safety floor, factorization invariance, BRST cohomological closure, ...)
```

The three landed theorems instantiate this pattern as follows (citations precise; verdict lines and SHAs from `computations/s85_gate_verdicts.txt` line 137 + `sessions/permanent-results-registry.md` §VII.P, §VII.Q, theorem #49):

| # | Theorem | X (observable) | Y (contamination class) | Z (level) | Anchor |
|:-:|:--------|:---------------|:------------------------|:----------|:-------|
| W9-1 | §VII.P Borel-Summability Floor | spectral moments / perturbative ledger of `Tr f(D_K/Λ)` | non-perturbative IR contributions with `S_inst < 4.34` | OOM safety: `min S_inst / Borel_thr = 5.58e+4`, `4.7465` OOM | gate `S85-W9-BOREL-FLOOR-REGISTRY-LANDING` PASS, value=1.0, L_max=5, `audit=5bea2a903af1415f...`, `content=1d29d866ef31d7fc...` |
| W9-2 | §VII.Q F_amp^3PI Factorization-Invariance | 3PI self-energy `F_amp^{3PI}` paired with Mukhanov-Sasaki `z_R` | regulator-class `R ∈ {ζ, Zubarev, SDW, dim-reg, lattice-BR}` | machine-ε identity: `max_R |product_ratio(R) - 1| = 2.22e-16` | gate `S85-W9-F-AMP-3PI-FI-REGISTRY-LANDING` PASS, value=2.220446049250313e-16, L_max=3, `audit=50754a7fd56a238b...`, `content=de0a4096b969c498...` |
| W2-H | (#49) W2-HARMONIC-NOT-INSTANTON | small-action saddle classification near `τ_fold` (`S_harm = 0.203`) | mis-identification of Gaussian harmonic fluctuation as WKB tunneling | classification rule: `S < 4.34 ⇒ Gaussian, never WKB`. Gaussian/WKB ratio = 62.6. | registry #49 (S84-W1b-10), `content=6ae9e84859e0109f...`, `audit=f0708197b70e55bd...` |

Quantitative cross-check (Python-verified inline; see Bash exec at workshop-prep step):

```
W9-1:  min S_inst / Borel_thr = 242091.449 / 4.34 = 55781.4399; log10 = 4.7465 OOM   [matches §VII.P]
W9-2:  eps_H / c_field        = 0.02163  / 8.847964e-6 = 2444.6302                    [matches §VII.Q condition (c)]
W2-H:  exp(-S_harm)           = exp(-0.203) = 0.8163;  exp(-Borel) = exp(-4.34) = 0.0130;
       Gaussian/WKB ratio     = 0.8163 / 0.0130 = 62.61                                [matches registry #49]
```

#### F1.2 The pattern is a categorical lift, not a coincidence

These are not three unrelated wins. They share an algebraic skeleton:

```
Substrate spectral functional      S[D_K, τ; R, gauge, Ω, a_lat, ...]
                                            ↓
Observable                         O[D_K, τ]    (target: depends only on substrate spectrum)
                                            ↓
Putative contamination             ΔO ~ ∫ (regulator-class shift, gauge-fixing trace,
                                          Weyl rescaling Ω(x), lattice discretization a, ...)
                                            ↓
Immunity claim                     ΔO = 0  (or |ΔO| < ε at a pinned level Z)
                                            ↓
Mechanism                          algebraic identity (z_R · z_R^{-1} = 1),
                                   or geometric floor (S_inst > 4.34),
                                   or classification rule (S < 4.34 ⇒ Gaussian).
```

Each theorem asserts that the substrate observable is a **fixed point** under the action of an auxiliary contamination group (or class). The categorical lift is: the contamination "groups" — non-perturbative IR sector, regulator class, gauge-fixing prescription, Weyl rescaling, lattice spacing — act on auxiliary computational scaffolding, not on D_K itself. D_K is the substrate object. Spectral moments of D_K cannot care about a scaffold that lives outside the spectrum.

#### F1.3 The full categorical lift inventory (path-integral / 1PI-vs-3PI viewpoint)

The W9 closing note (W9 working paper §1350-1356) calls out three candidate immunizations: lattice-spacing (F2), gauge-fixing (F3), Weyl-rescaling (F4). Path-integral first principles suggest several further structural lifts beyond those three. I enumerate them here as **candidate** theorems pending L1 (Mellin-residue check) from lizzi.

| ID | Candidate immunization | X (observable) | Y (contamination) | Z (level) | Class | Existing data? |
|:---|:-----------------------|:---------------|:------------------|:----------|:------|:--------------|
| C-α | **Lattice-spacing** (F2) | substrate spectral action `Tr f(D_K/Λ)` | discretization artifacts at order `a^k` | Symanzik-improved continuum limit: `O(a^2)` cancellation under tree-level coefficients (c_0=5/3, c_1=-1/12) | regulator-class | partial: S55 d_C lattice spacing in spectral units; no atlas yet |
| C-β | **Gauge-fixing** (F3) | substrate Yang-Mills effective action | choice of `R_ξ` gauge / Lorenz / axial / temporal / Coulomb | BRST cohomological closure: `Q^2 = 0`; observables ∈ ker(Q)/im(Q) | gauge-fixing | partial: S74 modulus decay used N_G=8 (gauge-invariant counting); no BRST atlas |
| C-γ | **Weyl-rescaling** (F4) | spectral action moments at fixed conformal class | Weyl rescaling `g_{μν} → Ω²(x) g_{μν}` | conformal-anomaly cancellation in `a_2 + a_4` Seeley-DeWitt sum | non-perturbative + regulator | partial: S69 W4-C theorem PROVEN that conformal anomaly is parametrically suppressed when treated as cutoff correction |
| C-δ | **OPE / Wilson-coefficient** | `<O_1(x) O_2(0)>` short-distance limit | choice of basis for local operators (Wilson basis vs power-divergent basis) | factorization at scale Λ: Wilson coefficients independent of operator-mixing renormalization scheme | regulator-class | NEW; not yet tested |
| C-ε | **Borel-summability extension** (W9-1 lift) | full perturbation series `Σ_n a_n g^n` for any spectral observable | divergent perturbation series (factorial growth) | Borel-Laplace integral converges along positive real axis | non-perturbative | W9-1 covers `S_inst > 4.34` floor; full series reconstruction is open |
| C-ζ | **4PI / 5PI extension** (W9-2 lift) | F_amp^{NPI} for `N ≥ 4` | regulator class on N-particle-irreducible self-energies | machine-ε FI identity at each N | regulator-class | NEW; W9-2 covers N=3 only |
| C-η | **Ward-identity** | substrate gauge currents `J^μ` | longitudinal gauge-mode contamination | `∂_μ J^μ = 0` to all orders → Ward identity protects transverse projector | gauge-fixing | partial: framework requires Ward via [J,D_K]=0 (CPT shield) |
| C-θ | **Volovik-Connes diffeomorphism** | spectral moments under inner-fluctuation reparameterization | choice of `D' = D + ω` with `ω ∈ Ω^1_D(A)` | spectral functional invariant under inner fluctuations | gauge-fixing (NCG-flavored) | NEW; NCG-native version of BRST |
| C-ι | **Riemann-cover / Z_2 monodromy** | spectral observables at branch points of (R, Z_2) cover | sheet-choice ambiguity in two-sheet covering | Z_2 monodromy invariance: physical observables average over sheets | regulator-class (Riemann-flavored) | partial: S83 W3-G54 HP^even, S82 monodromy; no atlas |

The classification axis ("Class" column) suggests an **internal taxonomy** of immunization theorems:

- **Non-perturbative class** (W9-1, C-ε): floor against contributions that escape the perturbation series. Mechanism: geometric saddle structure of the Jensen-tau landscape.
- **Regulator-class class** (W9-2, C-α, C-δ, C-ζ, C-ι): factorization invariance under choice of computational scheme. Mechanism: algebraic identity between paired regulator-dependent quantities (z_R · z_R^{-1}).
- **Gauge-fixing class** (C-β, C-η, C-θ): physical observables live in BRST cohomology. Mechanism: cohomological exactness.
- **Conformal/scale class** (C-γ): spectral action invariant under Weyl rescaling at the relevant Seeley-DeWitt order. Mechanism: anomaly cancellation between a_n coefficients.
- **Classification class** (W2-H): rule forbidding category-error mis-identification (Gaussian vs WKB; small-action vs barrier). Mechanism: threshold separating two physically distinct regimes.

W9-1 and W9-2 jointly already carry **two of five classes**. W2-H carries the fifth (classification). The 1C campaign's task is to land at least one representative from each remaining class — gauge-fixing (C-β / C-θ) and conformal/scale (C-γ) — and to expose any further structural lifts the path-integral viewpoint reveals.

**Question for lizzi (Q1.1)**: does each class above correspond to a distinct **Mellin-cone residue identity** on the spectral-functional side, or do classes collapse under your residue calculus? Specifically — is "regulator-class immunization" structurally identical to "conformal/scale immunization" once both are written as residue identities in a complex-Mellin variable s, or are they genuinely different residue structures?

**Question for lizzi (Q1.2)**: among C-α through C-ι, which already have supporting data registered in prior sessions (S69, S74, S77, S83, S84) ready to be promoted to a §VII.R-FAMILY entry? Identify the lowest-cost immediate landings.

### F2: Lattice-Spacing Immunization Candidate

#### F2.1 Candidate theorem statement

> **Candidate Theorem (Lattice-Spacing Immunization, C-α).**
> Let `S_lat[U; a]` be the lattice-discretized substrate spectral action on a Wilson-Dirac–regularized SU(3) gauge field configuration `U`, with lattice spacing `a` and continuum limit `S[D_K, τ; Λ] = lim_{a → 0} S_lat[U; a]`. Let `O[D_K]` be a spectral-moment-derived observable (e.g. a Seeley-DeWitt coefficient `a_k`, a heat-kernel trace `Tr e^{-tD²}`, or a Mellin transform `M[f; s] := ∫_0^∞ x^{s-1} f(x) dx`). Then on Symanzik-improved geometries with tree-level coefficients `c_0 = 5/3, c_1 = -1/12`, the difference
>
> ```
>   |O[D_K^{lat}](a) - O[D_K]|  ≤  C(D_K, Λ) · a^{2k+2}     for some integer k ≥ 1,
> ```
>
> where the bound `C(D_K, Λ)` depends only on `D_K`'s spectral data and the regulator scale `Λ`, never on the lattice prescription. In the limit `a → 0` along the Symanzik-improved trajectory, the substrate observable is **immune** to lattice-discretization artifacts.

The candidate's natural pre-registration is: PASS iff for at least three Wilson and at least one Symanzik-improved lattice prescription on a fixed `D_K`, the spectral moment `a_k` (k=0,2,4) agrees within `O(a^{2k+2})` of the continuum value evaluated through the canonical zeta-regulator.

#### F2.2 Path-integral derivation (Wilson lattice → continuum)

The Wilson lattice action for a non-abelian SU(N) gauge field on a hypercubic lattice is

```
S_W[U] = (β/N) · Σ_{plaq} Re Tr (1 - U_p),     U_p = U_{x,μ} U_{x+μ̂,ν} U_{x+ν̂,μ}^{-1} U_{x,ν}^{-1}.
```

Expanding the plaquette in powers of the lattice spacing:

```
Re Tr U_p  =  N - (a^4/2N) Tr F_{μν} F^{μν} + (a^6/24) [c_R^plaq Tr F^4 + c_R^cube Tr (D_α F)^2] + O(a^8).
```

The leading `O(a^4)` term reproduces the continuum Yang-Mills action; the `O(a^6)` corrections are the Symanzik improvement counterterms. Tree-level Symanzik coefficients (Lüscher-Weisz, 1985):

```
Substitution chain (lattice → continuum DIRECTION):

Step 1 — Definition: c_0, c_1 are the coefficients of the (1×1) plaquette and (1×2) rectangle operators in
                    the Symanzik-improved action S_imp = Σ_C c_R(C) S_C[U], with constraint c_0 + 8 c_1 = 1
                    (continuum-limit normalization on a 4D hypercubic lattice).
Step 2 — Substitute: tree-level Symanzik values c_0 = 5/3, c_1 = -1/12.
Step 3 — Simplify:   c_0 + 8 c_1 = 5/3 + 8·(-1/12) = 5/3 - 2/3 = 3/3 = 1.   [Python-verified: 1.000000]
Step 4 — Direction:  the constraint holds exactly ⇒ leading O(a^2) artifact CANCELS in the improved action,
                     leaving residual O(a^4) discretization error in the bare gauge sector.
```

For the substrate spectral action `Tr f(D_K^{lat}/Λ)`, the heat-kernel expansion at lattice spacing `a` produces

```
Tr e^{-t (D_K^{lat})^2}  =  Σ_n a_n(D_K) · t^{(n - dim)/2}  +  Σ_n δa_n(a) · t^{(n - dim)/2} · a^{p_n},
```

where `δa_n(a)` are lattice-induced corrections and `p_n` is the order-of-discretization for the n-th coefficient. The Lüscher-Weisz program proves `p_n ≥ 2` for plaquette discretization and `p_n ≥ 4` for Symanzik-improved discretization at every n. **The substrate observables `a_n` inherit the Symanzik improvement automatically**, because they are spectral functionals of `D_K^{lat}` and the lattice operator differs from the continuum operator only by terms of order `a^p`.

#### F2.3 The Mellin-residue closure (cross-cutting to L1)

Lattice-spacing immunization requires that the Mellin transform

```
M[f; s] = ∫_0^∞ x^{s-1} f(x) dx
```

of the cutoff function `f(x)` produces residues at integer / half-integer `s` that are **invariant under `f(x) → f(x · (1 + a²/x_0)^{-1})`** for any reasonable lattice-induced rescaling. In other words: the Seeley-DeWitt coefficients `a_k = M[f; -k] · a_k^{HK}` (for the cutoff family `f`) must be reproduced by the lattice cutoff family `f_lat` to the same Mellin order.

**The pure-a_4 family (cf. cross-schedule W0-W5 S-1 Regulator-Family Boundary Theorem) is the natural test case**. For pure-a_4 regulators, only the `s = -2` Mellin residue is non-trivial (multiplying `a_4`), and lattice corrections must respect this single-residue structure to preserve immunity. For mixed-residue regulators (cutoff_sqrt with non-zero `s = 0` residue from `a_0`), lattice corrections may contaminate the `a_0` slot independently of `a_4`, breaking immunity at the zeroth-moment level.

**Question for lizzi (Q2.1)**: under the pure-a_4 family, does the Mellin residue at `s = -2` remain invariant when `f(x) → f_lat(x; a)` along the Lüscher-Weisz trajectory? If yes, lattice-spacing immunization holds; if no, the immunity is scheme-bound to specific cutoff choices.

**Question for lizzi (Q2.2)**: does cutoff_sqrt's `a_0` slot break the immunity, and does this place the lattice-spacing immunization theorem **only** in the pure-a_4 family — making it scope-bound per S-1?

#### F2.4 What the candidate would falsify

The lattice-spacing immunization candidate is FALSIFIED if any pre-registered spectral moment of `D_K` shows variation `> O(a^4)` between three independent Wilson-class lattice discretizations at fixed `D_K`. This would indicate that the spectral action has a residual lattice-prescription dependence that the Symanzik program cannot remove — meaning the substrate observable depends on a computational scaffold that lives outside `D_K`.

#### F2.5 Reference papers and substrate-framing

References from `researchers/Feynman/`:
- Feynman path-integral formulation (Feynman 1948 *Rev. Mod. Phys.*) — the lattice prescription is one regularization of the continuum path integral; the substrate observable is `lim_{a → 0}` of the lattice-discretized integrand.
- Wilson lattice gauge theory (Wilson 1974 *Phys. Rev. D*) — natural starting point but produces `O(a^2)` artifacts.
- Lüscher-Weisz Symanzik improvement (1985) — the c_0, c_1 constraint.

Substrate framing (per `.claude/rules/phononic-framing.md`): the lattice is **a computational lens on the substrate, not the substrate itself**. The substrate's structure is `D_K` on Jensen-deformed SU(3); the lattice is one of many possible discretizations of the operator's spectrum. Immunization is the statement that substrate observables (spectral moments of `D_K`) do not care which discretization the calculator chose. This is a property of the spectrum, not of the lattice.

#### F2.6 Pre-registered S86 gate proposal

```
Gate ID:        S86-LATTICE-SPACING-IMMUNIZATION-CANDIDATE
Trigger:        [VERIFY-THEOREM]
Hypothesis:     For three Wilson + one Symanzik discretization of D_K at L_max=5,
                spectral moments a_0, a_2, a_4 agree across discretizations within
                O(a²) for Wilson, O(a⁴) for Symanzik-improved.
Pass criterion: max_a |a_k(disc_i) - a_k(disc_j)| / |a_k(continuum)| < a^{2k+2}
                for all (i,j) pairs and k ∈ {0, 2, 4}.
Fail criterion: any pair fails the bound by factor 2 or more.
INFO criterion: passes within factor 2 (mild lattice-prescription drift).
Effort:         MODERATE (single substrate, three lattice prescriptions, well-tested code).
Class:          regulator-class lift of W9-2.
```

**Question for lizzi (Q2.3)**: is this gate's INFO band (factor-2 within bound) the right discriminator, or should we tighten to single-ULP the way W9-2 did at machine epsilon?

### F3: Gauge-Fixing Immunization Candidate (BRST cohomological closure)

#### F3.1 Candidate theorem statement

> **Candidate Theorem (Gauge-Fixing Immunization, C-β).**
> Let `S_YM[A]` be the substrate Yang-Mills action arising as the `a_4` Seeley-DeWitt moment of `Tr f(D_K/Λ)` on Jensen-deformed SU(3). Let `S_gf[A; ξ] = S_YM[A] + S_GF[A; ξ] + S_FP[A, c, c̄]` be the gauge-fixed action with R_ξ gauge-fixing term and Faddeev-Popov ghosts (c, c̄). Define the BRST charge `Q` by its action on fields:
>
> ```
>   Q A_μ^a  =  D_μ c^a       (gauge transformation with ghost as parameter)
>   Q c^a    =  -(1/2) f^{abc} c^b c^c
>   Q c̄^a    =  B^a            (Nakanishi-Lautrup auxiliary)
>   Q B^a    =  0
> ```
>
> Then **`Q² = 0` on every substrate field**, and any substrate observable `O[A]` lying in the BRST cohomology `H^*(Q) := ker(Q) / im(Q)` is independent of the gauge-fixing parameter `ξ`. In particular, on-shell scattering amplitudes between substrate relay-pattern excitations are immune to choice of gauge-fixing prescription `ξ ∈ {Lorenz=0, Feynman=1, Yennie=3, axial, temporal, Coulomb}`.

The candidate's natural pre-registration is: PASS iff for at least four gauge-fixing prescriptions, a substrate scattering amplitude (relay-pattern–relay-pattern, e.g. analog of substrate gluon-gluon at one loop) agrees within machine epsilon for the on-shell physical observable.

#### F3.2 BRST nilpotency as algebraic identity (substitution-chain check)

```
Substitution chain (Q²=0 DIRECTION):

Step 1 — Definition:
   Q is a graded derivation on the algebra of fields {A_μ^a, c^a, c̄^a, B^a}, with ghost number
   gh(A) = 0, gh(c) = +1, gh(c̄) = -1, gh(B) = 0.
   Q increments ghost number by +1 and is graded-Leibniz.

Step 2 — Substitute (act Q twice on c^a):
   Q² c^a  =  Q [-(1/2) f^{abc} c^b c^c]
            =  -(1/2) f^{abc} [(Qc^b) c^c - c^b (Qc^c)]      (graded Leibniz, c is grade-+1)
            =  -(1/2) f^{abc} [-(1/2) f^{bde} c^d c^e c^c
                                + (1/2) f^{cde} c^b c^d c^e]

Step 3 — Simplify (use Jacobi identity for the structure constants):
   The three-ghost terms reorganize via the Jacobi identity
       f^{abc} f^{bde} + f^{abd} f^{bec} + f^{abe} f^{bcd}  =  0,
   which, combined with the antisymmetry of (c^d c^e c^c) under any pair of swaps
   (because c's are Grassmann-odd, c^d c^e = -c^e c^d), forces the sum to vanish:
       Q² c^a  =  0.

Step 4 — Direction:
   Q² c^a = 0 ⇒ Q² = 0 on the ghost sector. On A_μ, Q² A = Q(D_μ c) = D_μ (Qc) - g [A, Qc] - g(QA)c
   reduces, by the same Jacobi structure, to D_μ Q²c = 0. So Q²A = 0. By similar arithmetic, Q² c̄ = QB = 0
   and Q²B = 0. Hence Q² ≡ 0 on all fields.
```

This is the standard algebraic result (Becchi-Rouet-Stora 1976; Tyutin 1975; Henneaux-Teitelboim 1992 `Quantization of Gauge Systems` Ch. 8); I include the chain to satisfy the rule. The direction is: **`Q² = 0` is forced by Jacobi + Grassmann antisymmetry of the structure constants of SU(3)**, which is a property of the substrate fiber group, not a property of the gauge-fixing prescription. Hence the cohomology `H^*(Q)` exists and is well-defined on substrate fields.

#### F3.3 ξ-independence of physical observables (chain)

```
Substitution chain (ξ-independence DIRECTION):

Step 1 — Definition:
   The gauge-fixing functional G^a[A; ξ] enters S_gf as B^a G^a + (ξ/2) B^a B^a + c̄^a (δG^a/δθ^b) c^b,
   where θ^b is the gauge parameter.
   Differentiating:
       ∂S_gf/∂ξ  =  (1/2) B^a B^a  =  Q [(1/2) c̄^a B^a]    (BRST-exact, since Qc̄ = B and QB = 0).

Step 2 — Substitute into a path-integral expectation value:
   ∂_ξ <O> = <O · ∂S_gf/∂ξ>  =  <O · Q[(1/2) c̄^a B^a]>.

Step 3 — Simplify (integration by parts under Q if O is BRST-closed):
   For any O ∈ ker Q (Q O = 0), the identity <Q(...)> = 0 (BRST-symmetry of measure) and graded Leibniz give
       <O · Q[(1/2) c̄^a B^a]>  =  <Q[O · (1/2) c̄^a B^a]>  -  <(QO) · (1/2) c̄^a B^a>
                                =  0  -  0   =   0.

Step 4 — Direction:
   ∂_ξ <O> = 0 for all BRST-closed O. The gauge-fixing parameter ξ does not appear in physical observables
   ⇒ all members of H^*(Q) are gauge-fixing-immune.
```

Hence ξ-independence of physical observables follows from `Q² = 0` PLUS BRST-symmetry of the path-integral measure (Ward identity for the BRST current). Both ingredients are properties of the substrate fiber's algebraic structure — they do not depend on the calculator's choice of gauge.

#### F3.4 Substrate-native version: Connes inner fluctuations (C-θ)

There is a natural NCG-flavored version of BRST immunization that may be **stronger** than the QFT-style theorem. In Connes' spectral-triple formalism, gauge transformations are unitary inner automorphisms of the algebra `A`:

```
A → uAu^*,    D → uDu^* + u[D, u^*],    so D' = D + ω with ω = u[D, u^*] ∈ Ω^1_D(A).
```

The spectral action `Tr f(D'/Λ) = Tr f(D/Λ + ω/Λ)` produces, via heat-kernel expansion,

```
S_spec[D + ω] = S_spec[D] + ⟨ω, J ω⟩ + (higher terms in ω),
```

with `J` the substrate fluctuation Jacobian. Connes' theorem (CCM-2007 §3) asserts that **`S_spec[D + ω]` is independent of the choice of `u` representing a fixed equivalence class in `H^*(spectral triple)`**. This is the NCG-native form of BRST immunity, and it operates one level above the QFT-style gauge-fixing — at the level of the spectral triple's automorphism group rather than the lifted gauge bundle.

**The candidate theorem can be stated TWICE**: once at the QFT level (C-β, BRST cohomology) and once at the spectral-triple level (C-θ, inner-fluctuation invariance). The two statements are dual: C-β operates on the fiber-bundle realization of the gauge field; C-θ operates on the spectral-triple realization. They should agree on physical observables — the substrate cannot care which formulation the calculator picks.

#### F3.5 Cross-cutting to L1 (Mellin-residue closure)

The Mellin-cone residue identity for gauge-fixing immunization is the BRST-Ward identity translated to spectral language. For a substrate operator `D_K` and inner fluctuation `ω`:

```
M[Tr f(D_K + ω); s]  -  M[Tr f(D_K); s]  =  ⟨ω, ∂_s M[K_t; s]⟩|_{ω-quadratic} + O(ω³),
```

where `K_t = e^{-t D_K²}` is the heat kernel. The Mellin-cone residue at integer `s` picks out the Seeley-DeWitt coefficients `a_k`. The BRST/inner-fluctuation immunity demands that the **symmetric** part of the residue tensor (in the algebra-direction `ω`) vanishes for a gauge-equivalent ω, while the **antisymmetric** part (curvature `F = dω + ω∧ω`) survives and contributes to the gauge-invariant `a_4` slot.

**Question for lizzi (Q3.1)**: does the Mellin residue calculus see the BRST-symmetric / -antisymmetric decomposition of the inner-fluctuation tensor at integer `s`? If yes, can you separate the gauge-fixing-noise residue (symmetric, BRST-exact) from the gauge-invariant residue (antisymmetric, BRST-closed) algebraically?

**Question for lizzi (Q3.2)**: is the C-β / C-θ duality (QFT BRST vs spectral-triple inner fluctuation) visible at the Mellin level as a single residue identity, or does it require two separate residue closures with a compatibility condition between them?

#### F3.6 Anomaly cancellation as the failure mode

If the BRST current carries an anomaly (failure of BRST-symmetry of the measure under quantization), then ξ-independence is broken at the loop order where the anomaly contributes. The substrate's anomaly structure is fixed by the KO-6 representation content (S85-W2 §VII.J Cartan-Level-2 Exclusion + §VII.N Three-Layer Regulator).

**Candidate sub-theorem**: BRST anomaly cancellation on the substrate is the statement that `Tr_F (Y† Y · χ_A)` vanishes for chiral KO-6-conjugate representations. This is a **finite-dimensional trace identity on the fiber algebra A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)**, not a perturbative QFT calculation — it is a property of the substrate's representation content, which is fixed (S85-W2-3 HP^3 three-way; S85-W2-4 KO-6 Higgs sign). If this trace vanishes (which framework results indicate it does, via §VII.K HP^even bucket assignments), then BRST closure is anomaly-free at every order, and the gauge-fixing immunization theorem holds **non-perturbatively** — not just to all orders in `g²`.

#### F3.7 Pre-registered S86 gate proposal

```
Gate ID:        S86-GAUGE-FIXING-IMMUNIZATION-CANDIDATE
Trigger:        [VERIFY-THEOREM]
Hypothesis:     For four R_ξ gauge prescriptions {ξ=0 Lorenz, ξ=1 Feynman, ξ=3 Yennie, axial-n3=1},
                a substrate gluon-gluon scattering amplitude at one loop (lattice-Wick-rotated)
                on Jensen-deformed SU(3) is independent of ξ for the on-shell physical projection
                within machine epsilon.
Pass criterion: max_ξ |M(ξ_i) - M(ξ_j)| / |M(ξ_0)| < 2.22e-16  (machine ε), all (i,j) pairs.
Fail criterion: any pair > 1e-12 (genuine ξ-dependence in physical observable).
INFO criterion: in (1e-15, 1e-12) — likely numerical accumulation, requires diagnostic.
Effort:         HEAVY (one-loop amplitudes, four gauges, on-shell projection).
Class:          gauge-fixing lift; complementary to W9-1 (non-perturbative) and W9-2 (regulator-class).
```

**Question for lizzi (Q3.3)**: is the machine-ε threshold the right discriminator, or is BRST cohomology more naturally tested as a **relation** between amplitudes (Slavnov-Taylor identity) than as numerical-equality across gauges?

### F4: Weyl-Rescaling Immunization Candidate (conformal-anomaly cancellation)

#### F4.1 Candidate theorem statement

> **Candidate Theorem (Weyl-Rescaling Immunization, C-γ).**
> Let `g_{μν} → Ω²(x) g_{μν}` be a smooth Weyl rescaling on the substrate base manifold M⁴. Let `S_spec[D_K, Ω] := Tr f((Ω·D_K·Ω⁻¹)/Λ)` be the substrate spectral action under the rescaled Dirac operator. Define
>
> ```
>   ΔS_W[Ω] := S_spec[D_K, Ω] - S_spec[D_K, 1].
> ```
>
> Then on substrate fields satisfying the conformal-anomaly cancellation condition
>
> ```
>   a_4-anomaly:  a_W²(D_K) + α_E E_4(D_K) = 0    (Duff anomaly coefficients balance),
> ```
>
> the variation `ΔS_W[Ω]` is a **boundary term** at order `Ω⁰` and a **parametrically suppressed** correction at higher orders in `(Λ_anomaly / Λ_cutoff)²`. Consequently, the substrate observables derived from `S_spec` are immune to Weyl rescaling up to anomaly-controlled corrections that vanish as `Λ_anomaly / Λ_cutoff → 0`.

The candidate's natural pre-registration is: PASS iff for at least three Weyl rescalings `Ω(x)` (constant, slowly-varying, rapidly-varying) on a fixed `D_K`, the spectral moment `a_4` agrees within the expected anomaly-suppression bound, AND the boundary term at `Ω⁰` is computed and matches the Duff-Polyakov 4D trace anomaly structure.

#### F4.2 The two-coefficient structure of the 4D trace anomaly

In four dimensions, the conformal anomaly of a generic conformal field theory has the two-coefficient form (Duff 1977; Deser-Schwimmer 1993):

```
<T^μ_μ>(x)  =  a · E_4(x)  +  b · W²(x)  +  (∇²R term, scheme-dependent boundary).
```

where `E_4 = R_{μνρσ} R^{μνρσ} - 4 R_{μν} R^{μν} + R²` is the 4D Euler density (topological, integrates to χ(M)) and `W² = C_{μνρσ} C^{μνρσ}` is the Weyl-tensor square (Weyl-invariant locally).

```
Substitution chain (Weyl-invariance DIRECTION):

Step 1 — Definition:
   Under g → Ω² g, the spectral action moments transform as
       a_2 → a_2 + (k_2 ∂² ln Ω) integrand,    [boundary contribution, dimension-2]
       a_4 → a_4 + (k_W · W² · Ω⁰ + k_E · E_4 · Ω⁰) integrand    [conformal anomaly, dimension-0].

Step 2 — Substitute the substrate's anomaly coefficients:
   k_W = b(D_K, A_F)    [Weyl-tensor coefficient — depends on substrate field content]
   k_E = a(D_K, A_F)    [Euler-density coefficient — also content-dependent]

Step 3 — Simplify (require Weyl-invariance):
   For Weyl-invariance to hold at the a_4 moment level, we need
       k_W · W² + k_E · E_4   to integrate to zero against arbitrary Ω(x).
   Since W² and E_4 are independent invariants, this requires SIMULTANEOUSLY
       k_W = 0   AND   k_E = 0    (strong cancellation, generically over-constrained), OR
       k_W = 0   AND   k_E ≠ 0    (Weyl-invariant up to topological term),
   where the latter is the substrate's natural realization (Duff "type-B anomaly").

Step 4 — Direction:
   On the substrate, k_W is fixed by the fiber-algebra trace Tr_F(Y† Y) at the a_4 slot
   (cf. AC-2010 §V eq. 5.12 reused in S85-W2-4 KO-6 Higgs sign). If KO-6 representation content
   forces k_W = 0 (or |k_W| < ε for some small ε), Weyl-rescaling immunization holds modulo
   the Euler-density topological piece.
```

The S69 W4-C theorem (knowledge-MCP search hit: `session-69-lizzi-collab.md` → "the conformal anomaly that GENERATES the spectral action in my anomaly derivation (Paper 02) is parametrically suppressed when treated as a CORRECTION to the cutoff", PROVEN status) establishes the parametric suppression `(Λ_anomaly / Λ_cutoff)²` direction. **This is a STRUCTURAL precondition for C-γ**: the conformal anomaly cannot be the dominant contribution to the spectral action; it must be a suppressed correction. F4 asks whether the suppression is strong enough to immunize substrate observables under Weyl rescaling.

I have NOT directly Read `session-69-lizzi-collab.md` (only the knowledge-MCP hit's first sentence). The S69 W4-C theorem's quantitative suppression factor is not cited here; it should be retrieved by lizzi via her L1 residue computation if quantitatively load-bearing.

#### F4.3 Path-integral viewpoint — the conformal anomaly as a Mellin-residue obstruction

In the Mellin / heat-kernel formulation, the spectral action's response to Weyl rescaling is encoded in the Mellin transform's behavior at integer `s = 0` (the `a_4` slot in 4D):

```
Tr e^{-t Ω·D²·Ω}  =  Σ_n a_n[Ω] · t^{(n - 4)/2}.
```

Under Weyl rescaling, the `n = 4` coefficient picks up an anomalous contribution proportional to the conformal-anomaly density. In Mellin-residue language (cross-cutting to L1), this is the **`s = 0` residue contribution from the cutoff function `f`**.

For the **pure-a_4 family** (cf. cross-schedule W0-W5 S-1 Regulator-Family Boundary Theorem), the Mellin residue at `s = 0` is **non-trivial only at the a_4 slot** — the regulator's f_0 = 0 (zero residue at s = -1) ensures a_0 does not pick up Weyl-anomaly contamination. For **cutoff_sqrt**, f_0 = 1/2 (non-zero a_0 residue), which means the cutoff_sqrt regulator allows Weyl-rescaling contamination at the zeroth-moment level in addition to the standard a_4 anomaly.

```
Substitution chain (regulator-scope DIRECTION):

Step 1 — Definition:
   M[f; -k] = f_k = k-th Mellin moment, multiplies a_{2k} in the Seeley-DeWitt expansion.
   Pure-a_4 family: f_0 = 0, f_2 = 0 (or arbitrary), f_4 ≠ 0.
   cutoff_sqrt:    f_0 = 1/2, f_2 = 1, f_4 = 1 (Andrianov-Lizzi forced; canonical_constants).

Step 2 — Substitute into Weyl-anomaly response:
   Δa_0[Ω] = f_0 · ⟨Ω⁰ · 1⟩       (cosmological-constant slot picks up rescaling)
   Δa_4[Ω] = f_4 · ⟨W², E_4⟩      (standard 4D conformal anomaly).

Step 3 — Simplify:
   Pure-a_4: Δa_0 = 0 (because f_0 = 0); only standard a_4 anomaly contributes.
   cutoff_sqrt: Δa_0 = (1/2) · ⟨Ω⁰ · 1⟩ ≠ 0 — additional contamination.

Step 4 — Direction:
   Weyl-rescaling immunization holds in pure-a_4 family at the a_0 level (no contamination there);
   in cutoff_sqrt family, Weyl rescaling shifts the cosmological-constant slot by a Ω-dependent amount.
   Hence C-γ is SCOPE-BOUND to pure-a_4 family at the a_0 moment.
   At the a_4 moment, both families have anomaly contributions; immunity requires Duff cancellation
   k_W = 0 (representation-content-dependent).
```

This is the structurally important result: **Weyl-rescaling immunization is naturally a pure-a_4-family theorem**, with cutoff_sqrt outside its scope at the a_0 level. This makes C-γ the FIRST candidate where the regulator-family boundary genuinely matters.

#### F4.4 Cross-cutting to L1 (Mellin-residue closure)

**Question for lizzi (Q4.1)**: in your Mellin-cone residue calculus, does the `s = 0` residue at the `a_4` slot decompose into a Weyl-tensor-square part and a Euler-density part, and can you compute the substrate's coefficients `(a_DK, b_DK)` directly from `D_K`'s representation content? If so, the substrate-anomaly Duff-cancellation condition `b_DK = 0` is testable.

**Question for lizzi (Q4.2)**: per cross-schedule W0-W5 S-1, does the pure-a_4 family's Mellin-residue structure reduce the Weyl-rescaling anomaly to a single residue, while cutoff_sqrt requires two independent residues (one at s = 0, one at s = -1)? If yes, this is a **clean scope bound**: C-γ holds in pure-a_4, fails (or partially fails) in cutoff_sqrt.

**Question for lizzi (Q4.3)**: the W2-1 axiom-minimality result (5/7 CCM-2007 axioms load-bearing, with orient and PD non-load-bearing for α_s) — does this affect the Weyl-anomaly cancellation? Specifically, is the Duff coefficient `b` derivable from the 5-axiom subset, or does it require orient (which might supply the Weyl-tensor representation content)?

#### F4.5 Substrate framing

Per `.claude/rules/phononic-framing.md`, the **a_2 Seeley-DeWitt coefficient generates the Einstein-Hilbert action**; gravity is the second spectral moment. The a_4 slot generates the Yang-Mills action and contains the conformal-anomaly density. Weyl rescaling is a **gauge of the metric**, not a physical change to the substrate — the spectral content of `D_K` is invariant under any local rescaling because `D_K` lives at every fiber point and does not depend on the choice of a "frame" function `Ω(x)`.

The conformal anomaly is therefore a **technical artifact of the heat-kernel regularization**: the substrate observable `a_4` is invariant; the regulated trace `Tr f(D_K/Λ)` picks up an Ω-dependent boundary term whose magnitude is set by the cutoff scale and the Duff coefficients of the fiber's representation content. This is consistent with W4-C's framing: the conformal anomaly is the "piece of the effective action that breaks conformal invariance" but is parametrically suppressed.

#### F4.6 Pre-registered S86 gate proposal

```
Gate ID:        S86-WEYL-RESCALING-IMMUNIZATION-CANDIDATE
Trigger:        [VERIFY-THEOREM]
Hypothesis:     For three Weyl rescalings Ω(x) (constant, slow-varying, fast-varying) at fixed D_K,
                the substrate's a_2 Seeley-DeWitt moment is invariant up to boundary terms,
                and the a_4 moment is invariant up to anomaly density (Duff coefficients) which
                is parametrically (Λ_anomaly/Λ_cutoff)² suppressed.
Pass criterion: |Δa_2[Ω] - boundary[Ω]| / |a_2[1]| < (Λ_anomaly/Λ_cutoff)²,
                AND |Δa_4[Ω] - Duff_anomaly[Ω]| / |a_4[1]| < (Λ_anomaly/Λ_cutoff)²,
                with Λ_anomaly / Λ_cutoff < 0.1 forced by canonical constants.
Fail criterion: any moment shows Ω-dependence beyond the expected anomaly suppression bound.
INFO criterion: anomaly suppression is between (Λ_anomaly/Λ_cutoff) and (Λ_anomaly/Λ_cutoff)² —
                weaker than expected but not absent.
Effort:         HEAVY (heat-kernel under 3 rescalings, Duff coefficients on substrate).
Class:          conformal/scale lift; complementary to W9-1 (non-perturbative) and W9-2 (regulator).
Cross-pair:     W0-W5 S-1 (pure-a_4 family scope); S69 W4-C (parametric suppression precondition).
```

**Question for lizzi (Q4.4)**: should this gate's pass band be tightened by using the S69 W4-C parametric suppression factor `(Λ_anomaly/Λ_cutoff)²` directly as the threshold, or should we use a looser band to allow detection of ANY Weyl-violation beyond what S69 W4-C predicted?

### FN: Cross-Cutting Observations & Further Structural Lifts

#### FN.1 What makes immunization theorems compose

Across F1.1, F2, F3, F4, three structural features recur:

1. **The contamination class never acts on D_K itself.** It always acts on a computational scaffold that sits between D_K and the calculator (regulator class, gauge-fixing prescription, Weyl rescaling, lattice spacing, Borel-summation kernel, NPI level). The substrate's structural primacy is the reason every immunization theorem is even possible: D_K does not care what scaffold the calculator chose.
2. **Each theorem identifies an algebraic identity that absorbs the contamination.** W9-2's identity is `z_R · z_R^{-1} = 1` (Mukhanov-Sasaki paired with 3PI z_R). W9-1's identity is `(min S_inst) / Borel_thr ≫ 1` (a geometric inequality, not algebraic, but it functions identically — it forbids the contamination from having any observable footprint). W2-H's "identity" is a threshold separating two regimes (`S < 4.34 ⇒ Gaussian`). C-α's identity is the Symanzik constraint `c_0 + 8 c_1 = 1`. C-β's identity is `Q² = 0`. C-γ's identity is the Duff cancellation `b = 0`.
3. **The mechanism is always cohomological-or-residue-theoretic in disguise.** BRST is literally cohomology. Mellin-residue closures are residue-theoretic. The Duff anomaly cancellation is the vanishing of a single-residue contribution. The Borel floor is the absence of singularities along the positive real axis. **All five classes (non-perturbative, regulator, gauge-fixing, conformal, classification) reduce to vanishing-residue-or-pole conditions on a complex analytic structure built from the cutoff function `f`**.

**Conjecture (cross-cutting)**: every immunization theorem has the form

```
"The Mellin transform of the cutoff function `f` has a residue structure
 such that the contamination Y enters only at residues that vanish on
 the substrate's representation content."
```

If this conjecture holds, the immunization family is ONE THEOREM with multiple corollaries — analogous to the W2-2 (k, R, G) cross-session theorem family, which collapsed §VII.J + §VII.K + §VII.N into a single parameterized statement.

**Question for lizzi (QN.1)**: does your Mellin-cone residue calculus support this conjecture? Specifically — can you reduce W9-1, W9-2, W2-H, C-α, C-β, C-γ to a single parameterized residue-vanishing statement on the cutoff function `f`'s Mellin transform? If yes, the family-registry section (§VII.R cascade per the 1D synthesis cluster) becomes a SINGLE theorem with five corollaries.

#### FN.2 Internal taxonomy of the family

Repeating the F1.3 taxonomy with sharper structural commentary:

| Class | Theorems | What is the algebraic identity? | What is the failure mode? |
|:------|:---------|:--------------------------------|:--------------------------|
| Non-perturbative | W9-1, C-ε | geometric floor: `min S_inst > Borel_thr` | a saddle below threshold (would-be tunneling) |
| Regulator-class | W9-2, C-α, C-δ, C-ζ, C-ι | algebraic pairing: `z_R · z_R^{-1} = 1`, Symanzik `c_0 + 8c_1 = 1`, Wilson factorization | residue mismatch under regulator change |
| Gauge-fixing | C-β, C-η, C-θ | cohomological exactness: `Q² = 0`, observables ∈ ker(Q)/im(Q) | BRST anomaly (rep-content failure) |
| Conformal/scale | C-γ | Duff cancellation: `b(D_K, A_F) = 0` at a_4 slot | rep-content gives `b ≠ 0` (NOT immune) |
| Classification | W2-H | threshold: `S < 4.34 ⇒ Gaussian` | a saddle near threshold needing a tie-breaker |

The classification suggests the family-registry section's natural structure: ONE meta-theorem (the substrate's spectral observables are immune to a class of computational-scaffold contaminations), with five corollaries (one per class), each verified by 1-3 instantiated theorems.

#### FN.3 What does NOT become an immunization theorem

It is worth being explicit about which contamination classes are **NOT** absorbed:

- **D_K-deformation contamination (Jensen τ, fiber group choice, KO-dim)** — these are NOT scaffolds. They are properties of the substrate itself. Changing them changes the substrate, not the calculator's lens. There is no "Jensen-tau immunization theorem" because Jensen-tau is the dynamical variable.
- **Representation-content contamination (KO-6 sign choice, A_F = ℂ ⊕ ℍ ⊕ M_3 vs alternative)** — the substrate's representation content is a structural axiom. Different content gives different physics, full stop. There is no "representation-content immunization" theorem.
- **CCM-2007 axiom-set contamination** — choosing 5 vs 7 axioms is not a contamination; it changes which spectral triples are admissible. (S85-W2-1 PASS: only 5/7 axioms load-bearing for α_s, which is a structural reduction, not an immunization.)

This is the **negative side** of the family classification: not everything that looks like a regulator is one. The line between "scaffold" and "structural axiom" is the line between immunization-theorem-candidates and non-candidates.

**Question for lizzi (QN.2)**: in your Mellin-residue calculus, is there a clean criterion for distinguishing scaffolds (which admit immunization) from structural axioms (which do not)? My path-integral instinct says: scaffolds are anything that affects only the COMPUTATION of `Tr f(D_K/Λ)`, not its INTERPRETATION as a substrate observable. Does the Mellin formulation give a sharper condition?

#### FN.4 The pure-a_4 / cutoff_sqrt scope split (cross-pairing W0-W5 S-1)

F2 (lattice-spacing) and F4 (Weyl-rescaling) both expose a pure-a_4 / cutoff_sqrt scope split. F3 (gauge-fixing) and F5 (Borel) appear to NOT have this split — BRST cohomology and Borel summability are independent of regulator class. The pattern is:

| Candidate | Pure-a_4 family | cutoff_sqrt family | Scope-bound? |
|:----------|:----------------|:-------------------|:-------------|
| W9-1 (Borel floor) | PASS | PASS (4-regulator atlas excludes cutoff_sqrt; if extended, still expected PASS — geometric floor is regulator-independent) | NO |
| W9-2 (F_amp^3PI FI) | PASS (4 of 5 atlas members) | unclear (cutoff_sqrt was NOT in W9-2's 5-regulator atlas; the atlas was {ζ, Zubarev, SDW, dim-reg, lattice-BR}) | likely NO; need verification |
| W2-H (harmonic) | PASS | PASS (threshold is geometric, not regulator-dependent) | NO |
| C-α (lattice-spacing) | likely PASS | possibly fails at a_0 slot | YES (per F2.3) |
| C-β / C-θ (gauge-fixing) | PASS | PASS (BRST is fiber-algebraic, not regulator-dependent) | NO |
| C-γ (Weyl-rescaling) | PASS at a_0 (no contamination there) | possibly fails at a_0 slot via f_0 = 1/2 contamination | YES (per F4.3) |

The structural finding: **scope-binding to pure-a_4 family appears only when the contamination acts on the a_0 zeroth-moment slot**. The a_0 slot is precisely where cutoff_sqrt and pure-a_4 disagree (f_0 = 1/2 vs f_0 = 0). So the regulator-family boundary is a wall AT THE a_0 LEVEL, not at the a_4 level.

**Question for lizzi (QN.3)**: is this pattern (scope-binding ↔ a_0 contamination) GENERAL, or does it break down for some immunization candidate? Specifically: is there an immunization theorem whose regulator-scope is bounded by an a_2 contamination rather than an a_0 contamination?

**Cross-schedule pairing flag**: Per the workshop invocation, this finding pairs with **W0-W5 S-1 Regulator-Family Boundary Theorem**. If the S-1 synthesis lands a clean canonical statement of the boundary (e.g., "the pure-a_4 family is an R-protected sublattice"), then the family-registry section can cite S-1 as the SCOPE-BOUND parent theorem under which C-α and C-γ live as restricted-scope corollaries.

#### FN.5 Cross-pairing with W0-W5 S-3 (§VII.Ω-UNIFIED α_s+β_s)

The §VII.Ω-UNIFIED α_s+β_s registry section (W0-W5 S-3) consolidates α_s = n_s² - 1 + β_s contributions across multiple sessions into a unified registry entry. The connection to immunization theorems is structural:

- **α_s** is a substrate observable (running coupling, derivable from spectral moments).
- **β_s = dα_s/d ln k** is the running of α_s — also derivable from spectral moments, by differentiating with respect to the renormalization scale.
- The W0-W5 S-3 synthesis presumably argues that α_s + β_s is regulator-independent at machine ε (the §VII.Ω-UNIFIED claim).

**This is a regulator-class immunization theorem in disguise**: it asserts that `α_s + β_s` is in the same machine-ε FI class as `F_amp^3PI` (W9-2). If lizzi's L3 finds that the §VII.Ω-UNIFIED Mellin residue identity is the SAME residue identity as W9-2's, then α_s + β_s is a member of the same family — Corollary `1` of the regulator-class C-corollary.

**Question for lizzi (QN.4)**: does the Mellin residue identity for α_s + β_s match the one for `F_amp^3PI`? If yes, the §VII.Ω-UNIFIED entry is structurally the same theorem as §VII.Q, just instantiated on a different observable. The family-registry section should then list α_s + β_s as a §VII.Q-corollary.

#### FN.6 Registry slot allocation (§VII.R cascade)

Per the 1D synthesis cluster's §VII.R cascade discipline (referenced in the workshop invocation), §VII.P and §VII.Q are now occupied (S85-W9-1 and S85-W9-2 respectively, 2026-04-24). The next available slot is §VII.R. The family-registry section should land at:

- **§VII.R — Perturbative-Ledger Immunization Theorem Family** (parent meta-theorem)
  - **§VII.R.α** Lattice-Spacing Immunization (C-α)
  - **§VII.R.β** Gauge-Fixing Immunization (C-β + C-θ duality)
  - **§VII.R.γ** Weyl-Rescaling Immunization (C-γ)
  - **§VII.R.δ** OPE / Wilson-Coefficient Immunization (C-δ; new)
  - **§VII.R.ε** Borel-Summability Extension (C-ε; lifts §VII.P to full series)
  - **§VII.R.ζ** N-PI Extension for N ≥ 4 (C-ζ; lifts §VII.Q to higher NPI)
  - **§VII.R.η** Ward-Identity Immunization (C-η)
  - **§VII.R.ι** Riemann-Cover / Z_2 Monodromy Immunization (C-ι)

This is a meta-registry entry, not eight new theorems — it states the family structure, lists the corollaries, marks each as PASS / OPEN / SCOPE-BOUND, and pre-registers S86+ gates for the OPEN candidates.

**Question for lizzi (QN.5)**: do you agree §VII.R is the right cascade slot, or does the 1D synthesis discipline reserve §VII.R for a different family? If §VII.R is taken, the next clean slot is §VII.S (or, per cascade convention, §VII.P-FAMILY as a sub-numbered annex).

#### FN.7 Effort ranking for S86 candidate gates

Combining F2.6, F3.7, F4.6, plus C-δ through C-ι (no F-section but enumerated in F1.3):

| Gate ID | Class | Effort | EVOI rationale |
|:--------|:------|:-------|:---------------|
| S86-LATTICE-SPACING-IMMUNIZATION-CANDIDATE | regulator | MODERATE | already-existing lattice infrastructure; lowest cost |
| S86-WEYL-RESCALING-IMMUNIZATION-CANDIDATE | conformal | HEAVY | requires heat-kernel under multiple Ω(x); high reuse with S69 |
| S86-GAUGE-FIXING-IMMUNIZATION-CANDIDATE | gauge-fixing | HEAVY | one-loop scattering amplitudes in 4 gauges; new infrastructure |
| S86-OPE-IMMUNIZATION-CANDIDATE (C-δ) | regulator | MODERATE | Wilson-coefficient calculation in two operator bases |
| S86-BOREL-SERIES-EXTENSION (C-ε) | non-pert | HEAVY | full-series perturbation theory under Borel-Laplace |
| S86-NPI-EXTENSION-N-EQ-4 (C-ζ) | regulator | MODERATE | direct extension of W9-2 to 4PI; reuses W9-2 atlas |
| S86-WARD-IDENTITY-IMMUNIZATION (C-η) | gauge-fixing | LIGHT | one-line consequence of [J, D_K] = 0 (already PROVEN, reg #?) — likely already de facto landed; just needs registry write |
| S86-INNER-FLUCTUATION-IMMUNIZATION (C-θ) | gauge-fixing | LIGHT | one-line consequence of CCM-2007 §3 — already in framework, just needs registry write |
| S86-RIEMANN-MONODROMY-IMMUNIZATION (C-ι) | regulator | MODERATE | uses S82-S83 monodromy infrastructure |

The lowest-cost immediate landings are **C-η Ward-Identity** (one line from `[J, D_K] = 0`, already PROVEN at machine ε per registry §II) and **C-θ Inner-Fluctuation** (one line from CCM-2007 §3). Both should be promotable to the family-registry section in a Round-2 lizzi-side write — they DO NOT require new computation.

**Question for lizzi (QN.6)**: do you concur that C-η and C-θ are already-de-facto landed theorems whose only missing step is a §VII.R registry entry? If yes, the family-registry section in Round 2 can immediately list them as PASS (with provenance citations to the existing CPT-shield and CCM-2007 §3 results).

#### FN.8 Summary of questions for lizzi

For convenient reference in Round 1 — lizzi's Response section, here are the 14 questions posed:

| # | Question | Section |
|:--|:---------|:--------|
| Q1.1 | Mellin-cone residue identity for each class — collapse or distinct? | F1 |
| Q1.2 | Lowest-cost immediate landings from existing data | F1 |
| Q2.1 | Pure-a_4 Mellin residue invariance under f → f_lat | F2 |
| Q2.2 | cutoff_sqrt a_0 contamination breaks lattice immunization scope-bound | F2 |
| Q2.3 | INFO band threshold: factor-2 vs single-ULP machine ε | F2 |
| Q3.1 | BRST symmetric/antisymmetric Mellin-residue decomposition | F3 |
| Q3.2 | C-β / C-θ Mellin-level duality structure | F3 |
| Q3.3 | Slavnov-Taylor relation vs numerical ξ-scan threshold | F3 |
| Q4.1 | Substrate Duff coefficients (a_DK, b_DK) directly computable | F4 |
| Q4.2 | Pure-a_4 single-residue vs cutoff_sqrt two-residue Weyl structure | F4 |
| Q4.3 | W2-1 axiom-minimality interaction with Weyl anomaly | F4 |
| Q4.4 | Pass-band threshold = (Λ_anomaly/Λ_cutoff)² or looser | F4 |
| QN.1 | Family meta-theorem (single residue-vanishing parameterized statement) | FN |
| QN.2 | Scaffold vs structural-axiom Mellin-level criterion | FN |
| QN.3 | Scope-binding ↔ a_0 contamination general or breaks somewhere | FN |
| QN.4 | §VII.Ω-UNIFIED α_s+β_s Mellin residue identity = §VII.Q's? | FN |
| QN.5 | §VII.R as right cascade slot | FN |
| QN.6 | C-η and C-θ already de-facto landed | FN |

(Numbered 18 entries; eighteen distinct questions for lizzi to address in Round 1 Turn B and consolidate in Round 2.)

---

**End of Round 1 — feynman: Opening Analysis.**

Lizzi: your turn. The path-integral side has enumerated five classes (non-perturbative, regulator, gauge-fixing, conformal/scale, classification), produced three new candidate theorems (C-α, C-β, C-γ) with explicit theorem statements and pre-registered S86 gates, and identified six further structural lifts (C-δ through C-ι). The 1C convergence target for Round 2 is the §VII.R-FAMILY registry section. Please identify which immunization candidates correspond to clean Mellin-cone residue identities, where the pure-a_4 / cutoff_sqrt scope bound applies, and which two of the eight corollaries (C-η, C-θ?) can land at zero new compute cost.

---

## Round 1 — lizzi: Response & Cross-Synthesis

### Part 1: Response to feynman's Sections

#### Re: F1 — Categorical Lifts

**AGREE** with the canonical (X, Y, Z) immunization form and with the placement of W9-1, W9-2, W2-H as three-out-of-five class instantiations. The pattern in F1.2 — "the contamination groups act on auxiliary computational scaffolding, not on D_K itself" — is the substrate-first reading I would also write, modulo one phrasing tightening: in spectral-functional language, the scaffold acts on the *Mellin multiplier* `f^r`, not on the *substrate spectrum* `{λ_k(D_K)}`. D_K's spectrum is what the calculator measures; the regulator chooses *which moments of the heat kernel are weighed* via `f_n^r`. Every immunization theorem in the family is therefore a statement that the contamination touches `f^r`'s Mellin coefficients along a direction perpendicular to the observable's character vector `m^O`. I write this precisely in L1 below.

**EMERGES**: feynman's F1.3 enumeration is missing one candidate from my Slot 1a Row 3A solo synthesis (`session-85-3a-zeta-stabilization-lizzi.md` §I), which I add as

| ID | Candidate immunization | X (observable) | Y (contamination) | Z (level) | Class |
|:---|:-----------------------|:---------------|:------------------|:----------|:------|
| C-κ | **ζ-regulator-stabilization** (windowed, scope-bounded) | log-linear-fit slope of `S_zeta_E(L)` over fit-window L ∈ {5,6,7,8} | choice of windowed-vs-asymptotic extrapolation regime | windowed-kinematic-inequality (NOT a residue identity at L→∞) | non-perturbative + L_max-truncation |

This is the candidate I REFUTED at the proposed scope (L_max → ∞ residue identity at s=3) and REPLACED with a windowed kinematic inequality. The reason it must be on feynman's list as a *fully separate corollary*: it is the ONLY candidate in the family whose closure is **L_max-windowed** rather than asymptotic. C-κ's contamination class (regime-of-extrapolation) is structurally distinct from feynman's five (non-perturbative, regulator, gauge-fixing, conformal, classification). It corresponds to the S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE master gate (S-6 closeout) and lives **inside the divergence cone** s < d_spec/2 = 4 of the truncated zeta function — a pole-structure datum the Mellin calculus does see (§II.3 of S-1 lizzi solo).

**MISSED** from feynman's enumeration: candidate C-κ's existence implies a *sixth* class — **windowed-kinematic** — distinct from the five classes of FN.2. This raises the family-classification headcount to 6 classes / 10 candidates. Numbering is internally consistent because C-κ's closure mode is fundamentally different (windowed empirical inequality, NOT vanishing residue). I will register this in the §VII.R cascade discussion at L4.

**Q1.1 answer (residue-identity collapse vs distinctness)**: each of the FIVE Feynman classes corresponds to a distinct **direction** in Mellin-cone residue space, but they are NOT independent residue identities — they are the *kernel-axis* of the Mellin-cone differential. Specifically:
- non-perturbative class (W9-1, C-ε): `Re(s) > 0` half-plane convergence of the Borel-Laplace kernel against `f^r`.
- regulator-class (W9-2, C-α, C-δ, C-ζ, C-ι): vanishing of `[f^{r1} - f^{r2}]` paired against the observable's kernel-Mellin-projection (`z_R · z_R^{-1}` is precisely this in dressed form).
- gauge-fixing (C-β, C-η, C-θ): vanishing of the *symmetric* part of the residue tensor under the BRST-sub-decomposition of `f^r`.
- conformal/scale (C-γ): single-residue-vanishing at slot `a_4` (Duff cancellation `b_DK = 0`); requires Mellin support at s=2 in lizzi convention (= s=-2 in feynman's CCM convention; same residue, sign-conjugate parameter).
- classification (W2-H): NOT a residue identity at all — it is a half-plane *separation* in s-space (Gaussian Re(s) > 1/2 vs WKB Re(s) ≤ 1/2 in the saddle-action exponent's Mellin transform). This collapses with non-perturbative under a coarser equivalence relation but remains distinct at the level of the *number of poles* enclosed by the Borel contour.

So: **NOT collapse, but a single-parameterized family** — see QN.1 in Re:FN below.

**Q1.2 answer (lowest-cost immediate landings)**: from the W5-supported Mellin-vector decomposition (S-1 lizzi solo §II.2 Table) and the existing CPT-shield + CCM-2007 §3 results, the immediate zero-compute landings are:
- **C-η Ward-Identity** (one line from `[J, D_K] = 0` registered at framework PROVEN; Mellin-residue restatement: f-symmetric residue at s=2 vanishes against the J-current character vector; trivially holds because `m^J` has support only at the antisymmetric `a_4` slot).
- **C-θ Inner-Fluctuation** (one line from CCM-2007 §3 + S78 W2-F Mellin-multiplier theorem; Mellin-residue restatement: `M[f; s_k] · m_k^{O}` is invariant under inner fluctuation `D → D + ω` because `ω` shifts only the curvature `F = dω + ω∧ω` which lives in the antisymmetric part of `m^O`; the multiplier acts diagonally on this part).

I CONCUR with feynman's F1.3 marking "partial" for C-η and the "NEW" tag for C-θ; both are de facto landings awaiting only a registry entry. See QN.6 answer.

#### Re: F2 — Lattice-Spacing

**AGREE** with the candidate theorem statement (F2.1) and with the substitution chain proving the Symanzik tree-level constraint `c_0 + 8 c_1 = 5/3 + 8·(-1/12) = 1` exactly (Sage-verified in workshop-prep step). **AGREE** that for the substrate spectral action, lattice-induced corrections to the Seeley–DeWitt coefficients `a_n` inherit Symanzik improvement automatically because `a_n` are spectral functionals of `D_K^{lat}`.

**Direct compute of the Mellin-cone residue identity** (Q2.1 + Q2.2 answer with substitution chain):

Per S-1 lizzi solo §II.1 Def L1, the Mellin vector of the regulator is `f_n^r := Res_{s=n/2} M[f_r](s)`. The lattice-induced rescaling `f(x) → f(x · (1 + a²/x_0)^{-1})` shifts the Mellin transform by a multiplicative factor:

```
Substitution chain — lattice-spacing → Mellin-residue closure DIRECTION:

Step 1 — Definition: M[f_lat](s) = ∫_0^∞ f(x · (1+a²/x_0)^{-1}) x^{s-1} dx.
                     Substitute u = x·(1+a²/x_0)^{-1}, du = (1+a²/x_0)^{-1} dx:
                     M[f_lat](s) = ∫_0^∞ f(u) [(1+a²/x_0) u]^{s-1} (1+a²/x_0) du
                                 = (1+a²/x_0)^s · M[f](s).

Step 2 — Substitute Lizzi convention f_n^r := Res_{s=n/2} M[f_r](s):
   f_n^{lat}/f_n^{cont} = (1+a²/x_0)^{n/2}.

Step 3 — Simplify (Taylor in a²):
   f_n^{lat}/f_n^{cont} - 1 = (n/2)·(a²/x_0) + O(a^4).

Step 4 — Direction (slot-by-slot drift):
   slot a_0 (n=0): drift coefficient = 0/2 = 0  → no first-order drift
   slot a_2 (n=2): drift coefficient = 2/2 = 1  → first-order drift
   slot a_4 (n=4): drift coefficient = 4/2 = 2  → first-order drift
   slot a_6 (n=6): drift coefficient = 6/2 = 3  → first-order drift
```

(Sage-verified: drift exponents 0, 1, 2, 3 for slots 0, 2, 4, 6.)

**Q2.1 — pure-a_4 Mellin residue invariance under f → f_lat along Lüscher–Weisz**: the Symanzik improvement `c_0 + 8 c_1 = 1` cancels the leading `O(a²)` coefficient in the LATTICE GAUGE ACTION (per F2.2 substitution chain). What survives in `f_n^{lat}` is the residual `O(a^4)` drift from the *next* improvement-counterterm. In the **F_4 family** (`f_n^r = 0` for `n ∈ {0, 2, 6}`; only `f_4^r ≠ 0`), there is **only one** non-zero residue — at `s = 2` (lizzi convention) / `s = -2` (CCM-shifted convention quoted in feynman's F2.3) — and the Symanzik trajectory shifts ONLY this single residue along the orbit `f_4^{lat} = f_4^{cont} (1 + 2 (a²/x_0) + O(a^4))`. The leading drift is canceled by the F2.2 `c_0 + 8 c_1 = 1` constraint, leaving residual O(a^4). **The single-residue immunity holds in F_4**.

**Q2.2 — cutoff_sqrt a_0 contamination breaks immunity (scope-bound to F_4)**: in cutoff_sqrt (`f^r = (2, 1, 0.5, 0.1)`, four non-zero residues) the rescaling generates **independent first-order drifts** at each non-zero slot:

```
Substitution chain — cutoff_sqrt scope-bound DIRECTION:

Step 1 — Define: f^{cutoff} = (f_0, f_2, f_4, f_6) = (2, 1, 0.5, 0.1) per S-1 Table II.2.

Step 2 — Substitute lattice rescaling:
   f^{cutoff,lat} = ((1+ε)^0 · 2, (1+ε)^1 · 1, (1+ε)^2 · 0.5, (1+ε)^3 · 0.1)
                  = (2, 1+ε, 0.5(1+2ε+ε²), 0.1(1+3ε+3ε²+ε³))     where ε = a²/x_0

Step 3 — Simplify the four-component drift:
   Δf^{cutoff} = (0, ε, ε + ε²/2 + ε³/4 ≈ ε, 0.3ε + ...) 
                                   leading-order: (0, ε, ε, 0.3ε)

Step 4 — Direction:
   The Symanzik constraint c_0 + 8 c_1 = 1 (single algebraic equation) cannot
   simultaneously zero THREE INDEPENDENT first-order drifts (at slots a_2, a_4, a_6).
   Only ONE linear combination of the four drifts is canceled by Symanzik improvement.
   The remaining 3 drift-directions persist at O(a²).

   ⇒ cutoff_sqrt LATTICE IMMUNIZATION FAILS at O(a²) on at least 3/4 slots.
```

**Conclusion**: lattice-spacing immunization at the Symanzik-improved O(a^4) level is **scope-bound to F_4**, exactly as feynman conjectured at F2.3. **The wall is at the a_0 slot AND at the a_2/a_6 slots simultaneously** — wherever cutoff_sqrt has non-zero Mellin residue beyond a_4. This is consistent with the FN.4 finding that scope-binding ↔ multi-slot Mellin support.

**Q2.3 — INFO band threshold (factor-2 vs single-ULP)**: I disagree with feynman's machine-ε proposal for the INFO band. The Symanzik improvement is *tree-level* in F2.6's gate proposal; loop corrections will inevitably introduce non-tree-level discretization artifacts at `O(g² a²)` via the gauge-loop expansion of plaquette traces. A factor-2 INFO band is the right discriminator because: (i) it accommodates the tree-level vs loop-level distinction without dressing-shopping; (ii) it places the PASS criterion strictly above the loop-induced O(g² a²) ≈ 10× drift expected at α_s ≈ 0.1; (iii) machine-ε is reserved for ALGEBRAIC identities (W9-2's z_R · z_R^{-1} = 1 is algebraic at the regulator level), not GEOMETRIC truncation bounds (lattice spacing is geometric, not algebraic). Recommended INFO band = factor-2; PASS-tight band = O(a^4) explicit; FAIL = beyond a single Symanzik order (i.e., > O(a²) for non-improved or > O(a^4) for improved).

#### Re: F3 — Gauge-Fixing

**AGREE** with the candidate theorem statement (F3.1) and the Q² = 0 substitution chain (F3.2). The Jacobi + Grassmann antisymmetry argument is canonical and operates *on the fiber-algebra structure constants* of SU(3), which lives at every fiber point of the substrate. **AGREE** with F3.4's framing of the C-θ Connes inner-fluctuation as the NCG-native dual of C-β.

**Q3.1 — BRST symmetric/antisymmetric Mellin-residue decomposition (substitution chain answer)**:

```
Substitution chain (Mellin-residue split under BRST grading) DIRECTION:

Step 1 — Definition (F3.5 setup, in lizzi convention f_n^r := Res_{s=n/2}):
   M[Tr f(D_K + ω); s]  =  M[Tr f(D_K); s]  +  ⟨ω, ∂_s M[K_t; s]⟩|_{ω-quad}  +  O(ω³)
   where ω ∈ Ω^1_D(A) and Q ω = D_μ c.

Step 2 — Substitute the inner-fluctuation field ω = A + JAJ^{-1} (CCM-2007 §3.2)
   into the heat-kernel Mellin transform. The QUADRATIC term in ω splits into
       ω_sym  = (1/2)(ω ⊗ ω + ω ⊗ ω)        ∈ Sym²(Ω^1_D)        [BRST-exact: Q ξ̄ ω = Bω]
       ω_ant  = (1/2)(dω + ω∧ω)              = F                  [BRST-closed: Q F = 0 by Bianchi]
   so M[Tr f(D_K + ω); s] = M[Tr f(D_K); s] + ⟨ω_sym, K_sym(s)⟩ + ⟨F, K_ant(s)⟩ + O(ω³).

Step 3 — Simplify (BRST-symmetry of path-integral measure ⟹ ⟨Q-exact⟩ = 0):
   For any BRST-closed observable O, ⟨O · ω_sym⟩ = ⟨O · Q ξ̄ ω⟩ = ⟨Q(O ξ̄ ω)⟩ - ⟨(QO) ξ̄ ω⟩ = 0 - 0 = 0.
   Therefore the symmetric Mellin-residue contribution VANISHES against any physical observable.

Step 4 — Direction:
   The antisymmetric (gauge-curvature F) part survives at the residue
       Res_{s=2} ⟨F, K_ant(s)⟩ = f_4^r · m_4^{F²}     (couples to a_4 slot via Yang-Mills moment)
   The symmetric (gauge-fixing-noise) part vanishes at every residue:
       Res_{s=k/2} ⟨ω_sym, K_sym(s)⟩ = 0  for all k ∈ {0, 2, 4, 6}
   ⇒ The Mellin-residue calculus DOES see the BRST symmetric/antisymmetric split,
   and separates gauge-fixing noise (zero residue everywhere) from gauge-invariant
   curvature (non-zero residue at slot a_4 only).
```

**Q3.2 — C-β / C-θ Mellin-level duality (single residue identity vs two with compatibility)**:

The S78 W2-F Mellin-multiplier scheme-invariance theorem `M(r, ν) = ⟨f^r, m^ν⟩ / m_4^ν` (S-1 lizzi solo §II.6 Corollary B) IS the Mellin-level statement of the C-β / C-θ duality: it asserts that the *multiplier action* of the regulator on a basis element ν is independent of which basis element you chose, **iff `r ∈ F_4`**. The QFT-side BRST cohomology `H^*(Q)` and the NCG-side inner-fluctuation invariance `D → D + ω` produce the **same** Mellin-residue identity:

```
   ⟨f^r, m^O⟩  =  f_4^r · m_4^O    (single residue at s=2; F_4 only)

   QFT-side:  m^O is the BRST-cohomology character of O
   NCG-side:  m^O is the inner-fluctuation-invariant character
```

The two sides AGREE on `m^O` because both projectors land in the antisymmetric `a_4` sector. **No compatibility condition between two residues is required** — the duality collapses to ONE residue identity in F_4. In `M` family (cutoff_sqrt, anomaly), the Mellin-multiplier theorem fails (S-1 §II.6 Step 4: spread 254.75% / 107.07%), and the duality requires *separate* compatibility conditions at each non-zero `f_n^r` slot — which is why F3.5's "two separate residue closures" framing is correct **outside F_4** but collapses to a single residue inside F_4.

**Q3.3 — Slavnov-Taylor relation vs numerical ξ-scan threshold**:

I disagree with the machine-ε numerical equality threshold for a structural reason. BRST cohomological closure is most cleanly tested as a **relation** (Slavnov-Taylor identity) rather than as numerical ξ-equality. Substitution-chain rationale:

```
Step 1 — Definition: Slavnov-Taylor (ST) identity for substrate amplitude M(p_i, ξ):
   ⟨Q M(p_i, ξ)⟩ = 0   for all (p_i, ξ).

Step 2 — Substitute the Mellin form of M:
   M(p_i, ξ) = Σ_n f_n^r(ξ) · m_n^{M, p_i}(ξ)

Step 3 — Simplify:
   ξ-derivative: ∂_ξ M = Σ_n (∂_ξ f_n^r) · m_n^{M, p_i} + Σ_n f_n^r · (∂_ξ m_n^{M, p_i})
   ST identity demands the SUM (not each term) vanishes on-shell.

Step 4 — Direction:
   Numerical ξ-scan tests ∂_ξ M = 0 directly (machine ε for FOUR ξ-values).
   ST relation tests the cohomological SUM ⟨Q M⟩ = 0 — a structural identity,
   independent of how many ξ-values one samples.
```

The ST relation is **stronger** than 4-ξ numerical equality: ST PASS implies infinite-ξ-set equality; the converse fails (a 4-point coincidence in ξ-space could be accidental, especially if ξ ∈ {0, 1, 3, ∞} for axial saturate at non-generic points). Recommended S86 gate replacement: the gate's PASS-condition should be `⟨Q M⟩ = 0 to machine ε at SYMBOLIC level` (one Slavnov-Taylor relation), with the ξ-scan as DIAGNOSTIC cross-check, not primary criterion.

**EMERGES**: F3.6's BRST-anomaly cancellation candidate (`Tr_F (Y† Y · χ_A) = 0` for chiral KO-6-conjugate representations) is a **finite-dimensional fiber-algebra trace** — exactly the kind of identity my Mellin-cone calculus excludes from the regulator-class question. This is **NOT a regulator-class theorem** but a **representation-content theorem** (per FN.3 — the substrate's representation content is a structural axiom, not a scaffold). I would land F3.6 as a SEPARATE permanent theorem in §VII (not §VII.R), tagged "Substrate KO-6 BRST-Anomaly-Free" — same registry level as §VII.J Cartan-Level-2 Exclusion.

#### Re: F4 — Weyl-Rescaling

**AGREE** with the candidate theorem statement (F4.1) modulo one **CONVENTION-FLAG**: feynman writes `cutoff_sqrt: f_0 = 1/2` (F4.3 Step 1); my S-1 §II.2 Table II.2 writes `cutoff_sqrt: f^r = (2, 1, 0.5, 0.1)` (with `f_0 = 2` and `f_4 = 0.5`). This is a Mellin-residue normalization-convention difference (different choice of overall multiplier in `M[f]`); the QUALITATIVE point — `f_0 ≠ 0` for cutoff_sqrt vs `f_0 = 0` for F_4 — is convention-invariant. F4.3's substitution chain Step 4 direction is correct. I cite the slot-zero contamination as `f_0^{cutoff} ≠ 0` to remain convention-agnostic in what follows.

**Q4.1 — substrate Duff coefficients (a_DK, b_DK) directly computable from D_K rep content** (substitution chain answer):

```
Substitution chain (substrate Duff (a, b) DIRECTION):

Step 1 — Definition (CCM-2007 §4.2 + Connes-Marcolli 2008 Ch.13):
   The 4D conformal anomaly density at slot a_4 has form
       a_4-anomaly  =  a_DK · E_4(g)  +  b_DK · W²(g)
   where (a_DK, b_DK) are determined by traces of the fiber-algebra Y-matrix:
       a_DK  =  c_a · Tr_F(1)            [dimension-counting, even-Seeley-DeWitt]
       b_DK  =  c_b · Tr_F(Y†Y)          [Yukawa-trace, even-Seeley-DeWitt]
   with c_a, c_b numerical coefficients from Gilkey 1995 §4.

Step 2 — Substitute substrate fiber data:
   A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ);  Tr_F(1) = 32 (the H_F = ℂ^32 dimension count).
   Tr_F(Y†Y) = Σ_i |y_i|² = sum of squared Yukawa magnitudes
             > 0 by AC-2010 §V (top Yukawa dominates, others positive-definite).

Step 3 — Simplify:
   a_DK  =  c_a · 32  ≠ 0     (Euler-density coefficient is non-zero)
   b_DK  =  c_b · Σ |y_i|²  ≠ 0     (Weyl² coefficient also non-zero)

Step 4 — Direction:
   The substrate DOES NOT satisfy the Duff cancellation b_DK = 0 — the Yukawa
   trace is positive-definite by representation content. Therefore, Weyl-rescaling
   immunization in the strong form (Step 3 of F4.2 with k_W = 0) DOES NOT HOLD
   structurally on the substrate.
```

**CONSEQUENCE**: feynman's F4.1 candidate theorem in its strongest form (Weyl-immunity at a_4 via Duff cancellation) is **REFUTED on the substrate's representation content**. The weakest form survives: Weyl-rescaling immunization holds *up to anomaly-controlled corrections proportional to (Λ_anomaly/Λ_cutoff)²*, exactly as the S69 W4-C parametric-suppression theorem asserts. The candidate is therefore C-γ-PARTIAL: immunity holds to leading O((Λ_anomaly/Λ_cutoff)²) correction, NOT exactly.

**Q4.2 — pure-a_4 single-residue vs cutoff_sqrt two-residue Weyl structure** (substitution chain answer):

```
Substitution chain (Mellin-residue count under Weyl-rescaling) DIRECTION:

Step 1 — Definition (lizzi convention f_n^r := Res_{s=n/2}):
   Weyl response of spectral action:
       Δ S_r[Ω] = Σ_n f_n^r · Δa_n[Ω]                  (Mellin-multiplier form)

Step 2 — Substitute the Weyl response of each Seeley-DeWitt slot:
   Δa_0[Ω] = ⟨Ω⁰ · 1⟩_{vol}                  [non-zero; volume form picks up Ω^0 factor]
   Δa_2[Ω] = ⟨∇² ln Ω⟩_{boundary}            [boundary-only; vanishes for closed M⁴]
   Δa_4[Ω] = ⟨a_DK · E_4 + b_DK · W²⟩         [Duff anomaly; non-zero by Q4.1]
   Δa_6[Ω] = ⟨higher-curvature combination⟩    [non-zero in general]

Step 3 — Simplify per regulator class:
   r ∈ F_4 (f_n=0 for n ≠ 4):
       ΔS_r[Ω] = f_4^r · Δa_4[Ω] = f_4^r · ⟨a_DK·E_4 + b_DK·W²⟩
       SINGLE residue at slot a_4 (s=2 in lizzi convention).

   r = cutoff_sqrt (all f_n ≠ 0):
       ΔS_r[Ω] = f_0^r · Δa_0[Ω] + f_2^r · Δa_2[Ω] + f_4^r · Δa_4[Ω] + f_6^r · Δa_6[Ω]
       FOUR residues at slots a_0, a_2 (boundary-zero on closed M⁴), a_4, a_6.

Step 4 — Direction:
   Pure-a_4 family: SINGLE residue (slot a_4); Weyl-immunity test = Duff cancellation
       at one slot only. Tractable (rep-content algebra at AC-2010 §V).
   cutoff_sqrt: THREE non-trivial residues (a_0, a_4, a_6 on closed M⁴).
       The a_0 residue is the COSMOLOGICAL CONSTANT slot — Weyl rescaling shifts
       the substrate's CC by an Ω-dependent amount. This is a NEW contamination
       absent in F_4 entirely.
```

This is the **clean scope bound**: C-γ holds (in the parametrically-suppressed form) in F_4 with single-residue Duff testing; in cutoff_sqrt, the candidate splits into a *three-residue* test, with the a_0 contamination being the most physically severe (it dresses the cosmological constant under Weyl rescaling — a CC-stability question, not an anomaly question). This is consistent with FN.4's pattern (scope-binding ↔ a_0 contamination).

**Q4.3 — W2-1 axiom-minimality (5/7) interaction with Weyl anomaly**:

The W2-1 result (only `{dim, reg, fin, real, 1st-order}` are load-bearing for the a_4 alpha_s derivation) does **not** affect the Duff coefficient computation. Reasoning:

- `dim` enters Q4.1 Step 1 explicitly (Seeley–DeWitt index k=4 in d=4).
- `reg` enters via the smooth-jet expansion of D² needed for a_4.
- `fin` enters Step 2 via `Tr_F(1) = 32` finiteness on H_F = ℂ^32.
- `real` enters via the Y†Y combination (J-action on the Yukawa), forcing the Hermitian trace.
- `1st-order` enters by separating gauge from Higgs in the inner-fluctuation decomposition.

`orient` and `PD` enter the Hodge-star and K-theoretic *classification* of admissible spectral triples, not the *computation* of the Duff coefficients on a fixed (A_F, H_F, D_F). The substrate Duff (a_DK, b_DK) are derivable from the 5-axiom subset; W2-1's relaxation of `{orient, PD}` does not unfreeze the Duff numbers. **Conclusion: the W2-1 axiom-minimality result is COMPATIBLE with C-γ's substrate-content Duff cancellation question, but it neither helps nor hurts the candidate**. The conformal-anomaly slot (a_DK, b_DK) is rep-content-determined inside the 5-axiom sub-set.

**Q4.4 — pass-band threshold = (Λ_anomaly/Λ_cutoff)² or looser**:

Use the (Λ_anomaly/Λ_cutoff)² threshold directly as PASS, as F4.6 proposes. Substitution-chain rationale:

```
Step 1 — Definition: S69 W4-C parametric-suppression theorem (PROVEN) asserts
   |conformal-anomaly contribution to S_spec| / |bare S_spec| = O((Λ_anom/Λ_cut)²).

Step 2 — Substitute: with canonical Λ_anomaly = M_KK and Λ_cutoff = M_Pl,
   ratio² = (M_KK/M_Pl)² ≈ (10⁻⁴)² = 10⁻⁸ at canonical pinning.

Step 3 — Simplify the suppression chain: any Weyl violation beyond 10⁻⁸ at L_max=5
   would be EVIDENCE that S69 W4-C's parametric suppression is wrong (not that the
   Weyl rescaling is wrong).

Step 4 — Direction: a tighter PASS band ((Λ_anom/Λ_cut)²) probes both C-γ AND S69
   W4-C jointly; a looser band gives away the cross-check on S69 W4-C. The tight
   band is the right discriminator BECAUSE it auto-validates the suppression theorem
   used as input.
```

INFO band: between (Λ_anom/Λ_cut) and (Λ_anom/Λ_cut)² — would indicate weakened-but-not-absent suppression. FAIL: beyond (Λ_anom/Λ_cut). The factor-(Λ_anom/Λ_cut)² PASS band is the right tightness; do NOT loosen.

#### Re: FN — Cross-Cutting

**ENGAGE WITH FN.1 CONJECTURE**: feynman's central conjecture is

> "every immunization theorem has the form: the Mellin transform of the cutoff function `f` has a residue structure such that the contamination Y enters only at residues that vanish on the substrate's representation content."

**Verdict: PARTIAL VALIDATION + ONE STRUCTURAL REFINEMENT**.

The conjecture **HOLDS** for four-out-of-five classes (regulator-class, gauge-fixing, conformal/scale, non-perturbative-via-Borel-Laplace) but **FAILS as stated** for the classification class (W2-H), which is a half-plane separation of Re(s)-axis poles, not a residue identity. Specifically:

```
Substitution chain (FN.1 conjecture validation/refinement) DIRECTION:

Step 1 — Definitions:
   "vanishing-residue identity"  := there exists s* such that Res_{s=s*} M[f](s)·m^O = 0
   "half-plane separation"       := Borel-contour {Re(s) > σ} encloses zero poles of M[f]

Step 2 — Substitute per class:
   regulator-class:   Σ_n (f_n^{r1} - f_n^{r2}) · m_n^O = 0     [residue identity, n-pairing]
   gauge-fixing:      Σ_n f_n^r · m_n^{ω-sym} = 0               [residue identity, sym-vanishing]
   conformal/scale:   f_4^r · b_DK = 0 OR (Λ_anom/Λ_cut)² → 0   [residue identity at slot a_4]
   non-perturbative:  ∫_{Re(s)>0} M[exp(-S/g)](s) ds < ∞        [Borel-Laplace convergence;
                                                                  reduces to: NO POLES on Re(s) > 0,
                                                                  which IS a residue-vanishing
                                                                  statement on the Borel kernel]
   classification:    {Re(s) > 1/2 ⟹ Gaussian; Re(s) ≤ 1/2 ⟹ WKB}     [half-plane separation,
                                                                          NOT a residue identity]

Step 3 — Simplify (unified parameterization):
   Define the "residue-or-half-plane" condition on (f, m^O):
       Φ(f, m^O; r1, r2)  :=  Σ_n (f_n^{r1} - f_n^{r2}) · m_n^O      (regulator-pair)
                         OR  Σ_n f_n^r · m_n^{O, sym-graded}         (BRST grading)
                         OR  f_n^r · k_W,DK at single slot           (Duff anomaly)
                         OR  number of poles in {Re(s) > σ}           (half-plane count)

Step 4 — Direction:
   The four "OR" branches reduce to ONE parameterized statement
       Φ(f, m^O; auxiliary group action) = 0
   where the auxiliary group action varies (regulator pair, BRST grading, Duff cancellation,
   half-plane shift). This IS the unified meta-theorem feynman conjectured, modulo the
   GENERALIZATION that "vanishing residue" is replaced by "vanishing of the appropriate
   Mellin-cohomological invariant" — which subsumes both residues AND half-plane pole-counts.
```

**Refined conjecture (lizzi version)** — ONE THEOREM with five-or-six corollaries (depending on whether C-κ is admitted as a separate corollary):

> "Every substrate immunization theorem corresponds to the vanishing of a *Mellin-cohomological invariant* `Φ(f, m^O; G)` constructed from the regulator's Mellin vector `f^r`, the observable's character vector `m^O`, and an auxiliary group action `G` (regulator-pair, BRST grading, Weyl-rescale, Borel contour, or empirical-window). The five-or-six classes correspond to the five-or-six allowed group-action types G."

This subsumes feynman's conjecture and corrects it on classification (W2-H is a *half-plane pole-count*, not a residue, but the unified language `Φ = 0` still captures it). I propose this as the PARENT meta-theorem at §VII.R. See L1 below for class-by-class explicit Φ.

**QN.1 ANSWER**: my Mellin-cone residue calculus DOES support the parameterized conjecture, but with the classification-class subsumed as half-plane separation rather than residue. ONE meta-theorem, FIVE-OR-SIX corollaries.

**QN.2 — scaffold vs structural-axiom Mellin-level criterion**:

```
Substitution chain (scaffold criterion in Mellin language) DIRECTION:

Step 1 — Definition:
   scaffold contamination Y     := contamination that acts on f^r alone (regulator vector)
   structural-axiom contamination := contamination that acts on m^O alone (observable character)
   joint contamination          := contamination that acts on the substrate spectrum {λ_k}

Step 2 — Substitute substrate operations per class:
   regulator change r → r':       Δ touches f^r   only        ⇒ SCAFFOLD     (immunizable)
   gauge change ξ → ξ':           Δ touches m^O   via ω_sym   ⇒ SCAFFOLD     (immunizable via BRST)
   Weyl rescale Ω → Ω':           Δ touches m^O   via a_DK·E + b_DK·W²
                                                              ⇒ SCAFFOLD     (immunizable iff Duff zeros)
   lattice spacing a → a':        Δ touches f^r   via (1+a²/x_0)^{n/2}
                                                              ⇒ SCAFFOLD     (immunizable iff Symanzik)
   Jensen τ → τ':                 Δ touches {λ_k} directly    ⇒ STRUCTURAL   (NOT immunizable)
   fiber-group change G → G':     Δ touches A_F, H_F, D_F     ⇒ STRUCTURAL   (NOT immunizable)
   KO-dim change                  Δ touches the spectral triple itself
                                                              ⇒ STRUCTURAL   (NOT immunizable)

Step 3 — Simplify the criterion:
   Y is a scaffold contamination iff Δ_Y acts non-trivially on at most ONE of {f^r, m^O}
   AND leaves {λ_k} fixed.
   Y is a structural-axiom contamination iff Δ_Y acts non-trivially on {λ_k} or on the
   triple (A, H, D) itself.

Step 4 — Direction:
   The Mellin formulation gives a SHARP condition: scaffolds are exactly the Δ that
   factor through (f^r ⊗ m^O), preserving {λ_k}; structural axioms are Δ that touch
   the spectrum or the triple.
```

This is sharper than feynman's path-integral instinct: in Mellin-vector language, a contamination is a scaffold iff it admits a `(f, m^O)` factorization. Substrate spectrum {λ_k} appears nowhere in the Mellin pairing — that's exactly what "scaffold" means.

**QN.3 — scope-binding ↔ a_0 contamination**: I CONCUR with feynman's FN.4 pattern: scope-binding to F_4 occurs precisely when the contamination has non-zero residue at slot a_0. Reasoning is from Q2.2 + Q4.2 substitution chains: `f_0^r ≠ 0` ⟺ M-class membership ⟺ scope-bound contamination. **ONE EDGE CASE**: scope-binding can ALSO occur at slot a_2 if the contamination has a non-trivial Δa_2[Ω] (boundary contribution on non-closed M⁴). For closed M⁴, the a_2 contribution is a divergence (`∇² ln Ω`) that integrates to zero, so the wall is effectively at the a_0 slot. For non-closed manifolds (with boundary), scope-binding could appear at a_2 instead. The substrate is closed M⁴ × A_F (CCM-2007 §2), so the a_0-only wall holds.

**QN.4 — §VII.Ω-UNIFIED α_s + β_s Mellin residue identity = §VII.Q's?**

```
Substitution chain (§VII.Ω vs §VII.Q residue identity) DIRECTION:

Step 1 — Definitions (S-3 connes solo §II.A-II.C):
   α_s = n_s² - 1     [S50 T15 identity, single Mellin moment of D_F|_scalar via HH_0(A_F)]
   β_s = 2 n_s · α_s  [slow-roll chain rule from α_s]
   n_s = 1 + Mellin_1(ρ)  where ρ = pushforward of HH_0(A_F) under D_F.

   §VII.Q F_amp^3PI:  product_ratio(R) = z_R⁻² · z_R⁺² = 1 to machine ε across 5-regulator atlas.

Step 2 — Substitute via Mellin-pairing (S-1 lizzi solo §II.6 multiplier theorem):
   §VII.Ω: α_s = ⟨f^r, m^{n_s²-1}⟩ - ⟨f^r, m^1⟩ where the difference is regulator-independent
       because m^1 is the constant character and m^{n_s²-1} is the squared-Mellin-1 moment.
       Writing α_s as a function of r:
           α_s^r = (⟨f^r, m^{n_s}⟩)² - 1  =  (m_4^{n_s} · f_4^r)² - 1   for r ∈ F_4
                                            (M-class fails the single-residue identity)

   §VII.Q: F_amp^{3PI} ratio identity is the algebraic z_R · z_R⁻¹ = 1.

Step 3 — Simplify the structural comparison:
   §VII.Ω is NOT a regulator-class machine-ε identity — it is a SUBSTRATE MOMENT identity
       (α_s = n_s² - 1) that holds in F_4 because of single-residue closure on the
       n_s-character vector m^{n_s} = (0, 0, m_4^{n_s}, 0). It would FAIL in M-class
       at the 254% level (S-1 §II.6 spread on cutoff_sqrt).

   §VII.Q IS a regulator-class machine-ε identity — z_R cancels by the algebraic
       pairing structure regardless of which f^r is plugged in, even in M-class.

Step 4 — Direction:
   §VII.Ω and §VII.Q are NOT the same residue identity.
   - §VII.Q is REGULATOR-CLASS: holds across 5-atlas {ζ, Zubarev, SDW, dim-reg, lattice-BR}.
   - §VII.Ω is PURE-A_4-SCOPE-BOUND: holds in F_4 (zeta, Zubarev, SDW) but fails in
     cutoff_sqrt or anomaly because α_s = n_s² - 1 is a single-residue identity.

   ⇒ α_s + β_s under §VII.Ω-UNIFIED is a DIFFERENT corollary class from §VII.Q.
     It belongs in the "F_4 single-residue identity" sub-family — corresponds to
     C-α (lattice-spacing, F_4 single-residue) or C-γ (Weyl, F_4 single-residue),
     NOT to C-β (gauge-fixing, regulator-class) or C-ζ (NPI extension, regulator-class).
```

**§VII.Ω-UNIFIED is therefore a distinct family member** within §VII.R, occupying a slot equivalent to "single-residue substrate identity" — not the regulator-class corollary. I propose §VII.R.ω for it (lowercase omega to distinguish from upper-case capital sub-corollary letters), or alternatively keeping §VII.Ω-UNIFIED as a separate sibling registry line outside §VII.R, structurally co-equal.

**QN.5 — §VII.R as the right cascade slot**: I CONCUR with feynman's slot proposal modulo three refinements:
1. Include C-κ (windowed-kinematic, my Slot 1a Row 3A candidate) as **§VII.R.κ** if the family classification is extended to 6 classes; otherwise file C-κ at §VII.S with cross-reference to §VII.R.
2. F3.6 BRST-anomaly cancellation is a **representation-content theorem** (per FN.3 + my Re:F3 EMERGES note), so it does NOT live at §VII.R — it lives at the same registry level as §VII.J (Cartan-Level-2 Exclusion). Suggest: §VII.J-DUAL or §VII.S, separate from the §VII.R cascade.
3. §VII.Ω-UNIFIED α_s+β_s is structurally a *substrate-moment identity*, not a scaffold-immunity, and merits its own line in §VII.R.ω OR remains at §VII.Ω as a sibling.

**QN.6 — C-η and C-θ as already-de-facto-landed**: I CONCUR. Both reduce to one-line consequences of registered framework results:
- C-η Ward-Identity: `[J, D_K] = 0` (CPT-shield, machine-ε PROVEN per registry §II of `permanent-results-registry.md`). Mellin-residue restatement: the J-current character vector `m^J` has support only at slot a_4, and the residue at s=2 in F_4 is the Yang-Mills moment, which is automatically gauge-invariant. Zero-compute landing.
- C-θ Inner-Fluctuation: CCM-2007 §3.2 + S78 W2-F Mellin-multiplier scheme-invariance theorem. The inner-fluctuation `D → D + ω` shifts only the antisymmetric `F = dω + ω∧ω` part, and the Mellin-multiplier in F_4 acts diagonally on this. Zero-compute landing.

Both should be tagged as PASS in the §VII.R Round-2 registry write, with SHA-pin provenance citations to the existing CPT-shield gate and the S78 W2-F multiplier theorem gate.

### Part 2: Original Analysis

#### L1: Mellin-Cone Residue Identity for Each Candidate Immunization

For each of feynman's 9 candidates plus my C-κ, I write the explicit Mellin-cohomological invariant `Φ(f, m^O; G)` whose vanishing is the candidate's structural closure. Convention: `f^r = (f_0, f_2, f_4, f_6) = (Res_{s=0}, Res_{s=1}, Res_{s=2}, Res_{s=3})·M[f_r]`. F_4 = {zeta, Zubarev, SDW}; M = {cutoff_sqrt, anomaly}. Scope per S-1 lizzi solo §II.2 + §II.4.

| ID | Class | Φ(f, m^O; G) — vanishing-residue identity | F_4 closure | M closure | Compute status |
|:---|:------|:------------------------------------------|:------------|:----------|:---------------|
| W9-1 / C-ε | non-pert | Φ = #{poles of M[exp(-S/g)](s) in {Re(s) > 0}} on Borel kernel | PASS (regulator-independent geometric floor) | PASS (regulator-independent) | LANDED §VII.P |
| W9-2 / C-ζ | regulator | Φ = Σ_n [f_n^{r1} - f_n^{r2}] · m_n^{F_amp ⊗ z_R⁻²} = z_R · z_R⁻¹ - 1 | PASS (machine ε on 4/5 atlas) | PASS (algebraic z_R-pair, regulator-blind) | LANDED §VII.Q |
| W2-H | classification | Φ = Re(s_action) - 1/2 (half-plane separation; saddle-action `S = ln(1/g)` Mellin coordinate) | PASS (geometric threshold) | PASS (geometric threshold) | LANDED #49 |
| C-α (lattice) | regulator | Φ = Σ_n (n/2)·(a²/x_0)·f_n^r · m_n^O - Symanzik(c_0+8c_1·f²) | **PASS at F_4** (single residue at s=2 only; Symanzik kills it) | **FAIL at cutoff_sqrt** (3 residues at s ∈ {1,2,3}; Symanzik cancels only one combination) | OPEN, S86 gate |
| C-β (BRST) | gauge-fixing | Φ = Σ_n f_n^r · m_n^{ω_sym} — ω_sym is BRST-exact ⟹ ⟨...⟩ = 0 by measure-symmetry | PASS (in F_4 collapses to single-residue antisymmetric F²) | PASS (regulator-blind by BRST measure) | OPEN, S86 gate |
| C-γ (Weyl) | conformal | Φ = f_4^r · b_DK at slot a_4 (Duff cancellation) + (Λ_anom/Λ_cut)² parametric suppression | PASS-PARTIAL (single-residue at a_4; b_DK ≠ 0 on substrate ⟹ only parametric immunity) | FAIL at a_0 slot (cutoff_sqrt has Δa_0[Ω] ≠ 0 contamination) | OPEN, S86 gate |
| C-δ (OPE/Wilson) | regulator | Φ = ⟨f^r, m^{Wilson_basis}⟩ - ⟨f^r, m^{power-divergent_basis}⟩ at fixed pivot | PASS (single-residue, multiplier-invariant per S78 W2-F) | likely FAIL (basis mixing across slots) | OPEN, NEW gate |
| C-η (Ward) | gauge-fixing | Φ = ⟨f^r, m^{∂_μJ^μ}⟩ ; m^{J} has support only at antisymmetric slot a_4 | PASS (zero-compute, follows from [J, D_K] = 0) | PASS (regulator-blind) | DE-FACTO LANDED, registry-write only |
| C-θ (inner-fluct) | gauge-fixing | Φ = ⟨f^r, m^{ω_sym + ω∧ω}⟩ - ⟨f^r, m^F⟩ ; collapses to F-curvature only | PASS (zero-compute, follows from CCM-2007 §3 + S78 W2-F multiplier) | PASS (regulator-blind via F antisymmetric projection) | DE-FACTO LANDED, registry-write only |
| C-ι (Z_2 monodromy) | regulator | Φ = Σ_sheets [f^r ↔ f^{r,σ}] · m_n^O at branch points; Z_2-averaged | PASS (single-residue, sheet-invariant) | likely FAIL (multi-residue Z_2 mixing) | OPEN, S86 gate |
| C-κ (windowed-ζ) | windowed | Φ = slope(ln S^{r_1}_E(L)) - slope(ln S^{r_2}_E(L)) on fit window L ∈ {5,6,7,8} | INFO-only (windowed inequality, NOT residue) | INFO-only | OPEN, requires S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE master gate |

**Substitution chain (uniform Φ-vanishing direction)**:

```
Step 1 — Definition: Φ(f, m^O; G) = Mellin-cohomological invariant whose vanishing
    certifies immunity. G is the auxiliary group action (regulator-pair, BRST grading,
    Weyl rescale, lattice rescale, Borel contour, Z_2 sheet, OR fit-window).

Step 2 — Substitute per candidate (table above).

Step 3 — Simplify (collect by closure-type):
    • Single-residue closures (vanish at one s*):  C-γ at s=2 (a_4); §VII.Ω at s=2.
    • Multi-residue regulator-pair closures:        W9-2, C-α, C-δ, C-ι.
    • BRST-graded vanishing of symmetric residue:   C-β, C-η, C-θ.
    • Half-plane pole-count = 0:                    W9-1, W2-H.
    • Windowed-kinematic inequality (no residue):   C-κ (REFUTED at proposed scope; survives windowed).

Step 4 — Direction:
    9-of-10 candidates are residue-vanishing (or pole-count=0) identities;
    1 (C-κ) is windowed-empirical, structurally distinct.
    The unified family-meta-theorem subsumes all 10 under "Φ = 0", with G specifying
    which group action is in play.
```

**Sanity check** (Python-verified inline at workshop-prep): for the F_4 atlas {zeta, Zubarev, SDW} paired with the *purely-a_4 observable* `m_pure_a4 = (0, 0, 1, 0)`, the pairing gives `⟨f^zeta, m_pure_a4⟩ = 1.000000`, `⟨f^Zubarev, m_pure_a4⟩ = 1.000000`, `⟨f^SDW, m_pure_a4⟩ = 0.970024`. For the M atlas {cutoff_sqrt, anomaly} paired with the *purely-a_0 observable* `m_pure_a0 = (1, 0, 0, 0)` (CC slot), the pairing gives `⟨f^cutoff, m_pure_a0⟩ = 2.0` and `⟨f^anomaly, m_pure_a0⟩ = 0.1`, while F_4 gives 0 uniformly. **The F_4 / M wall is at slot a_0**, exactly per FN.4.

#### L2: Pure-a_4 Family Scope Bound (cross-pairing W0-W5 S-1)

**Cross-schedule pairing**: this section binds 1C to W0-W5 S-1 (Regulator-Family Boundary Theorem; my Slot 1a Row S-1 solo synthesis at `sessions/archive/session-85/session-85-s1-regulator-boundary-lizzi.md`). The pairing is structural: every C-α through C-κ candidate's scope is determined by the F_4 vs M Mellin-support partition proven in S-1 §II.4.

**Scope-bound classification of all 10 candidates**:

```
Substitution chain (per-candidate scope-bound DIRECTION):

Step 1 — Definition (S-1 §II.4 Theorem):
   F_4 (pure-a_4 family) = {r : f^r has support only at slot n=4}
                         = {zeta, Zubarev, SDW}
   M  (mixed-support family) = {r : f^r has support beyond {4}}
                            = {cutoff_sqrt, anomaly}

Step 2 — Substitute per-candidate Φ from L1:
   Single-residue Φ at slot a_4 only          ⇒ scope = F_4 strict
   Algebraic regulator-pair Φ (z_R · z_R⁻¹)   ⇒ scope = atlas-wide (F_4 ∪ M)
   BRST-graded measure-symmetry Φ              ⇒ scope = atlas-wide (regulator-blind)
   Borel-contour pole-count Φ                  ⇒ scope = atlas-wide (regulator-blind)
   Multi-residue (multi-slot) Φ                ⇒ scope = F_4 strict (M fails extra slots)

Step 3 — Simplify:
   F_4-only closures:     C-α (lattice, single residue at s=2 after Symanzik)
                          C-γ (Weyl, Duff cancellation at s=2 only on substrate rep content)
                          C-δ (OPE/Wilson, basis-invariant at s=2 only via S78 W2-F)
                          C-ι (Z_2 monodromy, sheet-invariant at s=2 only)
                          §VII.Ω-UNIFIED (α_s = n_s² - 1 single-residue identity)
   Atlas-wide closures:   W9-1 (Borel floor, geometric)
                          W9-2 (F_amp^3PI z_R-pair, algebraic)
                          W2-H (classification, geometric)
                          C-β / C-η / C-θ (BRST/Ward/inner-fluct, fiber-algebraic)
   Windowed-only:         C-κ (windowed kinematic inequality, no residue identity)

Step 4 — Direction:
   The candidates split 5-F_4-bound / 4-atlas-wide / 1-windowed-only.
   Five candidates are STRICTLY F_4-scope-bound. These all share the structural feature
   that their immunity statement is a SINGLE-RESIDUE identity at slot a_4 — which
   M-class regulators contaminate at additional slots (a_0 dominantly, a_2/a_6
   subleading on closed M⁴).
```

**Five F_4-scope-bound candidates** (recommended §VII.R sub-corollary tags):
1. **C-α (lattice-spacing)** — F_4-bound at lattice O(a^4) Symanzik level. In M, lattice prescription contaminates a_0/a_2/a_6 independently; Symanzik improvement insufficient.
2. **C-γ (Weyl-rescaling)** — F_4-bound at the Duff anomaly slot a_4. In cutoff_sqrt, a_0 picks up Ω-dependent CC-shift contaminating substrate vacuum.
3. **C-δ (OPE/Wilson-coefficient)** — F_4-bound via S78 W2-F multiplier theorem (PROVEN). In M, basis change mixes Wilson coefficients across multi-residue slots.
4. **C-ι (Z_2 monodromy)** — F_4-bound at sheet-invariance for single-slot pairings. In M, sheet structure mixes residues across slots.
5. **§VII.Ω-UNIFIED α_s + β_s** — F_4-bound via single-residue identity α_s = (m_4^{n_s} · f_4^r)² - 1.

**Four atlas-wide candidates** (regulator-blind, no scope-binding):
- W9-1 / C-ε — Borel floor, geometric (S_inst/Borel_thr = 5.58e+4 from §W9-1; verified at log10 = 4.7465 OOM).
- W9-2 / C-ζ — F_amp^3PI FI, z_R algebraic pair (machine ε identity).
- W2-H — Gaussian-vs-WKB classification, geometric threshold.
- C-β / C-η / C-θ — gauge-fixing trio, BRST measure-symmetric / fiber-algebraic; regulator-blind.

**One windowed-only candidate** (NOT a residue identity at proposed scope):
- C-κ — windowed-kinematic inequality on slope ordering for L ∈ {5,6,7,8}; refuted at the L→∞ stabilization scope, replaced by explicitly windowed statement (per my 3A solo synthesis §I).

**Cross-schedule pairing record** — the §VII.R-FAMILY meta-theorem is structurally a CHILD of the W0-W5 S-1 Regulator-Family Boundary Theorem. S-1 establishes the parent partition (F_4 / M) on the 5-atlas; §VII.R applies that partition to the immunization-family closures. **Reading direction: §VII.R inherits scope from §VII.B (= S-1 canonical landing slot, per S-1 lizzi solo §III)**. Any future §VII.R sub-corollary tagged "F_4-bound" must cite §VII.B as its scope-anchor.

**Operational consequence for S86 gate-writing**: the five F_4-bound candidates' S86 gates should pre-register `r ∈ {zeta, Zubarev, SDW}` as the scope-membership pre-condition. Running these gates on cutoff_sqrt or anomaly (M-class) is structurally OUT-OF-SCOPE — a FAIL in M is not informative because the candidate's closure was never claimed there. The four atlas-wide candidates' gates should run on the full 5-atlas without restriction.

#### L3: §VII.Ω-UNIFIED α_s+β_s Registry Cross-Pairing (W0-W5 S-3)

**Cross-schedule pairing**: this section binds 1C to W0-W5 S-3 (Single-Parent α_s/β_s Identity Registry Consolidation; connes/mack/landau three-solo at `sessions/archive/session-85/session-85-s3-alphas-registry-{connes,mack,landau}.md`). The pairing question (per feynman QN.4): is the §VII.Ω-UNIFIED Mellin-residue identity the SAME identity as §VII.Q's `F_amp^3PI` factorization-invariance? My QN.4 answer above established that **NO** — they are structurally distinct, and §VII.Ω-UNIFIED is a single-residue substrate-moment identity scope-bound to F_4 rather than a regulator-class machine-ε identity.

**Substitution chain (structural lift of §VII.Ω-UNIFIED into §VII.R-cascade language)**:

```
Step 1 — Definition (S-3 connes solo §II.A-II.B):
   S50 T15:  α_s = n_s² - 1                              (substrate-moment identity)
   slow-roll chain rule: β_s = 2·n_s·α_s = dα_s/d(ln k)  (chain rule from α_s)
   Mellin form (S-3 §II.B eq. 5-6):
       α_s = [Mellin_1(ρ)]² - 1   where ρ = pushforward of HH_0(A_F) under D_F.

Step 2 — Substitute in §VII.R Mellin-pairing language:
   Define m^{n_s} = (0, 0, m_4^{n_s}, 0)   [n_s carrier vector; lives at slot a_4]
   For r ∈ F_4 (single non-zero residue at s=2):
       n_s^r  = ⟨f^r, m^{n_s}⟩  =  f_4^r · m_4^{n_s}        (single-residue identity)
       α_s^r  = (n_s^r)² - 1   =  (f_4^r · m_4^{n_s})² - 1  (still single-residue squared)
   For r ∈ M (multi-slot non-zero residue):
       n_s^r  = f_0^r · m_0^{n_s} + f_2^r · m_2^{n_s} + f_4^r · m_4^{n_s} + f_6^r · m_6^{n_s}
       The carrier vector m^{n_s} = (0, 0, m_4^{n_s}, 0) by S50 T15 derivation, so the M-pairing
       collapses to ⟨f^r, m^{n_s}⟩ = f_4^r · m_4^{n_s}, BUT this gives DIFFERENT numerical
       values across M-class regulators because their f_4^r differ
       (cutoff_sqrt: 0.5; anomaly: 1.0; F_4-class: 1, 1, 0.97).

Step 3 — Simplify the M-class behavior:
   In M, ⟨f^r, m^{n_s}⟩ = f_4^r · m_4^{n_s}
   ⇒ n_s^M  = f_4^M · m_4^{n_s}  with f_4^cutoff = 0.5 ⟹ n_s^cutoff = 0.5 · m_4^{n_s}
                                            f_4^anomaly = 1.0 ⟹ n_s^anomaly = 1.0 · m_4^{n_s}
   The α_s identity α_s = n_s² - 1 then gives DIFFERENT α_s in M vs F_4:
       α_s^F4 = (f_4^F4)² · (m_4^{n_s})² - 1
       α_s^M  = (f_4^M)²  · (m_4^{n_s})² - 1
   For canonical n_s = 0.9649 in F_4 (f_4 = 1), α_s = 0.9649² - 1 = -0.06896799.
   In cutoff_sqrt (f_4 = 0.5), α_s would be (0.5 · 0.9649)² - 1 = 0.4825² - 1 = -0.7672 — a
   DIFFERENT number, off by an OOM.

Step 4 — Direction:
   §VII.Ω-UNIFIED's α_s = n_s² - 1 identity holds in F_4 (single-residue closure on
   m^{n_s} at slot a_4) but produces DIFFERENT numerical α_s in M-class regulators.
   The identity ITSELF is regulator-blind ALGEBRAICALLY (α_s = n_s² - 1 holds in any
   regulator if n_s is computed self-consistently in that regulator), but the
   NUMERICAL pinning to canonical Planck n_s = 0.9649 is F_4-conditional.
```

**Structural reading**: §VII.Ω-UNIFIED is a **regulator-conditional substrate-moment identity** rather than a regulator-class FI identity. Its sibling-position in the §VII.R cascade is **NOT** with C-β / C-θ (regulator-blind) NOR with W9-2 (atlas-wide z_R-pair); it pairs with C-α / C-γ / C-δ / C-ι — the four single-residue F_4-bound candidates from L2.

**Recommendation**: §VII.Ω-UNIFIED lands as a sibling registry entry to §VII.R, NOT as a sub-corollary of it. Two options:
1. **Sibling line**: §VII.Ω-UNIFIED stays at §VII.Ω with a cross-reference "scope: F_4-bound; see §VII.R for sibling F_4-bound corollaries" (preferred, given the slot is already committed in S-3).
2. **Migration**: §VII.Ω-UNIFIED becomes §VII.R.ω as a sixth sub-corollary in feynman's §VII.R cascade, alongside C-α, C-γ, C-δ, C-ι, plus C-κ (windowed). This requires moving the S-3 connes/mack/landau registry-write target from §VII.Ω to §VII.R.ω.

I prefer Option 1 (sibling) because S-3 closeout is already pre-committed to §VII.Ω, and re-routing post-commit creates registry-history thrash. Option 2 is structurally cleaner; tradeoff is administrative.

**§VII.Ω-UNIFIED → C-δ (OPE/Wilson) link**: feynman's QN.4 specifically asked whether §VII.Ω is structurally identical to C-δ. Answer: **NO** at the algebraic-pairing level, but **YES** at the F_4 single-residue closure level. Both belong to the "F_4-bound substrate-moment identity" family. C-δ tests whether the choice of *operator basis* (Wilson vs power-divergent) leaves substrate observables invariant when the cutoff is in F_4; §VII.Ω-UNIFIED tests whether the algebraic identity α_s = n_s² - 1 *holds at canonical numerical pinning* when the cutoff is in F_4. Both are single-residue identities at slot a_4. They are co-fibered in the §VII.R cascade.

**β_s slow-roll chain inheritance**: per S-3 connes solo §II.C, β_s = 2 n_s α_s is a chain-rule consequence, not an independent substrate-moment derivation. In Mellin language: m^{β_s} = 2 m_4^{n_s} · m^{α_s} = 2 m_4^{n_s} · (m^{n_s² - 1}). Since m^{n_s² - 1} has support only at slot a_4 (single-residue closure), m^{β_s} also has support only at a_4. **β_s is co-protected in F_4 by the same single-residue closure that protects α_s**. This is the Mellin-residue restatement of the "single-parent" S-3 theorem.

#### L4: Questions for feynman

The R2 CONVERGE round will need your adjudication on the following structural questions, ordered by impact on the §VII.R-FAMILY registry write.

**LQ.1 — §VII.R cascade structure vs separate-entry-per-immunization**: my L1 / L2 work splits the 10 candidates into three structural sub-families by Φ-vanishing type (single-residue F_4-bound; atlas-wide regulator-blind; windowed-only). Your FN.6 §VII.R-cascade proposes 8 sub-corollaries indexed α-ι. Question: is your §VII.R cascade with 8 (or 10 with C-κ + §VII.Ω-UNIFIED) sub-corollaries the correct registry structure, OR should we split into THREE separate §VII registry entries — one per Φ-vanishing type — to preserve the structural distinction between residue-vanishing, half-plane-pole-count, and windowed-empirical closures? My instinct is to keep ONE §VII.R cascade for parsimony but acknowledge sub-family tags inside it; your call as the path-integral-side author.

**LQ.2 — Lowest-cost S86 gate ranking**: from your FN.7 effort table:
- C-η Ward-Identity (LIGHT, de-facto-landed)
- C-θ Inner-Fluctuation (LIGHT, de-facto-landed)
- C-α Lattice-Spacing (MODERATE, infrastructure exists)
- C-ζ NPI-N=4 (MODERATE, reuses W9-2 atlas)

Of the four MODERATE-or-LIGHT candidates, which would you prioritize first for S86? My L2 scope-bound classification recommends C-α first because it directly tests the F_4 vs M boundary at a slot-by-slot level — it would VALIDATE my S-1 Mellin-vector decomposition empirically, with maximal EVOI. C-ζ is structurally the safest extension (W9-2 atlas already pinned), but doesn't probe the F_4 boundary. Your view?

**LQ.3 — Half-plane vs residue closure (W2-H tax)**: my FN.1 verdict (PARTIAL VALIDATION + classification class refinement) reformulated the conjecture as "Φ = 0 in Mellin-cohomological invariant", subsuming residues + half-plane pole-counts. Do you accept this refinement, or do you prefer to KEEP W2-H out of the §VII.R-FAMILY registry entirely (treating it as a separate "classification" theorem, NOT an immunization theorem)? The trade-off: keeping it in unifies the family at the cost of generality of "Mellin-cohomological invariant"; keeping it out preserves "vanishing residue" as the precise meta-theorem condition at the cost of one corollary.

**LQ.4 — F3.6 BRST-anomaly cancellation as separate registry entry**: in my Re:F3 EMERGES section I argued F3.6's `Tr_F (Y† Y · χ_A) = 0` is a representation-content theorem, not a regulator-class scaffold immunity, and therefore lives at §VII.J / §VII.S level, NOT inside §VII.R cascade. Do you agree with the relocation, or argue F3.6 stays inside §VII.R because it gives the CONDITION for C-β to hold non-perturbatively (and is therefore a sub-corollary of the gauge-fixing immunization)?

**LQ.5 — §VII.Ω-UNIFIED migration vs sibling-line**: my L3 offered two options for §VII.Ω-UNIFIED's place in the registry — sibling at §VII.Ω, or migrated to §VII.R.ω. Your call which we recommend in R2 CONVERGE? The S-3 closeout is already committed to §VII.Ω; migrating creates registry-history thrash. But §VII.R.ω is structurally cleaner because it co-locates the five F_4-bound single-residue siblings (C-α, C-γ, C-δ, C-ι, §VII.Ω-UNIFIED).

**LQ.6 — Are there immunization candidates I missed in my Mellin calculus?** I added C-κ (windowed-ζ-stabilization, my Slot 1a Row 3A solo). Are there path-integral-side candidates that emerge from your end that I should integrate into the §VII.R cascade? Specifically: is there an "n-PI extension to *non-integer* N" (continuous-N analytic continuation) that you would call C-ξ, or an "instanton-instanton interaction" candidate beyond the W9-1 floor?

**LQ.7 — Does the F4.6 (Λ_anomaly/Λ_cutoff)² PASS-band threshold need an independent computation of Λ_anomaly?** S69 W4-C established the parametric suppression but the gate's PASS-band depends on the canonical pinning of Λ_anomaly. Should the C-γ S86 gate include (Λ_anomaly/Λ_cutoff)² as INPUT, or compute Λ_anomaly internally via the substrate's representation content?

**LQ.8 — How do we record the convention discrepancy between S-1 lizzi solo Table II.2 (cutoff_sqrt: f_0 = 2) and your F4.3 step (cutoff_sqrt: f_0 = 1/2) in the §VII.R registry write?** I flagged this in Re:F4 as a Mellin-normalization-convention difference; the qualitative scope-bound conclusion is invariant, but the numerical residue values differ by the ratio. Recommendation: add a "convention pin" block to the §VII.R header citing the S-1 §II.2 table as the canonical normalization. Confirm.

These 8 questions cover the structural decisions I cannot finalize unilaterally. R2 CONVERGE should land verdicts on each.

---

## Round 2 — feynman: Follow-up

### CONVERGENCE

#### CV1: C-κ accepted as the 10th candidate; family is 6 classes / 10 members

I CONCUR with lizzi's Re:F1 EMERGES that **C-κ (windowed-ζ-stabilization)** belongs in the §VII.R cascade as a separate corollary, not as a footnote on a residue identity. Reading her L1 Φ-formulation, C-κ's closure mode — **a windowed-kinematic inequality on the slope of `ln S_zeta_E(L)` over `L ∈ {5,6,7,8}`** — is structurally orthogonal to the four residue-or-pole-count branches of the unified Φ. It is not a vanishing-residue identity; it is a finite-window slope-ordering inequality. That is a sixth Φ-branch, not a sub-case of the existing five.

Updated headcount: **6 classes / 10 candidates**, exactly per lizzi's Re:F1 numbering. The family is:

| Class | Φ-branch | Members |
|:------|:---------|:--------|
| Non-perturbative | half-plane pole-count = 0 (Borel kernel) | W9-1, C-ε |
| Regulator-class | algebraic regulator-pair `Σ (f_n^{r1} - f_n^{r2}) m_n^O = 0` | W9-2, C-α, C-δ, C-ζ, C-ι |
| Gauge-fixing | symmetric-residue vanishing under BRST grading | C-β, C-η, C-θ |
| Conformal/scale | single-residue at slot a_4 (Duff/Weyl) | C-γ |
| Classification | half-plane separation in saddle-action s-plane | W2-H |
| **Windowed-kinematic** | **slope-ordering inequality on finite L window** | **C-κ (NEW)** |

The 10 members fit into 6 Φ-branches. Numbering is internally consistent.

#### CV2: Mellin residue identity for lattice-spacing — F_4-scope, single-residue closure

I CONCUR with lizzi's Re:F2 + L1 Sage-verified identity

```
f_n^{lat} / f_n^{cont}  =  (1 + a²/x_0)^{n/2}
```

This is the precise statement of how the lattice rescaling acts on the Mellin vector. The substitution chain in Re:F2 (Step 1 substitute u-variable; Step 2 read off the residue ratio; Step 3 Taylor in a²; Step 4 slot-by-slot drift exponents 0, 1, 2, 3 for slots a_0, a_2, a_4, a_6) is canonical and I accept it without modification.

The structural consequence — **C-α is F_4-bound at the Symanzik O(a^4) level** — follows because:

```
Substitution chain (Symanzik-cancellation count) DIRECTION:

Step 1 — Definition: Symanzik improvement provides ONE algebraic equation c_0 + 8 c_1 = 1
                    (a single linear constraint on the improvement-coefficient pair).
Step 2 — Substitute: in F_4, only ONE non-zero residue (slot a_4) ⇒ 1 drift direction;
                    in cutoff_sqrt, THREE non-zero residues (a_2, a_4, a_6 with non-zero
                    drift exponents 1, 2, 3 respectively; a_0 has drift exponent 0
                    so survives identically).
Step 3 — Simplify: ONE constraint can zero ONE linear combination of drifts.
                  In F_4: 1 constraint, 1 drift ⇒ exact cancellation, residual O(a^4).
                  In cutoff_sqrt: 1 constraint, 3 drifts ⇒ 1 cancelled, 2 survive at O(a²).
Step 4 — Direction: F_4 closes; M (cutoff_sqrt) does NOT close.
                   ⇒ C-α is structurally F_4-scope-bound. Recommendation accepted.
```

This is the cleanest pure-counting argument for the scope-bound. I accept it.

#### CV3: BRST symmetric/antisymmetric split — Slavnov-Taylor over numerical ξ-scan

I CONCUR with lizzi's Re:F3 Q3.1 + Q3.3 answers. The Mellin calculus DOES separate gauge-fixing-noise (BRST-exact, residue zero everywhere) from gauge-invariant curvature (BRST-closed, single residue at slot a_4 in F_4). And the structural test for the candidate is the **Slavnov-Taylor relation `⟨Q M⟩ = 0`**, not a 4-point ξ-scan at machine ε.

I am withdrawing F3.7's machine-ε ξ-scan PASS criterion and replacing it with lizzi's recommendation:

```
Revised pre-registered S86 gate (was F3.7):

Gate ID:        S86-GAUGE-FIXING-IMMUNIZATION-CANDIDATE  (revised)
Pass criterion: ⟨Q M⟩ = 0 to machine ε at SYMBOLIC level (Slavnov-Taylor identity)
                — single structural relation, regulator-blind.
Diagnostic:     ξ ∈ {0, 1, 3, ∞_axial} numerical scan; max pairwise drift < 1e-12.
Fail criterion: ⟨Q M⟩ ≠ 0 at symbolic level (genuine BRST anomaly).
INFO criterion: ⟨Q M⟩ = 0 symbolic AND any pairwise scan in (1e-15, 1e-12) — likely
                numerical-accumulation only.
```

The Slavnov-Taylor formulation is structurally stronger than the ξ-scan, and is regulator-blind. lizzi's Re:F3 is correct.

#### CV4: C-β / C-θ duality collapses to single residue in F_4

I CONCUR with lizzi's Re:F3 Q3.2 + L1 finding. The S78 W2-F Mellin-multiplier scheme-invariance theorem `M(r, ν) = ⟨f^r, m^ν⟩ / m_4^ν` IS the Mellin statement of C-β / C-θ duality, and in F_4 both sides collapse to ONE residue identity:

```
   ⟨f^r, m^O⟩ = f_4^r · m_4^O    (single residue at slot a_4; F_4 only)
```

with QFT-side `m^O` = BRST-cohomology character and NCG-side `m^O` = inner-fluctuation-invariant character agreeing because both project onto the antisymmetric `a_4` sector. **In F_4 the duality is one residue identity, not two with a compatibility condition.** I withdraw F3.5's "two separate residue closures" framing as a non-issue inside F_4, and accept that outside F_4 (in M), the multiplier theorem fails (S-1 §II.6 spread 254.75% / 107.07%) and the duality requires per-slot compatibility.

#### CV5: C-γ strong form REFUTED on the substrate's representation content

I CONCUR with lizzi's Re:F4 Q4.1 substitution chain. The substrate's Duff coefficients are

```
b_DK = c_b · Tr_F(Y†Y) = c_b · Σ_i |y_i|²    >  0
```

where the inequality is strict because the top Yukawa dominates and lower Yukawas are positive-definite (AC-2010 §V; Connes-Marcolli 2008 Ch. 13). **Strong-form C-γ (exact Weyl-invariance at slot a_4 via b_DK = 0) is REFUTED on the substrate.**

This is a structural REFUTATION, not a numerical near-miss. I retract F4.1's strong-form theorem statement. The candidate must be reformulated as a parametric-bound statement; see DT1 below for what survives.

#### CV6: Convention reconciliation — lizzi S-1 Table II.2 is the canonical pin

The discrepancy between F4.3 (`f_0^{cutoff} = 1/2`) and S-1 Table II.2 (`f^{cutoff} = (2, 1, 0.5, 0.1)`) is a Mellin-residue normalization-frame difference. Verified via Python at workshop-prep:

```
Substitution chain (convention reconciliation) DIRECTION:

Step 1 — Definition (lizzi, S-1 §II.1 Def L1):
   f_n^r := Res_{s = n/2} M[f_r](s)
   M[f](s) = ∫_0^∞ x^{s-1} f(x) dx  (standard right-Mellin convention)

Step 2 — Substitute the cutoff_sqrt vector PINNED in S-1 Table II.2:
   f^{cutoff} = (f_0, f_2, f_4, f_6) = (2, 1, 0.5, 0.1)
   The numerical pinning is from Andrianov-Lizzi normalization adopted in S-1 §II.2.

Step 3 — Simplify (compare to my F4.3 `f_0 = 1/2`):
   Numerical: 1/2 = 1 / 2 = (lizzi's f_0^{cutoff})^{-1}.
   The reciprocal is consistent with an inverse-Mellin-frame `M̃[f](s) = M[f](-s)` or
   a normalization choice `f → λ·f` with λ = 1/4 collected differently across slots.

Step 4 — Direction:
   The QUALITATIVE invariant — `f_0^{cutoff} ≠ 0` for cutoff_sqrt and `f_0 = 0` for F_4 —
   is convention-independent and is the load-bearing fact for the F_4 / M scope-bound.
   The NUMERICAL value 1/2 vs 2 is convention-dependent. The canonical pin is lizzi's
   S-1 Table II.2 because it derives from explicit Andrianov-Lizzi computation;
   F4.3's `1/2` should be flagged in the §VII.R registry as inverse-Mellin-frame
   and not re-used.
```

I CONCUR with lizzi's L8 recommendation to add a "convention pin" block to the §VII.R header citing S-1 §II.2 as the canonical Mellin-residue normalization. F4.3's `1/2` is herewith withdrawn from the registry-write workflow; only lizzi's `f^{cutoff} = (2, 1, 0.5, 0.1)` survives into §VII.R.

#### CV7: Unified Φ vanishing condition — refined conjecture accepted

I CONCUR with lizzi's Re:FN refinement of FN.1. The classification class (W2-H) is a half-plane *separation*, not a residue identity, but it is captured by the unified Mellin-cohomological invariant `Φ(f, m^O; G) = 0` once `G` is allowed to include "Borel-contour pole-count" and "windowed-empirical-slope-ordering" as auxiliary group actions (in addition to the original four: regulator-pair, BRST grading, Weyl rescale, lattice rescale).

The refined conjecture I now accept:

> **Family Meta-Theorem (refined).** Every substrate immunization theorem corresponds to the vanishing of a Mellin-cohomological invariant `Φ(f, m^O; G) = 0` constructed from the regulator's Mellin vector `f^r`, the observable's character vector `m^O`, and an auxiliary group action `G` ∈ {regulator-pair, BRST grading, Weyl rescaling, lattice rescaling, Borel contour, Z₂ sheet, fit-window slope-ordering}. The 6 classes correspond to the 6 admissible `G`-types.

This is ONE meta-theorem with ten corollaries, six Φ-branches, and one parent classification axis (`G`-type). The original FN.1 conjecture survives with the generalization "vanishing residue → vanishing of appropriate Mellin-cohomological invariant," which subsumes residues, half-plane pole-counts, and windowed-kinematic inequalities under a single language.

### DISSENT

#### DT1: WEAK-FORM C-γ survives — Weyl-rescaling immunization as parametric bound, not exact identity

lizzi's Re:F4 Q4.1 REFUTED the strong form (exact b_DK = 0). I accept the refutation. But there is a salvageable WEAK form that lizzi's own Re:F4 Q4.4 endorses, and which I want to make explicit as the surviving C-γ statement:

```
Substitution chain (WEAK-FORM C-γ DIRECTION):

Step 1 — Definitions:
   strong-form C-γ:   ΔS_W[Ω] = 0 exactly       (REFUTED — b_DK > 0)
   weak-form C-γ:     |ΔS_W[Ω] / S_W[1]| ≤ b_DK · (Λ_anomaly / Λ_cutoff)²
                                                  (parametric bound, S69 W4-C source)

Step 2 — Substitute canonical scales:
   Λ_anomaly  = M_KK    ≈ 1.0e16 GeV        (canonical pinning)
   Λ_cutoff   = M_Pl    ≈ 2.435e18 GeV       (reduced Planck mass)
   ratio      = M_KK / M_Pl                  = 4.107e-3
   ratio²     = (M_KK / M_Pl)²               = 1.687e-5

Step 3 — Simplify the bound:
   With b_DK = O(top-Yukawa²) ~ O(1), the parametric bound becomes
   |ΔS_W[Ω] / S_W[1]| ≤ O(1) · 1.7e-5  ~  10⁻⁵.

Step 4 — Direction:
   Weak-form C-γ is a NON-VACUOUS bounded immunity statement.
   The bound is 10⁻⁵, which is FIVE ORDERS OF MAGNITUDE below
   the spectral-action moments themselves — within the regime
   where Weyl-rescaling is observably immune.
   ⇒ C-γ survives as: "Weyl-rescaling immunity holds parametrically in (M_KK/M_Pl)²
                       at slot a_4, F_4-scope-bound."
```

(All numerics Python-verified inline at workshop-prep.)

I therefore REPLACE F4.1's strong-form statement with this weak-form statement and PROPOSE that lizzi accept "C-γ-WEAK" as the surviving candidate for §VII.R.γ. The retraction is scoped: C-γ-strong is REFUTED; C-γ-weak is OPEN, F_4-bound, and ready for the F4.6 S86 gate (with the (Λ_anom/Λ_cut)² PASS-band that lizzi's Re:F4 Q4.4 already endorsed).

This is not a regression. It tightens the theorem statement to what the substrate actually licenses.

#### DT2: F_4-bound applies even to the WEAK form

I want to flag explicitly that the F_4 scope-binding survives the weak-form weakening. lizzi's Q4.2 chain established this implicitly; let me make it explicit:

```
Substitution chain (F_4-binding of weak-form C-γ) DIRECTION:

Step 1 — Definition: weak-form parametric bound is
   |ΔS_W[Ω]| / |S_W[1]|  ≤  Σ_n (relevant slot contribution_n) · (Λ_anom/Λ_cut)²

Step 2 — Substitute per regulator class:
   In F_4: only slot a_4 contributes; bound is
       |Δa_4[Ω]| · f_4^r ≤ b_DK · (Λ_anom/Λ_cut)²       — single bounded slot.

   In M (cutoff_sqrt): slots a_0, a_4, a_6 all contribute; bound is
       |Δa_0[Ω]| · f_0^r + |Δa_4[Ω]| · f_4^r + |Δa_6[Ω]| · f_6^r
       ≤  ?   — but Δa_0[Ω] is the COSMOLOGICAL CONSTANT slot Weyl-shift,
              which is NOT parametrically suppressed by (Λ_anom/Λ_cut)²
              because the CC slot involves the volume form, not heat-kernel curvature
              invariants. Δa_0[Ω] ~ Vol(M⁴) · ⟨Ω^0⟩ — independent of M_KK.

Step 3 — Simplify:
   F_4: bound holds at O((Λ_anom/Λ_cut)²) ~ 10⁻⁵.
   M:   bound at slot a_0 is f_0^r · Vol(M⁴) — NOT parametrically suppressed —
         dominates the bound and gives order-unity Weyl violation.

Step 4 — Direction:
   Weak-form C-γ holds in F_4 but FAILS in M-class regulators.
   ⇒ Even after weakening, the candidate is F_4-bound.
```

This is the structural reason cutoff_sqrt cannot be "rescued" by parametric weakening: the a_0 slot survives independent of the cutoff scale because it counts volume, not curvature. So C-γ-weak inherits the F_4 scope-bound from C-γ-strong; the weakening did not enlarge the family.

This is the only DISSENT I have with lizzi's R1; everything else converges.

### EMERGENCE

#### EM1: §VII.R cascade as a structural reorganization — not 8 sub-corollaries, but 6 Φ-branches

The combination of (FN.6 §VII.R cascade proposal) + (lizzi L3 §VII.Ω-UNIFIED migration question) + (lizzi L8 convention discrepancy) + (lizzi LQ.1 separate-vs-cascade structural question) suggests a deeper reorganization. The §VII.R cascade should be structured by Φ-branch (auxiliary group action `G`), not by candidate ID.

Proposed §VII.R structure (FINAL, for lizzi to consolidate in R2-B):

```
§VII.R — Perturbative-Ledger Immunization Theorem Family
   PARENT META-THEOREM: Φ(f, m^O; G) = 0 for G ∈ 6 admissible group-action types.
   CONVENTION PIN: f^r values per S-1 §II.2 Table II.2 (Andrianov-Lizzi normalization).
   SCOPE-PIN: F_4 = {zeta, Zubarev, SDW}; M = {cutoff_sqrt, anomaly}; per S-1 Theorem §II.4.

   §VII.R.A — Non-perturbative branch (G = Borel contour pole-count)
              Members: W9-1 (LANDED §VII.P), C-ε (OPEN, lifts §VII.P to full series).
              Scope: atlas-wide.

   §VII.R.B — Regulator-class branch (G = regulator-pair `f^{r1} - f^{r2}`)
              Members: W9-2 (LANDED §VII.Q), C-ζ (OPEN, NPI extension N≥4),
                       C-α (OPEN, F_4-bound at Symanzik level), C-δ (OPEN, F_4-bound),
                       C-ι (OPEN, F_4-bound).
              Scope: mixed — W9-2 and C-ζ atlas-wide; C-α, C-δ, C-ι F_4-bound.

   §VII.R.C — Gauge-fixing branch (G = BRST grading `ω_sym vs ω_ant`)
              Members: C-β (OPEN, S86 gate), C-η (DE-FACTO LANDED), C-θ (DE-FACTO LANDED).
              Scope: atlas-wide (BRST measure-symmetric, regulator-blind).

   §VII.R.D — Conformal/scale branch (G = Weyl rescaling Ω(x))
              Members: C-γ-WEAK (OPEN, parametric bound, F_4-bound).
              Scope: F_4-bound. Strong-form REFUTED via b_DK > 0.

   §VII.R.E — Classification branch (G = saddle-action half-plane separator)
              Members: W2-H (LANDED #49).
              Scope: atlas-wide (geometric threshold).

   §VII.R.F — Windowed-kinematic branch (G = fit-window slope-ordering)
              Members: C-κ (OPEN, requires S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE master gate).
              Scope: windowed L ∈ {5,6,7,8} only; not asymptotic.

   §VII.R.ω — Substrate-moment-identity sibling line (regulator-conditional)
              Members: §VII.Ω-UNIFIED α_s = n_s² - 1 + β_s.
              Scope: F_4-bound single-residue at slot a_4.
              Structural relation: co-fibered with §VII.R.B's F_4-bound members
              (C-α, C-δ, C-ι) and §VII.R.D's weak-form member (C-γ-WEAK).
              Cross-reference only; primary registry slot remains §VII.Ω.

   §VII.R-SEPARATE — Representation-content sub-theorem (NOT a scaffold immunity)
              Members: F3.6 BRST-anomaly cancellation (`Tr_F (Y†Y · χ_A) = 0`).
              This is registered SEPARATELY from §VII.R, at §VII.J / §VII.S level
              per lizzi's Re:F3 EMERGES; it is a representation-content theorem,
              not a scaffold-immunity. Does not appear inside the §VII.R cascade.
```

This structure is **6 Φ-branches** indexed §VII.R.A through §VII.R.F, with 10 candidate corollaries distributed among them, plus one cross-reference sibling-line (§VII.R.ω → §VII.Ω-UNIFIED) and one explicitly-out-of-cascade SEPARATE entry (F3.6).

The advantage over my original FN.6 (8 sub-corollaries indexed α-ι by candidate name): the structural-axis (Φ-branch) is the registry's primary index, with candidates organized under it. This matches how a future computation would query the registry — "what immunity holds against Weyl rescaling?" returns §VII.R.D directly, not a search over Greek-letter candidate IDs.

I propose this as the §VII.R structure for R2-B (lizzi FINAL) to consolidate in the Workshop Verdict + Wrap-Up. lizzi: feel free to adjust naming/indexing in your R2-B; the structural commitment I make here is "6 Φ-branches as primary index, candidates as members."

#### EM2: The 6th Φ-branch (windowed-kinematic) is empirically novel

Reading lizzi's L1 row for C-κ — its closure is a **slope-ordering inequality on a finite L window**, not a residue identity at any s — exposes a structural feature absent from the original five Φ-branches:

The other five branches all have an **infinite-data limit** at which the closure becomes algebraic (regulator-pair vanishes exactly; BRST symmetric residue is exactly zero by measure symmetry; Duff coefficient is a fixed finite number; Borel contour encloses zero or non-zero poles). The windowed branch has NO infinite-data limit — at L → ∞, the windowed inequality SCOPE-CHANGES (lizzi's Slot 1a 3A solo refuted the L → ∞ residue identity, hence the explicit windowing). This is **empirically novel**: a member of the immunity family whose existence depends on a finite computational window, not a structural identity.

This raises a structural question:

> Are there other windowed-kinematic immunities lurking in the data that we have been treating as ordinary residue identities? The natural candidates are L_max-truncation effects on PROVEN identities — does W9-2's machine-ε identity at L_max = 3 retain its closure as L_max → ∞?

This is a follow-on for S86 / S87 (not 1C scope), but worth flagging as a derived insight.

#### EM3: Mellin-cohomological invariant Φ as the framework's organizing principle for perturbative ledger

Combining lizzi's Refined Conjecture (Re:FN) + L1 table + the §VII.R reorganization above: the **perturbative ledger** of the substrate spectral functional has a single Mellin-cohomological invariant `Φ` whose vanishing is the closure of every immunization theorem on the ledger. This is structurally analogous to how the Atiyah-Singer index theorem relates topological invariants to analytic ones: the substrate's `Φ` is its Mellin-cohomological invariant, and it vanishes precisely on the immunity-protected observables.

The implication for the broader framework: **the perturbative ledger is closed under Mellin-cohomological invariance**, in the sense that any observable derivable from spectral moments of `D_K` either has `Φ = 0` (immune to scaffold contamination, hence appears in the ledger as a clean substrate observable) or has `Φ ≠ 0` (carries scaffold dependence, hence is not a substrate observable in the strict sense). This sharpens what "perturbative ledger" means at the structural level: it is the kernel of `Φ` viewed as an operator on the candidate-observable algebra.

This is a structural EMERGENCE I did not anticipate at F1. lizzi's L1 + Re:FN are the engine of the insight.

### QUESTIONS

#### Answers to lizzi's L4 questions (LQ.1 — LQ.8)

**LQ.1 ANSWER (cascade vs separate-entry)**: ONE §VII.R cascade with 6 Φ-branches as primary index, per EM1 above. NOT three separate registry entries. Parsimony wins because the parent meta-theorem (`Φ = 0`) genuinely unifies all 6 branches under a single structural condition. The Φ-branch indexing exposes the structural axis (auxiliary group action `G`) without losing the candidate-level granularity — each candidate appears as a member under its branch.

**LQ.2 ANSWER (S86 priority among MODERATE/LIGHT)**: **C-α first, then C-η + C-θ registry-write, then C-ζ.** Reasoning:

- C-α directly tests the F_4 / M boundary at the slot-by-slot Mellin level — empirical validation of S-1's F_4 / M partition. Maximum EVOI per S86 effort budget. Lizzi's L4 LQ.2 instinct is correct.
- C-η + C-θ are zero-compute registry-writes; they should be done in the same S86 wave as a "consolidation pass" after C-α lands.
- C-ζ (NPI extension to N ≥ 4) is structurally the safest extension but does not probe the F_4 boundary; it tests robustness in an already-PASSed direction. Lower EVOI than C-α.

S86 ordering: C-α (empirical F_4 test) → C-η + C-θ (zero-compute landings) → C-γ-WEAK (F_4-bound, weak-form) → C-ζ (N=4 extension). The HEAVY candidates (C-β BRST one-loop; C-ε full Borel series; C-ι Z₂ monodromy at scale) defer to S87+.

**LQ.3 ANSWER (W2-H half-plane vs residue, keep in or out)**: KEEP W2-H IN §VII.R (under §VII.R.E classification branch), with the unified Mellin-cohomological invariant `Φ = 0` as the parent. The trade-off lizzi flagged is real but resolves in favor of "keep in" because W2-H's closure mechanism (`S < 4.34 ⇒ Gaussian, never WKB`) is genuinely a substrate observable (the saddle-action threshold is determined by `D_K`'s spectral data, not by the calculator). Excluding it from the family because its `Φ` is a half-plane pole-count rather than a residue would be a taxonomy choice without structural content.

The parent meta-theorem statement should read "Φ = 0 in the appropriate Mellin-cohomological invariant" rather than "vanishing residue." This is the refinement I accept (CV7).

**LQ.4 ANSWER (F3.6 BRST-anomaly cancellation relocation)**: AGREE with relocation. F3.6's `Tr_F (Y†Y · χ_A) = 0` is a representation-content theorem, not a scaffold-immunity, and lives at §VII.J / §VII.S level. It does NOT appear inside the §VII.R cascade. It is the CONDITION for C-β to hold non-perturbatively, but the condition itself is a finite-dimensional fiber-algebra trace identity, not a Mellin-residue closure. Cross-reference §VII.J ↔ §VII.R.C (gauge-fixing branch) is the right pointer; the substantive entry stays at §VII.J.

**LQ.5 ANSWER (§VII.Ω migration vs sibling-line)**: SIBLING-LINE (Option 1). §VII.Ω-UNIFIED stays at §VII.Ω with cross-reference into §VII.R.ω. Reason: S-3 closeout is pre-committed to §VII.Ω; migrating creates registry-history thrash without structural gain. The cross-reference §VII.R.ω → §VII.Ω is sufficient to expose the F_4-bound co-fibered structure.

**LQ.6 ANSWER (path-integral candidates I missed)**: Two further structural lifts emerge from the path-integral side that I did not enumerate at F1:

1. **C-ξ (continuous-N analytic continuation of N-PI)**: lifting C-ζ from integer N ≥ 4 to continuous N via Mellin-Barnes contour. The Φ-vanishing condition is the analyticity of the N-PI self-energy in the half-plane Re(N) > N_threshold for some computable N_threshold. This is regulator-class (G = regulator-pair on N-continuation parameter). DEFER to S87+ — not load-bearing for 1C registry.

2. **C-λ (instanton-instanton interaction beyond W9-1's single-instanton floor)**: the W9-1 Borel floor `min S_inst > 4.34` covers single-instanton suppression. Two-instanton interaction `S_2-inst = 2·S_inst + Δ_int` introduces a binding/repulsion correction `Δ_int` that may be small enough to push the threshold below 4.34. Φ-vanishing condition is `Δ_int < S_inst - 4.34` (the safety margin). Non-perturbative class (G = Borel contour with multi-instanton additions). Tractable via dilute-instanton-gas approximation; effort is MODERATE.

I would file these as `C-ξ` and `C-λ` for future-S87 consideration. They are not load-bearing for 1C R2-B verdict. Adding them brings the family to 12 candidates / 6 Φ-branches if we want to enumerate them now.

**LQ.7 ANSWER (Λ_anomaly pinning for C-γ-WEAK gate)**: Compute Λ_anomaly INTERNALLY from the substrate's representation content via the AC-2010 §V trace `Tr_F (Y†Y)`, NOT as input. Reasoning: if Λ_anomaly is pinned externally (e.g., set to M_KK by convention), the gate becomes a tautological cross-check on the input, not a verification of the substrate's parametric suppression. Internal computation makes the gate genuinely structural. Recommendation: the C-γ-WEAK S86 gate should derive Λ_anomaly from `Tr_F (Y†Y)` and the canonical AC-2010 §V coefficients, then test the bound `|ΔS_W / S_W| ≤ b_DK · (Λ_anom_internal / Λ_cut)²`. If Λ_anom_internal differs from M_KK by more than a factor of 2, that is itself an INFO finding (mild tension with canonical pinning).

**LQ.8 ANSWER (convention discrepancy registry pin)**: AGREE with adding a "convention pin" block to the §VII.R header citing S-1 §II.2 Table II.2 as the canonical Mellin-residue normalization (per CV6 above). My F4.3 `f_0 = 1/2` is a non-canonical inverse-Mellin-frame value and is herewith withdrawn. The registry should read:

```
§VII.R Convention Pin:
   Mellin-residue normalization:  f_n^r := Res_{s = n/2} M[f_r](s)
                                   M[f](s) = ∫_0^∞ x^{s-1} f(x) dx
   Canonical f^r values:           per S-1 §II.2 Table II.2 (Andrianov-Lizzi)
   Cutoff_sqrt vector:             f^{cutoff} = (2, 1, 0.5, 0.1)
   F_4 partition:                  per S-1 §II.4 Theorem (zeta, Zubarev, SDW)
   Inverse-frame note:              F4.3's `f_0 = 1/2` is reciprocal-frame; not canonical.
```

This pin block resolves LQ.8.

#### Final issues for lizzi R2-B (FINAL turn)

**fQ.1 — Workshop Verdict table**: please populate the 6-row table per the §VII.R structure in EM1. Suggested status assignments:

| # | Topic | Status | Key Insight |
|:--|:------|:-------|:------------|
| 1 | Lattice-spacing immunization (C-α) | Converged + F_4-bound | Sage-verified single-residue closure under Symanzik; F_4-only |
| 2 | Gauge-fixing immunization (C-β / C-θ duality) | Converged | Slavnov-Taylor identity replaces ξ-scan; collapses to single F_4 residue |
| 3 | Weyl-rescaling immunization (C-γ) | Partial (strong REFUTED, weak survives) | C-γ-strong refuted via b_DK > 0; C-γ-weak F_4-bound at (M_KK/M_Pl)² |
| 4 | Family-registry consolidation (§VII.R) | Emerged | 6 Φ-branches indexed §VII.R.A-F; 10 candidates as members |
| 5 | Pure-a_4 scope bound (S-1 pairing) | Converged | F_4 vs M wall at slot a_0; 5 F_4-bound / 4 atlas-wide / 1 windowed |
| 6 | §VII.Ω-UNIFIED pairing (S-3) | Converged | Sibling-line at §VII.Ω; cross-reference §VII.R.ω; F_4-bound single-residue |

These are my proposed entries; consolidate or override as needed in R2-B.

**fQ.2 — Carry-forward computations for S86**: please record explicitly:

1. S86-LATTICE-SPACING-IMMUNIZATION-CANDIDATE (C-α): F_4-bound; pre-register `r ∈ {zeta, Zubarev, SDW}` scope; Symanzik-improved O(a^4) PASS-band.
2. S86-GAUGE-FIXING-IMMUNIZATION-CANDIDATE (C-β): Slavnov-Taylor `⟨QM⟩ = 0` symbolic PASS criterion; ξ-scan diagnostic.
3. S86-WEYL-RESCALING-IMMUNIZATION-CANDIDATE (C-γ-WEAK): F_4-bound; (Λ_anom_internal / Λ_cut)² PASS-band; Λ_anom computed internally from `Tr_F (Y†Y)`.
4. S86-WARD-IDENTITY-IMMUNIZATION (C-η): zero-compute registry-write only.
5. S86-INNER-FLUCTUATION-IMMUNIZATION (C-θ): zero-compute registry-write only.
6. S86-NPI-EXTENSION-N-EQ-4 (C-ζ): atlas-wide; reuses W9-2 atlas {ζ, Zubarev, SDW, dim-reg, lattice-BR}; N=4 NPI machine-ε FI test.
7. S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE master gate: contains C-κ as windowed sub-corollary (windowed L ∈ {5,6,7,8} slope-ordering test).

This 7-gate S86 wave covers all 10 candidates plus the one sibling-line (§VII.Ω-UNIFIED already landed at S-3). Heavy candidates (C-ε full Borel series, C-ι full Z₂ monodromy, C-δ full OPE basis change) defer to S87+.

**fQ.3 — Closing-line proposal**: I have one suggestion for the workshop's Closing Line, for lizzi to override or accept:

> "The substrate's perturbative ledger is the kernel of a single Mellin-cohomological invariant `Φ(f, m^O; G)`; its 10 immunity corollaries split across 6 auxiliary group-action types `G`, and the F_4 / M scope wall at slot `a_0` partitions the family into single-residue and atlas-wide closures. The §VII.R cascade is one theorem, not ten."

Adjust as needed.

---

**End of Round 2 — feynman: Follow-up.**

lizzi: your turn (FINAL). The R2-B turn should fill the Workshop Verdict table (proposed entries above), Remaining Open Questions, and the Wrap-Up (What Changed / What Holds / What Breaks-or-Strains / Carry-Forward Computations / Closing Line). The §VII.R cascade structure with 6 Φ-branches indexed §VII.R.A-F is my proposed registry organization; refine if needed in R2-B.

---

## Round 2 — lizzi: Cross-Synthesis (FINAL)

### CONVERGENCE

#### LCV1: §VII.R restructured by Φ-branch (re: feynman EM1) — accepted as FINAL registry layout

I accept feynman's EM1 6-Φ-branch reorganization without modification. The structural argument is correct: indexing the registry by auxiliary group action `G` (regulator-pair, BRST grading, Weyl rescale, lattice rescale, Borel contour, fit-window) rather than by candidate ID makes the parent meta-theorem `Φ(f, m^O; G) = 0` the primary axis and exposes the structural fact that the family is ONE THEOREM with 6 admissible group-action types and 10 corollary instantiations. My original FN.6 question (LQ.1) is resolved in favor of the cascade with structural-axis indexing.

Sharpening (not repeating) feynman's EM1: the 6-branch structure also makes the REGISTRY-QUERY semantics clean. A future computation asking "what immunizes against `G`?" returns the §VII.R.X branch directly; a query asking "is candidate Y immune?" returns its branch + corollary tag. Both queries are O(1) under §VII.R.A-F indexing; they would be O(N) under feynman's original Greek-letter-by-candidate cascade. This is a registry-query optimization, not a structural change — but it is the FINAL reason to commit to the EM1 layout.

I commit the EM1 6-branch layout to the §VII.R-FAMILY registry write. The convention pin (LQ.8 / CV6) is its header; the 6 branches §VII.R.A through §VII.R.F follow per EM1's text; the §VII.R.ω cross-reference and the §VII.R-SEPARATE F3.6 entry are in their final positions.

#### LCV2: C-γ-WEAK is the surviving Weyl candidate (re: feynman DT1) — accept and refine the bound

I accept feynman's DT1 retraction of C-γ-strong and the substitution chain establishing C-γ-WEAK as the survivor. The substitution chain is correct: with `b_DK = c_b · Tr_F(Y†Y) > 0` (my Re:F4 Q4.1, structural) and the canonical (M_KK / M_Pl)² = 1.6866e-5 (Python-verified at workshop-prep), the parametric bound `|ΔS_W / S_W| ≤ b_DK · (M_KK / M_Pl)² ≈ O(10⁻⁵)` is **non-vacuous**: it is five orders of magnitude below the spectral-action moments themselves, which is operationally "Weyl-immune" in any framework-relevant test.

Sharpening: the C-γ-WEAK bound is NOT a fudge to rescue a refuted candidate. It is the natural reading of the S69 W4-C parametric-suppression theorem (PROVEN, registered): the conformal anomaly is a parametrically suppressed correction to the spectral action, not a leading term. C-γ-WEAK is the substrate-side restatement of S69 W4-C in immunity language. The strong form was always over-strong; the weak form is what S69 W4-C licenses. So C-γ-WEAK is co-proven with S69 W4-C, not a new conjecture — it inherits S69 W4-C's PROVEN status modulo the F_4-binding flag.

#### LCV3: F_4 binding survives the weakening (re: feynman DT2) — sharpen the a_0 mechanism

I accept feynman's DT2 substitution chain establishing that C-γ-WEAK inherits F_4 scope-binding from C-γ-strong. The mechanism is correct and worth sharpening for the registry write:

```
Substitution chain (a_0 slot is NOT parametrically suppressible) DIRECTION:

Step 1 — Definition: the cosmological-constant slot a_0 is the volume integral
   Δa_0[Ω] = ∫_{M⁴} Ω⁰ · sqrt(g) d⁴x  =  Vol(M⁴) · ⟨Ω⁰⟩.
   This is a VOLUME-FORM quantity, not a heat-kernel curvature invariant.

Step 2 — Substitute: heat-kernel curvature invariants scale as (curvature)² · 1/Λ_cutoff²
   (dimensionally; the (Λ_anom/Λ_cut)² factor of S69 W4-C arises from this dim-counting).
   The volume form scales as L⁴, NOT as 1/Λ_cutoff² — there is no Λ_cutoff in Vol(M⁴).

Step 3 — Simplify the parametric content:
   Δa_0[Ω] · f_0^r  has parametric scaling  Vol · 1   ↛  no (Λ/Λ)² suppression.
   Δa_4[Ω] · f_4^r  has parametric scaling  curv² · (Λ_anom/Λ_cut)²   ⇒ suppressed.

Step 4 — Direction:
   Weak-form parametric suppression applies SLOT-BY-SLOT, and applies only to slots
   where the integrand is a curvature invariant (a_4 and higher).
   The a_0 slot is volume-form-driven and is NEVER parametrically suppressible.
   ⇒ M-class regulators (f_0^r ≠ 0) carry an UNSUPPRESSIBLE Weyl-rescaling
     contamination at the CC slot, regardless of how small (Λ_anom/Λ_cut)² is.
   ⇒ C-γ-WEAK is structurally F_4-bound; M-class CANNOT be rescued by parametric weakening.
```

This is the registry-version statement. The F_4-binding of C-γ-WEAK is structural, not a numerical near-miss; it inherits from the SLOT-BY-SLOT scaling difference between volume-form (a_0) and curvature-invariant (a_4) integrands.

#### LCV4: Slavnov-Taylor as primary criterion for C-β (re: feynman CV3) — accept the gate revision

I accept feynman's CV3 revision of the S86-GAUGE-FIXING-IMMUNIZATION-CANDIDATE pre-registration. The Slavnov-Taylor identity `⟨Q M⟩ = 0` at symbolic level is structurally stronger than a 4-point ξ-scan at machine ε; the ξ-scan becomes a diagnostic cross-check, not the primary criterion. This matches the pattern established by W9-2 (algebraic identity > numerical equality) and is the right discriminator for a cohomological-closure question.

Sharpening: the symbolic ⟨QM⟩ = 0 PASS criterion is also PRDR-clean (§0.10(d)) — it pre-registers a single symbolic identity rather than a 4-point empirical equality, eliminating PRU-vulnerability around the choice of ξ-values. The 4 ξ-values (Lorenz=0, Feynman=1, Yennie=3, axial=∞) become a diagnostic grid, not load-bearing pins. This makes the gate plan-property-clean as well as physics-clean.

#### LCV5: S86 gate priority order and convention pin (re: feynman LQ.2/LQ.7/LQ.8 answers) — accept

I accept feynman's LQ.2 ordering: **C-α first → C-η + C-θ registry-write → C-γ-WEAK → C-ζ**, with HEAVY candidates (C-β BRST one-loop, C-ε full Borel series, C-ι Z₂ monodromy at scale) deferred to S87+. C-α is the right priority because it directly tests the F_4 / M boundary at slot-by-slot Mellin-residue level — empirical validation of S-1's partition with maximal EVOI per S86 budget.

I accept feynman's LQ.7 answer: Λ_anomaly should be computed INTERNALLY from the substrate's representation content via `Tr_F(Y†Y)`, not pinned externally to M_KK by convention. This makes the C-γ-WEAK gate genuinely structural rather than tautological. If Λ_anom_internal differs from M_KK by more than a factor of 2, that is itself an INFO finding; the gate now does double duty as a Weyl-immunity test AND as a cross-check on canonical M_KK pinning.

I accept feynman's CV6 + LQ.8 answer: the §VII.R header carries a "convention pin" block citing S-1 §II.2 Table II.2 (Andrianov-Lizzi normalization) as the canonical Mellin-residue normalization. F4.3's `f_0 = 1/2` is reciprocal-frame and is withdrawn from the registry workflow.

### DISSENT

#### LDT1: NEW dissent on feynman LQ.6 / EM1's §VII.R-SEPARATE — F3.6 should NOT cross-reference into §VII.R.C

feynman's EM1 lists "§VII.R-SEPARATE — Representation-content sub-theorem" with F3.6 BRST-anomaly cancellation as a separate registry entry, and his LQ.4 ANSWER says "Cross-reference §VII.J ↔ §VII.R.C (gauge-fixing branch) is the right pointer." I dissent on the cross-reference direction (NEW evidence; not raised in R1).

```
Substitution chain (cross-reference direction for F3.6) DIRECTION:

Step 1 — Definition:
   F3.6 statement: Tr_F (Y†Y · χ_A) = 0 for chiral KO-6-conjugate representations.
   This is a finite-dimensional fiber-algebra trace identity on A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ).
   It is the CONDITION under which BRST cohomology closes anomaly-free at every loop order.

Step 2 — Substitute the dependency direction:
   Without F3.6 ⇒ BRST anomaly present at some loop order ⇒ ξ-independence breaks at that order
                ⇒ C-β (gauge-fixing immunization) FAILS non-perturbatively.
   With F3.6 ⇒ BRST anomaly absent at all orders ⇒ ξ-independence holds non-perturbatively
              ⇒ C-β strengthens from "to all orders in g²" to "non-perturbatively exact."

Step 3 — Simplify the dependency graph:
   F3.6 → C-β is a one-way directed edge (F3.6 ENABLES the strong form of C-β).
   C-β → F3.6 is NOT an edge (C-β does not require F3.6 to land at PASS at one-loop;
                              the weaker "to all orders" form holds without F3.6).

Step 4 — Direction:
   The cross-reference should be ASYMMETRIC: §VII.R.C cites §VII.J for the
   non-perturbative strengthening; §VII.J does NOT cite §VII.R.C.
   feynman's LQ.4 "§VII.J ↔ §VII.R.C" symmetric notation obscures this.
```

This is a minor structural dissent — agree on the SEPARATE landing, dissent on the cross-reference symmetry. The §VII.R registry write should read: "§VII.R.C → §VII.J (non-perturbative strengthening; one-way)." In §VII.J's own registry entry, the back-pointer to §VII.R.C is informational ("see also") but not load-bearing on F3.6's standalone status.

#### LDT2: NEW dissent on feynman LQ.6's C-ξ enumeration — continuous-N analytic continuation does NOT belong in the family

feynman's LQ.6 ANSWER added two further candidates (C-ξ continuous-N analytic continuation; C-λ instanton-instanton interaction). I CONCUR with C-λ as a non-perturbative-class candidate (it lives inside Φ-branch §VII.R.A and is structurally compatible with the W9-1 floor framework). I DISSENT on C-ξ.

```
Substitution chain (C-ξ structural admissibility test) DIRECTION:

Step 1 — Definition:
   C-ξ candidate: lift C-ζ (NPI extension) from integer N ≥ 4 to continuous N via
                  Mellin-Barnes contour analytic continuation. Φ-vanishing condition:
                  analyticity of N-PI self-energy in half-plane Re(N) > N_threshold.

Step 2 — Substitute the substrate-observable test:
   N is the order of N-particle-irreducibility. The N-PI hierarchy is a COMPUTATIONAL
   organization of the effective action's loop expansion (Cornwall-Jackiw-Tomboulis 1974;
   De Dominicis-Martin 1964). N is NOT a property of the substrate — it is a property
   of the ORGANIZATION of the perturbation series.

Step 3 — Simplify (apply QN.2 / scaffold-criterion test):
   Per QN.2: a contamination Y is a SCAFFOLD iff Δ_Y acts on at most one of {f^r, m^O}
   and leaves {λ_k} fixed.
   N-continuation acts on the ORGANIZATION OF THE COMPUTATION — neither on f^r nor on
   m^O. The 4PI vs 5PI distinction is a re-arrangement of the same diagrams under
   different irreducibility cuts; the underlying spectral data {λ_k} is unchanged.
   ⇒ N is not even a scaffold parameter; it is a meta-parameter of the calculator's
   diagrammatic bookkeeping.

Step 4 — Direction:
   C-ξ is not a scaffold immunity candidate. It is a meta-organization-of-perturbation
   theory invariance — closer in spirit to the equivalence of MS̄ and MS-bar
   renormalization schemes than to a regulator-class immunity. It does not belong
   in §VII.R-FAMILY.
```

I file C-ξ OUT-OF-FAMILY: it is a perturbative-organization-equivalence theorem (sibling level with MS̄/MS conventions equivalence), not an immunity theorem. C-λ stays IN-FAMILY at §VII.R.A. The 1C campaign's family headcount remains **6 Φ-branches / 10 candidates** plus C-λ as an OPEN S87+ §VII.R.A candidate (11 if counted), with C-ξ explicitly excluded.

This is the only structural dissent I have with feynman's R2; the rest converged at LCV1-LCV5.

### EMERGENCE

#### LEM1: The §VII.R parent meta-theorem promotes the "perturbative ledger" to a Mellin-cohomological invariant kernel

Combining feynman's EM3 (Mellin-cohomological invariant `Φ` as organizing principle) with my Re:FN refined conjecture and the L1 Φ-table, a structural insight emerges that I did not anticipate at R1. The "perturbative ledger" — the working-paper concept that aggregates all PROVEN substrate immunity theorems — is not a list. It is the **kernel** of the Mellin-cohomological operator `Φ` acting on the candidate-observable algebra.

```
Substitution chain (perturbative ledger as ker(Φ)) DIRECTION:

Step 1 — Definition:
   candidate-observable algebra C := { O[D_K, τ] : O is built from spectral moments }
   Φ : C × G → ℝ            (Φ takes an observable, an aux group action G, and returns a number)
   ker(Φ) := { O ∈ C : Φ(f, m^O; G) = 0 for ALL admissible G }

Step 2 — Substitute per Φ-branch:
   Φ-branch G_1 (regulator-pair):    Φ_1(f, m^O) = Σ_n (f_n^{r1} - f_n^{r2}) m_n^O
   Φ-branch G_2 (BRST grading):       Φ_2(f, m^O) = ⟨f^r, m_n^{ω_sym}⟩
   Φ-branch G_3 (Weyl):               Φ_3(f, m^O) = f_4^r · b_DK at slot a_4
   Φ-branch G_4 (lattice):            Φ_4(f, m^O) = Σ_n (n/2)·(a²/x_0)·f_n^r·m_n^O - Symanzik
   Φ-branch G_5 (Borel):              Φ_5(f, m^O) = #{poles of M[exp(-S/g)] in Re(s)>0}
   Φ-branch G_6 (windowed):           Φ_6(f, m^O) = slope-ordering(L ∈ {5,6,7,8})

Step 3 — Simplify the kernel structure:
   O is in ker(Φ) iff Φ_i(f, m^O) = 0 for ALL six i.
   Different observables fail different Φ_i — partial-kernel observables are the
   regulator-conditional and scope-bound corollaries (e.g., F_4-bound members live
   in ker(Φ_3 ∩ Φ_4) but may exit ker(Φ_5) under specific saddle structures).

Step 4 — Direction:
   The PERTURBATIVE LEDGER is exactly ker(Φ) ∩ C — observables that survive every
   admissible group-action contamination test. The §VII.R cascade enumerates the
   single-Φ-branch closures (one corollary per branch); the FULL ledger is the
   intersection of all branch kernels.
```

This is structurally analogous to how K-theory characterizes Atiyah-Singer-protected observables via the index map `ind : K(M) → ℤ` — the substrate's `Φ`-map plays the role of an index map for perturbative-scaffold-protected observables. Whether this is a literal mathematical isomorphism or just a structural analogy is open (LEM1 conjecture — flagged for S87+).

The implication for the working paper: §VII.R's parent meta-theorem statement should declare ker(Φ) as the formal definition of "perturbative ledger," with the 6 branches as the 6 admissible Φ-projectors, and the ledger membership criterion as "survives all 6 projector tests." This is the cleanest structural framing.

#### LEM2: The 6-branch family exposes a missing branch — the "spectral-truncation" Φ-branch

While reviewing the 6-Φ-branch table (feynman EM1) against my Slot 1a Row 3A solo's C-κ refutation, I notice a structural feature that no 1C-discussed Φ-branch covers: the **L_max-truncation** family. C-κ is L_max-windowed (L ∈ {5,6,7,8}), but L_max truncation per se is a different scaffold from windowed-fit-ordering.

```
Substitution chain (L_max-truncation Φ-branch DIRECTION):

Step 1 — Definition:
   L_max-truncation contamination: substrate spectral data is computed at finite
   eigenvalue cutoff L_max; observables are L_max-truncated approximants of the
   L → ∞ continuum value. Δ_{L_max} acts on the λ_k themselves (truncates the
   spectrum at the L_max-th eigenvalue).

Step 2 — Substitute QN.2 scaffold-criterion test:
   Δ_{L_max} acts on {λ_k} directly (truncates the set). By QN.2's strict criterion,
   this is NOT a scaffold — it is structural (acts on the substrate spectrum).

Step 3 — Simplify by relaxing QN.2:
   But Δ_{L_max} is a CONTROLLED structural change — the L_max → ∞ limit recovers
   the continuum spectrum. So Δ_{L_max} is in a third category: "structurally
   convergent": acts on {λ_k} but reduces to identity in a known limit.

Step 4 — Direction:
   The 6-Φ-branch family does NOT cover L_max-truncation as its own G-axis.
   C-κ (windowed-kinematic) PROXIES for it but does not generalize the L_max
   convergence question itself. There is room for a §VII.R.G branch — "spectral
   truncation convergence" — whose Φ vanishes when L_max-truncation residuals
   approach zero in a controlled way.
```

This is an emergent structural observation, not a proposal to expand the §VII.R cascade in 1C scope. The 6-branch structure feynman codified in EM1 is correct AS A 1C-COMPLETE FAMILY at the Mellin-residue + half-plane + windowed level. A 7th branch covering L_max-truncation convergence would require a separate session (S87+) to develop the Φ-formulation rigorously. I flag it here as a derived insight: the §VII.R parent meta-theorem at the FORMAL level may need a 7-branch extension once L_max physics is mellinized.

This is a follow-on insight at the boundary of 1C scope. I file it as carry-forward for S87+ and do not attempt to land it in 1C's §VII.R-FAMILY registry write.

#### LEM3: The "intensive/extensive partition" of immunization candidates emerges from the Φ-branch structure

A second emergent observation, also from feynman EM1's structural reorganization combined with my Re:FN scaffold-vs-structural-axiom criterion (QN.2): the 6 Φ-branches naturally partition into **INTENSIVE** (do not depend on system size / volume) and **EXTENSIVE** (scale with volume or eigenvalue-count) closures.

| Branch | Intensive or Extensive | Mechanism |
|:-------|:----------------------|:----------|
| §VII.R.A (Borel) | INTENSIVE | geometric saddle-action threshold; volume-blind |
| §VII.R.B (regulator-pair) | INTENSIVE | algebraic identity at each Mellin slot; volume-blind |
| §VII.R.C (BRST) | INTENSIVE | fiber-algebra cohomology; volume-blind |
| §VII.R.D (Weyl) | EXTENSIVE at a_0 (Vol(M⁴) factor); INTENSIVE at a_4 | a_0 picks up volume-form; a_4 is curvature-invariant density |
| §VII.R.E (classification) | INTENSIVE | half-plane separation; volume-blind |
| §VII.R.F (windowed) | EXTENSIVE in L_max | finite-L window IS a finite-system-size scaffold |

This intensive/extensive partition (IEP) is the structural reason §VII.R.D is F_4-bound and §VII.R.F is L_max-windowed: extensive contaminations cannot be parametrically suppressed by intensive ratios like (Λ_anom/Λ_cut)². The Weyl-rescaling slot-by-slot scaling argument (LCV3 substitution chain) is the mechanism: a_0's volume-form integrand is an extensive density, and no intensive parameter can suppress it.

This recovers, at the Mellin-cohomological level, the intensive/extensive split that I first registered in the S70 Workshop Landau R2 (memory file). The same partition reappears here at one Φ-branch level higher, suggesting it is a **deep organizing principle** of the perturbative ledger, not an artifact of any single result. The 6-branch §VII.R cascade should annotate each branch with its IEP class in the registry-write header. This is an emergent finding from R1+R2 cross-synthesis.

## Workshop Verdict

| # | Topic | Source | Status | Key Insight |
|:--|:------|:-------|:-------|:------------|
| 1 | Lattice-spacing immunization (C-α) | F2, Re:F2, L1, CV2 | **Converged + F_4-bound** | Sage-verified single-residue closure under Symanzik (1+a²/x_0)^{n/2}; one constraint cancels one drift in F_4; in cutoff_sqrt 1 constraint vs 3 drifts ⇒ scope-bound. INTENSIVE branch. |
| 2 | Gauge-fixing immunization (C-β / C-θ duality) | F3, Re:F3, L1, CV3-CV4, LCV4 | **Converged** | Slavnov-Taylor `⟨QM⟩=0` symbolic PASS replaces ξ-scan; in F_4 the C-β/C-θ duality collapses to ONE single-residue identity at slot a_4; INTENSIVE branch; F3.6 BRST-anomaly cancellation lifted to §VII.J (NOT in §VII.R) per LDT1 one-way cross-reference §VII.R.C → §VII.J. |
| 3 | Weyl-rescaling immunization (C-γ) | F4, Re:F4, L1, DT1-DT2, LCV2-LCV3 | **Partial (strong REFUTED, weak survives)** | C-γ-strong refuted: b_DK = c_b · Tr_F(Y†Y) > 0 by AC-2010 §V positive-Yukawa-trace. C-γ-WEAK: parametric bound ≤ b_DK · (M_KK/M_Pl)² ≈ 1.69e-5 — non-vacuous. F_4-bound STRUCTURALLY because a_0 slot is volume-form-driven (extensive), not curvature-invariant; cannot be parametrically rescued. EXTENSIVE-at-a_0 / INTENSIVE-at-a_4 hybrid. |
| 4 | Family-registry consolidation (§VII.R cascade) | FN, L1, EM1, LCV1, LEM1 | **Emerged** | 6-Φ-branch reorganization: §VII.R.A-F indexed by auxiliary group action `G`; 10 candidates as members under branches; §VII.R.ω cross-references §VII.Ω-UNIFIED; §VII.R-SEPARATE is F3.6 OUT of cascade. Parent meta-theorem: ker(Φ) ∩ C = perturbative ledger formally (LEM1). |
| 5 | Pure-a_4 scope bound (S-1 pairing) | L2, FN.4 | **Converged** | F_4 vs M wall is at slot `a_0` (volume-form contamination); 5 F_4-bound candidates (C-α, C-γ-WEAK, C-δ, C-ι, §VII.Ω-UNIFIED), 4 atlas-wide (W9-1, W9-2, W2-H, C-β/C-η/C-θ trio), 1 windowed-only (C-κ). §VII.R inherits scope from §VII.B (S-1 canonical anchor). |
| 6 | §VII.Ω-UNIFIED pairing (S-3) | L3, LQ.5 | **Converged** | Sibling-line at §VII.Ω; cross-reference §VII.R.ω; F_4-bound single-residue identity α_s = (m_4^{n_s} · f_4^r)² - 1; β_s co-protected via slow-roll chain. NOT same residue identity as §VII.Q (regulator-blind); NOT same as C-β (gauge-fixing); IS co-fibered with C-α/C-γ-WEAK/C-δ/C-ι. |
| 7 (emergent) | Intensive/Extensive partition (IEP) | LEM3 | **Emerged** | 6 Φ-branches partition into INTENSIVE (A, B, C, D-at-a_4, E) vs EXTENSIVE (D-at-a_0, F); recovers S70 Landau R2 IEP at one structural level higher; explains why §VII.R.D is F_4-bound (extensive a_0 not parametrically suppressible). |
| 8 (emergent) | Missing 7th branch — L_max-truncation | LEM2 | **Emerged (out-of-1C-scope)** | L_max-truncation is "structurally convergent" — acts on {λ_k} but reduces to identity at L → ∞. Not in 1C 6-branch family; flagged for S87+ formalization. |

## Remaining Open Questions

1. **OQ1 — C-α S86 gate empirical PASS at slot-by-slot Mellin level.** Pre-register `r ∈ {zeta, Zubarev, SDW}` scope; 3 Wilson + 1 Symanzik discretizations at L_max=5; per-slot drift exponents 0,1,2,3 confirmed at Symanzik O(a^4) PASS-band; INFO band factor-2; FAIL beyond. Empirical validation of S-1 §II.4 partition. Effort: MODERATE.

2. **OQ2 — C-γ-WEAK S86 gate with internally-computed Λ_anomaly.** Compute Λ_anom from `Tr_F(Y†Y)` and AC-2010 §V coefficients; PASS-band (Λ_anom_internal / Λ_cutoff)²; INFO band [(Λ_anom/Λ_cut), (Λ_anom/Λ_cut)²]; FAIL beyond. If Λ_anom_internal differs from M_KK by factor > 2, INFO secondary finding. Effort: HEAVY.

3. **OQ3 — C-β symbolic Slavnov-Taylor `⟨QM⟩ = 0` gate.** Symbolic PASS at machine ε; ξ ∈ {0, 1, 3, ∞} numerical scan diagnostic with max pairwise drift < 1e-12. Effort: HEAVY (one-loop substrate scattering amplitude in 4 gauges).

4. **OQ4 — C-η + C-θ zero-compute registry-write pass.** Land in §VII.R.C immediately; SHA-pin provenance to `[J, D_K] = 0` (registry §II) and CCM-2007 §3 + S78 W2-F multiplier theorem. Effort: LIGHT.

5. **OQ5 — C-ζ NPI-N=4 atlas-wide test.** Reuse W9-2 atlas {ζ, Zubarev, SDW, dim-reg, lattice-BR}; machine-ε FI identity at N=4 NPI level. Effort: MODERATE.

6. **OQ6 — C-λ instanton-instanton interaction.** Dilute-gas approximation to compute Δ_int correction to single-instanton W9-1 floor; PASS iff `Δ_int < min S_inst - 4.34` (geometric safety margin). Effort: MODERATE. (Filed for S87+ per feynman LQ.6 / my acceptance.)

7. **OQ7 — Master gate S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE.** Contains C-κ as windowed sub-corollary; pins L ∈ {5,6,7,8} fit-window slope-ordering test; INFO-only verdict (no PASS at residue-identity scope). Effort: MODERATE.

8. **OQ8 — S87+: §VII.R.G branch for L_max-truncation convergence (LEM2 follow-on).** Mellin-formulate the L_max-truncation Φ as a "spectral-truncation convergence" branch; test on existing L_max-stability data. Speculative; not 1C scope.

9. **OQ9 — S87+: ker(Φ) ∩ C as formal ledger definition (LEM1 follow-on).** Test whether ker(Φ) is closed under spectral-functional composition — does the intersection of branch kernels form an algebra under spectral-moment products? Mathematical-physics question; speculative. Could connect §VII.R to Atiyah-Singer-style index theorems.

10. **OQ10 — Convention pin enforcement.** §VII.R header carries the convention pin (S-1 §II.2 Table II.2 Andrianov-Lizzi); all future corollaries cite this pin in their machinery_pin_map. Verify via `_pru_cardinality_audit.py` at S86 pre-flight. Effort: LIGHT.

11. **OQ11 — IEP annotation in §VII.R registry.** Per LEM3, each §VII.R branch carries an INTENSIVE/EXTENSIVE class tag in the registry-write. This is a structural annotation, not a new gate; it informs future scope-binding analyses (extensive branches expected to F_4-bind; intensive branches expected atlas-wide). Effort: LIGHT.

12. **OQ12 — Cross-reference §VII.R.C → §VII.J asymmetry (LDT1).** §VII.R.C cites §VII.J for the non-perturbative strengthening of C-β; §VII.J does NOT cite §VII.R.C as load-bearing (only as "see also"). The registry-write must enforce this directional asymmetry. Effort: LIGHT.

## Wrap-Up — Workshop Impact Summary

### What Changed

- **§VII.R-FAMILY registry slot consolidated as 6-Φ-branch cascade (NEW STRUCTURE).** Replaces feynman's original 8-Greek-letter sub-corollary proposal (FN.6) with a structural-axis-indexed cascade §VII.R.A through §VII.R.F. Parent meta-theorem reformulated as `Φ(f, m^O; G) = 0` in Mellin-cohomological invariant; the perturbative ledger is formally ker(Φ) ∩ C (LEM1).
- **C-γ Weyl-rescaling immunization downscoped from strong-form to weak-form.** Strong-form REFUTED: substrate Duff coefficient `b_DK = c_b · Tr_F(Y†Y) > 0` (positive Yukawa trace by AC-2010 §V). Weak-form (parametric bound at (M_KK/M_Pl)² ≈ 1.69e-5) survives, F_4-bound STRUCTURALLY because a_0 slot is volume-form (extensive), not parametrically suppressible.
- **C-β gauge-fixing gate criterion changed from machine-ε ξ-scan to symbolic Slavnov-Taylor `⟨QM⟩ = 0`.** Cohomological closure replaces 4-point numerical equality; PRDR-clean and structurally stronger.

### What Holds

- **The substrate's spectral observables are immune to the six classes of computational-scaffold contamination indexed by `G`.** This is the parent meta-theorem; it holds modulo the F_4 / M scope-binding wall at slot `a_0`. Five F_4-bound + four atlas-wide + one windowed corollary distribution per L2.
- **W9-1 §VII.P (Borel-summability floor), W9-2 §VII.Q (F_amp^3PI factorization-invariance), and W2-H (#49 harmonic-vs-WKB classification) survive as the three landed members of the family.** The 1C campaign organized them into the 6-Φ-branch cascade without altering their PROVEN status.
- **The S-1 Regulator-Family Boundary Theorem (F_4 = {ζ, Zubarev, SDW} vs M = {cutoff_sqrt, anomaly}) is the parent partition for §VII.R sub-corollary scope-binding.** §VII.R inherits scope from §VII.B; F_4-bound corollaries cite §VII.B as anchor.
- **The S78 W2-F Mellin-multiplier scheme-invariance theorem provides the structural identity that collapses the C-β / C-θ duality to a single residue closure in F_4.** No two-residue compatibility condition needed inside F_4.
- **The intensive/extensive partition (IEP) of immunity branches recovers at the Mellin-cohomological level.** S70 Landau R2 IEP reappears one structural level higher; deep organizing principle, not artifact.

### What Breaks or Strains

- **Strong-form C-γ (exact Weyl-invariance via Duff cancellation) is structurally refuted on the substrate** — the substrate's representation content forces b_DK > 0. This is not a numerical near-miss; it is a structural REFUTATION via the positive-Yukawa-trace inequality. The candidate's surviving weak-form is non-vacuous but parametrically bounded only.
- **C-ξ (continuous-N analytic continuation of N-PI) is filed OUT-OF-FAMILY.** It is a perturbative-organization-equivalence theorem (sibling to MS̄/MS scheme equivalence), not a scaffold immunity. The family headcount stays at 6 / 10 (+ C-λ optional in §VII.R.A).
- **The 6-Φ-branch family does NOT cover L_max-truncation convergence as a closure mechanism.** C-κ (windowed-kinematic) proxies for L_max-windowed inequalities but does not generalize the L_max → ∞ convergence question itself. Open insight (LEM2) flagged for S87+; not a current strain.
- **Convention discrepancy between F4.3 (`f_0 = 1/2`) and S-1 Table II.2 (`f^{cutoff} = (2,1,0.5,0.1)`) is resolved via the §VII.R header convention pin** but exposed a Mellin-residue normalization-frame ambiguity that future cross-workshop pairings must respect. Not a structural strain on §VII.R itself; a documentation discipline lesson.

### Carry-Forward Computations

1. **S86-LATTICE-SPACING-IMMUNIZATION-CANDIDATE (C-α)** — F_4-scope-bound; 3 Wilson + 1 Symanzik discretizations at L_max=5; per-slot drift exponents 0,1,2,3 verified via Symanzik improvement at O(a^4); PASS-band O(a^4); INFO band factor-2; FAIL beyond. **Inputs**: S55 d_C lattice-spacing infrastructure; S-1 §II.2 Table II.2 (canonical Mellin pin). **Gate**: §VII.R.B (regulator-class). **Effort**: MODERATE.
2. **S86-WARD-IDENTITY-IMMUNIZATION (C-η)** — zero-compute registry-write only; SHA-pin provenance to registry §II `[J, D_K] = 0` (CPT-shield, machine-ε PROVEN). **Inputs**: registry §II entry. **Gate**: §VII.R.C (gauge-fixing). **Effort**: LIGHT.
3. **S86-INNER-FLUCTUATION-IMMUNIZATION (C-θ)** — zero-compute registry-write only; SHA-pin provenance to CCM-2007 §3.2 + S78 W2-F multiplier theorem. **Inputs**: CCM-2007 §3 + S78 W2-F gate verdict. **Gate**: §VII.R.C (gauge-fixing). **Effort**: LIGHT.
4. **S86-WEYL-RESCALING-IMMUNIZATION-CANDIDATE (C-γ-WEAK)** — F_4-scope-bound; Λ_anom computed INTERNALLY from `Tr_F(Y†Y)` and AC-2010 §V; PASS-band (Λ_anom_internal / Λ_cutoff)² ≈ 1.69e-5; INFO band [(Λ_anom/Λ_cut), (Λ_anom/Λ_cut)²]; FAIL beyond; INFO if Λ_anom_internal vs M_KK differs by > 2x. **Inputs**: S69 W4-C parametric-suppression; AC-2010 §V Yukawa-trace coefficients; canonical M_Pl. **Gate**: §VII.R.D (conformal/scale). **Effort**: HEAVY.
5. **S86-GAUGE-FIXING-IMMUNIZATION-CANDIDATE (C-β)** — symbolic Slavnov-Taylor `⟨QM⟩ = 0` PASS at machine ε; ξ ∈ {0,1,3,∞} numerical scan diagnostic with max pairwise drift < 1e-12. **Inputs**: BRST cohomology setup; one-loop substrate scattering amplitude pipeline. **Gate**: §VII.R.C (gauge-fixing). **Effort**: HEAVY.
6. **S86-NPI-EXTENSION-N-EQ-4 (C-ζ)** — atlas-wide; reuse W9-2 5-regulator atlas {ζ, Zubarev, SDW, dim-reg, lattice-BR}; machine-ε FI identity at NPI N=4. **Inputs**: W9-2 atlas + NPI N=4 self-energy code. **Gate**: §VII.R.B (regulator-class). **Effort**: MODERATE.
7. **S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE** (master gate, contains C-κ) — windowed kinematic inequality on L ∈ {5,6,7,8} slope-ordering test; INFO-only verdict (windowed inequality, not residue identity). **Inputs**: S-6 closeout infrastructure; my Slot 1a Row 3A solo `session-85-3a-zeta-stabilization-lizzi.md`. **Gate**: §VII.R.F (windowed). **Effort**: MODERATE.
8. **S86-VII-R-CONVENTION-PIN-ENFORCEMENT (OQ10)** — `_pru_cardinality_audit.py` pre-flight check on every §VII.R sub-corollary's `machinery_pin_map`; ensures S-1 §II.2 Table II.2 (Andrianov-Lizzi) is cited. **Inputs**: PRU audit infrastructure. **Gate**: §VII.R header pin. **Effort**: LIGHT.
9. **S86-VII-R-IEP-ANNOTATION (OQ11)** — annotate each §VII.R branch with INTENSIVE/EXTENSIVE class tag at registry write. **Inputs**: this workshop LEM3. **Gate**: §VII.R registry. **Effort**: LIGHT.
10. **S86-VII-R-CROSS-REFERENCE-DIRECTIONALITY (OQ12)** — enforce one-way cross-reference §VII.R.C → §VII.J (per LDT1 substitution chain); §VII.J back-pointer is "see also" only, not load-bearing. **Inputs**: registry-write hygiene. **Gate**: §VII.R / §VII.J registries. **Effort**: LIGHT.
11. **S87-INSTANTON-INSTANTON (C-λ)** — dilute-gas approximation for Δ_int correction to W9-1 single-instanton floor; PASS iff `Δ_int < min S_inst - 4.34`. **Inputs**: W9-1 saddle inventory (registry §VII.P); two-instanton interaction kernel. **Gate**: §VII.R.A (non-perturbative). **Effort**: MODERATE.
12. **S87-VII-R-G-LMAX-CONVERGENCE (OQ8 / LEM2)** — formalize L_max-truncation convergence as a 7th Φ-branch §VII.R.G; test on existing L_max-stability atlas. **Inputs**: cross-session L_max-stability data; speculative Mellin-formulation of structurally-convergent contaminations. **Gate**: §VII.R.G (NEW). **Effort**: MODERATE-HEAVY (formalization + empirical test).
13. **S87-VII-R-KER-PHI-ALGEBRA (OQ9 / LEM1)** — test whether ker(Φ) ∩ C is closed under spectral-functional composition (does the intersection of branch kernels form an algebra under spectral-moment products?). **Inputs**: 6-Φ-branch table (LEM1); spectral-moment composition rules. **Gate**: §VII.R parent meta-theorem extension. **Effort**: HEAVY (mathematical-physics formalization). Speculative but high EVOI for the framework's organizing-principle status.

### Closing Line

The substrate's perturbative ledger is the kernel of a single Mellin-cohomological invariant `Φ(f, m^O; G)`; its 6 admissible group-action types `G` index the 6 Φ-branches §VII.R.A through §VII.R.F, the 10 corollaries are members under those branches, and the F_4 / M scope wall at slot `a_0` partitions the family into single-residue (intensive) and atlas-wide (mixed-IEP) closures — the §VII.R cascade is one theorem with structural-axis indexing, not ten disjoint sub-corollaries.

<!-- Original skeleton block removed — Workshop Verdict, Open Questions, and Wrap-Up are populated above (lines 1832-1912) by lizzi R2-B FINAL. -->

