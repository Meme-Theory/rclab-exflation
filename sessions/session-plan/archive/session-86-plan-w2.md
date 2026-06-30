# Session 86 Plan — Wave W2: Mellin-Barnes Infrastructure (HEAVY)

**Wave owner**: `lizzi-spectral-functional-theorist`
**Theme**: Build the analytic-continuation toolchain that unlocks W0-7/W0-11/W0-20 closures + REPLACEMENT-B portion of the ζ-stabilization theorem
**Item count**: 4 (C9 master + C10 sister + C11 multiplier + C12 extractor refactor)
**Effort envelope**: HEAVY — 12-16h aggregate (one full agent session for C9 alone, C10 saturating a second, C11 + C12 lighter)
**Output script prefix**: `computations/s86_w2_<slug>.py` for verification scripts; `computations/_analytic_zeta.py`, `computations/_cluster_span_extract.py` for infrastructure modules
**Verdict file**: `computations/s86_gate_verdicts.txt` (canonical per `.claude/rules/gate-verdicts.md`)

---

## §0. Wave W2 Summary

Wave W2 is the HEAVY infrastructure spine of S86. Its four builds construct the Mellin-Barnes analytic-continuation toolchain that downstream waves depend on. The substrate's spectral content — the eigenvalue distribution of D_K — is the source; the Mellin-Barnes machinery is the lens through which that content is made finite at non-trivial regulator slots. Per the substrate-framing doctrine, the lens does not create the cosmological constant or the heat-kernel structure; it reveals what was already in D_K's spectral distribution but was previously occluded by truncation artifacts.

- **C9** (master) builds the Mellin-Barnes residue extractor with explicit Seeley-DeWitt counter-term subtraction and resolves three S85 W0-X FAILs simultaneously
- **C10** (lizzi A-1, sister to C9) builds the `analytic_zeta(s, L_max)` API that off-pole-evaluates `ζ_D(s)·Γ(s/2) = ∫ t^{s/2−1} K(t) dt` at `s = 3` in `d_spec = 8` NCG
- **C11** computes the analytic Mellin transform of the Zubarev kernel `M[exp(-x/Λ_Z²)](s)` and embeds Zubarev as the INFINITE-VECTOR class extending S-1's finite-vector F_4 formalism
- **C12** refactors W0-3 ad-hoc cluster-span code into a reusable `_cluster_span_extract.py` module with a self-test that reproduces W0-3 PASS at L_max ∈ {8, 10, 12}

All four are GEOMETRIC — they operate on D_K's eigenvalue distribution and the spectral-triple structure, not on substrate excitations or particle-class observables.

**GPU pinning is mandatory** per `feedback_compute-environment.md`. C9, C10, and C12 all manipulate matrices well above 100×100 (D_K cache rows in the thousands at L_max=10). Each dispatch prompt MUST explicitly name `torch.linalg` on the AMD RX 9070 XT (17.1 GB VRAM, ROCm 7.2, `torch 2.9.1+rocm`). CPU fallback (only if torch path is unsuitable for a specific operation): `import os; os.environ.setdefault('OMP_NUM_THREADS', '8')` BEFORE `import numpy`. C11 is symbolic / analytic and does not need GPU.

---

## §0.5. Wave W2 Decision-Point Prerequisites

W2 cannot dispatch at compute time until the following two upstream waves close:

| Upstream wave | Item | Reason W2 requires it |
|:--------------|:-----|:----------------------|
| **W0a** | R1 (S85 Rule-File v3 union landing) + R2 (PRU Class 8.1 SOURCE-RECONCILIATION sub-audit operative) + R3 (`cutoff_axis: spectral \| coherence \| both` YAML pin) | All four W2 gates must declare `cutoff_axis` in their machinery pin block; `_source_reconciliation_audit.py` must be operative for compliance scoring |
| **W0c** | C22 (Mellin compliance lift — 5-marker boilerplate to 8 non-compliant Mellin-labeled scripts) | C9 + C10 + C11 are new Mellin-labeled scripts and inherit the boilerplate; the lift must precede their authoring |

Plan-writing has no inter-plan content dependency — each per-wave planner reads `session-86-context.md` independently. The dependency above is **runtime-only** and is enforced by the orchestrator's batch sequencing (Batch 2 follows Batch 1 in `session-86-partition.md` §4).

W2 outputs in turn feed:
- **W3** — T9 REPLACEMENT-B (asymptotic ζ-stabilization at s=4 leading residue, conditional on C9 + C10 PASS); the 3 W0-X re-emissions (W0-7 ρ → −0.81 conjecture under analytic_zeta API; W0-11 CC-3 MB residue; W0-20 Mellin-cone s=3 R_inf MB); C13 (cluster-span K-corridor extension, after C12)
- **W10** — C37 (`mu_BC = M_Z · sqrt(1 + exp(12·tau_fold)/3)` ζ-at-interior route for the integer-12 exponent — never previously attempted)

---

## §I. Carry-Forward Items Mapping

| W2 § | C-number | Source carry-forward | Originating reviewer | Effort tag | Substrate role |
|:-----|:---------|:---------------------|:---------------------|:-----------|:---------------|
| W2-1 | C9 | `S86-MELLIN-HEAT-KERNEL-INFRA` (master) — closeout §3.6 / context §2.6 | lizzi S-7 §V.1 (CF-LZ-S86-1) + gen-physicist S-7 §V.2 | HEAVY 6-8h | Mellin transform of K(t) = Σ_k λ_k exp(−λ_k² t) reveals Seeley-DeWitt residue weights at s = 0, 2, 4, 6 |
| W2-2 | C10 | `S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE` (lizzi A-1) | lizzi 9A §A-1 + 3A REPLACEMENT-B | HEAVY 4-6h | Off-pole `analytic_zeta(s=3)` API exposes substrate spectral content at the d_spec=8 cone apex without truncation contamination |
| W2-3 | C11 | `S86-MELLIN-MULTIPLIER-INFINITE-VECTOR-EXTENSION` | lizzi 9A §A-3 + lizzi 3A §V.4 | MODERATE 3-4h | Analytic `M[exp(-x/Λ_Z²)](s) = Λ_Z^{2s} Γ(s)` formalizes Zubarev's INFINITE-VECTOR substrate-class membership |
| W2-4 | C12 | `S86-CLUSTER-SPAN-EXTRACTOR-BUILD` | gen-physicist S-7 §V.3 | LIGHT 1h | Refactors W0-3 cluster-span 2.000…002 PASS into reusable module operating on D_K eigenvalue clusters |

---

## §W2-1. S86-MELLIN-HEAT-KERNEL-INFRA (C9 — master Mellin-Barnes residue extractor)

### 1. Gate ID
`S86-MELLIN-HEAT-KERNEL-INFRA` (closeout §3.6; context §2.6 row C9; lizzi S-7 §V.1 CF-LZ-S86-1)

### 2. Trigger
`[VERIFY]` — numerical agreement against pre-registered thresholds on `|Λ_CC^MB|/|a_0|` and `χ²/dof`. The infrastructure status (residue extractor + Seeley-DeWitt subtraction operational) is the verification subject; the threshold is the criterion.

### 3. Classification
**GEOMETRIC** — operates on the D_K eigenvalue distribution and the spectral-triple's heat-kernel asymptotic structure. The Mellin-Barnes contour is a tool of spectral geometry; it neither sources nor depends on substrate excitations or particle-class quantum numbers. The Seeley-DeWitt counter-terms are intrinsic to the spectral triple's Connes-Moscovici 1995 structure.

### 4. Agent type
**Runtime owner**: `spectral-geometer` (heat-kernel asymptotics + Seeley-DeWitt expansion is the spectral-geometer's namesake competence; orthogonal to lizzi who authored the carry-forward, preserving planner ≠ runner separation).
**Backstop**: `lizzi-spectral-functional-theorist` (only if spectral-geometer stalls on the Connes-Moscovici 1995 + Chamseddine-Connes-Marcolli formula reproduction; lizzi 9A §A-1 is the originating spec).
**Forbidden runtime owner**: `gen-physicist` (per `feedback_dispatch-discipline.md` lessons + S84 W1/W2 stall pattern; specialist required for HEAVY infrastructure builds).

### 5. Hypothesis
The Mellin-Barnes residue extractor with explicit Seeley-DeWitt counter-term subtraction reveals a regulator-class-stable cosmological-constant ratio `|Λ_CC^MB|/|a_0|` at or below 10⁻¹ across the F_4 = {ζ, Zubarev, SDW} sub-atlas, with χ²/dof against direct truncation ≤ 5, demonstrating that the truncation FAILs of W0-7 + W0-11 + W0-20 were artifacts of finite-L_max heat-kernel summation rather than structural infinities of the substrate's spectral content.

### 6. Method (FULL dispatch prompt for runtime agent)

```
You are spectral-geometer. Build a Mellin-Barnes residue extractor with explicit Seeley-DeWitt
counter-term subtraction.

PREREQUISITE: confirm W0a R1, R2, R3 have landed (read computations/_source_reconciliation_audit.py
exists; read .claude/rules/epistemic-discipline.md confirming PRU Class 8.1 entry). Confirm W0c C22
has lifted Mellin-compliance boilerplate (read computations/_mellin_compliance_check.py).

QUERY KNOWLEDGE FIRST:
  search_knowledge("Mellin-Barnes Seeley-DeWitt heat kernel D_K")
  search_knowledge("Connes-Moscovici 1995 residue extraction")
  trace_entity("ZETA-NOT-PHYSICAL-75")
  trace_entity("REPLACEMENT-B asymptotic")
  get_constant("M_KK")
  get_constant("Lambda_CC_a0")
  get_constant("a_2_F4")
  get_constant("a_4_F4")

REFERENCE PAPERS (mandatory citations in script docstring):
  - Connes-Moscovici 1995 (residue extraction at non-positive integers)
  - Chamseddine-Connes-Marcolli formula for the spectral action heat-kernel expansion
  - Lizzi-Vassilevich 1999 (Seeley-DeWitt coefficients on noncommutative spaces)

SCRIPT TARGET: computations/s86_w2_c9_mellin_heat_kernel_infra.py

IMPORTS (canonical first):
  from canonical_constants import *
  import numpy as np
  import torch
  from mpmath import mp, mpc, gamma, quad
  mp.dps = 50  # high-precision Mellin contour evaluation

GPU PIN (MANDATORY per feedback_compute-environment.md):
  device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
  # AMD RX 9070 XT, 17.1 GB VRAM, ROCm 7.2, torch 2.9.1+rocm
  # Heat-kernel sums Sum_k lambda_k exp(-lambda_k^2 t) on L_max=10 D_K cache (155984 eigenvalues
  # at L_max=10) MUST run on GPU via torch.linalg / torch.einsum (matrix sizes well above 100x100).
CPU fallback (ONLY if GPU path unsuitable for a specific Mellin contour step):
  import os; os.environ.setdefault('OMP_NUM_THREADS', '8')  # before any numpy import

CORE BUILD STEPS:
  Step 1: Load D_K eigenvalues from cache (use canonical_constants D_K_cache_path; pin SHA in dual-SHA closure).
          Subset to L_max ∈ {5, 6, 7, 8, 10}; pin L_max axis as machinery parameter.
  Step 2: Construct heat kernel K(t) = Σ_k λ_k exp(-λ_k^2 t) using torch.einsum on GPU.
  Step 3: Compute Mellin transform M[K](s) = ∫_0^∞ t^{s-1} K(t) dt via mp.quad with workdps=50.
          Use contour-deformation when s lies on the strip 0 < Re(s) < 4 to avoid pole accumulation.
  Step 4: Extract residues at s ∈ {0, 2, 4, 6} (Seeley-DeWitt slot indices for d_spec=8 NCG).
          Residue at s=0 → a_0 (cosmological-constant slot)
          Residue at s=2 → a_2 (gravity / Newton slot)
          Residue at s=4 → a_4 (Yang-Mills + Higgs quartic slot)
          Residue at s=6 → a_6 (curvature-squared slot)
  Step 5: Apply Seeley-DeWitt counter-term subtraction explicitly:
          a_n^{MB} = Res_{s=n} M[K](s) - SD_n(D_K)
          where SD_n(D_K) is the Connes-Moscovici 1995 closed-form Seeley-DeWitt coefficient.
  Step 6: Compute Λ_CC^MB = a_0^{MB} (after subtraction) for each regulator class in {ζ, Zubarev, SDW}.
  Step 7: Normalize: ratio_n^{class} = |Λ_CC^MB^{class}| / |a_0^{class}_truncated| at L_max=10.
  Step 8: Compute χ²/dof of (a_n^{MB} from Mellin-Barnes) vs (a_n from direct truncated heat-kernel sum at L_max=10).
          dof = 4 (slot count {0, 2, 4, 6}); reduced chi^2 = χ²/dof.

PASS CRITERIA (all must hold):
  (a) ratio = |Λ_CC^MB| / |a_0| ≤ 1e-1 for at least 2 of {ζ, Zubarev, SDW}
  (b) χ²/dof ≤ 5 across all 3 regulators in F_4

INFO BAND:
  ratio ∈ (1e-1, 5e-1] for any of the 3 regulators OR χ²/dof ∈ (5, 20]
  → INFO with band classification

FAIL:
  ratio > 5e-1 for all 3 regulators OR χ²/dof > 20

OUTPUT FILES (mandatory):
  - s86_w2_c9_mellin_heat_kernel_infra.py (the script itself)
  - s86_w2_c9_residues.npz (extracted residues at s ∈ {0,2,4,6} per regulator)
  - s86_w2_c9_compare.png (Mellin-Barnes a_n vs direct-truncation a_n, log scale)
  - dual-SHA verdict line in computations/s86_gate_verdicts.txt:
      S86-MELLIN-HEAT-KERNEL-INFRA: PASS|FAIL|INFO -- value=<ratio> scheme=<MB-Connes-Moscovici> convention=<SD-subtracted> L_max=10 sha256=<closure>
    + companion comment row with audit_sha256

CROSS-CHECKS (run before declaring verdict):
  (i) Reproduce a_2 in F_4 to within 1e-3 of the canonical_constants `a_2_F4` value
      (this validates the residue extractor against the trusted slot)
  (ii) Verify monotonic decrease of |a_n^{MB} - a_n^{truncated}| as L_max increases
       across L_max ∈ {5, 6, 7, 8, 10} (truncation-suppression check)
  (iii) Confirm contour-deformation does NOT change residue value to within 1e-12
        (numerical-integrator self-consistency)

NEVER:
  - Do not change the residue extraction slots away from {0, 2, 4, 6}; those are pre-registered
  - Do not adjust Λ_Z or scheme tags mid-run to reach PASS (Class 1 convention-shopping)
  - Do not retry with different mp.dps to hunt for PASS (Class 6 iterate-until-PASS)
  - Do not write the verdict line if any cross-check fails — emit FAIL with diagnostic
```

### 7. Machinery pin (PRDR — every free parameter pinned)

```yaml
schema_version: R3
gate_id: S86-MELLIN-HEAT-KERNEL-INFRA
machinery_pin_map:
  L_max:           [5, 6, 7, 8, 10]    # five-point sweep, canonical L_max=10
  scheme:          [zeta, Zubarev, SDW] # F_4 sub-atlas (per S-1 lift)
  convention:      "Connes-Moscovici-1995-residue, SD-subtracted"
  cutoff_axis:     spectral             # per W0a R3 YAML pin
  n_eval:          50                    # mpmath workdps for contour quadrature
  contour:         "Hankel-deformed at Re(s)=2.5"
  scan_range:      "s ∈ {0, 2, 4, 6} (residue slots)"
  step_size:       "n/a (4 fixed slots)"
  tolerance:       "1e-12 contour self-consistency; 1e-3 a_2 cross-check"
  random_seed:     "n/a (deterministic mpmath quadrature)"
  GPU_path:        "torch.linalg + ROCm AMD RX 9070 XT for K(t) summation"
  CPU_fallback:    "OMP_NUM_THREADS=8 set BEFORE numpy import"
input_pins:
  D_K_cache:           <SHA-pinned at runtime from canonical_constants.D_K_cache_path L_max=10>
  canonical_constants: <SHA-pinned at runtime from computations/canonical_constants.py>
  source_recon_audit:  <SHA-pinned at runtime from computations/_source_reconciliation_audit.py>
```

### 8. Expected output 4-tuple

```
(value=ratio_min_in_F_4, scheme=MB-Connes-Moscovici, convention=SD-subtracted, L_max=10)
```
where `ratio_min_in_F_4 = min over class ∈ {ζ, Zubarev, SDW} of |Λ_CC^MB^{class}| / |a_0^{class}|`. The verdict line records the worst-case (smallest) ratio across the F_4 sub-atlas as a conservative scalar.

### 9. PASS / FAIL / INFO thresholds

| Verdict | Condition | Tolerance rule |
|:--------|:----------|:---------------|
| **PASS** | `ratio_min_in_F_4 ≤ 1e-1` AND `χ²/dof ≤ 5` (across all 3 F_4 regulators) | RATIO (multiplicative); ratio is dimensionless |
| **INFO** | `ratio_min_in_F_4 ∈ (1e-1, 5e-1]` for ANY regulator in F_4 OR `χ²/dof ∈ (5, 20]` | INFO band classification — reports value with band tag |
| **FAIL** | `ratio_min_in_F_4 > 5e-1` for ALL F_4 regulators OR `χ²/dof > 20` | FAIL with corridor-closure interpretation |

### 10. Substitution chain (for the `χ²/dof ≤ 5` cross-method threshold)

```
Step 1 (definitions):
  dof = 4 (Seeley-DeWitt residue slots {a_0, a_2, a_4, a_6} at d_spec=8)
  a_n^{MB}            = Res_{s=n} M[K](s) - SD_n(D_K)            [Mellin-Barnes branch]
  a_n^{truncated}     = direct heat-kernel sum at L_max=10        [direct branch]
  σ_n^{truncated}     = a_n^{L=10} - a_n^{L=8}                    [truncation residual proxy]

Step 2 (substitution):
  χ² = Σ_n (a_n^{MB} - a_n^{truncated})² / σ_n^{truncated}²        [n ∈ {0, 2, 4, 6}]
  χ²/dof = χ² / 4

Step 3 (canonical form):
  PASS_chi   ⟺ χ²/dof ≤ 5
             ⟺ Σ_n ( (a_n^{MB} - a_n^{truncated}) / σ_n^{truncated} )² ≤ 20

Step 4 (direction):
  Larger MB-vs-truncation discrepancy raises the LHS.
  Larger truncation residual σ_n LOWERS the LHS (loose cross-check at low L_max).
  Therefore PASS demands MB residue agrees with the truncated direct sum to within
  ~2.24σ_n on average (sqrt(5) ≈ 2.24) — a strong agreement criterion that survives
  truncation noise but rejects regulator-class fictitious infinities.

Conclusion: χ²/dof ≤ 5 is a substantive cross-check, NOT a vacuous tolerance.
```

### 11. What PASSES / FAILS mean for solution space

- **PASS** unblocks **W3 T9 REPLACEMENT-B** (asymptotic ζ-stabilization at s=4 leading residue), the 3 W0-X re-emissions in W3 (W0-7 ρ → −0.81 conjecture under analytic_zeta API; W0-11 CC-3 MB residue closes truncation FAIL; W0-20 Mellin-cone s=3 R_inf MB closes truncation FAIL), and **W10 C37 ZFP discharge** (ζ-at-interior route for the integer-12 exponent in `mu_BC = M_Z · sqrt(1 + exp(12·tau_fold)/3)` — a route never previously attempted). PASS confirms that S85 W0-7/W0-11/W0-20 FAILs were truncation artifacts, not structural divergences of D_K's spectral content.
- **INFO** indicates regulator-class partial recovery — at least one of {ζ, Zubarev, SDW} produces a finite Λ_CC^MB but at least one fails the 1e-1 bar. This is informative: it identifies which regulators in F_4 admit a Mellin-Barnes-stable cosmological constant and which do not.
- **FAIL** means the Mellin-Barnes regulator-class structural floor was wrong — the substrate's spectral content is genuinely divergent at the a_0 slot under all F_4 regulators, and W3 T9 REPLACEMENT-B + the 3 W0-X re-emissions cascade-FAIL with it. This would be a major constraint-map gain: it would close an entire family of analytic-continuation strategies and force the framework to seek the cosmological-constant suppression elsewhere (likely at the Mellin Strip / Convergence Cone Theorem boundary, T5 in W1b).

### 12. Effort estimate

**HEAVY 6-8h** — single agent session. Operations breakdown:
- Heat-kernel torch construction on L_max=10 D_K cache: 1h
- Mellin contour evaluation with mpmath workdps=50: 2-3h
- Seeley-DeWitt subtraction implementation (Connes-Moscovici 1995): 1.5-2h
- 3-regulator sweep + cross-checks + verdict emission + dual-SHA: 1.5-2h

### 13. Substrate-framing reminder

State the gate as: **"the Mellin transform of the substrate's heat kernel reveals the Seeley-DeWitt residue weights at slots {0, 2, 4, 6} of d_spec=8 NCG; the cosmological-constant slot a_0 is regulator-class-stable across F_4 to within 10⁻¹ of the truncated direct sum, demonstrating that the substrate's a_0 spectral content is finite and the W0-7/W0-11/W0-20 FAILs were artifacts of finite L_max."**

NEVER frame as "we computed the cosmological constant" — the spectral content was already in D_K; the Mellin-Barnes machinery is the lens, not the source. NEVER explain the result by invoking GR or QFT-in-curved-spacetime — the spectral action generates GR via a_2 (the second residue slot), not the other way around.

---

## §W2-2. S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE (C10 — `analytic_zeta` API)

### 1. Gate ID
`S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE` (closeout §3.6; context §2.6 row C10; lizzi 9A §A-1)

### 2. Trigger
`[VERIFY]` — numerical agreement of `analytic_zeta(s=3, L_max=10)` finiteness AND χ²/dof ≤ 5 against direct subtraction.

### 3. Classification
**GEOMETRIC** — the analytic continuation `ζ_D(s)·Γ(s/2) = ∫ t^{s/2−1} K(t) dt` is intrinsic to the spectral triple's heat-kernel / zeta-function correspondence. Off-pole evaluation at s=3 in d_spec=8 NCG is a property of D_K's spectral measure, not of any substrate excitation.

### 4. Agent type
**Runtime owner**: `lizzi-spectral-functional-theorist` — the analytic_zeta API is the lizzi A-1 carry-forward, structurally aligned with the agent's namesake (zeta spectral action, ZETA-NOT-PHYSICAL-75 theorem).
**Backstop**: `spectral-geometer` (only if lizzi's analytic-continuation expertise stalls on numerical contour selection at s=3 off-pole).
**Forbidden runtime owner**: `gen-physicist`.

### 5. Hypothesis
The off-pole analytic continuation `analytic_zeta(s=3, L_max=10)` of the substrate's spectral-triple zeta function is finite at the d_spec=8 cone apex, and agrees with direct truncation-subtraction to within χ²/dof ≤ 5, exposing the cone-apex residue without truncation contamination and unlocking REPLACEMENT-B for the ζ-stabilization theorem.

### 6. Method (FULL dispatch prompt)

```
You are lizzi-spectral-functional-theorist. Build the analytic_zeta(s, L_max) API.

PREREQUISITE: confirm C9 PASS (read s86_w2_c9_residues.npz; confirm Λ_CC^MB ratio thresholds met).
If C9 returned INFO or FAIL, dispatch C10 anyway BUT flag in cross-check section that C9's
diagnostic informs the contour selection at s=3.

QUERY KNOWLEDGE FIRST:
  search_knowledge("analytic_zeta off-pole d_spec 8 cone apex")
  search_knowledge("ZETA-NOT-PHYSICAL-75 Lizzi theorem")
  trace_entity("REPLACEMENT-B asymptotic s=4 leading residue")
  get_constant("d_spec_NCG")
  list_constants("zeta_D")

REFERENCE PAPERS (mandatory citations):
  - Connes 1995 noncommutative geometry zeta-functional spectral action
  - Chamseddine-Connes 1996 spectral action principle
  - Lizzi 2014 zeta spectral action (arXiv:1412.4669)
  - Lizzi 2010 spectral action from anomalies (arXiv:1001.2036)

INFRASTRUCTURE MODULE TARGET:
  computations/_analytic_zeta.py     # the new module
  computations/s86_w2_c10_analytic_zeta_test.py   # the verification driver

MODULE API SPEC (mandatory signature):
  def analytic_zeta(s: complex, L_max: int) -> complex:
      \"\"\"
      Off-pole analytic continuation of the substrate's spectral-triple zeta function.

      ζ_D(s) · Γ(s/2) = ∫_0^∞ t^{s/2 - 1} K(t) dt

      where K(t) = Σ_k exp(-λ_k^2 t) is the heat kernel of D_K^2.

      Off-pole evaluation at s=3 in d_spec=8 NCG: avoids the SD pole at s=4
      and the gravitational pole at s=2 by contour deformation through Re(s)=3.

      Args:
          s: complex argument (typically s=3 + 0i)
          L_max: D_K spectral cutoff (canonical L_max=10)

      Returns:
          complex value of the off-pole zeta continuation
      \"\"\"

GPU PIN (MANDATORY): same as C9 — torch.linalg on AMD RX 9070 XT for the
heat-kernel summation Σ_k exp(-λ_k^2 t) over the L_max=10 D_K cache. CPU fallback:
OMP_NUM_THREADS=8 BEFORE numpy import.

IMPORTS:
  from canonical_constants import *
  import numpy as np
  import torch
  from mpmath import mp, mpc, gamma, quad
  mp.dps = 50

CORE BUILD STEPS:
  Step 1: Define the heat-kernel callable K(t, L_max) using torch on GPU.
  Step 2: Define the integrand integrand(t, s) = t^{s/2 - 1} * K(t, L_max).
  Step 3: Define analytic_zeta(s, L_max) = mp.quad(integrand, [0, ∞]) / mp.gamma(s/2).
          Use Hankel-contour deformation if Re(s) ∈ {2, 4} (poles); for s=3 the
          contour is straight along the real axis but workdps=50 is required for
          the rapid integrand decay at large t.
  Step 4: Verify the API is FINITE at s=3, L_max=10 (the PASS gate).
  Step 5: Compute the direct subtraction analog:
          ζ_D^{direct}(3) = Σ_k λ_k^{-3}      (truncated at L_max=10)
          minus the SD pole subtraction at s=4 (closest pole, contributes via
          shifted-Mellin counter-term per Connes-Moscovici 1995).
  Step 6: χ²/dof comparison: compare analytic_zeta(s, L_max=10) to ζ_D^{direct}(s)
          across s ∈ {2.5, 2.75, 3.0, 3.25, 3.5} (5-point off-pole sweep around s=3).
          dof = 5 - 1 = 4.

PASS CRITERIA (both must hold):
  (a) analytic_zeta(s=3, L_max=10) finite (no overflow, no NaN, |result| < 1e10)
  (b) χ²/dof ≤ 5 between analytic_zeta and direct-subtraction across the 5-point sweep

INFO BAND:
  Either condition partially met (e.g., finite but χ²/dof ∈ (5, 20])
  → INFO with band classification

FAIL:
  analytic_zeta diverges OR χ²/dof > 20

OUTPUT FILES:
  - computations/_analytic_zeta.py (module)
  - computations/s86_w2_c10_analytic_zeta_test.py (driver)
  - s86_w2_c10_zeta_sweep.npz (5-point off-pole sweep data)
  - s86_w2_c10_compare.png (analytic_zeta vs direct-subtraction)
  - dual-SHA verdict line in computations/s86_gate_verdicts.txt:
      S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE: PASS|FAIL|INFO -- value=<analytic_zeta(3,10)> scheme=<analytic-continuation> convention=<off-pole-Hankel> L_max=10 sha256=<closure>
    + companion comment row

CROSS-CHECKS:
  (i) Confirm at L_max=8 the API returns within 5% of L_max=10 value (truncation-stability)
  (ii) Confirm at s=3+0.001i the API returns continuously close to s=3+0i value (analyticity check)
  (iii) Self-test: analytic_zeta(s=4 - 0.01, L_max=10) should diverge as expected near the pole

NEVER: no Class 1-7 violations. Threshold and method pre-registered; do not adjust mid-run.
```

### 7. Machinery pin (PRDR)

```yaml
schema_version: R3
gate_id: S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE
machinery_pin_map:
  L_max:           [8, 10]              # canonical L_max=10; cross-check at 8
  s_evaluation:    3+0i                  # off-pole canonical evaluation point
  s_sweep:         [2.5, 2.75, 3.0, 3.25, 3.5]   # 5-point off-pole sweep for χ²/dof
  scheme:          analytic-continuation  # zeta-functional spectral action lineage
  convention:      "off-pole-Hankel-deformed"
  cutoff_axis:     spectral
  n_eval:          50                     # mpmath workdps
  contour:         "real-axis at Re(s)=3, Hankel-deformed near s∈{2,4}"
  d_spec:          8                       # NCG spectral dimension
  tolerance:       "5% L_max=8 vs L_max=10; analyticity 1e-3 at s=3+0.001i"
  random_seed:     "n/a (deterministic)"
  GPU_path:        "torch.linalg + ROCm AMD RX 9070 XT"
  CPU_fallback:    "OMP_NUM_THREADS=8 BEFORE numpy import"
input_pins:
  D_K_cache:           <SHA-pinned at runtime from canonical_constants.D_K_cache_path L_max=10>
  canonical_constants: <SHA-pinned at runtime>
  c9_residues:         <SHA-pinned at runtime if C9 PASS; otherwise tagged "C9 INFO/FAIL — diagnostic only">
```

### 8. Expected output 4-tuple

```
(value=analytic_zeta(s=3, L_max=10), scheme=analytic-continuation, convention=off-pole-Hankel, L_max=10)
```

### 9. PASS / FAIL / INFO thresholds

| Verdict | Condition | Tolerance rule |
|:--------|:----------|:---------------|
| **PASS** | `analytic_zeta(s=3, L_max=10)` finite (no NaN, no overflow, |result| < 1e10) AND `χ²/dof ≤ 5` against direct subtraction across 5-point sweep | RATIO (cross-method); ABSOLUTE (finiteness check) |
| **INFO** | Finite at s=3 but `χ²/dof ∈ (5, 20]` against direct subtraction OR finite at L_max=10 but unstable (>5%) at L_max=8 | INFO band classification with diagnostic |
| **FAIL** | `analytic_zeta(s=3, L_max=10)` non-finite OR `χ²/dof > 20` | FAIL — analytic_zeta API non-functional; cascading FAIL into W3 T9 REPLACEMENT-B |

### 10. Substitution chain (for the `χ²/dof ≤ 5` against direct subtraction)

```
Step 1 (definitions):
  dof = 5 (sweep points) - 1 (one fitted offset) = 4
  analytic_zeta(s, 10)   = mp.quad(integrand(t, s), [0, ∞]) / mp.gamma(s/2)
  ζ_D^{direct}(s)        = Σ_k λ_k^{-s}    (L_max=10 truncated)
  σ(s)                   = max(|analytic_zeta(s, 8) - analytic_zeta(s, 10)|, 1e-12)
                           [truncation noise floor]

Step 2 (substitution):
  χ² = Σ_{s∈sweep} ( (analytic_zeta(s, 10) - ζ_D^{direct}(s)) / σ(s) )²
  χ²/dof = χ² / 4

Step 3 (canonical form):
  PASS ⟺ χ²/dof ≤ 5
       ⟺ average normalized discrepancy ≤ sqrt(5) ≈ 2.24σ across the 5-point sweep

Step 4 (direction):
  PASS demands the analytic continuation tracks the direct truncation across the
  off-pole strip to within ~2.24 truncation-noise units. This is a STRONG agreement
  criterion: it rules out spurious analytic-continuation artifacts while permitting
  truncation-induced scatter at L_max=10.

Conclusion: 5 is a defensible threshold for cross-method numerical agreement in the
off-pole NCG regime; not a vacuous tolerance.
```

### 11. What PASSES / FAILS mean for solution space

- **PASS** delivers the `analytic_zeta(s, L_max)` API as a reusable module, unlocking **W3 T9 REPLACEMENT-B** directly, **W3's W0-7 re-emission** (ρ → −0.81 conjecture test under the API), and **W10 C37 ZFP discharge** (ζ-at-interior route for `mu_BC` — depends on Mellin-cone framework). PASS demonstrates that the substrate's d_spec=8 cone apex is well-defined off-pole at s=3.
- **INFO** preserves the API but flags it as cross-check-conditional; downstream gates may use it but must declare the χ²/dof or stability INFO band as a known limitation.
- **FAIL** means the off-pole continuation is not numerically stable in the ROCm + mpmath workflow — either a fundamental failure of analytic continuation in this regime (substrate-class result: D_K spectral measure is too sparse at L_max=10 to support s=3 off-pole evaluation) or a workflow defect (which would require infrastructure remediation in S87).

### 12. Effort estimate

**HEAVY 4-6h** — new infrastructure module. Breakdown:
- Module API design + signature freeze: 0.5h
- mp.quad integrand implementation + GPU heat-kernel: 1.5h
- Off-pole sweep + χ²/dof computation: 1.5h
- Cross-checks + dual-SHA verdict emission: 1-2h

### 13. Substrate-framing reminder

State as: **"The off-pole analytic continuation of the substrate's spectral-triple zeta function exposes the d_spec=8 cone apex at s=3 without truncation contamination — the Mellin-Barnes lens reveals that the substrate's spectral content is finite at this off-pole point, validating the lens for downstream REPLACEMENT-B and W0-X re-emission gates."**

NEVER frame the analytic continuation as "creating" finiteness — D_K's spectrum either supports off-pole continuation at s=3 or does not; the API merely measures.

---

## §W2-3. S86-MELLIN-MULTIPLIER-INFINITE-VECTOR-EXTENSION (C11)

### 1. Gate ID
`S86-MELLIN-MULTIPLIER-INFINITE-VECTOR-EXTENSION` (closeout §3.6; context §2.6 row C11; lizzi 9A §A-3 + lizzi 3A §V.4)

### 2. Trigger
`[VERIFY]` — numerical reproduction of the analytic Mellin transform `M[exp(-x/Λ_Z²)](s) = Λ_Z^{2s}·Γ(s)` at high-precision sample points AND formalization of the INFINITE-VECTOR vs FINITE-VECTOR class asymmetry as a registered framework note.

### 3. Classification
**GEOMETRIC** — the Mellin transform of the Zubarev kernel is a classification statement about the regulator's algebraic class: finite-vector (e_4 ∈ ℝ^4 over slots {a_0, a_2, a_4, a_6}) vs infinite-vector (Schwartz-class continuous spectrum). This is structural to the spectral-triple's regulator algebra, not to any substrate excitation.

### 4. Agent type
**Runtime owner**: `lizzi-spectral-functional-theorist` — Zubarev-INFINITE-VECTOR vs ζ-FINITE-VECTOR distinction is the lizzi 9A §A-3 carry-forward; lizzi's S-1 finite-vector F_4 formalism is the parent framework being extended.
**Backstop**: `connes-ncg-theorist` — Schwartz-class Mellin transforms and the algebra of regulator multipliers are core NCG; connes can derive the analytic form independently as a cross-check.
**Forbidden runtime owner**: `gen-physicist`.

### 5. Hypothesis
The Zubarev kernel `exp(-x/Λ_Z²)` has Mellin transform `Λ_Z^{2s}·Γ(s)` (a closed analytic form; INFINITE-VECTOR class), in contrast to the ζ-class regulator's finite-vector e_4 = (1, 1, 1, 1) ∈ ℝ^4 over the four Seeley-DeWitt slots. The INFINITE-VECTOR vs FINITE-VECTOR algebraic asymmetry is the regulator-class structural floor explaining why F_4 = {ζ, Zubarev, SDW} cannot collapse to a single equivalence class.

### 6. Method (FULL dispatch prompt)

```
You are lizzi-spectral-functional-theorist. Compute the analytic Mellin transform of the Zubarev
kernel, embed Zubarev as INFINITE-VECTOR class, and formalize the ζ-class (finite-vector e_4)
vs Zubarev-class (infinite-vector M[Schwartz]) asymmetry as a framework note.

QUERY KNOWLEDGE FIRST:
  search_knowledge("Zubarev regulator INFINITE-VECTOR Mellin transform")
  search_knowledge("Lizzi S-1 F_4 finite-vector e_4 formalism")
  trace_entity("Mellin Strip Convergence Cone Theorem")
  get_constant("Lambda_Z")
  list_constants("Zubarev")

REFERENCE PAPERS (mandatory citations):
  - Lizzi S-1 §IV (the F_4 finite-vector formalism)
  - Lizzi 3A §V.4 (the INFINITE-VECTOR extension proposal)
  - Mellin transform tables (Erdelyi 1953; Gradshteyn-Ryzhik §6.561)

SCRIPT TARGET: computations/s86_w2_c11_mellin_multiplier_infinite_vector.py
FRAMEWORK NOTE TARGET: sessions/framework/registry/lizzi-finite-infinite-vector-classification.md
  (CREATE THIS FILE — it does not exist; project-level registry per
   .claude/rules/agent-standards.md §Memory Scope)

IMPORTS:
  from canonical_constants import *
  import numpy as np
  from mpmath import mp, mpc, gamma, quad
  mp.dps = 50

GPU PIN: not required — this is a closed-form symbolic verification, not a heavy
matrix workload. Use mpmath at workdps=50 throughout.

CORE COMPUTATION STEPS:
  Step 1: Define the Zubarev kernel f_Z(x) = exp(-x/Λ_Z²) with Λ_Z from canonical_constants.
  Step 2: Compute analytically: M[f_Z](s) = ∫_0^∞ x^{s-1} exp(-x/Λ_Z²) dx
                              = Λ_Z^{2s} · Γ(s)         (substitute u = x/Λ_Z²)
  Step 3: Numerical verification via mp.quad at sample points s ∈ {0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0}
          (8-point sweep avoiding s=0 pole of Γ).
  Step 4: Compare numerical mp.quad result vs closed-form Λ_Z^{2s}·Γ(s) at each sample.
          Per-point relative error must be ≤ 1e-12 (machine-precision identity).
  Step 5: Classify Zubarev as INFINITE-VECTOR class:
          - Finite-vector ζ-class: spectral action = sum of 4 discrete moments
            ⟨a_n⟩ for n ∈ {0, 2, 4, 6} → e_4 = (1, 1, 1, 1) ∈ ℝ^4
          - Infinite-vector Zubarev-class: spectral action = continuous Mellin profile
            M[Schwartz](s) over s ∈ ℂ → infinite-dimensional vector
  Step 6: Document the asymmetry: F_4 = {ζ, SDW} are finite-vector, Zubarev is the unique
          infinite-vector member of F_4. Mixed-support family M = {cutoff_sqrt, anomaly} is
          ALSO infinite-vector but with a different multiplier algebra.
  Step 7: Write the framework note `sessions/framework/registry/lizzi-finite-infinite-vector-classification.md`
          with §1 finite-vector definition, §2 infinite-vector definition, §3 asymmetry table
          (per regulator: class, multiplier vector, dimensionality), §4 implications for the
          F_4 / M partition theorem.

PASS CRITERIA (both must hold):
  (a) Per-point relative error of M[f_Z](s) numerical-vs-closed-form ≤ 1e-12 across all 8 sample points
  (b) Framework note `sessions/framework/registry/lizzi-finite-infinite-vector-classification.md` written with all 4 sections

FAIL:
  Any sample point relative error > 1e-12 (numerical inconsistency with closed form)
  OR framework note not written / stub (<25 lines of substantive content)

OUTPUT FILES:
  - s86_w2_c11_mellin_multiplier_infinite_vector.py
  - s86_w2_c11_mellin_table.npz (8-point sweep, numerical vs closed-form)
  - sessions/framework/registry/lizzi-finite-infinite-vector-classification.md (the framework note)
  - dual-SHA verdict line in computations/s86_gate_verdicts.txt:
      S86-MELLIN-MULTIPLIER-INFINITE-VECTOR-EXTENSION: PASS|FAIL -- value=<max_rel_err> scheme=<analytic-Mellin> convention=<closed-form-verification> L_max=NA sha256=<closure>
    + companion comment row

CROSS-CHECKS:
  (i) M[f_Z](s=1) = Λ_Z² · Γ(1) = Λ_Z²; verify numerically.
  (ii) M[f_Z](s=2) = Λ_Z⁴ · Γ(2) = Λ_Z⁴; verify numerically.
  (iii) Recurrence: M[f_Z](s+1) / M[f_Z](s) = Λ_Z² · s; verify across the sweep.

NEVER: do not extend the framework note beyond its scope; this gate's role is the formal landing
of the asymmetry, not a derivation of new physical consequences.
```

### 7. Machinery pin (PRDR)

```yaml
schema_version: R3
gate_id: S86-MELLIN-MULTIPLIER-INFINITE-VECTOR-EXTENSION
machinery_pin_map:
  L_max:           "n/a (closed-form Mellin transform; no D_K cache access)"
  Lambda_Z:        <from canonical_constants.Lambda_Z>
  scheme:          analytic-Mellin-closed-form
  convention:      "M[exp(-x/Λ_Z²)](s) = Λ_Z^{2s} Γ(s) per Erdelyi 1953"
  cutoff_axis:     spectral
  s_sample:        [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
  n_eval:          50                   # mpmath workdps
  tolerance:       "1e-12 relative error per sample (machine-precision identity)"
  random_seed:     "n/a (deterministic mpmath)"
  GPU_path:        "n/a (closed-form symbolic verification)"
  CPU_fallback:    "OMP_NUM_THREADS=8 BEFORE numpy import (defensive)"
input_pins:
  canonical_constants: <SHA-pinned at runtime>
  s_1_lift:            <SHA-pinned at runtime from sessions/framework/lizzi-s1-regulator-family-boundary.md if exists; otherwise from S85 closeout §1.5>
```

### 8. Expected output 4-tuple

```
(value=max_rel_err over 8 samples, scheme=analytic-Mellin, convention=closed-form-verification, L_max=NA)
```

### 9. PASS / FAIL / INFO thresholds

| Verdict | Condition | Tolerance rule |
|:--------|:----------|:---------------|
| **PASS** | `max_rel_err ≤ 1e-12` across all 8 sample points AND framework note written with §1-§4 substantive content | RATIO (relative error); NOTE-EXISTENCE (framework note must exist with ≥25 substantive lines) |
| **FAIL** | Any `rel_err > 1e-12` OR framework note absent / stub | FAIL — closed-form identity not numerically reproducible (would indicate canonical_constants Λ_Z mis-pin) or registry write skipped |

(No INFO band — this is a closed-form analytic identity; either it reproduces to machine precision or there is a canonical-constants defect. INFO would be vacuous.)

### 10. Substitution chain (for the closed-form identity verification)

```
Step 1 (definition):
  M[f](s) = ∫_0^∞ x^{s-1} f(x) dx       [Mellin transform definition]
  f_Z(x)  = exp(-x / Λ_Z²)              [Zubarev kernel definition]

Step 2 (substitution):
  M[f_Z](s) = ∫_0^∞ x^{s-1} exp(-x / Λ_Z²) dx

Step 3 (variable change u = x / Λ_Z²; dx = Λ_Z² du):
  M[f_Z](s) = ∫_0^∞ (Λ_Z² u)^{s-1} exp(-u) · Λ_Z² du
            = Λ_Z^{2(s-1)} · Λ_Z² · ∫_0^∞ u^{s-1} exp(-u) du
            = Λ_Z^{2s} · Γ(s)

Step 4 (canonical form):
  M[f_Z](s) = Λ_Z^{2s} · Γ(s)            [closed-form identity]

Step 5 (direction):
  This is an algebraic identity — numerical mp.quad must reproduce it to within
  the integrator's intrinsic precision (workdps=50 → ~1e-50 absolute error; the
  1e-12 relative tolerance is conservative and absorbs only floating-point
  accumulation in the closed-form Γ evaluation).

Conclusion: The 1e-12 threshold is a sanity check on canonical_constants Λ_Z
correctness and on mpmath workdps configuration. Any failure indicates a
canonical-pin defect, NOT a physics finding.
```

### 11. What PASSES / FAILS mean for solution space

- **PASS** formalizes the INFINITE-VECTOR vs FINITE-VECTOR asymmetry as a registered framework distinction. This unblocks downstream classifications: the F_4 = {ζ, Zubarev, SDW} sub-atlas's internal heterogeneity (Zubarev being the unique infinite-vector member) becomes citable in S86+ syntheses, and the M = {cutoff_sqrt, anomaly} mixed-support family's regulator-class structural floor gets a precise algebraic anchor. The Mellin Strip / Convergence Cone Theorem (T5 in W1b) gains a sister classification pillar.
- **FAIL** indicates a canonical_constants defect (Λ_Z mis-pinned) or mpmath configuration error — a remediation problem, not a physics finding.

### 12. Effort estimate

**MODERATE 3-4h** — closed-form verification + framework note authoring. Breakdown:
- Closed-form derivation + 8-point numerical verification: 1h
- Framework note §1-§4 authoring: 2h
- Cross-checks + dual-SHA verdict emission: 0.5-1h

### 13. Substrate-framing reminder

State as: **"The Mellin transform of the Zubarev kernel reveals that Zubarev acts on the substrate's spectral content as an infinite-dimensional multiplier (continuous Mellin profile over s ∈ ℂ), while ζ acts as a 4-dimensional multiplier on the discrete Seeley-DeWitt slots. The substrate's spectral content is the same in both cases; the regulator-class asymmetry lives entirely in the lens, not in D_K."**

NEVER frame the asymmetry as "Zubarev sees more of the substrate" — both regulators see all of D_K; the difference is the algebraic class of the multiplier vector.

---

## §W2-4. S86-CLUSTER-SPAN-EXTRACTOR-BUILD (C12)

### 1. Gate ID
`S86-CLUSTER-SPAN-EXTRACTOR-BUILD` (closeout §3.6; context §2.6 row C12; gen-physicist S-7 §V.3)

### 2. Trigger
`[VERIFY]` — module exists and self-test reproduces W0-3 PASS at L_max ∈ {8, 10, 12}.

### 3. Classification
**GEOMETRIC** — cluster-span extraction operates on D_K eigenvalue clusters (groupings of nearby eigenvalues by the W0-3 / CC-5 rule). The operation is structural to the spectral-triple's spectrum, independent of substrate excitations or particle-class quantum numbers.

### 4. Agent type
**Runtime owner**: `connes-ncg-theorist` — module-class refactoring of an existing CC-5 W0-3 PASS is core NCG infrastructure work; connes is the structural-cleanup specialist.
**Backstop**: `lizzi-spectral-functional-theorist` (only if connes stalls on the cluster-span algorithm semantics, since W0-3 is a Lizzi-track theorem candidate).
**Forbidden runtime owner**: `gen-physicist`.

### 5. Hypothesis
The W0-3 cluster-span PASS (CC-5 cluster-span identity 2.000…002) admits a clean module-class refactor: a reusable `cluster_span(L_max: int) -> tuple[float, float]` API in `computations/_cluster_span_extract.py` that reproduces the W0-3 verdict at L_max ∈ {8, 10, 12} under a single self-test driver.

### 6. Method (FULL dispatch prompt)

```
You are connes-ncg-theorist. Refactor the W0-3 ad-hoc cluster-span code into a reusable module
with a self-test that reproduces W0-3 PASS at L_max ∈ {8, 10, 12}.

QUERY KNOWLEDGE FIRST:
  search_knowledge("W0-3 cluster-span CC-5 identity 2.000")
  search_knowledge("b_pow span_2 span_3 cluster")
  trace_entity("CC-5 cluster-span identity")
  get_constant("M_KK")
  list_constants("L_max")

LOCATE THE EXISTING W0-3 SCRIPT:
  Use Grep to find the script that produced W0-3 PASS in S85:
    Grep: "S86-MELLIN-HEAT-KERNEL" → no, wrong gate
    Grep: "W0-3" → likely computations/s85_w0_3_cluster_span.py or similar
    Grep: "cluster_span" type:py → identify the existing implementation
  Read the existing script (do NOT modify it; it is the canonical W0-3 reference).
  Extract: the cluster-span algorithm, the b_pow definition, the eigenvalue grouping rule.

INFRASTRUCTURE MODULE TARGET:
  computations/_cluster_span_extract.py     # the new reusable module
  computations/s86_w2_c12_cluster_span_self_test.py   # the verification driver

MODULE API SPEC (mandatory signature):
  def cluster_span(L_max: int) -> tuple[float, float]:
      \"\"\"
      Extract the b_pow(span_2) and b_pow(span_3) cluster-span exponents from D_K eigenvalues.

      W0-3 CC-5 identity: b_pow(span_2) = 2 * b_pow(span_3) at machine precision.

      Args:
          L_max: D_K spectral cutoff (canonical L_max=10; supports {8, 10, 12})

      Returns:
          tuple (b_pow_span_2, b_pow_span_3); the W0-3 PASS reproduces b_pow_span_2 = 2*b_pow_span_3
          to within 1e-15 at L_max=10.
      \"\"\"

GPU PIN: D_K eigenvalue load + cluster grouping is at L_max=12 above 100x100 matrix scale.
Use torch.linalg on AMD RX 9070 XT for the eigenvalue load + clustering pass; CPU fallback
OMP_NUM_THREADS=8 BEFORE numpy import.

IMPORTS:
  from canonical_constants import *
  import numpy as np
  import torch

CORE BUILD STEPS:
  Step 1: Read the existing W0-3 script; identify the cluster-span algorithm verbatim.
  Step 2: Refactor the algorithm into the cluster_span(L_max) function in _cluster_span_extract.py:
          - Load D_K eigenvalues at L_max from canonical cache (GPU torch.linalg)
          - Apply the W0-3 clustering rule (eigenvalue groups by CC-5 spec)
          - Compute b_pow(span_n) for n ∈ {2, 3}
          - Return the tuple
  Step 3: Write the self-test driver s86_w2_c12_cluster_span_self_test.py:
          - For L_max ∈ {8, 10, 12}:
              (b2, b3) = cluster_span(L_max)
              relative_error = |b2 - 2*b3| / max(|b2|, 1e-15)
              assert relative_error < 1e-15, f"L_max={L_max}: identity violated, rel_err={relative_error}"
          - Print the PASS table to stdout.
  Step 4: Verify the self-test PASSes at all 3 L_max values.

PASS CRITERIA (all must hold):
  (a) Module file `computations/_cluster_span_extract.py` exists with the cluster_span signature
  (b) Self-test passes at L_max=8 (rel_err < 1e-15)
  (c) Self-test passes at L_max=10 (rel_err < 1e-15) — this MUST reproduce the canonical W0-3 verdict
  (d) Self-test passes at L_max=12 (rel_err < 1e-15)

FAIL:
  Any of (a)-(d) fails. In particular, if (c) fails, the refactor broke the W0-3 algorithm
  semantics — STOP and DO NOT publish the module; document the divergence in the verdict line
  and request a follow-up dispatch to align with the original W0-3 implementation.

OUTPUT FILES:
  - computations/_cluster_span_extract.py (the module)
  - computations/s86_w2_c12_cluster_span_self_test.py (the driver)
  - s86_w2_c12_self_test_results.npz (b_pow_span_2 and b_pow_span_3 at each L_max)
  - dual-SHA verdict line in computations/s86_gate_verdicts.txt:
      S86-CLUSTER-SPAN-EXTRACTOR-BUILD: PASS|FAIL -- value=<max_rel_err over L_max in {8,10,12}> scheme=<refactor> convention=<W0-3-canonical> L_max=multi-{8,10,12} sha256=<closure>
    + companion comment row

CROSS-CHECKS:
  (i) Compare cluster_span(10) output against the canonical W0-3 verdict-file value (2.000...002)
  (ii) Confirm the module raises a clear error if L_max not in supported set (defensive design)
  (iii) Confirm the module imports cleanly when invoked from a downstream caller
        (no circular imports, no implicit canonical_constants writes)

NEVER:
  - Do not modify the original W0-3 script (it is the canonical reference)
  - Do not adjust the clustering rule semantics; this is a refactor, not a re-derivation
```

### 7. Machinery pin (PRDR)

```yaml
schema_version: R3
gate_id: S86-CLUSTER-SPAN-EXTRACTOR-BUILD
machinery_pin_map:
  L_max:           [8, 10, 12]           # 3-point self-test sweep
  scheme:          refactor               # not a regulator scheme — refactor of existing W0-3 code
  convention:      "W0-3 canonical CC-5 identity"
  cutoff_axis:     spectral
  n_eval:          "n/a (deterministic eigenvalue grouping)"
  tolerance:       "1e-15 relative error on |b2 - 2*b3| (machine epsilon identity)"
  random_seed:     "n/a (deterministic)"
  GPU_path:        "torch.linalg + ROCm AMD RX 9070 XT for eigenvalue load at L_max=12"
  CPU_fallback:    "OMP_NUM_THREADS=8 BEFORE numpy import"
input_pins:
  D_K_cache:                    <SHA-pinned at runtime for L_max ∈ {8, 10, 12}>
  canonical_constants:          <SHA-pinned at runtime>
  w0_3_canonical_script:        <SHA-pinned at runtime; identified via Grep at dispatch>
```

### 8. Expected output 4-tuple

```
(value=max_rel_err over L_max in {8,10,12}, scheme=refactor, convention=W0-3-canonical, L_max=multi-{8,10,12})
```

### 9. PASS / FAIL / INFO thresholds

| Verdict | Condition | Tolerance rule |
|:--------|:----------|:---------------|
| **PASS** | Module file exists with `cluster_span(L_max) -> tuple[float, float]` signature AND self-test passes at all of L_max ∈ {8, 10, 12} with `rel_err < 1e-15` | RATIO (relative error, machine-epsilon); MODULE-EXISTENCE |
| **FAIL** | Module absent / wrong signature OR any L_max in {8, 10, 12} fails the self-test | FAIL — refactor broke W0-3 semantics OR module not landed |

(No INFO band — this is a refactor with a closed-form identity at the heart; either the W0-3 algorithm is preserved across L_max values or it is not. INFO would be vacuous.)

### 10. Substitution chain (for the `rel_err < 1e-15` threshold)

```
Step 1 (definition):
  W0-3 CC-5 identity: b_pow(span_2) = 2 * b_pow(span_3)            [exact algebraic identity]
  rel_err(L_max) = |b_pow_span_2(L_max) - 2 * b_pow_span_3(L_max)| / max(|b_pow_span_2(L_max)|, 1e-15)

Step 2 (substitution):
  Identity holds exactly at the symbolic level; numerical computation introduces only
  floating-point accumulation error from the eigenvalue load + clustering.
  Floating-point relative error per arithmetic operation ~ 2.22e-16 (IEEE 754 double).
  Cluster grouping at L_max=12 involves O(L_max^4) ~ O(20000) operations.
  Accumulated relative error bound ~ 20000 * 2.22e-16 ~ 4.44e-12 (worst-case, no cancellation).

Step 3 (canonical form):
  PASS ⟺ rel_err(L_max) < 1e-15 for all L_max in {8, 10, 12}
       ⟺ floating-point cancellation in the b_pow computation is essentially complete

Step 4 (direction):
  The 1e-15 threshold is BELOW the worst-case accumulation bound (4.44e-12), but
  the W0-3 PASS at S85 demonstrated the operation actually achieves machine epsilon
  thanks to favorable cancellation in b_pow construction (the identity is structural,
  so the computation lands near zero by construction). The 1e-15 floor is what W0-3 ACHIEVED;
  the refactor must preserve this — anything looser indicates an algorithmic divergence
  from the canonical W0-3 implementation.

Conclusion: 1e-15 is the W0-3-canonical achieved-precision floor, NOT a vacuous threshold.
```

### 11. What PASSES / FAILS mean for solution space

- **PASS** delivers `_cluster_span_extract.py` as a reusable module, unlocking **W3 C13** (`b_pow(span_2) = 2·b_pow(span_3)` machine-precision test across K ∈ [K_R5, K_crit] under L_max=10 + sheet-by-sheet on post-fold Riemann cover K ∈ [K_crit, K_FIRAS]). The module decouples cluster-span analysis from the W0-3 verdict-file, enabling downstream gates to call it without code duplication.
- **FAIL** indicates the W0-3 algorithm is more ad-hoc than its PASS verdict suggests — refactoring breaks the identity. In that case the refactor is rolled back and the original W0-3 script remains the canonical implementation; downstream W3 C13 must call the original script directly rather than the new module.

### 12. Effort estimate

**LIGHT 1h** — module-class refactor + 3-point self-test. Fastest gate of W2.

### 13. Substrate-framing reminder

State as: **"The cluster-span extractor reads the substrate's D_K eigenvalue distribution at L_max ∈ {8, 10, 12} and exposes the W0-3 CC-5 identity as a structural property of the spectral-triple's eigenvalue clustering — the substrate's spectral content satisfies b_pow(span_2) = 2·b_pow(span_3) by construction; the module is a reusable lens for downstream K-corridor extensions."**

The cluster-span identity is intrinsic to D_K's spectrum, not to the cluster algorithm.

---

## §X. Wave W2 → Downstream Decision Point

W2 is a HEAVY infrastructure spine. Its outputs feed two later waves directly and one indirectly:

| Downstream wave | Upstream W2 dependency | Reason |
|:----------------|:------------------------|:-------|
| **W3** T9 REPLACEMENT-B (asymptotic ζ-stabilization at s=4 leading residue) | **C9 PASS + C10 PASS** (joint condition) | T9's PASS-condition requires both the Mellin-Barnes residue extractor (a_n^{MB}) and the off-pole `analytic_zeta(s, L_max)` API to be operational |
| **W3** W0-7 / W0-11 / W0-20 re-emissions (3 truncation-FAIL closures) | **C9 PASS** (primary), **C10 PASS** (secondary for W0-7 conjecture test) | Each W0-X re-emission applies the Mellin-Barnes residue extractor + analytic_zeta API to the original failed gate; substrates content unchanged, lens improved |
| **W3** C13 cluster-span K-corridor extension | **C12 PASS** (mandatory) | C13 calls the `cluster_span(L_max)` module across K ∈ [K_R5, K_crit] and on the post-fold Riemann cover K ∈ [K_crit, K_FIRAS]; without the refactored module C13 has no infrastructure to call |
| **W10** C37 ζ-at-interior derivation (mu_BC integer-12 exponent) | **C9 PASS** (informative; route may use Mellin-cone framework) | C37 attempts a ζ-at-interior route never previously attempted per W9-5 status; depends on C9's Mellin-cone infrastructure for the ζ-functional regularization at the interior point |

**If C9 INFO**: T9 REPLACEMENT-B + W0-X re-emissions proceed under conditional pre-registration ("INFO-conditional PASS" flagging in their verdict lines).
**If C9 FAIL**: T9 REPLACEMENT-B + 3 W0-X re-emissions cascade-FAIL; W3 narrows to C13 + C43 only; W10 C37 falls back to C38 + C39 routes (rep-theoretic + heat-kernel diagnostic — methodologically independent of Mellin-cone). The cascade-FAIL is itself a major constraint-map gain (Mellin-Barnes regulator-class structural floor closed).
**If C10 INFO/FAIL**: T9 REPLACEMENT-B PASS-condition unmet; W3 T9 lands as INFO-conditional or FAIL respectively; W0-7 re-emission falls back to direct truncation-extrapolation (less informative than analytic_zeta-based test).
**If C11 FAIL**: indicates canonical_constants Λ_Z mis-pinning; remediate via canonical_constants update before re-dispatching; does not block C9/C10/C12.
**If C12 FAIL**: W3 C13 falls back to direct call to the original W0-3 script (loss: code duplication; gain: identity preserved).

---

## §0.10. Wave W2 Machinery-Enumeration Pin (HEAVY GPU pinning)

Aggregate machinery enumeration across all 4 W2 gates:

| Parameter | C9 | C10 | C11 | C12 |
|:----------|:---|:----|:----|:----|
| L_max | [5, 6, 7, 8, 10] | [8, 10] | n/a | [8, 10, 12] |
| scheme | [zeta, Zubarev, SDW] | analytic-continuation | analytic-Mellin-closed-form | refactor |
| convention | Connes-Moscovici-1995-residue, SD-subtracted | off-pole-Hankel-deformed | M[exp(-x/Λ_Z²)] = Λ_Z^{2s}Γ(s) | W0-3 canonical CC-5 identity |
| cutoff_axis | spectral | spectral | spectral | spectral |
| n_eval | 50 (mp.dps) | 50 (mp.dps) | 50 (mp.dps) | n/a |
| s_evaluation | {0, 2, 4, 6} | 3+0i (canonical) | sweep [0.5..4.0] | n/a |
| tolerance | 1e-12 contour SC; 1e-3 a_2 cross-check | 5% L_max=8 vs 10; 1e-3 analyticity | 1e-12 per sample | 1e-15 rel_err |
| random_seed | n/a | n/a | n/a | n/a |
| GPU_path | torch.linalg + ROCm | torch.linalg + ROCm | n/a | torch.linalg + ROCm |
| CPU_fallback | OMP=8 before numpy | OMP=8 before numpy | OMP=8 (defensive) | OMP=8 before numpy |

**GPU envelope**: 3 of 4 gates use GPU (C9, C10, C12); aggregate VRAM budget at L_max=12 D_K eigenvalue cache ~ 4-6 GB (well within 17.1 GB AMD RX 9070 XT envelope).

**Per-script PRDR**: each gate's machinery_pin_map block above is the canonical pre-registration. None of the 4 gates is PRU-vulnerable (PRU Class 8) under the W0a R1+R2+R3 v3 rule-file landing.

---

## §0.11. Wave W2 Input-SHA Ledger

| Input | Used by | Pin source |
|:------|:--------|:-----------|
| `computations/canonical_constants.py` | C9, C10, C11, C12 | runtime SHA at dispatch |
| `computations/_source_reconciliation_audit.py` | C9 (compliance check) | runtime SHA after W0a R2 lands |
| `computations/_mellin_compliance_check.py` | C9 (5-marker boilerplate) | runtime SHA after W0c C22 lands |
| `D_K_cache` at L_max=10 | C9, C10 | runtime SHA from `canonical_constants.D_K_cache_path` |
| `D_K_cache` at L_max ∈ {5, 6, 7, 8, 10} | C9 | runtime SHAs (5 cache files) |
| `D_K_cache` at L_max=8 | C10 (cross-check) | runtime SHA |
| `D_K_cache` at L_max ∈ {8, 10, 12} | C12 | runtime SHAs (3 cache files) |
| `s86_w2_c9_residues.npz` | C10 (informative diagnostic) | runtime SHA after C9 completes |
| W0-3 canonical script (Grep-located at C12 dispatch) | C12 | runtime SHA at dispatch |
| `sessions/framework/lizzi-s1-regulator-family-boundary.md` (if exists) | C11 | runtime SHA at dispatch |

**Closure SHA computation** (per `.claude/templates/script-template.py`): each gate computes the 64-character `sha256` closure from the ordered input-pin map and emits it in the dual-SHA verdict line. The companion comment row records the `audit_sha256` (per `.claude/rules/gate-verdicts.md` S81+ canonical form).

---

## §Y. Wave W2 Stall Handling

If the runtime agent reports "killed" or "stalled" without writing one of the 4 output files, dispatch sub-waves per the partition manifest §1 W2 "Natural split candidates":
- **W2a**: C9 alone (master heat-kernel build) — full HEAVY 6-8h spec
- **W2b**: C10 alone (analytic_zeta API) — full HEAVY 4-6h spec
- **W2c**: C11 (Mellin multiplier) + C12 (cluster-span extractor) — combined MODERATE 4-5h
Do NOT re-dispatch with a leaner spec. The full-fidelity prompt is canonical (per `feedback_max-effort-full-fidelity.md`).

---

**End of Wave W2 plan. 4 gate blocks, full 13-field per `.claude/skills/rclab-plan/skill.md` §3b.**
