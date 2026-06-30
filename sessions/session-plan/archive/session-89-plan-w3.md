# Session 89 Plan — Wave 3: Substrate-IS structural derivations + substrate-clock pinning

> **Provenance**: lizzi-spectral-functional-theorist orchestrator-direct planner-write per `/rclab-plan` skill §3b; per-gate runtime authors per ledger explicit hints (mixed lizzi/connes/volovik distribution: 3 lizzi-runtime + 3 connes-runtime + 3 volovik-runtime).
> **Theme**: ξ_KZ + d_eff Jensen perturbation + cocycle ratio regulator-class invariance + V_4 Sage-QQ enumeration + substrate-clock cancellation + substrate-clock pinning uniqueness + κ_2 resolvent expansion + SU(N) cross-validation + HK-5 τ_max bound (Ledger A items A.2, A.9, A.14, A.16, A.17, A.18, A.29, A.32, A.35).
> **Composition order**: Wave 3 dispatches in S89 Batch 1 with W1-W2 + W4-W7 in parallel.
> **Natural-split fallback** (RECOMMENDED — 9 items mixed authorship): W3a = A.14, A.32, A.35 (lizzi 3 items, regulator/atlas/HK regime program); W3b = A.9, A.16, A.29 (connes 3 items, CM-1995 §III.4 + V_4 program); W3c = A.2, A.17, A.18 (volovik 3 items, KZ + substrate-clock program). Single-pass write attempted; split available if mid-wave context exhaustion.
> **Source ledger**: `sessions/archive/session-88/s88-pending-edits-ledger.md` Ledger A Cluster C (lines 58-70 of S89 context manifest).

---

## Wave 3 Summary

Wave 3 lands 9 substrate-IS structural derivation gates spanning four substrate-physics domains:

1. **ξ_KZ closed-form derivation from atlas T1** (A.2): substrate-natural Kibble-Zurek scaling derived from Bogoliubov unitarity at the fold + cascade-tail effective dimension, with hawking-theorist BLACKLISTED per ledger constraint (volovik PRIMARY runtime). The substrate IS the KZ-transit; ξ_KZ is intrinsic to the substrate's deformation through the fold.

2. **d_eff and κ_2 second-order Jensen perturbation** (A.9 + A.29): two CM-1995 §III.4 finite-spectral-triple residue formula derivations, supplying closed-form coefficients for the HK-5 residual structure (`HK-5(τ_fold) + c·τ² + O(τ³)`) and the higher-order resolvent expansion κ_2_substrate. Connes-domain.

3. **Cocycle ratio regulator-class invariance + SU(N) cross-validation + HK-5 τ_max bound** (A.14 + A.32 + A.35): three lizzi-runtime substrate-spectral-functional gates testing (i) regulator-class invariance of substrate cocycle norm ratios under the 4-regulator atlas {ζ, Pauli-Villars, Mellin, sharp-cutoff}, (ii) SU(N) Cartan-rational-sum cross-validation discriminating LOAD-BEARING vs COINCIDENCE for the 5π = (dim+rank)/2 · π_Plancherel chain, (iii) HK-5 closed-form regime-of-validity τ_max bound.

4. **V_4 Sage-QQ enumeration extended sectors** (A.16): connes-domain V_4-on-triality character enumeration at L_max ∈ {8, 10, 12} with cocycle functor F invariance test, spanning BOTH single-τ-slice (Level-1) AND moduli-deformation (Level-2) substrate-IS levels per S88 W-7 V.4 K=2 MANDATORY.

5. **Substrate-clock cancellation + pinning uniqueness** (A.17 + A.18): two volovik-runtime substrate-clock gates testing (i) discriminating Pinning-A vs Pinning-B cancellation predicate at Δ(g=322) ≈ 290.80 OOM, (ii) uniqueness derivation for `a_substrate(g) ~ L_pix(g)` as THE unique substrate-natural clock for the lock cascade.

All 9 gates are COMPUTE-class per `wave-classification.md` M1∧M2∧M3∧M4 conjunction. None require methodology-wave-allowlist append; none are MIXED-class.

## Wave 3 Decision Point Prerequisites

- **No upstream Wave dependencies INSIDE Wave 3.** All 9 gates are Wave-3-internal except for cross-wave outputs feeding Waves 5 and 6 (declared in §"Wave 3 → Waves 5/6 Decision Point" below).
- **Canonical constants required at plan-freeze** (all imported via `from canonical_constants import *`):
  - `tau_fold = 0.19` (R-PROTECTED)
  - `M_KK = 7.428660036284456e+16 GeV`
  - `Delta_BCS = 0.4642547394830737` (R-PROTECTED)
  - `cocycle_norm_phi67 = 0.793346 M_KK²`
  - `cocycle_norm_phi88 = 0.108307 M_KK²`
  - `substrate_cocycle_ratio_67_88 = 7.324992` (Sage-exact at machine precision)
- **D_K spectral cache pinned** at `computations/_shared/s84_spectrum_cache_L12_tau019.npz` (SHA at plan-freeze; consumed by A.14, A.16, A.29, A.35).
- **Atlas T1 substrate-spectral source pinned** at `sessions/archive/session-88/workshops/s88-w2-kz-universality-class.md` §VII (consumed by A.2).
- **CM-1995 §III.4 finite-spectral-triple residue formula** is the substrate-IS source for A.9 and A.29; cited verbatim in machinery pin field.
- **No Stage-1-CANDIDATE registry entries pinned as Input-SHA** in this wave (Wave 3 produces structural derivations; downstream Stage-2 verifies in Wave 8 cross-axis).

---

## §W3-1. S89-XI-KZ-SUBSTRATE-NATURAL-DERIVATION-FROM-T1-ATLAS  (A.2)

### 1. Gate ID
`S89-XI-KZ-SUBSTRATE-NATURAL-DERIVATION-FROM-T1-ATLAS`

### 2. Trigger
`[VERIFY-THEOREM]` — closed-form derivation of ξ_KZ from substrate-spectral first principles; PASS predicate is theorem-form (closed-form expression with explicit (ν, z) pin), NOT numerical comparison.

### 3. Classification
**PHONONIC** — ξ_KZ governs substrate excitation spectrum across the fold transit; the substrate IS the KZ-transit, and ξ_KZ measures the intrinsic correlation length at which substrate excitations decouple from the deformation rate. Excitations through the fold are phononic relay patterns of the substrate's deformation manifold.

### 4. Agent type
**Runtime author**: `volovik-superfluid-universe-theorist` (PRIMARY per ledger line 84: "volovik PRIMARY; connes CO-AUTHOR; hawking BLACKLISTED").
**Co-reviewer**: `connes-ncg-theorist` (CO-AUTHOR, NCG-axiomatic side).
**BLACKLISTED**: `hawking-theorist` (per ledger explicit constraint; hawking's Penrose-causal frame defaults to container-thinking on causally-disconnected pre/post-fold sectors, contaminating the substrate-IS derivation).
**FORBIDDEN at runtime**: `gen-physicist` (per `feedback_reporting-framing.md` agent BLACKLIST applied to test-case design; gen-physicist's defaults route ξ_KZ through laboratory-IN BEC analog rather than substrate-IS spectral structure).

### 5. Hypothesis
ξ_KZ is derivable in closed form from substrate-spectral arguments (atlas T1 `dt/T_L` rate × Bogoliubov unitarity at the fold + cascade-tail effective dimension d_eff) with explicit (ν, z) critical exponent pin for the BdG-A_2 transition class, INDEPENDENT of laboratory-IN BEC analog calibration.

### 6. Method (self-contained dispatch prompt)

**Script path**: `computations/session-89/s89_w3_xi_kz_substrate_natural_derivation.py`

**Compute environment**:
- Python: `phonon-exflation-sim/.venv312/Scripts/python.exe` (MANDATORY)
- `import os; os.environ.setdefault('OMP_NUM_THREADS', '8')` BEFORE `import numpy`
- GPU not required (closed-form symbolic derivation; numerical verification at single τ point only)
- `from canonical_constants import *` (MANDATORY)
- Optional: `from sage.all import Rational, sqrt, pi, simplify` for Sage-QQ exact arithmetic verification (via Sage MCP `sage_eval` if local Sage not available)

**Step-by-step instructions**:

1. Import canonicals: `tau_fold`, `M_KK`, `Delta_BCS`, `xi_E_GGE_inv` (= 13.642473425595973 per S86 W4 P4).
2. Read atlas T1 substrate-spectral source from `sessions/archive/session-88/workshops/s88-w2-kz-universality-class.md` §VII (precomputed PROVEN per S88 W-2 KZ universality class workshop). Extract: (a) substrate quench rate `dt/T_L` evaluated at fold; (b) Bogoliubov unitarity transformation at fold; (c) cascade-tail effective dimension d_eff (anchored to A.9 closed-form HK-5 + Jensen perturbation; if A.9 not yet PASS at plan-freeze, use HK-5(τ_fold) baseline).
3. Derive ν (correlation-length critical exponent) for BdG-A_2 transition class from substrate-spectral source: ν = 1/(2−η_anom), with η_anom computed from substrate Hochschild cocycle anomalous dimension at the fold's polycritical point. Pin ν as Sage-Q rational where possible; if irrational, pin to bit-exact float64 with substrate-physics provenance.
4. Derive z (dynamic critical exponent) from Bogoliubov unitarity at fold: z = 1 + γ_dyn, with γ_dyn computed from the substrate's effective dimension d_eff and the BdG quasiparticle dispersion at the fold's polycritical point.
5. Assemble closed-form ξ_KZ expression: ξ_KZ ~ |T_Q|^(ν/(1+νz)) · (substrate-spectral prefactor), where T_Q = `dt/T_L`|_fold is the substrate quench timescale. The closed-form derivation MUST include the substrate-spectral prefactor (NOT just the Kibble-Zurek scaling form) since the prefactor encodes the substrate's intrinsic length-scale (`xi_E_GGE_inv` substrate-natural anchor).
6. Verify dimensional consistency: [ξ_KZ] = length; [T_Q] = time; [ν], [z] dimensionless. Verify limiting cases: (a) ν → ½, z → 2 reproduces classical KZ form; (b) z → 1 (Lorentz-invariant limit) reproduces Bogoliubov-quench prediction; (c) ν → 0 (mean-field limit) suppresses ξ_KZ to substrate-natural anchor.
7. Compute numerical evaluation at τ_fold: ξ_KZ(τ_fold) in M_KK^{-1} units; cross-check against substrate-natural xi_E_GGE_inv anchor.
8. Cross-check against Sage MCP `sage_eval` for Sage-QQ exact match where ν and z are rational.
9. Emit:
   - JSON sidecar with closed-form ξ_KZ expression (LaTeX-compatible string), (ν, z) pin (as Sage-QQ Fraction or float64), substrate-spectral prefactor, numerical evaluation at τ_fold.
   - PNG plot showing ξ_KZ(τ) across τ ∈ [0, 0.4] with τ_fold annotated.
   - Verdict line per Schema-v2 in `computations/session-89/s89_gate_verdicts.txt`.

**Input SHA-256 pins** (each file the script reads; computed at plan-freeze and pinned in INPUT-PIN MAP):
- `canonical_constants.py` — `<pinned at plan-freeze>` (consumes tau_fold, M_KK, Delta_BCS, xi_E_GGE_inv)
- `sessions/archive/session-88/workshops/s88-w2-kz-universality-class.md` — `<pinned at plan-freeze>` (atlas T1 source)
- `sessions/permanent-results-registry.md` — `<pinned at plan-freeze>` (BdG-A_2 transition class registry)

**Cross-checks**:
- Dimensional consistency [ξ_KZ] = length (MANDATORY, per `agent-standards.md §"Formal Rigor"`)
- Limiting cases (ν → ½ classical KZ, z → 1 Lorentz-invariant, ν → 0 mean-field) — MANDATORY
- Sage-QQ exact arithmetic verification of ν and z where rational — RECOMMENDED
- Cross-check ξ_KZ(τ_fold) against substrate-natural xi_E_GGE_inv anchor (relative deviation < 50% expected since xi_E_GGE_inv is the static-correlation-length substrate-natural anchor and ξ_KZ is the dynamic-quench correlation length — order-of-magnitude match expected)

### 7. Machinery pin (PRDR — every free parameter pinned)

```yaml
gate_id: S89-XI-KZ-SUBSTRATE-NATURAL-DERIVATION-FROM-T1-ATLAS
schema_version: R3
trigger: VERIFY-THEOREM
classification: PHONONIC
machinery_pin_map:
  tau_evaluate: 0.19  # tau_fold canonical pin (R-PROTECTED)
  L_max: 12  # for any spectral-cache cross-check
  transition_class: "BdG-A_2"  # pinned at plan-freeze per S88 W-2 PROVEN atlas T1
  bogoliubov_unitarity_method: "fold-anchored unitary transformation; substrate-spectral source per s88-w2-kz-universality-class.md §VII"
  d_eff_source: "A.9 HK-5 closed-form + Jensen perturbation if available; HK-5 baseline at tau_fold otherwise"
  d_eff_baseline: "HK-5(tau_fold) = 5/(1 - tau_fold/(5*pi))"  # per S87 d_eff workshop
  nu_derivation: "1/(2 - eta_anom) from substrate Hochschild cocycle anomalous dimension at fold polycritical point"
  z_derivation: "1 + gamma_dyn from substrate effective dimension + BdG quasiparticle dispersion at fold polycritical point"
  prefactor_anchor: "xi_E_GGE_inv = 13.642473425595973"
  scheme: "substrate-natural-T1-atlas-derivation"
  convention: "BdG-A_2-transition-class-fold-anchored"
  random_seed: N/A  # closed-form derivation, no Monte Carlo
  GPU_path: N/A  # closed-form symbolic + single-point numerical evaluation
input_sha_pins:
  canonical_constants_py: <pinned at plan-freeze>
  atlas_T1_source: <pinned at plan-freeze>
  permanent_results_registry: <pinned at plan-freeze>
output_4_tuple:
  value: "{closed-form-xi-KZ-expression, (nu, z) pin, prefactor, numerical-eval-at-tau-fold}"
  scheme: "substrate-natural-T1-atlas-derivation"
  convention: "BdG-A_2-transition-class-fold-anchored"
  L_max: 12
audit_sha256: <computed at runtime via closure_hash(input_pin_map)>
```

### 8. Expected output 4-tuple
- `value`: 4-element record `{xi_KZ_closed_form (LaTeX string), (nu, z) Sage-QQ Fraction or float64, prefactor (float64), xi_KZ_at_tau_fold (M_KK^{-1} units)}`
- `scheme`: `substrate-natural-T1-atlas-derivation`
- `convention`: `BdG-A_2-transition-class-fold-anchored`
- `L_max`: `12`

### 9. PASS/FAIL/INFO thresholds with tolerance rule

- **PASS** iff:
  - (a) Closed-form ξ_KZ expression derived with explicit (ν, z) pin from substrate-spectral source (theorem-form output, NOT numerical fit).
  - (b) Dimensional consistency verified: [ξ_KZ] = length.
  - (c) Limiting cases verified: ν → ½ + z → 2 reproduces classical KZ; z → 1 reproduces Bogoliubov-quench prediction.
  - (d) Numerical ξ_KZ(τ_fold) computed and cross-checked against substrate-natural xi_E_GGE_inv anchor at order-of-magnitude (relative deviation < 200%).
- **INFO** iff (a) holds but (b) and/or (c) and/or (d) fail; the closed-form is derived but verification is incomplete (carry-forward to S90 W-X for completion).
- **FAIL** iff (a) fails — no closed-form derivation possible from substrate-spectral source; ledger A.2 hypothesis falsified.
- **Tolerance rule**: THEOREM tolerance for (a)-(c) (theorem-form match, not numerical band); RATIO tolerance < 200% for (d) (order-of-magnitude match against substrate-natural anchor).

### 10. Substitution chain

A.2 is a derivation gate, not a sign/direction/threshold claim. The substitution chain is the derivation itself; written in §6 Method Steps 3-5 above. No additional pre-registration substitution chain is required at the plan-block level (the derivation IS the chain).

### 11. What PASSES/FAILS MEAN for solution space

- **PASS**: ξ_KZ is substrate-derivable from atlas T1 + Bogoliubov unitarity + d_eff cascade-tail. The substrate-IS reading of KZ universality is structurally complete; future cross-pillar bridge entries (e.g., FWD-Cn substrate-IS ξ_KZ ↔ laboratory-IN BEC quench correlation length) become registry-eligible per the 5 IS-not-IN anatomy elements + 3-level structural-confidence ladder per `cross-pillar-bridge-anatomy.md`.
- **INFO**: closed-form derived but verification incomplete; substrate-IS reading partially supported, requires completion in S90.
- **FAIL**: substrate-spectral source insufficient to derive ξ_KZ in closed form; the BdG-A_2 transition class either (i) requires non-substrate-IS information (laboratory-IN data) OR (ii) the atlas T1 PROVEN status was over-claimed at S88 W-2. Both readings would route to plan-freeze halt at S90 with mandatory remediation.

### 12. Effort estimate
**1.0 wave-equivalents** — closed-form derivation requires (a) extracting atlas T1 elements, (b) deriving ν and z from substrate-physics first principles, (c) assembling closed form, (d) verifying limits + dimensional consistency. Single-pass derivation at the closed-form level; no Monte Carlo or large-spectrum sweep.

### 13. Substrate framing per `phononic-framing.md` IS-not-IN

The substrate IS the KZ-transit through the fold. ξ_KZ is the intrinsic correlation length at which the substrate's excitation spectrum decouples from its own deformation rate; it is NOT a property of fields living "in" a pre-existing geometric container. The Bogoliubov unitarity at the fold IS the substrate's own deformation transformation (Volovik superfluid-universe analogy is laboratory-IN model OF the substrate-IS structure, not a container).

**FORBIDDEN container-thinking** (must be actively corrected if hawking-style language emerges):
- "Particles created IN the curved spacetime around the fold"
- "ξ_KZ is the correlation length IN the BEC analog"
- "The substrate moves through the fold"

**REQUIRED substrate-IS framing**:
- The fold IS the substrate's intrinsic phase transition; ξ_KZ measures the substrate's own correlation length at the transition.
- The BEC analog is a laboratory-IN model OF the substrate-IS KZ structure; the substrate is fundamental, the BEC is a projection.
- The substrate's deformation (parameterized by τ) is intrinsic; "moving through" τ is container language and must be reframed as "the substrate IS the τ-deformation manifold; ξ_KZ measures the correlation length of substrate excitations at τ_fold."

---

## §W3-2. S89-D-EFF-CM-1995-SECTION-III-4-SECOND-ORDER-JENSEN-PERTURBATION  (A.9)

### 1. Gate ID
`S89-D-EFF-CM-1995-SECTION-III-4-SECOND-ORDER-JENSEN-PERTURBATION`

### 2. Trigger
`[VERIFY-THEOREM]` — closed-form derivation of coefficient `c` in `HK-5(τ_fold) + c·τ² + O(τ³)` from CM-1995 §III.4 second-order Jensen perturbation; PASS predicate is theorem-form (closed-form c expression) AND numerical match against W-12 W3c-57 residual within 5%.

### 3. Classification
**GEOMETRIC** — d_eff is a substrate spectral structure observable derived from the heat-kernel expansion of D_K^2 at τ_fold; the Jensen perturbation is the substrate's own deformation at second order in τ. This is substrate spectral content, not phononic excitation propagation.

### 4. Agent type
**Runtime author**: `connes-ncg-theorist` (PRIMARY; CM-1995 §III.4 finite-spectral-triple residue formula IS connes-domain — the formula was derived by Connes-Moscovici 1995 and is the substrate-IS source for finite-spectral-triple residues at the second order).
**Co-reviewer**: `lizzi-spectral-functional-theorist` (CO-AUTHOR, regulator-axis cross-check on the c coefficient's regulator-class invariance).
**FORBIDDEN at runtime**: `gen-physicist` (per `feedback_reporting-framing.md`; gen-physicist defaults route Jensen perturbation through gauge-theory-on-curved-background container language).

### 5. Hypothesis
The HK-5 closed-form residual c coefficient in the expansion `d_eff(τ) = HK-5(τ_fold) + c·τ² + O(τ³)` is derivable from CM-1995 §III.4 finite-spectral-triple residue formula at second order in the Jensen deformation chain rule, with closed-form `c(L_max=12)` matching the numerical residual observed at S88 W-12 W3c-57 within 5%.

### 6. Method (self-contained dispatch prompt)

**Script path**: `computations/session-89/s89_w3_d_eff_cm1995_second_order_jensen_perturbation.py`

**Compute environment**:
- Python: `phonon-exflation-sim/.venv312/Scripts/python.exe` (MANDATORY)
- `import os; os.environ.setdefault('OMP_NUM_THREADS', '8')` BEFORE `import numpy`
- GPU recommended for D_K^2 spectral evaluation if matrix dim ≥ 100×100 at L_max=12 (use `torch.linalg` per `math-scripts.md §Environment`); plan-freeze cache at `s84_spectrum_cache_L12_tau019.npz` makes recomputation unnecessary at L_max ≤ 12 — reuse cache.
- `from canonical_constants import *` (MANDATORY)
- Sage MCP for symbolic computation: `sage_eval` for Sage-QQ exact second-order Jensen perturbation expansion

**Step-by-step instructions**:

1. Import canonicals: `tau_fold`, `M_KK`. Set HK-5 closed-form: `HK_5_closed = 5 / (1 - tau_fold / (5*pi))` per S87 d_eff workshop substrate-IS pin.
2. Read D_K spectral cache `computations/_shared/s84_spectrum_cache_L12_tau019.npz` (eigenvalues at τ_fold, L_max=12, sector-decomposed).
3. Read CM-1995 §III.4 finite-spectral-triple residue formula citation. The formula gives the second-order Jensen perturbation of d_eff via the chain rule:
   `c = (1/2) · ∂²d_eff / ∂τ² |_{τ=τ_fold}` evaluated through the residue formula on the perturbed Dirac operator `D_K(τ_fold + δτ) = D_K(τ_fold) + δτ · ∂D_K/∂τ + (δτ²/2) · ∂²D_K/∂τ² + ...`.
4. Derive ∂D_K/∂τ and ∂²D_K/∂τ² from the Jensen TT-deformation explicit form (TT-deformation is the framework's canonical Jensen deformation; the deformation operator structure is fixed by the substrate algebra `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`).
5. Apply the residue formula at second order:
   `c = Res_{s=0} [d²/ds² Tr(P_0 · D_K(τ)^{-2s}) ]_{τ_fold}`
   where P_0 is the band-0 spectral projector and the residue is taken via the substrate's dimension spectrum.
6. Evaluate the residue numerically at L_max=12 using the cached spectrum + Sage-QQ symbolic expansion of the residue formula's coefficients. Pin `c(L_max=12)` to bit-exact float64 (or Sage-QQ Fraction if rational).
7. Cross-check against S88 W-12 W3c-57 residual: extract residual = d_eff_observed - HK-5_closed at τ near τ_fold + δτ for δτ ∈ {0.01, 0.02, 0.05}; fit residual ~ c·δτ² + O(δτ³); compare fit-extracted c against substrate-derived closed-form c.
8. Verify limiting cases: (a) c → 0 as τ_fold → 0 (no second-order correction at trivial deformation); (b) c finite at τ_fold = 0.19 (well-defined substrate-IS spectral content).
9. Verify regulator-class invariance: re-derive c under {ζ, Pauli-Villars, Mellin, sharp-cutoff} regulators (per `regulator-pin-discipline.md`); MANDATORY tagging `a_n^{regulator}` for each regulator's intermediate quantities.
10. Emit:
    - JSON sidecar with closed-form c expression (Sage-QQ form if rational), numerical c(L_max=12), residual fit-extracted c, relative deviation between substrate-derived and fit-extracted c, regulator-class scan results.
    - PNG plot showing d_eff(τ) - HK-5_closed(τ) ~ c·τ² fit at L_max=12.
    - Verdict line per Schema-v2 in `computations/session-89/s89_gate_verdicts.txt`.

**Input SHA-256 pins**:
- `canonical_constants.py` — `<pinned at plan-freeze>`
- `computations/_shared/s84_spectrum_cache_L12_tau019.npz` — `<pinned at plan-freeze>`
- `sessions/archive/session-88/workshops/s88-w12-w3c-57-hk5-residual-origin.md` — `<pinned at plan-freeze>` (W-12 V.2 source)
- CM-1995 §III.4 reference (mathematical-source, no SHA pin needed; cited in machinery field)

**Cross-checks**:
- Limiting case c → 0 as τ_fold → 0 (MANDATORY per `agent-standards.md §"Formal Rigor"`)
- Regulator-class invariance scan {ζ, Pauli-Villars, Mellin, sharp-cutoff} (MANDATORY per `regulator-pin-discipline.md`)
- Residual fit-extracted c vs substrate-derived c comparison (MANDATORY for PASS predicate)
- Sage-QQ exact arithmetic verification where feasible (RECOMMENDED)

### 7. Machinery pin (PRDR)

```yaml
gate_id: S89-D-EFF-CM-1995-SECTION-III-4-SECOND-ORDER-JENSEN-PERTURBATION
schema_version: R3
trigger: VERIFY-THEOREM
classification: GEOMETRIC
machinery_pin_map:
  tau_evaluate: 0.19  # tau_fold (R-PROTECTED)
  L_max: 12
  HK_5_closed_form: "5 / (1 - tau_fold / (5*pi))"  # S87 d_eff workshop substrate-IS pin
  CM_1995_section: "III.4"  # finite-spectral-triple residue formula
  jensen_deformation_class: "TT-deformation"  # framework canonical
  derivative_method: "Jensen chain rule second order on D_K(tau)"
  residue_formula: "c = Res_{s=0} [d²/ds² Tr(P_0 · D_K(tau)^{-2s}) ]_{tau_fold}"
  band_projector: "P_0"  # band-0 spectral projector
  delta_tau_scan: [0.01, 0.02, 0.05]  # for residual fit extraction
  regulator_scan: ["zeta", "Pauli-Villars", "Mellin", "sharp-cutoff"]  # MANDATORY tagging
  scheme: "CM-1995-section-III-4-second-order-Jensen-perturbation"
  convention: "TT-deformation-fold-anchored-band-0-projector"
  random_seed: N/A
  GPU_path: "torch.linalg if matrix dim >= 100x100; else numpy with OMP=8"
input_sha_pins:
  canonical_constants_py: <pinned at plan-freeze>
  spectrum_cache_L12_tau019_npz: <pinned at plan-freeze>
  s88_w12_w3c_57_md: <pinned at plan-freeze>
output_4_tuple:
  value: "{c_closed_form (Sage-QQ or LaTeX), c_L12 (float64), c_fit_extracted (float64), rel_dev (float64), regulator_scan_pass_count}"
  scheme: "CM-1995-section-III-4-second-order-Jensen-perturbation"
  convention: "TT-deformation-fold-anchored-band-0-projector"
  L_max: 12
audit_sha256: <computed at runtime via closure_hash(input_pin_map)>
```

### 8. Expected output 4-tuple
- `value`: 5-element record `{c_closed_form (Sage-QQ form or LaTeX string), c_L12 (float64), c_fit_extracted (float64), rel_dev (float64), regulator_scan_pass_count (int 0..4)}`
- `scheme`: `CM-1995-section-III-4-second-order-Jensen-perturbation`
- `convention`: `TT-deformation-fold-anchored-band-0-projector`
- `L_max`: `12`

### 9. PASS/FAIL/INFO thresholds with tolerance rule

- **PASS** iff:
  - (a) Closed-form `c` derived via CM-1995 §III.4 residue formula at second order.
  - (b) `|c_L12 - c_fit_extracted| / |c_fit_extracted| ≤ 0.05` (5% match between substrate-derived and W-12 W3c-57 residual fit).
  - (c) Limiting cases verified: c → 0 as τ_fold → 0; c finite at τ_fold = 0.19.
  - (d) Regulator-class invariance: `regulator_scan_pass_count == 4` (all 4 regulators yield same c within 1%; substrate-IS observable should be regulator-class invariant).
- **INFO** iff (a) and (c) hold but (b) FAILs (5% < rel_dev ≤ 20%) OR (d) FAILs (3 of 4 regulators agree); the substrate-derived c is structurally correct but numerical alignment is partial.
- **FAIL** iff (a) fails OR (c) fails OR rel_dev > 20%; the substrate-IS HK-5 residual structure cannot be derived from CM-1995 §III.4 at second order via Jensen perturbation.
- **Tolerance rule**: RATIO tolerance ≤ 5% for PASS on (b); ABSOLUTE tolerance ≤ 1% relative spread across regulators for PASS on (d); THEOREM tolerance for (a) and (c).

### 10. Substitution chain

A.9 is a closed-form derivation gate; the substitution chain is the derivation in §6 Method Steps 3-5. No additional sign/direction claim requiring pre-registration substitution chain.

### 11. What PASSES/FAILS MEAN for solution space

- **PASS**: HK-5 closed-form `5/(1−τ/(5π))` is the exact d_eff at τ_fold; residuals at small δτ are explained by CM-1995 §III.4 second-order Jensen perturbation. The substrate's d_eff structure is fully understood at second order; W-12 W3c-57 residual origin is settled. d_eff Richardson scan A.8 (Wave 5) becomes a test of HK-5 + c·τ² + O(τ³) expansion CONVERGENCE rather than HK-5 form discovery.
- **INFO**: closed-form derived but numerical alignment with W-12 residual partial; substrate-IS reading partially supported, requires regulator-class scan completion or higher-order resolvent expansion (links to A.29 κ_2 substrate).
- **FAIL**: HK-5 + c·τ² is NOT the substrate-IS structure of d_eff; either HK-5 closed form is wrong (contradicts S87 d_eff workshop) OR Jensen perturbation does not capture residual at L_max=12. Both readings route to S90 plan-freeze halt with mandatory remediation citing CM-1995 §III.4 limits.

### 12. Effort estimate
**1.0–1.5 wave-equivalents** — closed-form derivation via CM-1995 §III.4 + numerical residual fit + regulator-class scan. Single dispatch; uses pre-existing L_max=12 spectrum cache.

### 13. Substrate framing per `phononic-framing.md` IS-not-IN

The substrate IS the heat-kernel structure of D_K^2 at τ_fold. d_eff is the substrate's own effective dimension at the heat-kernel small-time limit; HK-5 is the closed-form expression of this substrate-IS observable. Jensen perturbation IS the substrate's intrinsic deformation manifold (TT-deformation parameter τ); second-order in τ is the substrate's own second derivative at its fold anchor.

**FORBIDDEN container-thinking**:
- "d_eff is the dimension of the space the substrate lives in"
- "Jensen perturbation deforms the substrate"
- "Heat-kernel expansion in curved-spacetime background"

**REQUIRED substrate-IS framing**:
- d_eff IS the substrate's spectral dimension; the substrate has no "host space."
- Jensen perturbation IS the substrate's intrinsic deformation; "deforming the substrate" reframed as "the substrate's τ-deformation manifold has tangent vector ∂/∂τ."
- Heat-kernel expansion IS the substrate's own short-time spectral asymptotic; no external "background spacetime" exists.

---

## §W3-3. S89-SUBSTRATE-COCYCLE-RATIO-REGULATOR-CLASS-INVARIANCE-SCAN  (A.14)

### 1. Gate ID
`S89-SUBSTRATE-COCYCLE-RATIO-REGULATOR-CLASS-INVARIANCE-SCAN`

### 2. Trigger
`[VERIFY]` — regulator-class invariance scan of the substrate cocycle norm ratio ‖φ_67‖^R / ‖φ_88‖^R under R ∈ {ζ, Pauli-Villars, Mellin, sharp-cutoff}; PASS predicate is numerical: ratio ≡ 7.324992 within 0.1% across all 4 regulators.

### 3. Classification
**GEOMETRIC** — substrate cocycle norms are spectral-IS structural quantities defined on the substrate's algebra `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`; the ratio's regulator-class invariance is a substrate-spectral-structure test, not a phononic excitation propagation test.

### 4. Agent type
**Runtime author**: `lizzi-spectral-functional-theorist` (PRIMARY; regulator-axis program is lizzi's central contribution per agent definition — "the choice between S_cutoff = Tr f(D^2/Λ²) and S_zeta = ζ_D(0) is not mathematical convenience — it determines which spectral moments enter the action").
**Co-reviewer**: `connes-ncg-theorist` (CO-AUTHOR, NCG-axiomatic side; substrate-axis verification on cocycle definition).
**FORBIDDEN at runtime**: `gen-physicist`.

### 5. Hypothesis
The substrate cocycle norm ratio ‖φ_67‖ / ‖φ_88‖ is regulator-class INVARIANT (Sage-exact value 7.324992 to machine precision) across the 4-regulator atlas {ζ, Pauli-Villars, Mellin, sharp-cutoff}, demonstrating that substrate-IS cocycle structure is independent of the UV-regulator axis choice.

### 6. Method (self-contained dispatch prompt)

**Script path**: `computations/session-89/s89_w3_substrate_cocycle_ratio_regulator_class_invariance_scan.py`

**Compute environment**:
- Python: `phonon-exflation-sim/.venv312/Scripts/python.exe`
- `import os; os.environ.setdefault('OMP_NUM_THREADS', '8')` BEFORE `import numpy`
- GPU recommended for ‖φ_a‖^R Mellin-residue evaluation at L_max=10 (matrix dim ~ 1000×1000 sector-decomposed; use `torch.linalg`)
- `from canonical_constants import *` (MANDATORY)

**Step-by-step instructions**:

1. Import canonicals: `tau_fold`, `M_KK`, `cocycle_norm_phi67` (= 0.793346 M_KK²), `cocycle_norm_phi88` (= 0.108307 M_KK²), `substrate_cocycle_ratio_67_88` (= 7.324992 Sage-exact).
2. Read D_K spectral cache `computations/_shared/s84_spectrum_cache_L12_tau019.npz` filtered to L_max=10.
3. Read substrate cocycle definition for φ_67 (chiral pair ker(ι_*) generator) and φ_88 (Cartan hypercharge ker(ι_*) generator) from S86 W-5 substrate-IS source. Both cocycles live on `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` algebra projection χ : A_K → M_2(ℂ) sending M_3(ℂ) → 0.
4. For each regulator R ∈ {ζ, Pauli-Villars, Mellin, sharp-cutoff}, evaluate ‖φ_a‖^R for a ∈ {67, 88}:
   - **R = ζ**: `‖φ_a‖^ζ = ζ_{D_K}(0; φ_a) = Res_{s=0} Tr(φ_a · D_K^{-2s})` per zeta-regulated cocycle norm. Tag intermediate as `a_n^{ζ}` per `regulator-pin-discipline.md` MANDATORY tagging.
   - **R = Pauli-Villars**: `‖φ_a‖^{PV} = lim_{Λ→∞} Tr(φ_a · [D_K² / (D_K² + Λ²)]^N)` for sufficient subtractions N. Tag `a_n^{Pauli-Villars}`.
   - **R = Mellin**: `‖φ_a‖^{Mellin} = (1/(2πi)) ∮_C ds Γ(s) · Tr(φ_a · D_K^{-2s})` with contour C around s=0 pole. Tag `a_n^{Mellin}`.
   - **R = sharp-cutoff**: `‖φ_a‖^{cutoff} = Tr(φ_a · θ(Λ_UV - |D_K|))` for Λ_UV = M_KK substrate canonical UV scale. Tag `a_n^{cutoff}`.
5. Compute ratio R_a/R_b = ‖φ_67‖^R / ‖φ_88‖^R for each R. Pin each ratio as bit-exact float64 (Sage-QQ Fraction where rational).
6. Compute relative deviation per regulator: `rel_dev_R = |ratio^R - substrate_cocycle_ratio_67_88| / substrate_cocycle_ratio_67_88`.
7. Verify regulator-class invariance: PASS iff `max_R rel_dev_R ≤ 0.001` (0.1% across all 4 regulators); INFO iff (0.001, 0.01]; FAIL iff > 0.01.
8. Cross-check (Δ_B/Δ_A)^p cancellation theorem applicability: confirm that φ_67 and φ_88 share common p_67 = p_88 = p (per `inheritance-falsifier-protocol.md §"(Δ_B/Δ_A)^p Cancellation Theorem"`); if so, the ratio is preserved under any common-exponent lab conversion (cross-link to W-5 §VII.W substrate-IS bridge).
9. Verify Sage-QQ exact arithmetic at machine precision: cross-check via Sage MCP `sage_eval` for the canonical ratio value.
10. Emit:
    - NPZ sidecar with per-regulator ratios, relative deviations, ‖φ_a‖^R values, regulator-class invariance verdict.
    - PNG plot showing ratio across 4 regulators with substrate canonical 7.324992 line annotated.
    - JSON metadata with substitution-chain verification + regulator-pin discipline compliance.
    - Verdict line per Schema-v2 in `computations/session-89/s89_gate_verdicts.txt` with `convention=4-regulator-atlas-substrate-cocycle-ratio-invariance` (no SCHEMATIC suffix; this gate uses FULL physical regularizations, not the SCHEMATIC `_spectral_action_regulators.py` helpers — class pin = FULL).

**Input SHA-256 pins**:
- `canonical_constants.py` — `<pinned at plan-freeze>`
- `computations/_shared/s84_spectrum_cache_L12_tau019.npz` — `<pinned at plan-freeze>` (filtered to L_max=10)
- `sessions/archive/session-86/workshops/s86-w-5-hp1-quantum-metric-bridge.md` — `<pinned at plan-freeze>` (S86 W-5 cocycle source)
- `sessions/permanent-results-registry.md §VII.W` — `<pinned at plan-freeze>` (substrate cocycle anchor)

**Cross-checks**:
- Sage-QQ exact arithmetic verification of substrate canonical ratio 7.324992 (MANDATORY)
- (Δ_B/Δ_A)^p cancellation theorem cross-link (RECOMMENDED for downstream lab-falsifier consistency)
- All 4 regulators satisfy regulator-pin discipline `a_n^{R}` MANDATORY tagging (MANDATORY per `regulator-pin-discipline.md`)
- Class pin = FULL (full physical regularization, not SCHEMATIC) — declared in machinery pin field per `substrate-first-canonical-sourcing.md §(iv)` MANDATORY at K=4 since S88 W7b-83

### 7. Machinery pin (PRDR)

```yaml
gate_id: S89-SUBSTRATE-COCYCLE-RATIO-REGULATOR-CLASS-INVARIANCE-SCAN
schema_version: R3
trigger: VERIFY
classification: GEOMETRIC
machinery_pin_map:
  tau_evaluate: 0.19
  L_max: 10
  cocycle_phi_67_definition: "ker(iota_*) chiral pair generator on A_K projection chi : A_K -> M_2(C); per S86 W-5"
  cocycle_phi_88_definition: "ker(iota_*) Cartan hypercharge generator on A_K projection chi; per S86 W-5"
  regulator_atlas: ["zeta", "Pauli-Villars", "Mellin", "sharp-cutoff"]  # MANDATORY tagging per regulator-pin-discipline.md
  zeta_method: "Res_{s=0} Tr(phi_a · D_K^{-2s})"
  pauli_villars_method: "lim Tr(phi_a · [D_K^2 / (D_K^2 + Lambda^2)]^N) with N=2 subtractions"
  pauli_villars_Lambda_UV: "M_KK = 7.428660036284456e+16 GeV"
  mellin_method: "(1/(2*pi*i)) contour integral around s=0 pole; Mellin-cone substrate-distance-1"
  sharp_cutoff_Lambda_UV: "M_KK"
  class_pin: "FULL"  # full physical regularization, NOT SCHEMATIC; per substrate-first-canonical-sourcing.md §(iv) MANDATORY at K=4
  substrate_canonical_ratio: 7.324992  # Sage-exact at machine precision
  pass_band: 0.001  # 0.1% relative deviation across all 4 regulators
  info_band: 0.01  # 1% relative deviation
  scheme: "4-regulator-atlas-substrate-cocycle-ratio-invariance"
  convention: "regulator-class-invariance-FULL-pin"
  random_seed: N/A
  GPU_path: "torch.linalg for matrix dim >= 100x100"
input_sha_pins:
  canonical_constants_py: <pinned at plan-freeze>
  spectrum_cache_L12_tau019_npz: <pinned at plan-freeze>
  s86_w_5_workshop_md: <pinned at plan-freeze>
  permanent_results_registry_VII_W: <pinned at plan-freeze>
output_4_tuple:
  value: "{ratio_zeta, ratio_PV, ratio_Mellin, ratio_cutoff, max_rel_dev, regulator_class_invariant_bool}"
  scheme: "4-regulator-atlas-substrate-cocycle-ratio-invariance"
  convention: "regulator-class-invariance-FULL-pin"
  L_max: 10
audit_sha256: <computed at runtime via closure_hash(input_pin_map)>
```

### 8. Expected output 4-tuple
- `value`: 6-element record `{ratio_zeta, ratio_PV, ratio_Mellin, ratio_cutoff (4× float64), max_rel_dev (float64), regulator_class_invariant (bool)}`
- `scheme`: `4-regulator-atlas-substrate-cocycle-ratio-invariance`
- `convention`: `regulator-class-invariance-FULL-pin`
- `L_max`: `10`

### 9. PASS/FAIL/INFO thresholds with tolerance rule

- **PASS** iff `max_R rel_dev_R ≤ 0.001` (0.1% across all 4 regulators); regulator-class invariance confirmed.
- **INFO** iff `0.001 < max_R rel_dev_R ≤ 0.01` (between 0.1% and 1%); regulator-class invariance partial — substrate-IS reading supported but full-precision invariance requires extension (e.g., L_max → 12 + Sage-QQ exact computation).
- **FAIL** iff `max_R rel_dev_R > 0.01` (≥ 1% spread); regulator-class invariance VIOLATED — at least one regulator's ‖φ_67‖^R / ‖φ_88‖^R ratio diverges from substrate canonical 7.324992. This would falsify the regulator-axis-INVARIANT reading of substrate cocycle structure.
- **Tolerance rule**: RATIO tolerance ≤ 0.001 for PASS (0.1% per ledger gate criterion); RATIO tolerance ≤ 0.01 for INFO; otherwise FAIL.

### 10. Substitution chain

A.14 has no sign/direction claim requiring pre-registration substitution chain at the plan-block level (it is a numerical match against a Sage-exact substrate canonical, not a directional prediction). The substitution chain for the substrate canonical 7.324992 is documented at S86 W-5 R2-B Convergence #3.

### 11. What PASSES/FAILS MEAN for solution space

- **PASS**: substrate cocycle ratio is regulator-class invariant; the substrate's IS-cocycle structure is regulator-axis-invariant by construction. Lab inheritance falsifier protocol's Class-B cohomology-asymmetry ratio (per `inheritance-falsifier-protocol.md`) inherits the ratio invariance; W-5 ‖φ_67‖/‖φ_88‖ = 7.324992 ± 0.1% prediction is regulator-class robust. Lizzi's "ratios are observables; absolute moments are regulator-dressed" pattern (S82 W-3 §VII.K classification) is structurally confirmed at the cocycle layer.
- **INFO**: regulator-class invariance partial; substrate reading supported but L_max → 12 extension OR Sage-QQ exact arithmetic is required to reach full-precision invariance. Cross-link to A.41 D_max measurement in W6 (Wave 6 forwards a regulator-class baseline from this gate's npz output).
- **FAIL**: regulator-class invariance VIOLATED; the substrate cocycle structure is regulator-axis-DEPENDENT, contradicting the IS-cocycle reading. Either (i) the cocycles φ_67 and φ_88 are not algebra-INVARIANT spectrum-only functionals (they leak state-pair-functional content via algebra-axis orthogonality K-counter MANDATORY at K=3 — `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`), OR (ii) the canonical 7.324992 is regulator-anchored to one specific regulator (e.g., zeta) and not regulator-class invariant. Both readings route to S90 plan-freeze halt with mandatory remediation.

### 12. Effort estimate
**0.6 wave-equivalents** — 4-regulator atlas evaluation at L_max=10 reusing pre-existing spectrum cache; per-regulator cost ~0.15 wave-equivalents.

### 13. Substrate framing per `phononic-framing.md` IS-not-IN

The substrate IS the cocycle structure on `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`. The cocycles φ_67 and φ_88 are intrinsic substrate observables (ker(ι_*) generators of the inheritance morphism); they are NOT fields living "in" some host algebra. The 4-regulator atlas IS a substrate-internal tool: each regulator R produces a definite ‖φ_a‖^R, and regulator-class invariance is the substrate's structural prediction that the RATIO is regulator-axis-invariant even though absolute moments are regulator-dressed.

**FORBIDDEN container-thinking**:
- "Cocycles live IN the algebra"
- "Regulators are a choice we make about how to compute on the substrate"

**REQUIRED substrate-IS framing**:
- The cocycles ARE substrate-intrinsic structural observables.
- The 4-regulator atlas IS a coordinate-chart family on the substrate's spectral-functional axis (lizzi pluralism); regulator-class invariance is the substrate's transition-function consistency condition.

---

## §W3-4. S89-V4-SAGE-QQ-ENUMERATION-EXTENDED-SECTORS  (A.16)

### 1. Gate ID
`S89-V4-SAGE-QQ-ENUMERATION-EXTENDED-SECTORS`

### 2. Trigger
`[VERIFY-THEOREM]` — Sage-QQ exact match between bot20 sector occupation V_4-on-triality character pattern at L_max ∈ {8, 10, 12} and S88 W-7 V.2 V_4-triality workshop's predicted multi-orbit cardinality vector invariance under the cocycle functor F : m(p,q) ↦ Δ_0(m).

### 3. Classification
**GEOMETRIC** — V_4-on-triality character is a substrate spectral-structure observable on the SU(3) Peter-Weyl decomposition; the cocycle functor F operates on the substrate's combinatorial sector occupation. Spans BOTH single-τ-slice (Level-1) AND moduli-deformation (Level-2) substrate-IS levels per `phononic-framing.md §"Single-τ-slice vs moduli-deformation"` K=2 MANDATORY since S88 W-7 V.4.

### 4. Agent type
**Runtime author**: `connes-ncg-theorist` (PRIMARY; V_4 program + cocycle functor F + Sage-QQ exact enumeration is connes-domain — derives from finite-spectral-triple character theory + V_4-on-triality structure on Peter-Weyl decomposition of SU(3)).
**Co-reviewer**: `lizzi-spectral-functional-theorist` (CO-AUTHOR, regulator-class invariance cross-check on character integrals; cocycle norm consistency).
**FORBIDDEN at runtime**: `gen-physicist`.

### 5. Hypothesis
At L_max ∈ {8, 10, 12}, the V_4-on-triality character pattern (⟨χ_tri, g_C⟩, ⟨χ_tri, g_H⟩, ⟨χ_tri, g_M⟩) on bot20 sector occupation matches Sage-QQ exact prediction with Δ_0 = 16 invariant on cover C under cocycle functor F : m(p,q) ↦ Δ_0(m), confirming Level-1 single-τ-slice + Level-2 moduli-deformation substrate-IS simultaneous demonstration.

### 6. Method (self-contained dispatch prompt)

**Script path**: `computations/session-89/s89_w3_v4_sage_qq_enumeration_extended_sectors.py`

**Compute environment**:
- Python: `phonon-exflation-sim/.venv312/Scripts/python.exe`
- `import os; os.environ.setdefault('OMP_NUM_THREADS', '8')` BEFORE `import numpy`
- GPU not required (combinatorial enumeration on bot20 sectors; Peter-Weyl irrep dims ≤ 100 at L_max=12)
- Sage MCP for symbolic computation: `sage_eval` for Sage-QQ Result C anchor verification

**Step-by-step instructions**:

1. Import canonicals: `tau_fold`, `M_KK`. Pin SU(3) triality character: χ_tri(p,q) = (1, ω, ω²) for (p−q) mod 3 ∈ {0, 1, 2} where ω = exp(2πi/3); equivalent V_4 → Z_2 reading is (p−q) mod 3 → Z_2 via `chi_tri(p,q) = +1 if (p-q) mod 3 == 0 else -1` (V_4-on-triality two-fold reading per S88 W-7 V.2).
2. For each L_max ∈ {8, 10, 12}, read D_K spectral cache filtered to L_max (use `s84_spectrum_cache_L12_tau019.npz` at L_max=12; for L_max ∈ {8, 10}, filter the L_max=12 cache).
3. Extract bot20 sector occupation `m(p,q)` at τ_fold = 0.19 (cardinality of each Peter-Weyl (p,q) sector among the bottom-20 D_K eigenvalues).
4. Compute V_4-on-triality character inner products on cover C, H, M:
   - ⟨χ_tri, g_C⟩ = Σ_{(p,q) ∈ cover C} m(p,q) · χ_tri(p,q)
   - ⟨χ_tri, g_H⟩ = Σ_{(p,q) ∈ cover H} m(p,q) · χ_tri(p,q)
   - ⟨χ_tri, g_M⟩ = Σ_{(p,q) ∈ cover M} m(p,q) · χ_tri(p,q)
   where covers C, H, M are the three multi-orbit covers per S88 W-7 V.2 V_4-triality workshop §V.4.
5. Compute Δ_0 = 4·c_{σ⁻¹((-1,-1))} per S88 W-2 W2-8 §VII.AD localization formula on cover C; expected value Δ_0 = 16 on cover C invariant under cocycle functor F (Sage-QQ Result C summary per S88 W-7 V.4).
6. Cross-check Sage-QQ exact match: invoke Sage MCP `sage_eval` for Result C anchor `Delta_0_cover_C = 16` and per-cover character pattern; emit Sage-QQ exact verdict.
7. Verify Level-1 substrate-IS at single-τ-slice = τ_fold = 0.19: bot20 sector occupation m(p,q) is intrinsic to the spectral triple `(A_K, H_K, D_K(τ_fold))`; declare Level-1 in JSON metadata.
8. Verify Level-2 substrate-IS at moduli-deformation: per S88 W-7 V.4, bot20 sector occupation lifts to Level-2 invariant under cocycle functor F across V_4-triality multi-orbit deformation; declare Level-2 in JSON metadata.
9. Cross-check L_max-stability: pattern (⟨χ_tri, g_C⟩, ⟨χ_tri, g_H⟩, ⟨χ_tri, g_M⟩) at L_max=8 → 10 → 12 should converge (substrate-IS Level-1 stability per `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"`).
10. Emit:
    - NPZ sidecar with per-L_max character inner products, Δ_0 cover C value, Sage-QQ exact verdict, Level-1 / Level-2 declarations.
    - PNG plot showing character pattern across L_max ∈ {8, 10, 12} with Sage-QQ Result C anchor Δ_0 = 16 line annotated.
    - JSON metadata with Level-1 + Level-2 substrate-IS declarations per `phononic-framing.md` MANDATORY at K=2.
    - Verdict line per Schema-v2 in `computations/session-89/s89_gate_verdicts.txt`.

**Input SHA-256 pins**:
- `canonical_constants.py` — `<pinned at plan-freeze>`
- `computations/_shared/s84_spectrum_cache_L12_tau019.npz` — `<pinned at plan-freeze>`
- `sessions/archive/session-88/workshops/s88-w7-w2-2-v4-triality.md` — `<pinned at plan-freeze>` (W-7 V.2 + V.4 source)
- `sessions/permanent-results-registry.md §VII.AE` — `<pinned at plan-freeze>` (S88 W2-9 moduli-space τ-asymmetry, Level-2 calibration anchor)

**Cross-checks**:
- Sage-QQ exact match for Δ_0 = 16 on cover C (MANDATORY)
- Level-1 single-τ-slice + Level-2 moduli-deformation declaration per `phononic-framing.md` (MANDATORY at K=2)
- L_max stability convergence pattern (MANDATORY per `math-scripts.md §"D_K Block-Diagonality"`)
- V_4-on-triality character symmetry: ⟨χ_tri, g_C⟩ + ⟨χ_tri, g_H⟩ + ⟨χ_tri, g_M⟩ should sum to Σ_{(p,q)} m(p,q) · χ_tri(p,q) = global character integral (MANDATORY consistency check)

### 7. Machinery pin (PRDR)

```yaml
gate_id: S89-V4-SAGE-QQ-ENUMERATION-EXTENDED-SECTORS
schema_version: R3
trigger: VERIFY-THEOREM
classification: GEOMETRIC
machinery_pin_map:
  tau_evaluate: 0.19  # tau_fold (R-PROTECTED)
  L_max_scan: [8, 10, 12]
  triality_character_definition: "chi_tri(p,q) = +1 if (p-q) mod 3 == 0 else -1 (V_4 -> Z_2 reading per S88 W-7 V.2)"
  bot20_extraction: "bottom-20 |D_K| eigenvalues at tau_fold, sector-decomposed via Peter-Weyl block-diagonality"
  cover_definitions: "covers C, H, M per S88 W-7 V.2 V_4-triality workshop §V.4"
  delta_0_formula: "4 * c_{sigma^{-1}((-1, -1))} on cover C per S88 W-2 W2-8 §VII.AD localization formula"
  delta_0_cover_C_predicted: 16  # Sage-QQ Result C summary per S88 W-7 V.4
  cocycle_functor_F: "F : m(p,q) -> Delta_0(m); invariance under V_4-triality multi-orbit deformation"
  level_1_substrate_IS: "single-tau-slice at tau_fold = 0.19; intrinsic to (A_K, H_K, D_K(tau_fold))"
  level_2_substrate_IS: "moduli-deformation invariance under cocycle functor F across V_4-triality multi-orbit"
  sage_qq_method: "sage_eval via MCP for Result C anchor Delta_0_cover_C = 16"
  scheme: "V_4-triality-Sage-QQ-enumeration-extended-sectors"
  convention: "L_max-scan-bot20-sector-occupation-cocycle-functor-F-invariance"
  random_seed: N/A
  GPU_path: "N/A; combinatorial enumeration on bot20 sectors"
input_sha_pins:
  canonical_constants_py: <pinned at plan-freeze>
  spectrum_cache_L12_tau019_npz: <pinned at plan-freeze>
  s88_w7_w2_2_v4_triality_md: <pinned at plan-freeze>
  permanent_results_registry_VII_AE: <pinned at plan-freeze>
output_4_tuple:
  value: "{character_pattern_L8, character_pattern_L10, character_pattern_L12, delta_0_cover_C, sage_qq_exact_match_bool}"
  scheme: "V_4-triality-Sage-QQ-enumeration-extended-sectors"
  convention: "L_max-scan-bot20-sector-occupation-cocycle-functor-F-invariance"
  L_max: 12
audit_sha256: <computed at runtime via closure_hash(input_pin_map)>
```

### 8. Expected output 4-tuple
- `value`: 5-element record `{character_pattern_L8 (3-tuple of int or Sage-Q), character_pattern_L10 (3-tuple), character_pattern_L12 (3-tuple), delta_0_cover_C (int = 16 expected), sage_qq_exact_match (bool)}`
- `scheme`: `V_4-triality-Sage-QQ-enumeration-extended-sectors`
- `convention`: `L_max-scan-bot20-sector-occupation-cocycle-functor-F-invariance`
- `L_max`: `12`

### 9. PASS/FAIL/INFO thresholds with tolerance rule

- **PASS** iff:
  - (a) `delta_0_cover_C == 16` EXACTLY at L_max ∈ {10, 12} (Sage-QQ Result C anchor satisfied; Level-2 invariance under cocycle functor F).
  - (b) Character pattern (⟨χ_tri, g_C⟩, ⟨χ_tri, g_H⟩, ⟨χ_tri, g_M⟩) at L_max ∈ {10, 12} matches Sage-QQ predicted multi-orbit pattern bit-exactly (Sage-QQ exact match via MCP).
  - (c) Cardinality vector (m(p,q) sums on bot20) is INVARIANT across L_max ∈ {10, 12} per Level-1 stability (per S88 W2-6 partition stability).
  - (d) Level-1 + Level-2 substrate-IS declarations present in JSON metadata.
- **INFO** iff:
  - (a) holds at L_max=12 but partial at L_max ∈ {8, 10} (truncation effect; substrate-IS reading supported but extension required).
  - (b) holds within Sage-QQ-induced rounding tolerance < 0.01 (numerical precision floor).
  - (c) and (d) hold.
- **FAIL** iff:
  - (a) fails at L_max ∈ {10, 12} (Δ_0 ≠ 16; cocycle functor F invariance VIOLATED).
  - OR (b) fails (character pattern does not match Sage-QQ prediction; W-7 V.2 prediction falsified).
- **Tolerance rule**: THEOREM (bit-exact Sage-QQ) for (a) and (b); ABSOLUTE invariance for (c) (cardinality vector identical); presence test for (d).

### 10. Substitution chain

A.16 is a Sage-QQ exact theorem-matching gate; the substitution chain for Δ_0 = 16 on cover C is documented at S88 W-7 V.4 V_4-triality workshop §V.4 Result C summary. No additional sign/direction claim requiring pre-registration substitution chain at the plan-block level.

### 11. What PASSES/FAILS MEAN for solution space

- **PASS**: V_4-on-triality cocycle functor F invariance is structurally confirmed at extended L_max sectors; substrate-IS reading at BOTH Level-1 (single-τ-slice intrinsic spectral triple) AND Level-2 (moduli-deformation invariance) is simultaneously demonstrated. K-counter advancement on `phononic-framing.md §"Single-τ-slice vs moduli-deformation"` corpus (K=2 → K=3 MANDATORY). The substrate's V_4-triality structure is regulator-class-INVARIANT and L_max-stable; downstream cross-pillar bridge candidates citing V_4-on-triality become registry-eligible per the 5-anatomy + 3-level discipline.
- **INFO**: Sage-QQ exact match holds at L_max=12 but truncation effects at L_max ∈ {8, 10}; substrate-IS reading partially supported, requires L_max=14 extension. Cross-link to `math-scripts.md §"Friedrich-Bär saturation"` for L_max → ∞ lift.
- **FAIL**: cocycle functor F invariance VIOLATED; either (i) Sage-QQ Result C anchor Δ_0 = 16 was wrongly computed at S88 W-7 V.4 (workshop result challenge) OR (ii) bot20 sector occupation m(p,q) is L_max-DEPENDENT in a way that breaks the cocycle-functor-F lift. Both readings route to S90 plan-freeze halt with mandatory remediation citing V_4-on-triality workshop derivation.

### 12. Effort estimate
**0.6 wave-equivalents** — 3-L_max combinatorial enumeration on bot20 sectors + Sage-QQ exact match + Level-1 / Level-2 declarations.

### 13. Substrate framing per `phononic-framing.md` IS-not-IN

**Level-1 declaration** (single-τ-slice substrate-IS): at fixed τ = τ_fold = 0.19, the substrate IS the spectral triple `(A_K, H_K, D_K(τ_fold))`. Bot20 sector occupation m(p,q) is intrinsic to this spectral triple; the V_4-on-triality character is the substrate's own Peter-Weyl decomposition structure.

**Level-2 declaration** (moduli-deformation substrate-IS): the set of τ values `{(A_K, H_K, D_K(τ)) : τ ∈ moduli-space}` is itself a substrate-IS object; bot20 sector occupation INVARIANT under cocycle functor F across V_4-triality multi-orbit deformation IS the substrate's own moduli-space invariance.

**FORBIDDEN container-thinking**:
- "Sectors live IN the SU(3) representation theory"
- "V_4 acts ON the substrate"
- "The cocycle functor F maps the substrate INTO another structure"

**REQUIRED substrate-IS framing**:
- Sectors ARE the substrate's spectral content (Peter-Weyl block-diagonality is intrinsic).
- V_4-triality IS the substrate's intrinsic Z_2 grading on (p−q) mod 3; not an external action.
- Cocycle functor F IS the substrate's intrinsic moduli-deformation invariance test.

---

## §W3-5. S89-SUBSTRATE-CLOCK-CANCELLATION-DISCRIMINATING-PREDICATE-GATE  (A.17)

### 1. Gate ID
`S89-SUBSTRATE-CLOCK-CANCELLATION-DISCRIMINATING-PREDICATE-GATE`

### 2. Trigger
`[SIGN]` + `[VERIFY]` — pre-registered Δ(g=322) ≈ 290.80 OOM cancellation under Pinning-A (substrate-clock canonical) AND Pinning-A vs Pinning-B discriminating predicate; Schema-v2 3-tuple companion comment row required (sign_verdict / magnitude_verdict / regime_verdict).

### 3. Classification
**PHONONIC** — substrate-clock IS the substrate's intrinsic temporal structure for the lock cascade; cancellation predicate at g=322 tests substrate-clock vs mode-density alternative pinning, both of which describe the substrate's intrinsic cascade dynamics. The lock cascade IS the substrate's deformation through cascade generations; it is phononic substrate dynamics (not a propagating-excitation-on-background gate).

### 4. Agent type
**Runtime author**: `volovik-superfluid-universe-theorist` (PRIMARY; substrate-clock + lock cascade is Volovik's domain — cosmological clock structure on the substrate's superfluid-analog deformation).
**Co-reviewer**: `landau-condensed-matter-theorist` (CO-AUTHOR, condensed-matter-analog cross-check on lock cascade dynamics).
**FORBIDDEN at runtime**: `gen-physicist`, `hawking-theorist` (both default to container-thinking on cosmological clock structure).

### 5. Hypothesis
The substrate-clock canonical Pinning-A (`a_substrate(g) ~ L_pix(g)`) produces Δ(g=322) ≈ 290.80 OOM cancellation on the lock cascade observable at g=322, AND mode-density Pinning-B FAILS the same cancellation predicate, demonstrating that substrate-clock vs mode-density readings are DISCRIMINATING (not equivalent up to convention).

### 6. Method (self-contained dispatch prompt)

**Script path**: `computations/session-89/s89_w3_substrate_clock_cancellation_discriminating_predicate.py`

**Compute environment**:
- Python: `phonon-exflation-sim/.venv312/Scripts/python.exe`
- `import os; os.environ.setdefault('OMP_NUM_THREADS', '8')` BEFORE `import numpy`
- GPU not required (closed-form OOM evaluation; substrate-clock is a scalar function of g)
- `from canonical_constants import *` (MANDATORY)

**Step-by-step instructions**:

1. Import canonicals: `tau_fold`, `M_KK`, `Delta_BCS`. Define substrate-clock canonical Pinning-A: `a_substrate(g) = L_pix(g)`, where `L_pix(g)` is the pixelation lock length at cascade generation g (per S88 W-1 substrate-clock cancellation workshop).
2. Define mode-density alternative Pinning-B: `a_mode(g) = N_modes(g)^{1/d_eff}`, where N_modes(g) is the substrate mode count at generation g and d_eff is the effective dimension at τ_fold (HK-5(τ_fold) baseline).
3. Read S88 W-1 substrate-clock cancellation workshop source `sessions/archive/session-88/workshops/s88-w1-substrate-clock-cancellation.md` §7 CF-W1-WS1-A for cancellation predicate definition: Δ(g) := log10(a_substrate(g) · CASCADE_TAIL_COEFF(g)) − log10(a_baseline(g) · CASCADE_TAIL_COEFF(g)) at the lock-cascade observable.
4. For each pinning P ∈ {A, B} and each g ∈ {143, 322, 384}:
   - Compute Δ_P(g) = log10(numerator_P(g)) − log10(denominator_P(g)).
   - Pin Δ_P(g) at bit-exact float64.
5. Verify SIGN predicate: at Pinning-A, Δ(g=322) ≈ +290.80 OOM (positive, as pre-registered per S88 W-1 §7 CF-W1-WS1-A). At Pinning-B, Δ(g=322) should DIFFER (either different sign or different magnitude OOM).
6. Verify MAGNITUDE predicate: |Δ_A(g=322) − 290.80| / 290.80 ≤ 0.01 (1% relative match against pre-registration).
7. Verify DISCRIMINATING predicate: |Δ_A(g=322) − Δ_B(g=322)| / max(|Δ_A|, |Δ_B|) ≥ 0.05 (5% structural difference between Pinning-A and Pinning-B; Pinnings are not convention-equivalent).
8. Verify regime: substrate-clock Pinning-A is well-defined throughout g ∈ {143, 322, 384} (regime VALID); if any g exits the lock-cascade regime, regime_verdict = MARGINAL or BREAKDOWN per `gate-verdicts.md` Schema-v2.
9. Substitution chain for SIGN claim (per `math-scripts.md §"Double-Check Logic Before Compute"`):
   ```
   Step 1: a_substrate(g) := L_pix(g)  [definition; Pinning-A canonical]
   Step 2: numerator_A(g) := a_substrate(g) · CASCADE_TAIL_COEFF(g)
            denominator_A(g) := a_baseline(g) · CASCADE_TAIL_COEFF(g)
   Step 3: At g=322, Pinning-A canonical predicts a_substrate(322) >> a_baseline(322) per substrate-clock pixelation-lock structure (S88 W-1 derivation).
   Step 4: Δ_A(322) = log10(L_pix(322) / a_baseline(322)) ≈ +290.80 OOM (S88 W-1 pre-registration)
   Step 5: SIGN = positive; MAGNITUDE ≈ 290.80 OOM at Pinning-A.
   ```
10. Emit:
    - NPZ sidecar with Δ_A(g) and Δ_B(g) at all 3 g values, sign_verdict, magnitude_verdict, regime_verdict, discriminating predicate verdict.
    - PNG plot showing Δ_A and Δ_B across g ∈ {143, 322, 384} with pre-registered 290.80 OOM line annotated.
    - JSON metadata with substitution chain documented.
    - Verdict line per Schema-v2 in `computations/session-89/s89_gate_verdicts.txt` WITH:
      - First canonical line: `S89-SUBSTRATE-CLOCK-CANCELLATION-DISCRIMINATING-PREDICATE-GATE: PASS|FAIL|INFO -- value='{Δ_A(322)}' scheme=substrate-clock-pinning-A-vs-mode-density-pinning-B convention=g-scan-143-322-384 L_max=N/A audit_sha256=... content_sha256=... schema_version=S87+`
      - Dual-SHA companion comment row (W9a-99 split standard)
      - **SIGN/MAGNITUDE/REGIME 3-tuple companion comment row** (Schema-v2 MANDATORY for [SIGN] trigger):
        `# sign_verdict={PASS|FAIL|N/A} magnitude_verdict={PASS|INFO|FAIL} regime_verdict={VALID|MARGINAL|BREAKDOWN} # S89-SUBSTRATE-CLOCK-CANCELLATION-DISCRIMINATING-PREDICATE-GATE 3-tuple annotation (S87 schema-v2)`

**Input SHA-256 pins**:
- `canonical_constants.py` — `<pinned at plan-freeze>`
- `sessions/archive/session-88/workshops/s88-w1-substrate-clock-cancellation.md` — `<pinned at plan-freeze>` (W-1 §7 CF-W1-WS1-A source)
- `sessions/permanent-results-registry.md` (if substrate-clock canonical entry exists) — `<pinned at plan-freeze>`

**Cross-checks**:
- Substitution chain for SIGN claim (MANDATORY per `math-scripts.md §"Double-Check Logic"`)
- DISCRIMINATING predicate (MANDATORY for PASS; Pinning-A and Pinning-B must differ structurally)
- Regime verdict (MANDATORY per Schema-v2)
- Pinning-A and Pinning-B definitions explicit at plan-freeze (MANDATORY per ledger gate criterion)

### 7. Machinery pin (PRDR)

```yaml
gate_id: S89-SUBSTRATE-CLOCK-CANCELLATION-DISCRIMINATING-PREDICATE-GATE
schema_version: R3
trigger: SIGN+VERIFY
classification: PHONONIC
machinery_pin_map:
  pinning_A_definition: "a_substrate(g) = L_pix(g) (substrate-clock canonical; pixelation-lock length per S88 W-1)"
  pinning_B_definition: "a_mode(g) = N_modes(g)^(1/d_eff) (mode-density alternative; d_eff = HK-5(tau_fold))"
  g_scan: [143, 322, 384]
  cancellation_observable: "Delta(g) = log10(numerator(g)) - log10(denominator(g)) at lock-cascade observable per S88 W-1 §7 CF-W1-WS1-A"
  pre_registered_Delta_A_322: 290.80  # OOM, per S88 W-1 §7 CF-W1-WS1-A
  pass_band_magnitude: 0.01  # 1% relative match
  pass_band_discriminating: 0.05  # 5% structural difference between Pinning-A and Pinning-B
  scheme: "substrate-clock-pinning-A-vs-mode-density-pinning-B"
  convention: "g-scan-143-322-384"
  random_seed: N/A
  GPU_path: "N/A; closed-form OOM evaluation"
input_sha_pins:
  canonical_constants_py: <pinned at plan-freeze>
  s88_w1_substrate_clock_cancellation_md: <pinned at plan-freeze>
  permanent_results_registry: <pinned at plan-freeze>
output_4_tuple:
  value: "{Delta_A(143), Delta_A(322), Delta_A(384), Delta_B(143), Delta_B(322), Delta_B(384), discriminating_bool, sign_verdict, magnitude_verdict, regime_verdict}"
  scheme: "substrate-clock-pinning-A-vs-mode-density-pinning-B"
  convention: "g-scan-143-322-384"
  L_max: N/A
audit_sha256: <computed at runtime via closure_hash(input_pin_map)>
```

### 8. Expected output 4-tuple
- `value`: 10-element record `{Δ_A(143), Δ_A(322), Δ_A(384), Δ_B(143), Δ_B(322), Δ_B(384) (6× float64), discriminating (bool), sign_verdict, magnitude_verdict, regime_verdict (3× enum)}`
- `scheme`: `substrate-clock-pinning-A-vs-mode-density-pinning-B`
- `convention`: `g-scan-143-322-384`
- `L_max`: `N/A` (substrate-clock observable is not L_max-dependent)

### 9. PASS/FAIL/INFO thresholds with tolerance rule

- **PASS** iff:
  - (a) `sign_verdict == PASS` (Δ_A(322) > 0, matching pre-registered direction).
  - (b) `magnitude_verdict == PASS` (|Δ_A(322) − 290.80| / 290.80 ≤ 0.01; 1% magnitude match).
  - (c) `discriminating == True` (|Δ_A(322) − Δ_B(322)| / max(|Δ_A|, |Δ_B|) ≥ 0.05).
  - (d) `regime_verdict == VALID` (Pinning-A well-defined throughout g scan).
  - Composite collapse rule per `gate-verdicts.md`: all 4 PASS → composite PASS.
- **INFO** iff:
  - (a) PASS, (b) INFO (1% < magnitude band ≤ 10%), (c) PASS, (d) VALID or MARGINAL.
  - Composite: magnitude_verdict=INFO + regime=VALID → composite INFO.
- **FAIL** iff:
  - (a) FAIL (sign mismatch — Δ_A(322) negative or zero) OR
  - (c) FAIL (Pinning-A and Pinning-B not discriminating; |Δ_A − Δ_B| < 5%) OR
  - regime BREAKDOWN.
  - Per Schema-v2 collapse: regime BREAKDOWN → FAIL regardless; sign FAIL → FAIL; magnitude FAIL + regime VALID → FAIL.
- **Tolerance rule**: ABSOLUTE for sign (sign(Δ_A(322)) > 0); RATIO for magnitude (≤1% PASS, ≤10% INFO); RATIO for discriminating (≥5% PASS); per Schema-v2 composite collapse rule.

### 10. Substitution chain (MANDATORY for SIGN claim)

```
Definitions:
  L_pix(g)               = pixelation-lock length at cascade generation g (per S88 W-1)
  a_substrate(g)         = L_pix(g) [Pinning-A canonical]
  CASCADE_TAIL_COEFF(g) = cascade-tail coefficient, common to numerator and denominator of Δ
  Δ_A(g)                = log10(a_substrate(g) · CASCADE_TAIL_COEFF(g)) − log10(a_baseline(g) · CASCADE_TAIL_COEFF(g))
                         = log10(L_pix(g)) − log10(a_baseline(g))    [CASCADE_TAIL_COEFF cancels]
  a_baseline(g)         = the cascade-baseline normalizer at generation g (Volovik partition canonical)

Substitutions at g = 322:
  Step 1: L_pix(322) ~ 10^(290.80) · a_baseline(322)
                     [from S88 W-1 substrate-clock derivation; pixelation-lock length at g=322
                      grows by 290.80 OOM relative to baseline due to lock-cascade structure]
  Step 2: Δ_A(322) = log10(L_pix(322) / a_baseline(322))
                   = log10(10^(290.80))
                   = +290.80 OOM
  Step 3: At Pinning-B, a_mode(322) = N_modes(322)^(1/d_eff) ~ N_modes(322)^(1/HK-5(0.19))
          where N_modes(322) ~ 10^(α · 322) for some sub-exponent α << 1 in the substrate's mode-density scaling.
          The OOM growth of a_mode(322) is bounded by 322·α·log10(e)/d_eff << 290.80.
  Step 4: Δ_B(322) = log10(a_mode(322) / a_baseline(322))
                   = (322·α/d_eff) · log10(e) − log10(a_baseline(322)) << 290.80 OOM
  Step 5: SIGN = positive at both Pinning-A and Pinning-B (both numerators dominate baseline).
          MAGNITUDE: Δ_A(322) ≈ +290.80 OOM; Δ_B(322) << 290.80 OOM (typically order(10) OOM).
          DISCRIMINATING: |Δ_A − Δ_B| / |Δ_A| ≈ 1 (∼100% structural difference), well above 5% PASS threshold.
Conclusion: SIGN = positive, MAGNITUDE ≈ 290.80 OOM at Pinning-A,
            and Pinning-A vs Pinning-B is DISCRIMINATING by construction.
```

### 11. What PASSES/FAILS MEAN for solution space

- **PASS**: substrate-clock canonical Pinning-A is the structurally-correct cosmological clock for the lock cascade; mode-density Pinning-B is FALSIFIED at the cancellation predicate. Cross-link to A.18 uniqueness derivation (next gate): A.17 PASS supplies empirical evidence for A.18's substrate-clock uniqueness theorem.
- **INFO**: sign correct + discriminating but magnitude partial; substrate-clock reading supported but pre-registered 290.80 OOM may need sharpening (substitution chain may have an O(1) correction). Cross-link to A.18 uniqueness derivation as deferred.
- **FAIL**: substrate-clock Pinning-A is FALSIFIED OR Pinning-A vs Pinning-B is NOT DISCRIMINATING (i.e., the two pinnings are convention-equivalent up to overall normalization). Either reading routes to S90 plan-freeze halt with mandatory remediation citing S88 W-1 substrate-clock derivation.

### 12. Effort estimate
**0.4 wave-equivalents** — closed-form OOM evaluation; no spectrum cache reload; runs as scalar computation per g.

### 13. Substrate framing per `phononic-framing.md` IS-not-IN

The substrate-clock IS the substrate's intrinsic temporal structure for the lock cascade. `a_substrate(g) ~ L_pix(g)` IS the substrate's pixelation-lock length at cascade generation g — it is NOT a clock that "ticks IN" some external time container. The lock cascade IS the substrate's own deformation through generations; substrate clock pinning IS choosing the substrate-natural unit for this deformation.

**FORBIDDEN container-thinking**:
- "The substrate evolves IN cosmological time"
- "Pinning-A is a clock attached TO the substrate"
- "The lock cascade unfolds IN time as g increases"

**REQUIRED substrate-IS framing**:
- The substrate IS the lock cascade; cascade generations g are the substrate's intrinsic deformation parameter.
- Substrate-clock IS the substrate's own pixelation-lock length L_pix(g), which scales with g via the substrate-IS lock-cascade dynamics.
- Pinning-A vs Pinning-B is choosing among substrate-natural temporal coordinates; cancellation predicate tests which coordinate is intrinsic.

---

## §W3-6. S89-SUBSTRATE-CLOCK-PINNING-UNIQUENESS-DERIVATION  (A.18)

### 1. Gate ID
`S89-SUBSTRATE-CLOCK-PINNING-UNIQUENESS-DERIVATION`

### 2. Trigger
`[VERIFY-THEOREM]` — first-principles derivation that `a_substrate(g) ~ L_pix(g)` is THE unique substrate-natural clock for the lock cascade (uniqueness theorem program); PASS predicate is theorem-form (uniqueness proof) OR INFO if multiple candidates survive the substrate-naturalness criterion.

### 3. Classification
**PHONONIC** — substrate-clock uniqueness is a structural property of the substrate's lock-cascade dynamics; the substrate IS the lock cascade and substrate-clock IS the substrate's intrinsic temporal coordinate. This is phononic substrate dynamics (cascade generation evolution = substrate intrinsic deformation).

### 4. Agent type
**Runtime author**: `volovik-superfluid-universe-theorist` (PRIMARY; substrate-clock + uniqueness theorem program is Volovik's domain — superfluid-analog cosmological clock structure).
**Co-reviewer**: `landau-condensed-matter-theorist` (CO-AUTHOR, condensed-matter analog cross-check on alternative pinning candidates).
**FORBIDDEN at runtime**: `gen-physicist`, `hawking-theorist` (container-thinking on cosmological clock).

### 5. Hypothesis
`a_substrate(g) ~ L_pix(g)` (the pixelation-lock length per cascade generation) is THE unique substrate-natural clock for the lock cascade, with uniqueness derivable from substrate-naturalness criteria (regulator-class invariance + substrate-IS Level-1 + Level-2 invariance + minimality of free parameters + cancellation-discriminating predicate per A.17).

### 6. Method (self-contained dispatch prompt)

**Script path**: `computations/session-89/s89_w3_substrate_clock_pinning_uniqueness_derivation.py`

**Compute environment**:
- Python: `phonon-exflation-sim/.venv312/Scripts/python.exe`
- `import os; os.environ.setdefault('OMP_NUM_THREADS', '8')` BEFORE `import numpy`
- GPU not required (theorem-form derivation; numerical verification of candidate-pinning properties at finite L_max)
- `from canonical_constants import *` (MANDATORY)

**Step-by-step instructions**:

1. Import canonicals: `tau_fold`, `M_KK`, `Delta_BCS`, `xi_E_GGE_inv`. Read S88 W-1 substrate-clock pinning candidates from `sessions/archive/session-88/workshops/s88-w1-substrate-clock-cancellation.md` §7 CF-W1-WS1-C.
2. Enumerate substrate-clock pinning candidates {P_1, P_2, ..., P_N} (typically N ∈ {3, 5, 7} per S88 W-1 candidate space):
   - **P_1**: a_substrate(g) = L_pix(g) (Pinning-A canonical; pixelation-lock length)
   - **P_2**: a_mode(g) = N_modes(g)^(1/d_eff) (Pinning-B mode-density)
   - **P_3**: a_GGE(g) = ξ_E_GGE_inv · (1 + g/G_critical) (GGE-anchored)
   - **P_4** (and beyond): per S88 W-1 enumeration
3. Define substrate-naturalness criteria (uniqueness criteria):
   - **C1 — Regulator-class invariance**: a_P(g) is invariant under {ζ, Pauli-Villars, Mellin, sharp-cutoff} regulator scan (per `regulator-pin-discipline.md`).
   - **C2 — Level-1 substrate-IS**: a_P(g) is intrinsic to the spectral triple at fixed τ-slice (no external geometric input).
   - **C3 — Level-2 substrate-IS**: a_P(g) is moduli-deformation invariant or transforms covariantly under cocycle functor F (per `phononic-framing.md` Level-1 vs Level-2 K=2 MANDATORY).
   - **C4 — Minimality**: a_P(g) has no free parameters beyond substrate canonicals (M_KK, Delta_BCS, tau_fold, xi_E_GGE_inv).
   - **C5 — Cancellation-discriminating predicate**: a_P(g) PASSES the A.17 discriminating predicate (Δ(g=322) ≈ 290.80 OOM at the canonical reading).
4. For each candidate P_i, evaluate satisfaction of {C1, C2, C3, C4, C5}:
   - C1: scan {ζ, Pauli-Villars, Mellin, sharp-cutoff} (cross-link to A.14 regulator-class invariance scan); compute relative deviation max_R rel_dev_R.
   - C2: declare Level-1 single-τ-slice intrinsicity; no external geometric input means a_P(g) is computable from `(A_K, H_K, D_K(τ_fold))` alone.
   - C3: compute under cocycle functor F (cross-link to A.16 V_4 enumeration); Level-2 invariance OR covariance.
   - C4: enumerate free parameters of a_P(g) explicitly; minimality is satisfied if free parameters ⊆ {M_KK, Delta_BCS, tau_fold, xi_E_GGE_inv}.
   - C5: at canonical reading of P_i, compute Δ(g=322); satisfies if magnitude PASSes the A.17 pre-registered band.
5. Rank candidates by criterion satisfaction count (5/5 → C1∧C2∧C3∧C4∧C5; 4/5 partial; etc.). Apply uniqueness theorem: P_i is THE unique substrate-natural clock iff P_i satisfies all 5 criteria AND no other candidate satisfies all 5.
6. Verify P_1 (`a_substrate(g) = L_pix(g)`) satisfies all 5 criteria:
   - C1: cross-link to A.14 PASS (cocycle ratio regulator-class invariance) implies pixelation-lock-length regulator-class invariance via the substrate's pixelation-lock derivation chain (substrate-IS spectral mass scale derived from cocycle-invariant moments).
   - C2: L_pix(g) is intrinsic to the substrate's spectral triple at τ_fold (computable from D_K spectrum at L_max ≤ 10).
   - C3: L_pix(g) is moduli-deformation invariant under the cocycle functor F (Level-2 invariance from V_4-triality consistency).
   - C4: L_pix(g) has substrate canonicals M_KK + Delta_BCS + tau_fold; no free parameters.
   - C5: A.17 PASS (or A.17 INFO; if A.17 FAILs, A.18 cannot promote to PASS).
7. Verify other candidates fail at least one criterion:
   - P_2 (mode-density): C5 FAILs per A.17 substitution chain (Δ_B(322) << 290.80 OOM).
   - P_3 (GGE-anchored): C4 FAILs (introduces G_critical free parameter NOT in substrate canonicals).
   - P_4+: similar disqualification per S88 W-1 candidate space.
8. Emit uniqueness verdict:
   - **PASS** iff P_1 satisfies all 5 criteria AND no other candidate satisfies all 5.
   - **INFO** iff P_1 satisfies all 5 criteria but ≥1 other candidate also satisfies all 5 (multiple substrate-natural clocks survive; uniqueness fails).
   - **FAIL** iff P_1 fails ≥1 criterion (substrate-clock canonical Pinning-A is NOT substrate-natural).
9. Cross-check uniqueness theorem against S86 framework lessons: the substrate has unique canonicals (KO-dim=6, [J,D_K]=0 CPT, etc.) per the framework's PROVEN structural results. Substrate-clock uniqueness extends this list IF PASS.
10. Emit:
    - JSON sidecar with per-candidate criterion-satisfaction matrix, uniqueness verdict, ranking.
    - Markdown sidecar with verbose uniqueness theorem proof (substrate-naturalness criteria + per-candidate evaluation + minimality argument).
    - Verdict line per Schema-v2 in `computations/session-89/s89_gate_verdicts.txt`.

**Input SHA-256 pins**:
- `canonical_constants.py` — `<pinned at plan-freeze>`
- `sessions/archive/session-88/workshops/s88-w1-substrate-clock-cancellation.md` — `<pinned at plan-freeze>` (W-1 §7 CF-W1-WS1-C source)
- `computations/session-89/s89_w3_substrate_clock_cancellation_discriminating_predicate.py` output (A.17 NPZ) — `<computed-at-runtime>` (A.17 PASS/INFO required for A.18 PASS)
- `computations/session-89/s89_w3_substrate_cocycle_ratio_regulator_class_invariance_scan.py` output (A.14 NPZ) — `<computed-at-runtime>` (A.14 PASS for C1)
- `computations/session-89/s89_w3_v4_sage_qq_enumeration_extended_sectors.py` output (A.16 NPZ) — `<computed-at-runtime>` (A.16 PASS for C3)

**Cross-checks**:
- Per-candidate criterion-satisfaction matrix (MANDATORY)
- Cross-link to A.14 (C1 regulator-class invariance), A.16 (C3 Level-2 invariance), A.17 (C5 cancellation-discriminating predicate) — all 3 must be available at A.18 dispatch
- Minimality argument explicit (MANDATORY per `agent-standards.md §"Formal Rigor"`)
- Substrate-naturalness criteria documented in markdown sidecar (MANDATORY)

### 7. Machinery pin (PRDR)

```yaml
gate_id: S89-SUBSTRATE-CLOCK-PINNING-UNIQUENESS-DERIVATION
schema_version: R3
trigger: VERIFY-THEOREM
classification: PHONONIC
machinery_pin_map:
  candidate_pinnings: ["P_1: a_substrate(g) = L_pix(g)", "P_2: a_mode(g) = N_modes(g)^(1/d_eff)", "P_3: a_GGE(g) = xi_E_GGE_inv · (1 + g/G_critical)", "P_4+: per S88 W-1 §7 CF-W1-WS1-C"]
  uniqueness_criteria:
    C1: "regulator-class invariance under {zeta, Pauli-Villars, Mellin, sharp-cutoff}"
    C2: "Level-1 substrate-IS at fixed tau-slice (no external geometric input)"
    C3: "Level-2 substrate-IS moduli-deformation invariance under cocycle functor F"
    C4: "minimality of free parameters (subset of {M_KK, Delta_BCS, tau_fold, xi_E_GGE_inv})"
    C5: "cancellation-discriminating predicate passes A.17 reading"
  cross_links:
    A_14: "cocycle ratio regulator-class invariance (provides C1 evidence for P_1)"
    A_16: "V_4 Sage-QQ enumeration extended sectors (provides C3 evidence for P_1)"
    A_17: "substrate-clock cancellation discriminating predicate (provides C5 evidence for P_1)"
  scheme: "substrate-clock-pinning-uniqueness-derivation-5-criteria"
  convention: "L-pix-canonical-vs-mode-density-vs-GGE-anchored-candidate-space"
  random_seed: N/A
  GPU_path: "N/A; theorem-form derivation"
input_sha_pins:
  canonical_constants_py: <pinned at plan-freeze>
  s88_w1_substrate_clock_md: <pinned at plan-freeze>
  A_17_npz: <computed-at-runtime>
  A_14_npz: <computed-at-runtime>
  A_16_npz: <computed-at-runtime>
output_4_tuple:
  value: "{P_uniqueness_verdict (P_1 unique | multiple-candidates | none), criterion_satisfaction_matrix (N_candidates × 5), ranking (top-3 by satisfaction count), markdown_proof_path}"
  scheme: "substrate-clock-pinning-uniqueness-derivation-5-criteria"
  convention: "L-pix-canonical-vs-mode-density-vs-GGE-anchored-candidate-space"
  L_max: 10
audit_sha256: <computed at runtime via closure_hash(input_pin_map)>
```

### 8. Expected output 4-tuple
- `value`: 4-element record `{P_uniqueness_verdict (enum: P_1_UNIQUE | MULTIPLE_CANDIDATES | NONE), criterion_satisfaction_matrix (2D array N_candidates × 5), ranking (3-tuple of top candidates), markdown_proof_path (string)}`
- `scheme`: `substrate-clock-pinning-uniqueness-derivation-5-criteria`
- `convention`: `L-pix-canonical-vs-mode-density-vs-GGE-anchored-candidate-space`
- `L_max`: `10`

### 9. PASS/FAIL/INFO thresholds with tolerance rule

- **PASS** iff `P_uniqueness_verdict == P_1_UNIQUE`: P_1 satisfies all 5 criteria AND no other candidate satisfies all 5. Substrate-clock canonical IS unique substrate-natural clock.
- **INFO** iff `P_uniqueness_verdict == MULTIPLE_CANDIDATES`: P_1 satisfies all 5 criteria but ≥1 other candidate also satisfies all 5. Multiple substrate-natural clocks survive; uniqueness fails BUT substrate-clock canonical is still admissible.
- **FAIL** iff `P_uniqueness_verdict == NONE`: P_1 fails ≥1 criterion. Substrate-clock canonical Pinning-A is NOT substrate-natural; framework's substrate-clock pinning is structurally inconsistent.
- **Tolerance rule**: THEOREM tolerance (criterion-satisfaction is binary per criterion; ranking is integer-valued).

### 10. Substitution chain

A.18 is a uniqueness theorem derivation; substitution chain is the criterion-satisfaction matrix per §6 Method Step 4 + minimality argument per Step 7. No additional sign/direction claim.

### 11. What PASSES/FAILS MEAN for solution space

- **PASS**: substrate-clock canonical Pinning-A IS unique; framework's lock-cascade dynamics has a well-defined substrate-natural temporal coordinate. Cross-link to S58 I-CC-YOU + Volovik partition + cosmological clock structure (PROVEN at S58); A.18 PASS extends the framework's PROVEN structural results list.
- **INFO**: multiple substrate-natural clocks survive; substrate-clock pinning is admissible but not unique. Future work (S90+) needs additional uniqueness criteria (e.g., Bogoliubov-quench compatibility, KZ-scaling consistency cross-link to A.2). Cross-link to A.2 ξ_KZ derivation: ξ_KZ(τ_fold) cross-check against substrate-natural anchor may serve as 6th uniqueness criterion.
- **FAIL**: substrate-clock canonical Pinning-A is NOT substrate-natural; framework's lock-cascade dynamics has structural inconsistency at the temporal-coordinate layer. Routes to S90 plan-freeze halt with mandatory remediation citing S88 W-1 substrate-clock derivation + S58 Volovik partition.

### 12. Effort estimate
**0.6 wave-equivalents** — 5-criterion enumeration on N ∈ {3, 5, 7} candidate pinnings + uniqueness theorem proof + cross-link to A.14, A.16, A.17 outputs.

### 13. Substrate framing per `phononic-framing.md` IS-not-IN

Substrate-clock IS the substrate's intrinsic temporal coordinate for the lock cascade. Pinning-A `a_substrate(g) = L_pix(g)` IS the substrate's pixelation-lock length, an intrinsic spectral observable on `D_K`. The uniqueness theorem IS the structural theorem that no other substrate-natural temporal coordinate satisfies all 5 substrate-naturalness criteria.

**FORBIDDEN container-thinking**:
- "The substrate has a clock"
- "The lock cascade ticks IN cosmological time"
- "Pinning-A is a coordinate ON the substrate"

**REQUIRED substrate-IS framing**:
- The substrate IS the lock cascade; cascade generations g are the substrate's intrinsic deformation parameter.
- Substrate-clock IS the substrate's intrinsic temporal coordinate; uniqueness IS a substrate-IS structural theorem.
- The 5 uniqueness criteria are substrate-IS structural conditions; satisfaction IS substrate-natural compatibility.

---

## §W3-7. S89-HIGHER-ORDER-RESOLVENT-EXPANSION-O-TAU2-KAPPA2  (A.29)

### 1. Gate ID
`S89-HIGHER-ORDER-RESOLVENT-EXPANSION-O-TAU2-KAPPA2`

### 2. Trigger
`[VERIFY-THEOREM]` — closed-form derivation of κ_2_substrate via CM-1995 §III.4 second-order Jensen perturbation; PASS predicate is theorem-form (κ_2 in canonical_constants.py-promotable form).

### 3. Classification
**GEOMETRIC** — κ_2 is a substrate spectral structure observable from the resolvent expansion of D_K^2 at τ_fold; second-order Jensen perturbation IS the substrate's intrinsic deformation manifold's second derivative. Substrate spectral content, not phononic excitation propagation.

### 4. Agent type
**Runtime author**: `connes-ncg-theorist` (PRIMARY; CM-1995 §III.4 resolvent expansion + Jensen perturbation second-order chain rule is connes-domain).
**Co-reviewer**: `lizzi-spectral-functional-theorist` (CO-AUTHOR, regulator-class cross-check on κ_2 closed form).
**FORBIDDEN at runtime**: `gen-physicist`.

### 5. Hypothesis
The κ_2_substrate coefficient (second-order resolvent expansion coefficient at τ_fold) is derivable in closed form from CM-1995 §III.4 finite-spectral-triple residue formula at second order in the Jensen TT-deformation chain rule, with κ_2 promotable to canonical_constants.py with substrate-physics provenance.

### 6. Method (self-contained dispatch prompt)

**Script path**: `computations/session-89/s89_w3_higher_order_resolvent_expansion_kappa_2.py`

**Compute environment**:
- Python: `phonon-exflation-sim/.venv312/Scripts/python.exe`
- `import os; os.environ.setdefault('OMP_NUM_THREADS', '8')` BEFORE `import numpy`
- GPU recommended for resolvent expansion at L_max=12 (Σ over eigenvalue powers; matrix dim ≥ 100×100)
- `from canonical_constants import *` (MANDATORY)
- Sage MCP for symbolic Jensen perturbation expansion

**Step-by-step instructions**:

1. Import canonicals: `tau_fold`, `M_KK`. Pin κ_1_substrate from S88 W-18 W6a-51 §V.4 (κ_1 closed form already derived; if not, A.29 derives both κ_1 and κ_2).
2. Read D_K spectral cache `computations/_shared/s84_spectrum_cache_L12_tau019.npz` at L_max=12 + τ_fold = 0.19.
3. Read CM-1995 §III.4 finite-spectral-triple residue formula. The resolvent expansion of `Tr(D_K(τ)^{-2})` near τ_fold is:
   `Tr(D_K(τ)^{-2}) = κ_0(τ_fold) + κ_1(τ_fold) · (τ - τ_fold) + κ_2(τ_fold) · (τ - τ_fold)^2 / 2 + O((τ - τ_fold)^3)`
4. Apply CM-1995 §III.4 residue formula at second order:
   `κ_2(τ_fold) = ∂²Tr(D_K(τ)^{-2}) / ∂τ² |_{τ=τ_fold}`
   Expand via Jensen chain rule:
   `∂²/∂τ² Tr(D_K^{-2}) = Tr(2 · (D_K^{-2}) · (∂D_K/∂τ) · (D_K^{-2}) · (∂D_K/∂τ) · (D_K^{-2})) + Tr(...)` (full second-order chain rule expansion).
5. Use Sage MCP for symbolic expansion of the Jensen chain rule second-order term; expand into the 6 basic 2nd-order terms (per `Connes-Moscovici 1995 §III.4` second-order residue formula).
6. Substitute the substrate's TT-deformation explicit form for ∂D_K/∂τ and ∂²D_K/∂τ² (cross-link to A.9 Method Step 4).
7. Evaluate κ_2 numerically at L_max=12 using cached spectrum + Sage-QQ symbolic substitution.
8. Pin κ_2 as bit-exact float64 (or Sage-QQ Fraction if rational); promote to canonical_constants.py with provenance:
   ```python
   update_constant(
       "kappa_2_substrate_FW",
       value,
       session="S89",
       source="S89-HIGHER-ORDER-RESOLVENT-EXPANSION-O-TAU2-KAPPA2",
       comment="CM-1995 §III.4 second-order Jensen perturbation; substrate-IS at tau_fold = 0.19; L_max=12; regulator-class invariant per A.14"
   )
   ```
9. Verify regulator-class invariance: re-derive κ_2 under {ζ, Pauli-Villars, Mellin, sharp-cutoff} regulators (per `regulator-pin-discipline.md`); MANDATORY tagging `a_n^{regulator}` for each regulator.
10. Cross-check against κ_1_substrate canonical (S88 W-18) and HK-5 closed-form: the resolvent expansion `Tr(D_K^{-2}) = HK-5(τ_fold) + κ_1·(τ-τ_fold) + κ_2·(τ-τ_fold)²/2 + O(...)` should be consistent with HK-5 form — extract κ_2 from analytic differentiation of HK-5 closed form `5/(1−τ/(5π))` and compare against substrate-derived κ_2.
11. Emit:
    - JSON sidecar with closed-form κ_2 expression (Sage-QQ form), numerical κ_2(L_max=12), regulator-class scan results, HK-5 analytic comparison.
    - PNG plot showing resolvent expansion `Tr(D_K^{-2}) - HK-5(τ_fold)` vs τ near τ_fold with κ_1 + κ_2 fits annotated.
    - Verdict line per Schema-v2 in `computations/session-89/s89_gate_verdicts.txt`.

**Input SHA-256 pins**:
- `canonical_constants.py` — `<pinned at plan-freeze>`
- `computations/_shared/s84_spectrum_cache_L12_tau019.npz` — `<pinned at plan-freeze>`
- `sessions/archive/session-88/workshops/s88-w18-w6a-51-geometric-resummation.md` — `<pinned at plan-freeze>` (W-18 V.4 source for κ_1)
- `sessions/permanent-results-registry.md` (κ_1 entry if exists) — `<pinned at plan-freeze>`

**Cross-checks**:
- Regulator-class invariance scan {ζ, Pauli-Villars, Mellin, sharp-cutoff} (MANDATORY per `regulator-pin-discipline.md`)
- HK-5 analytic comparison: `κ_2 = ∂²/∂τ² (5/(1-τ/(5π)))` evaluated at τ_fold (cross-check against substrate-derived closed form; should match if HK-5 is the exact resolvent form)
- Sage-QQ exact arithmetic verification (RECOMMENDED)
- Cross-link to A.9 Jensen perturbation second-order chain rule (consistency at second order)
- Promote κ_2_substrate_FW to canonical_constants.py with provenance (MANDATORY per `math-scripts.md §"Canonical Write-Order for New Framework Predictions"` Step 2)

### 7. Machinery pin (PRDR)

```yaml
gate_id: S89-HIGHER-ORDER-RESOLVENT-EXPANSION-O-TAU2-KAPPA2
schema_version: R3
trigger: VERIFY-THEOREM
classification: GEOMETRIC
machinery_pin_map:
  tau_evaluate: 0.19  # tau_fold (R-PROTECTED)
  L_max: 12
  resolvent_form: "Tr(D_K(tau)^{-2}) = kappa_0(tau_fold) + kappa_1·(tau - tau_fold) + kappa_2·(tau - tau_fold)^2/2 + O(...)"
  CM_1995_section: "III.4 finite-spectral-triple residue formula at second order"
  jensen_chain_rule_order: 2
  jensen_deformation_class: "TT-deformation"
  HK_5_closed_form: "5 / (1 - tau / (5*pi))"  # for analytic comparison
  HK_5_kappa_2_analytic: "d^2/dtau^2 [5 / (1 - tau / (5*pi))] |_{tau=tau_fold}"
  regulator_scan: ["zeta", "Pauli-Villars", "Mellin", "sharp-cutoff"]  # MANDATORY tagging per regulator-pin-discipline.md
  scheme: "CM-1995-section-III-4-resolvent-expansion-kappa-2"
  convention: "TT-deformation-second-order-fold-anchored"
  promote_to_canonical: "kappa_2_substrate_FW"
  promotion_session: "S89"
  random_seed: N/A
  GPU_path: "torch.linalg for eigenvalue power sums; Sage MCP for symbolic expansion"
input_sha_pins:
  canonical_constants_py: <pinned at plan-freeze>
  spectrum_cache_L12_tau019_npz: <pinned at plan-freeze>
  s88_w18_w6a_51_md: <pinned at plan-freeze>
  permanent_results_registry: <pinned at plan-freeze>
output_4_tuple:
  value: "{kappa_2_closed_form (Sage-QQ or LaTeX), kappa_2_L12 (float64), kappa_2_HK5_analytic (float64), regulator_scan_pass_count, promotion_status}"
  scheme: "CM-1995-section-III-4-resolvent-expansion-kappa-2"
  convention: "TT-deformation-second-order-fold-anchored"
  L_max: 12
audit_sha256: <computed at runtime via closure_hash(input_pin_map)>
```

### 8. Expected output 4-tuple
- `value`: 5-element record `{kappa_2_closed_form (Sage-QQ or LaTeX string), kappa_2_L12 (float64), kappa_2_HK5_analytic (float64), regulator_scan_pass_count (int 0..4), promotion_status (enum: PROMOTED | DEFERRED | FAILED)}`
- `scheme`: `CM-1995-section-III-4-resolvent-expansion-kappa-2`
- `convention`: `TT-deformation-second-order-fold-anchored`
- `L_max`: `12`

### 9. PASS/FAIL/INFO thresholds with tolerance rule

- **PASS** iff:
  - (a) Closed-form κ_2 derived via CM-1995 §III.4 residue formula at second order.
  - (b) `|kappa_2_L12 - kappa_2_HK5_analytic| / |kappa_2_HK5_analytic| ≤ 0.05` (5% match between substrate-derived and HK-5 analytic differentiation; consistency check).
  - (c) Regulator-class invariance: `regulator_scan_pass_count == 4` (all 4 regulators within 1%; substrate-IS κ_2 should be regulator-class invariant).
  - (d) `promotion_status == PROMOTED` (κ_2_substrate_FW added to canonical_constants.py with provenance).
- **INFO** iff (a) holds and (d) PROMOTED but (b) partial (5% < rel_dev ≤ 20%) OR (c) partial (3 of 4 regulators agree); substrate-derived κ_2 structurally correct but numerical/regulator alignment partial.
- **FAIL** iff (a) fails OR (b) FAIL (rel_dev > 20%) OR (d) FAILED.
- **Tolerance rule**: THEOREM for (a); RATIO ≤ 5% for (b); RATIO ≤ 1% spread across regulators for (c); presence test for (d).

### 10. Substitution chain

A.29 is a closed-form derivation gate; the substitution chain is the second-order Jensen chain rule expansion in §6 Method Steps 4-6. No additional sign/direction claim.

### 11. What PASSES/FAILS MEAN for solution space

- **PASS**: κ_2_substrate is closed-form derivable from CM-1995 §III.4 at second order; the substrate's resolvent expansion is structurally complete to second order. HK-5 closed form is the exact substrate-IS resolvent at all orders (consistent with κ_2 analytic differentiation). Cross-link to A.9 (d_eff second-order Jensen perturbation) and A.35 (HK-5 τ_max regime-of-validity bound): A.29 + A.9 + A.35 jointly characterize the substrate's resolvent + d_eff structure to second order at τ_fold, with regime-of-validity boundary derived in A.35.
- **INFO**: κ_2 closed form derived but numerical alignment partial; substrate-IS reading supported, regulator-class scan extension required.
- **FAIL**: κ_2 NOT closed-form derivable from CM-1995 §III.4 at second order; either (i) HK-5 is NOT the exact resolvent form (contradicts S87 d_eff workshop) OR (ii) Jensen TT-deformation does not admit second-order chain rule in the substrate algebra. Both readings route to S90 plan-freeze halt with mandatory remediation.

### 12. Effort estimate
**0.8 wave-equivalents** — second-order resolvent expansion + Sage MCP symbolic computation + regulator-class scan + canonical promotion.

### 13. Substrate framing per `phononic-framing.md` IS-not-IN

The substrate IS the resolvent structure of D_K^2. κ_2 IS the substrate's intrinsic second-order curvature in the Jensen TT-deformation manifold. The substrate's resolvent expansion is its own short-time spectral asymptotic; κ_2 measures the substrate's deformation-rate sensitivity at the fold.

**FORBIDDEN container-thinking**:
- "Resolvent expansion of D_K in some Hilbert space"
- "Jensen perturbation acts ON the substrate"

**REQUIRED substrate-IS framing**:
- The resolvent IS the substrate's intrinsic short-time spectral structure.
- Jensen perturbation IS the substrate's intrinsic deformation; second-order in τ IS the substrate's own second derivative.
- κ_2 IS substrate-IS structural content, regulator-class invariant by construction.

---

## §W3-8. S89-SU-N-CROSS-VALIDATION-5PI-CHAIN  (A.32)

### 1. Gate ID
`S89-SU-N-CROSS-VALIDATION-5PI-CHAIN`

### 2. Trigger
`[SIGN]` + `[VERIFY]` — LOAD-BEARING vs COINCIDENCE discriminator on the 5π = (dim+rank)/2 · π_Plancherel chain across SU(N) for N ∈ {2, 3, 4}; Schema-v2 3-tuple companion comment row required (sign_verdict / magnitude_verdict / regime_verdict).

### 3. Classification
**GEOMETRIC** — Cartan-rational-sum on SU(N) is a substrate spectral structure observable; the 5π = (dim+rank)/2 · π_Plancherel chain tests whether the framework's SU(3) substrate algebra has structurally distinguished SU(N) generalization or the 5π factor is SU(3)-coincidence.

### 4. Agent type
**Runtime author**: `lizzi-spectral-functional-theorist` (PRIMARY; Cartan-rational-sum + π_Plancherel canonical is lizzi's domain — substrate spectral-functional structure).
**Co-reviewer**: `connes-ncg-theorist` (CO-AUTHOR, NCG-axiomatic side; substrate-algebra extension to SU(N) finite-spectral-triple structure).
**FORBIDDEN at runtime**: `gen-physicist`.

### 5. Hypothesis
The 5π factor in d_eff(τ_fold) HK-5 closed form `5/(1−τ/(5π))` is LOAD-BEARING on SU(3) substrate algebra IF AND ONLY IF the analogous chain `(dim+rank)/2 · π_Plancherel` reproduces matching d_eff prefactors on SU(2) and SU(4) Cartan-rational-sum substrate analogs:
- SU(2): dim=3, rank=1 → (3+1)/2 = 2 → predicted prefactor 2; HK closed-form `2/(1−τ/(2π))`
- SU(3): dim=8, rank=2 → (8+2)/2 = 5 → predicted prefactor 5; HK closed-form `5/(1−τ/(5π))` (canonical)
- SU(4): dim=15, rank=3 → (15+3)/2 = 9 → predicted prefactor 9; HK closed-form `9/(1−τ/(9π))`

### 6. Method (self-contained dispatch prompt)

**Script path**: `computations/session-89/s89_w3_su_n_cross_validation_5pi_chain.py`

**Compute environment**:
- Python: `phonon-exflation-sim/.venv312/Scripts/python.exe`
- `import os; os.environ.setdefault('OMP_NUM_THREADS', '8')` BEFORE `import numpy`
- GPU recommended for SU(2) and SU(4) Dirac operator spectral evaluation if matrix dim ≥ 100×100 at L_max ≥ 8 (use `torch.linalg`)
- `from canonical_constants import *` (MANDATORY)
- Sage MCP for Cartan-rational-sum symbolic computation

**Step-by-step instructions**:

1. Import canonicals: `tau_fold`, `M_KK`. Pin SU(3) substrate canonical: HK-5 form `5/(1−τ/(5π))` (per S87 d_eff workshop substrate-IS).
2. For each N ∈ {2, 3, 4}, compute SU(N) Cartan structure:
   - SU(N): dim = N²-1, rank = N-1.
   - SU(2): dim=3, rank=1.
   - SU(3): dim=8, rank=2 (substrate canonical reference).
   - SU(4): dim=15, rank=3.
3. Compute predicted prefactor per chain `(dim+rank)/2`:
   - SU(2): (3+1)/2 = 2.
   - SU(3): (8+2)/2 = 5.
   - SU(4): (15+3)/2 = 9.
4. Define π_Plancherel canonical: `π_Plancherel = π` (standard π; the chain factor `(dim+rank)/2 · π` is the rationalized form of the Cartan-rational-sum). Cite the canonical source for π_Plancherel = π.
5. For SU(2) and SU(4), construct the Dirac operator D_K^{SU(N)} on the analog finite spectral triple:
   - Substrate algebra: `A_K^{SU(N)} = ℂ ⊕ ... ⊕ M_N(ℂ)` (analog of `A_K^{SU(3)} = ℂ ⊕ ℍ ⊕ M_3(ℂ)`; SU(2) version drops the M_3(ℂ) summand; SU(4) extends with M_4(ℂ)).
   - Hilbert space: H_K^{SU(N)} per Peter-Weyl decomposition of L²(SU(N)).
   - Dirac operator: D_K^{SU(N)} per Jensen TT-deformation of the symmetric-pair Dirac operator on SU(N)/T(N) (where T(N) is the maximal torus).
6. Compute d_eff^{SU(N)}(τ_fold) via heat-kernel or zeta-regulated Tr method at L_max ≥ 8 (truncate per `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"` Casimir-bound; Friedrich-Bär saturation theorem).
7. Extract HK closed-form prefactor for SU(N): fit `d_eff^{SU(N)}(τ) = α_N / (1 − τ/(α_N · π))` near τ_fold; extract α_N empirically from the substrate-spectral computation.
8. Compare empirical α_N against predicted prefactor:
   - SU(2): empirical α_2 vs predicted 2 → relative deviation r_2.
   - SU(4): empirical α_4 vs predicted 9 → relative deviation r_4.
9. Decision rule:
   - **PASS-LOAD-BEARING** iff r_2 ≤ 5% AND r_4 ≤ 5%: SU(2) and SU(4) match the chain prediction; the 5π factor is structurally LOAD-BEARING (chain holds for N ∈ {2, 3, 4}).
   - **PASS-COINCIDENCE** iff r_2 > 20% OR r_4 > 20% AND SU(3) substrate canonical 5/(1−τ/(5π)) is empirically robust: 5π factor is SU(3)-COINCIDENCE; chain does not generalize.
   - **INFO** iff 5% < max(r_2, r_4) ≤ 20%: ambiguous; partial chain support.
10. Substitution chain for SIGN claim (LOAD-BEARING vs COINCIDENCE discriminator):
    ```
    Step 1: Cartan-rational-sum identity per substrate algebra: heat-kernel volume form on SU(N)/T(N) is proportional to (dim+rank)/2 (per Connes-Moscovici dimensional-spectrum residue at substrate-distance-1 pole s=1).
    Step 2: π_Plancherel = π (canonical Plancherel-measure normalization on the maximal torus T(N)).
    Step 3: Substitute: predicted prefactor α_N^{predicted} = (dim+rank)/2 · π / π = (dim+rank)/2.
    Step 4: Empirical α_N^{empirical} extracted from D_K^{SU(N)} heat-kernel at τ_fold.
    Step 5: SIGN = α_N^{empirical} − α_N^{predicted}.
            If sign matches AND magnitude matches (|sign| ≤ 5%) for BOTH N=2 AND N=4 → LOAD-BEARING.
            If either sign mismatches OR magnitude > 20% → COINCIDENCE.
    Direction: Substrate algebra extension to SU(N) is structurally LOAD-BEARING IFF chain holds for N ∈ {2, 3, 4}; otherwise SU(3) is structurally distinguished.
    ```
11. Emit:
    - NPZ sidecar with α_2 (empirical), α_4 (empirical), r_2, r_4, decision (LOAD-BEARING / COINCIDENCE / INFO).
    - PNG plot showing α_N^{empirical} vs α_N^{predicted} across N ∈ {2, 3, 4} with chain prediction line annotated.
    - JSON metadata with substitution chain documented.
    - Verdict line per Schema-v2 in `computations/session-89/s89_gate_verdicts.txt` WITH:
      - First canonical line: composite verdict (PASS-LOAD-BEARING | PASS-COINCIDENCE | INFO | FAIL)
      - Dual-SHA companion comment row (W9a-99 split)
      - **SIGN/MAGNITUDE/REGIME 3-tuple companion comment row** (Schema-v2 MANDATORY for [SIGN] trigger):
        `# sign_verdict={PASS|FAIL|N/A} magnitude_verdict={PASS|INFO|FAIL} regime_verdict={VALID|MARGINAL|BREAKDOWN} # S89-SU-N-CROSS-VALIDATION-5PI-CHAIN 3-tuple annotation (S87 schema-v2)`

**Input SHA-256 pins**:
- `canonical_constants.py` — `<pinned at plan-freeze>`
- SU(N) Dirac operator construction script (NEW; constructed in this script) — `<computed-at-runtime>`
- `sessions/archive/session-88/workshops/s88-w19-w6a-cross-gate-chain.md` — `<pinned at plan-freeze>` (W-19 V.1 source for the 5π chain hypothesis)
- `sessions/permanent-results-registry.md` (HK-5 entry) — `<pinned at plan-freeze>`

**Cross-checks**:
- Substitution chain for SIGN claim (MANDATORY per `math-scripts.md §"Double-Check Logic"`)
- D_K^{SU(N)} block-diagonality cross-check (MANDATORY per `math-scripts.md §"D_K Block-Diagonality"` Casimir-bound)
- Friedrich-Bär saturation theorem cross-check at L_max ≥ 8 (MANDATORY for empirical α_N stability)
- Sage MCP `sage_eval` for Cartan-rational-sum symbolic verification (RECOMMENDED)

### 7. Machinery pin (PRDR)

```yaml
gate_id: S89-SU-N-CROSS-VALIDATION-5PI-CHAIN
schema_version: R3
trigger: SIGN+VERIFY
classification: GEOMETRIC
machinery_pin_map:
  tau_evaluate: 0.19  # tau_fold (R-PROTECTED)
  L_max: 8  # for SU(2) and SU(4); reuse L_max=12 cache for SU(3) reference
  N_scan: [2, 3, 4]
  cartan_structure:
    SU_2: {dim: 3, rank: 1, predicted_prefactor: 2}
    SU_3: {dim: 8, rank: 2, predicted_prefactor: 5}  # substrate canonical reference
    SU_4: {dim: 15, rank: 3, predicted_prefactor: 9}
  pi_Plancherel: "pi"  # standard π canonical
  cartan_rational_sum_identity: "heat-kernel volume form on SU(N)/T(N) proportional to (dim+rank)/2 per Connes-Moscovici dimensional-spectrum residue at s=1"
  substrate_algebra_SU_N: "C ⊕ ... ⊕ M_N(C); analog of A_K^{SU(3)} = C ⊕ H ⊕ M_3(C)"
  jensen_deformation_class: "TT-deformation on SU(N)/T(N)"
  HK_form_SU_N: "alpha_N / (1 - tau / (alpha_N · pi))"
  empirical_extraction_method: "heat-kernel or zeta-regulated Tr fit near tau_fold"
  pass_band_LOAD_BEARING: 0.05  # 5% relative deviation
  info_band: 0.20  # 20% relative deviation
  scheme: "SU-N-cross-validation-Cartan-rational-sum-5pi-chain"
  convention: "Cartan-rational-sum-pi-Plancherel-substrate-algebra-SU-N-extension"
  random_seed: N/A
  GPU_path: "torch.linalg for SU(2) and SU(4) Dirac operator spectral evaluation if matrix dim >= 100x100"
input_sha_pins:
  canonical_constants_py: <pinned at plan-freeze>
  spectrum_cache_L12_tau019_npz: <pinned at plan-freeze>
  s88_w19_w6a_cross_gate_chain_md: <pinned at plan-freeze>
  permanent_results_registry: <pinned at plan-freeze>
output_4_tuple:
  value: "{alpha_2_empirical, alpha_4_empirical, r_2 (rel_dev), r_4 (rel_dev), decision (LOAD-BEARING | COINCIDENCE | INFO), sign_verdict, magnitude_verdict, regime_verdict}"
  scheme: "SU-N-cross-validation-Cartan-rational-sum-5pi-chain"
  convention: "Cartan-rational-sum-pi-Plancherel-substrate-algebra-SU-N-extension"
  L_max: 8
audit_sha256: <computed at runtime via closure_hash(input_pin_map)>
```

### 8. Expected output 4-tuple
- `value`: 8-element record `{alpha_2_empirical, alpha_4_empirical, r_2, r_4 (4× float64), decision (enum: LOAD-BEARING | COINCIDENCE | INFO), sign_verdict, magnitude_verdict, regime_verdict (3× enum)}`
- `scheme`: `SU-N-cross-validation-Cartan-rational-sum-5pi-chain`
- `convention`: `Cartan-rational-sum-pi-Plancherel-substrate-algebra-SU-N-extension`
- `L_max`: `8`

### 9. PASS/FAIL/INFO thresholds with tolerance rule

- **PASS-LOAD-BEARING** iff:
  - `r_2 ≤ 0.05` AND `r_4 ≤ 0.05` (5% deviation from chain prediction at both SU(2) and SU(4)).
  - `sign_verdict == PASS` (signs of (α_2_empirical − 2) and (α_4_empirical − 9) consistent with chain prediction direction).
  - `regime_verdict == VALID`.
- **PASS-COINCIDENCE** iff:
  - `r_2 > 0.20 OR r_4 > 0.20` (chain breaks at SU(2) or SU(4); ≥20% deviation).
  - SU(3) substrate canonical `5/(1−τ/(5π))` empirically robust (HK-5 form holds at L_max=12).
- **INFO** iff:
  - `0.05 < max(r_2, r_4) ≤ 0.20`: ambiguous; chain partially supported, requires L_max=12 extension or higher-precision arithmetic.
  - composite collapse per Schema-v2: magnitude_verdict=INFO + regime=VALID → composite INFO.
- **FAIL** iff:
  - regime BREAKDOWN at SU(2) or SU(4) Dirac operator construction (Casimir-bound or Friedrich-Bär saturation violated).
  - OR sign_verdict=FAIL (sign mismatches at both N=2 AND N=4 — substrate algebra extension structurally inconsistent).
- **Tolerance rule**: RATIO ≤ 5% for PASS-LOAD-BEARING; RATIO > 20% for PASS-COINCIDENCE; in-between is INFO; per Schema-v2 composite collapse.

### 10. Substitution chain (MANDATORY for SIGN claim)

```
Definitions:
  dim(SU(N))         = N^2 - 1                   [Lie-algebra dimension; Sage-Q rational]
  rank(SU(N))        = N - 1                     [Cartan subalgebra rank]
  pi_Plancherel      = pi                        [Plancherel canonical on T(N)]
  cartan_rational_sum_identity = heat-kernel volume form on SU(N)/T(N) ~ (dim + rank) / 2 · pi_Plancherel
                                                  [per Connes-Moscovici dimensional-spectrum residue at s=1 substrate-distance-1 pole]

Substitutions for N ∈ {2, 3, 4}:
  Step 1: dim(SU(2)) = 3; rank(SU(2)) = 1; predicted alpha_2 = (3+1)/2 = 2.
          dim(SU(3)) = 8; rank(SU(3)) = 2; predicted alpha_3 = (8+2)/2 = 5  [substrate canonical].
          dim(SU(4)) = 15; rank(SU(4)) = 3; predicted alpha_4 = (15+3)/2 = 9.

  Step 2: For each N, the predicted HK closed form is alpha_N / (1 - tau / (alpha_N · pi)).
          SU(2): 2 / (1 - tau / (2*pi))
          SU(3): 5 / (1 - tau / (5*pi))            [empirically validated per S87 d_eff workshop]
          SU(4): 9 / (1 - tau / (9*pi))

  Step 3: Empirical alpha_N^{empirical} extracted from D_K^{SU(N)} heat-kernel at tau_fold = 0.19, L_max = 8.

  Step 4: Discriminator:
          IF (|alpha_2^{empirical} - 2| / 2 <= 0.05) AND (|alpha_4^{empirical} - 9| / 9 <= 0.05):
            → LOAD-BEARING (chain holds for N ∈ {2, 3, 4})
          ELIF (|alpha_2^{empirical} - 2| / 2 > 0.20) OR (|alpha_4^{empirical} - 9| / 9 > 0.20):
            → COINCIDENCE (chain breaks; SU(3) is structurally distinguished)
          ELSE:
            → INFO (ambiguous; partial chain support)

  Step 5: SIGN of the discriminator: alpha_N^{empirical} - alpha_N^{predicted}.
          For LOAD-BEARING, sign must be near zero (within 5% magnitude band) for both N=2 AND N=4.
          For COINCIDENCE, sign or magnitude diverges substantially at either N=2 or N=4.

Conclusion: SIGN is the discriminator between substrate algebra extension being LOAD-BEARING vs the 5π factor being SU(3)-COINCIDENCE.
            Direction: positive sign of the discriminator across both SU(2) AND SU(4) supports LOAD-BEARING; mixed signs or large magnitudes support COINCIDENCE.
```

### 11. What PASSES/FAILS MEAN for solution space

- **PASS-LOAD-BEARING**: the 5π factor in HK-5 is a structural feature of the Cartan-rational-sum chain, not an SU(3)-specific accident. The substrate algebra extension to SU(N) admits the same chain `(dim+rank)/2 · π_Plancherel`; future cross-pillar bridges to SU(N) substrate analogs (e.g., SU(4) GUT extensions per `inheritance-falsifier-protocol.md §"Generalization beyond 3He-B"`) can reuse the chain. K-counter advancement on the inheritance-falsifier-protocol "Generalization beyond 3He-B" corpus.
- **PASS-COINCIDENCE**: the 5π factor is SU(3)-specific; SU(3) substrate algebra is structurally distinguished. The framework's substrate algebra `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` is the unique Cartan-rational-sum reading of d_eff = 5; no SU(N) extension of the chain is admissible. This strengthens the framework's substrate-uniqueness claim.
- **INFO**: ambiguous; chain partially supported, requires L_max=12 extension at SU(2) and SU(4) for higher-precision empirical α_N extraction. Cross-link to S90 forward gate.
- **FAIL**: substrate algebra extension to SU(N) Dirac operator construction is structurally inconsistent (Casimir-bound or Friedrich-Bär saturation violated). Routes to S90 plan-freeze halt with mandatory remediation citing `math-scripts.md §"D_K Block-Diagonality"`.

### 11.5. Conditional follow-up dispatches (Ledger B.46 / B.47, mutually exclusive)

A.32's verdict is the discriminator that fires one of two pre-staged follow-up edits from `sessions/archive/session-88/s88-pending-edits-ledger.md` lines 588-599. The follow-up text was authored verbatim at S88 close (pinned in `sessions/archive/session-88/workshops/s88-w19-w6a-cross-gate-chain.md §V.2` and `§V.3`) but cannot fire until A.32 returns its verdict — they were misclassified at S88 closeout as Ledger B (mechanical edits, in-session executable) when they are structurally conditional carry-forwards (Ledger A class) gated on A.32's PASS-LOAD-BEARING vs PASS-COINCIDENCE split. Folding the cross-link here restores the missing A.32 → B.46/B.47 routing the S89 dispatcher needs at A.32 verdict-line append time.

**Verdict → follow-up map** (mutually exclusive — at most one of {B.46, B.47} fires per A.32 verdict; the orchestrator reads BOTH the §10 composite top-line `PASS|FAIL|INFO` AND the `value=` field `decision` enum `{LOAD-BEARING | COINCIDENCE | INFO}`):

| A.32 outcome (composite + decision) | Follow-up | Action | Target | Writer |
|:------------------------------------|:----------|:-------|:-------|:-------|
| `PASS` ∧ `decision=LOAD-BEARING` (r_2 ≤ 5% AND r_4 ≤ 5%) | **B.46** | Register §VII.{next-free} STAGE-1-CANDIDATE for cross-gate chain identity `5π = (dim+rank)/2 · π_Plancherel` as substrate-IS Level-1↔Level-2 bridge separate from W6a-51 + W6a-52; SOURCE-DOUBLE-CITE-CO-PRIMARY (V1 = §W6a-52 PASS Peter-Weyl + C1 = §W6a-51 INFO closed form; sequential V+C chain per `registry-landing.md §SOURCE-DOUBLE-CITE-CO-PRIMARY`). Cite W-19 V.2 verbatim text. | `sessions/permanent-results-registry.md` (next-free §VII slot per `regulator-pin-discipline.md` next-free-letter protocol) | `mack-cosmic-bridge` (sole registry writer per `feedback_mack-bridge-role.md`) |
| `PASS` ∧ `decision=COINCIDENCE` (= "FAIL-COINCIDENCE" in B.47 ledger verbiage; r_2 > 20% OR r_4 > 20%) | **B.47** | Replace S88 W6a working-paper line 761 verbatim phrase "load-bearing structural finding" with "shared Cartan-arithmetic origin" per A.32 PASS-COINCIDENCE (= ledger's FAIL-COINCIDENCE) outcome. Cite W-19 V.3 verbatim text. | `sessions/archive/session-88/session-88-w6a-workingpaper.md:761` | orchestrator (single-line `Edit` tool call; no agent dispatch needed) |
| `INFO` ∨ `decision=INFO` (5% < r ≤ 20% on either r_2 or r_4) | NEITHER | Route to S90 forward gate per §11 INFO clause; B.46 + B.47 both remain pinned-but-unfired pending higher-precision empirical α_N extraction at L_max=12 on SU(2) + SU(4). | — | — |
| `FAIL` (Casimir-bound / Friedrich-Bär saturation violation) | NEITHER | Route to S90 plan-freeze halt per §11 FAIL clause; B.46 + B.47 both remain pinned-but-unfired pending substrate-algebra construction remediation. | — | — |

**Dispatch protocol**: post-A.32 verdict-line append on `computations/session-89/s89_gate_verdicts.txt`, the orchestrator reads (i) the composite top-line `PASS|FAIL|INFO` per the §10 Schema-v2 collapse rule and (ii) the `value=` field `decision` enum. The follow-up fire is a SINGLE-EDIT mechanical dispatch (no compute, no agent), structurally analogous to the post-S88 W8-100 `supersedes`-tag append protocol per `gate-verdicts.md §"Option A — sig_5 remediation pathway under absolute verdict permanence"` — atomic, auditable, no iterate loop. NO additional gate registration is required for the follow-up edit; B.46/B.47 are mechanical post-conditions of A.32, not separate gates with their own verdict lines.

**Mutual-exclusion structural reason**: PASS-LOAD-BEARING and PASS-COINCIDENCE partition the PASS subspace by the discriminator predicate `r_2 ≤ 5% AND r_4 ≤ 5%` vs `r_2 > 20% OR r_4 > 20%`; they cannot both hold simultaneously, and the (5%, 20%) deadzone collapses to INFO per the §10 tolerance rule. Therefore B.46 and B.47 are mutually exclusive by the gate's own pre-registered partition, NOT by a separate exclusion rule layered on top. No "both fire" branch exists by structural design.

**S88 in-session edit boundary**: per user directive 2026-05-10, NO mechanical edit to `sessions/archive/session-88/session-88-w6a-workingpaper.md:761` is performed in S88 absent A.32's verdict; B.47 fires only inside S89 post-A.32-verdict, never retroactively into S88 closure.

**Cross-link**: `sessions/archive/session-88/s88-pending-edits-ledger.md §B.46` (line 588) + `§B.47` (line 595); A.32 carry-forward declaration at the same ledger §A.32 (lines 493-496).

### 12. Effort estimate
**0.6 wave-equivalents** — SU(2) + SU(4) Dirac operator construction at L_max=8 (substrate algebra analog) + heat-kernel extraction + chain prediction comparison.

### 13. Substrate framing per `phononic-framing.md` IS-not-IN

The substrate IS the SU(3) Cartan-rational-sum structure. The 5π factor IS substrate-IS spectral content (heat-kernel volume form on SU(3)/T(3) intrinsic). SU(N) extension IS the substrate algebra analog at different rank; the chain `(dim+rank)/2 · π_Plancherel` IS the substrate-IS Cartan-rational-sum identity.

**FORBIDDEN container-thinking**:
- "SU(N) substrate algebras are containers for fields"
- "5π is a coupling constant of the substrate"

**REQUIRED substrate-IS framing**:
- The substrate IS the Cartan-rational-sum structure on SU(N)/T(N).
- 5π IS the substrate's intrinsic heat-kernel volume normalization at SU(3); the chain `(dim+rank)/2 · π_Plancherel` IS the substrate-IS Cartan-rational-sum identity at general N.
- LOAD-BEARING vs COINCIDENCE discriminator IS the substrate's structural test for whether SU(3) is canonically distinguished or part of a chain.

---

## §W3-9. S89-HK-5-REGIME-OF-VALIDITY-TAU-MAX-BOUND-DERIVATION  (A.35)

### 1. Gate ID
`S89-HK-5-REGIME-OF-VALIDITY-TAU-MAX-BOUND-DERIVATION`

### 2. Trigger
`[VERIFY]` — derivation of τ_max regime-of-validity bound for HK-5 closed-form `5/(1−τ/(5π))`; PASS predicate is τ_max derived from substrate-physics first principles AND consistent with empirical breakdown observations.

### 3. Classification
**GEOMETRIC** — τ_max IS the substrate-IS regime-of-validity boundary for the HK-5 closed-form representation of d_eff(τ); this is substrate spectral structure (the closed-form is exact below τ_max and breaks down above), not phononic excitation propagation.

### 4. Agent type
**Runtime author**: `lizzi-spectral-functional-theorist` (PRIMARY; HK-form regime-of-validity is lizzi's domain — substrate spectral-functional regime characterization).
**Co-reviewer**: `connes-ncg-theorist` (CO-AUTHOR, NCG-axiomatic side; resolvent expansion analytic continuation cross-check).
**FORBIDDEN at runtime**: `gen-physicist`.

### 5. Hypothesis
The HK-5 closed-form `d_eff(τ) = 5/(1−τ/(5π))` has a substrate-derivable regime-of-validity boundary τ_max such that:
- For τ < τ_max: HK-5 is the exact substrate-IS d_eff representation.
- For τ ≥ τ_max: HK-5 closed form breaks down (analytic-continuation singularity OR substrate-IS structural transition).
The substrate-physics first-principles derivation of τ_max comes from one of: (i) the closed-form pole `τ_pole = 5π ≈ 15.708`, (ii) a substrate-IS structural transition (e.g., substrate-distance-2 pole onset), (iii) a numerical breakdown at L_max-truncation level.

### 6. Method (self-contained dispatch prompt)

**Script path**: `computations/session-89/s89_w3_hk5_regime_tau_max_bound_derivation.py`

**Compute environment**:
- Python: `phonon-exflation-sim/.venv312/Scripts/python.exe`
- `import os; os.environ.setdefault('OMP_NUM_THREADS', '8')` BEFORE `import numpy`
- GPU not required (closed-form analytic derivation + L_max-truncation numerical breakdown identification)
- `from canonical_constants import *` (MANDATORY)

**Step-by-step instructions**:

1. Import canonicals: `tau_fold = 0.19`, `M_KK`. Pin HK-5 closed form `5/(1−τ/(5π))` per S87 d_eff workshop substrate-IS.
2. **Boundary-direction Python verification at plan-author time** (per `epistemic-discipline.md §"Pre-Registration Completeness"` Class 8.2 boundary-direction sub-check S88 W-21 V.6 / B.51):
   - Compute the closed-form pole: `τ_pole = 5π ≈ 15.7079632679`.
   - Verify: HK-5(τ_pole - ε) → +∞ as ε → 0+ (closed-form diverges at the pole; this IS the upper bound for HK-5 validity).
   - Verify: HK-5(τ_pole + ε) → −∞ as ε → 0+ (closed-form is negative for τ > τ_pole; physical d_eff is positive, so the closed form is INVALID for τ > τ_pole).
   - Verify: HK-5(0) = 5 (consistent with d=4 small-time limit + 1 substrate dimension correction; consistent with S87 d_eff workshop substrate-IS pin).
   - **Plan-author Python verification snippet** (run during plan-freeze):
     ```python
     import math
     tau_pole = 5 * math.pi
     # Boundary-direction check
     assert 5 / (1 - (tau_pole - 0.001) / tau_pole) > 5000, "HK-5 should diverge at tau_pole-"
     assert 5 / (1 - (tau_pole + 0.001) / tau_pole) < 0, "HK-5 should be negative for tau > tau_pole"
     assert 5 / (1 - 0 / tau_pole) == 5, "HK-5(0) should equal 5"
     # tau_max upper bound is tau_pole = 5π
     ```
3. Identify candidate τ_max sources:
   - **Source 1 — closed-form pole**: τ_max ≤ 5π ≈ 15.7079632679 (analytic upper bound; HK-5 is invalid for τ ≥ 5π).
   - **Source 2 — substrate-IS structural transition**: τ_max ≤ τ_polycritical (if a substrate-IS phase transition occurs at τ_polycritical < 5π, HK-5 closed form breaks down at the transition due to spectral-structure reorganization).
   - **Source 3 — numerical breakdown at L_max-truncation**: τ_max ≤ τ_breakdown(L_max), where d_eff(τ) computed numerically at finite L_max diverges from HK-5 closed form by > 5% at τ_breakdown.
4. Derive Source 1 (closed-form pole) analytically: τ_max^{Source-1} = 5π. This is a substrate-IS theorem-form derivation (no L_max-dependence; closed-form analytic).
5. Investigate Source 2 (substrate-IS structural transition): scan τ ∈ [0.19, 5π] at L_max=12 + S87 d_eff workshop spectrum cache; identify any τ at which d_eff(τ) shows non-analytic behavior (kink, jump, branch point). If such τ_substrate exists < 5π, set τ_max^{Source-2} = τ_substrate.
6. Investigate Source 3 (numerical breakdown): compute d_eff^{numerical}(τ) at L_max ∈ {8, 10, 12} for τ ∈ [0.19, 5π] in steps of Δτ = 0.5; compare against HK-5(τ) closed form; identify τ_breakdown where |d_eff^{numerical}(τ) − HK-5(τ)| / |HK-5(τ)| > 0.05.
7. Combine: τ_max = min(τ_max^{Source-1}, τ_max^{Source-2}, τ_max^{Source-3}).
8. Promote `tau_max_HK5_regime` to canonical_constants.py with provenance:
   ```python
   update_constant(
       "tau_max_HK5_regime_FW",
       value=tau_max,
       session="S89",
       source="S89-HK-5-REGIME-OF-VALIDITY-TAU-MAX-BOUND-DERIVATION",
       comment="HK-5 closed-form '5/(1-tau/(5π))' regime-of-validity upper bound; min over Source-1 (pole 5π), Source-2 (substrate-IS structural transition), Source-3 (numerical breakdown at L_max). Per S88 W-21 V.5 derivation."
   )
   ```
9. Verify consistency with empirical breakdown observations: cross-link to S88 W-21 W6b-d_spec_B-k1-k2 workshop §V.5 (W-21 source); compare derived τ_max against W-21 empirical breakdown.
10. Cross-check at τ_fold = 0.19 << τ_max: HK-5 is valid throughout the canonical operating regime; cross-link to A.9 (d_eff Jensen perturbation second-order) shows τ_fold is well within the regime-of-validity.
11. Cross-check downstream consumers: confirm A.28 (Wave 5; τ=2·τ_fold = 0.38 cross-validation) operates within τ_max regime per A.35 bound (0.38 << 5π ≈ 15.708; safe by ~41×).
12. Emit:
    - JSON sidecar with τ_max value, source breakdown (per Source 1, 2, 3), boundary-direction verification results, downstream-consumer regime check (A.28 0.38 << τ_max).
    - PNG plot showing HK-5(τ) closed form across τ ∈ [0, 5π] with τ_fold and τ_max annotated; numerical d_eff^{L_max=12} overlay; breakdown points marked.
    - Verdict line per Schema-v2 in `computations/session-89/s89_gate_verdicts.txt`.

**Input SHA-256 pins**:
- `canonical_constants.py` — `<pinned at plan-freeze>`
- `computations/_shared/s84_spectrum_cache_L12_tau019.npz` — `<pinned at plan-freeze>` (for L_max-truncation numerical breakdown at τ_fold)
- D_K spectrum at τ ≠ τ_fold (extended τ scan) — `<computed-at-runtime>`
- `sessions/archive/session-88/workshops/s88-w21-w6b-d_spec_B-k1-k2.md` — `<pinned at plan-freeze>` (W-21 V.5 source for empirical breakdown observations)

**Cross-checks**:
- Boundary-direction Python verification at plan-author time (MANDATORY per `epistemic-discipline.md §"Pre-Registration Completeness"` Class 8.2 boundary-direction sub-check S88 W-21 V.6 / B.51)
- Source 1 (closed-form pole) derivation (MANDATORY)
- Source 2 (substrate-IS structural transition) scan (MANDATORY)
- Source 3 (numerical breakdown at L_max) scan (MANDATORY)
- Empirical breakdown consistency (MANDATORY per ledger gate criterion)
- Downstream consumer regime check: A.28 τ=0.38 cross-validation operates within τ_max regime per A.35 bound (cross-wave dependency declared in §"Wave 3 → Waves 5/6 Decision Point" below)
- Promote `tau_max_HK5_regime_FW` to canonical_constants.py with provenance (MANDATORY)

### 7. Machinery pin (PRDR)

```yaml
gate_id: S89-HK-5-REGIME-OF-VALIDITY-TAU-MAX-BOUND-DERIVATION
schema_version: R3
trigger: VERIFY
classification: GEOMETRIC
machinery_pin_map:
  tau_evaluate_canonical: 0.19  # tau_fold (R-PROTECTED); reference point well within regime
  tau_scan_range: [0.19, 5*math.pi]  # full range up to closed-form pole
  tau_scan_step: 0.5
  L_max_scan: [8, 10, 12]  # for Source-3 numerical breakdown identification
  HK_5_closed_form: "5 / (1 - tau / (5*pi))"
  source_1_pole: "5*pi ≈ 15.7079632679"  # closed-form analytic upper bound
  source_2_substrate_IS_transition: "scan for non-analytic d_eff behavior at tau in [0.19, 5*pi]"
  source_3_numerical_breakdown: "tau where |d_eff^{num}(tau) - HK_5(tau)| / |HK_5(tau)| > 0.05"
  boundary_direction_verification: "plan-author Python check; HK_5(tau_pole-) -> +inf; HK_5(tau_pole+) < 0; HK_5(0) == 5"
  downstream_consumer_check: "A.28 tau=0.38 << tau_max"
  promote_to_canonical: "tau_max_HK5_regime_FW"
  promotion_session: "S89"
  scheme: "HK-5-regime-of-validity-tau-max-bound-derivation"
  convention: "min-over-3-sources-pole-substrate-IS-numerical-breakdown"
  random_seed: N/A
  GPU_path: "N/A; closed-form + L_max-truncation numerical breakdown"
input_sha_pins:
  canonical_constants_py: <pinned at plan-freeze>
  spectrum_cache_L12_tau019_npz: <pinned at plan-freeze>
  s88_w21_w6b_d_spec_B_md: <pinned at plan-freeze>
output_4_tuple:
  value: "{tau_max (float64), source_1_pole (=5*pi), source_2_substrate_IS_transition (Optional[float64]), source_3_numerical_breakdown (Optional[float64]), boundary_direction_verification_pass (bool), promotion_status}"
  scheme: "HK-5-regime-of-validity-tau-max-bound-derivation"
  convention: "min-over-3-sources-pole-substrate-IS-numerical-breakdown"
  L_max: 12
audit_sha256: <computed at runtime via closure_hash(input_pin_map)>
```

### 8. Expected output 4-tuple
- `value`: 6-element record `{tau_max (float64), source_1_pole (= 5π), source_2_substrate_IS_transition (Optional[float64] or None), source_3_numerical_breakdown (Optional[float64] or None), boundary_direction_verification_pass (bool), promotion_status (enum: PROMOTED | DEFERRED | FAILED)}`
- `scheme`: `HK-5-regime-of-validity-tau-max-bound-derivation`
- `convention`: `min-over-3-sources-pole-substrate-IS-numerical-breakdown`
- `L_max`: `12`

### 9. PASS/FAIL/INFO thresholds with tolerance rule

- **PASS** iff:
  - (a) τ_max derived from substrate-physics first principles via min(Source-1, Source-2, Source-3) (theorem-form OR L_max-truncation numerical).
  - (b) `boundary_direction_verification_pass == True` (HK-5 boundary direction at τ_pole verified at plan-author time).
  - (c) Empirical breakdown consistency: derived τ_max consistent with W-21 V.5 empirical observations.
  - (d) Downstream consumer regime check: A.28 τ=0.38 << τ_max (regime safe).
  - (e) `promotion_status == PROMOTED` (`tau_max_HK5_regime_FW` added to canonical_constants.py).
- **INFO** iff:
  - (a) and (b) and (e) hold but (c) shows partial inconsistency (W-21 empirical breakdown ≠ derived τ_max within 50%) OR (d) marginal (A.28 τ=0.38 within 50% of τ_max margin).
- **FAIL** iff:
  - (a) fails (τ_max not derivable) OR
  - (b) FAILs (boundary direction inconsistent with HK-5 closed form) OR
  - (e) FAILS (canonical promotion blocked).
- **Tolerance rule**: THEOREM for (a) and (b); RATIO for (c) and (d); presence test for (e).

### 10. Substitution chain (boundary-direction verification at plan-author time per `epistemic-discipline.md §"Pre-Registration Completeness"` Class 8.2 boundary-direction sub-check)

```
Definitions:
  HK-5(tau)         = 5 / (1 - tau / (5*pi))
  tau_pole          = 5*pi ≈ 15.7079632679

Boundary-direction substitutions:
  Step 1: tau = 0.19 (tau_fold canonical)
          HK-5(0.19) = 5 / (1 - 0.19 / 15.7080) = 5 / (1 - 0.01210) = 5 / 0.98790 ≈ 5.06127
          [d_eff at tau_fold ≈ 5.06; small positive deviation from d=4+1=5, consistent with substrate-IS first-order Jensen perturbation]

  Step 2: tau = tau_pole - 0.001 = 15.7069...
          HK-5(15.7069) = 5 / (1 - 15.7069 / 15.7080) = 5 / 0.0000700 ≈ 71428
          [d_eff diverges to +inf; HK-5 closed form is APPROACHING the pole from below; valid regime]

  Step 3: tau = tau_pole + 0.001 = 15.7090...
          HK-5(15.7090) = 5 / (1 - 15.7090 / 15.7080) = 5 / (-0.0000638) ≈ -78400
          [d_eff is NEGATIVE; physical d_eff must be positive; HK-5 closed form is INVALID above tau_pole]

  Step 4: tau = 0 (trivial limit)
          HK-5(0) = 5 / (1 - 0) = 5
          [d_eff = 5 in the small-tau limit; consistent with substrate's intrinsic dimension contribution]

Conclusion: HK-5 boundary direction at tau_pole = 5*pi is verified.
            Below tau_pole: HK-5 is positive and finite (valid regime).
            Above tau_pole: HK-5 is negative (invalid for physical d_eff).
            Therefore tau_max <= tau_pole = 5*pi from Source-1 (closed-form pole).
            Final tau_max = min(5*pi, tau_substrate_IS_transition, tau_numerical_breakdown).

Direction: tau_max is strictly bounded above by 5*pi.
           The substrate-IS regime-of-validity is the half-line tau in [0, tau_max).
           For tau >= tau_max, HK-5 is INVALID; substrate-IS d_eff must be computed numerically OR via Source-2/Source-3 alternative closed forms.
```

### 11. What PASSES/FAILS MEAN for solution space

- **PASS**: HK-5 closed-form regime-of-validity τ_max is substrate-derivable. The substrate's d_eff structure has a well-characterized validity boundary at τ_max; HK-5 is the exact substrate-IS representation below τ_max and breaks down above. `tau_max_HK5_regime_FW` becomes a canonical_constants.py entry. Cross-link to A.9 (d_eff second-order Jensen perturbation at τ_fold) and A.29 (κ_2 substrate at second order): A.9 + A.29 + A.35 jointly characterize d_eff to second order at τ_fold, with regime boundary at τ_max ≤ 5π.
- **INFO**: τ_max derived but empirical breakdown consistency partial; W-21 V.5 empirical observations not fully aligned. Cross-link to S90 forward gate for refined empirical breakdown observation.
- **FAIL**: τ_max not derivable from substrate-physics first principles OR boundary-direction verification fails. Either (i) HK-5 closed form is wrong (contradicts S87 d_eff workshop) OR (ii) substrate-IS d_eff has no well-defined regime-of-validity (contradicts substrate canonicity). Both routes to S90 plan-freeze halt with mandatory remediation.

### 12. Effort estimate
**0.6 wave-equivalents** — closed-form analytic derivation (Source-1) + Source-2 substrate-IS scan + Source-3 numerical breakdown identification + boundary-direction verification + canonical promotion.

### 13. Substrate framing per `phononic-framing.md` IS-not-IN

The substrate IS the heat-kernel structure of D_K^2; HK-5 closed form `5/(1−τ/(5π))` IS the substrate's intrinsic d_eff representation in the regime [0, τ_max). τ_max IS the substrate-IS regime-of-validity boundary; above τ_max, the substrate's spectral structure reorganizes (Source-2 substrate-IS transition) or the closed form becomes singular (Source-1 analytic pole) or numerical truncation breaks (Source-3).

**FORBIDDEN container-thinking**:
- "HK-5 is valid IN some range of tau"
- "The closed form approximates the substrate"

**REQUIRED substrate-IS framing**:
- HK-5 IS the substrate's intrinsic d_eff representation below τ_max; it is exact, not approximate.
- τ_max IS the substrate's intrinsic regime-of-validity boundary; the substrate's spectral structure reorganizes at the boundary.
- The 3 sources (closed-form pole, substrate-IS structural transition, numerical breakdown) are 3 independent substrate-IS criteria for the regime boundary.

---

## Wave 3 → Waves 5/6 Decision Point

Wave 3 produces 3 cross-wave outputs feeding Wave 5 and Wave 6:

### Cross-wave output 1: A.14 → W6 A.41 D_max measurement

- **Producer**: A.14 `S89-SUBSTRATE-COCYCLE-RATIO-REGULATOR-CLASS-INVARIANCE-SCAN` (Wave 3)
- **Consumer**: A.41 `S89-D-MAX-MEASUREMENT-W9B-2-VS-FULL-PV-PIPELINE` (Wave 6)
- **Dependency**: A.41 reads regulator-class invariant baseline from A.14 npz (the baseline is the substrate cocycle ratio canonical 7.324992 verified across 4 regulators); A.41 measures D_max of W9b-2 SCHEMATIC output against this FULL physical regularization baseline.
- **Forward declaration**: A.14 npz output `s89_w3_substrate_cocycle_ratio_regulator_class_invariance_scan.npz` MUST be available before A.41 dispatch. Cross-wave dispatch order: Wave 3 PASS → Wave 6 dispatch.

### Cross-wave output 2: A.9 → W5 A.8 d_eff Richardson scan

- **Producer**: A.9 `S89-D-EFF-CM-1995-SECTION-III-4-SECOND-ORDER-JENSEN-PERTURBATION` (Wave 3)
- **Consumer**: A.8 `S89-D-EFF-RICHARDSON-LMAX-18-LMAX-14-BASELINE-SCAN` (Wave 5)
- **Dependency**: A.8 anchors against A.9 closed-form `c` coefficient for residual extraction (residual(L_max) = d_eff^{numerical}(L_max) − HK-5(τ_fold) − c·τ²); A.8's PASS predicate `residual(18) ≤ 0.5 × residual(14)` requires substrate-derived `c` from A.9.
- **Forward declaration**: A.9 npz output `s89_w3_d_eff_cm1995_second_order_jensen_perturbation.npz` MUST be available before A.8 dispatch. Cross-wave dispatch order: Wave 3 PASS → Wave 5 dispatch.

### Cross-wave output 3: A.35 → W5 A.28 τ=2·τ_fold cross-validation

- **Producer**: A.35 `S89-HK-5-REGIME-OF-VALIDITY-TAU-MAX-BOUND-DERIVATION` (Wave 3)
- **Consumer**: A.28 `S89-TAU-2X-FOLD-CROSS-VALIDATION-READING-A-VS-READING-B` (Wave 5)
- **Dependency**: A.28 must verify τ=2·τ_fold = 0.38 is within τ_max regime per A.35 bound; if τ=0.38 ≥ τ_max (predicted FALSE per boundary-direction substitution chain showing 0.38 << 5π ≈ 15.708), A.28 falls outside the regime-of-validity and PASS-A vs PASS-B discriminator becomes structurally invalid.
- **Forward declaration**: A.35 npz output `s89_w3_hk5_regime_tau_max_bound_derivation.npz` MUST be available before A.28 dispatch. Cross-wave dispatch order: Wave 3 PASS → Wave 5 dispatch.

### Wave 3 internal dependencies

- **A.18 depends on A.14, A.16, A.17** (criterion C1, C3, C5 cross-link). Wave 3 internal dispatch order:
  1. **First sub-batch (parallel-eligible)**: A.2, A.9, A.14, A.16, A.17, A.29, A.32, A.35 (8 gates dispatched together).
  2. **Second sub-batch (sequential after first batch)**: A.18 (depends on A.14 PASS + A.16 PASS + A.17 PASS).
- **A.18 fallback**: if any of A.14 / A.16 / A.17 FAILs, A.18 emits INFO with criterion-satisfaction matrix and routes to S90 plan-freeze halt with mandatory remediation.

---

## Wave 3 Machinery-Enumeration Pin (§0.11)

Per `.claude/templates/pru-pre-registration-template.md` PRDR scaffold + `epistemic-discipline.md §"Pre-Registration Completeness"` PRDR keyword 8-K-atom enumeration:

| Gate ID | scheme | convention | L_max | tolerance | regulator (if scan) | random_seed | GPU path |
|:--------|:-------|:-----------|:------|:----------|:--------------------|:------------|:---------|
| S89-XI-KZ-SUBSTRATE-NATURAL-DERIVATION-FROM-T1-ATLAS (A.2) | substrate-natural-T1-atlas-derivation | BdG-A_2-transition-class-fold-anchored | 12 | THEOREM (closed-form) + RATIO 200% (numerical) | N/A | N/A | N/A |
| S89-D-EFF-CM-1995-SECTION-III-4-SECOND-ORDER-JENSEN-PERTURBATION (A.9) | CM-1995-section-III-4-second-order-Jensen-perturbation | TT-deformation-fold-anchored-band-0-projector | 12 | RATIO ≤ 5% (PASS); 5%-20% (INFO) | {ζ, Pauli-Villars, Mellin, sharp-cutoff} | N/A | torch.linalg if dim ≥ 100×100 |
| S89-SUBSTRATE-COCYCLE-RATIO-REGULATOR-CLASS-INVARIANCE-SCAN (A.14) | 4-regulator-atlas-substrate-cocycle-ratio-invariance | regulator-class-invariance-FULL-pin | 10 | RATIO ≤ 0.1% (PASS); 0.1%-1% (INFO) | {ζ, Pauli-Villars, Mellin, sharp-cutoff} | N/A | torch.linalg if dim ≥ 100×100 |
| S89-V4-SAGE-QQ-ENUMERATION-EXTENDED-SECTORS (A.16) | V_4-triality-Sage-QQ-enumeration-extended-sectors | L_max-scan-bot20-sector-occupation-cocycle-functor-F-invariance | 12 | THEOREM (Sage-QQ exact) | N/A | N/A | N/A |
| S89-SUBSTRATE-CLOCK-CANCELLATION-DISCRIMINATING-PREDICATE-GATE (A.17) | substrate-clock-pinning-A-vs-mode-density-pinning-B | g-scan-143-322-384 | N/A | RATIO ≤ 1% magnitude; ≥ 5% discriminating | N/A | N/A | N/A |
| S89-SUBSTRATE-CLOCK-PINNING-UNIQUENESS-DERIVATION (A.18) | substrate-clock-pinning-uniqueness-derivation-5-criteria | L-pix-canonical-vs-mode-density-vs-GGE-anchored-candidate-space | 10 | THEOREM (criterion-satisfaction matrix) | scan via A.14 link | N/A | N/A |
| S89-HIGHER-ORDER-RESOLVENT-EXPANSION-O-TAU2-KAPPA2 (A.29) | CM-1995-section-III-4-resolvent-expansion-kappa-2 | TT-deformation-second-order-fold-anchored | 12 | RATIO ≤ 5% (PASS); ≤ 20% (INFO) | {ζ, Pauli-Villars, Mellin, sharp-cutoff} | N/A | torch.linalg if dim ≥ 100×100 |
| S89-SU-N-CROSS-VALIDATION-5PI-CHAIN (A.32) | SU-N-cross-validation-Cartan-rational-sum-5pi-chain | Cartan-rational-sum-pi-Plancherel-substrate-algebra-SU-N-extension | 8 (SU(2), SU(4)); 12 (SU(3) ref) | RATIO ≤ 5% (PASS-LOAD-BEARING); > 20% (PASS-COINCIDENCE); 5%-20% (INFO) | N/A (single Cartan-rational-sum) | N/A | torch.linalg if dim ≥ 100×100 |
| S89-HK-5-REGIME-OF-VALIDITY-TAU-MAX-BOUND-DERIVATION (A.35) | HK-5-regime-of-validity-tau-max-bound-derivation | min-over-3-sources-pole-substrate-IS-numerical-breakdown | 12 | THEOREM (closed-form pole) + RATIO 50% (empirical) | N/A | N/A | N/A |

All 9 gates' machinery is PRDR-pinned at plan-freeze. None are PRU-vulnerable (Class 8.0/8.1 cardinality clear). Schema 8.2 verifier-rubric pre-registration applies to A.16 (Sage-QQ exact match rubric) and A.18 (criterion-satisfaction matrix rubric); both rubrics are pre-registered in §6 Method of each gate. Schema 8.3 publication-precision pre-registration applies to canonical promotions (A.29 κ_2_substrate_FW; A.35 tau_max_HK5_regime_FW) — full float64 precision MANDATORY; downstream verifier rel_tol ≥ 10^(−15).

---

## Wave 3 Input-SHA Ledger

Plan-freeze SHA pinning (each input file's content_sha256 is computed at plan-freeze and inserted into the gate block's input_sha_pins field):

| File | Consumed by | SHA pin status |
|:-----|:------------|:---------------|
| `canonical_constants.py` | All 9 gates | `<pinned at plan-freeze>` |
| `computations/_shared/s84_spectrum_cache_L12_tau019.npz` | A.9, A.14, A.16, A.29, A.32, A.35 | `<pinned at plan-freeze>` |
| `sessions/archive/session-88/workshops/s88-w2-kz-universality-class.md` | A.2 | `<pinned at plan-freeze>` |
| `sessions/archive/session-88/workshops/s88-w12-w3c-57-hk5-residual-origin.md` | A.9 | `<pinned at plan-freeze>` |
| `sessions/archive/session-86/workshops/s86-w-5-hp1-quantum-metric-bridge.md` | A.14 | `<pinned at plan-freeze>` |
| `sessions/archive/session-88/workshops/s88-w7-w2-2-v4-triality.md` | A.16 | `<pinned at plan-freeze>` |
| `sessions/archive/session-88/workshops/s88-w1-substrate-clock-cancellation.md` | A.17, A.18 | `<pinned at plan-freeze>` |
| `sessions/archive/session-88/workshops/s88-w18-w6a-51-geometric-resummation.md` | A.29 | `<pinned at plan-freeze>` |
| `sessions/archive/session-88/workshops/s88-w19-w6a-cross-gate-chain.md` | A.32 | `<pinned at plan-freeze>` |
| `sessions/archive/session-88/workshops/s88-w21-w6b-d_spec_B-k1-k2.md` | A.35 | `<pinned at plan-freeze>` |
| `sessions/permanent-results-registry.md` | A.2, A.14, A.16, A.29, A.32 | `<pinned at plan-freeze>` |
| Wave 3 internal cross-links: A.14 npz, A.16 npz, A.17 npz | A.18 (criteria C1, C3, C5) | `<computed-at-runtime>` |

**Plan-freeze SHA computation step**: at plan-freeze time, the orchestrator invokes `closure_hash(input_pin_map)` per gate per `_script_template.py append_verdict()` pattern; each gate's `audit_sha256` is derived from this closure hash deterministically and emitted at runtime. No agent-memory pins (per `agent-standards.md §"AMRI"` Test 1; the only AMRI-eligible inputs are project-level files in `sessions/`, `computations/`, and `canonical_constants.py`).

**No `pending` placeholders**: all inputs are project-level files with stable SHAs at plan-freeze.

---

## Wave 3 Authorship + Dispatch Plan

| Gate | Runtime author (PRIMARY) | Co-reviewer (CO-AUTHOR) | BLACKLISTED | Dispatch path |
|:-----|:------------------------|:-----------------------|:------------|:--------------|
| A.2 | volovik-superfluid-universe-theorist | connes-ncg-theorist | hawking-theorist (per ledger), gen-physicist | COMPUTE-class via `/rclab-coordinate` |
| A.9 | connes-ncg-theorist | lizzi-spectral-functional-theorist | gen-physicist | COMPUTE-class |
| A.14 | lizzi-spectral-functional-theorist | connes-ncg-theorist | gen-physicist | COMPUTE-class |
| A.16 | connes-ncg-theorist | lizzi-spectral-functional-theorist | gen-physicist | COMPUTE-class |
| A.17 | volovik-superfluid-universe-theorist | landau-condensed-matter-theorist | gen-physicist, hawking-theorist | COMPUTE-class |
| A.18 | volovik-superfluid-universe-theorist | landau-condensed-matter-theorist | gen-physicist, hawking-theorist | COMPUTE-class (sequential after A.14, A.16, A.17) |
| A.29 | connes-ncg-theorist | lizzi-spectral-functional-theorist | gen-physicist | COMPUTE-class |
| A.32 | lizzi-spectral-functional-theorist | connes-ncg-theorist | gen-physicist | COMPUTE-class |
| A.35 | lizzi-spectral-functional-theorist | connes-ncg-theorist | gen-physicist | COMPUTE-class |

**Wave 3 dispatch waves**:
- Sub-batch 1 (8 gates parallel): A.2, A.9, A.14, A.16, A.17, A.29, A.32, A.35
- Sub-batch 2 (1 gate sequential): A.18 (after A.14, A.16, A.17 PASS or INFO)

**Concurrent-dispatch cap** (per `feedback_dispatch-discipline.md`): 8 gates in sub-batch 1 = at cap; do NOT add A.18 to sub-batch 1.

**Wave 3 → Wave 5/6 cross-dispatch**: Wave 3 outputs feed Wave 5 (A.8, A.28) and Wave 6 (A.41) per §"Wave 3 → Waves 5/6 Decision Point" above. Wave 5 and Wave 6 dispatch only after Wave 3 sub-batch 1 PASS or INFO.

---

## Wave 3 Wave-Synthesis Carry-Forward Section (post-execution)

After all 9 Wave 3 gates emit verdicts, the wave-synthesis section will be appended at the bottom of this file (per `feedback_no-asking-just-execute.md`; auto-execute T8 synthesis without asking). Carry-forwards from Wave 3 to S90+ are produced as 4-field specs (what / inputs / gate / effort) per `feedback_fix-in-session-never-defer.md`. Wave 3 in-session housekeeping items (closing-paragraph audit, cross-link cleanups, registry-state classification) are processed in-session per `CLAUDE.md §"No Technical Debt"` and do NOT propagate to S90 unless they require new substrate-physics derivation.

---

End of Wave 3 Plan.
