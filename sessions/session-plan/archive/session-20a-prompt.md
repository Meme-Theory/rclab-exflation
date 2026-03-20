# Session 20a: Seeley-DeWitt Fast Gate + Riemann Tensor Infrastructure

## Session Type: Computation from Existing Data + New Infrastructure (1 DAY)
## Agents: connes-ncg-theorist + phonon-exflation-sim
## Session Goal: (1) Compute da_2/dtau and da_4/dtau from existing curvature data — the cheapest possible gate for spectral action stabilization. (2) Build the full Riemann tensor R_{abcd}(tau), the prerequisite for Session 20b's Lichnerowicz computation.

---

# I. CONTEXT

Session 19d delivered a clean CLOSED on Casimir energy for scalar+vector modes (R = 9.92:1 constant, both pre-registered criteria fired). But sim's self-audit discovered the **27-dimensional TT 2-tensor fiber** omitted from all computations since Session 18. With TT modes: F/B flips from 8.36:1 to **0.44:1** (boson-dominated). The Lichnerowicz operator on TT 2-tensors couples to the **full Riemann tensor** R_{acbd} — qualitatively different tau-dependence from all previously computed spectra.

**Two parallel tracks emerged from the 14-agent Session 19d review:**

- **Track A (this session)**: The Seeley-DeWitt shortcut. The NCG spectral action V_eff = 2f_2 Lambda^2 a_2(tau) + f_0 a_4(tau) has a minimum when da_2/dtau and da_4/dtau have opposite signs. Since a_0 is tau-independent (volume preservation), the Lambda^4 term drops out. Computable from existing curvature data **in hours**.

- **Track B (Session 20b)**: Full Lichnerowicz eigenvalue sweep on TT 2-tensors. Requires R_{abcd}(tau) as input — built here.

**Why these agents**: connes-ncg-theorist proposed the Seeley-DeWitt shortcut (Session 19d collaboration) and understands the NCG interpretation of a_2, a_4. phonon-exflation-sim owns the curvature infrastructure (`b6_scalar_vector_laplacian.py`, `sp2_final_verification.py`) and builds R_{abcd}(tau) for 20b.

**Dependencies**: Independent of 20b and 20c. Uses existing data from Sessions 17b and 18.

---

# II. REQUIRED READING

## For connes-ncg-theorist:

1. **Session 19d Connes collaboration**: `sessions/session-19/session-19d-connes-collab.md` — Your Seeley-DeWitt shortcut proposal (da_2/dtau vs da_4/dtau). You designed this.

2. **Connes Paper 07**: `researchers/Connes/07_1996_Connes_Chamseddine_spectral_action_principle.md` — The spectral action and Seeley-DeWitt expansion.

3. **Session 17b SP-2 curvature**: `tier0-computation/sp2_final_verification.py` — 4 curvature invariants as exact analytic functions. R_K(tau), |Ric|^2(tau), Kretschner scalar, Weyl tensor.

4. **Your agent memory**: `.claude/agent-memory/connes-ncg-theorist/`

## For phonon-exflation-sim:

5. **`tier0-computation/b6_scalar_vector_laplacian.py`** — Contains `compute_connection_ON()` and `ricci_tensor_ON()`. You are extending these to produce the full R_{abcd}.

6. **`tier0-computation/tier1_dirac_spectrum.py`** — `jensen_metric()`, Gell-Mann structure constants. The Lie algebra infrastructure.

7. **Session 19d synthesis**: `sessions/session-19/session-19d-synthesis.md` — Section IV (why R_{abcd} is the key differentiator).

8. **Your agent memory**: `.claude/agent-memory/phonon-exflation-sim/`

## Key Equations

**Seeley-DeWitt expansion (NCG spectral action):**
```
V_eff(tau) = 2 f_4 Lambda^4 a_0(tau) + 2 f_2 Lambda^2 a_2(tau) + f_0 a_4(tau) + O(Lambda^{-2})

a_0(tau) = (4pi)^{-4} Vol(K)                    [tau-INDEPENDENT, volume-preserving]
a_2(tau) = (4pi)^{-4} (1/6) integral R_K(tau) dvol
a_4(tau) = (4pi)^{-4} (1/360) integral [5R_K^2 - 2|Ric|^2 + 2|Riem|^2](tau) dvol
```

**Minimum condition:**
```
dV_eff/dtau = 2 f_2 Lambda^2 (da_2/dtau) + f_0 (da_4/dtau) = 0
=> da_2/dtau and da_4/dtau must have OPPOSITE SIGNS at some tau
```

**Riemann tensor on Lie group (Milnor 1976, Baptista Paper 15 eqs 3.14-3.19):**
```
R_{abcd} = -(1/4) f_{abe} f^e_{cd}    [bi-invariant, tau=0]
```
Jensen deformation introduces anisotropic corrections through the metric components e^{2tau}, e^{-2tau}, e^{tau}.

---

# III. CALCULATION ASSIGNMENTS

## Agent Allocation

| Assignment | Primary | Secondary | Rationale |
|:-----------|:--------|:----------|:----------|
| SD-1: Seeley-DeWitt sign check | connes | phonon-sim (curvature data) | NCG expertise for a_2, a_4 interpretation |
| R-1: Full Riemann tensor | phonon-sim | connes (validation) | Extension of existing infrastructure |

**Workflow**: SD-1 and R-1 run in PARALLEL. SD-1 uses existing curvature invariants. R-1 builds new infrastructure for 20b.

---

### Assignment SD-1: Seeley-DeWitt Fast Gate (HOURS)

**Agent**: connes-ncg-theorist

#### Computation Steps

1. **Compute a_2(tau)**: a_2 = (1/6) R_K(tau) (on unit-volume SU(3)). From Session 17b SP-2:
   ```
   R_K(tau) is an exact analytic function of tau (given in sp2_final_verification.py)
   ```
   Compute da_2/dtau analytically. **Expected: da_2/dtau > 0 for tau > 0** (scalar curvature increases with deformation).

2. **Compute a_4(tau)**: Requires |Riem|^2(tau) = R_{abcd} R^{abcd} — the Kretschner scalar. From Session 17b SP-2, |Ric|^2 and R_K^2 are already computed analytically. The Kretschner scalar may also be available. If not, coordinate with phonon-sim's R-1 output.

3. **Compute da_4/dtau**: Numerical differentiation across tau grid [0, 2.0].

4. **Sign check**: At each tau, record sign(da_2/dtau) and sign(da_4/dtau). If opposite at any tau, the spectral action has a minimum for appropriate f_2/f_0 ratio.

5. **If opposite signs exist**: Find the tau range where the balance holds. Compute the required f_2/f_0 ratio. Is it natural (O(1)) or fine-tuned (>>1 or <<1)?

#### Closure / Confirm

- **OPEN**: da_2/dtau and da_4/dtau have opposite signs at some tau in [0, 2.0]. NCG spectral action path to stabilization is viable with appropriate cutoff function.
- **CLOSED**: Same sign everywhere. NCG spectral action cannot produce a minimum for ANY cutoff function. Only the numerical Lichnerowicz path (20b) remains.

#### Deliverable
- Table: a_2(tau), a_4(tau), da_2/dtau, da_4/dtau at 21 tau-values
- Plot: da_2/dtau and da_4/dtau vs tau (sign comparison)
- VERDICT: NCG path OPEN or CLOSED
- If OPEN: tau range and required f_2/f_0 ratio

**Write to**: `tier0-computation/sd20a_seeley_dewitt_gate.py`

---

### Assignment R-1: Full Riemann Tensor R_{abcd}(tau) (PREREQUISITE for 20b)

**Agent**: phonon-exflation-sim

#### Background

Session 20b needs R_{abcd}(tau) for the Lichnerowicz operator. The infrastructure for connection coefficients and Ricci tensor already exists in `b6_scalar_vector_laplacian.py`. The task is to extend it to the full 4-index Riemann tensor.

#### Computation Steps

1. Load Gell-Mann structure constants f^c_{ab} (already in `tier1_dirac_spectrum.py`).

2. For each tau in [0, 0.1, ..., 2.0]:
   - Jensen metric g_{ab}(tau) from `jensen_metric(tau)` — 8x8 diagonal
   - Connection coefficients Gamma^c_{ab}(tau) from Koszul formula — shape (8,8,8)
   - Riemann tensor R^d_{abc}(tau) — shape (8,8,8,8)
   - Lowered R_{abcd}(tau) — shape (8,8,8,8)

3. **Validation at tau=0**: Verify R_{abcd}|_{tau=0} = -(1/4) f_{abe} f^e_{cd}.

4. **Cross-check**: R_{ab} = R^c_{acb} must match `ricci_tensor_ON()`. R_K = g^{ab} R_{ab} must match SP-2.

5. **Compute |Riem|^2(tau)**: Feed to SD-1 for the Kretschner scalar in a_4.

6. **Save**: R_{abcd}(tau) at all 21 tau-values to `r20a_riemann_tensor.npz`.

#### Deliverable
- Function `compute_riemann_tensor_ON(s)` returning 8x8x8x8 array
- Validation: Ricci contraction matches existing, R_K matches SP-2
- |Riem|^2(tau) for SD-1
- Data file: `r20a_riemann_tensor.npz`

**Write to**: `tier0-computation/r20a_riemann_tensor.py`

---

# IV. DECISION GATE

| Result | Interpretation | Impact on 20b |
|:-------|:--------------|:-------------|
| SD-1 OPEN + R-1 validated | Both NCG and numerical paths viable | 20b proceeds with validated R_{abcd}. Two independent paths to tau_0. |
| SD-1 CLOSED + R-1 validated | NCG path closed, numerical required | 20b is sole path. Higher stakes. |
| SD-1 OPEN + R-1 fails validation | NCG path suggestive but infrastructure broken | Debug R_{abcd} before 20b. |

---

# V. SUCCESS CRITERIA

- [ ] SD-1: da_2/dtau and da_4/dtau computed + sign comparison + OPEN/CLOSED verdict
- [ ] R-1: R_{abcd}(tau) at 21 tau-values + validated against Ricci + |Riem|^2 for SD-1
- [ ] R_{abcd} data saved for Session 20b consumption

**2 deliverables from 2 agents in 1 day.** Both run in parallel.

All scripts in `tier0-computation/`. Environment: `phonon-exflation-sim/.venv312/Scripts/python.exe`.

---

# VI. WHAT THIS SESSION DOES NOT COVER

| Item | Session | Status |
|:-----|:--------|:-------|
| Lichnerowicz eigenvalue sweep on TT 2-tensors | 20b | Consumes R-1 output from this session |
| V_total minimum search | 20b | After Lichnerowicz eigenvalues |
| Synthesis + hanging task triage | 20c | After 20a + 20b results |
| D_total Pfaffian | 21+ | Needs 19c eigenvectors |
| Spectral back-reaction simulation | 21+ | Needs eigenvectors + coupling matrix |

---

# VII. RELATION TO SESSION 20b

**If SD-1 finds OPEN**: Session 20b has TWO independent paths to tau_0 — the NCG analytic path (f_2/f_0 ratio) and the numerical Casimir path. If both converge on the same tau_0, that's a strong cross-validation.

**If SD-1 finds CLOSED**: Session 20b carries the full weight. The Lichnerowicz eigenvalues become the sole remaining perturbative stabilization mechanism.

**Either way**: R-1's Riemann tensor data is consumed by 20b. This session is a prerequisite.

---

*"The cleanest NCG path to stabilization is through the Seeley-DeWitt coefficients a_2(tau) and a_4(tau), computable analytically from existing curvature data in hours."* — Connes (Session 19d)

*"The Riemann tensor is highly anisotropic under Jensen deformation: u(1) x u(1) sectional curvatures scale as e^{4s}, su(2) x su(2) as e^{-4s}."* — Baptista (Session 19d)
