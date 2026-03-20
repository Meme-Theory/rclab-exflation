# Session 34a Synthesis: D_phys Fold Survival and Trap 1 Confirmation

**Date**: 2026-03-06
**Format**: 3-agent team (bap, connes, coord)
**Prompt**: session-34-plan.md (D_phys spectrum and mechanism chain survival under inner fluctuations)
**Gate verdicts**: tier0-computation/s34a_gate_verdicts.txt

---

## 1. Session Outcome

All five pre-registered gates were computed. Four returned favorable verdicts; one FAILED.

| Gate | Type | Verdict | Key Number |
|:-----|:-----|:--------|:-----------|
| DPHYS-34a-1 | Existential | **PASS** | d2 = 1.226 at phi=gap (fold survives) |
| TRAP1-34a | Structural | **CONFIRMED** | V(B1,B1) = 0.000 exact (Trap 1 remains) |
| DPHYS-34a-2 | Existential | **PASS** | V(B2,B2) = 0.086 at phi=gap (50% enhanced) |
| DPHYS-34a-3 | Existential | **FAIL** | M_max = 0.899 at phi=gap (all walls < 1) |
| RPA-34a | Diagnostic | **CONSISTENT** | d2S = 180.09 at phi=gap (333x margin) |

The B2 eigenvalue fold survives inner fluctuations (34a-1), the Kosmann pairing kernel is enhanced by 50% in the D_phys eigenbasis (34a-2), and the spectral action curvature increases to 333x margin (RPA-34a). However, the Thouless criterion FAILS: M_max = 0.899 < 1.0 at phi=gap for all wall configurations. The BCS link is CLOSED in the correct spinor pairing basis.

**Upstream Finding**: The computation also revealed that TRAP-33b (M_max = 2.062) used the wrong V matrix -- frame-space structure constants instead of spinor matrix elements. The correct spinor V gives M_max = 0.90, below threshold even at phi=0. The Kosmann-BCS mechanism was never above threshold in the correct basis.

---

## 2. DPHYS-34a-1: Fold Survival Under Inner Fluctuations

### 2.1 What Was Computed

The physical Dirac operator D_phys = D_K + phi + J*phi*J^{-1} was constructed in the singlet Peter-Weyl sector. The inner fluctuation phi = sum_i a_i[D_K, b_i] was built from the algebra A_F = C + H + M_3(C) acting on the 16-dimensional eigenspace. The fold location, curvature, and B2 splitting were tracked as a function of the fluctuation amplitude |phi_VEV|.

### 2.2 J Operator Correction

The charge conjugation operator J used in prior sessions (B = sigma_2^{x4}) was incorrect. The correct J for KO-dimension 0 is:

C2 = gamma_1 * gamma_3 * gamma_5 * gamma_7

This is the product of real gamma matrices in the Clifford algebra Cl(4). It satisfies J D_K J^{-1} = +D_K to machine epsilon.

**Upstream impact**: NONE. Verified by inspection of all tier0 scripts:
- TRAP-33b, K-1e retraction, Kosmann kernel computations: no J usage
- build_J_projector (Sessions 26-28): uses spectral pairing, not explicit J matrix
- s28c axiom check: KO-dim 6 based on J^2 = +I (valid for both B and C2); axiom 4 intertwining signs should be re-verified (non-blocking)

All 5 prior mechanism chain gates are unaffected by the J correction.

### 2.3 Quantitative Results

| Quantity | Value |
|:---------|:------|
| d2 at phi=0 (bare) | 1.176 |
| d2 at phi=gap (0.133) | 1.226 |
| tau_min at phi=gap | 0.190 (no drift) |
| B2 splitting at phi=gap | 0.021 |
| Maximum surviving |phi| | 0.17 (1.28x gate threshold) |
| Fold destroyed at | 0.18 |
| Strong Pass threshold (2*gap) | 0.266 |

The fold is **stabilized** by inner fluctuations in the worst-case electroweak direction: d2 increases from 1.176 to 1.226. This was not predicted by W1 -- the destruction bound of 0.42 predicted survival but not reinforcement.

### 2.4 Generator Survey

At |phi| = gap, 10 of 13 A_F generators preserve the fold (77%). All electroweak generators (C_Im, H_i, H_j, H_k) preserve it. Three color generators (M3_2, M3_3, M3_6) destroy the fold by shifting tau_min outside the [0.14, 0.24] window. The physical phi is a linear combination of all generators; the worst-case single-generator result (H_j) was used for the gate.

### 2.5 Cross-Checks

Five independent cross-checks passed:
1. J commutation: J D_K J^{-1} = +D_K (machine epsilon)
2. Eigenvalue reconstruction at phi=0
3. phi=0 reproduces bare D_K spectrum exactly
4. Perturbation theory scaling: corrections O(phi^2)
5. Algebra commutation relations verified

### 2.6 DPHYS-34a-2: Kosmann Kernel Reprojection

The Kosmann pairing kernel V_nm = sum_{a=0}^7 |<psi_n|K_a|psi_m>|^2 was recomputed in the D_phys eigenbasis, where psi_n(phi) are eigenvectors of D_phys = D_K + phi + J*phi*J^{-1}. The K_a matrices (Kosmann-Lichnerowicz derivatives along su(3) Killing fields) are unchanged -- they are geometric properties of the isometry algebra. Only the basis rotates.

**Method**: The overlap matrix U = evecs_bare^H @ evecs_phys transforms K_a from the bare eigenspinor basis to the D_phys eigenspinor basis: K_a^{phys} = U^H K_a^{bare} U. The B2 branch in the D_phys spectrum is identified by maximum overlap with bare B2 eigenstates.

**Quantitative Results** (tau = 0.20, worst-case H_j direction):

| Quantity | phi = 0 (bare) | phi = gap (0.133) | Change |
|:---------|:---------------|:------------------|:-------|
| V(B2,B2) max off-diagonal | 0.057 | 0.086 | +50% |
| V(B2,B2) SU(2) component | 0.046 | 0.031 | -33% |
| V(B2,B2) C^2 component | 0.000 | 0.017 | new channel |
| V(B2,B2) U(1) component | 0.054 | 0.054 | stable |
| V(B1,B2) max | 0.080 | 0.077 | -4% |
| V(B3,B2) max | 0.027 | 0.022 | -17% |
| B2 overlap with bare | 1.000 | 0.935 | 6.5% mixing |
| V(B2,B2) diagonal max | 0.063 | 0.000 | self-coupling eliminated |

**Key Findings**:

1. **Pairing enhanced**: V(B2,B2) increases from 0.057 to 0.086 under inner fluctuations. The phi rotation opens a new C^2 channel (0 to 0.017) that more than compensates the SU(2) decrease. This was not predicted.

2. **Self-coupling vanishes**: When phi lifts the B2 degeneracy, the D_phys eigenbasis rotates such that V(B2_i,B2_i) = 0 exactly. All pairing strength is channeled into off-diagonal elements. This is favorable for BCS, where off-diagonal V drives Cooper pairing.

3. **Multi-tau stability**: V(B2,B2) at phi=gap increases monotonically from 0.081 (tau=0.10) to 0.091 (tau=0.30) across the fold region. The result is not tau-specific.

4. **B3 channel does NOT open**: V(B3,B2) decreases by 17% under phi, contradicting the W1 prediction. The B3 pairing channel weakens, not strengthens.

5. **Basis identity correction (CRITICAL)**: The V(B2,B2) = 0.287 from A_antisym and 0.057 from K_a_matrix are NOT different basis choices within the degenerate B2 subspace. They are fundamentally different mathematical objects. A_antisym_{i}_{a} stores $A^a_{rs} = \Gamma^s_{ra} - \Gamma^r_{sa}$, the Levi-Civita structure constants in FRAME INDEX space (r,s = tangent directions on SU(3)). K_a_matrix stores $\langle \psi_n | K_a | \psi_m \rangle$, the spinor matrix elements of the Kosmann operator $K_a = \frac{1}{8}\sum_{rs} A^a_{rs} \gamma_r \gamma_s$. The frame indices have no intrinsic branch labeling (B1/B2/B3). The TRAP-33b computation incorrectly treated frame indices as eigenspinor branch indices. See Section 4b for full analysis.

**Cross-check**: At phi=0, V(phi=0) reproduces the bare Kosmann kernel to 1.94e-16 (machine epsilon).

---

## 3. TRAP1-34a: Trap 1 Confirmation

### 3.1 What Was Computed

The Kosmann pairing kernel V_nm = sum_{a=0}^7 |<n|K_a|m>|^2 was evaluated at the gap-edge mode (B1, the U(2) singlet) using all 8 su(3) generators. This re-evaluates Trap 1 ("V(gap,gap) = 0 at exact gap edge") in light of the K-1e retraction, which showed that the C^2-generator-only kernel was incomplete.

### 3.2 Result

V(B1,B1) = 0.000 (exact zero, 0.00e+00) at all 9 tau values, all 8 generators.

This is not a near-zero result -- it is an exact zero arising from a representation-theoretic selection rule: B1 is the unique U(2) singlet in the positive sector, and the singlet has zero weight under every generator of su(3). The Kosmann Lie derivative K_a acts as zero on the singlet regardless of which generator a is chosen.

### 3.3 Distinction from K-1e

| Property | K-1e (RETRACTED) | Trap 1 (CONFIRMED) |
|:---------|:-----------------|:-------------------|
| Mode | B2 (doublet) | B1 (singlet) |
| C^2 generators | V = 0 (charge conservation) | V = 0 |
| Full kernel | V = 0.287 (nonzero) | V = 0 (exact) |
| Selection rule | C^2-specific (incomplete) | Full U(2) singlet (permanent) |
| Status | RETRACTED | CONFIRMED |

### 3.4 Impact

Trap 1 confirmation means the gap-edge divergence M ~ V/|xi| is regulated: V = 0 at the B1 mode where |xi| -> 0. The BCS mechanism operates in the B2 sector (spinor V(B2,B2) = 0.057; frame V = 0.287 is the wrong quantity). See Section 4b.

---

## 3b. RPA-34a: Spectral Action Curvature Under D_phys

### 3b.1 What Was Computed

The spectral action S(tau; phi) = sum_k |lambda_k(tau; phi)| was computed from D_phys eigenvalues at each (tau, phi_VEV) grid point. The second derivative d^2S/dtau^2 was extracted by central finite difference at the dump point (tau=0.20), using the same method as RPA-32b. The phi amplitude was swept from 0 to 0.17 in the worst-case H_j direction.

### 3b.2 Quantitative Results

| Quantity | Value |
|:---------|:------|
| d2S_abs (bare, phi=0) | 20.43 |
| d2S_abs (D_phys, phi=gap) | 180.09 |
| Ratio phi=gap / bare | 8.82x |
| Margin over threshold 0.54 | 333x |
| Bare margin | 38x |
| Minimum d2S across all phi | 20.43 (at phi=0) |

The curvature is **monotonically increasing** with |phi| at the dump point:

| |phi| | d2S_abs | ratio to bare |
|:------|:--------|:--------------|
| 0.00 | 20.43 | 1.00x |
| 0.05 | 44.00 | 2.15x |
| 0.10 | 112.66 | 5.51x |
| 0.133 (gap) | 180.09 | 8.82x |
| 0.17 | 273.64 | 13.39x |

### 3b.3 Physical Mechanism

Inner fluctuations create a **local dip** in S(tau) near the dump point that does not exist in the bare case. The bare S(tau) is monotonically increasing. Under phi=gap, S drops from 14.655 (tau=0.15) to 14.585 (tau=0.20) before rising to 14.966 (tau=0.25). This dip concentrates positive curvature at the dump point while creating negative curvature at flanking tau values:

| tau | d2S (bare) | d2S (phi=gap) |
|:----|:-----------|:--------------|
| 0.10 | 20.6 | -14.0 |
| 0.15 | 20.5 | -69.0 |
| 0.20 | 20.4 | +180.1 |
| 0.25 | 20.5 | -63.9 |
| 0.30 | 20.6 | +46.8 |

The concentration of curvature at the dump point is a consequence of the B2 fold: the fold creates a minimum in B2 eigenvalues near tau=0.20, which translates to a dip in S = sum|lambda| because the B2 branch contributes less to the sum at its minimum.

### 3b.4 Cross-Checks

Two cross-checks passed:
1. phi=0 reproduces bare d2S_abs to machine precision at all three evaluation tau values
2. phi=0 reproduces bare D_K eigenvalues exactly at all 9 tau values

### 3b.5 Gate Classification

**CONSISTENT**: d2S = 180.09 >> 0.54 at |phi| = gap. The spectral action curvature not only survives inner fluctuations but is enhanced by 8.8x. The W1 prediction "38x margin implausible to overturn" is confirmed -- the margin actually increases to 333x. The Turing link is NOT closed.

---

## 4. Constraint Map Update

### New Entries

| Constraint | Type | Session | Status |
|:-----------|:-----|:--------|:-------|
| DPHYS-34a-1 | Existential | 34a | **PASS** (d2=1.226 at phi=gap) |
| TRAP1-34a | Structural | 34a | **CONFIRMED** (V(B1,B1)=0 exact) |
| DPHYS-34a-2 | Existential | 34a | **PASS** (V(B2,B2)=0.086, 50% enhanced) |
| DPHYS-34a-3 | Existential | 34a | **FAIL** (M_max=0.899, all walls < 1) |
| RPA-34a | Diagnostic | 34a | **CONSISTENT** (d2S=180.09, 333x margin) |
| J correction | Foundational | 34a | C2 = gamma_1*gamma_3*gamma_5*gamma_7; no upstream impact |
| V matrix identity | Upstream | 34a | TRAP-33b used frame-space V (wrong); spinor V gives M_max=0.90 |

### Mechanism Chain (FINAL)

```
I-1 (instanton gas)          PASS       3.2-9.6x    Session 31Ba
RPA-32b (collective osc.)    PASS       38x         Session 32b
U-32a (domain formation)     PASS       D=16-3435   Session 32a
W-32b (flat-band trapping)   PASS       1.9-3.2x    Session 32b
TRAP-33b (BCS at walls)      RETRACTED  wrong V     Session 33b -> 34a
NUC-33b (nucleation)         FAIL*      swallowtail Session 33b
DPHYS-34a-1 (fold @ D_phys)  PASS       d2=1.226    Session 34a
DPHYS-34a-2 (Kosmann@D_phys) PASS       V=0.086     Session 34a
RPA-34a (curvature @ D_phys) CONSISTENT d2S=180     Session 34a
DPHYS-34a-3 (BCS @ D_phys)   FAIL       M_max=0.90  Session 34a
```

*NUC-33b FAIL restricts to swallowtail vertex. TRAP-33b RETRACTED due to V matrix misidentification (see Section 4b).

**CHAIN STATUS: BROKEN at BCS link.** The fold, kernel, and curvature all survive D_phys. But the absolute spinor pairing strength is insufficient for Thouless instability. M_max = 0.90, shortfall 1.11x.

### W1 Predictions Scorecard

| Prediction | Tested? | Result |
|:-----------|:--------|:-------|
| Destruction bound 0.42 < 1 | YES | CONFIRMED (fold stabilized, d2 increases) |
| B2 splits 2+2 (J-mandated) | YES | CONFIRMED (splitting 0.021 at phi=gap) |
| LDOS reduction 1.0-1.3x | N/A | BCS link closed; LDOS test moot |
| 38x margin implausible to overturn | YES | **CONFIRMED** (margin increases to 333x) |
| B3 channel opens | YES | NOT CONFIRMED (V(B3,B2) decreased 17%) |

---

## 4b. DPHYS-34a-3: Thouless Criterion Under D_phys (FAIL)

### 4b.1 What Was Computed

The Thouless criterion M_nm = V_nm(phi) * rho_m / (2|xi_m(phi)|) was computed in the D_phys eigenbasis at tau=0.20 using the worst-case H_j inner fluctuation direction. D_phys eigenvalues from s34a_dphys_fold.npz provide |xi_m(phi)|, the reprojected Kosmann kernel from s34a_dphys_kosmann.npz provides V_nm(phi), and wall DOS from s32b_wall_dos.npz provides rho_m. The phi amplitude was swept from 0 to 0.17 across all three wall configurations.

### 4b.2 Quantitative Results

| Wall | tau range | rho/mode | M_max(phi=0) | M_max(phi=gap) | Verdict |
|:-----|:----------|:---------|:-------------|:---------------|:--------|
| 0 | [0.10, 0.25] | 5.10 | 0.555 | 0.548 | FAIL |
| 1 | [0.10, 0.20] | 7.20 | 0.752 | 0.747 | FAIL |
| 2 | [0.15, 0.25] | 8.81 | 0.902 | 0.899 | FAIL |

M_max is essentially flat across the entire phi range (0 to 0.17). Inner fluctuations have negligible effect on the Thouless criterion: the ratio M_max(phi=gap)/M_max(phi=0) = 0.996.

### 4b.3 V Matrix Identity (Upstream Finding)

The TRAP-33b computation (Session 33b) reported M_max = 2.062 using V_nm = sum_a |A^a_{nm}|^2. This computation revealed that A_antisym and K_a_matrix are completely different mathematical objects:

| Object | Definition | Space | V(B2,B2) max | M_max(W2) |
|:-------|:-----------|:------|:-------------|:----------|
| A_antisym | $A^a_{rs} = \Gamma^s_{ra} - \Gamma^r_{sa}$ | Frame (tangent space) | 0.287 | 2.062 |
| K_a_matrix | $\langle \psi_n \| K_a \| \psi_m \rangle$ | Spinor (eigenspinors) | 0.057 | 0.902 |

The A_antisym tensor stores Levi-Civita connection structure constants in the frame index space (r,s = 0,...,7 = tangent directions on SU(3)). The K_a_matrix stores the spinor operator $K_a = \frac{1}{8}\sum_{rs} A^a_{rs} \gamma_r \gamma_s$ projected into the eigenspinor basis.

The s33b code mapped frame indices to eigenspinor branch labels (B3={0,1,2}, B2={3,4,5,6}, B1={7}) without physical justification. Frame indices {0,...,7} label tangent directions on SU(3), not spinor eigenvalues. The correct BCS pairing kernel uses spinor matrix elements.

**CONSEQUENCE**: TRAP-33b M_max = 2.062 was computed with the wrong V matrix. The correct spinor pairing gives M_max = 0.902 < 1.0. The Kosmann-BCS instability was never present in the correct spinor basis. TRAP-33b is RETRACTED.

### 4b.4 Cross-Checks

Three cross-checks confirm the computation:
1. A_antisym basis reproduces s33b M_max = 2.062 to 0.00% precision (confirming the discrepancy is a V matrix identity issue, not numerical error)
2. Spinor V at phi=0 matches s34a_dphys_kosmann baseline V(B2,B2) = 0.057
3. Wall DOS and enhancement factors identical to s33b

### 4b.5 Regulator Sensitivity

M_max(W2) = 0.8987 is completely insensitive to the regulator eta (tested from 0.0001 to 0.05). All eigenvalues are well-separated from mu=0; the regulator is never activated.

### 4b.6 Shortfall Analysis

The shortfall is 11%: M_max = 0.90 vs threshold 1.0. Possible rescue paths:

1. **Higher wall DOS**: Current rho_needed = 9.78 vs rho_available = 8.81 (11% gap). Non-singlet sector pairing (currently suppressed by cross-sector eigenvalue gap xi_cross = 0.236) could provide additional DOS if the suppression is relaxed.

2. **Finite-density spectral action (P2b)**: Nonzero chemical potential mu shifts eigenvalues closer to Fermi surface, potentially increasing M ~ V/(2|xi-mu|).

3. **Alternative pairing channels**: The spinor V has V(B1,B2) = 0.080, which enters the 5x5 Thouless matrix. If B1 spectral weight is enhanced (e.g., by non-singlet contributions), the cross-channel could push M_max above 1.

---

## 5. Assessment

All five pre-registered gates have been computed. The mechanism chain is BROKEN at the BCS link.

The fold structure (34a-1), Kosmann pairing kernel (34a-2), and spectral action curvature (RPA-34a) all survive D_phys inner fluctuations. The geometric infrastructure is sound. The failure is quantitative: the spinor pairing matrix elements V(B2,B2) = 0.057-0.087 are a factor of ~5x smaller than the frame-space structure constants V = 0.287 that were used in TRAP-33b. This factor traces to the gamma matrix algebra in $K_a = \frac{1}{8}\sum_{rs} A^a_{rs} \gamma_r \gamma_s$, which redistributes the pairing strength across the full 16-dimensional spinor space rather than concentrating it in the 8x8 positive sector.

The shortfall is 11%. This is not a qualitative failure (like the V_tree or Casimir mechanisms, which missed by orders of magnitude). It sits at the boundary of the constraint surface. Whether the BCS link can be rescued depends on whether the conservative assumptions in the DOS calculation (single-sector, mu=0, conservative impedance) can yield an additional 11% enhancement.

### Follow-Up Items

1. s28c axiom re-verification with C2 (non-blocking)
2. J operator independent cross-check (deferred)
3. TRAP-33b retraction assessment: downstream impact analysis
4. Shortfall rescue: test P2b (finite mu), non-singlet DOS boost, cross-channel enhancement

---

## 6. Files

| File | Agent | Content |
|:-----|:------|:--------|
| `tier0-computation/s34a_dphys_fold.{py,npz,png}` | bap | D_phys construction, fold survival, eigenvalue flow |
| `tier0-computation/s34a_trap1_reeval.{py,npz,png}` | connes | Trap 1 re-evaluation, full kernel V(B1,B1) |
| `tier0-computation/s34a_dphys_kosmann.{py,npz,png}` | bap | Kosmann kernel reprojection into D_phys eigenbasis |
| `tier0-computation/s34a_rpa_curvature.{py,npz,png}` | bap | Spectral action curvature under D_phys (RPA-34a) |
| `tier0-computation/s34a_dphys_thouless.{py,npz,png}` | bap | Thouless criterion under D_phys (DPHYS-34a-3 FAIL) |
| `tier0-computation/s34a_gate_verdicts.txt` | coord | Gate classifications (ALL 5 COMPUTED) |
| `sessions/session-34/session-34a-synthesis.md` | coord | This document |
