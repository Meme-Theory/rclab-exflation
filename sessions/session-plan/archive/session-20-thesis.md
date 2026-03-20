# Session 20: Twenty-Seven Drums — The Lichnerowicz Operator on TT 2-Tensors

## Session Type: New Code + Decisive Computation (2-3 DAYS)
## Agents: phonon-exflation-sim + kaluza-klein-theorist + connes-ncg-theorist
## Session Goal: Compute the Lichnerowicz eigenvalue spectrum on symmetric traceless-transverse (TT) 2-tensors on (SU(3), g_Jensen(tau)). Determine whether the full bosonic Casimir energy (with TT modes) creates a minimum in V_total(tau) where V_tree + V_CW alone does not. ONE decisive computation from the single most important finding in Session 19d.

---

# I. WHERE WE ARE: THE STATE OF THE FRAMEWORK

## Twenty Sessions. One Remaining Route.

Sessions 1 through 19d have established:

**PROVEN (machine epsilon or exact theorem):**
- KO-dimension = 6. Parameter-free. (Sessions 7-8)
- SM quantum numbers from Psi_+ = C^16. (Session 7)
- [J, D_K(tau)] = 0 identically. CPT hardwired. (Session 17a D-1)
- 79,968 eigenvalue pairs with max error 3.29e-13. (Session 17a D-3)
- 67 Baptista geometry checks at machine epsilon. Zero failures. (Session 17b)
- g_1/g_2 = e^{-2tau} derived from eq 3.71. (Session 17a B-1)
- Volume-preserving TT-deformation: det(g_tau)/det(g_0) = 1.000000000. (Session 12)
- Diagonal metric in Gell-Mann basis. (Session 17a SP-1)
- Pfaffian Z_2 = +1 for all tau in [0, 2.5]. Topologically trivial. (Session 17c D-2)
- AZ class BDI, T^2 = +1. (Session 17c D-4)
- 4 curvature invariants as exact analytic functions of tau. u(1) Ricci = 1/4 for all tau. (Session 17b SP-2)
- phi_paasch: m_{(3,0)}/m_{(0,0)} = 1.531580 at tau=0.15 (0.0005% from phi_P = 1.53158). (Session 12)
- sin^2(theta_W) constraint: tau_0 = 0.2994 from g_1/g_2 = e^{-2tau}. (Session 17a B-1)

**CLOSED (definitively ruled out):**
- V_tree minimum: Monotonically decreasing, 3rd-order inflection at tau=0, V'''(0) = -7.2. (Session 17a SP-4)
- 1-loop Coleman-Weinberg minimum: Monotonically decreasing for ALL tau > 0 at ALL truncation orders. F/B = 8.4:1 fermion dominance. Convergent to 0.55% between mps=5 and mps=6. (Session 18)
- Casimir energy (scalar + vector): F/B = 9.92:1, constant to 1.83%. Same monotonicity as V_CW. (Session 19d D-1)
- Spectral back-reaction (scalar + vector): Same sign as V_CW. (Session 19d)
- Fermion condensate: Spectral gap > 0.818 everywhere. (Session 17c H-3)
- D_K Pfaffian topological transition: Z_2 = +1 throughout. (Session 17c D-2)
- Single-field tau slow-roll: epsilon ~ 2.1 >> 1. (Session 19b R-1)

**OPEN (tested but ambiguous or not yet computed):**
- Rolling modulus (quintessence): Status from Session 19b TBD; independent of TT 2-tensor computation.
- Spectral complexity (Anderson transition): Structural null — requires full off-diagonal D_K (Kosmann-Lichnerowicz coupling), not available from block-diagonal Peter-Weyl data.
- D_total Pfaffian: Queued (Session 20+); requires eigenvectors from Session 19c E-1.
- Instanton corrections: Deferred (weeks of work, non-perturbative).
- Lattice SU(3): Deferred (months).

**THE CRITICAL DISCOVERY FROM SESSION 19D:**

> *"ALL computations from Sessions 18 and 19d omit the Lichnerowicz operator on symmetric traceless-transverse (TT) 2-tensors — the graviton-like KK modes from metric fluctuations. These contribute 741,636 bosonic DOF at max_pq=6. With TT modes, F/B flips from 8.36:1 (fermion-dominated) to 0.44:1 (boson-dominated)."* — Session 19d, Section VII-B

This is not a small correction. It inverts the entire DOF balance. It reopens Casimir stabilization from a definitively closed route to the most important uncomputed quantity in the framework.

---

# II. THE PHYSICS: WHY TT 2-TENSORS ARE DECISIVE

## II-A. The DOF Count Is Exact Representation Theory

The symmetric traceless-transverse 2-tensor fiber dimension is 27. This is not an estimate.

**Derivation:**

On an 8-dimensional manifold K = SU(3), the cotangent bundle T*K has fiber R^8. The symmetric 2-tensor bundle Sym^2(T*K) has fiber dimension 8 * 9 / 2 = 36. Decompose:

```
h_{ab} = h^TT_{ab} + nabla_{(a} V_{b)} + (1/8) g_{ab} h

where:
  h   = g^{ab} h_{ab}              (trace: 1 DOF, scalar)
  V_b = divergence component       (longitudinal: 8 DOF, gauge/vector)
  h^TT_{ab}                        (transverse-traceless: 36 - 1 - 8 = 27 DOF)
```

Under the adjoint action of SU(3):

```
Sym^2(8) = 1 + 8 + 27

where:
  1  = trivial (trace)               -> already counted in scalar Laplacian
  8  = adjoint (divergence/gauge)    -> already counted in vector tower
  27 = (2,2) irrep of SU(3), dim(2,2) = 27  -> ENTIRELY NEW
```

The (2,2) irrep has dim(2,2) = (2+1)(2+1)(2+2+2)/2 = 27. This is exact.

**Corrected DOF table:**

| Species | Fiber dim | DOF at mps=6 | Operator |
|:--------|:----------|:-------------|:---------|
| Scalar Laplacian | 1 | 27,468 | -nabla^2 |
| Vector Hodge | 8 | 219,744 | d*d + dd* |
| TT 2-tensor (Lichnerowicz) | 27 | **741,636** | Delta_L |
| Dirac (spinor) | 16 | 439,488 | D_K |
| **Total bosonic** | **36** | **988,848** | |
| **Total fermionic** | **16** | **439,488** | |
| **F/B ratio** | | **0.44:1** | |

The asymptotic fiber ratio is 36:16 = 9:4 — a geometric invariant of an 8-manifold, independent of the specific group or metric.

**Independent verification:** Tesla (Session 19d), Feynman, Dirac, KK-theorist, Baptista, Hawking, and 8 additional reviewers all confirmed this counting in the 14-agent Session 19d collaborative review. The representation theory is airtight.

## II-B. The Lichnerowicz Operator Is Qualitatively Different

The Lichnerowicz operator on TT 2-tensors is:

```
Delta_L h_{ab} = -nabla^2 h_{ab} - 2 R_{acbd} h^{cd} + 2 R_{(a}^c h_{b)c}
```

The FULL Riemann tensor R_{acbd}(tau) enters — not just the scalar curvature R_K(tau) (which appears in the Dirac operator through D^2 = nabla^2 + R_K/4). This is qualitatively different.

**Why this matters:**

| Operator | Curvature coupling | tau-dependence |
|:---------|:-------------------|:---------------|
| Scalar Laplacian Delta_0 | None (just -nabla^2) | Tracks metric components: e^{2tau}, e^{tau}, e^{-2tau} |
| Dirac operator D_K | R_K/4 (scalar curvature) | Same as scalar + fixed fraction of R_K(tau) |
| Lichnerowicz Delta_L | Full R_{acbd} (Riemann tensor) | **New tau-dependence via curvature products** |

The Riemann tensor on Jensen-deformed SU(3) has anisotropic components:
- u(1) sector sectional curvatures: scale as e^{4tau}
- su(2) sector sectional curvatures: scale as e^{-4tau}
- C^2 sector sectional curvatures: mixed
- Cross-sector terms: involve structure constants

**Consequence (Hawking, Session 19d):** The TT eigenvalues have DIFFERENT tau-dependence from scalar eigenvalues. For the scalar+vector tower, R(tau) = |E_fermion|/E_boson varied by only 1.83% across [0, 2.0] — because both bosonic and fermionic towers saw the same metric exponentials. The TT Lichnerowicz operator introduces PRODUCTS of metric exponentials (through R_{acbd} ~ g * partial^2 g + (partial g)^2) that break this parallel flow.

**The physical picture (Tesla + Hawking, Session 19d):**

- **Scalar modes**: Breathing oscillations. Bulk cavity modes.
- **Vector modes**: Sloshing oscillations. Boundary displacement modes.
- **TT 2-tensor modes**: SHAPE OSCILLATIONS. The cavity walls themselves.

In any physical cavity — electromagnetic, acoustic, superfluid — the Casimir energy is dominated by the boundary/shape modes. The Schumann resonances (7.83 Hz) are shape modes of the Earth-ionosphere cavity, not bulk air compression. We computed the air compression while ignoring the spherical shell. The 27 drums were silent.

## II-C. Multiple Physical Interpretations Converge

The 14-agent Session 19d collaborative review found the same computation decisive from every angle:

| Perspective | TT 2-tensors are... | Stabilization mechanism |
|:-----------|:--------------------|:-----------------------|
| Einstein | Linearized graviton modes on K | Internal gravity balancing matter (T_uv without G_uv was the error) |
| Feynman | Massive spin-2 KK graviton gas | Path integral minimum |
| Hawking | Shape oscillations of internal cavity | Casimir pressure of cavity walls |
| Landau | Elastic DOF of internal geometry | Phase transition with cubic term V'''(0) = -7.2 |
| Tesla | Cavity wall resonance modes | Impedance matching condition |
| Connes | Outer automorphisms of spectral triple | Spectral action minimum from a_2/a_4 competition |
| KK-theorist | Graviton KK tower from h_{ab} | Freund-Rubin-like balance |
| Baptista | Shape phonons (TT component) | V_eff minimum from eq 3.87 with complete mode content |
| Dirac | J-neutral bosons (J doesn't act on Sym^2_0) | DOF flip without J-violation |

**Fourteen voices. One geometry. Twenty-seven drums.**

---

# III. THE COMPUTATION: LICHNEROWICZ EIGENVALUES ON TT 2-TENSORS

## The Formula

The Lichnerowicz operator on TT 2-tensors on (SU(3), g_Jensen(tau)) in the orthonormal left-invariant frame {e_a}:

```
(Delta_L h)_{ab} = -nabla^2 h_{ab} - 2 R_{acbd} h^{cd} + 2 Ric_{(a}^c h_{b)c}
```

On a Lie group with left-invariant metric, the connection and curvature tensor are computed from the structure constants f_{ab}^c and metric g_{ab}(tau):

**Riemann tensor (Milnor 1976, also Baptista Paper 15 eqs 3.14-3.19):**

```
R_{abcd} = (1/4)(g_{ae} f_{bc}^e)(g_{df} f_{bc}^f) - ... [standard formula in terms of structure constants and metric]
```

The bi-invariant result (tau=0):

```
R_{abcd}|_{tau=0} = -(1/4) f_{abe} f^e_{cd}     [structure constant formula]
```

Under Jensen deformation, R_{abcd}(tau) acquires anisotropic corrections from the metric components e^{2tau}, e^{-2tau}, e^{tau}. The Ricci tensor components are already known analytically (Baptista eq 3.66):

```
Ric|_{u(1)} = (3*lambda_1)/(2*lambda_2*lambda_3) * g|_{u(1)}
Ric|_{su(2)} = (1/lambda_2 + lambda_2/(2*lambda_3^2)) * g|_{su(2)}
Ric|_{C^2}  = (3*lambda_3/4 - (lambda_1+lambda_2)/(2*lambda_3)) * g|_{C^2}

where lambda_1 = e^{2tau}, lambda_2 = e^{-2tau}, lambda_3 = e^{tau}
```

The FULL Riemann tensor R_{abcd}(tau) is needed for the Lichnerowicz coupling, not just the Ricci contraction.

## Peter-Weyl Decomposition for TT 2-Tensors

The left-regular representation on L^2(SU(3), Sym^2_{TT}(T*K)) decomposes as:

```
bigoplus_{(p,q)} rho_{(p,q)} tensor Sym^2_{TT}(su(3)^*)
```

At each sector (p,q), the Lichnerowicz operator acts on a space of dimension dim(p,q) * d_TT where d_TT = 27 (at tau=0) or effectively 35 with on-the-fly TT projection at tau != 0.

**Matrix sizes:**

| Sector (p,q) | dim(p,q) | Matrix size (dim * 35) |
|:-------------|:---------|:----------------------|
| (0,0) | 1 | 35 x 35 |
| (1,0), (0,1) | 3 | 105 x 105 |
| (1,1) | 8 | 280 x 280 |
| (2,0), (0,2) | 6 | 210 x 210 |
| (3,0), (0,3) | 10 | 350 x 350 |
| (2,1), (1,2) | 15 | 525 x 525 |
| (3,1), (1,3) | 24 | 840 x 840 |
| (2,2) | 27 | 945 x 945 |
| (4,0), (0,4) | 15 | 525 x 525 |
| (6,0), (0,6) | 28 | 980 x 980 |
| (3,3) | 64 | 2240 x 2240 |

All tractable on 32-core Ryzen with 17GB VRAM. Largest matrix: (3,3) at 2240 x 2240 — trivial for GPU eigenvalue solver.

**Estimated runtime per tau-value:** ~4 minutes at mps=6 (KK-theorist, Session 19d).
**Full sweep (21 tau-values):** ~84 minutes. Feasible in a single session.

## What Already Exists

The following infrastructure is already implemented in `tier0-computation/`:

| Component | File | What It Provides |
|:----------|:-----|:----------------|
| Jensen metric g_{ab}(tau) | `tier1_dirac_spectrum.py` | `jensen_metric()` at any tau |
| Connection coefficients Gamma^c_{ab}(tau) | `b6_scalar_vector_laplacian.py` | `compute_connection_ON()` |
| Ricci tensor Ric_{ab}(tau) | `b6_scalar_vector_laplacian.py` | `ricci_tensor_ON()` |
| Peter-Weyl irrep matrices | `tier1_dirac_spectrum.py` | `get_irrep_matrices()` |
| Scalar Laplacian eigenvalues | `b6_scalar_vector_laplacian.py` | Reference for cross-checking |
| V_CW data | `h5_standalone_verify.py` | 26-point V_eff(tau) at multiple mu |
| V_tree analytic | `tier1_spectral_action.py` | `baptista_V_tree()` |
| Casimir proxy machinery | `d19d_casimir_gate.py` | E_proxy boson/fermion separation |

**What is NEW and must be written:**

1. **Full Riemann tensor R_{abcd}(tau)**: Extend `ricci_tensor_ON()` to store all four indices. The formula from structure constants is known. This is the critical new ingredient. (~80 lines)

2. **Lichnerowicz matrix assembly in Peter-Weyl sector (p,q)**: Given R_{abcd}(tau) and the Sym^2_{TT} fiber structure, assemble the (dim(p,q) * 35) x (dim(p,q) * 35) Lichnerowicz matrix with on-the-fly TT projection. (~200 lines)

3. **TT eigenvalue sweep**: Sweep tau in [0, 2.0] at 21 values. For each tau, compute Lichnerowicz eigenvalues in all 28 sectors. Record eigenvalues and multiplicities. (~100 lines)

4. **Total Casimir assembly**: Combine scalar + vector (from `d19d_casimir_gate.py`) + TT 2-tensor (new) + fermionic (from `s19a_sweep_data.npz`). Compute R(tau) = |E_fermion| / E_boson for full spectrum. Check for sign flip and monotonicity change. (~80 lines)

5. **V_total minimum search**: V_total = V_tree + V_CW + E_Casimir_total. Find sign change in dV_total/dtau. (~50 lines)

**Total new code:** ~510 lines. Estimate 2-3 days including validation.

## The Seeley-DeWitt Shortcut (Fast Path — Hours)

Connes (Session 19d) identified a faster preliminary check using the spectral action formalism:

```
V_eff(tau) = 2 f_4 Lambda^4 a_0(tau) + 2 f_2 Lambda^2 a_2(tau) + f_0 a_4(tau) + O(Lambda^{-2})

where:
  a_0(tau) = (4pi)^{-4} Vol(K)          [tau-independent! Volume-preserving.]
  a_2(tau) = (4pi)^{-4} (1/6) int R_K(tau) dvol_K
  a_4(tau) = (4pi)^{-4} (1/360) int [5R_K^2 - 2|Ric|^2 + 2|Riem|^2](tau) dvol_K
```

For V_eff to have a minimum, we need:

```
dV_eff/dtau = 2 f_2 Lambda^2 (da_2/dtau) + f_0 (da_4/dtau) = 0
```

The condition: **da_2/dtau and da_4/dtau must have opposite signs at some tau.**

- da_2/dtau: involves d(R_K)/dtau. From Session 17b SP-2, R_K(tau) = (3/2)(2e^{2tau} - 1 + 8e^{-tau} - e^{-4tau}). So dR_K/dtau = (3/2)(4e^{2tau} - 8e^{-tau} + 4e^{-4tau}) > 0 for all tau > 0. **da_2/dtau > 0.**

- da_4/dtau: involves d(|Riem|^2)/dtau. The full Riemann tensor squared |R_{abcd}|^2 has components from u(1), su(2), and C^2 sectors scaling as e^{4tau}, e^{-4tau}, and e^{2tau} respectively. The competition between growing (u(1)) and shrinking (su(2)) terms could produce a sign change.

**If da_4/dtau < 0 at some tau:** The Connes f_2/f_0 ratio can be chosen to balance, giving a V_eff minimum. This is computable from existing curvature data IN HOURS.

**This is the fast gate.** Compute |Riem|^2(tau) from the Riemann tensor components. If da_4/dtau ever changes sign, the spectral action path to stabilization is OPEN.

---

# IV. REQUIRED READING

## ALL agents:

1. **Session 19d Casimir energy minutes**: `sessions/session-19/session-19d-casimir-energy.md`
   Focus: Section VII-B (TT 2-tensor discovery), Section III (theoretical analysis), Section V (data quality issue with `kk1_bosonic_spectrum.npz`)

2. **Session 19d master collaborative synthesis**: `sessions/session-19/session-19d-master-collab.md`
   Focus: Section II (Session 20 pipeline), Section III (convergent themes), Section IV (new physics), Section VI (priority-ordered agenda)

3. **Session 18 V_eff convergence**: `sessions/session-18/session-18-veff-convergence.md`
   Focus: DOF counts, V_CW data points, convergence diagnostics (0.55% between mps=5 and mps=6)

4. **Your agent memory**: `.claude/agent-memory/{your-agent}/`

## phonon-exflation-sim additionally:

5. **`tier0-computation/b6_scalar_vector_laplacian.py`** — Contains `compute_connection_ON()` and `ricci_tensor_ON()`. You are extending these to produce the full Riemann tensor R_{abcd}(tau).

6. **`tier0-computation/d19d_casimir_gate.py`** — Your D-1 gate script. Contains the E_proxy boson/fermion machinery you will extend to include TT modes.

7. **`tier0-computation/tier1_dirac_spectrum.py`** — `jensen_metric()`, `get_irrep_matrices()`, `collect_spectrum()`. The Peter-Weyl infrastructure you are extending to TT 2-tensors.

8. **`tier0-computation/h5_standalone_verify.py`** — V_CW data at 26 tau-values. Needed for D-3 (V_total assembly).

## kaluza-klein-theorist additionally:

9. **Session 19d KK collaboration**: `sessions/session-19/session-19d-kk-collab.md` — Your prior analysis including sector-by-sector matrix size estimates, Duff-Nilsson-Pope instability theorem, and Freund-Rubin balance framework.

10. **Baptista Paper 15**: `researchers/Baptista/15_2024_Internal_symmetries_in_Kaluza_Klein_models.md`
    Focus: eqs (3.14)-(3.19) — the EXACT framework for Lichnerowicz on TT 2-tensors in this KK setting. eq (3.17) gives 4D TT mode masses: m_n^2 = mu_n - R_K/4.

11. **Session 17b SP-2 curvature output**: `tier0-computation/sp2_final_verification.py` — 4 curvature invariants as analytic functions of tau. R_{abcd}(tau) components are partially encoded here.

## connes-ncg-theorist additionally:

12. **Session 19d Connes collaboration**: `sessions/session-19/session-19d-connes-collab.md` — Your Seeley-DeWitt shortcut (Section 3.1: compute da_2/dtau and da_4/dtau). This is the fast path.

13. **Connes papers in your corpus**: Focus on Papers 07 (spectral action principle), 10 (Chamseddine-Connes-Marcolli), 14 (NCG spectral standpoint). The a_2 and a_4 coefficients and their physical interpretation.

14. **`tier0-computation/tier1_spectral_action.py`** — Seeley-DeWitt coefficient computations. Contains `baptista_V_tree()` and the spectral action infrastructure.

---

# V. CALCULATION ASSIGNMENTS

## Agent Allocation

| Assignment | Primary | Secondary | Rationale |
|:-----------|:--------|:----------|:----------|
| L-0: Seeley-DeWitt fast gate | connes | kk (validation) | Fastest path; uses existing curvature data. Hours. |
| L-1: Full Riemann tensor R_{abcd}(tau) | phonon-exflation-sim | kk (formula check) | Extension of existing `ricci_tensor_ON()`. New ingredient. |
| L-2: Lichnerowicz matrix assembly | phonon-exflation-sim | kk (TT projection) | Peter-Weyl + Riemann coupling. Core new code. |
| L-3: TT eigenvalue sweep | phonon-exflation-sim | kk (convergence) | 21 tau-values, 28 sectors, mps=6. |
| L-4: V_total assembly + minimum search | phonon-exflation-sim | kk + connes (physics) | Combines all contributions. DECISIVE. |
| L-5: Phonon band structure | kk | connes (NCG framing) | omega vs C_2(p,q) for all four mode types. |
| L-6: tau_0 physics extraction | All | — | If minimum exists: couplings, mass ratios, predictions. |

**Phase 1 (parallel):**
- connes: L-0 (Seeley-DeWitt shortcut, HOURS)
- phonon-exflation-sim: L-1 (Riemann tensor, prerequisite for L-2)

**Phase 2 (parallel, after L-1):**
- phonon-exflation-sim: L-2 + L-3 (Lichnerowicz assembly + sweep)
- kk: L-5 (phonon band structure from existing eigenvalue data)

**Phase 3 (sequential, after L-3):**
- phonon-exflation-sim: L-4 (V_total minimum search) — DECISIVE

**Phase 4 (conditional on L-4 finding minimum):**
- All: L-6 (physics extraction at tau_0)

---

## Assignment L-0: Seeley-DeWitt Fast Gate (HOURS)

**Agent**: connes-ncg-theorist
**Priority**: FIRST — run this before Phase 2. It costs hours and could confirm the fast path.

### Background

The spectral action effective potential is:

```
V_eff(tau) = 2 f_2 Lambda^2 a_2(tau) + f_0 a_4(tau)
```

(a_0 is tau-independent by volume preservation.) A minimum requires:

```
dV_eff/dtau = 0
=> 2 f_2 Lambda^2 (da_2/dtau) + f_0 (da_4/dtau) = 0
=> da_2/dtau and da_4/dtau must have OPPOSITE SIGNS
```

### Computation Steps

1. **Compute a_2(tau)**: Evaluate a_2 = (1/6) * R_K(tau) * Vol(K). Use the exact formula R_K(tau) = (3/2)(2e^{2tau} - 1 + 8e^{-tau} - e^{-4tau}) from Session 17b SP-2. Compute da_2/dtau analytically.

2. **Compute a_4(tau)**: From the Session 17b SP-2 curvature invariants:
   - R_K^2(tau) — already computed
   - |Ric|^2(tau) = sum_{a,b} Ric_{ab}^2 — compute from Baptista eq 3.66 components
   - |Riem|^2(tau) = sum_{a,b,c,d} R_{abcd}^2 — **this requires the full Riemann tensor**

   Use the formula for a Lie group with left-invariant metric:
   ```
   |Riem|^2 = sum over all R_{abcd} components
   ```

   On SU(3) with bi-invariant metric (tau=0):
   ```
   R_{abcd}|_{tau=0} = -(1/4) f_{abe} f^e_{cd}
   |Riem|^2|_{tau=0} = (1/16) sum f_{abe} f^e_{cd} f^{ab}_g f^{gcd} [contract over all indices]
   ```

   Under Jensen deformation, the Riemann tensor acquires anisotropic corrections. Use the Koszul formula with the Jensen metric to extract R_{abcd}(tau) at several tau-values and compute |Riem|^2(tau).

3. **Compute da_4/dtau**: Numerical differentiation from the tau-grid.

4. **Check sign**: If sign(da_2/dtau) = -sign(da_4/dtau) at some tau, the spectral action has a minimum for appropriate f_2/f_0 ratio. Report the crossing tau.

5. **Find the optimal f_2/f_0**: The ratio 2 f_2 Lambda^2 / f_0 is the physical ratio. For the tau_c where da_2/dtau = -C * da_4/dtau, the ratio is C. Report whether this ratio requires fine-tuning or is natural (O(1)).

### Deliverable

- Table: a_2(tau), a_4(tau), da_2/dtau, da_4/dtau at 21 tau-values
- Plot: da_2/dtau and da_4/dtau vs tau
- RESULT: Do they have opposite signs? If yes — at what tau range? What is the required f_2/f_0?
- Assessment: Is the spectral action (NCG) path to stabilization OPEN or CLOSED?

**Write to**: `tier0-computation/l20_seeley_dewitt_gate.py`

---

## Assignment L-1: Full Riemann Tensor R_{abcd}(tau) (PREREQUISITE)

**Agent**: phonon-exflation-sim
**Priority**: HIGHEST — L-2 and L-3 block on this.

### Background

The Lichnerowicz operator requires R_{abcd}(tau) in the left-invariant frame. The `b6_scalar_vector_laplacian.py` script already computes the Riemann tensor implicitly (since `ricci_tensor_ON()` uses it via contraction). The task is to extract and store the full R_{abcd} array.

### Formula (Baptista + Milnor)

For a Lie group G with left-invariant metric g, the Riemann tensor in the orthonormal basis {e_a} is:

```
R^d_{abc} = sum_e (Gamma^e_{bc} Gamma^d_{ae} - Gamma^e_{ac} Gamma^d_{be} - f^e_{ab} Gamma^d_{ec})
```

where the connection coefficients (Koszul formula) are:

```
Gamma^c_{ab} = (1/2)(f^c_{ab} + g^{cd}(g_{ad} f^a_{bd}... ))
              = (1/2)([e_a, e_b]^c + g^{cd} g_{ac} [e_b, e_d]^c' - ...)
```

Explicit form for left-invariant metric on SU(3):

```
Gamma^c_{ab} = (1/2)(f^c_{ab} - g^{cd}(g_{ae} f^e_{bd} + g_{be} f^e_{ad}))
```

where f^c_{ab} are the structure constants (f_{1,2}^3 = 2, etc. for SU(3) Gell-Mann basis).

The lowered tensor: R_{abcd} = g_{ae} R^e_{bcd}.

### Computation Steps

1. Load the Gell-Mann structure constants f^c_{ab} (already in `tier1_dirac_spectrum.py`).

2. For each tau in [0, 0.1, ..., 2.0], compute:
   - Jensen metric g_{ab}(tau) from `jensen_metric(tau)` — returns 8x8 diagonal matrix
   - Connection coefficients Gamma^c_{ab}(tau) — shape (8,8,8), from Koszul formula
   - Riemann tensor R^d_{abc}(tau) — shape (8,8,8,8), from the formula above
   - Lowered R_{abcd}(tau) — shape (8,8,8,8), by contracting with g

3. **Validation**: At tau=0, verify R_{abcd}|_{tau=0} = -(1/4) f_{abe} f^e_{cd}. Cross-check against `ricci_tensor_ON()` output: R_{ab} = sum_c R^c_{acb} should match.

4. **Consistency with Session 17b SP-2**: The 4 curvature invariants from SP-2 should be recoverable from R_{abcd}:
   - R_K = g^{ac} R_{ab}^{\ \ b}{}_c (scalar curvature from Ricci trace)
   - |Ric|^2 = Ric_{ab} Ric^{ab}
   - K_max and K_min from sectional curvatures K(u,v) = R_{abcd} u^a v^b u^c v^d / (|u|^2|v|^2 - (u.v)^2)
   - |Weyl|^2 from W_{abcd} = R_{abcd} - (...)

### Deliverable

- Function `compute_riemann_tensor_ON(s)` that returns R_{abcd} as an 8x8x8x8 array
- Validation report: agreement with `ricci_tensor_ON()` and Session 17b curvature invariants
- Save R_{abcd}(tau) at all 21 tau-values to `l20_riemann_tensor.npz`

**Write to**: `tier0-computation/l20_riemann_tensor.py`

---

## Assignment L-2: Lichnerowicz Matrix Assembly in Peter-Weyl (CORE COMPUTATION)

**Agent**: phonon-exflation-sim
**Priority**: HIGH — BLOCKED BY L-1.

### Background

The Lichnerowicz operator in Peter-Weyl sector (p,q) acts on the tensor product space:

```
V_{(p,q)} tensor Sym^2_{TT}(su(3)^*)
```

where V_{(p,q)} is the representation space of the (p,q) irrep (dimension dim(p,q)) and Sym^2_{TT}(su(3)^*) is the 27-dimensional TT fiber (or 35-dimensional Sym^2_0 fiber before TT projection).

At the bi-invariant point (tau=0), the TT fiber is a definite SU(3) representation: the (2,2) irrep with dimension 27. At tau != 0, the Jensen metric breaks the right SU(3) symmetry, and the TT fiber must be treated as a 35-dimensional space (Sym^2_0 = traceless symmetric) with divergence-free condition imposed sector-by-sector.

### Computation Steps (following Baptista's correction, Session 19d)

1. **Work with Sym^2_0 (35-dimensional) fiber at tau != 0:**
   At tau != 0, the TT condition uses the DEFORMED connection, which mixes the 1 + 8 + 27 components of Sym^2(8). Work with Sym^2_0 (traceless symmetric, dimension 35) and impose the transversality constraint nabla^a h_{ab} = 0 within each Peter-Weyl sector separately.

2. **For each sector (p,q):**
   a. Construct the (dim(p,q) * 35) x (dim(p,q) * 35) rough Laplacian matrix in the Peter-Weyl basis. This uses the same structure as the vector Laplacian but with 35-dim fiber tensor structure.
   b. Construct the curvature coupling matrix: the -2 R_{acbd} h^{cd} term gives a (dim(p,q) * 35) x (dim(p,q) * 35) matrix via tensor contraction of R_{abcd}(tau) with the 35-dimensional fiber basis vectors.
   c. Construct the Ricci coupling: +2 Ric_{(a}^c h_{b)c} gives another matrix term.
   d. Sum to get the full Lichnerowicz matrix: M_L = M_nabla^2 + M_Riemann + M_Ricci.
   e. Impose TT constraint: Project onto the subspace of h_{ab} satisfying nabla^a h_{ab} = 0 in the deformed metric. This reduces the 35-dim fiber to (approximately) 27 physical TT modes per sector. At tau=0, exactly 27. At tau!=0, approximately 27 (divergence-free constraint may mix modes slightly).
   f. Diagonalize the projected Lichnerowicz matrix. Record eigenvalues and multiplicities.

3. **Multiplicity convention**: Use dim(p,q) as the multiplicity (same as scalar Laplacian convention in `b6_scalar_vector_laplacian.py`). The total TT DOF is sum over sectors of dim(p,q) * (number of TT eigenvalues per sector) ~ sum dim(p,q) * 27 = 741,636 at mps=6.

4. **Validation at tau=0:**
   - At the bi-invariant metric, the Lichnerowicz operator on TT 2-tensors is positive definite (Besse, Lie Groups, compact case). Verify all eigenvalues > 0.
   - At tau=0, compare to the analytic formula: Delta_L h_{ab}|_{tau=0} = -nabla^2 h_{ab} + (1/2) h_{ab} (using R_{abcd}|_{tau=0} = -(1/4) f_{abe} f^e_{cd} and the Bochner formula).
   - Check that Lichnerowicz eigenvalues exceed R_K/4 at tau=0 (required by the positive spectrum theorem).

5. **Tachyonic mode check (from Baptista eq 3.17):**
   The 4D TT KK mass is m_n^2 = mu_n - R_K(tau)/4. If any mu_n < R_K(tau)/4, the TT mode is tachyonic (unstable). Report the tachyon count at each tau.

### Deliverable

- Function `lichnerowicz_TT_sector(p, q, tau, R_abcd)` that returns TT eigenvalues and multiplicities for one (p,q) sector
- Function `collect_TT_spectrum(tau, max_pq_sum=6)` that sweeps all sectors
- Validation report at tau=0: positivity, Bochner bound, tachyon check
- Save TT eigenvalue data to `l20_TT_spectrum.npz`

**Write to**: `tier0-computation/l20_lichnerowicz.py`

---

## Assignment L-3: TT Eigenvalue Sweep + E_proxy Check (GATE)

**Agent**: phonon-exflation-sim
**Priority**: HIGH — BLOCKED BY L-2.

### Computation Steps

1. Run `collect_TT_spectrum(tau)` at all 21 tau-values (0.0, 0.1, ..., 2.0).

2. Compute E_proxy_TT(tau) = +(1/2) * sum mult_n * sqrt(mu_n(tau)) (linear weighting, bosonic, positive sign).

3. Compute the full bosonic E_proxy:
   ```
   E_proxy_boson_full(tau) = E_proxy_scalar(tau) + E_proxy_vector_full(tau) + E_proxy_TT(tau)
   ```
   where E_proxy_scalar and E_proxy_vector_full come from `d19d_casimir_gate.py` at matched truncation.

4. Compute the updated ratio R_full(tau) = |E_proxy_fermion(tau)| / E_proxy_boson_full(tau).

5. **Gate check**: Is R_full < 1 at any tau? (This would mean bosons dominate and sign of E_total flips.)

6. Compute dE_proxy_total_full/dtau. Does it change sign at any tau?

7. **Convergence check**: Run at mps=5 and mps=6. Does the TT Casimir energy shape stabilize?

### Deliverable

- E_proxy_TT(tau) at all 21 tau-values
- R_full(tau) = F/B ratio with all four mode types
- Plot: E_proxy_boson_full vs E_proxy_fermion vs tau
- GATE RESULT: Does dE_total/dtau change sign? YES/NO.

**Write to**: `tier0-computation/l20_TT_casimir_gate.py`

---

## Assignment L-4: V_total Assembly and Minimum Search (DECISIVE)

**Agent**: phonon-exflation-sim
**Priority**: DECISIVE — blocked by L-3. This is the computation that resolves the framework.

### Computation Steps

1. **Assemble V_total(tau):**
   ```
   V_total(tau) = V_tree(tau) + V_CW(tau) + E_Casimir_total(tau)

   where:
     V_tree: from baptista_V_tree() in tier1_spectral_action.py
     V_CW:   from h5_standalone_verify.py (26-point data, interpolate to 21-tau grid)
     E_Casimir_total = E_Casimir_scalar + E_Casimir_vector + E_Casimir_TT - E_Casimir_fermion
   ```

2. Note: the UNREGULATED E_proxy diverges as mps increases. The tau-DEPENDENCE is the physical content. For the minimum search, use the regulated Casimir via one of:
   - **Option A (fast)**: Use the Taylor-subtracted E_proxy at matched mps=5 and mps=6 to extract the tau-dependent SHAPE of E_Casimir, normalized to E_Casimir(0) = 0.
   - **Option B (rigorous)**: Full zeta-function regularization as specified in Session 19d D-2 (compute the heat kernel K(t, tau) and analytically continue via Seeley-DeWitt pole structure). More work, but physical.
   - **Recommendation**: Start with Option A to check for sign flip in dE_total/dtau. If sign flip is confirmed, upgrade to Option B for the minimum location.

3. **Compute dV_total/dtau** by finite differences.

4. **Search for sign change** in dV_total/dtau. If found: tau_0 is the minimum.

5. **mu-dependence scan**: V_CW depends on mu. Repeat at mu = 0.01, 1.0, 10.0 (using Session 18 multi-mu data). Does tau_0 shift significantly? What is the sensitivity?

6. **Convergence check**: Compare tau_0 at mps=5 vs mps=6. If shift > 50%, result is truncation-dominated.

### Closure / Survive / Decisive

| Result | Interpretation | Framework Status |
|:-------|:--------------|:-----------------|
| **CLOSED**: dV_total/dtau negative everywhere | TT modes reinforce runaway. Full Casimir closed. | 30-40%. Instantons/lattice required. |
| **WEAK SURVIVE**: Sign flip exists, tau_0 > 1.0 | Minimum found but in "wrong" zone | 45-55%. Suggestive but not compelling. |
| **STRONG SURVIVE**: tau_0 in [0.15, 0.30] | Three independent routes converge | 60-75%. Compelling. Publish. |
| **DECISIVE**: tau_0 in [0.15, 0.30] + phi_paasch at tau_0 | Four-fold convergence: gauge + phi + spectral + Casimir | 75-85%. Very strong. |

### Deliverable

- V_total(tau) = V_tree + V_CW + E_Casimir_total (plot showing all contributions)
- dV_total/dtau with sign changes marked (or absence thereof)
- tau_0 value (if minimum exists) + uncertainty from mu-dependence
- Convergence assessment at mps=5 vs mps=6
- VERDICT: CLOSED / WEAK SURVIVE / STRONG SURVIVE / DECISIVE

**Write to**: `tier0-computation/l20_vtotal_minimum.py`

---

## Assignment L-5: Phonon Band Structure Diagram (KK-theorist, PARALLEL)

**Agent**: kaluza-klein-theorist
**Priority**: HIGH — runs in parallel with L-1/L-2/L-3.

The Session 19d collaborative review unanimously identified this as the key visualization for Session 20.

### Computation Steps

1. From existing eigenvalue data (sweep_s_data), extract at each tau:
   - Scalar Laplacian eigenvalues: omega_scalar^2 = lambda_n^{scalar}(tau)
   - Dirac eigenvalues: omega_Dirac = |lambda_n^{Dirac}(tau)|

2. Once L-3 is complete:
   - TT Lichnerowicz eigenvalues: omega_TT^2 = mu_n^{TT}(tau)

3. Produce the phonon band structure diagram: omega vs C_2(p,q) for all four mode types (scalar, vector, TT, Dirac) at tau = 0, 0.15, 0.30, and tau_0 (if found).

4. Mark the key features:
   - Mode crossings (scalar vs Dirac, TT vs Dirac)
   - Avoided crossings
   - Spectral gaps
   - The sector (3,0) at tau=0.15 where phi_paasch emerges

5. **Tachyonic instability boundary**: From L-2, identify the smallest tau_* where any TT eigenvalue satisfies mu_n(tau) < R_K(tau)/4 (tachyon threshold from Baptista eq 3.17). Plot the tachyon boundary on the band structure.

### Deliverable

- Band structure diagram (omega vs C_2(p,q)) for all four mode types at four tau-values
- Tachyon boundary tau_* (if any TT mode goes tachyonic)
- Mode crossing diagram: which bosonic tower first crosses the fermionic contribution at tau_0?

**Write to**: `tier0-computation/l20_phonon_band_structure.py`

---

## Assignment L-6: Physics Extraction at tau_0 (CONDITIONAL ON L-4 SURVIVE)

**Agent**: ALL (jointly, after L-4)

If L-4 finds a minimum at tau_0:

1. **Gauge couplings**: Evaluate g_1/g_2 = e^{-2*tau_0}, sin^2(theta_W) = e^{-4*tau_0}/(1+e^{-4*tau_0}).
   Compare to experimental sin^2(theta_W) = 0.23121.

2. **Mass ratio + Paasch tests**: m_{(3,0)}/m_{(0,0)} at tau_0 from Dirac eigenvalues. Compare to phi_paasch = 1.53158. **Run the full pre-registered Paasch test battery (P-1 through P-4) from Section XII.** Blind analysis required for P-1 and P-2. Sector identification must be locked before any ratio comparison.

3. **Neutrino masses (Session 19d, Neutrino specialist)**: The three lightest Dirac eigenvalues at tau_0. Check:
   - KATRIN bound: m_nu < 0.45 eV (lightest)
   - Two oscillation mass-squared differences: Delta m^2_solar = 7.5e-5 eV^2, Delta m^2_atm = 2.5e-3 eV^2
   - Ratio of lightest three: approximately 1 : 33 (from oscillation data)

   This is a ZERO-PARAMETER prediction. It either agrees or fails.

4. **Tachyon check**: Is tau_0 below the tachyon boundary tau_*? If tau_0 > tau_*, the minimum is in a region where the TT modes are unstable — the vacuum is a saddle point, not a true minimum.

5. **Convergence table** (from Session 19c E-4 template):

| Source | tau value | Session |
|:-------|:---------|:--------|
| Level statistics inflection tau_c | ? | 19a (structural null; TBD with full D_K) |
| Spectral dimension d_s minimum | tau ~ 0.9 | 19a S-2 |
| Entropy production maximum | beta-dependent | 19a S-3 |
| FRW solution tau(t_now) | TBD | 19b R-2 |
| Gauge coupling (Weinberg angle) | 0.2994 | 17a B-1 |
| Mass ratio phi_paasch | 0.15 | Session 12 |
| Boltzmann minimum | 0.164 | 17a H-1 |
| CW inflection (not minimum) | 0.3-0.6 | Session 14 |
| **Lichnerowicz/Casimir tau_0** | **TBD (THIS SESSION)** | **20 L-4** |

How many independently-determined tau values agree?

---

# VI. PREDICTION TABLE AND DECISION GATES

## PRE-REGISTERED CONSTRAINT/Survive Criteria (Sagan standard)

From the 14-agent Session 19d collaborative review (Sagan Section 3, Hawking Section 2.4):

| Level | Criterion | Bayes Factor |
|:------|:----------|:-------------|
| **Interesting** | Robust minimum at any tau_0 (stable across mu, mps) | BF ~ 3-5 |
| **Compelling** | tau_0 in [0.15, 0.30] + gauge coupling match within 20% | BF ~ 10-30 |
| **Decisive** | phi_paasch mass ratio at tau_0 within 1%, AND tau_0 in [0.15, 0.30] | BF ~ 100+ |

**CLOSED**: No minimum at any tau, or minimum only with fine-tuned mu (>2 orders of magnitude sensitivity).
**FATAL CLOSED**: Minimum exists but is in a tachyonic region (tau_0 > tau_*), making it a saddle point.

## The Prediction Lookup Table (from Session 18 prompt, updated with TT)

```
  tau_0   sin2(tW)    g1/g2    m(3,0)/m(0,0)   phi_paasch match?
----------------------------------------------------------------------
 0.150    0.3580     0.763    1.53159          YES (0.0005%)
 0.164    0.3452     0.720    1.52892          CLOSE (0.17%)
 0.200    0.3100     0.670    1.51998          1%
 0.250    0.2769     0.619    1.50300          2%
 0.300    0.2315     0.549    1.48180          3%
 0.2994   0.2320     0.549    1.48208          WEINBERG MATCH
```

V_total(tau_0) picks the row. Experiment checks the columns.

---

# VII. SUCCESS CRITERIA

**Minimum success**: One of the following:
- (a) L-0 (Seeley-DeWitt): da_2/dtau and da_4/dtau have opposite signs. NCG path OPEN.
- (b) L-4: V_total(tau) has a robust minimum at some tau_0 in [0.0, 1.5]. Casimir stabilization confirmed.

**Full success**: L-4 finds tau_0 in [0.15, 0.30] + L-6 evaluates prediction table within 20% experimental values.

**Extraordinary success**: All of the above + phi_paasch mass ratio at tau_0 within 1%.

**Either of (a) or (b) is a major result.** Option (a) provides a parameter-based path (f_2/f_0 choice). Option (b) is parameter-free.

**DO NOT** produce another inconclusive result from incomplete mode counting. The TT modes are the largest bosonic sector. Include them. If the result with TT modes is still monotonic, report it cleanly — that result closes the Casimir path definitively with complete mode content.

---

# VIII. WORKFLOW AND FILE NAMING

```
Phase 1 (PARALLEL — HOURS):
  connes        -> L-0: l20_seeley_dewitt_gate.py
  phonon-sim    -> L-1: l20_riemann_tensor.py

Phase 2 (PARALLEL — after L-1):
  phonon-sim    -> L-2: l20_lichnerowicz.py
  kk            -> L-5: l20_phonon_band_structure.py (from existing data)

Phase 3 (SEQUENTIAL — after L-2):
  phonon-sim    -> L-3: l20_TT_casimir_gate.py

Phase 4 (SEQUENTIAL — after L-3):
  phonon-sim    -> L-4: l20_vtotal_minimum.py

Phase 5 (CONDITIONAL — after L-4 SURVIVE):
  All           -> L-6: l20_physics_extraction.py
```

**Environment**: GPU venv — `phonon-exflation-sim/.venv312/Scripts/python.exe` for ALL scripts. The RX 9070 XT has 17 GB VRAM. Eigenvalue computations at large matrix sizes (up to 2240 x 2240 for sector (3,3)) benefit from GPU.

**Output files** (all in `tier0-computation/`):

| Script | Purpose |
|:-------|:--------|
| `l20_seeley_dewitt_gate.py` | Fast NCG gate: da_2/dtau vs da_4/dtau |
| `l20_riemann_tensor.py` | Full R_{abcd}(tau) computation + validation |
| `l20_lichnerowicz.py` | Lichnerowicz matrix assembly + TT eigenvalue sweep |
| `l20_TT_casimir_gate.py` | Full F/B ratio with TT modes + sign check |
| `l20_vtotal_minimum.py` | V_total = V_tree + V_CW + E_Casimir, minimum search |
| `l20_phonon_band_structure.py` | omega vs C_2(p,q) for all four mode types |
| `l20_physics_extraction.py` | tau_0 physics: couplings, masses, neutrinos (conditional) |

---

# IX. DESIGNATED WRITER AND OUTPUT

**Designated writer for meeting minutes**: kaluza-klein-theorist.

**Final document**: `sessions/2026-02-XX-session-20-TT-lichnerowicz.md`

Must contain:
1. TT Lichnerowicz eigenvalue spectrum (table + plot by sector)
2. Full bosonic DOF count verification at mps=6
3. E_proxy_TT(tau) + updated F/B ratio R_full(tau) (plot)
4. V_total(tau) = V_tree + V_CW + E_Casimir_total (plot)
5. Minimum search result: tau_0 (or CLOSED verdict with evidence)
6. L-0 Seeley-DeWitt result: da_2/dtau vs da_4/dtau
7. L-5 phonon band structure diagram
8. Tachyon boundary check
9. If SURVIVE: prediction table at tau_0
10. If SURVIVE: neutrino mass predictions vs KATRIN/oscillation data
11. Updated framework probability with rationale
12. Session 21 plan based on outcome

---

# X. WHAT SESSION 20 DOES NOT COVER

The following are explicitly deferred:

| Item | Session | Status |
|:-----|:--------|:-------|
| D_total Pfaffian (full construction) | 21+ | Needs eigenvectors from 19c E-1; independent of Casimir |
| Full Anderson transition test (GOE level statistics) | 21+ | Requires full off-diagonal D_K with Kosmann-Lichnerowicz coupling; structural null in block-diagonal data |
| Spectral back-reaction simulation (Section IX of 19 primer) | 21+ | Needs eigenvectors + Landau-Zener coupling matrix code |
| Rolling modulus w(z) DESI DR2 comparison | 19b | Status from Session 19b pending |
| Instanton corrections on (SU(3), g_s) | Deferred | Non-perturbative, weeks |
| Lattice SU(3) with Jensen metric | Deferred | Months |
| Full analytic Casimir via exact zeta asymptotics | Deferred | Requires exact spectral asymptotics beyond current data |
| Kibble-Zurek defect spectrum from first-order transition | Post-20 | Follows from Landau's first-order classification |
| Albert algebra connection (dim 27 = dim J_3(O)) | Open question | Tesla flagged as speculative; worth tracking |

---

# XI. COMPLETE STABILIZATION STATUS TABLE

Accounting of every mechanism since Session 18:

| Mechanism | Status | Key Result | Session |
|:----------|:-------|:-----------|:--------|
| V_tree minimum | CLOSED | Monotonic, V'''(0) = -7.2 | 17a SP-4 |
| 1-loop CW minimum | CLOSED | Monotonic, F/B = 8.4:1, convergent | 18 |
| Casimir (scalar + vector) | CLOSED | R = 9.92:1 constant, same sign as CW | 19d D-1 |
| Spectral back-reaction (scal+vec) | CLOSED | Same sign as V_CW, reinforces runaway | 19d |
| Fermion condensate | CLOSED | Spectral gap > 0.818 everywhere | 19a S-4 |
| D_K Pfaffian Z_2 | TRIVIAL | Z_2 = +1 throughout, no transition | 17c D-2 |
| **Casimir (with TT 2-tensors)** | **OPEN** | **F/B flips to 0.44:1 if TT confirmed** | **THIS SESSION** |
| D_total Pfaffian (J * D_total) | QUEUED | Needs eigenvectors (19c) | 21+ |
| Rolling modulus (no minimum) | TESTED | Quintessence path, results from 19b | 19b |
| Spectral action NCG (Seeley-DeWitt balance) | **OPEN** | **da_2/da_4 sign check: THIS SESSION** | **L-0** |
| Instanton corrections | DEFERRED | Non-perturbative | --- |
| Lattice SU(3) | DEFERRED | Months | --- |

---

# XII. PRE-REGISTERED PAASCH REDEMPTION TESTS (Session 19 Duo Review)

**Source**: Joint verdict of paasch-mass-quantization-analyst + gen-physicist (2026-02-19).
**Context**: Session 16 closed Paasch's SCAFFOLDING (phi_paasch^n geometric series, spiral sequences, N(j)=7n integers, LNH) but left his ALGEBRAIC CORE untested on D(SU(3)). The duo concluded: "Session 16 closed Kepler's circular orbits, not Kepler's harmonic law T^2 ~ a^3." These tests activate IF L-4 finds tau_0. They cost zero additional computation — all observables are extractable from the Dirac eigenvalue data already computed at tau_0.

## P-0: Gate (Shared with L-4)

tau_0 exists — V_total has a local minimum at tau_0 > 0. PASS/FAIL. If FAIL: run all P-tests at gauge-coupling-imposed tau_W = 0.2994 as BACKUP (Level 2.5 evidence only, not redemption).

## Pre-Registered Test Table

| Test | Observable | Target | UPGRADE | SUGGESTIVE | CLOSED | Tier | Notes |
|:-----|:-----------|:-------|:--------|:-----------|:-----|:-----|:------|
| **P-1** | m_{(3,0)}/m_{(0,0)} at tau_0 | 1.53158 (phi_paasch) | <0.1% dev | <0.5% dev | >5% dev | 1 (immediate) | Blind analysis required |
| **P-2** | [m_{(3,0)}/m_{(0,0)}]^{2/3} at tau_0 | phi_paasch via N^{3/2} scaling | <0.3% dev | <1% dev | >3% dev | 1 (runs with P-1) | Most Paasch-specific test; separates N^{3/2} scaling from generic Casimir numerology |
| **P-3** | p/K sector ratio at tau_0 | 1.9006 (m_p/m_K, PDG) | <5% dev | <10% dev | >15% dev | 1 (needs U(2) ID) | Requires sector identification locked BEFORE ratio check |
| **P-4** | Consecutive sector M-ratio | 0.618034 (1/phi_golden) | <1% dev | <3% dev | >5% dev | 1 (needs sector ordering) | Tests Paasch's M-value golden ratio structure |
| **P-5** | N(b) from D_K multiplicities | 112 | exact +/-3 | +/-7 | wrong multiplicity | 2 | Requires eigenvalue multiplicity analysis |
| **P-6** | Z_3 generation hierarchy | 1:207:3477 (m_e:m_mu:m_tau) | factor-of-2 all three | factor-of-3 | wrong order of magnitude | 2 (spinor transport) | Requires Tier 2 Z_3 computation (Paper 18 App E) |
| **P-7** | alpha from spectral integers | 0.0072974 | <1e-6 | <1e-4 | >1% dev | 3 (requires P-5) | Conditional on N(b) derivation from D_K |

## R4: Alpha Circularity Constraint Condition (CHECK BEFORE SESSION 20 RESULTS)

The derivation chain phi_paasch -> Omega constant f -> alpha = f^{n_3} where n_3=10 must be verified as non-circular. The integer n_3 must be derivable from D_K eigenvalue multiplicities WITHOUT using alpha as input at any point. If n_3 comes from fitting the proton mass formula (which uses alpha), the derivation is circular: alpha -> n_3 -> alpha, and the 9-digit alpha result has zero predictive content. This is a paper analysis — run during Session 20 wait time.

## Mandatory Protocol

1. **Sector identification** (U(2) quantum number map) must be locked BEFORE checking any ratio. No post-hoc sector relabeling.
2. **Blind analysis** required for P-1 and P-2: agent computing eigenvalues must not compute significance; agent computing significance must not see raw eigenvalues until targets are locked.
3. **Pre-registration is binding**: these targets are stated BEFORE computation. Post-hoc rationalization of failures invalidates the test.

## The tau_0 Tension (Overconstrainedness Feature)

Two independent constraints prefer different tau_0 values:
- Gauge coupling (sin^2(theta_W) = 0.231): prefers tau_0 ~ 0.30 (Session 17a B-1)
- phi_paasch sector ratio (m_{(3,0)}/m_{(0,0)} = 1.53158): prefers tau_0 ~ 0.15 (Session 12)

A single tau_0 satisfying BOTH would be far more significant than satisfying either alone (one free parameter, two independent observables). This is what makes L-4 potentially decisive for Paasch: not just "does tau_0 exist?" but "does the tau_0 that minimizes V_total simultaneously explain gauge couplings AND mass ratio clustering?"

## Redemption Tiers

| Tier | Requirements | Framework Upgrade | Paasch Status |
|:-----|:-------------|:-----------------|:--------------|
| **A** | P-0 + P-1 UPGRADE + P-2 | +8-12% | "Newton identified, not yet verified" |
| **B** | Tier A + P-3 + P-4 | +12-18% | "The algebraic core has a geometric home" |
| **C** | Tier A + B + P-6 | +18-25% | FULL REDEMPTION — mass ratios from fiber geometry |

**Closure**: P-1 fails (>5% at tau_0) AND backup at tau_W = 0.2994 also fails -> Paasch-D_K connection permanently severed. Algebraic formulas survive as unexplained phenomenology only.

## Joint Probability Assessment (Paasch-analyst + Gen-physicist, 2026-02-19)

| Outcome | Probability |
|:--------|:-----------|
| Tier A (partial redemption) | 8-19% |
| Tier C (full redemption) | 3-10% |
| Permanent "Kepler without Newton" | 50-60% |
| Paasch completely closed | 10-15% |

---

# XIII. INSIGHTS FROM THE SESSION 19D COLLABORATIVE REVIEW

Thirty-four contributions from fourteen reviewers distilled into actionable physics:

**On the methodology:**
> *"PRE-REGISTERED CONSTRAINT criteria with gated pipeline. Three-agent independent verification. Honest reporting of a clean closure. This is how science should work."* — Sagan (Session 19d)

> *"The question 'What did we NOT compute?' is always more productive than 'Did we compute correctly?' The discovery that TT 2-tensor modes were entirely missing — a structural omission affecting every V_eff calculation since Session 18 — is the most important finding of the session."* — Hawking (Session 19d)

**On the physics:**
> *"By omitting TT modes, we were computing T_uv while forgetting that G_uv has its own dynamics."* — Einstein (Session 19d)

> *"Different spring constants in different directions. The Riemann coupling gives the TT modes different tau-dependence. That breaks the constant-ratio trap."* — Feynman (Session 19d)

> *"The TT 2-tensor modes ARE the shape oscillations of the internal cavity. In any cavity problem, the boundary modes dominate the Casimir pressure."* — Hawking (Session 19d)

> *"V_CW hears the overtones. Casimir hears the fundamental. On this geometry, they hear the same song — but we forgot the percussion section. Twenty-seven drums were silent."* — Tesla (Session 19d)

**On the transition:**
> *"V'''(0) = -7.2. The cubic term is nonvanishing. By the Landau criterion, the transition is NECESSARILY FIRST-ORDER."* — Landau (Session 19d)

**On the implications if a minimum is found:**
> *"Lichnerowicz eigenvalues -> Casimir sign flip -> V_total minimum at tau_0 -> D_K eigenvalue spectrum -> sector mass ratios -> particle masses. If tau_0 = 0.15, phi_paasch becomes a zero-parameter prediction. This is the Newton that Paasch's Kepler has been waiting for."* — Paasch (Session 19d)

> *"Once tau_0 is fixed by Lichnerowicz: the three lightest eigenvalues must simultaneously satisfy the KATRIN bound, two oscillation mass-squared differences, and their ratio ~ 33, all from a single M_scale with zero additional parameters. The framework becomes overconstrained."* — Neutrino specialist (Session 19d)

**Framework probability consensus (Session 19d):**
- Hawking: 60-75% framework, 40-55% Lichnerowicz produces minimum
- Feynman: 48-55% framework
- Sagan: 45-52% framework
- Overall consensus: **48-58% framework, 40-55% that TT Casimir minimum exists**

---

*"Fourteen voices. One geometry. Twenty-seven drums."*
*— Session 19d master collaborative synthesis*

*"The computation says no for the modes we computed. Then sim asked: what modes did we NOT compute?"*
*— Session 19d self-audit*

*"This is the eclipse expedition. Point the telescope at the sky."*
*— Session 18 prompt, rephrased: Twenty-seven drums. Strike them.*
