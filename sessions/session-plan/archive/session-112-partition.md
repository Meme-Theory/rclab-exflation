# Session 112 — Wave Partition Manifest

**Mode**: fanout. **Source**: `session-112-context.md` (8 carry-forwards + register consumption). **3 compute waves + 1 workshop track.**

Bucketed by theme/leverage. Wave owner = reviewer-origin/substrate specialist (planner for that wave); gate executors named per gate. All gate IDs use the `CF-S112-*` namespace (no collision with the S111 `s111_gate_verdicts.txt` ID space). Verdict file: `computations/session-112/s112_gate_verdicts.txt`.

---

## Wave 1 — M_KK keystone + H0 closure `[Tier-1, highest leverage]`

**Theme**: Derive the dimensionful M_KK anchor from a substrate-natural scale (the §6.3 a(t)/effective-Friedmann residual's magnitude half), then re-test H0 band closure conditional on it.
**Owner / planner**: `volovik-superfluid-universe-theorist` (emergent-scale / BCS dimensional-transmutation specialist; the S110-CF-CV2A lineage).

| # | Gate ID | Executor | Scope |
|:--|:--------|:---------|:------|
| 1 | CF-S112-MKK-SUBSTRATE-ANCHOR | volovik-superfluid-universe-theorist | Substrate-natural dimensionful scale fixing M_KK without CODATA/M_Pl; re-run τ-RG two-leg test. KEYSTONE. |
| 2 | CF-S112-H0-BAND-CLOSURE | mack-cosmic-bridge | H0 residual band re-test, conditional on #1 (UPSTREAM dependency). |

**Sequencing**: #2 depends on #1 (proximate). The wave plan must mark the intra-wave dependency; at `/rclab-coordinate` time #2 fires after #1 lands (forward-pinned-intra-session npz input — benign Phase-3a `n_missing_npz≥1` signature, disposition (b)).
**Natural split candidates**: none (2 gates, tight dependency — keep together).

---

## Wave 2 — Stage-2 cross-axis verify cohort `[registry-completion; parallel-compute Q3]`

**Theme**: Four NON-AUTHOR Stage-2 cross-axis PASS-AND verifies of S111's new STAGE-1-CANDIDATE §VII theorems (CG/CH/CI/CJ). Parallel-compute-wave (4 independent gates, each producing its own PASS-AND verdict on orthogonal axes — Q3 per `Investigating-Workshops.md`, NOT an adversarial panel).
**Owner / planner**: `gen-physicist` (breadth/collation owner).

| # | Gate ID | §VII slot | Stage-0 author EXCLUSIONS | Axis-A / Axis-B |
|:--|:--------|:----------|:--------------------------|:----------------|
| 3 | CF-S112-CLOCKLOC3-STAGE2 | §VII.CG (registry :169) | schwarzschild-penrose-geometer, hawking-theorist | causal-structure / semiclassical-gravity |
| 4 | CF-S112-NOHOLOFLUX-STAGE2 | §VII.CH (:170 / body 22231) | einstein-theorist, loop-quantum-gravity-theorist | NCG-axiomatic (connes/vdd) / cosmological-bridge (mack/volovik) |
| 5 | CF-S112-M1-INTERTWINER-STAGE2 | §VII.CI (:171 / body 22267) | connes-ncg-theorist, van-den-dungen-bridge-theorist | NCG/K-homology / C*-algebra-representation |
| 6 | CF-S112-VIICJ-STAGE2 | §VII.CJ (:172 / body 22301) | transit-dynamics-theorist | (both axes; transit is the sole Stage-0 math owner) |

**Discipline (per `joint-theorem-promotion.md §"Stage 2"`)**: each gate dispatches TWO cross-reviewers IN PARALLEL, axis-distinct, NON-AUTHOR (+ downstream-inheritance-reach exclusion), operating WITHOUT prior workshop transcript (read only the registered Stage-1 entry). JOINT clauses PASS-AND across both verdicts (logical AND). Reviewer-selection violations → plan-freeze HARD-HALT per `_joint_theorem_independent_verify_audit.py`. Cross-reviewer audit-machinery must not be self-authored (clause 6).
**Natural split candidates**: split into W2a {CG, CH} + W2b {CI, CJ} if the 8-reviewer concurrency exceeds the dispatch cap or a planner stalls.

---

## Wave 3 — compact-object + Floquet precision `[Tier-3 / non-blocking]`

**Theme**: Two independent precision/refinement computes — bracketed white-hole microstate count (land the ratio at unity) and the h_par 10%-pin via a physical late-time V_eff.
**Owner / planner**: `gen-physicist` (cross-domain; two distinct substrates).

| # | Gate ID | Executor | Scope |
|:--|:--------|:---------|:------|
| 7 | CF-S112-B5A-BRACKETED | hawking-theorist | Interpolate between edge-only (undershoot) and island (overshoot) → microstate/(A/4) within 10%. |
| 8 | CF-S112-FLOQUET3-HPAR-TIGHTEN | transit-dynamics-theorist | Re-integrate coupled modulus+Friedmann ODE with physical late-time V_eff; pin h_par to 10%. NON-BLOCKING. |

**Natural split candidates**: split into per-gate sub-waves if either planner stalls (the two gates are independent — clean split boundary).

---

## Workshop track (NOT a compute wave) — EVOI-frontier dive (`--extra`)

Authored at plan-freeze as `sessions/session-112/session-112-workshop-schedule.md` (orchestrator-authored, register-grounded). Targets the high-leverage EVOI standing gaps with NO tractable compute gate, per the `--extra` directive ("dive into EVOI items, similar to S110"). Seven candidate workshops (genuine Q1 adversarial tensions per `Investigating-Workshops.md` four-condition definition):

1. **WS-KPIVOT** — K_pivot scale-mapping (atlas-04 C2): substrate-derived bridge vs irreducible external calibration. [HIGH observational — "single largest observational load-bearing gap"]
2. **WS-TAUFOLD** — τ_fold relaxation: surviving dynamical mechanism-chain vs empirical-parameter acceptance. [the last tuned number; one-loop/variational corridors dead S95]
3. **WS-CCRESID** — residual-3% CC: Volovik-partition higher-order closure vs genuine new-physics residual + the BBN-epoch arm Q29. [Tier-1 #2 live edge]
4. **WS-DMMASS** — 170× DM-mass anchor: surviving mass-anchor mechanism vs irreducibly-unanchored Leggett mass. [HARDENED-OPEN; abundance intact]
5. **WS-AS-HTILDE** — A_s magnitude / CF21 TD-LI H̃-divergence: which leg sets the amplitude floor. [EVOI flags this "workshop-class adjudication"]
6. **WS-OBSAXIS** — §EVOI.BF CMB-orthogonal steer: NICER pulsar-mass EoS vs DESI/Euclid f·σ8 growth as the next falsifiable non-CMB prediction. [strategic; the BF re-anchor's load-bearing forward consequence]
7. **WS-YUKSHAPE** — homogeneity-obstruction SHAPE branch (#9b): off-Casimir-calculus route (full SU(3) σ-model) vs genuine wall. [fermion-mass frontier]

Lower-tier candidates (conceptual Tier-4, listed for completeness, default not scheduled): ARROW-OF-TIME (#15), BORN-RULE (#16) — derivation-open, likely solo/review not adversarial workshop.

**Routing**: the workshop schedule feeds `/rclab-review` / `/rclab-workshop` dispatches (separate from `/rclab-coordinate` compute). It is NOT consumed by `/rclab-plan`'s compute-wave pipeline.
