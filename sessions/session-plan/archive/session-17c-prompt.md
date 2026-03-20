# Session 17c: The Pfaffian + Phase Structure + Penrose Diagram

## Session Type: Focused Calculation Sprint (Phase 3 of 4)
## Agents: Dirac-Antimatter-Theorist + Hawking-Theorist + Schwarzschild-Penrose-Geometer
## Session Goal: Execute the Level 4 Pfaffian test, compute spectral phase structure, construct the Penrose diagram. All gates from Session 17b have been passed.

---

# I. CONTEXT

Sessions 17a-17b established the foundation:
- **17a** (all 4 agents): Gauge couplings derived (B-1), V_eff computed (H-1), explicit metric written (SP-1), exact V_tree (SP-4), J-compatibility verified (D-1), mass spectrum J-symmetry confirmed (D-3), Z₃ triality table built (B-4).
- **17b** (Baptista + SP): Geometry verified against Baptista equations (B-2 PASS), curvature invariants computed (SP-2), **D_K correctness audited and CLEARED for Pfaffian (B-3 PASS)**.

- **EINSTEIN REVIEW** Thorough Einstein analog review was provided in only three words: "Compute the Pfaffian."

**The Pfaffian computation is now CLEARED.** Baptista's B-3 audit has verified that D_K correctly implements Corollary 3.4, the connection coefficients match the Koszul formula, the Killing isometry condition holds, and the Lichnerowicz theorem is satisfied.

This is where we find out if the framework has a Level 4 prediction.

Your job: **calculate**. The Pfaffian is binary — it changes sign or it doesn't. The phase structure has critical points or it doesn't. The Penrose diagram has horizons or it doesn't. Numbers, not discussion.

---

# II. REQUIRED READING

## For ALL agents:

1. **`sessions/session-16-final.md`** — Section II (ranked action list). The Pfaffian is Rank #1b.

2. **`sessions/session-16-einstein-feynman-review.md`** — Section 5: Einstein picks Pfaffian, Feynman picks gauge couplings.

## For Dirac-Antimatter-Theorist — ADDITIONALLY:

3. **`/Antimatter/`** — Your paper library.

4. **`tier0-computation/branching_computation_32dim.py`** (~1200 lines) — The J operator construction. You need J explicitly for the Pfaffian.

5. **`tier0-computation/tier1_dirac_spectrum.py`** (~1580 lines) — The D_K eigenvalue/eigenvector engine. **NOTE**: You may need to modify `collect_spectrum()` to also return eigenvectors (not just eigenvalues). Session 16 specified this as a small code change.

6. **`tier0-computation/session11_gamma_F_correction.py`** — The corrected gamma_F. Key for BdG classification.

7. **Session 17a D-1 results** — J-compatibility audit results. Confirm $[J, D_K(s)] = 0$ holds before computing Pf(J·D_F).

8. **Session 17b B-3 results** — D_K correctness audit PASS. This is your authorization to proceed.

## For Hawking-Theorist — ADDITIONALLY:

9. **`Hawking/`** — Your paper library.

10. **Your agent memory**: `.claude/agent-memory/hawking-theorist/` — Your coffee table insight: V_CW = Helmholtz free energy.

11. **`tier0-computation/tier1_dirac_spectrum.py`** — You need the full eigenvalue tower for the spectral free energy.

12. **Session 17a H-1 results** — Your own V_eff computation. You now use it as the classical background for the phase structure.

## For Schwarzschild-Penrose-Geometer — ADDITIONALLY:

13. **`/Schwarzschild-Penrose/`** — Your paper library. Penrose diagrams are YOUR specialty.

14. **Session 17a SP-1 results** — Your explicit metric.

15. **Session 17b SP-2 results** — Your curvature invariants. You need to know if $K(s)$ diverges anywhere.

---

# III. PRIOR RESULTS (from Sessions 17a-17b)

| ID | Result | Status | Key Numbers |
|:---|:-------|:-------|:------------|
| B-1 | Gauge coupling ratios | COMPLETED 17a | $g_1/g_2(s)$, $g_1/g_3(s)$, $g_2/g_3(s)$ at 4 $s$-values |
| B-2 | Geometry verification | PASS (17b) | All 4 checks passed |
| B-3 | D_K audit | **PASS (17b)** | All 4 checks passed — **PFAFFIAN CLEARED** |
| B-4 | Z₃ triality table | COMPLETED 17a | 28 irreps in 3 Z₃ classes |
| H-1 | V_eff(s) | COMPLETED 17a | $s_0 = ?$, binding criterion = ? |
| SP-1 | Explicit metric $g_s$ | COMPLETED 17a | 8×8 matrix in coordinates |
| SP-2 | Curvature invariants | COMPLETED 17b | $R$, $R_{ab}R^{ab}$, $K$, $C^2$ at 50+ $s$-values |
| SP-4 | Exact V_tree | COMPLETED 17a | Analytic expression verified |
| D-1 | J-compatibility | COMPLETED 17a | $\|[J, D_K(s)]\|$ at 50+ $s$-values |
| D-3 | J-symmetry | COMPLETED 17a | $\max|\lambda_i + \lambda_{N-i}|$ at 7 $s$-values |

**NOTE**: Replace key numbers with actual values from 17a/17b outputs before launching.

---

# IV. CALCULATION ASSIGNMENTS

## Dirac-Antimatter-Theorist: 2 Assignments

### Assignment D-2: The Pfaffian Computation (Priority: CRITICAL — Evidential Rank #1b, Level 4 Test)

This is Einstein's "if I had one computation" pick. The Pfaffian:

$$\mathrm{Pf}(s) \;=\; \operatorname{sgn}\!\Big(\operatorname{Pf}\big(J \cdot D_F(s)\big)\Big)$$

where $D_F(s)$ is the finite-dimensional Dirac operator restricted to a single sector $(p,q)$, and $J$ is the real structure from `branching_computation_32dim.py`.

**YOUR TASK**:
1. **Construct $J \cdot D_F(s)$** as an antisymmetric matrix. Required: $J^T D_F = -(J D_F)^T$ (since $J^2 = +I$ and $JD = DJ$ in KO-dim 6). Verify antisymmetry: if $J \cdot D_F$ is NOT antisymmetric, diagnose why and fix.

2. **Compute $\operatorname{Pf}(J \cdot D_F(s))$** at 100 $s$-values in $[0,\, 2.5]$. Use `scipy.linalg` or direct determinant relation $\det(A) = \operatorname{Pf}(A)^2$ for numerical Pfaffian. For sign: compute via LU decomposition or Householder reduction.

3. **Determine**: does $\operatorname{sgn}(\operatorname{Pf})$ change at any $s_c$?

**TECHNICAL NOTE**: You need eigenvectors, not just eigenvalues, to construct $D_F$ in the sector basis. The existing `tier1_dirac_spectrum.py` may need a small modification to `collect_spectrum()` to return eigenvectors. This was pre-specified in Session 16 Rank 1b.

**DELIVERABLE**:
- Plot of $\operatorname{Pf}(s)$ vs $s$ (log scale for magnitude, separate plot for sign)
- If sign change exists: $s_c$ to 6 digits, spectral gap at $s_c$ (should vanish), identification of the zero mode (which fermion becomes massless, in which $(p,q)$ sector)
- If NO sign change: state "Pfaffian constant, sgn = ±1" and classify the topological phase

**WHY THIS MATTERS**: This is the ONLY Level 4 test candidate. Binary, zero parameters, topological. If the Pfaffian changes sign:
- $s_0 = s_c$ is PINNED BY TOPOLOGY (no free parameters)
- A massless fermion appears at $s_c$ (neutrino mass prediction)
- Overrides ALL other criteria
If no sign change: the framework has no topological prediction at this level. That is also a result.

### Assignment D-4: BdG Class DIII Physical Consequences (Priority: MEDIUM)

Session 11 identified the spectral triple as BdG class DIII (topological superconductor in internal space).

**YOUR TASK**: From the BdG classification and your D-2 results:
1. What is the $\mathbb{Z}_2$ topological invariant? (This IS the Pfaffian from D-2.)
2. What are the topologically protected edge modes? (Zero modes at $s_c$, if it exists.)
3. What is the bulk-boundary correspondence? SU(3) has no boundary, but the DEFORMATION parameterized by $s$ creates an effective "boundary" between topological phases.

**DELIVERABLE**: Explicit identification of the bulk-boundary correspondence. If topologically protected zero modes exist: their quantum numbers (which $(p,q)$ sector, which Z₃ class). Are they neutrinos?

---

## Hawking-Theorist: 1 Assignment

### Assignment H-2: Spectral Free Energy and Phase Structure (Priority: HIGH)

Your coffee table insight: V_CW = Helmholtz free energy $F(s, \mu)$ with $s$ as order parameter and $\mu$ as temperature.

**YOUR TASK**:
1. Compute $F(s, \mu) = -\sum_{(p,q)} \dim(p,q) \sum_j \ln\!\big(|\lambda_j^{(p,q)}(s)|^2/\mu^2\big)$ (spectral zeta regularization) using eigenvalues from `tier1_dirac_spectrum.py`.

2. Identify critical points: $\partial F/\partial s = 0$. At each critical point, compute:
   - $F''(s)$ = curvature of free energy (second-order if smooth, first-order if discontinuity in $F'$)
   - Is it a minimum, maximum, or saddle?

3. Classify phase transitions: first-order (latent heat = discontinuity in $\partial F/\partial \mu$) or second-order (continuous, divergence in specific heat)?

4. Compute specific heat: $C(s, \mu) = -\mu\, \partial^2 F / \partial \mu^2$

**DELIVERABLE**:
- Phase diagram in $(s, \mu)$ plane (heatmap or contour plot)
- Location and order of each phase transition
- Connection to V_eff minimum from H-1: is the free energy critical point at the same $s$ as the V_eff minimum?

**WHY THIS MATTERS**: If the V_eff minimum (H-1) and the free energy critical point (H-2) coincide, that's a thermodynamic consistency check. If they DON'T coincide, the 1-loop approximation may be inadequate.

---

## Schwarzschild-Penrose-Geometer: 1 Assignment

### Assignment SP-3: The Higher-Dimensional Penrose Diagram (Priority: MEDIUM)

The full spacetime is $M^4 \times (\mathrm{SU}(3),\, g_{s(t)})$, where $s(t)$ is the time-dependent Jensen parameter (spectral exflation).

**CONSTRUCT**: The Penrose diagram for the $(1+1)$-dimensional reduction:
- One external time coordinate $t$
- One "radial" internal coordinate: the Jensen parameter $s$ (or equivalently the shape modulus)

Map conformal infinity. Use your SP-2 curvature invariants to determine:
- Does $s \to \infty$ produce a singularity? (Check: does $K(s) \to \infty$?)
- Does $s \to 0$ (bi-invariant limit) have special causal status?
- Where are horizons, if any?

Apply the Penrose singularity theorem:
- Does the internal space satisfy the required energy condition?
- Does a trapped surface exist?
- Is the $(1+1)$-dimensional mini-superspace geodesically complete?

**DELIVERABLE**:
- ASCII Penrose diagram with all boundaries labeled
- Statement about geodesic completeness
- Singularity theorem applicability: which energy condition, does a trapped surface exist?

**WHY THIS MATTERS**: The causal structure of the internal space under deformation has never been analyzed. If $s \to \infty$ is a singularity, the framework has a natural UV cutoff. If it's a conformal boundary, the space is geodesically incomplete and needs boundary conditions.

---

# V. COORDINATION

```
  D-2 (Pfaffian) ───────── [Dirac, CRITICAL, needs B-3 PASS from 17b ✓]
  D-4 (BdG class DIII) ──── [Dirac, MEDIUM, uses D-2 results]
  H-2 (spectral free energy) [Hawking, HIGH, independent of D-2]
  SP-3 (Penrose diagram) ── [SP-Geometer, MEDIUM, uses SP-2 from 17b]
```

**Interaction rules**:
- D-2 is the star of this session. Dirac computes, reports to team lead.
- D-4 naturally follows D-2 (same mathematical objects). Dirac does both sequentially.
- H-2 runs fully independent — Hawking uses eigenvalue data directly.
- SP-3 runs independent — SP uses their own curvature results.
- **If D-2 finds a sign change**: Dirac messages Hawking immediately with $s_c$. Hawking begins H-3 preparation (Session 17d).

---

# VI. SUCCESS CRITERIA

### Dirac-Antimatter-Theorist
- [ ] D-2: Pfaffian $\operatorname{Pf}(J \cdot D_F(s))$ at 100 $s$-values. **Binary verdict: sign change YES/NO. If YES: $s_c$ to 6 digits.**
- [ ] D-4: BdG bulk-boundary identification. Topological invariant. Protected zero mode quantum numbers (if any).

### Hawking-Theorist
- [ ] H-2: Phase diagram in $(s, \mu)$ plane. Phase transition locations and classification. Comparison to H-1 V_eff minimum.

### Schwarzschild-Penrose-Geometer
- [ ] SP-3: ASCII Penrose diagram. Geodesic completeness statement. Singularity theorem applicability.

That is **4 deliverables** from **3 agents**. The critical output is D-2: does the Pfaffian change sign?

---

# VII. INFRASTRUCTURE

| Script | Lines | Who Needs It |
|:-------|:-----:|:-------------|
| `tier1_dirac_spectrum.py` | ~1580 | D-2 (needs eigenvector modification), H-2 (eigenvalue tower) |
| `branching_computation_32dim.py` | ~1200 | D-2 (J operator), D-4 (BdG classification) |
| `session11_gamma_F_correction.py` | ~300 | D-4 (gamma_F for BdG class) |
| `tier1_spectral_action.py` | ~900 | H-2 (R(s) for normalization) |

---

*"A physical law must possess mathematical beauty." — Dirac*
*"The universe does not care about our comfort. Follow the mathematics." — Hawking*
*"Write down $g_{\mu\nu}$." — Schwarzschild*
