# Session 85 Plan — Wave W5: lizzi-origin reviewer wave

**Generated**: 2026-04-21
**Owner**: lizzi-spectral-functional-theorist
**Theme**: lizzi-origin single-reviewer wave — spectral functional alternatives, regulator-scan atlas,
layer-dissonance (L0/L3) registry, FI-parity wall for ε_H, HP^0/HP^1 cohomology-disjoint-corridor
spectral-functional comparison, L_max sanity, lattice-join functoriality, two-layer obstruction.
**Item count**: 7

---

## Wave W5 Summary

W5 operationalizes the lizzi-origin carry-forward: the *spectral functional is itself a physical
degree of freedom*, and W5 turns each outstanding lizzi observation into a pre-registered gate that
either (i) lands the result as a permanent-results-registry entry (items 1, 3, 7), (ii) tests a
structural claim for robustness (items 2, 4, 5), or (iii) measures the size of a regulator-scheme
degree of freedom on an observable already declared functional-independent by ε_H-parity (item 6).

Substrate framing (non-negotiable across all 7 gates):

- The CC is a spectral MOMENT of D_K, not a "size" of the universe. `Tr f(D_K/Λ)` is the action;
  different f (cutoff sqrt, zeta, anomaly-derived, SDW, Zubarev) weight different moments.
- What survives regulator choice is STRUCTURAL (walls of solution space). What depends on regulator
  choice is a PHYSICAL DOF requiring a separate determination (consistency, experiment, or axiom).
- No gate in W5 may import "the" spectral action; every gate must name its f AND its layer tag.

Cross-cutting machinery (applies to every gate in W5):

- Python: `phonon-exflation-sim/.venv312/Scripts/python.exe`.
- GPU policy: if matrix dim ≥ 100×100, prefer `torch.linalg` (ROCm 7.2, RX 9070 XT). Otherwise cap
  CPU threads via `os.environ.setdefault('OMP_NUM_THREADS', '8')` before `import numpy`.
- canonical_constants: every script imports `from canonical_constants import *` (S34+ rule).
- Script prefix: `s85_w5_<slug>.py`, data `s85_w5_<slug>.npz`, plot `s85_w5_<slug>.png`.
- Verdict file (single canonical path): `computations/s85_gate_verdicts.txt`.
- Closure SHA: full 64-hex, emitted by the producing script at gate close (per
  `.claude/rules/gate-verdicts.md`).
- Regulator atlas (5-regulator canonical set, per S83 three-layer synthesis):
  `{zeta, Zubarev, SDW, cutoff_sqrt (≡ f(x)=√x), anomaly-derived}`.

---

## Wave W5 Decision Point Prerequisites

W5 does not emit to downstream waves; it is a reviewer-origin breadth wave. However, it CONSUMES
the following W0 outputs (if landed before W5 dispatch):

- **W0 CC-1 (η-invariant of full Jensen-SU(3)×A_F)** — if PASS with η computed in the zeta scheme,
  W5-§W5-6 regulator-scan ‖[ε_H]‖_{HP^1} can adopt the same zeta-closure SHA for the ε_H slot.
- **W0 CC-2 (Spin(8) triality orbit sum of χ_2)** — provides the χ_2 slot under triality orbits,
  which W5-§W5-2 (HP^0 intra-corridor) cites for the spectral-functional comparison baseline.
- **W0 CC-3 (Connes-Moscovici dimension-spectrum signed residue sum)** — provides residue-sum SHA
  that W5-§W5-3 (L0/L3 layer-dissonance) registers as the L0 representative.
- **W0 CC-5 (L_max ≥ 11 asymptotic refit)** — provides the asymptotic cluster-span refit that
  W5-§W5-5 (Layer-aware lattice-join functoriality) reuses as the baseline cluster-rank input.

Dependency discipline (per `feedback_dispatch-discipline.md`): W0 prereqs are *planner expectations*,
not halt-commands. If W0 has not landed a given SHA at W5 dispatch time, the W5 gate may proceed
by pinning `<computed-at-runtime>` for that input and emitting an internal SHA from the prior-wave
fallback (documented in §W5-{n} Machinery pin).

---

## §W5-1. S85-W5-1-FI-PARITY-REGISTRY — FI-parity theorem registration in §VII-B (ε_H permanent wall)

**Trigger**: `[VERIFY-THEOREM]` (registry landing; ε_H FI-parity is a S71/S72/S73a-supported structural claim;
this gate freezes the parity wall as a permanent §VII-B entry).

**Classification**: GEOMETRIC (spectral-triple parity of ε_H in KO-dim=6) — the parity datum is the
signature of the spectral triple under the real-structure J, not a phononic excitation.

**Agent type**: lizzi-spectral-functional-theorist (OWN; my registry-landing territory).

**Hypothesis**: The parity of `[ε_H]` under J-action (KO-dim=6 real structure) is a functional-
INDEPENDENT structural datum across all 5 regulators {zeta, Zubarev, SDW, cutoff_sqrt, anomaly}.
Specifically: sign(⟨ψ, J ε_H ψ⟩) is regulator-invariant for every ψ in the relevant KK-class.
This makes ε_H-parity a *permanent wall* — any mechanism claiming to flip the ε_H sign is closed.

**Method**:
- Script: `computations/s85_w5_1_fi_parity_registry.py`.
- Data: `s85_w5_1_fi_parity_registry.npz`; plot: `s85_w5_1_fi_parity_registry.png`.
- Canonical constants: `from canonical_constants import M_KK, tau_fold, L_max_canonical`.
- GPU/CPU: eigen-projection onto the ε_H component uses dim ≥ 155,984 (full L_max=10 spectrum);
  REQUIRED `torch.linalg` (GPU) — no numpy fallback for this gate.
- Reuses S66 eps_H sign-flip data (zeta vs cutoff) + S70 EPSH-ALPHA-70 + S71 CORRELATED-SENSITIVITY-71
  + S72 GILKEY-REEVAL-72 + S73a SPECTRAL-ACTION-PROFILE-73a.
- Per regulator, compute `sig(r) = sign(⟨ε_H, J ε_H⟩)` on the canonical eigenvector basis at
  L_max=10. Verify `sig(r) == sig(zeta)` for all r in the 5-regulator atlas.
- Input SHAs (pre-computed, static): the five S71-S73a npz files (zeta, Zubarev, SDW, cutoff_sqrt,
  anomaly-derived) — each pinned via SHA-256 at script start.

**Machinery pin (PRDR)**:
- `N_eval = 155984` (full L_max=10 D_K spectrum; single-crystal NOT fabric — see Lizzi memory
  `feedback_reporting-framing.md`, but parity is per-mode so single-crystal is admissible HERE).
- `L_max = 10` (canonical); `L_max_sensitivity = {8, 9, 10}` for robustness.
- `scan_range = N/A` (parity is boolean-valued, no scan).
- `step_size = N/A`.
- `tolerance = THEOREM` (exact sign match; any non-match is FAIL, no numerical slack).
- `scheme = 5-regulator atlas` (see Wave summary).
- `convention = KO-dim=6 J-action; Connes real-structure canonical form`.
- `random_seed = 42` (documentation — parity is deterministic).
- `GPU path = torch.linalg on ROCm 7.2; MANDATORY` (dim ≥ 100×100 rule).

**Expected output 4-tuple**: `(value = True, scheme = 5-regulator-atlas,
convention = KO-dim=6-J-canonical, L_max = 10)`.

**PASS / FAIL / INFO**:
- **PASS** if `sig(zeta) == sig(Zubarev) == sig(SDW) == sig(cutoff_sqrt) == sig(anomaly)` AND the
  common sign matches the S66/S71/S72 record. Registry entry §VII-B-{next} lands with ε_H FI-parity
  as a permanent wall.
- **FAIL** if any regulator flips the sign. The parity wall is demoted to SCHEME-DEPENDENT;
  §VII-B landing blocked; project registers a new STRUCTURAL-REGULATOR-DISSONANCE cluster.
- **INFO** if only 4/5 regulators agree AND the 5th is a known structurally-excluded regulator
  (e.g., anomaly-derived on non-KK-compatible sector, per S67 FUNCTIONAL-SELECT-67).

**Substitution chain [SIGN]**:
```
Step 1 (definition): sig(r) = sign(⟨ε_H, J ε_H⟩)_{L^2(E_D)}, where
  J is KO-dim=6 real structure, ε_H is Higgs-fiber fluctuation mode (S66 +/- datum).
Step 2 (definition of J under regulator r): J is REGULATOR-INDEPENDENT by NCG axiom (J is part
  of the spectral triple (A, H, D), not of the regulator f).
Step 3 (substitute): sig(r) = sign(⟨ε_H, J ε_H⟩) does NOT contain r explicitly.
  The regulator enters only through the measure on the spectrum (f(λ_k/Λ)), which is a POSITIVE
  weighting on a diagonal decomposition.
Step 4 (simplify): ⟨ε_H, J ε_H⟩_f = Σ_k f(λ_k/Λ) · ⟨ε_H, J ε_H⟩_k.
  Since f > 0 for all 5 regulators on the active spectrum, and since ε_H's J-projection is
  mode-wise concentrated on a block of definite sign (S66), the overall sign is determined by
  the block-sign, not by f.
Step 5 (direction): sign(⟨ε_H, J ε_H⟩_f) = sign(⟨ε_H, J ε_H⟩_k*) for the dominant k*.
  Conclusion: sig(r) is regulator-INDEPENDENT iff the block structure (S66 + AZ class BDI) is
  preserved. KO-dim=6 axiom guarantees it. FI-parity is a theorem candidate.
```

**PASS / FAIL implications for solution space**:
- **PASS**: Any mechanism proposing to "cancel" ε_H by choosing a regulator is STRUCTURALLY
  EXCLUDED — f > 0 preserves block-sign, so the wall is permanent. §VII-B entry closes 4 prior
  open proposals (one each per S66/S71/S72/S73a). Posterior reduces by tangible amount (mechanism
  exclusion is evidence per `.claude/rules/evoi-prioritization.md`).
- **FAIL**: Parity wall is NOT structural. A new free parameter (regulator choice) opens on the
  Higgs sector. This is a MAJOR structural finding and rewrites §VII-B from "wall" to "scan".

**Effort**: Low-medium. Reuses 5 existing npz files; net work is block-sign verification + registry-
landing prose. ~1 compute-day.

**Substrate framing**: ε_H is the *transverse fiber-embedding oscillation* (Higgs-as-|S|² mode).
Its J-parity is a structural datum of the Jensen-SU(3)×A_F spectral triple. The gate tests whether
the five regulators project to the same J-parity on this mode. Frame: FROM the spectral triple
parity → TOWARD the observed Higgs-sector sign-stability (no new CP violation from regulator).

---

## §W5-2. S85-W5-2-HP0-INTRA-CORRIDOR — HP^0 intra-corridor spectral-functional comparison

**Trigger**: `[VERIFY]` (first-time computation; baseline HP^0 pairing has no prior lizzi/connes
computation across the 5-regulator atlas).

**Classification**: GEOMETRIC (KK-HP^0 cohomology of the spectral triple, intra-corridor meaning
*within* the §VII.P disjoint-corridor).

**Agent type**: lizzi-spectral-functional-theorist (OWN). Cross-reference: W2 §W2 holds Connes'
disjoint-corridor items including three-way HP^3 extension; this W5 item is the HP^0 dual-question
in spectral-functional guise.

**Hypothesis**: HP^0(A_F) pairing with ε_H (intra-corridor, *within* the §VII.P surviving branch)
is REGULATOR-INDEPENDENT in magnitude up to a universal regulator multiplier M(f). Specifically:
`‖[ε_H] · ν‖_{HP^0, f} = M(f) · ‖[ε_H] · ν‖_{HP^0, zeta}` where M(f) is a scalar function of the
regulator, not of ν ∈ HP^0. If the M(f) scalar multiplier factorizes OUT of the pairing, HP^0 is
FI up to an overall regulator scale (Lizzi-observable pattern: intensive/extensive partition).

**Method**:
- Script: `computations/s85_w5_2_hp0_intra_corridor.py`.
- Data: `s85_w5_2_hp0_intra_corridor.npz`; plot: `s85_w5_2_hp0_intra_corridor.png`.
- Canonical constants: `from canonical_constants import M_KK, v_ew, Vol_SU3`.
- GPU/CPU: KK-HP^0 projection is computed on the finite A_F algebra (dim ≈ 30) — CPU path;
  `OMP_NUM_THREADS=8` cap.
- Build the A_F (finite-part) cycles, compute `[ε_H] ∈ KK(A_F, C)` (exists per S83 G5 Class-8),
  then pair with HP^0 basis elements.
- For each regulator r in the 5-regulator atlas, compute `‖[ε_H]‖_{HP^0, r}` and the pairing with
  a pre-fixed HP^0 basis (the Connes-Moscovici canonical generators, W2 item).
- Extract M(f) = ‖·‖_f / ‖·‖_zeta; test whether M(f) factorizes (is independent of basis element).

**Machinery pin (PRDR)**:
- `N_eval = 30` (A_F finite algebra dim).
- `L_max = 3` (canonical `a_n = zeta` truncation per S78 W3-L dictionary; all a_k snapshots at L=3).
- `scan_range = 5 regulators × 4 HP^0 basis elements = 20 computations`.
- `step_size = N/A`.
- `tolerance = RATIO; 5% multiplicative (Lizzi-observable class, per S78 W2-F Mellin multiplier
  scheme-invariance theorem; any drift > 5% between basis elements under the same regulator
  falsifies factorization)`.
- `scheme = 5-regulator atlas`.
- `convention = A_F basis per Connes-Chamseddine-Marcolli 2008`.
- `random_seed = N/A` (pairing is deterministic).
- `GPU path = CPU (dim 30 < 100)`.

**Input SHAs**:
- `canonical_constants.py` (pin at script start, full 64-hex).
- `tools/knowledge-index.json` (for HP^0 basis entries; `<computed-at-runtime>` if W0 HP^1
  item 16 has not landed).
- A_F-cycle npz from `computations/` (from S83 G4; `<static>`).

**Expected output 4-tuple**: `(value = M(f)-table, scheme = 5-regulator,
convention = CCM-2008-A_F-basis, L_max = 3)`.

**PASS / FAIL / INFO**:
- **PASS** if M(f) is basis-element-INDEPENDENT within 5% multiplicative tolerance for all 5
  regulators. HP^0 factorization theorem lands: `‖·‖_{HP^0, r} = M(r) · ‖·‖_{HP^0, zeta}`.
- **FAIL** if M(f) varies by > 5% between basis elements under the SAME regulator.
  Interpretation: HP^0 does NOT factor through the regulator; ε_H has basis-dependent regulator
  response. Major structural finding (closes factorization hope; opens basis-selection problem).
- **INFO** if 4/5 regulators factor but one (typically anomaly-derived, per S67) does not. Register
  that the anomaly-derived regulator lies structurally OUTSIDE the HP^0-factorizable family.

**Substitution chain [VERIFY]**:
```
Step 1 (definition): ‖[ε_H]‖_{HP^0, f} = |⟨[ε_H], ν⟩_f| for ν the HP^0 generator (Connes pairing).
Step 2 (definition of regulator entry): ⟨·, ·⟩_f = (residue at s=0 of Tr(f(D_K/Λ)^{-s} · ε_H · ν))
  per Connes-Moscovici residue formula.
Step 3 (substitute): the regulator f enters ONLY through the residue prefactor. If f is positive
  and smooth and admits a Mellin transform with simple pole at s=0 (true for zeta, Zubarev, SDW;
  cutoff_sqrt requires regularization; anomaly-derived is a distributional limit),
  then the residue is f_0 · (universal geometric residue).
Step 4 (simplify): ⟨[ε_H], ν⟩_f = f_0 · ⟨[ε_H], ν⟩_zeta, where f_0 = residue value.
Step 5 (direction): ‖·‖_f / ‖·‖_zeta = |f_0|, independent of ν. Factorization predicted IF the
  Mellin-multiplier theorem (S78 W2-F) extends to HP^0 (not yet proven; this gate IS the test).
  IF the test passes, HP^0 is a regulator-invariant cohomological datum (structural). IF it fails,
  HP^0 is regulator-DEPENDENT and ε_H has a hidden scheme-dependent phase.
```

**PASS / FAIL implications for solution space**:
- **PASS**: HP^0 joins HP^1 (S83 G5 ε_H-class) as a regulator-invariant cohomological anchor.
  Structural floor grows. Three permanent-registry §VII-B entries consolidate into one unified
  "Cohomology Parity Wall" theorem.
- **FAIL**: HP^0 is scheme-dependent. ε_H's HP^0 class is REGULATOR-DRESSED, undermining the
  disjoint-corridor theorem §VII.P proof hypothesis and re-opening 3 closed mechanisms (per
  S83 W3-G56 Godbillon-Vey primary-proxy discipline).

**Effort**: Medium. Requires A_F cycle library (exists in S83 artifacts) and 5 residue computations.
~2 compute-days.

**Substrate framing**: HP^0 is the ZEROTH cyclic-cohomology class — the "tracial" part of the
spectral triple. It measures the *spectral complexity* of the finite A_F sector (not the SU(3)
base). Frame: FROM the A_F spectral-moment structure → TOWARD the regulator-invariance of the
Higgs sector's cohomological address. Substrate claim: A_F HP^0 = a registry of intensive
(per-mode) partition invariants; if regulator-independent, the finite sector is "indexical."

---

## §W5-3. S85-W5-3-L0-L3-LAYER-DISSONANCE — L0/L3 layer-dissonance map update in §VII.M registry

**Trigger**: `[AUDIT]` (registry-maintenance gate; §VII.M already holds the L0/L1/L2/L3 three-layer
synthesis from S83; this gate updates the L0/L3-pair dissonance map with post-S84 data).

**Classification**: GEOMETRIC (the layer taxonomy is a regulator-side structural classification).

**Agent type**: lizzi-spectral-functional-theorist (OWN; solo-a registry landing per S83 three-layer
synthesis).

**Hypothesis**: The L0/L3-dissonance (layer-0 = non-interacting integer / layer-3 = per-observable
regulator, per S83) admits a closed-form *dissonance metric* `d(L0, L3, O)` for each observable O
in the §VII.K atlas. This gate computes d for the 42-row atlas and classifies each O by a dissonance
band: SMALL (d < 10%), MEDIUM (10% ≤ d < 30%), LARGE (d ≥ 30%). The prediction: SMALL-band
observables are L0-PASS, LARGE-band are L3-ONLY (cannot be L0-verified).

**Method**:
- Script: `computations/s85_w5_3_l0_l3_dissonance.py`.
- Data: `s85_w5_3_l0_l3_dissonance.npz`; plot: `s85_w5_3_l0_l3_dissonance.png` (42-row bar chart).
- Canonical constants: `from canonical_constants import *` (atlas loading requires ~12 constants).
- GPU/CPU: CPU-only (dim < 100); `OMP_NUM_THREADS=8`.
- For each of 42 atlas rows O:
  - `d(O) = |O(L0) − O(L3)| / max(|O(L0)|, |O(L3)|)` (normalized dissonance).
  - `L0(O) = zeta-axiom-native value` (S83 W1-G3 EN3 theorem).
  - `L3(O) = per-observable optimal regulator value` (from §VII.M registry row).
  - Band: SMALL < 10%, MEDIUM 10-30%, LARGE ≥ 30%.

**Machinery pin (PRDR)**:
- `N_eval = 42` (42-row §VII.K atlas).
- `L_max = 3` (canonical a_k truncation; matches S83 atlas).
- `scan_range = 42 observables × 2 layers = 84 queries`.
- `step_size = N/A`.
- `tolerance = RATIO; band thresholds 10%, 30% pre-registered`.
- `scheme = L0 (zeta) vs L3 (per-observable registry)`.
- `convention = S83 §VII.M three-layer registry as-of S84 close`.
- `random_seed = N/A`.
- `GPU path = CPU`.

**Input SHAs**:
- `sessions/framework/spectral-post-mortem.md` (L0/L3 registry source; `<computed-at-runtime>`).
- `tools/knowledge-index.json` (42-row atlas; `<computed-at-runtime>`).
- `computations/canonical_constants.py` (static hash).

**Expected output 4-tuple**: `(value = 42-band-histogram, scheme = L0/L3-pair,
convention = §VII.M-registry, L_max = 3)`.

**PASS / FAIL / INFO**:
- **PASS** if histogram shape matches S83 prediction: majority SMALL (≥ 26/42), MEDIUM 8-14/42,
  LARGE ≤ 5/42. §VII.M registry updates with dissonance band tags.
- **FAIL** if LARGE-band count > 8 (too much L0/L3 dissonance; structural-floor claim of §VII.M
  is weakened; three-layer synthesis requires reformulation).
- **INFO** if histogram has bimodal structure (e.g., 20 SMALL + 20 LARGE, 2 MEDIUM). Register a
  new observation pattern: "L0/L3 bimodal class" — suggests two sub-classes of observables with
  opposite layer-behavior.

**Substitution chain [AUDIT]**:
```
Step 1 (definition of d): d(O) = |O_L0 − O_L3| / max(|O_L0|, |O_L3|).
Step 2 (definition of O_L0): O_L0 = evaluate(O, regulator = zeta, scheme-axiom = L0).
Step 3 (definition of O_L3): O_L3 = evaluate(O, regulator = per-O-optimal, scheme-axiom = L3).
Step 4 (substitute for O = chi_2, concrete example):
  O_L0 = chi_2^{zeta} = 0.7400 (S78 W3-A BMA).
  O_L3 = chi_2^{SDW-per-observable} = 1.05 (S66 SDW value at per-obs optimum).
  d(chi_2) = |0.7400 − 1.05| / max(0.7400, 1.05) = 0.310 / 1.05 = 0.295 (MEDIUM, borderline).
Step 5 (direction): chi_2 sits at MEDIUM/LARGE boundary, consistent with S78's level-1 deadlock.
  Conclusion: for chi_2, L0/L3 dissonance is SUBSTANTIAL → chi_2 IS L3-only in principle.
  Repeat for 41 other observables; tabulate band distribution; compare to prediction.
```

**PASS / FAIL implications for solution space**:
- **PASS**: §VII.M three-layer synthesis is ROBUST; the layer-taxonomy predicts observable-class.
  New permanent theorem candidate: "L0/L3-band-indicator" for observable quality.
- **FAIL**: three-layer synthesis requires fourth layer OR reclassification; structural-floor
  claim weakened. Would re-open 3 closed §VII.M entries per S83.
- **INFO-bimodal**: reveals two-class observable structure, which is informative even if it
  doesn't confirm the S83 prediction.

**Effort**: Low. Atlas is existing; computation is 42 ratio evaluations. ~0.5 compute-day.

**Substrate framing**: L0 is the "non-interacting" (integer-coefficient) view of the spectrum;
L3 is the "per-observable" (regulator-dressed) view. Dissonance measures how much INTERACTION (i.e.,
regulator-physics) is needed to reach the observable. Frame: FROM the spectral-moment structure →
TOWARD the information content of regulator-dressing for each observable class.

---

## §W5-4. S85-W5-4-PARITY-LMAX-SANITY — L_max = 9 sensitivity test for parity wall (sanity check)

**Trigger**: `[VERIFY]` (sanity check on §W5-1's parity wall theorem; L_max sensitivity is the
most common failure mode in spectral computations — see S73b abs-extrap, where M_KK absorbs L_max
divergence but ε_H-class parity had not been tested at L_max ≠ 10).

**Classification**: GEOMETRIC (spectral-triple truncation test).

**Agent type**: lizzi-spectral-functional-theorist (OWN; sanity-check territory, paired with §W5-1).

**Hypothesis**: The FI-parity of §W5-1 (if PASS) is STABLE under L_max sweep in the window
{8, 9, 10}. Specifically, `sig(r, L_max = 9) == sig(r, L_max = 10)` for all 5 regulators.
The L_max = 9 test is an *odd* truncation (contrast with the canonical L_max = 10 even); if parity
is structural, odd/even L_max should agree. If odd/even differ, the parity is a truncation
artifact.

**Method**:
- Script: `computations/s85_w5_4_parity_lmax_sanity.py`.
- Data: `s85_w5_4_parity_lmax_sanity.npz`; plot: `s85_w5_4_parity_lmax_sanity.png`.
- Canonical constants: `from canonical_constants import L_max_canonical`.
- GPU/CPU: at L_max=8/9/10, spectrum dim = {~60k, ~104k, ~156k}; torch.linalg MANDATORY.
- For L ∈ {8, 9, 10}:
  - Build D_K at L_max = L.
  - For each of 5 regulators, compute `sig(r, L) = sign(⟨ε_H, J ε_H⟩)_f` at that L_max.
  - Tabulate 5 × 3 = 15 signs; verify columns (across L_max) are constant per-regulator.

**Machinery pin (PRDR)**:
- `N_eval` varies with L_max: {60k, 104k, 156k}; scripted.
- `L_max = {8, 9, 10}`; explicit sweep.
- `scan_range = 5 regulators × 3 L_max values = 15 computations`.
- `step_size = L_max step 1`.
- `tolerance = THEOREM` (exact sign; no slack).
- `scheme = 5-regulator atlas`.
- `convention = KO-dim=6 J canonical`.
- `random_seed = 42`.
- `GPU path = torch.linalg MANDATORY`.

**Input SHAs**:
- Same 5 S71-S73a npz files as §W5-1 (pinned).
- D_K at L=8 and L=9: `<computed-at-runtime>` (re-computed from canonical_constants at start).
- L=10 reuses S66 pre-computed spectrum (`<static>`).

**Expected output 4-tuple**: `(value = 5×3-sign-matrix-constant, scheme = 5-regulator,
convention = KO-dim=6-J, L_max = {8,9,10}-sweep)`.

**PASS / FAIL / INFO**:
- **PASS** if 5×3 matrix has constant columns (signs invariant across L_max in {8, 9, 10}) AND
  matches §W5-1's L_max=10 result. §W5-1 theorem is SANITY-VERIFIED.
- **FAIL** if any column flips sign as L_max varies. §W5-1 theorem is an L_max=10 artifact;
  the parity wall is downgraded to L_max-conditional, and §VII-B landing is blocked pending
  asymptotic L_max → ∞ extrapolation.
- **INFO** if L_max=8 differs from {9, 10} (pre-asymptotic effect) but {9, 10} agree. Register
  the pre-asymptotic threshold as the FI-parity validity floor.

**Substitution chain [VERIFY]**:
```
Step 1 (definition): sig(r, L) = sign(Σ_{k ≤ L} f(λ_k/Λ) · ⟨ε_H, J ε_H⟩_k).
Step 2 (L-sensitivity): partial sum convergence depends on whether ⟨ε_H, J ε_H⟩_k has a
  dominant block at k < 8 (below L=8 truncation) or extends to k ≥ 10.
Step 3 (substitute S73a data): dominant block is k ∈ [2, 6] per S73a SPECTRAL-ACTION-PROFILE-73a
  post-fold direction (already L_max < 8 concentrated).
Step 4 (simplify): since the dominant block is below L=8, sig(r, L=8) = sig(r, L=10).
Step 5 (direction): predicted PASS (constant columns). If FAIL, it means ε_H's J-pairing has
  significant L ≥ 9 tail contribution, contradicting S73a's post-fold-concentration finding.
  Would be a major structural surprise and require re-evaluation of S73a.
```

**PASS / FAIL implications for solution space**:
- **PASS**: §W5-1 theorem is robust. Parity wall lands permanently.
- **FAIL**: §W5-1 theorem is NOT robust; truncation-dependence. Two mechanisms re-open.
- **INFO**: pre-asymptotic floor is characterized; we learn a structural threshold.

**Effort**: Medium. L=9 spectrum is new; L=8 may exist in S73b. ~1.5 compute-days.

**Substrate framing**: L_max is the spectral-truncation budget — how many internal-fiber modes
the computation retains. Parity under J should not depend on truncation (the J-action is
mode-local, not global). Frame: FROM the fiber eigenvalue spectrum → TOWARD a truncation-robust
physical conclusion about Higgs-sector CP structure.

---

## §W5-5. S85-W5-5-LAYER-AWARE-LATTICE-JOIN — Layer-aware lattice-join functoriality test

**Trigger**: `[VERIFY]` (follow-up from W10-116 / S84, which introduced a layer-aware lattice
structure on the regulator poset; this gate tests functoriality — does the join operation
commute with the layer-projection?).

**Classification**: GEOMETRIC (categorical / lattice-theoretic test on regulator poset).

**Agent type**: lizzi-spectral-functional-theorist (OWN). Cross-reference: W11 vdd wave holds
"Formal categorical unification of parity-exclusion and rank-exclusion" which this item extends.

**Hypothesis**: The layer-aware lattice on the regulator poset (with L0 = top, L3 = bottom, joins
and meets per W10-116 construction) satisfies FUNCTORIALITY: `Π_L(r1 ∨ r2) = Π_L(r1) ∨ Π_L(r2)`,
where Π_L is the layer-projection and ∨ is the join in the regulator lattice. If functorial, the
lattice-join is a categorical operation (preserves layer structure); if not, joins mix layers and
the §VII.M three-layer synthesis needs a lattice-theoretic refinement.

**Method**:
- Script: `computations/s85_w5_5_layer_aware_join.py`.
- Data: `s85_w5_5_layer_aware_join.npz`; plot: `s85_w5_5_layer_aware_join.png` (lattice diagram
  with functoriality-violation edges flagged).
- Canonical constants: `from canonical_constants import *` (minimal — mostly categorical ops).
- GPU/CPU: CPU-only; lattice has < 30 elements.
- Enumerate regulator lattice: 5 base regulators + 10 pairwise joins + 10 pairwise meets = 25 elts.
- For each pair (r1, r2), compute:
  - LHS: `Π_L(r1 ∨ r2)` (join first, then project to layer L).
  - RHS: `Π_L(r1) ∨ Π_L(r2)` (project first, then join).
  - Compare for L ∈ {L0, L1, L2, L3}.
- Count violations: pair (r1, r2, L) where LHS ≠ RHS.

**Machinery pin (PRDR)**:
- `N_eval = 25` (lattice element count).
- `L_max = 3` (a_k truncation canonical).
- `scan_range = 10 pairs × 4 layers = 40 functoriality checks`.
- `step_size = N/A` (discrete).
- `tolerance = THEOREM` (categorical equality; any violation counts).
- `scheme = layer-aware lattice per W10-116 construction`.
- `convention = join ≡ supremum in regulator partial order; layer-projection per S83`.
- `random_seed = N/A`.
- `GPU path = CPU`.

**Input SHAs**:
- W10-116 artifact (lattice construction); `<computed-at-runtime>` if W10-116 landed; else
  reconstruct locally from the S83 three-layer synthesis.
- `canonical_constants.py` (static).

**Expected output 4-tuple**: `(value = functoriality-violation-count, scheme = layer-aware-lattice,
convention = W10-116, L_max = 3)`.

**PASS / FAIL / INFO**:
- **PASS** if violation-count = 0. Lattice-join is functorial; categorical-unification (W11 vdd)
  has a rigorous lattice backend.
- **FAIL** if violation-count ≥ 1 AND the violation is STRUCTURAL (not a numerical/definition
  artifact). Three-layer synthesis needs a refined fourth layer OR a non-functorial join operation.
- **INFO** if violation-count ≥ 1 but all violations involve L2 (known semi-structured layer,
  per S83). Register that L2 is the non-functorial "fringe."

**Substitution chain [VERIFY]**:
```
Step 1 (definition): Π_L is the layer-assignment map; ∨ is the regulator poset join.
Step 2 (functoriality is a CATEGORICAL claim): Π_L(r1 ∨ r2) =? Π_L(r1) ∨ Π_L(r2).
Step 3 (substitute, example): r1 = zeta (L0), r2 = SDW (L3).
  LHS: r1 ∨ r2 in regulator poset = coarsest common refinement = "zeta∨SDW" (a dressed zeta).
  Π_L(zeta∨SDW) = ? (depends on construction of join; W10-116 must specify).
  RHS: Π_L(zeta) ∨ Π_L(SDW) = L0 ∨ L3 = L0 (if layer poset has L0 top) or L3 (if L3 top).
Step 4 (simplify): requires explicit W10-116 join construction. Functoriality fails if W10-116's
  join is defined by INTERSECTION of per-layer projections (RHS) but the underlying physical join
  operates at the LAYER-MIXED level (LHS). This is the test.
Step 5 (direction): no pre-computed answer. Gate IS the test.
```

**PASS / FAIL implications for solution space**:
- **PASS**: Layer-aware lattice is a CATEGORICAL object. Categorical-unification (W11 §W11-3)
  can cite lattice-functoriality as a rigorous backend. One new permanent theorem.
- **FAIL**: layer-lattice has non-trivial categorical structure — it is not a Boolean algebra but
  rather a weighted or non-commutative lattice. Requires deeper categorification.

**Effort**: Medium. Depends on W10-116 availability. ~1-2 compute-days. If W10-116 not landed,
gate falls to PRE-REG-INCOMPLETE.

**Substrate framing**: The regulator lattice is a structure on the *choice-space of physical DOFs
in the spectral action*. Joins correspond to "coarser" regulators (less information). Functoriality
says: losing information commutes with layer-assignment. Frame: FROM the spectral-functional
choice space → TOWARD a categorical statement about the information flow between layers.

---

## §W5-6. S85-W5-6-REGULATOR-SCAN-EPS-H — Regulator-scan of ‖[ε_H]‖_{HP^1} magnitude under 5-regulator atlas

**Trigger**: `[VERIFY]` (first-time regulator-scan of ε_H HP^1 magnitude; §W5-1 tests parity
(sign), this gate tests magnitude).

**Classification**: GEOMETRIC (KK-HP^1 magnitude of ε_H under regulator variation).

**Agent type**: lizzi-spectral-functional-theorist (OWN; solo magnitude scan complements my §W5-1
parity scan).

**Hypothesis**: While sign(‖[ε_H]‖_{HP^1}) is FI (§W5-1 theorem candidate), the MAGNITUDE is
SCHEME-DEPENDENT. The magnitude-variance is a physical DOF measure for ε_H, not a signal of
framework failure. Specifically: `max(‖·‖) / min(‖·‖) ∈ [2, 100]` across 5 regulators, analogous
to S66's eps_H 381× dynamic range on the raw observable but reduced by the HP^1 normalization.
A range ≤ 10 suggests HP^1 normalization WORKS; a range ≥ 30 suggests it does NOT.

**Method**:
- Script: `computations/s85_w5_6_eps_h_hp1_scan.py`.
- Data: `s85_w5_6_eps_h_hp1_scan.npz`; plot: `s85_w5_6_eps_h_hp1_scan.png` (5-bar + error).
- Canonical constants: `from canonical_constants import M_KK, v_ew, Vol_SU3`.
- GPU/CPU: HP^1 pairing with KK-class requires a Dixmier-trace-like computation on full L_max=10
  spectrum (dim = 155,984); torch.linalg MANDATORY.
- For each regulator r in 5-atlas:
  - Compute `‖[ε_H]‖_{HP^1, r} = residue at s=0 of Tr(f_r(D/Λ) · ε_H^{2})` per Connes-Moscovici.
- Tabulate 5 values; compute max/min ratio.

**Machinery pin (PRDR)**:
- `N_eval = 155984` (full L_max=10 spectrum).
- `L_max = 10`.
- `scan_range = 5 regulators`.
- `step_size = N/A`.
- `tolerance = RATIO; pre-registered bands: range ≤ 10 "tight" / 10 < range ≤ 30 "acceptable" /
  range > 30 "wide" (matches observational-style band registration)`.
- `scheme = 5-regulator`.
- `convention = Connes-Moscovici residue; per S83 G56`.
- `random_seed = 42`.
- `GPU path = torch.linalg MANDATORY`.

**Input SHAs**:
- Same 5 S71-S73a npz files as §W5-1 (pinned).
- S83 G56 Godbillon-Vey artifact (for residue methodology); `<computed-at-runtime>` or
  pre-pinned hash if landed.

**Expected output 4-tuple**: `(value = max/min-ratio, scheme = 5-regulator,
convention = CM-residue, L_max = 10)`.

**PASS / FAIL / INFO** (observational-style band registration; no arbitrary gate):
- **INFO (tight)** if max/min ≤ 10. HP^1 normalization significantly reduces the raw S66 381×
  dynamic range. ε_H is a "near-FI" observable.
- **INFO (acceptable)** if 10 < max/min ≤ 30. HP^1 normalization partially reduces the range;
  consistent with expectation from Lizzi-observable theory.
- **INFO (wide)** if max/min > 30. HP^1 normalization does NOT reduce the range. ε_H magnitude
  is PERMANENTLY scheme-dependent; structural claim: magnitude of ε_H is NEVER observable.
- (No FAIL: this gate is observational-registration, per `feedback_arbitrary-gates.md`.)

**Substitution chain [VERIFY]**:
```
Step 1 (definition): ‖[ε_H]‖_{HP^1, r} = Res_{s=0} ζ_{D, ε_H^2, r}(s), the regulated spectral
  residue at s=0 of the zeta-function weighted by ε_H^2.
Step 2 (substitute regulator): for r = zeta, coefficient is 1 (canonical); for r = SDW, Zubarev,
  cutoff_sqrt, anomaly-derived, the coefficient is the Mellin-multiplier M_r (pre-computed in
  S78 W2-F).
Step 3 (simplify): ‖·‖_r = |M_r| · ‖·‖_zeta. Range = max|M_r| / min|M_r|.
Step 4 (plug in): from S78 W2-F, |M_{zeta}| = 1, |M_{SDW}| ≈ 0.97, |M_{cutoff_sqrt}| ≈ 0.87
  (pre-S85 estimates; refine in this gate). Zubarev and anomaly-derived: to be computed.
Step 5 (direction): if all |M_r| lie in [0.8, 1.2], range ≤ 1.5 (tight). If Zubarev |M| = 10,
  range expands. Predict: tight band likely, based on S78 Mellin-multiplier theorem.
```

**PASS / FAIL implications for solution space**:
- **INFO (tight)**: ε_H magnitude is a physical observable (up to small scheme correction).
- **INFO (wide)**: ε_H magnitude is intrinsically scheme-bound; Only its SIGN is physical.
  (Reinforces §W5-1.) Permanent boundary of observability.

**Effort**: Medium. 5 residues at L_max=10. ~1.5 compute-days.

**Substrate framing**: HP^1 magnitude is the *observational weight* of ε_H as a cohomological
class. The range across regulators measures how much of the magnitude is "physical" vs
"scheme-embedded." Frame: FROM the HP^1 cohomology → TOWARD the observable Higgs-transverse-mode
amplitude.

---

## §W5-7. S85-W5-7-TWO-LAYER-OBSTRUCTION — W10-114 + W6-67 joint theorem: "two-layer obstruction"

**Trigger**: `[VERIFY-THEOREM]` (joint theorem landing from two S84 precursors: W10-114 and W6-67).

**Classification**: GEOMETRIC (structural obstruction theorem).

**Agent type**: lizzi-spectral-functional-theorist (OWN; this item pairs my regulator-scan expertise
with the W10-114 layer-interface and W6-67 2-loop Z_R results to produce a joint theorem statement).

**Hypothesis**: The S84 W10-114 r_max layer-interface theorem (separating L1/L2/L3 at a scale r_max)
and the S84 W6-67 2-loop Z_R investigation (showing f_conv scheme-dependence at 2-loop order)
jointly imply a TWO-LAYER OBSTRUCTION THEOREM: *no single-regulator scheme can make both f_conv
scheme-independent and ε_H magnitude regulator-independent across the L1/L2 interface*. This is
a no-go / frustration theorem analogous to S67 FUNCTIONAL-SELECT-67.

**Method**:
- Script: `computations/s85_w5_7_two_layer_obstruction.py`.
- Data: `s85_w5_7_two_layer_obstruction.npz`; plot: `s85_w5_7_two_layer_obstruction.png`.
- Canonical constants: `from canonical_constants import *`.
- GPU/CPU: CPU-only (theorem-level computation with 5 regulators × 2 observables = 10 tabulated
  values, from prior artifacts).
- Structure:
  1. Load W10-114 r_max interface data.
  2. Load W6-67 2-loop Z_R scheme-dependence table.
  3. Load §W5-6 ‖ε_H‖_{HP^1} scan (if completed; else pin at `<computed-at-runtime>` and run
     §W5-6 first).
  4. Construct the 5-regulator × 2-observable (f_conv, ε_H) matrix.
  5. Test: does any row (regulator) jointly satisfy both "scheme-indep f_conv" AND
     "scheme-indep ε_H magnitude"? If the answer is NO for all 5 regulators, the obstruction
     theorem is established.

**Machinery pin (PRDR)**:
- `N_eval = 10` (5 regulators × 2 observables).
- `L_max = 10` (from §W5-6); `L_max = 3` for cohomological computations.
- `scan_range = 5 × 2 = 10 matrix entries`.
- `step_size = N/A`.
- `tolerance = THEOREM` (categorical; no row satisfies both = PASS).
- `scheme = 5-regulator atlas`.
- `convention = "scheme-indep" defined as drift ≤ 5% across the 5-atlas (Lizzi-observable
  threshold, S78 W2-F)`.
- `random_seed = N/A`.
- `GPU path = CPU (small matrix)`.

**Input SHAs**:
- W10-114 (layer-interface) npz from S84: `<static>`.
- W6-67 (2-loop Z_R) npz from S84: `<static>`.
- §W5-6 npz: `<computed-at-runtime>` (depends on W5-6 completion).
- canonical_constants: static.

**Expected output 4-tuple**: `(value = obstruction-theorem-verified, scheme = 5-regulator,
convention = 5%-scheme-indep-def, L_max = 10)`.

**PASS / FAIL / INFO**:
- **PASS** if no row satisfies both conditions. Joint theorem lands as permanent §VII-B entry
  "Two-Layer Obstruction," analogous to S67 "Frustration Triangle."
- **FAIL** if AT LEAST ONE row satisfies both. No obstruction exists; the spectral-functional
  DOF is smaller than predicted by L1/L2 interface. Favorable structural result but not the
  hypothesized one.
- **INFO** if 4 rows fail both conditions and 1 row marginally satisfies both (drift ≤ 7%, not
  ≤ 5%). Register an "Obstruction with Fringe" class.

**Substitution chain [VERIFY-THEOREM]**:
```
Step 1 (definitions):
  f_conv^r = S84 W6-67 value of f_conv under regulator r at 2-loop.
  ε_H^r = S85 W5-6 value of ‖[ε_H]‖_{HP^1, r}.
  SCHEME_INDEP(X) = (max_r X - min_r X) / |mean_r X| ≤ 5%.
Step 2 (theorem candidate): for all r: NOT(SCHEME_INDEP(f_conv^r) AND SCHEME_INDEP(ε_H^r)).
Step 3 (substitute): from W6-67, f_conv 2-loop drift is ≈ 8-15% across regulators (pre-S85
  estimate). So NOT SCHEME_INDEP(f_conv) for all r. HENCE the AND is false for all r, trivially.
Step 4 (simplify): theorem is proven if W6-67's drift > 5%. If W6-67's drift < 5%, must examine
  per-regulator ε_H.
Step 5 (direction): PASS predicted if W6-67's 2-loop drift > 5% (very likely per S78 evidence).
  Joint obstruction will be established as a consequence of W6-67's scheme-dependence.
```

**PASS / FAIL implications for solution space**:
- **PASS**: permanent §VII-B theorem; mirrors S67 frustration-triangle. Adds one wall to
  solution-space map. Closes proposals seeking to eliminate spectral-functional DOF via 2-loop
  regulator choice.
- **FAIL**: spectral-functional DOF collapses at 2-loop; major favorable finding. Re-opens
  proposals assuming universal 2-loop regulator.

**Effort**: Low (given §W5-6 and W10-114/W6-67 artifacts). ~0.5 compute-day.

**Substrate framing**: The obstruction is a NO-GO for regulator-unification at 2-loop. Frame:
FROM the 2-loop spectral-action loop corrections → TOWARD a permanent wall saying no single
regulator can control both the CC-channel (f_conv) and the Higgs-fiber channel (ε_H)
simultaneously. The substrate has a genuine two-channel DOF at this layer.

---

## Wave W5 → Wave W6 Decision Point

W5 does not dispatch to W6 (sp-origin, Schwarzschild-Penrose). W5 is a reviewer-origin breadth
wave producing:
- 3 registry-landing artifacts (§W5-1, §W5-3, §W5-7): permanent results for the solution-space
  map in §VII-B and §VII.M.
- 2 HP-cohomology computations (§W5-2, §W5-6): new numerical data on the regulator-invariance of
  the cohomological address of ε_H.
- 1 sanity check (§W5-4): truncation-robustness test on §W5-1.
- 1 categorical functoriality test (§W5-5): backends the lattice structure of the regulator poset.

Downstream consumers (W6 and beyond) may cite:
- §W5-1 ε_H parity wall when classifying conformal-infinity regulator-conditional Penrose
  diagrams (W6 §W6-3 CONFORMAL-INFINITY-BIFURCATION).
- §W5-7 two-layer obstruction in any Petrov-dependence-on-non-block-diagonal-perturbations
  analysis (W6 §W6-7), since the obstruction constrains what perturbations preserve the layer
  structure.

No cross-wave writes: W5 landing artifacts go to `sessions/archive/session-85/` per §W5-N, the
verdict file at `computations/s85_gate_verdicts.txt`, and the §VII-B/§VII.M registry updates
flow through the post-session `/weave --update` pipeline.

---

## Wave W5 Machinery-Enumeration Pin

Per PRDR discipline (`.claude/rules/epistemic-discipline.md` §Pre-Registration Completeness),
every gate block above pins the following machinery parameters:

| Parameter | Pin | Source |
|:----------|:----|:-------|
| `N_eval` | per-gate (30 / 42 / 155984 / varies) | §W5-N block |
| `L_max` | per-gate ({3, 8-10, 10}) | §W5-N block |
| `scan_range` | per-gate | §W5-N block |
| `step_size` | per-gate (N/A or discrete) | §W5-N block |
| `tolerance` | THEOREM / RATIO (5-10%) | §W5-N block |
| `scheme` | 5-regulator atlas (all gates) | Wave W5 Summary |
| `convention` | per-gate (KO-dim=6 / CCM-2008 / 5%-scheme-indep / §VII.M-registry) | §W5-N block |
| `random_seed` | 42 (documentation only; computations deterministic) | Wave W5 Summary |
| `GPU path` | MANDATORY torch.linalg for dim ≥ 100×100 gates (§W5-1, §W5-4, §W5-6) | Wave W5 Summary |

**PRU Class-8 audit**: each gate block declares every gate-relevant machinery parameter. No gate
block leaves a parameter as `<unpinned>` or `<TBD>`. Cross-gate dependencies (§W5-7 depends on
§W5-6; §W5-4 is sanity for §W5-1) are noted explicitly in the per-gate "Input SHAs" and "Effort"
fields. No PRU-vulnerability detected in W5 plan at time of write.

---

## Wave W5 Input-SHA Ledger

Static inputs (pre-computed SHA-256 pinned at script start, full 64-hex):

| Input | Source | Status at W5-dispatch |
|:------|:-------|:----------------------|
| `canonical_constants.py` | `computations/canonical_constants.py` | `<static>` |
| S71 CORRELATED-SENSITIVITY-71 data | `s71_correlated_sensitivity.npz` | `<static>` |
| S72 GILKEY-REEVAL-72 data | `s72_gilkey_reeval.npz` | `<static>` |
| S72 SPECTRAL-FUNCTIONAL-FIT-72 data | `s72_spectral_functional_fit.npz` | `<static>` |
| S73a SPECTRAL-ACTION-PROFILE-73a data | `s73a_spectral_action_profile.npz` | `<static>` |
| S66 eps_H sign-flip data | `s66_zeta_sa.npz` | `<static>` |
| S78 W2-F Mellin-multiplier table | `s78_w2f_a4_r2_fstar.npz` | `<static>` |
| S83 G56 Godbillon-Vey artifact | `s83_w3_g56_godbillon_vey.npz` | `<static>` |
| S83 G5 ε_H-class HP-decomposition | `s83_w1_g5_four_axis.npz` | `<static>` |
| §VII.K 42-row atlas | `tools/knowledge-index.json` (JSON-extracted) | `<computed-at-runtime>` |

Runtime-computed inputs (pinned at script execution by `closure_hash` per
`.claude/templates/script-template.py`):

| Input | Produced by | Consumer gate |
|:------|:------------|:--------------|
| §W5-6 `eps_h_hp1_scan.npz` | §W5-6 | §W5-7 |
| W0 CC-1 η-invariant (if landed) | W0 | §W5-6 (optional reuse) |
| W0 CC-3 residue-sum (if landed) | W0 | §W5-3 (optional reuse) |
| W0 CC-5 L_max≥11 refit (if landed) | W0 | §W5-5 (optional reuse) |
| W10-116 layer-lattice (if landed) | S84 W10 or fallback | §W5-5 |
| W10-114 r_max interface (from S84) | S84 W10 | §W5-7 |
| W6-67 2-loop Z_R (from S84) | S84 W6 | §W5-7 |

Each producing script MUST emit the SHA-256 of each input file in the first 20 lines of stdout
and emit the closure SHA as the final line before the verdict. The verdict line in
`computations/s85_gate_verdicts.txt` carries the full 64-character closure SHA (per
`.claude/rules/gate-verdicts.md`).

---

**End of Wave W5 Plan.**
