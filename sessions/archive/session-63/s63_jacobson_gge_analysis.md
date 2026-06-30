# JACOBSON-GGE-63: Formal Jacobson Derivation for Non-Thermal (GGE) Matter

**Gate**: JACOBSON-GGE-63
**Verdict**: INFO — Derivation EXTENDS to GGE matter without modification
**Agent**: einstein-theorist
**Session**: S63, Wave 3, W3-03
**Date**: 2026-03-30

---

## 1. Executive Summary

The Jacobson (1995) derivation of the Einstein equations from $\delta Q = T \, dS$ applied to local Rindler horizons **extends without modification** to matter in a Generalized Gibbs Ensemble (GGE) with non-Planckian occupation numbers locked by Richardson-Gaudin integrability. All seven steps of the derivation pass. The cosmological constant $\Lambda$ emerges as an undetermined integration constant, exactly as in the thermal case.

**Key correction to S62**: The Hawking-QA workshop (S62, Re:H6) concluded that $S_{\text{ent}} = 0$ for the GGE product state implies $\Lambda = 0$ via the Jacobson route. This is **incorrect**. Jacobson's derivation uses the **vacuum entanglement entropy** $S_{\text{vac}} = \eta \cdot A$ (entanglement of the BCS vacuum across the Rindler horizon), not the matter-state entropy $S_{\text{matter}}$ (which is indeed zero for the GGE product state). The vacuum entanglement entropy is always nonzero and proportional to the horizon area, regardless of the matter excitations above the vacuum. The CC problem persists at $\sim 114$ OOM.

**Comparison to Volovik**: Volovik's theorem ($\Lambda_{\text{eq}} = 0$ at thermodynamic equilibrium) does **not** apply to the GGE because the GGE is in constrained equilibrium (R-G charges prevent full thermalization to the Gibbs state). The GGE has $\Lambda \neq 0$.

---

## 2. The Jacobson Derivation: Seven Steps

### Step 1: Local Rindler Horizon Construction

**Status**: PASSES

At every spacetime point $p$, one constructs a local Rindler horizon from a spacelike 2-surface $\mathcal{P}$ whose past-directed null normal congruence has vanishing expansion and shear at $p$. This construction is **purely geometric** — it depends only on the spacetime metric $g_{ab}$, not on the matter content. The GGE state does not affect the existence or properties of local Rindler horizons.

### Step 2: Unruh Temperature

**Status**: PASSES

The Unruh temperature $T_U = \hbar \kappa / (2\pi)$ is a **kinematic** quantity determined by the observer's acceleration $a$ (or equivalently, the surface gravity $\kappa$ of the Rindler horizon). It does not depend on the nature of the matter fields or their state. An accelerated observer perceives $T_U$ regardless of whether the matter is in a Planck distribution, a GGE state, or any other state.

### Step 3: Heat Flux $\delta Q$

**Status**: PASSES

The heat flux across the Rindler horizon is:

$$\delta Q = -\kappa \int_{\mathcal{H}} \lambda \, T_{ab}^{\text{GGE}} k^a k^b \, d\lambda \, d\mathcal{A} \tag{1}$$

The energy-momentum tensor $T_{ab}^{\text{GGE}} = \langle \text{GGE} | \hat{T}_{ab} | \text{GGE} \rangle$ is well-defined for any quantum state. The GGE state

$$\rho_{\text{GGE}} = \frac{1}{Z_{\text{GGE}}} \exp\left(-\sum_k \beta_k I_k\right) \tag{2}$$

has a definite $T_{ab}$ that differs from the thermal $T_{ab}$ but satisfies energy-momentum conservation $\nabla^a T_{ab}^{\text{GGE}} = 0$ because $[H, I_k] = 0$ for all R-G charges $I_k$.

**Computed values** (from `s62_meissner_gge.npz` and `s62_cc_qtheory_gge.npz`):
- $T_{00}^{\text{GGE}} = 81{,}493.88 \, M_{\text{KK}}^4$ (total: ZP + BCS)
- $\rho_{\text{modes}} = 0.8198 \, M_{\text{KK}}^4$ (BCS quasiparticle contribution)
- Mode-by-mode deviations from Planck: up to $7{,}381\times$ for mode $k = 5$

### Step 4: Area Variation (Raychaudhuri Equation)

**Status**: PASSES

The Raychaudhuri equation

$$\frac{d\theta}{d\lambda} = -\frac{1}{2}\theta^2 - \sigma^2 - R_{ab} k^a k^b \tag{3}$$

is a **purely geometric identity** relating the expansion $\theta$ of null geodesics to the Ricci tensor. At the local equilibrium point ($\theta = \sigma = 0$), the area variation is:

$$\delta\mathcal{A} = -\int_{\mathcal{H}} \lambda \, R_{ab} k^a k^b \, d\lambda \, d\mathcal{A} \tag{4}$$

No assumption about the matter content or its thermal properties enters this step.

### Step 5: Entropy-Area Proportionality $dS = \eta \, \delta\mathcal{A}$

**Status**: PASSES (with clarifying subtlety)

This is the **critical step** where the S62 analysis went wrong. There are two distinct entropy concepts:

| Entropy | Definition | GGE value | Jacobson uses? |
|:--------|:-----------|:----------|:---------------|
| $S_{\text{matter}}$ | Von Neumann entropy of matter state | $= 0$ (GGE is product state in R-G eigenbasis) | **NO** |
| $S_{\text{vac}}$ | Entanglement entropy of vacuum across Rindler cut | $= \eta \cdot A$ (always nonzero) | **YES** |

Jacobson uses the **vacuum entanglement entropy**, not the matter entropy. The Bombelli-Koul-Lee-Sorkin (1986) / Srednicki (1993) result establishes that the entanglement entropy of the quantum vacuum across any spatial surface scales as:

$$S_{\text{vac}} = c_{\text{UV}} \frac{A}{\epsilon^2} + \text{subleading} \tag{5}$$

where $\epsilon$ is the UV cutoff. The BCS vacuum $|0_{\text{BCS}}\rangle$ has UV entanglement from the continuum, independent of the GGE excitations above it. The GGE modifications are perturbative corrections:

$$\frac{\delta S_{\text{GGE}}}{S_{\text{vac}}} \sim \sum_{k > 0} n_k^{\text{GGE}} \omega_k^2 \sim 7.8 \times 10^{-3} \tag{6}$$

This is a $< 1\%$ correction. The proportionality $S = \eta \cdot A$ holds to leading order.

**The S62 error**: The Hawking-QA workshop stated that $S_{\text{ent}} = 0$ for the GGE and concluded $\Lambda = 0$. They conflated $S_{\text{matter}} = 0$ (correct for the GGE product state) with $S_{\text{vac}} = 0$ (incorrect — the vacuum always has entanglement). Jacobson's derivation uses the vacuum entanglement, which is nonzero and proportional to the horizon area.

### Step 6: Clausius Relation $\delta Q = T_U \, dS$

**Status**: PASSES

Combining Steps 3 and 5:

$$-\kappa \int \lambda \, T_{ab}^{\text{GGE}} k^a k^b \, d\lambda \, d\mathcal{A} = \frac{\hbar\kappa}{2\pi} \eta \left(-\int \lambda \, R_{ab} k^a k^b \, d\lambda \, d\mathcal{A}\right) \tag{7}$$

The $\kappa$ cancels (as in the thermal case), yielding:

$$T_{ab}^{\text{GGE}} k^a k^b = \frac{\hbar\eta}{2\pi} R_{ab} k^a k^b \quad \forall \, \text{null} \, k^a \tag{8}$$

This is the same equation as in the thermal case, with $T_{ab}^{\text{GGE}}$ on the left instead of $T_{ab}^{\text{thermal}}$.

### Step 7: Einstein Equations via Bianchi Identity

**Status**: PASSES

Equation (8) holding for all null $k^a$ implies:

$$T_{ab}^{\text{GGE}} = \frac{\hbar\eta}{2\pi} (R_{ab} + f g_{ab}) \tag{9}$$

for some scalar function $f$. Energy-momentum conservation $\nabla^a T_{ab}^{\text{GGE}} = 0$ combined with the contracted Bianchi identity $\nabla^a G_{ab} = 0$ fixes $f = -R/2 + \Lambda$:

$$R_{ab} - \frac{1}{2}R g_{ab} + \Lambda g_{ab} = \frac{2\pi}{\hbar\eta} T_{ab}^{\text{GGE}} = 8\pi G \, T_{ab}^{\text{GGE}} \tag{10}$$

with $G = (4\hbar\eta)^{-1}$ and $\Lambda$ an **undetermined integration constant**.

---

## 3. Three Perspectives on $\Lambda$

### 3.1 Jacobson Perspective: $\Lambda$ = Integration Constant

The Jacobson derivation recovers the Einstein equations with $\Lambda$ undetermined. This is explicitly noted by Jacobson (1995). The derivation shows that the **form** of the Einstein equations follows from thermodynamics, but the **value** of $\Lambda$ requires additional input.

For the GGE, the derivation gives the same formal result as for thermal matter. The only difference is the specific form of $T_{ab}$ on the RHS. The CC problem is **reformulated** (what determines $\Lambda$?) but not **solved**.

### 3.2 Volovik Perspective: $\Lambda_{\text{eq}} = 0$ in Equilibrium

Volovik's thermodynamic argument: at $T = 0$ thermodynamic equilibrium, the Gibbs-Duhem relation implies that the pressure of the vacuum vanishes, $P_{\text{vac}} = -\rho_{\text{vac}} = 0$, hence $\Lambda_{\text{eq}} = 0$.

This does **NOT** apply to the GGE because:
1. The GGE is **not** in Gibbs equilibrium. It is in constrained equilibrium with R-G charges as constraints.
2. The GGE density matrix $\rho_{\text{GGE}} = Z^{-1}\exp(-\sum_k \beta_k I_k)$ maximizes entropy subject to the R-G constraints, not subject to energy alone.
3. The constrained pressure $P_{\text{GGE}} = -\partial F_{\text{GGE}}/\partial V |_{\{\beta_k\}}$ does not necessarily vanish.

**Computed**: $P_{\text{GGE}}(\text{constrained}) = -0.838 \, M_{\text{KK}}^4 \neq 0$.

The Volovik result is a theorem about **unconstrained** equilibrium. The GGE has R-G integrability constraints that prevent the system from reaching unconstrained equilibrium. The residual $\Lambda$ from the GGE constrained equilibrium is $\neq 0$.

### 3.3 Entanglement Perspective: $S_{\text{vac}} \neq 0$

The S62 Hawking-QA workshop argued:
- GGE is a product state in R-G eigenbasis
- Product states have zero entanglement entropy
- Therefore $dS = 0$ in Jacobson's derivation
- Therefore $\Lambda = 0$

This argument confuses two different entropies (see Step 5 above). The vacuum entanglement entropy $S_{\text{vac}}$ is nonzero and proportional to the horizon area for any vacuum state with UV correlations. The GGE state modifies this by $< 1\%$.

However, the S62 analysis raises an important question: **what if the LOCAL entanglement entropy of the GGE across a Rindler cut on the CG(24) fabric is genuinely zero or anomalously small?** This is the subject of LOCAL-ENTANGLE-63 (W3-01), which computes $S_{\text{ent}}(\text{local})$ directly. If $S_{\text{ent}}(\text{local}) \ll \eta \cdot A$, the Jacobson derivation would still hold (it applies to the continuum vacuum, not the lattice), but the **effective** $\Lambda$ seen by the lattice modes could be suppressed.

---

## 4. Effective $\Lambda$ from GGE

### 4.1 Five Options

| Option | $\Lambda_{\text{eff}}$ (GeV$^4$) | CC Gap (OOM) | Status |
|:-------|:--------------------------------|:-------------|:-------|
| A. Naive ($E_{\text{ZP}}$ gravitates) | $2.48 \times 10^{72}$ | 119.0 | Standard CC problem |
| B. Spectral action ($a_0 M_{\text{KK}}^4$) | $3.97 \times 10^{70}$ | 117.2 | SA route |
| C. BCS condensation only | $4.17 \times 10^{66}$ | 113.2 | Minimum gravitating energy |
| D. Volovik ($\Lambda_{\text{eq}} = 0$) | 0 | $-\infty$ | Does NOT apply to GGE |
| E. BCS + EIH suppression | $5.71 \times 10^{57}$ | 104.3 | With $(M_{\text{KK}}/M_{\text{Pl}})^4$ |

### 4.2 GGE Equation of State

The GGE matter decomposes into two components:

$$\rho_{\text{GGE}} = \rho_{\text{cond}} + \rho_{\text{qp}}$$

| Component | $\rho$ ($M_{\text{KK}}^4$) | $w$ |
|:----------|:---------------------------|:----|
| BCS condensate | 0.137 | $-1$ (vacuum energy) |
| Quasiparticles | 0.820 | $+1/3$ (relativistic) |
| **Total** | **0.957** | **$w_{\text{GGE}} = 0.143$** |

The composite equation of state $w_{\text{GGE}} = 0.143$ is matter-like, not dark-energy-like. The condensate contributes a $w = -1$ component but is subdominant to the quasiparticle excitations. For the GGE matter to serve as dark energy, the condensate fraction must dominate over the quasiparticle fraction.

---

## 5. What the GGE Structure Buys for the CC

### 5.1 What IS Resolved

1. **The form of the equations**: The Einstein equations hold with $T_{ab}^{\text{GGE}}$. General covariance is satisfied. The EIH program (S44) applies.

2. **Newton's constant**: $G = (4\hbar\eta)^{-1}$ is determined by the vacuum entanglement density $\eta$. The BCS vacuum modifies $\eta$ at the $O(1)$ level ($\delta\eta/\eta \sim \Delta_{\text{BCS}}^2 \sim 1.6$), consistent with the SAKHAROV-GN-44 result (factor 2.3 agreement).

3. **EIH suppression**: The $(M_{\text{KK}}/M_{\text{Pl}})^4 = 1.37 \times 10^{-9}$ suppression from the EIH projection is preserved in the Jacobson framework.

### 5.2 What Is NOT Resolved

1. **The CC magnitude**: The gap between $\rho_{\text{GGE}}$ and $\rho_{\Lambda}^{\text{obs}}$ is $\sim 114$ OOM (Options C-E above). The Jacobson derivation does not fix $\Lambda$.

2. **The CC problem reformulation**: The Jacobson framework shifts the CC problem from "why is $\Lambda$ small?" to "what determines $\Lambda$?". For the phonon-exflation framework, the answer must come from outside the Jacobson derivation — either from the spectral action (which is the entropy functional), from q-theory (variational principle on $\Lambda$), or from a nonlocal mechanism (Capozziello Paper 09).

3. **The Volovik equilibrium**: The GGE prevents the Volovik $\Lambda_{\text{eq}} = 0$ mechanism from operating. The R-G integrability locks the vacuum energy at a finite value. Breaking integrability (8 closures, S56-S62) remains the only identified route to $\Lambda \rightarrow 0$.

---

## 6. Structural Implications

### 6.1 The Jacobson-GGE Theorem (Permanent)

**THEOREM**: The Jacobson (1995) derivation of the Einstein equations from $\delta Q = T \, dS$ extends without modification to GGE matter with non-Planckian occupations locked by Richardson-Gaudin integrability. All seven steps of the derivation pass. The result is the standard Einstein equations $G_{ab} + \Lambda g_{ab} = 8\pi G \, T_{ab}^{\text{GGE}}$ with $\Lambda$ as an undetermined integration constant and $G = (4\hbar\eta)^{-1}$.

**Proof**: See Steps 1-7 above. The key insight is that Jacobson's derivation requires only: (a) a well-defined $T_{ab}$ (any quantum state has one), (b) vacuum entanglement entropy proportional to area (independent of matter excitations to leading order), (c) the kinematic Unruh temperature (independent of matter state), and (d) energy-momentum conservation (guaranteed by $[H, I_k] = 0$). None of these requirements involve thermal equilibrium of the matter fields.

### 6.2 The S62 Error (Correction)

The S62 Hawking-QA workshop conclusion ("$S_{\text{ent}} = 0$ for GGE $\Rightarrow \Lambda = 0$") conflated matter-state entropy (zero for GGE product state) with vacuum entanglement entropy (nonzero, proportional to area). Jacobson uses the latter, not the former. The Jacobson route does NOT give $\Lambda = 0$ for GGE matter.

### 6.3 Constraint Map Update

| Entity | Type | Old State | New State | Evidence |
|:-------|:-----|:----------|:----------|:---------|
| Jacobson-GGE extension | THEOREM | Uncomputed | EXTENDS (permanent) | 7/7 steps pass |
| S62 "Lambda=0 via Jacobson" | CLAIM | Accepted | CORRECTED | Entropy conflation |
| Volovik Lambda_eq=0 for GGE | THEOREM | Uncertain | DOES NOT APPLY | GGE ≠ Gibbs |
| CC gap (Jacobson route) | GATE | Open | 114 OOM (unchanged) | Computed |

---

## 7. Cross-Checks

1. **Dimensional consistency**: All equations checked. $\eta$ has dimensions $[\text{length}]^{-2}$, $G = (4\hbar\eta)^{-1}$ has correct dimensions.

2. **Limiting cases**: For $n_k^{\text{GGE}} \to n_k^{\text{Planck}}$, the derivation reduces to the standard Jacobson result. For $n_k^{\text{GGE}} \to 0$ (vacuum), $T_{ab} \to T_{ab}^{\text{vac}}$ and the derivation gives vacuum Einstein equations $G_{ab} + \Lambda g_{ab} = 0$.

3. **General covariance**: The result $G_{ab} + \Lambda g_{ab} = 8\pi G T_{ab}^{\text{GGE}}$ is manifestly generally covariant. Both sides are symmetric, divergence-free rank-2 tensors.

4. **Consistency with S44**: The EIH suppression $(M_{\text{KK}}/M_{\text{Pl}})^4 = 1.37 \times 10^{-9}$ and the Sakharov $G_N$ (factor 2.3) are consistent with the Jacobson framework.

---

## 8. Data Files

| File | Description |
|:-----|:------------|
| `computations/s63_jacobson_gge.py` | Computation script |
| `computations/s63_jacobson_gge.npz` | Output data (gate verdict, all computed quantities) |
| `sessions/archive/session-63/s63_jacobson_gge_analysis.md` | This document |

**Input data**:
| File | Used for |
|:-----|:---------|
| `computations/s62_meissner_gge.npz` | GGE occupations, condensate fraction |
| `computations/s62_cc_qtheory_gge.npz` | ZP energy, BCS energy, CC gap |

---

## 9. Gate Verdict

**Gate**: JACOBSON-GGE-63
**Verdict**: INFO
**Detail**: Jacobson derivation EXTENDS to GGE matter without modification. All 7 steps pass. $\Lambda$ remains undetermined integration constant. S62 claim ($S_{\text{ent}} = 0 \Rightarrow \Lambda = 0$) CORRECTED: Jacobson uses vacuum entanglement (nonzero), not matter-state entropy (zero for GGE). Volovik $\Lambda_{\text{eq}} = 0$ does NOT apply (GGE is constrained, not Gibbs). CC gap persists at $\sim 114$ OOM. $w_{\text{GGE}} = 0.143$ (dynamical, not pure CC). Jacobson reformulates CC problem but does not solve it.
