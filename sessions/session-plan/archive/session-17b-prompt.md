# Session 17b: Verification Gate — Geometry Audit + D_K Signoff

## Session Type: Focused Verification Sprint (Phase 2 of 4)
## Agents: Baptista-Spacetime-Analyst + Schwarzschild-Penrose-Geometer
## Session Goal: Quality-gate the Session 17a geometry before the Pfaffian computation. Baptista verifies SP's metric and audits D_K. SP computes curvature invariants.

---

# I. CONTEXT

Session 17a produced 7 foundation results in parallel. This phase CONSUMES those results:
- **SP-Geometer** wrote the explicit metric $g_s$ (SP-1) and exact $V_{\text{tree}}(s)$ (SP-4)
- **Dirac** verified J-compatibility (D-1) and mass spectrum J-symmetry (D-3)
- **Baptista** derived gauge coupling ratios (B-1) and built the Z₃ triality table (B-4)
- **Hawking** computed the full V_eff (H-1) — results pending or available

**This phase is the QUALITY GATE.** Nothing downstream (especially the Pfaffian in Session 17c) proceeds until Baptista signs off. One wrong sign in the metric or Dirac operator propagates to everything.

Your job is still to **calculate**, not to review or discuss. But now the calculations are VERIFICATION calculations — you compute the same things independently and check for agreement at machine epsilon.

---

# II. REQUIRED READING

## For BOTH agents — Read FIRST:

1. **`sessions/session-16-final.md`** — Section VI (11 proven results), Section VII (4 refuted claims). Know the established ground truth.

2. **`sessions/session-16-einstein-feynman-review.md`** — Section 4 "Hidden Assumptions or Gaps." Your job is to CLOSE gaps, not discuss them.

## For Baptista-Spacetime-Analyst — ADDITIONALLY:

3. **`Kaluza-Klein/`** — ALL 18 papers. You ARE the authority. For this phase, focus on:
   - Paper 15 (2024): eq 3.68 (Jensen metric), eq 3.70 (scalar curvature), eq 3.80 (V_eff)
   - Paper 17 (2025): Corollary 3.4 (D_K explicit), eq 3.8 (Dirac operator), Proposition 1.1 (Lichnerowicz)
   - Paper 18 (2026): Z₃ generation mechanism

4. **Your agent memory**: `.claude/agent-memory/baptista-spacetime-analyst/` — Your verified equation table is your quality-control checklist.

5. **`sessions/session-16-round-2b-dk-generations.md`** — Your joint work with KK-theorist on D_K correctness and Z₃ two-layer structure. Directly relevant to B-3.

6. **`tier0-computation/tier1_dirac_spectrum.py`** (~1580 lines) — The D_K implementation you are auditing (for B-3).

7. **`tier0-computation/tier1_spectral_action.py`** (~900 lines) — Contains R(s) and V_tree you are cross-checking (for B-2).

## For Schwarzschild-Penrose-Geometer — ADDITIONALLY:

8. **`/Schwarzschild-Penrose/`** — Your paper library.

9. **`Kaluza-Klein/`** — Papers 15-16 (for curvature computation conventions).

10. **`tier0-computation/tier1_spectral_action.py`** — Contains R(s) you will independently verify.

11. **Your own SP-1 output from Session 17a** — The explicit metric you wrote. You now use it for curvature.

---

# III. PRIOR RESULTS (from Session 17a)

These results were computed in Session 17a. Reference them but VERIFY independently where indicated.

| ID | Result | Status | File/Location |
|:---|:-------|:-------|:--------------|
| SP-1 | Explicit metric $g_s$ in coordinates | COMPLETED 17a | [SP-1 output location] |
| SP-4 | Exact analytic $V_{\text{tree}}(s) = -R(s) \cdot \text{Vol}$ | COMPLETED 17a | [SP-4 output location] |
| D-1 | $\|[J, D_K(s)]\|$ at 50+ $s$-values | COMPLETED 17a | [D-1 output location] |
| D-3 | Mass spectrum J-symmetry at 7 $s$-values | COMPLETED 17a | [D-3 output location] |
| B-1 | Gauge coupling ratios $g_1/g_2(s)$, $g_1/g_3(s)$, $g_2/g_3(s)$ | COMPLETED 17a | [B-1 output location] |
| B-4 | Z₃ triality table for 28 irreps | COMPLETED 17a | [B-4 output location] |
| H-1 | V_eff(s) across 40 parameter combos | COMPLETED 17a | [H-1 output location] |

**NOTE**: Replace `[output location]` with actual file paths before launching this session. These are the 17a deliverables.

---

# IV. CALCULATION ASSIGNMENTS

## Baptista-Spacetime-Analyst: 2 Assignments

### Assignment B-2: Cross-Verification of SP Geometry (Priority: HIGH — Quality Control)

**YOUR TASK**: Verify SP-Geometer's 17a outputs against Baptista's papers:

1. **Verify SP-1's explicit $g_{ab}$** reproduces eq 3.68 exactly. Check:
   - The Cartan decomposition: $\mathfrak{su}(3) = \mathfrak{u}(1) \oplus \mathfrak{su}(2) \oplus \mathbb{C}^2$
   - Scale factors: $e^{2s}$ on $\mathfrak{u}(1)$, $e^{-2s}$ on $\mathfrak{su}(2)$, $e^{s}$ on $\mathbb{C}^2$
   - Structure constants match Paper 15 conventions
   - Volume preservation: $\det(g_s)/\det(g_0) = 1$ (analytic, not just numerical)

2. **Verify SP-4's $R(s)$** matches Baptista eq 3.70:
$$\frac{R(s)}{R(0)} = \frac{2e^{2s} - 1 + 8e^{-s} - e^{-4s}}{8}$$
   where the bracket evaluates to $8$ at $s=0$ (tautological check). Compute at $s = \{0, 0.15, 0.30, 0.50, 1.0, 1.14, 2.0\}$ and compare to `tier1_spectral_action.py` values. Agreement must be $< 10^{-14}$.

3. **Verify SP-4's $V_{\text{tree}}(s)$** matches eq 3.80: $V_{\text{tree}} = -R(s) \cdot \text{Vol}(g_s)$

4. **Check all sign conventions**: Baptista uses signature $(+,+,\ldots,+)$ on SU(3). Confirm SP-Geometer used the same.

**DELIVERABLE**: Equation-by-equation comparison report. For each check: PASS (agreement to stated precision) or FAIL (discrepancy with exact values). Any FAIL flagged immediately via SendMessage to SP-Geometer.

### Assignment B-3: D_K Correctness Audit for Pfaffian (Priority: HIGH — Pfaffian prerequisite)

The Pfaffian computation (Session 17c, Assignment D-2) is the ONLY Level 4 test in the entire program. It MUST use the correct Dirac operator. You must sign off before Dirac proceeds.

**YOUR TASK**: Verify the D_K in `tier1_dirac_spectrum.py`:

1. **Corollary 3.4 (Paper 17)**: Does the code implement
$$D_K = \sum_a e_a \cdot \nabla^S_{e_a}$$
   where $\{e_a\}$ is an orthonormal frame for $(SU(3), g_s)$ and $\nabla^S$ is the spin connection?

2. **Connection coefficients**: Confirm $\Gamma^b_{ac}(s)$ in the spin connection $\Omega(s)$ match the Koszul formula:
$$g(\nabla_{e_a} e_b, e_c) = \frac{1}{2}\big(f_{abc} \cdot \sigma_a(s) + f_{bca} \cdot \sigma_b(s) - f_{cab} \cdot \sigma_c(s)\big)$$
   where $\sigma_a(s)$ are the scale factors from the Jensen deformation.

3. **Killing isometry**: Verify $[D_K, R_{\mathfrak{su}(3)}] = 0$. This means $D_K$ commutes with the regular representation of SU(3). Check numerically at $s = 0, 0.5, 1.0$.

4. **Lichnerowicz theorem (Paper 17, Proposition 1.1)**: Confirm $D_K$ anticommutes with $\Gamma_K$:
$$\{D_K, \Gamma_K\} = 0$$
   Check numerically at $s = 0, 0.5, 1.0$.

**DELIVERABLE**: Pass/fail on each of the 4 checks with explicit numerical evidence ($\|[\cdot,\cdot]\|$ or $\|\{\cdot,\cdot\}\|$ values). If ALL 4 pass: **Pfaffian computation is CLEARED for Session 17c.** If ANY fail: **Pfaffian INVALIDATED until fixed.**

---

## Schwarzschild-Penrose-Geometer: 1 Assignment

### Assignment SP-2: Curvature Invariants as Functions of s (Priority: HIGH)

Using the explicit metric from your SP-1 (Session 17a) or the structure-constant machinery in the code:

**COMPUTE**:
1. Scalar curvature $R(s)$ — already done. VERIFY independently against Baptista eq 3.70.
2. Ricci tensor squared: $R_{ab}\, R^{ab}(s)$
3. Kretschner scalar: $K(s) = R_{abcd}\, R^{abcd}(s)$
4. Weyl tensor squared: $C_{abcd}\, C^{abcd}(s)$

For a left-invariant metric on SU(3), these can all be computed from the structure constants and scale factors WITHOUT coordinates (using the Milnor frame formulas for homogeneous spaces). This is a FINITE computation — no integrals, no PDEs.

**DELIVERABLE**: Four functions of $s$, computed at 50+ $s$-values in $[0,\, 2.5]$. For each:
- Exact analytic expression (rational function of exponentials)
- Numerical values at 50+ points
- Plots

**Classification questions** (answer with numbers):
- Is $g_s$ ever singular? At what $s$ (if any) does $K(s)$ diverge?
- Is $g_0$ (bi-invariant) conformally flat? ($C_{abcd}C^{abcd}(0) = 0$?)
- Does the Weyl tensor have special structure at any $s$?

**WHY THIS MATTERS**: These are NUMBERS FROM GEOMETRY. If $K(s)$ diverges at finite $s$, that constrains the physical range of the Jensen parameter. If the Weyl tensor vanishes at some $s_{\text{special}}$, that is a geometric prediction.

---

# V. COORDINATION

This phase has a simple sequential dependency:

```
  SP-1 (from 17a) ─→ B-2 (Baptista verifies metric) ─→ SP-2 (curvature using verified metric)
  SP-4 (from 17a) ─→ B-2 (Baptista verifies V_tree)
  tier1_dirac_spectrum.py ─→ B-3 (Baptista audits D_K) ─→ [GATES Session 17c D-2 Pfaffian]
```

**Interaction rules**:
- Baptista checks SP-1 and SP-4 FIRST (B-2), then audits D_K (B-3)
- If B-2 finds discrepancies: message SP-Geometer immediately. SP fixes before proceeding to SP-2.
- If B-2 passes: SP-Geometer proceeds to SP-2 using the verified metric.
- B-3 result is a GATE: pass → Pfaffian cleared. Fail → Pfaffian blocked.

---

# VI. SUCCESS CRITERIA

### Baptista-Spacetime-Analyst
- [ ] B-2: Verification report — 4 checks (metric, R(s), V_tree, conventions), each PASS or FAIL with numerical evidence
- [ ] B-3: D_K audit — 4 checks (Cor 3.4, connection, Killing, Lichnerowicz), each PASS or FAIL. **Final verdict: Pfaffian CLEARED or BLOCKED.**

### Schwarzschild-Penrose-Geometer
- [ ] SP-2: Four curvature invariants ($R$, $R_{ab}R^{ab}$, $K$, $C_{abcd}C^{abcd}$) at 50+ $s$-values with analytic expressions and plots

That is **3 deliverables** from **2 agents**. The critical output is Baptista's B-3 verdict — it gates the Level 4 Pfaffian test.

---

# VII. INFRASTRUCTURE

Same scripts as Session 17a:
| Script | Lines | Who Needs It |
|:-------|:-----:|:-------------|
| `tier1_dirac_spectrum.py` | ~1580 | B-3 (D_K audit) |
| `tier1_spectral_action.py` | ~900 | B-2 (R(s) cross-check), SP-2 (curvature) |
| `branching_computation_32dim.py` | ~1200 | B-3 (Killing isometry check, representation matrices) |

---

*"One wrong sign in the metric propagates to everything downstream." — Session 17 Prompt*
*"The geometry determines the physics." — Baptista*
