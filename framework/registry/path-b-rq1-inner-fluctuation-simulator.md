# Path B RQ-1 — Inner-Fluctuation Simulator on `D_K(τ_fold)`

## Origin

Derived from the Path B D2 workshop closure (`sessions/framework/registry/path-b-d2-workshop.md`,
2026-04-27). The workshop closed D2(a) (gradient flow on the bare spectral action with
Jensen `τ` as variable) for cause across three independent reviewers (NCG axioms, heat-kernel
math, Volovik analog tradition) plus contradiction with the project's S38 GGE-permanence
theorem. The workshop validated the user's "wrong question" reframing: NCG licenses
dynamics of EXCITATIONS (inner fluctuations `D → D + A + JAJ⁻¹`) on a fixed spectral
triple, not dynamics of the spectral triple itself. RQ-1 is the strongest of three
reframed-question candidates, supported by all three reviewers:

| Round | Verdict on RQ-1 | Anchor |
|:------|:----------------|:-------|
| Round 1 (Connes/NCG) | LICENSED — "the fields that ARE dynamical in standard NCG-SM treatment are inner fluctuations" | Chamseddine-Connes hep-th/0605011 |
| Round 2 (math) | LICENSED — existing static `D_K(τ_fold)` infrastructure handles per-timestep needs; YM+Higgs eom mathematically standard | Existing computation infrastructure |
| Round 3 (Volovik) | STRONGLY SUPPORTED — "literal description of Volovik's anti-GUT inversion" | Volovik 1004.0597 §VII |

## Goal

Simulate the dynamics of the gauge connection `A_μ(x,t)` and Higgs field `S(x,t)` on the
fixed spectral triple `(A, H, D_K(τ_fold))`, derived from the spectral action under inner
fluctuations. The simulator does NOT evolve the substrate (the spectral triple is fixed);
it evolves excitations on the substrate. This closes the dynamical-side ↔ spectral-side
loop the framework has been missing for ~80 sessions: spectral-side computation produces
canonical observables at static fixed points; this simulator produces time-resolved
excitation dynamics that should reproduce the same canonical observables at equilibrium
and predict additional time-dependent observables (post-quench relaxation, KK mode
dynamics, GGE-permanence cross-check).

## Architecture sketch

| Component | Specification |
|:----------|:--------------|
| **State variable** | `(A_μ(x,t), S(x,t), {a_n^KK(t)})` — gauge connection on emergent 4D × SU(3), Higgs scalar on the SU(3) fiber, KK mode amplitudes for the lowest several KK levels |
| **Evolution rule** | Yang-Mills + Higgs equations of motion derived from `S_spec[D + A + JAJ⁻¹]` per Chamseddine-Connes 0605011 inner-fluctuation prescription. Standard 2nd-order Lagrangian eom; symplectic Verlet or RK4 integrator |
| **Inner loop** | `D_K(τ_fold)` is precomputed ONCE via existing computation infrastructure (155,984 eigenvalues at L_max=10). Per-timestep cost is YM+Higgs eom solve on the gauge/Higgs phase space, NOT eigenvalue solve — order(s) of magnitude faster than D2(a) would have been |
| **Observables** | Gauge boson masses (Higgs vev × coupling), Higgs profile (vev minimum + curvature), KK tower frequencies and amplitudes, post-quench relaxation timescales, energy partition between modes |
| **Initial conditions** | Cold start: A = 0, S = 0 perturbed; quench to broken-symmetry vacuum and observe relaxation |

The substrate (D_K at τ_fold) sits as the static stage. The dynamical content lives on it.
This is exactly Volovik's Paper 25 §VII picture — gauge fields and gravity are expansion
parameters of the Green's function around a Fermi point — translated into NCG language.

## Pre-registered gates

**RQ1-G1 — Static-equilibrium observable recovery.** At simulator equilibrium (after
relaxation from cold start), the inferred values of `(m_H, m_W, m_Z, α_s(M_Z), n_s)`
must match the framework's canonical constants within 5%. PASS gates the dynamical
layer's faithfulness to the spectral side. FAIL surfaces a structural disagreement
between the static D_K computation and the dynamical-equilibrium answer it should
reproduce.

**RQ1-G2 — KK tower spectrum.** Fundamental and first KK frequencies, plus the ratios
to higher KK modes, must match canonical `M_KK = 7.43×10¹⁶ GeV` and the structural
ratios within 2%. Tests the inner-fluctuation construction on the fixed `D_K(τ_fold)`
beyond the zero-mode sector that G1 covers.

**RQ1-G3 — GGE-permanence verification (the discriminating gate).** After perturbing
the simulator from equilibrium and letting it evolve, post-quench relaxation must show
NO thermalization on simulator timescales (consistent with S38 GGE-permanence theorem).
Quantitatively: integrability charges (locally-conserved quantities of the BCS+Leggett
sector) must be conserved within 10⁻³ relative drift over `~10³` characteristic times.
**FAIL would surface a contradiction between simulator effective dynamics and the
framework's S38 integrability claim — i.e., either the simulator is not faithfully
implementing inner fluctuations, or the framework's GGE-permanence claim breaks under
finite-mode truncation.** This gate is the cleanest empirical handle on whether the
substrate is genuinely integrable or merely approximately so.

## Research questions (open)

1. **Time-discretization on the noncommutative SU(3) fiber.** Standard YM uses link
   variables on a lattice. Our SU(3) fiber is internally noncommutative; lifting the
   lattice prescription requires either a discretization of the fiber or a spectral-mode
   truncation. Mode-truncation is the natural fit (use the static D_K eigenmodes as
   basis), but the truncation error vs. mode count tradeoff is not characterized.

2. **Initial-condition class for cold start.** Volovik's Paper 25 cold-start picture
   (vacuum at τ=0 with no excitations, quenched to τ_fold) maps to "gauge field A=0,
   Higgs S=0 perturbed by quantum fluctuations." What's the right characterization of
   "quantum fluctuations" on the noncommutative manifold? Vacuum-state two-point
   functions of A and S are standard for ordinary manifolds; they need to be transcribed
   to NCG.

3. **Mapping simulator-output to canonical constants.** The framework's canonical `m_H`
   etc. are derived from spectral moments of D_K(τ_fold) — i.e., from the structure of
   the spectral triple itself. Does a simulator that evolves inner fluctuations on the
   fixed D_K reproduce these from time-resolved excitation dynamics, or are these
   purely static-spectral results that the simulator merely re-confirms? The answer
   determines whether RQ1-G1 is non-trivial or tautological.

4. **GGE-permanence on truncated mode counts.** S38's GGE-permanence proof assumes the
   full integrability structure. The simulator runs on a truncated mode count; does
   approximate integrability survive truncation, and at what threshold? Numerical
   experiments needed.

## Development tasks

| Task | Status | Effort |
|:-----|:-------|:------|
| Static D_K(τ_fold) cache + spectral-mode basis exporter | Existing (computation infra; just needs persistence layer) | ~1 day |
| YM+Higgs eom solver in torch on the emergent 4D × SU(3) phase space | New | ~5-7 days |
| Symplectic integrator with energy/charge monitoring | New (standard physics; reusable) | ~2-3 days |
| Observable extractors (gauge masses, Higgs profile, KK frequencies) | Partial (some static extractors exist) | ~2-3 days |
| Quench-and-relax driver script | New | ~1-2 days |
| GGE integrability-charge tracker | New (algebraic part of S38 needs operational form) | ~2-3 days |
| Pre-registered gates RQ1-G1, G2, G3 implementation + verdict-line emission | New | ~2 days |

**Total estimated effort**: 3-4 dev-weeks for a working prototype + first pass at all
three gates. ~1-2 months including iteration on whichever gates fail first time.

## Effort + risk

**Risk 1 — Static / dynamical disagreement (probability moderate)**: the simulator's
equilibrium might not reproduce the canonical static observables. If the discrepancy
is large, it could signal either (a) the simulator is incorrectly implementing inner
fluctuations, or (b) the static D_K(τ_fold) computation is missing dynamical
contributions. Triage by comparing per-mode contributions in the two settings.

**Risk 2 — KK tower mode-count truncation (probability moderate)**: at L_max=10 the
KK tower is finite; dynamical evolution of mid-tower modes may show artifacts not
present in the static computation. Mitigation: compare convergence at L_max=8 vs.
L_max=10; if KK-tower observables drift between, the truncation is the issue.

**Risk 3 — GGE-permanence gate is too strong (probability low-moderate)**: S38's
proof assumes an idealized integrable structure. Real simulator with truncated modes
may show small thermalization signal that's a numerical artifact, not a physical
violation. Mitigation: pre-register the 10⁻³ relative-drift threshold and treat
larger drift as informative (probably truncation, not framework breakdown), smaller
drift as confirming GGE-permanence.

**Risk 4 — Mathematical infrastructure gaps in NCG dynamics (probability moderate)**:
the YM+Higgs eom on a noncommutative manifold uses Chamseddine-Connes 0605011 as the
foundation, but specific implementation details (ordering of products, gauge-fixing
on the noncommutative fiber) may require workshops with `connes-ncg-theorist` to
resolve cleanly. Budget 1-2 mid-stream workshops for this.

## Dependencies

- **Static infrastructure**: `computations/` D_K(τ_fold) cache, spectral-mode
  basis exports. Currently invoked from canonical-constants pipeline; needs a
  per-mode-amplitude exporter for dynamical use.
- **Framework canonicals**: `m_H = 131.8 GeV` (derived), `M_KK = 7.43×10¹⁶`,
  canonical mass values for gates G1, G2.
- **Existing closures**: S38 GGE-permanence theorem (input to G3). S77 monotonicity
  (orthogonal but should be cross-validated).
- **Other RQs**: independent of RQ-2 and RQ-3 — they can run in parallel. RQ-1 is the
  foundational simulator on which RQ-3 (phase transition) could later be layered as
  pre-fold and post-fold instances.

## Recommended next-action

If committed to RQ-1: a single workshop with `connes-ncg-theorist` + `spectral-geometer`
to resolve the four research questions (especially #1 noncommutative-fiber discretization
and #2 initial-condition class) before architecture spec is frozen. Then a focused
3-4 dev-week implementation effort.

Lower-commitment alternative: run Round 2's Item 4 (Connes-Landi NC two-torus toy with
FGK Ricci density) as a 2-week numerics-infrastructure validation before committing to
RQ-1's full architecture. Validates the GPU eigenvalue inner loop + spectral-mode basis
manipulation in a setting where the answer is analytically known.
