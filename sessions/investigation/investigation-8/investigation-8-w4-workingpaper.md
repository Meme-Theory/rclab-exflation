# Investigation 8 Wave 4 — Cross-Vantage Adjudications (Results Working Paper)

**Investigation**: 8 | **Wave**: 4 | **Plan**: investigation-8-plan-w4.md | **Theme**: the cluster's two genuine math/physics adjudication workshops — what the GGE IS (Bell vs hidden-variable) and the sign-or-null of isotropic cosmic birefringence β. Both gates are `gate_type: workshop`; per `.claude/rules/gate-verdicts.md §"Investigation-Track Canonical Path"` neither emits a verdict line — both close by **artifact-existence-with-content** of the workshop md (== `wave-classification.md §M1`).

## Gate Sections

### §W4-1. INV8-W4-1 (einstein-theorist ↔ kitaev-quantum-chaos-theorist)

**Status**: NOT STARTED
**Gate ID**: `INV8-W4-1`
**Gate type**: `workshop` (EXACTLY 2 agents, 2 rounds; NO verdict line — closes by artifact-existence-with-content per `wave-classification.md §M1` + `gate-verdicts.md §"Investigation-Track Canonical Path"`)
**Trigger**: `[VERIFY-THEOREM]` (structural-verdict adjudication, not a numeric gate)
**Classification**: **PHONONIC** (the GGE IS a substrate excitation spectrum — 8 Richardson-Gaudin quasiparticle-pair modes)
**Participants**: `einstein-theorist` (Reading A — principle-theory completeness / M2 thermodynamic⊥entanglement split) ↔ `kitaev-quantum-chaos-theorist` (Reading B — S70 Bell-PASS author / integrability⊥chaos split)
**Spec author**: `gen-physicist` (NEUTRAL; not a participant — einstein owns W2 and kitaev authored the S70 Bell-PASS, which is precisely why a neutral planner writes the spec)
**Hypothesis (scope line)**: the GGE may cleave into a classical thermodynamic layer (would-be hidden variable) and an irreducibly-quantum entanglement layer — adjudicating the S58 superdeterminism reading against the S70 CHSH-violation result via the framework's own M2 algebra-axis orthogonality, rather than treating the two priors as a flat contradiction.

**Plan reference**: `sessions/investigation/investigation-8/investigation-8-plan-w4.md` §W4-1 (workshop block: agents, rounds, sources, adjudication_question, context, substrate_framing).

**Adjudication tension** (the competing first-principles readings the workshop resolves):
- *Reading A (einstein)* — the S58 substrate-measurement addendum §II reads the GGE as a hidden-variable / superdeterministic account ("QM is the low-energy effective theory of a deterministic substrate"), but the S70 BELL-GGE-70 result shows the GGE pairs violate CHSH across 8/8 modes (S up to 2.452 > 2). By Bell's theorem that is not a local-hidden-variable account, so the S58 reading is false AS STATED. einstein's proposed resolution is the M2 split: the GGE's algebra-INVARIANT thermodynamic content (8 mode-effective temperatures {T_k = ω_k/β_k}, D_JS = 0.024 from Gibbs) is the would-be hidden layer; the algebra-DEPENDENT inter-mode CHSH-violating entanglement is irreducibly quantum — a non-local quantum theory whose non-locality is geometric (one fabric), not a deterministic one with QM bolted on.
- *Reading B (kitaev)* — the GGE IS quantum; the Horodecki two-qubit CHSH treatment of S70 supersedes the S69 bosonic-homodyne FAIL, and the 8/8-mode violation is the operative result. The classical/quantum partition is not temperature-vs-entanglement but an integrability-vs-chaos split of the mode algebra (bounded-Krylov → permanent / the Leggett channel; linear-Krylov → thermalize), with the substrate's λ_L = 0 integrability (S104) as the structural backdrop.

**Closure type**: ARTIFACT-EXISTENCE-WITH-CONTENT — the deliverable workshop md is the closure object; this gate has no numeric threshold and emits no verdict-file line (workshop gate per `gate-verdicts.md §"Investigation-Track Canonical Path"`).

**Output Artifacts** (artifact-existence closure checklist; mirrors the gate-block `output_artifacts:` YAML — workshop closure per `wave-classification.md §M1`, NOT a verdict-line emission):
*(pending — confirm the workshop deliverable exists (`ls "sessions/investigation/investigation-8/workshops/inv8-w4-1-bell-vs-hidden-variable.md"`) AND paste `grep -E '<pattern>' <path>` output for EACH must_contain pattern below. An entry with file missing OR any must_contain regex returning empty means the gate did not properly close — orchestrator MUST then SendMessage continuation to the same workshop agentId per `feedback_dispatch-discipline.md`. Verification is purely by content presence (regex match), NEVER by line/byte counts, per `feedback_max-effort-full-fidelity.md`.)*
- Deliverable: `sessions/investigation/investigation-8/workshops/inv8-w4-1-bell-vs-hidden-variable.md`
- `must_contain`:
  - `## Wrap-Up`
  - `Effected In-Session`
  - `Carry-Forward Computations`

**Results**:
*(pending — include: the 2 named participants [einstein-theorist ↔ kitaev-quantum-chaos-theorist]; the 2-round structure [R1 steelman own reading / R2 rebut opponent + converge on the structural verdict]; the adjudication question [what does the GGE IS — which substrate quantities are classical/thermodynamic vs irreducibly-quantum]; the three sub-questions answered — (a) does the S70 Bell-violation FALSIFY the S58 superdeterminism reading or reconcile via the M2 algebra-INVARIANT⊥algebra-DEPENDENT split, with each substrate quantity placed on its side and whether the M2 temperature/entanglement partition (einstein) coincides with the integrability/chaos partition (kitaev); (b) IF a classical layer is isolated, is the Born rule derivable FOR that layer (Gleason + GGE coarse-graining, cross-ref INV8-W2-3) and an INPUT for the entanglement layer, or an input for both; (c) does the resolution redirect the S58 quantum-foundations program (superdeterminism → geometric-non-locality) or leave it intact with a scoping caveat; the STRUCTURAL VERDICT — a named classical/quantum decomposition or a named obstruction to one, each substrate quantity placed by a first-principles argument (M2 orthogonality / Bell's theorem / Krylov-complexity integrability), with any directional claim the workshop derives carrying its own substitution chain per `math-scripts.md §"Double-Check Logic Before Compute"`; the `## Wrap-Up` block with `Effected In-Session` + `Carry-Forward Computations`.)*

---

### §W4-2. INV8-W4-2 (mack-cosmic-bridge ↔ connes-ncg-theorist)

**Status**: NOT STARTED
**Gate ID**: `INV8-W4-2`
**Gate type**: `workshop` (EXACTLY 2 agents, 2 rounds; NO verdict line — closes by artifact-existence-with-content per `wave-classification.md §M1` + `gate-verdicts.md §"Investigation-Track Canonical Path"`)
**Trigger**: `[VERIFY-THEOREM]` (structural-verdict adjudication on a sign/null, not a numeric gate)
**Classification**: **GEOMETRIC** (the question is whether the substrate's spectral/parity geometry — [J,D_K], γ9-grading — forbids an isotropic parity-odd term; a property of the fabric, not of an excitation)
**Participants**: `mack-cosmic-bridge` (Reading A — observational cosmology / effacement-residual parity-odd Chern-Simons coupling, β ≠ 0) ↔ `connes-ncg-theorist` (Reading B — NCG parity sector / CPT-exact + γ9-traceless, β = 0 null)
**Spec author**: `gen-physicist` (NEUTRAL; not a participant — mack owns W1 and connes owns the NCG parity sector, which is precisely why a neutral planner writes the spec)
**Hypothesis (scope line)**: isotropic cosmic birefringence β is either nonzero (the effacement-residual a₀ dark-energy condensate carries a parity-odd Chern-Simons coupling that evades γ9-tracelessness) or exactly zero (the CPT-exact, γ9-traceless substrate spectrum forbids an isotropic parity-odd term) — the structural verdict decides which, on the crux of the residual's γ9-grading, and whether the prediction is LiteBIRD-decisive.

**Plan reference**: `sessions/investigation/investigation-8/investigation-8-plan-w4.md` §W4-2 (workshop block: agents, rounds, sources, adjudication_question, context, substrate_framing).

**Adjudication tension** (the competing first-principles readings the workshop resolves):
- *Reading A (mack)* — the effacement residual (Γ_eff = 0.99970; the 3e-4 leakage that IS the dark-energy component, a slowly-evolving a₀ condensate with w₀ = −0.918) is a dynamical pseudo-scalar-like field; a slowly-evolving DE field coupling parity-oddly to the gauge sector (a Chern-Simons / φ F∧F term) produces ISOTROPIC β ≠ 0. Predict β from the residual's evolution and place it against Minami-Komatsu 0.342° ± 0.094° — a parity observable ORTHOGONAL to the tilt observables (n_s, α_s) and the a₀-DE EoS, breaking that degeneracy with one near-term measurement.
- *Reading B (connes)* — the substrate spectrum is CPT-EXACT ([J,D_K] = 0, PROVEN at all τ; J = C_2·K; forces η_B = 0, ε_1 = 0 EXACT) and the spectral action is γ9-TRACELESS (the W17 even-Seeley-DeWitt parity-blindness wall; canonical (η=0, GV≠0) signature on the (C_H, C_εH) parity-twin pair). An isotropic parity-odd Chern-Simons term is an odd-grading object; CPT-exactness + γ9-tracelessness FORBID it → β = 0, a NULL that is itself a falsifier if Minami-Komatsu firms up.

**Closure type**: ARTIFACT-EXISTENCE-WITH-CONTENT — the deliverable workshop md is the closure object; this gate has no numeric threshold and emits no verdict-file line (workshop gate per `gate-verdicts.md §"Investigation-Track Canonical Path"`).

**Output Artifacts** (artifact-existence closure checklist; mirrors the gate-block `output_artifacts:` YAML — workshop closure per `wave-classification.md §M1`, NOT a verdict-line emission):
*(pending — confirm the workshop deliverable exists (`ls "sessions/investigation/investigation-8/workshops/inv8-w4-2-cosmic-birefringence.md"`) AND paste `grep -E '<pattern>' <path>` output for EACH must_contain pattern below. An entry with file missing OR any must_contain regex returning empty means the gate did not properly close — orchestrator MUST then SendMessage continuation to the same workshop agentId per `feedback_dispatch-discipline.md`. Verification is purely by content presence (regex match), NEVER by line/byte counts, per `feedback_max-effort-full-fidelity.md`.)*
- Deliverable: `sessions/investigation/investigation-8/workshops/inv8-w4-2-cosmic-birefringence.md`
- `must_contain`:
  - `## Wrap-Up`
  - `Effected In-Session`
  - `Carry-Forward Computations`

**Results**:
*(pending — include: the 2 named participants [mack-cosmic-bridge ↔ connes-ncg-theorist]; the 2-round structure [R1 steelman own reading / R2 rebut opponent + converge on the structural verdict]; the adjudication question [does the effacement-residual a₀ DE component EVADE the substrate's γ9-tracelessness (β ≠ 0) or is it BOUND by it (β = 0, a null)]; the three sub-questions answered — (a) the crux: is the effacement residual on the γ9-ODD or γ9-EVEN grading (the register carries BOTH the "a₀ Seeley-DeWitt zeroth moment" even-grading framing AND the "impedance-effacement leakage at a₂" framing), and whether the parity-odd Chern-Simons coupling can live there; (b) what β (a number, in degrees) — or what exact NULL (β = 0 with its γ9-tracelessness / CPT structural reason) — the substrate's spectral geometry predicts, with provenance; (c) is the prediction LiteBIRD-decisive — place the predicted β (or null) against Minami-Komatsu 0.342° ± 0.094° (current ~3.6σ) and the LiteBIRD ~0.01° sensitivity, stating distinguishability from ΛCDM (β = 0); the STRUCTURAL VERDICT — the derived sign-or-null of β with its structural reason (β ≠ 0 with magnitude + effacement-residual γ9-odd provenance, OR β = 0 with the γ9-tracelessness / CPT argument forcing it), the β sign/null claim carrying its own substitution chain per `math-scripts.md §"Double-Check Logic Before Compute"`; the `## Wrap-Up` block with `Effected In-Session` + `Carry-Forward Computations`.)*

---

## Wave 4 Synthesis (team-lead)

Wave 4 closed 2/2 by artifact-existence (no verdict lines — investigation-track workshops). Both adversarial adjudications converged on DERIVED structural verdicts with genuine concessions, not agreement-counting.

- **INV8-W4-1 (Bell-vs-hidden-variable) → the GGE Orthogonal 2×2 Stratification** (a named decomposition). ρ_GGE = (M2 algebra-axis column: algebra-INVARIANT classical-shadow ⊥ algebra-DEPENDENT Bell-capable core) × (Krylov integrability/chaos row: bounded-Krylov λ_L=0 PERMANENT ⊥ linear-Krylov THERMALIZING). All four cells occupied, axes ORTHOGONAL, neither subsuming. The S58↔S70 contradiction dissolves: Bell-violation (S=2.452) is a **column** fact (substrate IS quantum; S58's literal local-hidden-variable reading is falsified), while surviving hidden content is a **row** fact (bounded-Krylov ⇒ permanent, re-scoped from "whole GGE" to "bounded-Krylov row"). The DM relic (LEGGETT-MOMENT-70) is the unique two-coordinate **Cell D-P** (algebra-DEPENDENT ∧ bounded-Krylov). Sub-(b): the Born rule is an INPUT for both layers (Gleason consistency-only; cross-ref INV8-W2-3). Sub-(c): S58 superdeterminism is redirected to *geometric non-locality* (an EPR-incompleteness verdict on "{R_k} as complete", NOT a falsification). The convergence was real — kitaev accepted einstein catching a genuine slip in his R1 (concurrence↔occupation swap), then refined with a Krylov-row scale-stratification.
- **INV8-W4-2 (cosmic birefringence) → isotropic β_FW = 0.000° EXACT** (a structural null with two independent PROVEN-wall provenances: the Grading Theorem `Tr(γ9·f(D_K²/Λ²))=0` ∀f,∀τ, and CPT-exactness `[J,D_K]=0 → η_B=0`). The framework's Popper-sharpest falsifier — one LiteBIRD measurement of nonzero isotropic β at σ~0.01° kills `[J,D_K]=0` OR the Grading Theorem. mack CONCEDED β_iso=0 on both structural grounds (the GV-Heitsch class is a Corner-II *between-corridor* secondary class that cannot project onto the k=0 isotropic monopole) AND arithmetic grounds (a self-caught factor-≈57 error in his R1: 0.246° → 0.004295°, then →0). connes *independently verified* the concession (Sage-QQ). Surviving residue of Reading A: an anisotropic-only parity-odd EB/ℓ≥2 signature, magnitude UNCOMPUTED.

### What Changed
**(a) Numerical revisions** — mack's β: 0.246° → 0.004295° (factor-57 correction) → 0 (isotropic, EXACT); the GV-Heitsch class `−40579.15` re-read as a between-corridor secondary class (Δ_scheme=0).
**(b) Structural changes** — flat S58↔S70 contradiction → orthogonal **2×2 stratification** (a type-promotion: 1D cleave → 2×2 grid); the single isotropic-β falsifier → **isotropic-null + anisotropic-EB-residue split** (a type-promotion of the prediction); S58 superdeterminism re-scoped (full program → geometric-non-locality with row-scoped permanence); Born rule confirmed INPUT for both stratification layers.

### Effected In-Session (non-math)
None effected here — both workshops' non-math outcomes are SESSION-track promotions, routed OUT to the `/rclab-investigate --investigation 8` close per the track-local boundary (catalogued in `investigation-8-housekeeping.md §B`):
- **W4-1** — the 2×2-stratification verdict feeds the S58 quantum-foundations program scoping (capstone §-foundations) + cross-links INV8-W2-3; any GGE-decomposition theorem is promoted into a session, not held here.
- **W4-2** — the β=0 null routes to the capstone §7 falsifier-row + `falsifier-master-inventory.md` as a LiteBIRD-decisive parity falsifier orthogonal to the tilt observables — `mack-cosmic-bridge` sole-writer, session-track (NOT effected by the investigation orchestrator).

## Carry-Forward Computations

### CF-INV8-W4-1 — GGE reduced-density-matrix entanglement-vs-thermal partition (2×2-cell confirmation)
| Field | Spec |
|:------|:-----|
| **What** | Per-mode 4×4 reduced-density-matrix decomposition of ρ_GGE × Krylov-fate cross-tabulation — numerically confirm the 2×2 stratification's cell assignments (which mode lands in I-P / I-T / D-P / D-T). |
| **Inputs** | the 8-mode GGE Bogoliubov amplitudes (s52_bogoliubov_amp.npz); the Richardson-Gaudin {R_k}; the GGE Liouvillian Krylov/Lanczos spectrum (S104). |
| **Gate** | pre-registered `|Spearman ρ| < 0.3` independence gate on (M2-membership, Krylov-fate): PASS = axes transverse (2×2 confirmed); FAIL = collapses to a 1D cleave, re-opening the adjudication. |
| **Effort** | ~1–2 wave-equivalents. |

### CF-INV8-W4-2 — anisotropic odd-EB power spectrum C_ℓ^{EB,β} from the GV-Heitsch class
| Field | Spec |
|:------|:-----|
| **What** | Explicit ℓ-space projection of the GV-Heitsch Corner-II secondary class onto photon transport to compute the anisotropic odd-EB power spectrum `C_ℓ^{EB,β}` (ℓ≥2) magnitude + sign — the surviving (uncomputed) residue of Reading A after isotropic β=0 EXACT. |
| **Inputs** | the GV-Heitsch class `gv_canonical_difference_FW=−40579.15`; the §VII.BG Corner-II classification; the photon-transport / CMB EB machinery. |
| **Gate** | `[SIGN]` + magnitude vs LiteBIRD / CMB-S4 EB sensitivity, with an ℓ=0-leak consistency check against the proven isotropic null. |
| **Effort** | ~2–3 wave-equivalents. |

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-15 | GGE classical/quantum identity (W4-1) | flat S58↔S70 contradiction | RESOLVED: orthogonal 2×2 stratification (M2 × Krylov) | Bell=column fact, hidden content=row fact; partitions cross |
| 2026-06-15 | S58 superdeterminism program | literal local-hidden-variable | redirected → geometric non-locality (row-scoped permanence) | CHSH-violation falsifies literal LHV; bounded-Krylov row survives |
| 2026-06-15 | Born rule (W4-1 ↔ W2-3) | DEFENSIBLE | INPUT for both stratification layers | Gleason consistency-only |
| 2026-06-15 | isotropic cosmic birefringence β (W4-2) | open (β≠0 vs β=0) | β_iso = 0 EXACT (two PROVEN walls) | Grading Theorem + CPT-exactness; GV class can't source k=0 |
| 2026-06-15 | mack R1 β=0.246° prediction | asserted | RETRACTED (factor-57 error + structural) | Sage-verified 0.004295°, then →0 isotropic |
| 2026-06-15 | anisotropic odd-EB signature | (new) | nonzero-but-uncomputed (ℓ≥2 residue) | GV-Heitsch Corner-II secondary class |
| 2026-06-15 | β=0 parity falsifier | (new) | LiteBIRD-decisive null, orthogonal to tilt observables | session-track falsifier inventory (mack) |

## Files Produced

| Gate | Deliverable md | Closure | must_contain verified |
|:-----|:---------------|:--------|:----------------------|
| INV8-W4-1 | `workshops/inv8-w4-1-bell-vs-hidden-variable.md` | artifact-existence | `## Wrap-Up` ✓ / `Effected In-Session` ✓ / `Carry-Forward Computations` ✓ |
| INV8-W4-2 | `workshops/inv8-w4-2-cosmic-birefringence.md` | artifact-existence | `## Wrap-Up` ✓ / `Effected In-Session` ✓ / `Carry-Forward Computations` ✓ |
