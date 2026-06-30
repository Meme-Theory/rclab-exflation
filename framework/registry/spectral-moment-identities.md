# Spectral-Moment Identities — REGULATOR-MONODROMY-AXIS-DECOMPOSITION

> **Provenance**: S86 W-12 RULE-W12-3 (5-step methodology, workshop §EMERGENCE E-2 R2-B lines 1207-1228, §CONVERGENCE C-4 R3-A lines 1278-1283); OTHER-W12-1 (intended-host-file decision, workshop §"Carry-Forward Computations" CF-W12-4 lines 1788-1795). Promoted to permanent framework registry via S86 housekeeping install queue (T2-6, READY-TO-INSTALL).

This file houses the framework's identities for spectral-action moments under regulator-class monodromy. It is the framework-side companion to:

- `.claude/rules/regulator-pin-discipline.md` — regulator-tag enforcement at the script/working-paper layer
- `sessions/permanent-results-registry.md` REG-W12-1 — V_4 monodromy at moment-integral layer (NEEDS-COMPUTATION, gated on S87-MONODROMY-V_4-EXPLICIT PASS-parallelogram-exact)
- `.claude/rules/epistemic-discipline.md` §"Pre-Registration Completeness" PRU Class-8.2 — verifier-rubric pre-registration failure

## 1. The 5-Step REGULATOR-MONODROMY-AXIS-DECOMPOSITION Methodology

When investigating regulator-class monodromy on spectral-action moments, follow this sequence (workshop §E-2 R2-B):

### Step 1 — Enumerate regulator-class boundaries

Enumerate the regulator-class boundaries in the regulator atlas. Each boundary corresponds to a sign convention or class selector that the regulator picks up when crossed. The W-12 calibration enumerated TWO boundaries:

- Axis-M (Mellin local-residue at s = -1)
- Axis-C (W6-3 global-asymptotic-topology, flat ℝ × S² ↔ dS S³)

### Step 2 — Classify each boundary as LOCAL or GLOBAL (Wodzicki-residue locality argument)

Classify each boundary using the Wodzicki-residue locality argument:

- **LOCAL** — UV / heat-kernel-coefficient sign. LOCAL boundary acts on a_k coefficients pointwise in heat-kernel expansion. The Wodzicki-residue / a_4 contribution is a LOCAL invariant of D_K, computed from bulk metric and gauge data.
- **GLOBAL** — IR / asymptotic-completion topology. GLOBAL boundary acts on asymptotic-completion data (e.g., choice of ℐ⁺ class, asymptotic conformal-end selector).

W-12 calibration:
- Axis-M (Mellin local-residue) → LOCAL
- Axis-C (W6-3 conformal-end selector) → GLOBAL

### Step 3 — Verify INDEPENDENCE

Verify INDEPENDENCE of the two axes:

- LOCAL data does NOT fix GLOBAL data
- GLOBAL data does NOT fix LOCAL data

If verified, the boundaries generate INDEPENDENT Z_2 factors. The W-12 calibration verified independence per FALS-W12-3: a regulator using Mellin-cone residue reads off the SAME a_4 regardless of whether asymptotic ℐ⁺ is flat (Λ_eff = 0) or dS (Λ_eff > 0); conformal-end choice does not change the residue value itself.

### Step 4 — The maximal abelian regulator monodromy is (Z_2)^n

The maximal abelian regulator monodromy is `(Z_2)^n` where:

```
n = m (LOCAL) + k (GLOBAL) + (any further independent axes)
```

W-12 calibration: m = 1, k = 1 → n = 2 → V_4 = (Z_2)^2 = Z_2(Mellin local-residue) × Z_2(W6-3 global-asymptotic-topology).

### Step 5 — Test the parallelogram identity (or hypercube-vertex character identity)

Test the parallelogram identity (or its (Z_2)^n generalization, the hypercube-vertex character identity) on spectral moments as the consistency check. This is the gate criterion of S87-MONODROMY-V_4-EXPLICIT (CF-W12-1) at d=2 and S87-HYPERCUBE-VERTEX-IDENTITY-LANDING (CF-W12-4) at d ∈ {2, 3, 4, 5}.

### NCG-side anchor

Wodzicki-residue / a_4 locality argument (S82 W2-5 MP-Exclusion theorem); Connes-Marcolli (2007) §1.17 separates local spectral-action computation from global asymptotic completion. The 5-step decomposition IS that separation applied to regulator-monodromy enumeration.

## 2. V_4 Parallelogram Identity at d = 2 (Substantive Form)

For an atlas with TWO independent regulator-class axes (LOCAL + GLOBAL), the spectral-action moments `A_n^(g)` for n ∈ {0, 2, 4} under the four V_4 cosets g ∈ {e, a, b, ab} satisfy the **parallelogram identity**:

```
| A_n^(ab) + A_n^(e) − A_n^(a) − A_n^(b) | / | A_n^(e) |  ≤  ε
```

with two operationally distinct thresholds:

- **PASS-parallelogram-EXACT**: ε = 1e-10 (substrate-physical structural claim per W-12 R3-A D-2)
- **PASS-parallelogram-APPROX**: ε = 0.05 (numerical-stability tolerance)

**Disjoint-support condition** (residual identity, W-12 §CONVERGENCE C-1 lines 1264-1267 + DISSENT D-1 R2-volovik lines 1086-1119): the residual is zero on disjoint support and equals `4 · m₀ · w(x₀) · x₀^n` on overlap mode at x₀ with multiplicity m₀ and weight w. Empty all-axes-flipped support `{i: σ_M(i) = σ_C(i) = -1} = ∅` is the structural condition for parallelogram-EXACT.

### What the V3 multiplicative character identity FAILS to do (W-12 FALS-W12-2)

The FALSIFIED V3 hypothesis was the multiplicative CHARACTER identity:

```
A_n^(ab)  =  A_n^(a) · A_n^(b) / A_n^(e)
```

This is a 1D group-character form, NOT the cocycle/parallelogram form satisfied by spectral moments. Mode-by-mode substitution chain shows the multiplicative identity holds only for delta-function spectra concentrated on a single mode, or for factorizable σ_M, σ_C with specific tuned values. General spectral moments satisfy the ADDITIVE COCYCLE / PARALLELOGRAM identity instead.

### Algebraic equivalence (W-12 §DISSENT D-1 R3-A lines 1295-1326 + §CONVERGENCE C-1 R3-volovik lines 1517-1535)

The parallelogram identity is symbolically equivalent to the additive cocycle form on the V_4 group. Sage-verified in-workshop. The framing distinction "additive cocycle is ALSO INCORRECT" was a normalization-mismatch artifact retracted at R3-volovik C-1.

## 3. Hypercube-Vertex Character Identity (General Form)

For an atlas with `d = m + k` independent regulator-class axes, the (Z_2)^d hypercube-vertex character identity reads:

```
Σ_{ε ∈ {0,1}^d}  (-1)^|ε|  A_n^(ε)   =   2^d  ·  Σ_{i: σ_j(i) = -1 ∀j}  n_i · w(x_i) · x_i^n
```

where:
- `ε ∈ {0,1}^d` enumerates the 2^d vertices of the d-dimensional hypercube (axis sign-vector)
- `|ε|` is the Hamming weight (number of -1 axes)
- `A_n^(ε)` is the n-th spectral moment under the regulator-class with axis-sign-vector ε
- `σ_j(i) ∈ {±1}` is the sign of mode i under axis j
- `n_i` is the multiplicity of mode x_i
- `w(x_i)` is the regulator weight at mode x_i

The right-hand sum is over modes that flip sign on EVERY axis (the "all-axes-flipped overlap"). When this set is empty, the LHS vanishes — the hypercube-vertex identity holds with EXACT residual.

### Prefactor +2^d

Sage-verified at d ∈ {2, 3, 4} during W-12 (workshop §EMERGENCE E-1 R3-A lines 1385-1430; §CONVERGENCE C-4 R3-volovik lines 1556-1576). S87-HYPERCUBE-VERTEX-IDENTITY-LANDING (CF-W12-4) extends Sage verification to d = 5 and lands the prefactor +2^d as a permanent registry-pinned mathematical identity.

The prefactor IS the structural-not-numerical content; routes via REGISTRY (this file + cross-link to permanent-results-registry) NOT canonical_constants.py.

### Recovery of the parallelogram identity at d = 2

Specializing d = 2 with axes labeled (M, C) and ε ∈ {(0,0), (1,0), (0,1), (1,1)} ↔ {e, a, b, ab}:

```
A_n^(e)  −  A_n^(a)  −  A_n^(b)  +  A_n^(ab)   =   2^2  ·  Σ_{i: σ_M(i) = σ_C(i) = -1}  n_i · w(x_i) · x_i^n
                                              =   4  ·  Σ_{overlap modes}
```

Disjoint support → RHS = 0 → parallelogram-EXACT. The W-12 numerical reproduction (DISSENT D-1 R2-volovik lines 1086-1119; CONVERGENCE C-1 R3-A lines 1264-1267) verified exactly this: disjoint-supports residual = 0; overlap residual = 4·m₀·w(x₀)·x₀². The factor of 4 is +2^d at d=2.

## 4. Disjoint-Support Condition

The parallelogram-EXACT (and hypercube-EXACT at higher d) condition requires that the all-axes-flipped support is empty:

```
{ i :  σ_j(i) = -1  for ALL  j ∈ {axes}  }   =   ∅
```

Equivalently: no spectral mode is flipped by EVERY axis simultaneously. The substrate's bottom-N mode content satisfies this condition iff regulator-monodromy depth is at least the atlas dimension d.

When the support is non-empty, the residual scales as the sum over overlap modes of the per-mode contribution `n_i · w(x_i) · x_i^n` (with the +2^d prefactor). Tracing residual > 0 to specific overlap modes is part of the S87-MONODROMY-V_4-EXPLICIT gate's diagnostic output.

## 5. Regulator-Monodromy Depth (forward-looking observable)

Define the **regulator-monodromy depth** `d_RM(substrate)` as the maximum d for which the (Z_2)^d hypercube-identity holds with EXACT residual on bottom-N modes at saturated L_max. Substrate at τ_fold has depth `d_RM ≥ 2` (V_4 confirmed candidate via S87-MONODROMY-V_4-EXPLICIT); whether `d_RM = 2` exactly or extends to higher d is the question of S87-MONODROMY-DEPTH-EXTENSION (CF-W12-6, latent).

Depth `d_RM` measures how many INDEPENDENT regulator-class boundaries the substrate's mode content respects without overlap; spectral analog of S60 inheritance framework's "correspondence count" (per W-12 §EMERGENCE E-2 R3-volovik lines 1643-1645).

## 6. Calibration Corpus

- **W-12 V_4 = Z_2(Mellin) × Z_2(W6-3) at moment-integral layer**: Sage-verified element orders V_4 = [1,2,2,2] vs Z_4 = [1,2,4,4]; Z_4 cyclic monodromy FALSIFIED. Bare-spectrum monodromy = Z_2 (Mellin reversal only). 4 V_4 cosets map to BULLETIN-4A categories with cardinality 8+1+1+1=11 (workshop §Re:C4 lines 487-521).
- **W-12 V3 multiplicative character identity** (`A_n^(ab) = A_n^(a) · A_n^(b) / A_n^(e)`): FALSIFIED (FALS-W12-2). Replaced by parallelogram identity above.
- **W-12 "Mellin's residue convention structurally tied to ℐ⁺ class"** (V4 Q3 R1-volovik): FALSIFIED (FALS-W12-3). Wodzicki-residue / a_4 is LOCAL invariant; conformal-end choice (Axis_C) determines downstream interpretation as CC contribution but does not change residue value itself.
- **W-12 "PV's 5 rank deviations are non-monotonicity"** (C2): FALSIFIED (FALS-W12-4). Sage-verified d/dx w_PV = -(x-1)/(x+1)³ > 0 ∀ x ∈ [0,1); 5 deviations are intra-stratum-4 float64 tie-break artifacts.

## 7. Cross-References

- **Permanent-results-registry candidate**: REG-W12-1 V_4 monodromy at moment-integral layer (NEEDS-COMPUTATION, gated on S87-MONODROMY-V_4-EXPLICIT)
- **PRU Class-8.2 calibration corpus**: epistemic-discipline.md §"Pre-Registration Completeness" — "Z_4 or similar" admitting Klein-four V_4 as "similar"
- **Connes-Marcolli (2007) §1.17**: separates local spectral-action computation (Seeley-DeWitt expansion) from global completion (choice of asymptotic regime)
- **S82 W2-5 MP-Exclusion theorem**: Wodzicki-residue locality argument anchor for Step 2
- **Correspondence-table-registry**: CORR-W12-3 local-vs-global axis decomposition ↔ Connes-Marcolli §1.17 separation
- **Forward gates**:
  - S87-MONODROMY-V_4-EXPLICIT (CF-W12-1; ~6 hours)
  - S87-PARTITION-STABILITY-4STRATUM (CF-W12-2; ~4-12 hours)
  - S87-STRATUM3-LMAX-SCAN (CF-W12-3; ~4-6 hours)
  - S87-HYPERCUBE-VERTEX-IDENTITY-LANDING (CF-W12-4; ~2 hours; lands the +2^d prefactor + d ∈ {2,3,4,5} Sage verification + extends this file)
  - S87-3HEB-EXCESS-INHERITANCE-COMPARISON (CF-W12-5; ~3-15 hours)
  - S87-MONODROMY-DEPTH-EXTENSION (CF-W12-6; latent, not pre-registered)

## 8. Forward-looking Maintenance

Every PASS at S87-HYPERCUBE-VERTEX-IDENTITY-LANDING extends this file with the new d sub-section (currently d=2 substantive; d=3,4,5 verified in Sage but pending registry-text formalization). Subsequent atlas extensions adding LOCAL or GLOBAL axes update Section 5 with the new depth observation.
