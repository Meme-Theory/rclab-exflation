# S75 Pomeranchuk Audit: Reclassification of Permanent Result #14

**Author**: Tesla-Resonance (Workhorse-Resonance)
**Date**: 2026-04-12
**Scope**: Bookkeeping audit of the Pomeranchuk instability result chain in light of S75 W4-K

---

## 1. Registry Entry: Current Text

The Pomeranchuk result appears in three locations within the permanent results registry (`sessions/permanent-results-registry.md`):

### 1A. Proven robustness audit theorem #14 (S73B numbering)

This is the numbering used in `s73b_proven_robustness_audit.py`, `s74_w5f_reverify.py`, and `s75_lmax_bidirectional.py`. The entry reads:

> **#14**: Pomeranchuk instability: f(0,0) = -4.687 < -3, g\*N(0) = 3.24
> Session: S22c F-1
> Proof type: NUMERICAL_L3
> Status: VERIFIED (L_max=7, S74 W4-N; L_max=5/7, S75 W3-A)

### 1B. Computed quantities table (Section IV)

> | f(0,0) Pomeranchuk | -4.687 (threshold -3) | 22c F-1 | Computed |

### 1C. NEEDS_REVERIFY section (now resolved)

> | S22c F-1 | Pomeranchuk f(0,0) = -4.687, g\*N(0) = 3.24 | g\*N(0) = 3.24 is algebraic via block-diagonality (N=2 singlet only, S34 correction). f(0,0) value uses BdG self-consistency at L_max=3. | g\*N(0) is permanent. f(0,0) may shift slightly; Pomeranchuk verdict (f < -3) has 1.7x safety margin. |

### 1D. User MEMORY.md PROVEN list

> Pomeranchuk

Listed as one of 16 PROVEN results.

### 1E. User framework-status.md

> Pomeranchuk instability (22c F-1): f(0,0)=-4.687 < -3. g\*N(0)=3.24

---

## 2. W4-K Findings (S75, Landau Condensed-Matter Theorist)

**Gate**: S75-N2-POMERAN-N. **Verdict: FAIL** (no instability at any N_cells).

### 2A. Method

Lattice RPA with Josephson coupling on three graph topologies (cycle C_N z=2, complete K_N z=N-1, CG(24)-approximation z=6) at N_cells = {4, 8, 12}. Two approaches:

- **(A) Perturbative RPA**: bare Josephson correction to single-cell Landau matrix
- **(B) Self-consistent RPA**: gap-screened Josephson with R_SC = Delta^2/(Delta^2 + J^2 z^2 gamma^2)

### 2B. Key numbers (z=6, CG(24)-like)

| N_cells | min(1+F) pert | min(1+F) SC | Pom(pert) | Pom(SC) |
|---------|---------------|-------------|-----------|---------|
| 4       | -0.458        | +0.946      | VIOLATED  | STABLE  |
| 8       | -0.458        | +0.946      | VIOLATED  | STABLE  |
| 12      | -0.458        | +0.946      | VIOLATED  | STABLE  |

### 2C. Critical thresholds

- **Perturbative z_crit** = 4.10 (all N)
- **Self-consistent z_crit** > 20 (all N)
- **CG(24) coordination number** z = 6
- **E_J/E_cond** = 24.8 (Josephson coupling 25x stronger than condensation energy)

### 2D. Physical interpretation (W4-K)

> "The perturbative instability at z >= z_crit ~ 4.1 is an artifact of treating E_J >> |E_cond| (ratio 24.8) as a perturbation. The BCS condensate screens the Josephson coupling through the Higgs mechanism: R_SC = Delta_BCS^2/(Delta_BCS^2 + (J z gamma)^2) << 1 in the strong-pairing regime."

---

## 3. Complete Pomeranchuk Computation History

Chronological chain of all prior computations found (15 scripts in computation-archive, 24 in computations/_shared):

### S22c F-1 (2026-01, computation-archive)
- **Definition**: Spectral-flow Landau parameter on SINGLE-CELL D_K spectrum
- **Formula**: f_{pq} = -<d(lambda)/d(tau)>_avg * N(0) / lambda_F
- **Result**: f(0,0) = -4.687 at tau = 0.30. Threshold = -3. Verdict: UNSTABLE
- **Scope**: Single cell, (0,0) sector only, spectral flow definition
- **Note**: g\*N(0) = 3.24 (deep BEC regime)

### S28b L-5 (2026-02, computation-archive)
- **Definition**: Per-sector Pomeranchuk map using Kosmann pairing matrices
- **Result**: ALL 9/9 sectors Pomeranchuk-unstable (D_K basis). Deepest: (1,0) at tau=0.35, f_0=-312.8
- **Scope**: Multi-sector single-cell. Diagnostic only.
- **Note**: Diagnosed tension: f_0 << -1 but BCS subcritical at mu=0

### S53 POMERANCHUK-HFB-53 (2026-03, computations/_shared)
- **Definition**: Direct V_ph * N(0) using HFB self-consistent spectrum
- **Result**: f_0 = +0.156 (REPULSIVE). S22c f_0=-4.687 RECLASSIFIED as spectral flow diagnostic, not direct particle-hole
- **Scope**: Single cell, HFB self-consistent
- **Status**: INFO. "Instability is Cooper channel, not Pomeranchuk channel"
- **CRITICAL**: This was the first indication that the S22c "Pomeranchuk" label was a misnomer

### S58 POMERANCHUK-GGE-58 (2026-03, computations/_shared)
- **Definition**: Full susceptibility matrix of GGE occupations
- **Result**: max|F_alpha| = 0.062. ALL within stability bounds. GGE is Pomeranchuk-STABLE
- **Gate verdict**: FAIL (no instability)
- **Scope**: Single cell, GGE state, full angular channel decomposition
- **Note**: Thermal smearing suppresses S22a instability by 50x

### S61 POMERAN-FABRIC-61 (2026-03, computations/_shared)
- **Definition**: Exact diagonalization of 2-cell Josephson-coupled system (dim=65536)
- **Result**: Deep stability (effective F ~ 10^6 from locked-phase compressibility)
- **Scope**: 2-cell, exact diag, Josephson-dominated regime
- **Note**: E_J/|E_cond| = 24.8 invalidates perturbative treatment

### S66 POMERAN-4CELL-66 (2026-03, computations/_shared)
- **Definition**: Lattice RPA on 4-cell C_4 cycle graph (z=2)
- **Result**: Perturbative F_0(q=0) ~ -0.49, still stable (cycle z=2 < z_crit=3.4)
- **Gate verdict**: FAIL (stable)
- **Scope**: 4-cell, perturbative RPA, z=2 topology

### S74 W4-N / W5F-REVERIFY-74 (2026-04, computations/_shared)
- **Definition**: L_max reverification of spectral-flow f(0,0)
- **Result**: f(0,0) = -15.7367 at BOTH L_max=3 and L_max=7. IDENTICAL to machine precision
- **Status**: VERIFIED (as L_max-invariant)
- **Note**: Value differs from S22c (-4.687) due to using full 8-mode spectral flow

### S75 W3-A / L-MAX-BIDIRECTIONAL-75 (2026-04, computations/_shared)
- **Definition**: Bidirectional L_max reverification at L_max = {5, 7}
- **Result**: f(0,0) = -15.7367 at both. Rel diff = 0.000e+00
- **Status**: ROBUST (L_max-invariant)
- **Note**: Confirmed W4-N result with independent L_max=5 data point

### S75 W4-K / POMERAN-N-SCAN-75 (2026-04, computations/_shared)
- **Definition**: Multi-cell lattice RPA with BOTH perturbative and self-consistent screening
- **Result**: Perturbative z=6: min(1+F) = -0.458 (VIOLATED). Self-consistent z=6: min(1+F) = +0.946 (STABLE)
- **Gate verdict**: FAIL (no instability at any N)
- **Scope**: N_cells = {4, 8, 12}, three graph topologies
- **Note**: F_0^s is N-INDEPENDENT. Self-consistent z_crit > 20, far above CG(24) z=6

### S75 W4-M / ATLAS-RECLASSIFY-75 (2026-04, computations/_shared)
- **Definition**: Reclassification of 70 NEEDS_REVERIFY entries
- **Result**: Pomeranchuk classified as ROBUST (L_max-invariant spectral flow)
- **Note**: This classifies the SPECTRAL FLOW QUANTITY as robust, not the physical instability conclusion

---

## 4. Analysis: What Exactly Is "Proven"?

The audit reveals that the Pomeranchuk result chain actually contains TWO distinct claims that have been conflated:

### Claim A: The spectral-flow Landau parameter f(0,0) satisfies f < -3

This is a mathematical fact about D_K on Jensen-deformed SU(3). The quantity f_{pq} = -<d(lambda)/d(tau)>_avg * N(0) / lambda_F is computed from (0,0) sector eigenvalues alone. It is:

- **Block-diagonal protected**: (0,0) sector eigenvalues are L_max-invariant (permanent #1)
- **Verified at L_max = 3, 5, 7**: Identical to machine precision (S74 W4-N, S75 W3-A)
- **Algebraically permanent**: g\*N(0) = 3.24 follows from block-diagonality (N=2 singlet)
- **Value**: f(0,0) = -15.7367 (S75 full formula) or -4.687 (S22c restricted formula). Both satisfy f < -3.

**STATUS: PERMANENTLY PROVEN as a mathematical identity on D_K.**

### Claim B: The physical fabric is Pomeranchuk-unstable

This would mean the quasiparticle description breaks down -- the Fermi surface spontaneously deforms. This is:

- **CONTRADICTED by S53**: Direct V_ph gives f_0 = +0.156 (repulsive). The "instability" is in the Cooper channel, not the Pomeranchuk channel.
- **CONTRADICTED by S58**: GGE state is Pomeranchuk-stable. max|F_alpha| = 0.062.
- **CONTRADICTED by S61**: 2-cell exact diag shows deep stability (F ~ 10^6).
- **CONTRADICTED by S66**: 4-cell perturbative RPA gives stability at z=2.
- **CONTRADICTED by S75 W4-K**: Self-consistent multi-cell gives min(1+F) = +0.946 at physical z=6.

**STATUS: CLOSED. The physical fabric is Pomeranchuk-STABLE. The spectral-flow f(0,0) < -3 is a property of the eigenvalue flow on D_K, not a physical Fermi-liquid instability.**

---

## 5. Reclassification Recommendation

### Current text (S73B audit, theorem #14):

> Pomeranchuk instability: f(0,0) = -4.687 < -3, g\*N(0) = 3.24

### Recommended new text:

> **Spectral-flow Landau parameter**: f(0,0) < -3 on Jensen-deformed SU(3) in the (0,0) sector. Block-diagonal protected, L_max-invariant (verified L=3,5,7). Value: -15.7367 (full 8-mode formula) or -4.687 (restricted S22c formula). g\*N(0) = 3.24 (algebraic). This is a mathematical property of D_K eigenvalue flow, NOT a physical Pomeranchuk instability. The physical fabric is Pomeranchuk-stable at all N_cells by self-consistent gap-screened RPA (S75 W4-K: min(1+F) = +0.946, z_crit_SC > 20 >> z_CG(24) = 6).

### Changes to registry sections:

1. **Theorem #14 name**: Change from "Pomeranchuk instability" to "Spectral-flow Landau parameter f(0,0) < -3"
2. **Computed quantities table**: Change "f(0,0) Pomeranchuk" entry to note it is a spectral-flow quantity, not a physical instability
3. **NEEDS_REVERIFY section**: Already resolved. No change needed -- the L_max invariance IS the permanent content
4. **Session ranking table**: Entry 8 "Pomeranchuk, Trap 3, Perturbative Exhaustion Theorem" -- add parenthetical "(spectral flow, not physical instability)"
5. **User MEMORY.md PROVEN list**: Change "Pomeranchuk" to "Spectral-flow f(0,0)<-3 (Pomeranchuk-STABLE physically)"

---

## 6. Impact Assessment on Constraint Map

### What changes:

1. **The fabric is Pomeranchuk-stable**: This is now a permanent positive result, not an instability. The quasiparticle description is self-consistent at ALL scales. This STRENGTHENS the BCS framework, not weakens it.

2. **The perturbative/self-consistent boundary at z_crit=4.10 vs z_crit_SC>20**: This establishes a new structural wall. Perturbative RPA is illegitimate for the physical CG(24) fabric (z=6, E_J/E_cond = 24.8). Any future computation using perturbative Landau parameters on the multi-cell fabric MUST use the self-consistent screening factor R_SC.

3. **N-independence of F(q=0)**: This is a new structural theorem. The Pomeranchuk parameter at q=0 does not depend on N_cells. Adding cells adds q-points with |gamma| < 1 but does not change the most dangerous mode.

### What does NOT change:

1. **The spectral-flow quantity f(0,0) < -3**: This remains proven. It is a mathematical identity on D_K, protected by block-diagonality.

2. **g\*N(0) = 3.24**: This remains algebraic and permanent.

3. **The BCS condensation mechanism**: The fact that f(0,0) < -3 as a spectral-flow quantity indicates strong eigenvalue-flow softening in the (0,0) sector. This is EXACTLY what drives BCS condensation. The instability is in the pairing channel (Cooper), not the density channel (Pomeranchuk). S53 already identified this correctly.

4. **All downstream BCS results**: BCS protection theorems (S69, 7 theorems), gap scaling (permanent #25), GGE universality (permanent #26), Volovik partition (permanent #27) -- none of these depend on Pomeranchuk instability. They depend on the BCS condensate existing, which is driven by the Cooper channel, not the Pomeranchuk channel.

### What opens:

Nothing. Pomeranchuk stability is the expected physical result for a BCS condensate with strong gap screening. The S53 reclassification already pointed in this direction. W4-K makes it quantitative and permanent.

### What closes:

The possibility that the fabric's quasiparticle description breaks down at large N_cells due to Pomeranchuk instability is PERMANENTLY CLOSED. This strengthens the Fermi-liquid foundation of the entire BCS analysis chain.

---

## 7. Downstream Result Audit

### Results that referenced "Pomeranchuk instability":

1. **S22c session ranking (entry #8)**: References Pomeranchuk as a key result. Reclassify wording.
2. **S28b L-5 gate verdict**: "Universal instability" diagnostic. Superseded by S53/S58/S75.
3. **Block-diagonal theorem protection claim**: States that DNP, Pomeranchuk, and phi_paasch are protected by block-diagonality. This remains true for the spectral-flow QUANTITY. The PHYSICAL INTERPRETATION changes.
4. **S74 foundational audit spec**: References "#14 Pomeranchuk" as one of 22 theorems in the floor. The theorem survives as a spectral-flow identity; the name changes.
5. **S75 W4-M atlas reclassify**: Classifies Pomeranchuk as ROBUST. Correct for the spectral-flow quantity.

### Results that DEPENDED on Pomeranchuk instability being physically real:

**NONE FOUND.** No computation in the chain from S22c through S75 uses the Pomeranchuk instability as an INPUT to derive another result. The BCS mechanism chain (I-1, RPA, Turing, WALL, BCS -- all PASS since S35) is driven by the Cooper channel, not the Pomeranchuk channel. S53 already clarified this distinction.

---

## 8. Carry-Forward Computations

### Required updates (bookkeeping):

1. **permanent-results-registry.md**: Rename theorem #14 per Section 5 above
2. **User MEMORY.md**: Update PROVEN list entry
3. **User framework-status.md**: Update Pomeranchuk line

### New permanent results to register:

1. **Pomeranchuk STABILITY of the physical fabric**: min(1+F) = +0.946 at physical z=6, self-consistent. N-independent. z_crit_SC > 20. (Source: S75 W4-K)
2. **N-independence of F(q=0)**: Structural theorem from W4-K. The q=0 mode (maximizing gamma=1) always determines the most dangerous Pomeranchuk direction, and its eigenvalue is N-independent.
3. **Perturbative RPA illegitimacy wall**: At E_J/E_cond = 24.8, perturbative treatment of Josephson coupling is structurally invalid. Self-consistent gap screening mandatory.

### No new computations required:

The reclassification is purely a matter of correctly distinguishing a spectral-flow mathematical identity from a physical Fermi-liquid instability. All numerical content is already computed and verified.

---

## 9. Summary

The Pomeranchuk result #14 should be RECLASSIFIED, not retracted. The mathematical content (f(0,0) < -3 as a spectral-flow identity on D_K) is permanently proven and L_max-invariant. The physical interpretation ("Pomeranchuk instability") was already challenged by S53 (2026-03, which found f_0 = +0.156 for the direct particle-hole channel) and is now definitively closed by S75 W4-K (self-consistent min(1+F) = +0.946 at physical coupling).

The fabric is Pomeranchuk-STABLE. This is a positive structural result that strengthens the BCS foundation of the entire framework.

No downstream results are affected because no computation in the chain ever used the Pomeranchuk instability as an input to derive another result. The BCS mechanism chain runs through the Cooper channel, which is the correct physical identification (as S53 already noted).

The reclassification is: "Pomeranchuk instability" --> "Spectral-flow Landau parameter f(0,0) < -3 (Pomeranchuk-STABLE physically)".
