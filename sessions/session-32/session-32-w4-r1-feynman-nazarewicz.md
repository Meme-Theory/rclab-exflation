# Session 32 Workshop W4 Round 1: Feynman x Nazarewicz

**Date**: 2026-03-06
**Agents**: feynman (feynman-theorist), nazarewicz (nazarewicz-nuclear-structure-theorist), coordinator (coordinator)
**Format**: Two-agent workshop with extensive cross-talk. Round 1.
**Mission**: Resolve the BCS pairing kernel at domain walls, stress-test the TRAP-1 trapping margin, determine self-consistent wall profile methodology, and assess the Turing PDE formulation.
**Synthesis Writer**: coordinator

**Input Files**:
- `sessions/session-32/session-32-Team-2-and-3-synthesis.md` (Tesla-LRD-Baptista meta-workshop)
- `sessions/session-32/session-32-Team-4-synthesis.md` (KK-Berry-Landau Round 2)
- `sessions/framework/framework-paasch-potential-master-collab.md` (Paasch wall-intersection master collab)
- `tier0-computation/s23a_kosmann_singlet.npz` (Kosmann pairing kernel)
- `tier0-computation/s32b_wall_dos.npz` (wall DOS, eigenvector overlaps)

---

## 1. Convergent Findings

Where both specialists agree after cross-talk, data verification, and self-correction.

### 1.1 TRAP-1 Margin Is ~1x, Not 100-500x

The central quantitative result of this workshop. Round 2 claimed a 100-500x trapping margin with off-diagonal intra-B2 coupling. This is **RETRACTED**. The verified picture:

**Pairing kernel structure at tau = 0.20** (verified against s23a_kosmann_singlet.npz source code and stored A_antisym matrices):

| Matrix element | Value | Source |
|:---------------|:------|:-------|
| V(B2_i, B2_j) within B2 | 0 (10^{-29}) | Trap 5 / J-reality. DEAD. |
| V(B1, B2_i) cross-branch | 0.0799 per generator subset | Feynman, verified |
| V(B1, B2_i) full sum | 0.311 avg, 0.497 max | Nazarewicz, data-verified |
| V(B1, B1) self-coupling | 0 (10^{-29}) | Trap 5 / J-reality |
| V(B2, B3) cross-branch | 0.006-0.027 | Small, orientation-dependent |
| Intra-B2 doublet 1 | 0.497 | Nazarewicz, data-verified |
| Intra-B2 doublet 2 | 0.287 | Nazarewicz, data-verified |

**V normalization discrepancy resolved**: Feynman's V = 0.0799 was computed from a subset of generators (per-generator contribution). The full-sum V_pairing = sum_a |<psi_i|K_a|psi_j>|^2 over all C^2 generators gives V = 0.12-0.50, consistent with the R2 range 0.09-0.63. Both are correct at their respective levels; the full sum is what enters the BCS gap equation.

**K-1e confirmation**: M_max = 0.104 at mu = 0 in the singlet sector (9.6x below threshold). The K-1e closure from Session 23a is CONFIRMED as correctly computed. The issue is not the coupling magnitude but the BULK DOS being insufficient.

**Wall-enhanced M_max** (Feynman's Thouless criterion, verified):

| Wall Config | tau range | N_B2 (singlet) | M_max | Status |
|:------------|:----------|:---------------|:------|:-------|
| 0 (wide) | [0.10, 0.25] | 12.5 | 0.59-0.92 | FAIL by 1.1-1.7x |
| 1 (medium) | [0.10, 0.20] | 17.7 | 0.84-1.56 | MARGINAL |
| 2 (straddling dump) | [0.15, 0.25] | 21.6 | 1.02-2.20 | PASS by 2-120% |

The range in M_max reflects the normalization uncertainty: Feynman's per-generator V = 0.0799 gives the lower bound; Nazarewicz's full-sum V = 0.311 gives the upper bound. Both agents agree the margin is ~1x -- genuinely borderline at singlet level.

**The transition from FAIL to PASS occurs at N_wall ~ 21.** Wall config 2 (straddling the dump point) is right at this boundary.

### 1.2 BCS Pairing Proceeds Through Shell-Crossing, Not Intra-B2

Both agents converge on the physical mechanism: BCS pairing at the wall is a **shell-crossing** (B1-B2 cross-branch) process, not intra-B2 self-pairing.

- V(B2, B2) = 0 exactly (Trap 5, J-reality). No Cooper pairing within B2.
- V(B1, B2) = 0.08-0.50. The ONLY significant pairing channel involving B2.
- The B1-B2 shell gap is 0.026 (lambda_B2 = 0.845, lambda_B1 = 0.819).

**Nazarewicz's nuclear analog**: This is structurally identical to the high-j intruder problem in nuclear structure. B2 (flat band, 4-fold degenerate) = nuclear i_{13/2} intruder orbital (high degeneracy, flat dispersion). B1 (gap-edge singlet) = last occupied normal-parity shell. The pairing window omega_D is set by the shell gap (0.026), not the B2 bandwidth (~0.001).

**Nuclear regime classification**: With V = 0.31 (avg) and N_wall ~ 22 at best config, g = V*N ~ 2-7. This places the system in the **moderate BCS regime** (120-Sn analog), where mean-field BCS is reliable.

### 1.3 Delta Is a Slaved Variable -- No Independent Dynamics

Both agents independently identify this structural feature: the BCS gap Delta(x) has **no independent kinetic energy or dynamics**. It is determined locally by the gap equation as a function of tau(x).

**Consequence**: The system is NOT a two-field reaction-diffusion (Turing) system. It reduces to a SINGLE scalar field equation:

    G_tt * Box(tau) = -dV_eff^{sc}(tau)/dtau

where V_eff^{sc}(tau) = V_FR(tau) + eta * V_spec(tau) + E_BCS(tau) includes the self-consistent BCS condensation energy E_BCS(tau) = -Delta^2(tau) * N(tau) / 2.

The BCS back-reaction adds a SINGULAR attractive term at the dump point:

    dE_BCS/dtau ~ -c_2 / sqrt(|tau - tau_dump|)

This singularity is integrable (E_BCS ~ -Delta^2 * sqrt(|tau - tau_dump|) is finite) and provides the self-consistent trapping mechanism.

### 1.4 Pattern Formation by Nucleation, Not Turing Instability

Both agents converge: the pattern-forming mechanism for domain walls is **first-order BCS nucleation**, not Turing activator-inhibitor instability.

- Delta is slaved (Section 1.3), eliminating the second field required for Turing
- The cubic Z_3 invariant (c = 0.007 from Landau R2) makes the BCS transition first-order
- Domain walls form as phase boundaries between BCS-condensed and normal phases
- Wall geometry is set by Z_3 topological constraints (Y-junctions), not diffusion-driven patterns

**Nazarewicz's nuclear analog**: Nuclear pasta in neutron star crusts (first-order liquid-gas transition under frustrated Coulomb energy). Geometry set by competition between surface tension and Coulomb frustration. Here: competition between wall surface tension and Z_3 topological constraint.

**Consequence for TURING-1 gate**: The original formulation "lambda_T > 0 (linear instability)" asks the wrong question. The correct question: "Does the first-order BCS phase nucleate at the barrier?" This is a nonlinear bubble-nucleation problem, not a linear stability analysis.

### 1.5 Swallowtail Vertex Is the Trapping Enabler

Both agents agree that the barrier-fold merger at (beta/alpha, eta) = (0.28, 0.04592) from KK's R2 capstone result is **essential** for robust trapping.

At generic eta: Delta/Delta_crit = 0.21-0.66, depending on self-consistency. MARGINAL to FAIL.

At the swallowtail vertex (eta = 0.04592): c_1 = 0. Delta_crit = 0+. Trapping is **unconditional** for any Delta > 0. The van Hove 1/sqrt(|tau - tau_dump|) singularity always dominates the zero potential slope.

**Joint conclusion**: The mechanism chain requires BOTH BCS condensation AND the barrier-fold merger. Neither alone suffices at generic parameters. The swallowtail provides structural stability -- a codimension-1 surface in (beta/alpha, eta) space where trapping works for any nonzero gap.

### 1.6 Self-Consistency Adds a Modest Correction (2-3x)

Nazarewicz's nuclear CHFB experience (Papers 02, 03, 12):
- Self-consistent binding energies differ from one-shot by 10-50%
- Self-consistent pairing gaps change by factors of 2-3x (both directions possible)
- For the wall problem: BCS condensation energy is most negative at wall center (van Hove peak), adding localized attraction
- Expected effect: wall profile NARROWS (BCS pulls tau toward tau_dump from both sides)
- Net Delta enhancement: ~2x (one-shot Delta ~ 0.015 -> self-consistent Delta ~ 0.03)

Self-consistency does NOT change the qualitative verdict. It refines the margin within each regime.

**PT well deepening**: Bare lambda_PT ~ 0.03 -> self-consistent ~0.04-0.05. Bound state count: 1 -> maybe 2. NOT sufficient for 3+ bound states.

### 1.7 LANDAU-SECTOR Test Is Now Highest Priority

Both agents converge: the **LANDAU-SECTOR test** (pre-registered in the Tesla-LRD-Baptista meta-workshop) is the decisive next computation.

If the B2 fold at tau ~ 0.19 is universal across sectors (p,q) != (0,0), multi-sector DOS contributions push M_max well above threshold. Nuclear BCS sums over ALL subshells, not one. The singlet-only M_max = 0.92-2.20 is a LOWER BOUND.

If the fold is singlet-specific, M_max remains borderline.

Zero cost from existing data (Sessions 20a/23a .npz files).

---

## 2. Novel Cross-Talk Results

Results that emerged from Feynman-Nazarewicz interaction, not present in any input file.

### 2.1 Result 1: Slaved Gap Eliminates Turing, Replaces with Nucleation

**Origin**: Nazarewicz identified from nuclear CHFB that Delta has no kinetic energy. Feynman confirmed from the effective action structure. Joint conclusion.

Delta(x) is determined locally by the gap equation -- it has no gradient term, no wave equation, no independent propagation. The system is a **single scalar field** (tau) with a modified potential, not a two-field reaction-diffusion system.

Pattern formation occurs through **nucleation** of the first-order BCS phase transition:
- The modulus encounters a first-order BCS transition at the dump point (Landau R2: cubic c = 0.007)
- Domain walls form as phase boundaries between BCS-condensed and normal phases
- Z_3 topological constraints select wall geometry (Y-junctions at 120 degrees)

This is the nuclear pasta mechanism (neutron star crusts), not Turing.

**TURING-1 revision**: Replace "lambda_T > 0" with "Gamma_nucleation > H" (nucleation rate exceeds Hubble rate during BCS epoch). This is a nonlinear computation.

**Status**: Convergent between both agents. Reframes TURING-1 gate.

### 2.2 Result 2: Shell-Crossing Pairing Identification

**Origin**: Feynman's diagrammatic decomposition identified B1-B2 as the only nonzero coupling. Nazarewicz recognized this as the nuclear high-j intruder problem.

The BCS pairing at the wall is a **2-band mechanism**:
- B1 (singlet, lambda = 0.819): gap-edge mode, moderate DOS
- B2 (quartet, lambda = 0.845): flat-band modes, van Hove enhanced DOS
- Shell gap: 0.026 (sets the pairing window omega_D)
- Coupling: V = 0.08-0.50 (B1-B2 cross-branch)

Nuclear analog: the i_{13/2} high-j intruder in rare-earth nuclei. The intruder has high degeneracy (2j+1 = 14 substates), lies close to the Fermi surface, and drives strong pairing despite being a single orbital. The four-fold B2 degeneracy plays the same role.

**The flat band paradox** (Feynman): B2 bandwidth omega_D(B2) ~ 0.001 -- huge DOS but tiny energy scale. Resolution (Nazarewicz): omega_D is set by the B1-B2 shell gap (0.026), not the B2 bandwidth. The pairing window extends across the gap. Nuclear experience confirms: pairing window ~ 5 MeV for i_{13/2} across a 2 MeV shell gap.

**Status**: Convergent. Identifies the physical pairing mechanism and resolves the flat-band paradox.

### 2.3 Result 3: Trapping Requires Swallowtail -- BCS Alone Insufficient

**Origin**: Feynman's verified M_max at each wall config, combined with Nazarewicz's self-consistency estimates, establish that generic-eta trapping FAILS by ~2-5x while swallowtail trapping PASSES unconditionally.

Quantitative summary:

| Scenario | Delta | Delta_crit | Ratio | Verdict |
|:---------|:------|:-----------|:------|:--------|
| One-shot, generic eta | 0.015 | 0.07 | 0.21 | FAIL |
| Self-consistent, generic eta | 0.03-0.045 | 0.07 | 0.43-0.64 | FAIL |
| One-shot, swallowtail (eta=0.046) | 0.015 | 0+ | infinite | PASS |
| Self-consistent, swallowtail | 0.03-0.045 | 0+ | infinite | PASS |

The mechanism chain requires BOTH ingredients:
1. BCS condensation (Delta > 0 at walls) -- provides the trapping force
2. Barrier-fold merger (c_1 = 0 at swallowtail) -- removes the trapping threshold

Neither alone suffices. This is a clean, quantitative conclusion that sharpens the R2 capstone result.

**Status**: Convergent. Narrows the viable parameter space to the swallowtail neighborhood.

### 2.4 Result 4: TRAP-1 Thouless Threshold at N_wall ~ 21

**Origin**: Feynman derived the Thouless criterion M_max = V_eff * N_B2(wall) / (2 * E_B2) and identified the critical DOS.

The transition from FAIL to PASS in the singlet sector occurs at N_wall ~ 21 B2-analog modes at the wall. The s32b data shows rho_wall = 12.5-21.6 across three wall configurations. Wall config 2 (straddling the dump point, tau = 0.15-0.25) sits RIGHT AT this threshold.

This means:
- The van Hove singularity (representation-theoretic, from d(lambda_B2)/d(tau) = 0) provides EXACTLY the right enhancement
- The coupling V and the DOS N are naturally matched -- neither over- nor under-shoots by orders of magnitude
- Multi-sector contributions would push M_max above threshold with margin

**Status**: Convergent. Establishes quantitative threshold for TRAP-1.

---

## 3. Divergent Assessments

### 3.1 V_pairing Normalization

**Feynman**: V = 0.0799 per generator subset (traced to Session 23a source code).

**Nazarewicz**: V = 0.311 avg, 0.497 max (verified against stored A_antisym matrices, full sum over all C^2 generators).

**Resolution**: Both are correct at their respective levels. The full-sum V_pairing = sum_a |<psi_i|K_a|psi_j>|^2 uses ALL generators. Feynman's value was a partial sum. The M_max range (0.59-2.20) reflects this normalization uncertainty. The TRAP-1 computation must use the full sum.

**Status**: RESOLVED in principle (use full sum). The exact normalization should be confirmed in the TRAP-1 computation.

### 3.2 Self-Consistency Magnitude

**Nazarewicz**: 2-3x enhancement from nuclear CHFB experience. Confident based on 9,400-nucleus UNEDF survey (Paper 12).

**Feynman**: Does not contest the 2-3x estimate but notes that the BCS singular back-reaction (dE_BCS/dtau ~ 1/sqrt) could produce a larger effect near the van Hove singularity than nuclear experience suggests, since nuclei have discrete levels while the wall has a continuum singularity.

**Status**: OPEN. Self-consistent wall computation would resolve.

### 3.3 Multi-Sector Coupling Strength

**Feynman**: Cautions that the cross-sector V_kk' may differ from the singlet value of 0.08-0.50. The 2% margin at singlet level could be erased if cross-sector coupling is weaker.

**Nazarewicz**: Nuclear experience says pairing sums over ALL subshells with comparable matrix elements. The B1-B2 coupling structure (Schur + CG coefficients) should be universal across sectors.

**Status**: OPEN. LANDAU-SECTOR test would resolve.

---

## 4. Corrections to Prior Work

### 4.1 R2 Trapping Margin RETRACTED

**R2 claim**: 100-500x trapping margin with off-diagonal intra-B2 coupling V ~ 0.3-0.63.

**Correction**: The 100-500x estimate conflated the particle-hole V matrix (R2 input) with the BCS pairing kernel. The actual margin at the wall is ~1x (M_max = 0.92-2.20 in singlet). The bifurcation is NOT between coupling channels (off-diagonal vs diagonal) but between eta values (generic vs swallowtail).

**Source**: Feynman diagrammatic analysis + Nazarewicz data verification.

### 4.2 R2 Binary Outcome REVISED to Three Cases

**R2 claim**: Binary outcome -- off-diagonal coupling gives 100-500x PASS, diagonal gives 10^{-4} FAIL.

**Correction**: Three regimes exist:

| Case | Coupling | g | Delta | Trapping |
|:-----|:---------|:--|:------|:---------|
| A: Singlet-only, generic eta | V = 0.31, N = 22 | 2-7 | 0.015 | FAIL (Delta < Delta_crit) |
| B: Multi-sector, generic eta | V ~ 0.31, N >> 22 | >> 7 | > 0.03 | MARGINAL |
| C: Any coupling, swallowtail | Any V > 0 | Any | Any > 0 | PASS (c_1 = 0) |

**Source**: Feynman Thouless calculation + Nazarewicz regime classification.

### 4.3 Feynman Exchange Claim RETRACTED

**Feynman's initial claim**: Exchange diagrams nearly cancel the direct Cooper interaction. V_BCS = 0.001. rho_crit = 1266 (47-250x above wall DOS).

**Retraction**: The Kosmann interaction is a CONTACT 4-fermion interaction (V = sum |<i|K_a|j>|^2). There is no separate exchange diagram in a contact interaction. The calculation incorrectly imported Coulomb exchange formalism.

**Source**: Feynman self-correction after tracing Session 23a source code.

### 4.4 TURING-1 Gate Formulation Questioned

**Prior formulation**: "lambda_T > 0" (linear Turing instability exists).

**Correction**: Delta is a slaved variable with no independent dynamics. The system is single-field, not reaction-diffusion. The correct question is nonlinear bubble nucleation, not linear stability.

**Proposed revision**: Replace "lambda_T > 0" with "Gamma_nucleation > H" (nucleation rate exceeds Hubble rate during BCS epoch).

**Source**: Nazarewicz (nuclear CHFB) + Feynman (effective action analysis). Convergent.

---

## 5. Concrete Computation Plan

### Priority 1: LANDAU-SECTOR Test (ZERO COST)

**What**: Check whether the B2 eigenvalue minimum at tau ~ 0.19 exists in sectors (1,0), (0,1) from existing .npz data.

**Why decisive**: If universal, multi-sector DOS pushes M_max well above threshold at singlet level. If singlet-specific, M_max remains borderline.

**Pre-registered diagnostic** (from Tesla-LRD-Baptista meta-workshop):
- UNIVERSAL: all sector minima within delta_tau < 0.02 of each other
- SINGLET-SPECIFIC: any minimum shifts by delta_tau > 0.05

**Input**: Sessions 20a/23a .npz files.
**Output**: Sector-resolved B2-analog eigenvalue minima.
**Cost**: Zero (existing data).
**Depends on**: Nothing.

### Priority 2: TRAP-1 REVISED -- Multi-Branch BdG at Wall

**What**: Solve multi-branch BdG (B1-B2 cross-shell, 4 B2 modes) at wall using full-sum V_pair from s23a_kosmann_singlet.npz. Include multi-sector DOS from s23a_eigenvectors_extended.npz (11,424 modes, 28 sectors).

**Pre-registered gates**:
- Delta_wall > 0 (BCS condensation exists)
- M_max > 1 (Thouless threshold)
- At swallowtail (eta = 0.046): any Delta > 0 suffices for trapping

**Input**: s23a_kosmann_singlet.npz, s23a_eigenvectors_extended.npz, s32b_wall_dos.npz.
**Output**: Delta(wall), M_max, trapping verdict.
**Cost**: Medium.
**Depends on**: Priority 1 (LANDAU-SECTOR determines multi-sector contribution).

### Priority 3: Self-Consistent CHFB Wall Profile

**What**: Iterative solution of coupled tau(x)-Delta(x) system. Discretize wall on ~100 grid points. Iterate 15-30 times.

**Algorithm** (Nazarewicz, from constrained HFB):
1. Initialize tau(x) from KK's kink soliton profile (s33w3_modulus_equation.npz)
2. At each grid point: interpolate B2 eigenvalues, compute local DOS
3. Solve multi-branch BdG locally (B1-B2 cross-shell)
4. Compute E_BCS(x) = -Delta^2(x) * N(x) / 2
5. Update V_total = V_FR + eta*V_spec + E_BCS
6. Re-solve 1D kink ODE with modified V_total
7. Repeat until convergence

**Pre-registered gate**: Does self-consistency increase Delta by > 2x?

**Input**: TRAP-1 results + s33w3_modulus_equation.npz (wall profiles).
**Output**: Self-consistent tau(x), Delta(x), convergence history.
**Cost**: Medium-High.
**Depends on**: Priority 2 (TRAP-1 provides starting Delta).

### Priority 4: Nucleation Rate Calculation (TURING-1 Replacement)

**What**: Compute bubble nucleation rate Gamma for first-order BCS phase transition at the Freund-Rubin barrier.

**Pre-registered gate**: Gamma_nucleation > H (nucleation rate exceeds Hubble rate during BCS epoch).

**Input**: V_eff from modulus equation, BCS free energy from TRAP-1.
**Output**: Nucleation rate, bubble critical radius.
**Cost**: Medium.
**Depends on**: Priority 2.

### Diagnostics (Zero-Cost)

| Diagnostic | What It Tests | Data Source |
|:-----------|:-------------|:-----------|
| V_pairing normalization | Full-sum vs per-generator | s23a_kosmann_singlet.npz |
| Cross-sector V_kk' comparison | Coupling universality | s23a_eigenvectors_extended.npz |
| B1 DOS at wall | B1 enhancement (aids 2-band BCS) | s32b_wall_dos.npz |

---

## 6. Gate Pre-Registrations

### 6.1 Revised Gates

| Gate | Original Threshold | Revised Threshold | Reason |
|:-----|:-------------------|:------------------|:-------|
| TRAP-1 | Delta_wall > 0 AND L_BCS > E_kin | M_max > 1 (Thouless) OR eta = 0.046 (swallowtail) | Thouless criterion is the correct formulation |
| TURING-1 | lambda_T > 0 (linear instability) | Gamma_nucleation > H (bubble nucleation) | Delta is slaved; system is single-field |

### 6.2 New Pre-Registrations

| Gate | Threshold | Source | Computation |
|:-----|:----------|:-------|:------------|
| LANDAU-SECTOR | B2-analog minima within delta_tau < 0.02 across sectors | Tesla-LRD-Baptista meta-workshop + this workshop (elevated to Priority 1) | Sector-resolved eigenvalue sweep from existing data |
| CHFB-convergence | Self-consistent Delta / one-shot Delta > 2 | Nazarewicz nuclear experience | Iterative CHFB computation |
| NUC-1 | Gamma_nucleation > H at the BCS barrier | This workshop (replaces TURING-1) | Bubble nucleation rate |

---

## 7. Constraint Map Updates

### 7.1 New Constraints

**Constraint W4-R1-A**: M_max(wall, singlet) = 0.92-2.20 from Thouless criterion with V_pair = 0.08-0.50, N_B2(wall) = 12.5-21.6.
**Source**: Feynman diagrammatic + Nazarewicz data verification.
**Implication**: Wall BCS is RIGHT AT THRESHOLD in the singlet sector. Neither overwhelming PASS nor definitive FAIL.
**Surviving solution space**: Multi-sector contributions or swallowtail vertex push to definitive PASS.

**Constraint W4-R1-B**: Delta is a slaved variable. The BCS gap has no independent dynamics.
**Source**: Nazarewicz (nuclear CHFB) + Feynman (effective action). Convergent.
**Implication**: System is single-field (tau only). Turing activator-inhibitor framework eliminated.
**Surviving solution space**: First-order nucleation as pattern-forming mechanism.

**Constraint W4-R1-C**: BCS pairing proceeds through B1-B2 shell-crossing channel. V(B2,B2) = 0 exactly (Trap 5).
**Source**: Feynman pairing kernel decomposition, verified against source code.
**Implication**: B2 does not self-pair. All BCS coupling flows through the B1 gap-edge mode.
**Surviving solution space**: Shell-crossing BCS with omega_D = shell gap (0.026).

**Constraint W4-R1-D**: The R2 trapping margin of 100-500x is incorrect. Actual margin is ~1x.
**Source**: Feynman Thouless criterion + Nazarewicz data verification.
**Implication**: TRAP-1 is genuinely uncertain, not a guaranteed PASS.
**Surviving solution space**: Swallowtail vertex (unconditional) or multi-sector enhancement.

### 7.2 R2 Constraints Updated

| R2 Constraint | Update |
|:-------------|:-------|
| W3-R2-F (Delta_crit ~ 0.07-0.10) | CONFIRMED. Delta(wall) ~ 0.015 one-shot vs 0.07 threshold = 4.7x shortfall at generic eta. |
| W3-R2-H (barrier-fold merger) | ELEVATED. Swallowtail is now the only robust trapping path. |
| W3-R2-I (binary 100x/10^{-4}) | CORRECTED to three cases (Section 4.2). |
| W3-R2-J (swallowtail unconditional) | CONFIRMED and now ESSENTIAL (not merely convenient). |

---

## 8. Open Questions

### 8.1 Is the B2 Fold Universal Across Sectors?

The LANDAU-SECTOR test determines whether M_max(wall) is borderline (singlet-only, ~1x) or comfortably above threshold (multi-sector). Zero-cost from existing data. Highest priority.

### 8.2 What Is the Full-Sum V_pairing Normalization?

Feynman's per-generator V = 0.0799 and Nazarewicz's full-sum V = 0.311 are both self-consistent but give different M_max estimates (0.59-1.02 vs 0.92-2.20). The TRAP-1 computation must resolve this by using the correctly normalized pairing kernel.

### 8.3 Does Self-Consistency Enhance or Suppress Delta at the Van Hove Singularity?

Nuclear experience says 2-3x either direction. Feynman notes that the van Hove continuum singularity may produce a larger enhancement than nuclear discrete levels. Resolution requires the full CHFB computation.

### 8.4 How Robust Is the Swallowtail to BCS Back-Reaction?

The barrier-fold merger was computed from V_eff without BCS back-reaction. Does the BCS condensation energy shift the merger point in (beta/alpha, eta) space? If it shifts significantly, the swallowtail may not sit at eta = 0.046.

### 8.5 What Is the Bubble Nucleation Rate?

With TURING-1 reframed as nucleation, the quantitative gate is Gamma_nucleation > H. The critical bubble radius and nucleation barrier depend on the BCS free energy landscape, which requires TRAP-1 output.

---

## 9. Self-Corrections During Workshop

### Feynman Self-Corrections

1. **"Exchange kills Cooper pairing" (RETRACTED)**: Incorrectly applied Coulomb exchange formalism to a contact interaction. The Kosmann interaction V = sum |<i|K_a|j>|^2 has no separate exchange diagram. Corrected after tracing Session 23a source code.

2. **"V*N ~ 0.3-0.4 weak coupling" (REVISED)**: Used per-generator V = 0.0799 in an incorrect formula. Correct Thouless criterion gives M_max ~ 0.6-1.0 at wall, depending on normalization.

3. **"100-500x margin" (CORRECTED to ~1x)**: R2 used V ~ 0.63 including all-branch contributions. The B1-B2 coupling that drives BCS gives margin ~1x.

### Nazarewicz Self-Corrections

1. **V(B1,B2) = 0.0799 (CORRECTED to 0.311 avg)**: Initially adopted Feynman's per-generator value. Data verification against stored A_antisym matrices showed full-sum V = 0.311 avg, 0.497 max.

2. **"100-500x retraction" (PARTIALLY WALKED BACK)**: The retraction of R2's margin was premature -- the correct V range (0.12-0.50) IS consistent with R2. However, the margin is ~1x at singlet level, not 100-500x.

3. **g = 0.3-0.4 marginal (CORRECTED to g = 2-7)**: Initial estimate used wrong V and N_eff. With full-sum V and wall DOS, g is in moderate BCS regime.

---

## Summary

This workshop produced one central quantitative result: **TRAP-1 margin is ~1x** (M_max = 0.92-2.20 at singlet level), not the 100-500x claimed in Round 2. The mechanism chain is genuinely borderline -- not dead, not guaranteed.

Three novel results survived all corrections and retractions:
1. **Slaved gap eliminates Turing**: Pattern formation by first-order nucleation, not activator-inhibitor instability. TURING-1 gate needs revision.
2. **Shell-crossing pairing is the physical channel**: B1-B2 coupling across the 0.026 shell gap drives BCS. Nuclear i_{13/2} intruder analog. omega_D = shell gap.
3. **Swallowtail vertex is essential for trapping**: Generic eta gives Delta/Delta_crit ~ 0.2-0.6 (FAIL). Swallowtail (eta = 0.046) gives unconditional PASS for any Delta > 0.

The decisive next computation is the **LANDAU-SECTOR test** (zero cost, existing data). If the B2 fold is universal across sectors, multi-sector DOS pushes M_max well above threshold. If singlet-specific, the mechanism chain depends entirely on the swallowtail.

One retraction documented (Feynman: exchange kills Cooper -- wrong formalism). One major R2 correction (100-500x margin -> ~1x). Four R2 constraints updated.

---

*Synthesis by coordinator. Integrates Feynman's diagrammatic BCS analysis (pairing kernel decomposition, Thouless criterion, wall-enhanced M_max, effective action) and Nazarewicz's nuclear structure methodology (constrained HFB algorithm, shell-crossing identification, regime classification, self-consistency estimates). Cross-talk messages exchanged between both agents, including one retraction (exchange) and multiple data-verification rounds. Three novel results stable after all corrections. All self-corrections documented with sources.*
