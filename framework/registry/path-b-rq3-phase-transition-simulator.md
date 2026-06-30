# Path B RQ-3 — Phase-Transition Simulator Across `τ_fold` (Bogoliubov Scattering Matching)

## Origin

Derived from the Path B D2 workshop closure (`sessions/framework/registry/path-b-d2-workshop.md`,
2026-04-27). RQ-3 is the framework-native cosmogenesis companion to RQ-1, supported
strongly by all three reviewers and most directly grounded in existing framework
infrastructure:

| Round | Verdict on RQ-3 | Anchor |
|:------|:----------------|:-------|
| Round 1 (Connes/NCG) | LICENSED — impulsive scattering matching does NOT require τ-evolution dynamics; the fold is treated as a non-analytic boundary, not a smooth attractor | First-order phase-transition language already in framework |
| Round 2 (math) | LICENSED — existing infrastructure (`s85_w6_acoustic_white_hole_formal.py`, `s52_bogoliubov_amp.npz`) handles per-step needs | Existing computation |
| Round 3 (Volovik) | STRONGLY SUPPORTED — direct laboratory analog (Rolley et al. hydraulic-jump 4He); matches Volovik Paper 09 + Paper 27 + Paper 25 §V structure | Volovik #09 (`physics/0508215`), #27 (`gr-qc/9901077`), #25 (`1004.0597 §V`) |

RQ-3 differs structurally from RQ-1 and RQ-2 in that it does NOT attempt to evolve the
substrate or any deformation parameter. Instead it treats the fold transit as an
*impulsive boundary* between two distinct vacuum states (pre-fold, post-fold), and computes
the Bogoliubov coefficients that connect their mode amplitudes. The dynamics on each side
of the fold is Hamiltonian wave evolution; the fold itself is a discontinuity, not a
smooth gradient flow.

## Goal

Build a simulator that computes the Bogoliubov coefficient structure across the τ_fold
phase transition, given pre-fold mode amplitudes as input and producing post-fold mode
amplitudes (occupation numbers, GGE relic structure) as output. The framework already
contains all the physical content for this in scattered form (`s85_w6_acoustic_white_hole_formal.py`,
`s52_bogoliubov_amp.npz`, S37-38 GGE-relic results, S58 Volovik partition, S60 collab
review). RQ-3 is mostly **operationalization**: package the physics as a callable
observable-generator and pre-register gates against the framework's canonical predictions.

The lab analog is direct: Volovik's Paper 09 hydraulic-jump white hole in superfluid 4He
(Rolley et al. cited therein) is a 2+1D Painlevé-Gullstrand metric with discontinuous
horizon — the same structure as the framework's substrate transit at τ_fold (Mach 13.75
supersonic transit per `project_substrate-not-c-limited.md` + `s85_w6_acoustic_white_hole_formal.py`).

## Architecture sketch

| Component | Specification |
|:----------|:--------------|
| **State variable** | Pre-fold and post-fold mode amplitudes `{α_n^pre(t), β_n^pre(t)}` and `{α_n^post(t), β_n^post(t)}` for the relevant phonon / KK / fermion modes |
| **Evolution rule** | Each side: Hamiltonian wave dynamics derived from the spectral action at fixed τ on that side. Across the fold: Bogoliubov scattering matrix `B` connecting pre-fold to post-fold mode amplitudes via `(α_post, β_post)^T = B · (α_pre, β_pre)^T` |
| **Inner loop** | Pre-fold simulator and post-fold simulator both use existing static-D_K infrastructure at the appropriate τ; matching layer is the new computation. Per-step cost is a single-mode Bogoliubov coefficient evaluation |
| **Observables** | GGE occupation numbers `n_eff`, post-transit power spectrum (→ `n_s`), Mach-13.75 transit kinematics, integrated post-fold energy and entropy budgets |
| **Initial conditions** | Pre-fold ground state (vacuum at `τ < τ_fold`); evolve through the fold via the matching prescription; observe post-fold relic |

## Pre-registered gates

**RQ3-G1 — n_eff prediction.** Post-transit GGE occupation numbers must reproduce the
framework's canonical `n_eff` prediction within 2%. The canonical value is the framework's
existing prediction from `s37`/`s38` GGE-relic computations and Mack-bridge analyses.
PASS validates the simulator's transit-physics implementation. FAIL surfaces a
discrepancy between the assembled simulator and the framework's existing canonical
prediction — informative either way.

**RQ3-G2 — Spectral tilt n_s from post-fold acoustic interference.** Post-fold acoustic
interference pattern, computed from the GGE relic occupation numbers + Bogoliubov phase
relations, must reproduce `n_s = 0.9561` (canonical, framework-derived) within tolerance
of 0.005 (≈0.5% — tight gate appropriate for the canonical value's reported precision).
PASS gates the framework's claim that `n_s` arises from substrate transit physics, not
from inflationary slow-roll. FAIL would either surface a missing piece in the existing
substrate-transit computation or refine the framework's canonical n_s derivation.

**RQ3-G3 — Mach-13.75 transit kinematics.** The supersonic transit profile (per
`project_substrate-not-c-limited.md` and `s85_w6_acoustic_white_hole_formal.py`) must
reproduce the canonical Mach number 13.75 ± 5%. Tests the kinematic match independently
of the dynamic Bogoliubov calculation. PASS gates that the simulator's pre-fold and
post-fold sound speeds, plus the transit velocity, are internally consistent with the
established framework canonical.

## Research questions (open)

1. **Matching prescription at the τ_fold boundary.** The Bogoliubov matching connects
   pre-fold and post-fold mode amplitudes via specific boundary conditions
   (continuity of field, jump in derivative determined by the fold's free-energy
   discontinuity). The framework's existing transit physics (`s85_w6_acoustic_white_hole_formal.py`)
   uses one matching prescription; the literature has multiple alternatives (Israel
   junction conditions, Andreev reflection at superfluid interface, Painlevé-Gullstrand
   horizon-crossing). Need a workshop to establish which is canonical for this
   framework, with backup tests against the others.

2. **Pre-fold initial state characterization.** What's the pre-fold vacuum state? The
   framework's S58 Volovik partition gives `w_0 = -0.918` (later migrated to `-0.842`
   per S86 W13 ledger), which sets the pre-fold equation-of-state. The pre-fold
   ground-state mode occupation is presumably zero (vacuum), but quantum fluctuations
   set the initial Bogoliubov amplitudes. Need to spec the pre-fold quantum vacuum
   precisely.

3. **Post-fold evolution timescale.** GGE-permanence (S38) says the post-fold relic
   never thermalizes. But the simulator runs on finite time intervals; over what
   timescale should the gates G1, G2 be evaluated? The natural choice is the Mack-
   bridge-relevant timescale (when CMB freeze-out happens), but this needs framework-
   canonical pinning.

4. **Coupling between RQ-3 and RQ-1.** RQ-1 (inner-fluctuation simulator on fixed D_K)
   and RQ-3 (pre-fold/post-fold transit simulator) are complementary: RQ-1 simulates
   physics on each side of the fold; RQ-3 simulates the transit between them. The two
   could be combined into a single full-cycle simulator (cold start at τ=0 → relax
   pre-fold → transit through fold → post-fold relic → observed CMB structure). Worth
   sketching this combined architecture before either is committed.

## Development tasks

| Task | Status | Effort |
|:-----|:-------|:------|
| Pre-fold and post-fold static-D_K caches at the relevant τ values (e.g., τ = 0.18 and 0.20) | Existing infra; needs per-side persistence | ~1 day |
| Pre-fold and post-fold Hamiltonian wave evolvers (separate phase spaces) | Partial (existing time-dependent structure scattered across S37/S38/S52) | ~3-5 days |
| Bogoliubov scattering matrix `B` calculator at the fold boundary | Partial (`s52_bogoliubov_amp.npz` exists; needs operationalization as callable) | ~2-3 days |
| Matching prescription enforcer (junction conditions / horizon-crossing) | New (research question #1 must close first) | ~2-3 days |
| GGE occupation extractor and `n_eff` aggregator | Partial (S37/S38 work) | ~1-2 days |
| Post-fold acoustic-interference → `n_s` mapper | Partial (existing canonical derivation; needs simulator-callable form) | ~2-3 days |
| Mach-number profile extractor | Existing (`s85_w6_acoustic_white_hole_formal.py`) | ~1 day |
| Pre-registered gates RQ3-G1, G2, G3 implementation | New | ~1-2 days |

**Total estimated effort**: 2-3 dev-weeks for a working prototype. Less than RQ-1
because most of the physical content already exists in the framework — RQ-3 is a
package-and-gate effort more than a build effort.

## Effort + risk

**Risk 1 — Re-skinning of existing infrastructure (probability moderate-high)**: RQ-3
overlaps significantly with existing S37/S38/S52/S85 work. The risk is that the
"simulator" ends up being a thin wrapper around already-existing physics, and the new
gates (G1, G2, G3) are implicitly already passed by the existing computations. Counter-
argument: even if so, the systematic packaging makes the framework's existing transit
physics callable and re-usable, which is value of its own.

**Risk 2 — Matching-prescription ambiguity (probability moderate)**: research question
#1 might not close cleanly. Multiple matching prescriptions could give different
quantitative predictions, especially for `n_eff`. Mitigation: pre-register the canonical
prescription from `s85_w6_acoustic_white_hole_formal.py` and treat alternative
prescriptions as variants whose mismatch with the canonical gates is informative.

**Risk 3 — Pre-fold vacuum specification gaps (probability moderate)**: research
question #2 requires precise specification of the pre-fold quantum vacuum. If this
turns out to require new derivation rather than existing canonicals, RQ-3's effort
balloons. Mitigation: workshop with `transit-dynamics-theorist` + `hawking-theorist`
+ `volovik-superfluid-universe-theorist` early to scope the vacuum specification.

**Risk 4 — n_s gate is too tight (probability low-moderate)**: 0.5% tolerance on
G2 is tight given that the existing canonical derivation has its own uncertainty.
Mitigation: pre-register a 1% tolerance with 0.5% as the stretch goal; report both.

## Dependencies

- **Static infrastructure**: D_K caches at pre-fold and post-fold τ values, existing
  Bogoliubov amplitude calculations.
- **Existing scripts**: `s85_w6_acoustic_white_hole_formal.py`, `s52_bogoliubov_amp.npz`,
  S37/S38 GGE-relic outputs, `s58_volovik_partition.py` (or analog).
- **Framework canonicals**: `n_eff` (canonical), `n_s = 0.9561`, Mach-13.75 transit,
  `w_0 = -0.842` (S86-migrated value).
- **Closures**: S38 GGE-permanence (input to interpretation of post-fold relic).
- **Other RQs**: complementary to RQ-1 (which simulates dynamics on each side of the
  fold). RQ-3 + RQ-1 could combine into a full-cycle simulator. Independent of RQ-2.

## Recommended next-action

If committed to RQ-3: a single workshop with `transit-dynamics-theorist` +
`volovik-superfluid-universe-theorist` + `hawking-theorist` to close research questions
#1 (matching prescription) and #2 (pre-fold vacuum specification). Estimated 1 day for
the workshop. Then ~2-3 dev-week implementation effort.

If committed to RQ-1 + RQ-3 combined: scope the joint architecture first — they share
substantial infrastructure (static D_K caches) and sequence naturally (cold start →
pre-fold relax → transit → post-fold). Combined effort estimate: 4-6 dev-weeks for both.

RQ-3 has the highest framework-internal-leverage of the three reframings: the lab analog
is direct (Rolley et al. hydraulic-jump 4He), the physical content is already established
(S37/S38/S58/S85), and the gates are tied to canonical observables (`n_eff`, `n_s`)
that the framework already predicts. The risk is that RQ-3 ends up being a packaging
exercise rather than new physics — but that's not a failure mode if the packaged
infrastructure becomes reusable for the broader framework calculator goal.
