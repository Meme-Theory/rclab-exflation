# Path B RQ-2 — Λ-Running via Chamseddine-Connes Scale-Invariance Dilaton

## Origin

Derived from the Path B D2 workshop closure (`sessions/framework/registry/path-b-d2-workshop.md`,
2026-04-27). RQ-2 is the smaller-scope fallback among three reframed-question candidates,
supported PARTIALLY by all three reviewers but with caveats:

| Round | Verdict on RQ-2 | Caveat |
|:------|:----------------|:-------|
| Round 1 (Connes/NCG) | PARTIALLY LICENSED | Dilaton has its own EOM via `δS_spec/δφ = 0`, but this is still a critical-point principle, not a flow rule; needs FRW coupling for any actual evolution |
| Round 2 (math) | PARTIALLY LICENSED | Well-defined for FRW background; dilaton mass + friction is still a research question |
| Round 3 (Volovik) | PARTIALLY SUPPORTED | q-theory matches `Λ ~ K³_QCD / E²_Planck` (Volovik #14 Eq. 6.7), but caveat: must couple to FRW background; analog precedent is Volovik q-theory operationalization (existing `s53`, `s67`, `s71` scripts) |

The reduced-scope nature of RQ-2 is structural: it does not aim to produce a "full
substrate simulator" — only to make the cosmological-constant cutoff scale `Λ` dynamical
via the Chamseddine-Connes 0512169 dilaton mechanism, and demonstrate that the dilaton
equilibrium reproduces the framework's canonical Λ_cc.

## Goal

Operationalize Chamseddine-Connes hep-th/0512169 ("Scale Invariance in the Spectral
Action") as a dynamical equation for the dilaton scalar field `φ(x,t)`, where `Λ → Λ·e^φ`
makes the spectral cutoff scale dynamical. The dilaton couples to a Friedmann-Robertson-
Walker background, with cosmological friction `3H · dφ/dt` providing dissipation. At
equilibrium, the dilaton settles into a configuration whose effective Λ matches the
canonical cosmological-constant-relevant scale.

This is the most direct framework-NCG bridge to q-theory. The Volovik-Klinkhamer
gluon-condensate q-running (Paper 14 Eq. 6.7) gives `Λ ~ K³_QCD / E²_Planck ~ (3×10⁻³ eV)⁴`
which matches the observed cosmological constant. RQ-2 asks whether the CC dilaton, under
Friedmann coupling, produces the same answer.

## Architecture sketch

| Component | Specification |
|:----------|:--------------|
| **State variable** | Dilaton scalar `φ(x,t)` on emergent 4D, plus FRW scale factor `a(t)` and Hubble `H(t)` |
| **Evolution rule** | Klein-Gordon-like equation `□φ + V'(φ) = 0` derived from `δ S_spec[Λe^φ]/δφ` per CC 0512169; FRW coupling adds Hubble friction `□φ → □φ - 3H·∂_t φ` |
| **Inner loop** | Per-timestep: spectral action moments `a_n(τ_fold; Λ·e^φ)` via existing static D_K infrastructure with Λ-rescaling. ~1 spectral-action evaluation per timestep |
| **Observables** | Effective `Λ_eff(t) = Λ·e^{φ(t)}`, equilibrium Λ_cc, dilaton mass `m_φ`, time-evolution under Hubble friction |
| **Initial conditions** | Cosmological boundary: `φ(t=t_0) = 0`, `a(t_0) = a_initial`, `H(t_0) = H_initial`. Evolve forward in cosmic time; observe `Λ_eff` relaxation |

## Pre-registered gates

**RQ2-G1 — Equilibrium-Λ recovery.** At late-time equilibrium under Hubble friction,
the simulator's `Λ_eff = Λ·e^{φ_eq}` must match the framework's canonical cosmological-
constant-relevant scale within 30% (a generous tolerance reflecting the OOM-level nature
of the CC observation). PASS would empirically validate the CC dilaton mechanism as a
cosmological Λ-runner. FAIL would surface that the bare CC dilaton is insufficient and
needs additional structure (q-theory thermodynamic potential, dressing terms).

**RQ2-G2 — q-theory cross-check (`Λ ~ K³_QCD/E²_Planck`).** Compare RQ-2 trajectory of
`Λ_eff(t)` against the existing q-theory operationalization (`s53_q_theory_gge.py`,
`s71_cc_from_gge_residual.py`). The two should agree on the equilibrium answer within
10% (since they're derived from related physics — the CC dilaton is the NCG dual of
the q-field). PASS gates the framework-internal consistency. FAIL would reveal that
the dilaton-NCG and q-theory routes give substantively different numerical predictions,
which is interesting either way.

**RQ2-G3 — Klein-Gordon mode spectrum.** The dilaton's mass `m_φ` and the lowest
oscillation frequency must be consistent with the spectral moment structure that
generated them — specifically, the dilaton mass should arise from the curvature of
`a_4(τ_fold; Λ·e^φ)` around `φ = 0`, which is a known framework computation. PASS
gates internal consistency. FAIL would reveal a structural error in the mapping
between the spectral action and the dilaton effective potential.

## Research questions (open)

1. **Coupling of dilaton to FRW background.** The CC 0512169 paper treats `Λ → Λ·e^φ`
   in a Wick-rotated static setting. Lifting to FRW requires identifying the right
   non-minimal coupling (e.g., a `ξ·R·φ²` term) and verifying that under cosmological
   evolution the dilaton picks up Hubble friction `3H·∂_t φ`. This is research, not
   derivation; standard scalar-field-on-FRW analysis applies but the NCG-derived
   couplings might modify the standard Klein-Gordon form.

2. **Dilaton effective potential from `a_n` curvature.** The mass `m_φ` arises from
   `∂² S_spec/∂φ²|_{φ=0}`. This needs explicit computation against the existing static
   `a_n(τ_fold)` infrastructure with `Λ·e^φ` substitution. Probably ~1 day of compute
   on the existing computation stack.

3. **Equilibrium uniqueness.** Does the CC dilaton's effective potential have a unique
   minimum at the cosmological-Λ-relevant scale, or multiple minima (false vacua)?
   The S84 W8a-90 constraint map's "DRESSED-SPECTRAL-ACTION as VP: OPEN" branch
   suggests the dressed potential might have multiple critical points; the bare-spectral-
   action-with-dilaton case needs explicit characterization.

4. **q-theory ↔ NCG dilaton equivalence.** Both produce Λ ~ K³_QCD/E²_Planck at the
   right OOM. Are they equivalent (same equation under different parameterization), or
   distinct (give different answers in some regime)? RQ2-G2 tests this empirically;
   the mathematical answer would inform whether RQ-2 adds anything beyond existing
   q-theory work.

## Development tasks

| Task | Status | Effort |
|:-----|:-------|:------|
| Spectral action with Λ-rescaling: `S_spec(τ_fold; Λ·e^φ)` callable | Partial (existing static evaluator; needs φ wrapping) | ~1 day |
| Dilaton effective potential `V(φ)` extraction via `∂² S_spec/∂φ²` at multiple φ values | New | ~2 days |
| Klein-Gordon evolver on FRW background with Hubble friction | New (standard physics) | ~2-3 days |
| Coupling to existing q-theory pipeline (`s53`, `s67`, `s71`) for cross-check | Partial | ~2 days |
| Pre-registered gates RQ2-G1, G2, G3 implementation | New | ~1-2 days |

**Total estimated effort**: 1-2 dev-weeks for a working prototype + first pass at all
three gates. Smaller scope than RQ-1 because most of the infrastructure (static D_K,
q-theory operationalization) is already in place.

## Effort + risk

**Risk 1 — RQ-2 is duplicative of existing q-theory (probability moderate)**: the
framework's `s53_q_theory_gge.py`, `s67_volovik_q_a0.py`, `s71_cc_from_gge_residual.py`
already operationalize q-theory dynamics. RQ-2 might be a re-skinning rather than new
physics. RQ2-G2 would catch this; if the two routes give identical answers, RQ-2 has
no value beyond rigor.

**Risk 2 — FRW coupling is non-trivial (probability moderate)**: the dilaton's non-
minimal coupling to gravity (`ξ·R·φ²` etc.) is a research question, not a derivation
from spectral action axioms. Different coupling choices could give different
quantitative answers, undermining the predictive power of RQ2-G1.

**Risk 3 — Bare-spectral-action limitations carry over (probability moderate)**: the
workshop established that the bare spectral action is monotonic in τ. Whether the
dilaton CC mechanism inherits similar monotonicity-vs-attractor structure depends on
the coupling and is not yet characterized. If the dilaton effective potential is also
monotonic in φ, RQ-2 would inherit the same equilibrium-existence problem D2(a) had.

**Risk 4 — Low overall framework value (probability moderate)**: RQ-2's smallest-scope
nature means it produces a single observable (Λ_eff) rather than the broad set RQ-1
or RQ-3 would produce. If the framework's existing static-side computation already
matches Λ_cc, the dynamical version adds rigor but not new physics.

## Dependencies

- **Static infrastructure**: existing computation spectral-action moment evaluator (`a_n(τ_fold; Λ)`)
  with Λ as a passable parameter.
- **q-theory pipeline**: `s53_q_theory_gge.py`, `s67_volovik_q_a0.py`, `s71_cc_from_gge_residual.py`
  for cross-check.
- **Framework canonicals**: canonical Λ_cc (cosmological-constant-relevant value).
- **Other RQs**: orthogonal to RQ-1 (which fixes Λ at the static cutoff) and RQ-3
  (which simulates fold-transit dynamics, not Λ-running). Could combine with either
  if the cosmological-Λ running is a sub-component.

## Recommended next-action

If RQ-2 is selected as the priority: a single 1-day cross-check against existing
q-theory output to determine whether RQ-2 is duplicative. If duplicative, redirect
effort to RQ-1 or RQ-3. If RQ-2 produces substantively different predictions, then
proceed with full ~1-2 dev-week implementation.

Lower-commitment alternative: bundle RQ-2 as a sub-component of RQ-1 (where the
static D_K(τ_fold) is the substrate but Λ becomes dynamical via dilaton on top of
the inner fluctuations). This avoids the "smaller-scope-fallback" issue by making
RQ-2 part of a larger architecture rather than standalone.

RQ-2 is most defensible as a **rigor pass** on the existing q-theory results — providing
an independent NCG-internal derivation of the same answer — rather than as a primary
research target. It's the lowest-leverage of the three reframings.
